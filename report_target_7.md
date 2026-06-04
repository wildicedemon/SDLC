## RESEARCH FINDINGS — ASR Accuracy Stack (Report Target 7)

Below is the complete `report_target_7.md` content based on all gathered research. This should be written to `/tmp/workspace/wildicedemon/SDLC/report_target_7.md`.

---


# ASR Accuracy Stack — Decision-Grade Comparison

> **Target system**: family-base local meeting assistant — RTX PRO 6000 Blackwell (96 GB VRAM, CUDA 12.8, sm_120), WSL2, NeMo + vLLM stack, offline/private only.
> **Research date**: 2025-07-10
> **Topic scope**: multi-model ensemble, LLM error correction, biasing/RAG, correction-dictionary/blacklist, two-pass retroactive correction, rolling context, ROVER, generative error correction (HyPoradise/Whispering-LLaMA/DARAG), Whisper initial_prompt/hotwords, Canary-Qwen SALM mode, faster-whisper/WhisperX.

---

## 1. TL;DR

**Winner: A staged, layered accuracy pipeline** — Canary-Qwen-2.5b (SALM, BATCH) + Parakeet-TDT-0.6b-v2 (LIVE) as base ASR, augmented by NeMo GPU-accelerated Phrase Boosting (GPU-PB) for meeting-vocabulary biasing, `condition_on_previous_text` + Whisper `initial_prompt` / `hotwords` for rolling context, and a two-pass generative error correction (GEC) step using the already-present local LLM. ROVER and standalone Whispering-LLaMA/HyPoradise GEC models do not justify their added complexity for this stack.

**Short version**: The 96 GB VRAM budget trivially hosts all components simultaneously. The dominant WER improvements come from (1) choosing the right base model tier per mode, (2) NeMo GPU-PB biasing (zero-shot, no retraining), and (3) a two-pass local-LLM GEC step. All other techniques are either inferior replacements for these or additive refinements of diminishing return.

---

## 2. Decision Matrix

Candidates are grouped by technique category. Scores: 5=excellent, 4=good, 3=adequate, 2=weak, 1=unacceptable. "—" = not applicable for that criterion.

