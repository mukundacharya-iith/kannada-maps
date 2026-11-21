TEMPLATE_VERSION = "v1"
CONDITIONS = ["baseline", "gold_explanation", "self_explanation"]

BASELINE = (
    "Question: What does the person mean by the proverb?\n"
    "Proverb: {proverb}\n"
    "Context: {conversation}\n"
    "Choices: A: {answer1} B: {answer2}\n"
    "Answer:"
)

WITH_EXPLANATION = (
    "Question: What does the person mean by the proverb?\n"
    "Proverb: {proverb}\n"
    "Explanation: {explanation}\n"
    "Context: {conversation}\n"
    "Choices: A: {answer1} B: {answer2}\n"
    "Answer:"
)

EXPLAIN_PROMPT = (
    "Explain the meaning of the proverb in one short sentence.\n"
    "Proverb: {proverb}\n"
    "Explanation:"
)


def build_prompt(row, condition, explanation=None):
    """Return the scoring prompt for one row.

    `explanation` is only used by self_explanation (the model's own text).
    For gold_explanation the row's own `explanation` field is used.
    """
    if condition == "baseline":
        return BASELINE.format(**row)
    if condition == "gold_explanation":
        return WITH_EXPLANATION.format(**row)
    if condition == "self_explanation":
        if explanation is None:
            raise ValueError("self_explanation needs the model-generated explanation")
        return WITH_EXPLANATION.format(**{**row, "explanation": explanation})
    raise ValueError(f"Unknown condition {condition!r}. Use one of {CONDITIONS}")


def build_explain_prompt(row):
    return EXPLAIN_PROMPT.format(proverb=row["proverb"])