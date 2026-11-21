"""Model wrappers.

Every wrapper offers two methods:

    score_ab(prompt)  -> (score_A, score_B)   higher score = model prefers it
    generate(prompt, max_new_tokens) -> str   greedy text, used for self_explanation

Backends (set "type" in configs/models.json):
    causal    - decoder-only models (BLOOMZ, Qwen, Gemma, LLaMA ...)
    seq2seq   - encoder-decoder models (mT0)
    random    - dummy model for testing the pipeline; also a chance baseline

torch / transformers are imported only when a real model is loaded, so the rest
of the repo (data loading, analysis, dry runs) works without them.
"""
import hashlib
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_model_registry(path=None):
    path = Path(path) if path else ROOT / "configs" / "models.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# --------------------------------------------------------------------------
# Dummy model (pipeline tests + chance baseline)
# --------------------------------------------------------------------------
class RandomModel:
    """Scores are pseudo-random but deterministic for a given prompt."""

    def __init__(self, seed=0):
        self.seed = seed

    def _rng(self, prompt):
        h = hashlib.sha256(f"{self.seed}|{prompt}".encode("utf-8")).hexdigest()
        return random.Random(h)

    def score_ab(self, prompt):
        r = self._rng(prompt)
        return r.random(), r.random()

    def generate(self, prompt, max_new_tokens=60):
        return "dummy explanation"


# --------------------------------------------------------------------------
# Hugging Face models
# --------------------------------------------------------------------------
THINK_TAGS = ("<think>", "</think>")


def _think_token_ids(tok):
    """Ids of Qwen-style <think>/</think> tokens, if this tokenizer has them.

    Qwen3.5 starts its output with <think> even for a plain prompt. Since we keep
    only the first line of the generated text, the "explanation" was then just
    "<think>". Blocking these tokens makes the model answer directly.
    """
    vocab = tok.get_vocab()
    return [vocab[t] for t in THINK_TAGS if t in vocab]


def clean_explanation(text):
    """Drop any <think>...</think> part and return the first non-empty line."""
    if "</think>" in text:
        text = text.split("</think>")[-1]
    for t in THINK_TAGS:
        text = text.replace(t, "")
    for line in text.split("\n"):
        if line.strip():
            return line.strip()
    return ""


def _letter_token_ids(tok, letter):
    """Token ids that can represent the answer letter right after 'Answer:'.

    Tokenizers differ on whether the letter has a leading space ("A" vs " A" /
    "▁A"), so we collect both variants and sum their probabilities.
    """
    ids = set()
    for s in (letter, " " + letter):
        enc = tok(s, add_special_tokens=False).input_ids
        if enc:
            ids.add(enc[-1])
    return sorted(ids)


class _HFBase:
    def __init__(self, spec):
        import torch  # noqa: F401  (imported here on purpose)
        from transformers import AutoTokenizer

        self.torch = torch
        self.spec = spec
        self.tok = AutoTokenizer.from_pretrained(spec["hf_id"])
        self.model = self._load_model(spec)
        self.model.eval()
        self.ids_a = _letter_token_ids(self.tok, "A")
        self.ids_b = _letter_token_ids(self.tok, "B")
        if set(self.ids_a) & set(self.ids_b):
            raise RuntimeError("A and B share a token id; check this tokenizer")

    def _dtype(self, spec, is_seq2seq):
        torch = self.torch
        want = spec.get("dtype", "auto")
        if want != "auto":
            return getattr(torch, want)
        if not torch.cuda.is_available():
            return torch.float32
        # mT0 / T5 models overflow in float16, so avoid it for seq2seq.
        if is_seq2seq:
            return torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float32
        return torch.float16

    def _device(self):
        return "cuda" if self.torch.cuda.is_available() else "cpu"

    def _quant_kwargs(self, spec):
        if not spec.get("load_in_4bit"):
            return {}
        from transformers import BitsAndBytesConfig
        return {
            "quantization_config": BitsAndBytesConfig(
                load_in_4bit=True, bnb_4bit_compute_dtype=self.torch.float16
            ),
            "device_map": "auto",
        }

    def _pick(self, logits):
        torch = self.torch
        logits = logits.float()
        a = torch.logsumexp(logits[self.ids_a], dim=0).item()
        b = torch.logsumexp(logits[self.ids_b], dim=0).item()
        return a, b


class HFCausal(_HFBase):
    def _load_model(self, spec):
        from transformers import AutoModelForCausalLM
        kw = self._quant_kwargs(spec)
        model = AutoModelForCausalLM.from_pretrained(
            spec["hf_id"], torch_dtype=self._dtype(spec, False), **kw
        )
        if not kw:
            model = model.to(self._device())
        return model

    def score_ab(self, prompt):
        torch = self.torch
        inputs = self.tok(prompt, return_tensors="pt").to(self.model.device)
        with torch.no_grad():
            logits = self.model(**inputs).logits[0, -1]
        return self._pick(logits)

    def generate(self, prompt, max_new_tokens=60):
        torch = self.torch
        inputs = self.tok(prompt, return_tensors="pt").to(self.model.device)
        pad = self.tok.pad_token_id if self.tok.pad_token_id is not None else self.tok.eos_token_id
        extra = {}
        think_ids = _think_token_ids(self.tok)
        if think_ids:  # only Qwen-style tokenizers have these; others are unchanged
            extra["bad_words_ids"] = [[i] for i in think_ids]
        with torch.no_grad():
            out = self.model.generate(
                **inputs, max_new_tokens=max_new_tokens, do_sample=False, pad_token_id=pad, **extra
            )
        text = self.tok.decode(out[0, inputs["input_ids"].shape[1]:], skip_special_tokens=True)
        return clean_explanation(text)


class HFSeq2Seq(_HFBase):
    def _load_model(self, spec):
        from transformers import AutoModelForSeq2SeqLM
        kw = self._quant_kwargs(spec)
        model = AutoModelForSeq2SeqLM.from_pretrained(
            spec["hf_id"], torch_dtype=self._dtype(spec, True), **kw
        )
        if not kw:
            model = model.to(self._device())
        return model

    def score_ab(self, prompt):
        torch = self.torch
        enc = self.tok(prompt, return_tensors="pt").to(self.model.device)
        start = self.model.config.decoder_start_token_id
        dec = torch.tensor([[start]], device=self.model.device)
        with torch.no_grad():
            logits = self.model(**enc, decoder_input_ids=dec).logits[0, -1]
        return self._pick(logits)

    def generate(self, prompt, max_new_tokens=60):
        torch = self.torch
        enc = self.tok(prompt, return_tensors="pt").to(self.model.device)
        with torch.no_grad():
            out = self.model.generate(**enc, max_new_tokens=max_new_tokens, do_sample=False)
        return clean_explanation(self.tok.decode(out[0], skip_special_tokens=True))


def load_model(name, registry=None, seed=0):
    registry = registry or load_model_registry()
    if name not in registry:
        raise KeyError(f"Unknown model {name!r}. Known: {sorted(registry)}")
    spec = registry[name]
    kind = spec["type"]
    if kind == "random":
        return RandomModel(seed), spec
    if kind == "causal":
        return HFCausal(spec), spec
    if kind == "seq2seq":
        return HFSeq2Seq(spec), spec
    raise ValueError(f"Unknown model type {kind!r} for {name}")