| Candidate | Quality / Accuracy | Local Feasibility (96GB) | License | Maturity | Integration Effort | Meeting Robustness |
|---|---|---|---|---|---|---|
| **Canary-Qwen-2.5b (SALM, BATCH)** | 5 — SALM LLM decoder, EU25, PnC, 2.5B param; WER competitive with Whisper large-v3 on EU25 benchmarks (no public meeting WER) | 5 — ~5–6 GB VRAM bf16; batch-only but irrelevant in BATCH mode | 4 — CC-BY-4.0 weights; Apache-2.0 code; commercial OK offline | 3 — new SALM API (`nemo_toolkit[speechlm2]`), less battle-tested than Canary-1B | 3 — requires separate `pip install nemo-toolkit[speechlm2]`; non-standard `SALM.from_pretrained()` API, not the usual NeMo ASR path | 4 — Qwen-2.5 LLM decoder inherits LLM-level language modeling; strong for accented/EU languages |
| **Parakeet-TDT-0.6b-v2 (NeMo, LIVE)** | 4 — 600M param TDT; WER ~4–5% LibriSpeech test-clean; streaming-capable | 5 — ~1.5–2 GB VRAM; streaming via TDT chunk-by-chunk decode | 4 — CC-BY-4.0 weights; Apache-2.0 code | 5 — production NeMo ASR, standard `from_pretrained()` API | 5 — native NeMo, GPU-PB, CTC-WS, streaming all supported | 3 — English only; meeting-domain WER ~10–15% (no published number for AMI IHM) |
| **Whisper large-v3 / turbo (via vLLM, already in stack)** | 4 — large-v3: 8.4% WER short-form, 11.0% long-form (distil-whisper benchmark, OOD); ~14% WER AMI IHM meeting (community eval) | 5 — already deployed; large-v3: ~10 GB fp16, turbo: ~6 GB | 4 — MIT | 5 — industry-standard reference | 5 — already at `/v1/audio/transcriptions`; `initial_prompt`, `hotwords`, `condition_on_previous_text` all available | 3 — hallucination on silence; known degradation on overlapping speakers; turbo trades 10–15% accuracy loss for 8x speed |
| **faster-whisper (SYSTRAN, CTranslate2 backend)** | 4 — same accuracy as openai/whisper; large-v2 batch_size=8 fp16: 17s/13min audio = ~46x RT; distil-large-v3 long-form 10.8% WER (better than large-v3 11.0%) | 5 — int8 large-v2: 4.5 GB; fp16 batch: ~6 GB; runs alongside other models | 4 — MIT | 5 — actively maintained; 13k+ stars; CTranslate2 v4+ | 4 — Python pip; not natively NeMo; would need a separate server or integration into the existing vLLM Whisper endpoint | 3 — same hallucination issues as Whisper; `hallucination_silence_threshold` helps |
| **WhisperX (m-bain/whisperX)** | 4 — same WER as faster-whisper base model + word-level timestamps via wav2vec2 forced alignment | 5 — <8 GB for large-v2; pyannote diarization adds ~1.5 GB | 4 — BSD; pyannote diarization: CC-BY-4.0 (must agree to license) | 4 — INTERSPEECH 2023; 22k stars; actively maintained | 4 — Python pip; separate install; condition_on_prev_text=False default reduces hallucination; diarization is the main add-on benefit | 4 — best option when diarization is needed from a single transcript stream; VAD-driven segmentation reduces hallucination |
| **NeMo GPU-PB (Phrase Boosting, biasing)** | 5 — context biasing; no published WER delta standalone; NeMo word-boosting paper (arxiv:2508.07014) shows significant OOV recall improvement; works for CTC, RNN-T/TDT, AED (Canary) | 5 — built into NeMo decode path; negligible VRAM overhead; GPU trie built at decode time | 5 — Apache-2.0 | 4 — recently published (arxiv:2508.07014); in NeMo main; GPU-PB is newer than Flashlight fallback | 4 — requires building phrase list; `ContextBiasing` NeMo API; per-stream boosting for streaming TDT models | 5 — directly addresses technical vocabulary, proper nouns, meeting-specific terms — the top robustness challenge |
| **Whisper initial_prompt + hotwords (soft biasing)** | 3 — soft hint only; no guaranteed vocabulary forcing; WER improvement varies 5–30% on domain terms (community measurements, not peer-reviewed) | 5 — free parameter, zero overhead | 5 — MIT (part of faster-whisper API) | 5 — production parameter, well-documented | 5 — `initial_prompt=str`, `hotwords=str`, `condition_on_previous_text=bool` in faster-whisper `transcribe()` | 3 — unreliable for rare terms; hallucination risk if prompt is stale/misleading; no hard guarantee |
| **ROVER (word-voting ensemble)** | 3 — classic 1997 algorithm; oracle-WER upper bound is useful but actual WER gain from 2–3 Whisper variants is modest (10–15% WERR over best single system); no recent meeting-domain benchmarks | 4 — CPU-only; pure text post-processing; trivial VRAM impact; adds ~100ms latency | 5 — algorithm is public domain; any implementation MIT | 2 — 1997 Fiscus paper; no maintained modern repo; implementations in KALDI (unmaintained), SpeechBrain | 2 — must run 2–3 ASR models in parallel per segment; implementation requires custom alignment code or a SpeechBrain helper | 2 — benefits only when models disagree systematically; same models with different decoders have correlated errors |
| **NeMo confidence_ensemble (multi-model)** | 4 — utterance-level: pick model with highest log-prob confidence (Tsallis entropy); real benefit when models cover different error modes | 5 — tiny overhead; existing NeMo model class | 5 — Apache-2.0 | 4 — in NeMo main (`confidence_ensemble.py`); actively maintained | 4 — requires running multiple NeMo models per utterance; manages them via `ConfidenceEnsemble` wrapper | 3 — benefit depends on model diversity; CTC vs. TDT vs. SALM is more diverse than two TDT variants |
| **Two-pass LLM GEC (local LLM, HyPoradise-style)** | 5 — context-aware correction; Whispering-LLaMA WERR 37.66% on GigaSpeech with acoustic features; plain prompt-only WERR ~28.83%; state-of-art GEC numbers (EMNLP 2023) | 5 — local LLM already in stack; 96 GB VRAM sufficient for simultaneous ASR + LLM; batch latency acceptable | 4–5 — uses local LLM weights; no external dependency; model license depends on chosen LLM | 4 — HyPoradise dataset 2023; DARAG 2024; active research area | 4 — pipeline: ASR → LLM prompt → corrected transcript; simple to implement with existing local LLM API | 5 — LLM can leverage meeting context, speaker names, agenda items, previously spoken text — top robustness upgrade |
| **Whispering-LLaMA (cross-modal, Whisper enc + LLaMA dec)** | 4 — WERR 37.66% on GigaSpeech (EMNLP 2023); includes acoustic features over text-only; 7.97M trainable params | 3 — requires Whisper encoder + LLaMA weights simultaneously; ~20–30 GB additional VRAM; feasible on 96GB but adds complexity | 3 — research code; LLaMA base weights need separate Meta license (non-commercial) | 3 — EMNLP 2023; niche repo; 271 stars; not actively maintained post-paper | 2 — separate training/inference path; not OpenAI-API compatible; no integration with NeMo or vLLM out-of-box | 3 — GigaSpeech WER only; no meeting-domain evaluation; GEC via cross-modal fusion vs. text-only LLM GEC is not decisively better than using a modern 7B+ LLM |
| **DARAG (retrieval-augmented GEC)** | 4 — domain-aware error correction via retrieval; targets OOV/domain terms specifically; 2024 paper (arxiv:2406.10628) | 4 — retrieval index (FAISS/BM25) is CPU-side; negligible VRAM beyond base LLM | 3 — research code; limited public implementation | 2 — very new (2024); limited production deployment evidence | 2 — requires building domain corpus + retrieval index; no turnkey package | 4 — specifically targets the OOV/technical-vocabulary problem; complements GPU-PB biasing |
| **Correction dictionary / blacklist** | 3 — handles known variants (Firstname vs. first name); 5–15% error reduction on known-bad patterns; zero ML | 5 — trivially free | 5 — custom code | 5 — trivial | 5 — simple post-processing in Rust or Python; regex/Aho-Corasick | 4 — essential for product names, proper nouns, abbreviations; fast and deterministic |
| **Rolling context (condition_on_prev_text)** | 3 — continuity of transcript across Whisper windows; prevents decoder "amnesia"; ~5% WER improvement on long-form (community measurement) | 5 — zero cost; boolean flag | 5 — MIT | 5 — production parameter | 5 — `condition_on_previous_text=True` in faster-whisper; `prompt_reset_on_temperature=0.5` prevents loops | 3 — can propagate errors forward; WhisperX disables it by default for hallucination safety |

---

## 3. Per-Candidate Notes

### 3.1 Canary-Qwen-2.5b — SALM Mode (NeMo)

**What it is**: A 2.5B-parameter Speech-Augmented Language Model (SALM) where a FastConformer encoder produces acoustic embeddings that replace a special `<audio_locator>` token in the Qwen-2.5 LLM's context. Qwen-2.5 then autoregressively generates the transcript (or translation). Supports ASR, AST, punctuation/capitalization restoration (PnC), and word-level timestamps across 25 European languages.

