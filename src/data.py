import json
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "proverb", "conversation", "explanation",
    "answer1", "answer2", "is_figurative", "answer_key",
]
TEXT_FIELDS = ["proverb", "conversation", "answer1", "answer2"]


def load_registry(path=None):
    """configs/datasets.json maps a short name to {"path": ..., "sheet": ...}."""
    path = Path(path) if path else ROOT / "configs" / "datasets.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_rows(path, sheet=None):
    """Read one xlsx file and return a list of row dicts with a clean schema."""
    p = Path(path)
    if not p.is_absolute():
        p = ROOT / p
    if not p.exists():
        raise FileNotFoundError(f"Dataset file not found: {p}")

    wb = openpyxl.load_workbook(p, read_only=True, data_only=True)
    ws = wb[sheet] if sheet else wb.worksheets[0]
    it = ws.iter_rows(values_only=True)
    header = [str(h).strip() if h is not None else "" for h in next(it)]

    missing = [c for c in REQUIRED if c not in header]
    if missing:
        raise ValueError(
            f"{p.name}: missing columns {missing}. Found columns: {header}"
        )
    idx = {c: header.index(c) for c in REQUIRED}

    rows = []
    for sheet_row, r in enumerate(it, start=2):
        if r is None or all(v is None for v in r):
            continue
        key = r[idx["answer_key"]]
        if key is None or str(key).strip() == "":
            continue  # trailing blank rows
        row = {"row_id": sheet_row}
        for c in ("proverb", "conversation", "explanation", "answer1", "answer2"):
            v = r[idx[c]]
            row[c] = "" if v is None else str(v).strip()
        row["is_figurative"] = int(float(r[idx["is_figurative"]]))
        row["answer_key"] = str(key).strip().upper()
        rows.append(row)
    wb.close()
    _validate(rows, p.name)
    return rows


def _validate(rows, name):
    if not rows:
        raise ValueError(f"{name}: no data rows found")
    for r in rows:
        if r["answer_key"] not in ("A", "B"):
            raise ValueError(f"{name} row {r['row_id']}: answer_key must be a/b, got {r['answer_key']!r}")
        if r["is_figurative"] not in (0, 1):
            raise ValueError(f"{name} row {r['row_id']}: is_figurative must be 0/1")
        for f in TEXT_FIELDS:
            if not r[f]:
                raise ValueError(f"{name} row {r['row_id']}: empty {f}")


def get_dataset(name, registry=None):
    """Load a dataset by its short name from configs/datasets.json."""
    registry = registry or load_registry()
    if name not in registry:
        raise KeyError(f"Unknown dataset {name!r}. Known: {sorted(registry)}")
    spec = registry[name]
    return load_rows(spec["path"], spec.get("sheet"))


if __name__ == "__main__":
    # Quick check: python -m src.data
    reg = load_registry()
    for n in reg:
        try:
            rows = get_dataset(n, reg)
            fig = sum(r["is_figurative"] for r in rows)
            a = sum(r["answer_key"] == "A" for r in rows)
            print(f"{n:24s} rows={len(rows):4d} figurative={fig:4d} key A/B={a}/{len(rows)-a}")
        except Exception as e:  # keep going so one bad path doesn't hide the rest
            print(f"{n:24s} ERROR: {e}")