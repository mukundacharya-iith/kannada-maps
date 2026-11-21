"""Summarise everything in results/ into one table.

    python -m src.analysis

Reads results/*.csv (one file per run) and writes
    results/summary.csv   machine-readable
    results/summary.md    table to paste into your report

For every (model, dataset, condition) it reports
    - accuracy with a 95% bootstrap confidence interval
    - accuracy on figurative and on literal items (with the item counts)
    - for non-baseline conditions: the change versus baseline on the same items
      and an exact McNemar p-value (paired test; are the two conditions different?)

Accuracy on literal items is based on few items in small datasets, so read those
numbers together with the n shown next to them.
"""
import argparse
import csv
from math import comb
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]


# Two ways of scoring the same run:
#   raw  - the paper's method: compare P(A) and P(B) once
#   swap - also score the item with the answers swapped and combine both,
#          which cancels a model's preference for one letter
SCORINGS = [("raw", "correct"), ("swap", "correct_swap")]


def read_runs(results_dir, column="correct"):
    runs = {}
    for p in sorted(results_dir.glob("*__*__*.csv")):
        with open(p, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        if not rows or column not in rows[0]:
            continue  # e.g. older result files made before the swap check existed
        key = (rows[0]["model"], rows[0]["dataset"], rows[0]["condition"])
        runs[key] = {int(r["row_id"]): (int(r[column]), int(r["is_figurative"])) for r in rows}
    return runs


def bootstrap_ci(correct, n_boot=2000, seed=0):
    c = np.asarray(correct, dtype=float)
    rng = np.random.default_rng(seed)
    means = c[rng.integers(0, len(c), size=(n_boot, len(c)))].mean(axis=1)
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def mcnemar_exact(base, other):
    """Exact two-sided McNemar test on paired 0/1 correctness lists."""
    b = sum(1 for x, y in zip(base, other) if x == 1 and y == 0)  # base right, other wrong
    c = sum(1 for x, y in zip(base, other) if x == 0 and y == 1)
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    p = 2 * sum(comb(n, i) for i in range(k + 1)) / 2 ** n
    return min(1.0, p)


def summarise(runs, scoring="raw"):
    out = []
    for (model, ds, cond), rows in sorted(runs.items()):
        ids = sorted(rows)
        correct = [rows[i][0] for i in ids]
        fig = [rows[i][0] for i in ids if rows[i][1] == 1]
        lit = [rows[i][0] for i in ids if rows[i][1] == 0]
        lo, hi = bootstrap_ci(correct)
        rec = {
            "scoring": scoring,
            "model": model, "dataset": ds, "condition": cond, "n": len(ids),
            "acc": np.mean(correct), "ci_lo": lo, "ci_hi": hi,
            "acc_figurative": np.mean(fig) if fig else float("nan"), "n_figurative": len(fig),
            "acc_literal": np.mean(lit) if lit else float("nan"), "n_literal": len(lit),
            "delta_vs_baseline": float("nan"), "mcnemar_p": float("nan"),
        }
        base = runs.get((model, ds, "baseline"))
        if cond != "baseline" and base is not None and set(base) == set(rows):
            b_corr = [base[i][0] for i in ids]
            rec["delta_vs_baseline"] = rec["acc"] - float(np.mean(b_corr))
            rec["mcnemar_p"] = mcnemar_exact(b_corr, correct)
        out.append(rec)
    return out


def fmt(x, pct=True, nd=1):
    if x != x:  # NaN
        return "-"
    return f"{100 * x:.{nd}f}" if pct else f"{x:.3f}"


TITLES = {
    "raw": "Raw scoring (as in the paper)",
    "swap": "Swap-debiased scoring (answers also scored in swapped order)",
}


def write_outputs(recs, results_dir):
    cols = ["scoring", "model", "dataset", "condition", "n", "acc", "ci_lo", "ci_hi",
            "acc_figurative", "n_figurative", "acc_literal", "n_literal",
            "delta_vs_baseline", "mcnemar_p"]
    with open(results_dir / "summary.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in recs:
            w.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()})

    lines = []
    for scoring, _ in SCORINGS:
        part = [r for r in recs if r["scoring"] == scoring]
        if part:
            lines += [f"## {TITLES[scoring]}", ""] + _table(part) + [""]
    (results_dir / "summary.md").write_text("\n".join(lines), encoding="utf-8")
    return "\n".join(lines)


def _table(recs):
    lines = [
        "| model | dataset | condition | n | acc % [95% CI] | figurative % (n) | literal % (n) | change vs baseline (pts) | McNemar p |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for r in recs:
        delta = "-" if r["delta_vs_baseline"] != r["delta_vs_baseline"] else f"{100 * r['delta_vs_baseline']:+.1f}"
        p = "-" if r["mcnemar_p"] != r["mcnemar_p"] else f"{r['mcnemar_p']:.3f}"
        lines.append(
            f"| {r['model']} | {r['dataset']} | {r['condition']} | {r['n']} | "
            f"{fmt(r['acc'])} [{fmt(r['ci_lo'])}, {fmt(r['ci_hi'])}] | "
            f"{fmt(r['acc_figurative'])} ({r['n_figurative']}) | "
            f"{fmt(r['acc_literal'])} ({r['n_literal']}) | {delta} | {p} |"
        )
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", default="results")
    args = ap.parse_args()
    rd = Path(args.results)
    if not rd.is_absolute():
        rd = ROOT / rd
    recs = []
    for scoring, column in SCORINGS:
        recs += summarise(read_runs(rd, column), scoring)
    if not recs:
        raise SystemExit(f"No result files found in {rd}")
    print(write_outputs(recs, rd))


if __name__ == "__main__":
    main()