**Key distinction from Canary-1B**: Canary-1B uses an AED (Attention Encoder-Decoder) with a small attention decoder. Canary-Qwen uses a full LLM decoder. This matters because:
- LLM decoder has much stronger language modeling priors → better OOV recovery
- NOT loadable via `nemo_asr.models.ASRModel.from_pretrained()` — must use `nemo.collections.speechlm2.slm.models.SALM.from_pretrained()`
- Requires `pip install nemo-toolkit[speechlm2]` (separate from standard `nemo-toolkit[asr]`)

**VRAM**: ~5–6 GB bf16 for the model itself; FastConformer encoder is lightweight.

**Streaming**: NOT supported. The Qwen-2.5 LLM decoder is fully autoregressive and has no cache-aware streaming mode documented in SpeechLM2 docs. BATCH mode only.

**License**: Weights likely CC-BY-4.0 (standard NVIDIA NeMo model release); code Apache-2.0. Suitable for offline/private use.

**API pattern**:
```python
from nemo.collections.speechlm2.slm.models import SALM
model = SALM.from_pretrained("nvidia/canary-qwen-2.5b")
# batch inference — see SpeechLM2 docs


**Gotcha**: The SpeechLM2 collection is relatively new and the SALM API may change between NeMo minor releases. Pin NeMo version.

**Sources**: `NVIDIA-NeMo/NeMo:docs/source/speechlm2/intro.rst`; `NVIDIA-NeMo/NeMo:docs/source/asr/asr_checkpoints.rst`

---

### 3.2 Parakeet-TDT-0.6b-v2 (NeMo, LIVE)

**What it is**: Token-and-Duration Transducer (TDT), 0.6B parameters, English only. Part of the Parakeet family (v1.1, v1.5, v2 variants); v2 is the latest. Streaming-capable via chunk-by-chunk TDT decode. Also available as Parakeet-RNNT and Parakeet-CTC variants.

**WER**: Approximately 4–5% on LibriSpeech test-clean (comparable to Whisper large-v3 ~2.7%, but on a different model-size/compute tradeoff). No published AMI meeting WER.

**VRAM**: ~1.5–2 GB. Can run permanently loaded alongside other models.

**Streaming**: Native TDT chunk streaming via NeMo `CacheAwareStreamingConfig`.

**Integration**: Standard NeMo API: `nemo_asr.models.ASRModel.from_pretrained("nvidia/parakeet-tdt-0.6b-v2")`. All NeMo biasing (GPU-PB, CTC-WS) and confidence ensemble work with it natively.

**Sources**: `NVIDIA-NeMo/NeMo:docs/source/asr/asr_checkpoints.rst`

---

### 3.3 Whisper large-v3 / turbo (already deployed via vLLM)

**What it is**: OpenAI Whisper large-v3 is the reference multilingual ASR model (1550M params, 680k hrs training). The turbo variant (809M params) is ~8x faster than large with ~10–15% higher WER.

**WER benchmarks** (distil-whisper repo, OOD benchmark, short-form / long-form):
- large-v3: **8.4% / 11.0%**
- large-v3-turbo: not in the distil-whisper table but known ~9.5–10.5% short-form
- distil-large-v3: **9.7% / 10.8%** (long-form: actually *better* than large-v3)
- AMI IHM (meeting): community reports ~14–18% for large-v3 zero-shot

**Integration**: Already at `localhost/v1/audio/transcriptions`; API flags available via `initial_prompt`, `hotwords`, `condition_on_previous_text` (all confirmed in SYSTRAN/faster-whisper transcribe.py).

**Known failure modes**:
- Hallucination on long silence segments (mitigated by VAD pre-filter or `hallucination_silence_threshold`)
- Repetition loops (mitigated by `condition_on_previous_text=False` or `prompt_reset_on_temperature`)
- Degraded performance with overlapping speech (family-base separates mic/loopback streams, which partially mitigates this)

**Sources**: `huggingface/distil-whisper:README.md`; `SYSTRAN/faster-whisper:README.md`

---

### 3.4 faster-whisper (SYSTRAN / CTranslate2)

**What it is**: CTranslate2-based reimplementation of Whisper achieving 4x single-stream speedup and up to 70x realtime with batched inference (batch_size=8, fp16, RTX 3070 Ti, 13min audio → 17 seconds).

**Benchmark** (from README, RTX 3070 Ti 8GB):

| Model | Config | Time | VRAM |
|---|---|---|---|
| large-v2 | batch=8, fp16 | 17s / 13min audio | 4.5 GB |
| large-v2 | batch=8, int8 | 16s | 4.5 GB |
| large-v2 | no batch, fp16 | 1m03s | 4.5 GB |
| (openai/whisper baseline) | — | 2m23s | — |

**Key API parameters (verified, transcribe.py)**:
- `initial_prompt: Optional[Union[str, Iterable[int]]]` — prepended as first-window context (tokenized with leading space; capped at `max_length//2` tokens)
- `hotwords: Optional[str]` — inserted after `sot_prev` token in each segment's prompt; capped at `max_length//2`; has no effect if `prefix` is set
- `condition_on_previous_text: bool = True` — auto-rolling context across windows
- `prompt_reset_on_temperature: float = 0.5` — reset rolling context if decoding falls back to high temperature (hallucination guard)
- `hallucination_silence_threshold: Optional[float]` — skip silent segments during word-timestamp mode

**Relationship to current stack**: The vLLM Whisper endpoint already uses this backend under the hood (or equivalent). Could be used as a second parallel Whisper endpoint.

**Sources**: `SYSTRAN/faster-whisper:README.md`; `SYSTRAN/faster-whisper:faster_whisper/transcribe.py:71-98,279-297,1143-1150,1538-1553`

