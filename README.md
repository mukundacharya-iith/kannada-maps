# Kannada Proverbs in Conversation

Do small multilingual language models understand Kannada proverbs used in
conversation? This project follows **MAPS** (Liu et al., NAACL 2024, "Are
Multilingual LLMs Culturally-Diverse Reasoners? An Investigation into
Multicultural Proverbs and Sayings") and extends it with:

1. **A Kannada dataset in MAPS format.** MAPS does not cover Kannada. The dataset
   has 326 items (21 few-shot, 305 test), with an English version of the test set.
2. **An explanation experiment.** Does the model do better when given the
   proverb's meaning (`gold_explanation`), or when it first writes its own
   (`self_explanation`)?
3. **Swap-debiased scoring.** Each item is also scored with the two answers
   swapped, which cancels the models' preference for one answer letter.
4. **A Bengali comparison.** mT0-large is re-run on MAPS Bengali with the same code.

**Task:** given a short conversation that uses a proverb, pick the intended
meaning from two candidates (A or B). Zero-shot, as in the paper.

## Results

Accuracy (%) on the 305 Kannada test items, swap-debiased. Chance is 50%.

| Model            | Kannada        | English | Kannada + gold explanation | Kannada + self-explanation |
| ---------------- | -------------- | ------- | -------------------------- | -------------------------- |
| mT0-large (1.2B) | 59.3           | 65.2    | 92.5                       | 57.7                       |
| Qwen3.5-2B       | 79.0           | 94.4    | 96.1                       | 78.0                       |
| Sarvam-1 (~2.5B) | **87.9** | 83.9    | **98.7**             | 85.2                       |

- **The Indian-language model is best on Kannada.** Only the general model
  (Qwen) is held back by the language.
- **The gap is missing knowledge, not reasoning.** Given the proverb's meaning,
  every model reaches 92–99%. Their own explanations do not help: they mostly
  copy the proverb, switch to another script (mT0 often writes Telugu), or give
  a wrong meaning.
- **Letter bias matters.** Under raw scoring, mT0-large picked "A" for 275 of 305
  items (54.8% raw vs 59.3% debiased).
- **Bengali comparison.** On MAPS Bengali, mT0-large scores 57.9%, close to its
  Kannada score.

Full numbers, with 95% confidence intervals and figurative/literal splits, are
in `results/summary.md`. The write-up is in `reports/`.

## Data

**The data is not included in this repository.** As with MAPS, access is
restricted, to keep the test set out of web-crawled LLM training data.

- **Kannada dataset:** on Google Drive, accessible to IITH accounts: `[dataset Drive URL]`
- **MAPS data (Bengali and the other languages):** shared by the authors through
  a request form, see https://github.com/UKPLab/maps

Place the files as follows (paths are set in `configs/datasets.json`):

```
data/kn/fs_proverbs.xlsx               21 few-shot items (dev/sanity checks only)
data/kn/test_proverbs.xlsx             305 test items, Kannada
data/kn/machine_translation_2en.xlsx   the same 305 items in English
data/bn/test_proverbs.xlsx             MAPS Bengali test set (340 items)
```

Each file has the MAPS columns: `proverb`, `conversation`, `explanation`,
`answer1`, `answer2`, `is_figurative` (1/0), `answer_key` (a/b).

**How the Kannada data was made:**

- Some items were written by hand and some drafted with an LLM. Every item was
  reviewed and corrected by native Kannada speakers.
- The split is stratified on figurative label × answer position (seed 42), and
  no proverb appears in both splits. The test set is 79% figurative (242/63) and
  has 155 A / 150 B answers.
- The English test set was machine-translated with Google Translate. Review
  flagged 84 rows, which were corrected by hand.
- Checks before the experiments fixed four data problems: a stray Urdu word,
  stray line breaks, a proverb that did not match its conversation, and a
  duplicate.

## Setup

```bash
pip install -r requirements.txt
python -m src.data        # checks that every dataset loads and is valid
```

The runs used `transformers==5.5.4`. mT0-large runs on a laptop CPU (float32).
Qwen3.5-2B and Sarvam-1 were run on a free Google Colab T4 GPU (float32).

## Running the experiments

All commands run from the repo root.

```bash
# 1. pipeline check: dummy model, no GPU or downloads (about 50% accuracy)
python -m src.run_experiment --model random --datasets kannada_test --conditions baseline

# 2. a real model, all three conditions, Kannada and English
python -m src.run_experiment --model mt0-large \
    --datasets kannada_test kannada_en_reviewed \
    --conditions baseline gold_explanation self_explanation

# 3. Bengali reference (baseline only)
python -m src.run_experiment --model mt0-large --datasets bengali_test --conditions baseline

# 4. summary table of everything in results/
python -m src.analysis
```

**On Colab:** upload the project folder to Google Drive and open
`notebooks/run_colab.ipynb` (Qwen3.5-2B) or `notebooks/run_colab_sarvam.ipynb`
(Sarvam-1). Choose a T4 GPU runtime and run the cells in order.

Runs are resumable: finished result files are skipped unless you pass
`--overwrite`. Models are listed in `configs/models.json` and datasets in
`configs/datasets.json`; add entries there to try more.

## Method

**Prompts.** English instructions for every language, as in MAPS. No chat
template; the same raw text for every model.

```
Question: What does the person mean by the proverb?
Proverb: {proverb}
Context: {conversation}
Choices: A: {answer1} B: {answer2}
Answer:
```

- `gold_explanation` adds `Explanation: {explanation}` after the proverb line,
  using the dataset's explanation.
- `self_explanation` first asks the model "Explain the meaning of the proverb in
  one short sentence." (up to 60 tokens, greedy, first non-empty line). It then
  uses that sentence in the same position.

**Scoring.** The model's logits for the next token after `Answer:` are compared
for "A" and "B" (letter variants with and without a leading space are combined).
Nothing is generated, so no answer is invalid. This is the MAPS method (raw
scoring).

**Swap-debiasing.** Each item is scored a second time with `answer1` and
`answer2` swapped:

```
m = (s_A - s_B) + (s'_B - s'_A)        choose answer1 if m > 0, else answer2
```

A constant preference for one letter cancels out; a real preference for one
meaning does not. Results files hold both: `correct` (raw) and `correct_swap`
(debiased).

**Qwen3.5 note.** Qwen starts generations with a `<think>` tag. These tokens are
blocked during generation and cleaned afterwards (`src/models.py`). Without this,
133 of 305 self-explanations were just `<think>`.

## Repository layout

| Path                      | Contents                                                                        |
| ------------------------- | ------------------------------------------------------------------------------- |
| `src/data.py`           | loads the xlsx files and checks columns and labels                              |
| `src/prompts.py`        | the three prompt conditions                                                     |
| `src/models.py`         | model wrappers (causal, seq2seq, random) and A/B scoring                        |
| `src/run_experiment.py` | runs model × dataset × condition; writes `results/*.csv` and `.meta.json` |
| `src/analysis.py`       | accuracy with 95% bootstrap CI, figurative/literal split, summary tables        |
| `configs/`              | dataset and model registries                                                    |
| `notebooks/`            | Colab notebooks for Qwen3.5-2B and Sarvam-1                                     |
| `results/`              | one CSV per run (per-item predictions), run settings,`summary.md`             |
| `reports/`              | final report (PDF)                                                              |

## Limitations

- Only small models (1.2–2.5B), of different types: mT0 is instruction-tuned,
  Qwen post-trained, Sarvam-1 a base model.
- 305 test items give confidence intervals of about ±5 points. There are only 63
  literal items (about ±10 points).
- The gold explanation partly gives the answer away: picking the answer with more
  word overlap with it already gets 91%. Treat gold accuracy as an upper bound.
- The English version is a reviewed machine translation, not a cultural adaptation.

## References

- Chen Cecilia Liu, Fajri Koto, Timothy Baldwin, Iryna Gurevych. 2024. A
  Multilingual LLMs Culturally-Diverse Reasoners? An Investigation into
  Multicultural Proverbs and Sayings. NAACL 2024.
  [arXiv:2309.08591](https://arxiv.org/abs/2309.08591) ·
  [github.com/UKPLab/maps](https://github.com/UKPLab/maps). The MAPS code has no
  stated license, so nothing here is copied from it.
- Muennighoff et al. 2023. Crosslingual Generalization through Multitask
  Finetuning (BLOOMZ and mT0). ACL 2023.
  [bigscience/mt0-large](https://huggingface.co/bigscience/mt0-large)
- Qwen Team. 2026. Qwen3.5. [Qwen/Qwen3.5-2B](https://huggingface.co/Qwen/Qwen3.5-2B)
- Sarvam AI. 2024. Sarvam-1. [sarvamai/sarvam-1](https://huggingface.co/sarvamai/sarvam-1)
  (non-commercial license)
