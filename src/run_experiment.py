"""Run one model on one or more datasets and conditions.

Examples (run from the repo root):

    # pipeline check with the dummy model, no GPU or downloads needed
    python -m src.run_experiment --model random --datasets kannada_test --conditions baseline

    # a real run
    python -m src.run_experiment --model mt0-base \
        --datasets kannada_test kannada_en_reviewed bengali_test \
        --conditions baseline gold_explanation self_explanation

Each (model, dataset, condition) writes
    results/<model>__<dataset>__<condition>.csv        one row per item
    results/<model>__<dataset>__<condition>.meta.json  settings used for the run
Existing result files are skipped unless --overwrite is given, so an interrupted
run (for example a free Colab session that disconnects) can simply be restarted.
"""
import argparse
import csv
import datetime as dt
import json
import sys
from pathlib import Path

from src import prompts
from src.data import get_dataset, load_registry
from src.models import load_model, load_model_registry

ROOT = Path(__file__).resolve().parents[1]
FIELDS = [
    "model", "dataset", "condition", "row_id", "is_figurative", "answer_key",
    "pred", "correct", "score_A", "score_B",
    "score_A_swap", "score_B_swap", "pred_swap", "correct_swap",
    "explanation_used", "proverb",
]


def _explanations_for(model, model_name, dataset_name, rows, results_dir, overwrite):
    """Generate (or load cached) model-written explanations for self_explanation."""
    cache_dir = results_dir / "cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = cache_dir / f"explanations__{model_name}__{dataset_name}.json"
    if path.exists() and not overwrite:
        with open(path, encoding="utf-8") as f:
            cached = json.load(f)
        if len(cached) == len(rows):
            return {int(k): v for k, v in cached.items()}
    out = {}
    for i, row in enumerate(rows, 1):
        out[row["row_id"]] = model.generate(prompts.build_explain_prompt(row))
        if i % 25 == 0:
            print(f"    generated {i}/{len(rows)} explanations", flush=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return out


def run_one(model, model_name, spec, dataset_name, rows, condition, results_dir, seed, overwrite):
    stem = f"{model_name}__{dataset_name}__{condition}"
    csv_path = results_dir / f"{stem}.csv"
    if csv_path.exists() and not overwrite:
        print(f"  skip {stem} (exists)")
        return

    gen = None
    if condition == "self_explanation":
        print("  generating explanations ...", flush=True)
        gen = _explanations_for(model, model_name, dataset_name, rows, results_dir, overwrite)

    out_rows = []
    for i, row in enumerate(rows, 1):
        expl = gen[row["row_id"]] if gen else None
        prompt = prompts.build_prompt(row, condition, explanation=expl)
        a, b = model.score_ab(prompt)
        pred = "A" if a > b else "B"

        # Swap check: show the same item again with the two answers swapped
        # (answer1 now appears as B, answer2 as A). A model that just likes the
        # letter "A" gets pushed both ways and cancels out; real preference for
        # one answer adds up. margin > 0 means answer1 (the original "A") wins.
        swapped_row = {**row, "answer1": row["answer2"], "answer2": row["answer1"]}
        a2, b2 = model.score_ab(prompts.build_prompt(swapped_row, condition, explanation=expl))
        margin = (a - b) + (b2 - a2)
        pred_swap = "A" if margin > 0 else "B"

        out_rows.append({
            "model": model_name, "dataset": dataset_name, "condition": condition,
            "row_id": row["row_id"], "is_figurative": row["is_figurative"],
            "answer_key": row["answer_key"], "pred": pred,
            "correct": int(pred == row["answer_key"]),
            "score_A": round(a, 6), "score_B": round(b, 6),
            "score_A_swap": round(a2, 6), "score_B_swap": round(b2, 6),
            "pred_swap": pred_swap, "correct_swap": int(pred_swap == row["answer_key"]),
            "explanation_used": (expl if expl is not None
                                 else row["explanation"] if condition == "gold_explanation" else ""),
            "proverb": row["proverb"],
        })
        if i % 100 == 0:
            print(f"    scored {i}/{len(rows)}", flush=True)

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(out_rows)

    acc = sum(r["correct"] for r in out_rows) / len(out_rows)
    acc_swap = sum(r["correct_swap"] for r in out_rows) / len(out_rows)
    n_pred_a = sum(r["pred"] == "A" for r in out_rows)
    meta = {
        "model": model_name, "hf_id": spec.get("hf_id"), "model_type": spec["type"],
        "dataset": dataset_name, "condition": condition, "n": len(out_rows),
        "accuracy": round(acc, 4), "accuracy_swap": round(acc_swap, 4),
        "raw_pred_A": n_pred_a, "template_version": prompts.TEMPLATE_VERSION,
        "seed": seed, "date_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "python": sys.version.split()[0],
    }
    try:
        import torch, transformers
        meta["torch"] = torch.__version__
        meta["transformers"] = transformers.__version__
    except Exception:
        pass
    with open(results_dir / f"{stem}.meta.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=1)
    print(f"  done {stem}: accuracy raw {acc:.3f}, swap-debiased {acc_swap:.3f} "
          f"(n={len(out_rows)}; raw predicted A for {n_pred_a})")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True, help="name in configs/models.json")
    ap.add_argument("--datasets", nargs="+", required=True, help="names in configs/datasets.json")
    ap.add_argument("--conditions", nargs="+", default=["baseline"], choices=prompts.CONDITIONS)
    ap.add_argument("--out", default="results")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()

    results_dir = Path(args.out)
    if not results_dir.is_absolute():
        results_dir = ROOT / results_dir
    results_dir.mkdir(parents=True, exist_ok=True)

    d_reg = load_registry()
    model, spec = load_model(args.model, load_model_registry(), seed=args.seed)
    for ds in args.datasets:
        rows = get_dataset(ds, d_reg)
        print(f"{args.model} on {ds} ({len(rows)} rows)")
        for cond in args.conditions:
            run_one(model, args.model, spec, ds, rows, cond, results_dir, args.seed, args.overwrite)


if __name__ == "__main__":
    main()