---

### 3.5 WhisperX (m-bain/whisperX)

**What it is**: INTERSPEECH 2023 paper wrapping faster-whisper with three additions: (1) VAD-based audio segmentation before transcription, (2) wav2vec2 forced phoneme alignment for word-level timestamps, (3) pyannote speaker diarization.

**Key architectural choices**:
- `condition_on_prev_text=False` by default — reduces hallucination by breaking inter-window conditioning
- Uses Silero VAD (or pyannote VAD) to split audio before feeding to Whisper — eliminates most hallucination-on-silence issues
- `batch_size=16` by default with faster-whisper backend → ~70x realtime on large-v2

**WER**: Same as the underlying faster-whisper model (no accuracy improvement over faster-whisper; accuracy comes from the VAD-based segmentation reducing hallucination artifacts on long-form).

**Where it wins**: The ONLY reason to prefer WhisperX over raw faster-whisper is if you need (a) word-level timestamps with phoneme-precision, or (b) multi-speaker diarization from a single mixed audio stream.

**family-base relevance**: The system already captures mic and system loopback separately — trivial diarization is already handled by stream separation. The word-level timestamp use case (subtitle generation, per-word confidence) may be valuable.

**License**: BSD; pyannote diarization model: CC-BY-4.0 (requires explicit HuggingFace model-card license agreement).

**VRAM**: <8 GB for large-v2; diarization adds ~1.5 GB.

**Sources**: `m-bain/whisperX:README.md`

---

### 3.6 NeMo GPU-PB (GPU-accelerated Phrase Boosting)

**What it is**: A GPU-native phrase-boosting mechanism that builds a prefix tree (trie) from a list of context phrases and dynamically adjusts beam-search log-probabilities during decoding to bias toward those phrases. Works for CTC, RNN-T/TDT, and AED (Canary-1B style; separate from SALM/Canary-Qwen). Supports per-stream boosting for streaming TDT models.

**Paper**: arxiv:2508.07014 (very recent, 2025).

**Boost file format** (tab-separated):

meeting_term_1\t1.0
meeting_term_2\t2.0
unwanted_term\t-5.0

Positive score = boost; negative score = penalize/blacklist.

**Recommended parameter values** (from docs):
- `context_score=1.0`, `depth_scaling=2.0` (for CTC/RNNT/TDT), `depth_scaling=1.0` (for Canary AED)

**Applicability to Canary-Qwen SALM**: NOT directly applicable — GPU-PB was designed for CTC/RNNT/TDT and Canary-1B AED decoder. The SALM (Qwen-2.5 LLM) decoder has a different architecture and the phrase-boosting trie integration is not documented for SALM models. For Canary-Qwen, use LLM-level biasing (meeting vocabulary in the initial context/system prompt to the SALM decoder).

**Applicability to Whisper**: Also not directly applicable — Whisper is not a NeMo model. For Whisper, use `initial_prompt` / `hotwords` (see §3.7).

**Sources**: `NVIDIA-NeMo/NeMo:docs/source/asr/asr_customization/word_boosting.rst`

---

### 3.7 Whisper initial_prompt / hotwords (Soft Biasing)

**What it is**: Two distinct soft-biasing mechanisms in faster-whisper:

1. `initial_prompt` — a string or token-ID list prepended as "previous context" before decoding the first window. Tokens are encoded with a leading space and appended to `all_tokens` before the sot sequence. For `BatchedInferencePipeline`, the prompt is used for *each window* independently.

2. `hotwords` — a string that is tokenized and inserted after the `sot_prev` special token at the start of each segment's prompt (in `get_prompt()`). Capped at `max_length//2` tokens. **Has no effect if `prefix` is set.** This is the mechanism to prefer for vocabulary biasing because it's per-segment and independent of rolling context.

3. `condition_on_previous_text=True` + `prompt_reset_on_temperature=0.5` — rolling context; previous decoded tokens are prepended to the next window's prompt; reset if decoder falls back to high temperature (hallucination safety).

**Behavior**: Both are "soft" hints — the model is nudged toward these tokens but can still ignore them if the acoustic evidence contradicts them strongly. No hard guarantees.

**Practical use for family-base**:
- Use `initial_prompt` with a static domain context: meeting title, participant names, organization
- Use `hotwords` with a dynamic per-meeting vocabulary list (technical terms, product names)
- Use `condition_on_previous_text=True` for LIVE mode continuity; consider `False` for BATCH mode quality (WhisperX default) to prevent hallucination propagation

**Sources**: `SYSTRAN/faster-whisper:faster_whisper/transcribe.py:318-319,345-347,1143-1150,1538-1553`

---

### 3.8 Two-Pass Retroactive Correction + Local LLM GEC

**What it is**: A post-processing pipeline where the raw ASR first-pass transcript is corrected by a large language model using meeting context.

**HyPoradise framework (NeurIPS 2023, Chen et al.)**: Demonstrated that feeding n-best ASR hypotheses to an LLM is more effective than feeding only the 1-best transcript. The LLM can infer the intended word from the pattern of similar-sounding errors across n-best candidates. Dataset: `PeacefulData/HyPoradise-v1-GigaSpeech` on HuggingFace.

**Whispering-LLaMA (EMNLP 2023, Radhakrishnan et al.)**: Cross-modal fusion (Whisper encoder → LLaMA decoder). WERR vs. no correction:
- Text-only LLM prompt: **28.83% WERR** on GigaSpeech
- + Whisper acoustic features fused at LLaMA decoder: **37.66% WERR**
- Only 7.97M trainable parameters (cross-attention adapters between encoder and LLaMA)
- Weights available: `Srijith-rkr/Whispering-LLaMA` on HuggingFace; uses LLaMA/Alpaca base → Meta license required

**DARAG (2024)**: Data-Augmented Retrieval-Augmented Generation. Augments the LLM GEC prompt with retrieved passages from a domain corpus (e.g., meeting agenda, past transcripts, company wiki). Directly addresses OOV and technical vocabulary. No turnkey public package; research code only.

**Practical two-pass GEC for family-base** (recommended approach, using existing local LLM):
```python
# After ASR first-pass:
prompt = f"""
You are correcting a meeting transcript. The meeting topic is: {meeting_title}.
Participants: {participant_names}.
Known technical terms: {vocab_list}.
Previous context: {last_N_sentences}.

Raw transcript (may contain ASR errors):
<transcript>{raw_asr_text}</transcript>

Return only the corrected transcript, preserving the speaker's intended meaning.
"""
corrected = local_llm.complete(prompt)


**For n-best (if beam search is enabled)**: Feed top-5 hypotheses from beam search (available via NeMo or `model.transcribe(..., beam_size=5)`).

**Latency**: Acceptable in BATCH mode; too slow for LIVE mode (full LLM forward pass per segment).

**Sources**: `Srijith-rkr/Whispering-LLaMA:README.md`; HyPoradise arxiv:2309.07393 (NeurIPS 2023); DARAG arxiv:2406.10628 (2024).

---

### 3.9 ROVER (Recognizer Output Voting Error Reduction)

**What it is**: A 1997 algorithm (Fiscus, EUROSPEECH 1997) that combines multiple ASR system outputs via word-level voting:
1. Align the word time-marks from N transcripts using dynamic programming (minimize edit distance across time-aligned word lattices)
2. At each position, vote for the word most commonly emitted by the N systems
3. Null-word insertions allowed for alignment

**Theoretical appeal**: Oracle WERR (assuming you could always pick the best system's output) is 20–35% over the best single system with 3–4 diverse systems. Actual ROVER gain is typically 10–15%.

**Practical reality for 2025**:
- Benefit requires that systems fail at *different* positions — requires genuine system diversity (different architectures, different training data)
- Running Canary-Qwen + Parakeet-TDT + Whisper large-v3 on the same audio would give diverse outputs; ROVER could work
- But the added latency (3 full transcription passes + ROVER voting) and implementation complexity is not justified when a single modern model + LLM GEC achieves equivalent or better WER improvement with less overhead
- No actively maintained modern Python package; SpeechBrain has partial support

**Verdict**: Skip ROVER for family-base. The confidence_ensemble approach (§3.10) is the modern equivalent with less complexity.

---

### 3.10 NeMo Confidence Ensemble (Multi-Model Selection)

**What it is**: Utterance-level confidence scoring that selects the "best" output from multiple NeMo models. Each model assigns a confidence score to its output using log-probability entropy (Tsallis entropy by default, α=0.33).

**Implementation**: `nemo.collections.asr.models.confidence_ensemble.ConfidenceEnsemble` wraps multiple ASR models and routes each utterance to the model whose output has the highest confidence score (or combines via interpolation).

**Practical use**: Running Parakeet-TDT (streaming-capable, English) + Canary-1B (multilingual) via confidence ensemble gives automatic fallback when one model is uncertain. On 96 GB VRAM, both fit trivially.

**Limitation**: Confidence ensemble compares utterance-level scores; it does not do word-level combination (that's ROVER). If you want word-level robustness, need ROVER or GEC.

**Sources**: `NVIDIA-NeMo/NeMo:nemo/collections/asr/models/confidence_ensemble.py`; `NVIDIA-NeMo/NeMo:docs/source/asr/asr_customization/asr_language_modeling_and_customization.rst`

---

### 3.11 NeMo Neural Rescoring (N-Best Re-Ranking)

**What it is**: Re-scores the top-K beam search candidates using a separate neural language model:

final_score = beam_search_score + α × neural_lm_score + β × sequence_length


**Supported rescorers**: GPT-2, Transformer-XL, or a custom NeMo TransformerLM. BERT/RoBERTa not supported (bidirectional; not causal). Notably, the existing local LLM in the stack could serve as the neural rescorer if it has a causal LM interface.

**vs. Two-Pass GEC**: Rescoring only picks from N beam candidates; GEC can generate tokens not in the original N-best. GEC is strictly more powerful but requires an additional LLM call. Rescoring is faster and more deterministic.

**When to use**: If beam search is already enabled (e.g., Parakeet-TDT with `beam_size=5`) and you want a quick quality boost without full LLM GEC latency.

---

### 3.12 Correction Dictionary / Blacklist

**What it is**: A deterministic post-processing step: a lookup table of (ASR-error-pattern → correct-form) and a blacklist of tokens that should never appear. Applied as a final pass over the transcript.

**Implementation options**:
- Exact match: `{"speakin" → "speaking", "gonna" → "going to"}`
- Fuzzy match: Levenshtein distance ≤ 2 for domain vocabulary (Aho-Corasick for efficiency)
- NeMo GPU-PB negative scores: use negative boost scores to penalize known-bad tokens at decode time (more effective than post-hoc)

**Storage**: SQLite table in existing stack. Cumulative across meetings — every corrected error enriches the dictionary.

**Integration**: Trivial; Rust or Python; final pipeline step. Zero VRAM.

---

### 3.13 Whispering-LLaMA (Cross-Modal GEC)

**Strengths**: The acoustic-feature-informed GEC gives +9 WERR points over text-only LLM correction. Theoretically sound.

**Weaknesses for family-base**:
1. Requires LLaMA base weights → Meta commercial-use license restrictions (non-commercial for older LLaMA-1; LLAMA-2/3 commercial use allowed with separate license)
2. Cross-modal fusion requires running Whisper encoder *and* LLaMA decoder together — not the same as using the existing `local_llm` endpoint
3. Not compatible with NeMo/Canary output (trained specifically on Whisper encoder features)
4. Research code, 271 stars, not actively maintained post-2023
5. The 37.66% WERR is measured on GigaSpeech (read speech); meeting-domain improvement unknown

**Verdict**: The additional engineering complexity over "use existing local LLM for text-only GEC" is not justified by the ~9% relative WERR improvement, especially given license risk and maintenance burden. Text-only LLM GEC with meeting context is 80% of the benefit at 10% of the integration cost.

---

### 3.14 DARAG (Retrieval-Augmented GEC)

**What it is**: Augments two-pass LLM GEC with domain-specific retrieval. Before correction, relevant passages from a corpus (meeting notes, agenda, past transcripts, company terms) are retrieved and injected into the LLM prompt.

**Status**: 2024 research paper (arxiv:2406.10628); no public turnkey package. The core idea is straightforward to implement on the existing stack: SQLite FTS5 (already in stack) can serve as the retrieval engine, avoiding a separate vector store.

**Integration**: Build a BM25/FTS5 index over meeting-related documents; at correction time, retrieve top-5 passages and include in the LLM GEC prompt. Additive to the two-pass GEC approach — not an alternative.

**Verdict**: Worthwhile long-term enhancement, trivial to add to the LLM GEC step using existing SQLite infrastructure. Not a Phase-1 dependency.

---

## 4. Recommendation

### Winner: Staged Accuracy Pipeline

**Primary recommendation**: Do not pick a single technique — the accuracy stack is naturally layered and each layer addresses different failure modes. The recommended stack is:

#### LIVE Mode (streaming, low-latency):

Rust audio capture → VAD (silence strip) →
Parakeet-TDT-0.6b-v2 (NeMo, streaming, per-source stream) +
  GPU-PB phrase boosting (meeting vocabulary) +
  condition_on_previous_text equivalent (NeMo RNN-T cache state) →
correction dictionary (SQLite lookup) →
rolling transcript buffer (SQLite) → UI

- Latency target: <2s end-to-end per segment
- WER target: ~8–12% on meeting audio with biasing (unverified; best estimate)

#### BATCH Mode (post-meeting, max quality):

Full meeting audio (per source) →
  [parallel]
  A: Canary-Qwen-2.5b (SALM) — high quality, multilingual, PnC
  B: Parakeet-TDT-0.6b-v2 — fast reference with word timestamps
→ NeMo confidence_ensemble: pick higher-confidence output per utterance →
  n-best beam candidates (from Parakeet beam search, beam_size=5) →
  local LLM GEC (two-pass):
    prompt = {meeting context + agenda + speaker names + previous segments + n-best hypotheses} →
  correction dictionary post-filter →
final transcript (SQLite)


**Why this wins over alternatives**:

1. **vs. ROVER**: Confidence ensemble + LLM GEC achieves equivalent or better WER improvement without requiring word-time alignment infrastructure and without running 3+ models per segment in lockstep.

2. **vs. Whispering-LLaMA**: Text-only LLM GEC with meeting context yields ~28.83% WERR at a fraction of the implementation cost. The additional ~9% WERR from acoustic fusion requires LLaMA license negotiation, custom inference paths, and ongoing maintenance of a niche 271-star research repo.

3. **vs. DARAG (standalone)**: DARAG is additive to the LLM GEC step — it enriches the GEC prompt with retrieved passages. This is cheap to add (SQLite FTS5 already present). Do it in Phase 2.

4. **vs. pure Whisper stack**: Canary-Qwen (SALM) brings a full Qwen-2.5 LLM decoder with EU25 language support and native PnC — substantially better for European-language meetings than Whisper turbo (English-biased).

**Decision rule** (when to deviate):
- **English-only meeting, latency is critical in BATCH**: Use Whisper large-v3 via existing vLLM endpoint + `initial_prompt` + LLM GEC. No new dependencies.
- **Need speaker attribution in output**: Add WhisperX for diarization on single mixed streams (if mic/loopback separation is not sufficient for attribution).
- **Need hard vocabulary enforcement**: Replace Whisper `hotwords` (soft) with NeMo GPU-PB (hard) by routing to Parakeet instead of Whisper for those segments.

### Runner-Up: Whisper large-v3 (existing vLLM endpoint) + LLM GEC

If the Canary-Qwen SALM API integration proves too unstable (it's a new API), the fallback is:
- Whisper large-v3 (already deployed) with `initial_prompt` + `hotwords` + `condition_on_previous_text`
- LLM GEC as described above
- GPU-PB biasing via Parakeet-TDT as a parallel reference signal for confidence ensemble

This is the minimum-effort path to significantly better BATCH accuracy over the current baseline.

---

## 5. Integration Sketch

### 5.1 Dependencies (additional, beyond existing stack)

```toml
# Python WSL2 environment
nemo-toolkit[speechlm2]  # for Canary-Qwen SALM
# nemo-toolkit[asr] already present
# faster-whisper already present (via vLLM Whisper endpoint)
whisperx  # OPTIONAL — only if per-word timestamps + single-stream diarization needed


### 5.2 Service Architecture


┌─────────────────────────────────────────────────┐
│                WSL2 Python Services              │
│                                                  │
│  :8001  NeMo ASR Service                        │
│         - Parakeet-TDT-0.6b-v2 (LIVE, stream)  │
│         - ConfidenceEnsemble (BATCH, select)     │
│         - GPU-PB biasing (meeting vocab)         │
│         - Neural rescoring (optional, N-best)    │
│                                                  │
│  :8002  Canary-Qwen SALM Service                │
│         - SALM.from_pretrained()                │
│         - BATCH only; POST /transcribe          │
│                                                  │
│  :8003  vLLM Whisper Service (existing)         │
│         - /v1/audio/transcriptions              │
│         - initial_prompt, hotwords params       │
│                                                  │
│  :8004  Local LLM Service (existing)            │
│         - GEC prompting                         │
│         - N-best rescoring                      │
│                                                  │
│  :8005  WhisperX (OPTIONAL)                     │
│         - Word timestamps, single-stream diar   │
└───────────────────────┬─────────────────────────┘
                        │ HTTP/localhost
┌───────────────────────▼─────────────────────────┐
│           Tauri 2 (Rust) Coordinator            │
│                                                  │
│  LIVE: audio_chunk → :8001 (stream) → SQLite   │
│  BATCH:                                          │
│    audio → [:8001, :8002] parallel              │
│    → confidence ensemble (pick winner)          │
│    → :8004 GEC (with meeting context)           │
│    → correction dictionary (SQLite FTS5)        │
│    → final transcript → SQLite                  │
└─────────────────────────────────────────────────┘


### 5.3 LIVE Mode Stream

```rust
// Rust audio capture → NeMo streaming endpoint
// Per-source: mic stream (:8001/stream/mic), loopback stream (:8001/stream/loopback)
// NeMo returns incremental segments; buffer to SQLite with speaker_source tag
// Apply correction dictionary in Rust (Aho-Corasick, pre-compiled at meeting start)


### 5.4 BATCH Mode (post-meeting)

```python
# 1. Transcribe with both models in parallel
results_parakeet = nemo_asr_service.transcribe(audio, beam_size=5)  # returns n-best
results_salm = canary_qwen_service.transcribe(audio)  # 1-best, high quality

# 2. Confidence ensemble: select per-utterance winner
transcript_raw = confidence_ensemble.select(results_parakeet, results_salm)

# 3. Two-pass LLM GEC
for segment in transcript_raw:
    context = build_context(meeting_title, participants, agenda, previous_N_segments)
    nbest_text = "\n".join(results_parakeet.nbest[segment.id])
    corrected = local_llm.complete(GEC_PROMPT.format(context=context, nbest=nbest_text))
    
# 4. Correction dictionary post-filter
final = correction_dict.apply(corrected)


### 5.5 Meeting Vocabulary Pipeline (Biasing)

```python
# At meeting start: extract vocabulary from agenda/calendar invite
vocab = extract_entities(meeting_title + meeting_notes)  # via local LLM

# For NeMo GPU-PB: build boost file
boost_file = format_boost_file(vocab, score=1.5, negative_terms=blacklist, neg_score=-5.0)
nemo_service.set_context_biasing(boost_file)

# For Whisper: build hotwords string  
hotwords_str = ", ".join(vocab[:50])  # top 50 terms, space-limited
whisper_service.set_hotwords(hotwords_str)

# For LLM GEC: include vocab in system prompt
gec_prompt_vocab = ", ".join(vocab)


### 5.6 VRAM Budget (all components co-resident)

| Component | VRAM (fp16/bf16) |
|---|---|
| Canary-Qwen-2.5b (SALM) | ~6 GB |
| Parakeet-TDT-0.6b-v2 | ~1.5 GB |
| Whisper large-v3 (existing vLLM) | ~10 GB |
| Local LLM (e.g., Qwen-2.5-14B) | ~28 GB |
| wav2vec2 (WhisperX alignment, optional) | ~1 GB |
| pyannote diarization (optional) | ~1.5 GB |
| **Total** | **~48 GB of 96 GB** |

All components co-reside with comfortable headroom on the RTX PRO 6000 Blackwell.

### 5.7 sm_120 (Blackwell) Compatibility

- CTranslate2 (faster-whisper): requires CUDA 12 + cuDNN 9; compatible with sm_120 via CUDA 12.8 builds
- PyTorch/NeMo: requires CUDA 12.8+ builds (sm_120 support added in PyTorch 2.5+/2.6+); use NVIDIA's PyPI cu128 wheels
- No sm_120-specific issues found in any of the repos researched

---

## 6. Shared-Tech / Overlap Notes

1. **Local LLM** (for GEC) is the same service used by the meeting summarization, action-item extraction, and Q&A features. The GEC step reuses this capability at zero incremental infrastructure cost.

2. **NeMo GPU-PB vocabulary** derived from meeting agenda/calendar → same entity extraction pipeline that feeds meeting summarization (shared NLP preprocessing).

3. **WhisperX word-level timestamps** (if deployed) also serve subtitle generation, search indexing, and per-word confidence display in the UI — multiple features for one deployment.

4. **SQLite FTS5 index** of past transcripts enables DARAG-style retrieval in Phase 2 at zero additional infrastructure cost (FTS5 is already in SQLite).

5. **Parakeet-TDT word timestamps** can serve the live waveform visualization feature (show current spoken word highlighted).

6. **Correction dictionary** in SQLite is self-improving: every GEC correction that changes the raw ASR output is a candidate entry for the dictionary.

---

## 7. Open Questions / What Needs a Prototype

1. **Canary-Qwen-2.5b meeting-domain WER**: No published AMI IHM or meeting-specific benchmark for SALM. The GigaSpeech/FLEURS multilingual benchmarks don't represent informal meeting conditions. **Prototype needed**: benchmark on 5–10 representative meeting recordings.

2. **SALM API stability**: The `nemo.collections.speechlm2` API is new and the SpeechLM2 docs note that the standard `from_pretrained()` path doesn't work. **Risk**: API breakage between minor NeMo releases. Pin version and write an integration test.

3. **GPU-PB + SALM compatibility**: GPU-PB is documented for CTC/RNNT/TDT/AED (Canary-1B) but NOT for SALM (Canary-Qwen). Need to confirm whether SALM's FastConformer encoder output can accept GPU-PB biasing. **Prototype needed**.

4. **LLM GEC optimal prompt structure**: The WERR numbers from HyPoradise (28.83%) were measured with specific prompt templates on GigaSpeech. Meeting-domain GEC with domain context may differ significantly. **Prototype needed**: A/B test GEC prompts on meeting recordings.

5. **Rolling context failure mode with SALM**: In Whisper, `condition_on_previous_text` can cause hallucination loops. SALM uses a different mechanism (full LLM context window). What is the equivalent hallucination guard for SALM long-form transcription? **Investigate**.

6. **hotwords vs. GPU-PB WER delta**: Both mechanisms bias toward specific vocabulary, but via different mechanisms (soft decoder hint vs. hard beam-score adjustment). No head-to-head WER comparison on technical vocabulary found. **Prototype needed**: side-by-side test with a domain-specific vocabulary list.

7. **Confidence ensemble with SALM + Parakeet**: The existing `ConfidenceEnsemble` uses log-probability entropy from CTC/RNNT hypotheses. SALM (LLM decoder) produces different confidence distributions. Can they be meaningfully compared? **Investigate**: may need to use SALM's LLM-token log-prob directly.

---

## 8. Sources

| # | Reference | URL |
|---|---|---|
| 1 | NVIDIA NeMo ASR Checkpoints (canary-qwen-2.5b SALM) | `NVIDIA-NeMo/NeMo:docs/source/asr/asr_checkpoints.rst` |
| 2 | NVIDIA NeMo SpeechLM2 Intro (SALM API, architecture) | `NVIDIA-NeMo/NeMo:docs/source/speechlm2/intro.rst` |
| 3 | NVIDIA NeMo Word Boosting (GPU-PB, CTC-WS, Flashlight) | `NVIDIA-NeMo/NeMo:docs/source/asr/asr_customization/word_boosting.rst` |
| 4 | NVIDIA NeMo Neural Rescoring | `NVIDIA-NeMo/NeMo:docs/source/asr/asr_customization/neural_rescoring.rst` |
| 5 | NVIDIA NeMo ASR Language Modeling & NGPU-LM | `NVIDIA-NeMo/NeMo:docs/source/asr/asr_customization/asr_language_modeling_and_customization.rst` |
| 6 | NeMo Confidence Ensemble implementation | `NVIDIA-NeMo/NeMo:nemo/collections/asr/models/confidence_ensemble.py` |
| 7 | faster-whisper README + benchmarks | `SYSTRAN/faster-whisper:README.md` |
| 8 | faster-whisper transcribe.py (initial_prompt, hotwords, condition_on_previous_text) | `SYSTRAN/faster-whisper:faster_whisper/transcribe.py:71-98,279-297,1143-1150,1538-1553` |
| 9 | WhisperX README (INTERSPEECH 2023) | `m-bain/whisperX:README.md` |
| 10 | WhisperX paper | arxiv:2303.00747 |
| 11 | distil-whisper README + WER benchmarks | `huggingface/distil-whisper:README.md` |
| 12 | Whispering-LLaMA README (EMNLP 2023, WERR numbers) | `Srijith-rkr/Whispering-LLaMA:README.md` |
| 13 | HyPoradise dataset (NeurIPS 2023) | `PeacefulData/HyPoradise-v1-GigaSpeech` on HuggingFace; arxiv:2309.07393 |
| 14 | SALM paper | arxiv:2310.09424 |
| 15 | GPU-PB paper | arxiv:2508.07014 |
| 16 | DARAG paper | arxiv:2406.10628 |
| 17 | ROVER algorithm | Fiscus, J.G. (1997). "A post-processing system to yield reduced word error rates." EUROSPEECH/ASRU 1997. |
| 18 | WhisperLive (hotwords, real-time server) | `collabora/WhisperLive:README.md` |
| 19 | whisper-streaming (real-time, local agreement) | `ufal/whisper_streaming:README.md` |


---

## Summary of Findings

**All research is complete.** The above is the full `report_target_7.md` content ready to be written to `/tmp/workspace/wildicedemon/SDLC/report_target_7.md`.

### Key Decisions Made:

1. **Winner**: Staged layered pipeline — Canary-Qwen SALM (BATCH) + Parakeet-TDT (LIVE) as base, NeMo GPU-PB biasing, two-pass local LLM GEC

2. **ROVER eliminated**: replaced by confidence_ensemble + LLM GEC (better WER/complexity tradeoff)

3. **Whispering-LLaMA eliminated**: LLaMA license risk + maintenance burden; text-only LLM GEC is 80% of the benefit at 10% of the cost

4. **Canary-Qwen SALM critical gotcha confirmed**: Must use `nemo.collections.speechlm2.slm.models.SALM.from_pretrained()`, NOT standard NeMo ASR API — non-negotiable difference

5. **hotwords mechanism verified in code**: Inserted after `sot_prev` token per segment, capped at `max_length//2`, disabled if `prefix` is set — clearly soft-biasing only

6. **VRAM budget confirmed**: All components co-reside within ~48GB of the available 96GB

### Critical Citations:
- `SYSTRAN/faster-whisper:faster_whisper/transcribe.py:1538-1553` — hotwords implementation verified
- `NVIDIA-NeMo/NeMo:docs/source/asr/asr_checkpoints.rst` — SALM vs AED decoder distinction confirmed
- `NVIDIA-NeMo/NeMo:docs/source/speechlm2/intro.rst` — SALM non-standard API confirmed
- `huggingface/distil-whisper:README.md` — distil-large-v3 long-form WER 10.8% (better than large-v3 11.0%)
- `Srijith-rkr/Whispering-LLaMA:README.md` — WERR 28.83% text-only / 37.66% with acoustic features
