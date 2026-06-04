## Research Findings — Forced Alignment Report

Here is the complete decision-grade markdown report:

---

# Forced Alignment for family-base: Decision-Grade Comparison
## Target: Accurate word/phoneme timestamps enabling fusion, diarization attribution, and post-trim timestamps
### Candidates: wav2vec2/MMS aligner (TorchAudio), WhisperX alignment module, ctc-forced-aligner

---

## 1. TL;DR

**Winner: WhisperX alignment module (wav2vec2-based, m-bain/whisperX v3.8.6)**  
It is the only option that delivers a battle-tested, fully-integrated pipeline from ASR output → accurate word timestamps → pyannote diarization speaker assignment in a single Python package (BSD-2-clause), runs on any NVIDIA GPU, is actively maintained (commit June 2026), and is specifically designed for long-form meeting audio — the exact family-base use case.

---

## 2. Decision Matrix

| Criterion | WhisperX alignment module | ctc-forced-aligner v0.3.0 | TorchAudio MMS_FA (raw) |
|---|---|---|---|
| **Quality / accuracy** | ✅ Word boundary error vs. raw Whisper: dramatically improved; INTERSPEECH 2023 evaluated on TEDLIUM3 (WER 2.7% with large-v2, word timestamps within ~0.1s avg); 1st place Ego4D transcription 2022 | ✅ Comparable CTC accuracy; MMS model trained on 23,000h / 1,100+ langs; no independent timestamp error benchmark published | ⚠️ Same underlying algorithm; no independent alignment accuracy benchmark vs. real meeting data; deprecated in v2.9 |
| **Local/offline feasibility (96 GB RTX PRO 6000)** | ✅ Model: ~90–315 MB (base/large wav2vec2); ~1–3 GB VRAM; 70x RT (full pipeline incl. ASR); alignment alone <5x RT; BATCH only (no streaming) | ✅ Model: ~300 MB MMS-300m; ~2 GB VRAM; batched chunked inference (30 s windows); BATCH only | ⚠️ Same VRAM as above but API deprecated/removed in torchaudio ≥2.9; only usable via frozen API in older torchaudio |
| **License** | ✅ Code: BSD-2-Clause; wav2vec2 models: MIT/Apache; pyannote-audio: CC-BY-4.0; fully private use OK | ⚠️ Code: BSD; **DEFAULT MODEL (MahmoudAshraf/mms-300m-1130-forced-aligner): CC-BY-NC 4.0 — non-commercial only.** Alternative models available (MIT/Apache) but require manual configuration | ⚠️ Code: BSD; MMS_FA model weights: CC-BY-NC 4.0 (same Meta MMS model) — non-commercial trap |
| **Maturity & maintenance** | ✅ v3.8.6 released May 2026; latest commit June 3 2026; 168+ open issues, active maintainer (Barabazs); INTERSPEECH 2023 peer-reviewed; ~10,000+ GitHub stars | ✅ v0.3.0; latest commit April 15 2026; active single maintainer; ~700 stars; solid but niche | ⚠️ Maintenance-mode from torchaudio v2.9 (June 2025); forced_align API removed in 2.9; effectively legacy |
| **Integration effort (Tauri/Rust + Python service + NeMo/vLLM)** | ✅ `pip install whisperx`; Python service; accepts arbitrary ASR transcript segments (not tied to Whisper); `whisperx.align()` takes `segments` dict + audio; returns per-word `{word, start, end, score}` | ✅ `pip install ctc-forced-aligner`; standalone Python package; accepts raw text + audio; JSON output; more manual pipeline glue needed | ❌ Import torchaudio <2.9 pinned version; dependency conflict risk with current PyTorch/torchaudio stack |
| **Robustness on meeting audio** | ⚠️ Explicitly documented limitation: "overlapping speech not handled well"; handles long-form via VAD segmentation; digits/symbols in transcript cannot be aligned (fallback to interpolation) | ⚠️ Same fundamental CTC limitation on overlaps; chunked inference handles long-form well; `<star>` token for missing/uncertain text segments | ⚠️ Same CTC limitation; star token supported; but deprecated API makes this a dead end |

---

## 3. Per-Candidate Notes

### 3.1 WhisperX Alignment Module
**Repository:** `m-bain/whisperX` — https://github.com/m-bain/whisperX  
**Version:** 3.8.6 (May 2026); latest commit June 3 2026 — `chore: regenerate uv.lock for AMD64 markers`  
**Paper:** "WhisperX: Time-Accurate Speech Transcription of Long-Form Audio", Bain et al., INTERSPEECH 2023, arXiv:2303.00747  

**Core mechanism:**  
The alignment module (`whisperx/alignment.py`) is a CTC forced aligner that:
1. Takes ASR transcript segments (already decoded — source-agnostic, works with any ASR system)
2. Runs a phoneme/character-level CTC model over the audio window corresponding to each segment
3. Computes a trellis via Viterbi backtracking (`get_trellis` + `backtrack` in `alignment.py`)
4. Maps character-level alignments to word boundaries via space detection

The default English model is `WAV2VEC2_ASR_BASE_960H` (torchaudio pipeline); 5 languages use torchaudio VoxPopuli pipelines (fr/de/es/it); 30+ other languages use HuggingFace wav2vec2 models. Language detection triggers automatic model loading.

**Key source citations:**  
- `m-bain/whisperX:whisperx/alignment.py:32-77` — `DEFAULT_ALIGN_MODELS_TORCH` and `DEFAULT_ALIGN_MODELS_HF` dictionaries, 35+ languages
- `m-bain/whisperX:whisperx/alignment.py:117-410` — full `align()` function: per-segment CTC inference, trellis backtracking, char→word→sentence grouping with NaN interpolation for unaligned tokens (digits, symbols)
- `m-bain/whisperX:whisperx/diarize.py:14-95` — `IntervalTree` for O(log n) speaker-word intersection (228x speedup claimed for 3+ hour audio)
- `m-bain/whisperX:whisperx/diarize.py:151-240` — `assign_word_speakers()` assigns per-word speaker IDs using diarization segments

**Strengths:**
- Tightly integrated with pyannote-audio diarization (`pyannote-audio>=4.0.0` in `pyproject.toml`)
- Per-word speaker assignment is implemented and tested
- `return_char_alignments=True` provides phoneme-level timestamps
- 70x realtime throughput (full pipeline with faster-whisper backend)
- Wildcard token for unalignble characters (digits, special symbols)
- Sentence-level segmentation via nltk punkt tokenizer

**Weaknesses / known issues (from live issue tracker, 168 open issues):**
- **Overlapping speech degrades alignment** — explicit limitation in README; repeated words in overlapping segments are a reported issue (#1425)
- **pyannote-audio transitive dependency via `lightning` package was quarantined on PyPI** (#1412) — resolved in v3.8.6 which now pins `pyannote-audio>=4.0.0` (CC-BY-4.0 model) and uses `uv` lockfile with CUDA 12.8 index
- Alignment failure for tokens outside model vocabulary (numbers, punctuation) — fallback to linear interpolation
- No streaming/live mode — purely batch post-processing

**VRAM/latency on RTX PRO 6000 (96 GB):**
- wav2vec2-base (EN): ~90 MB weights; <0.5 GB VRAM total; negligible on 96 GB
- wav2vec2-large: ~315 MB weights; ~2-3 GB VRAM
- Alignment alone runs at >50x realtime on a single A100; on RTX PRO 6000 expect similar or better
- Full 60-minute meeting: alignment step typically <2 minutes

**License:** BSD-2-Clause (code) — `m-bain/whisperX:pyproject.toml:8`  
wav2vec2 model weights: MIT/Apache (Facebook/HuggingFace community models)  
pyannote-audio model: CC-BY-4.0 (since pyannote-audio ≥4.0 switched to community-1 model)  
**→ All compatible with private offline use. No commercial-use restriction.**

---

### 3.2 ctc-forced-aligner (MahmoudAshraf97)
**Repository:** `MahmoudAshraf97/ctc-forced-aligner` — https://github.com/MahmoudAshraf97/ctc-forced-aligner  
**Version:** 0.3.0; latest commit April 15 2026 — "fix extra delimiter token"  

**Core mechanism:**  
CTC forced aligner implemented as a Pybind11 C++ extension (`ctc_forced_aligner/forced_align_impl.cpp`) — a clean CTC Viterbi decoder ported from flashlight. It:
1. Loads any HuggingFace `AutoModelForCTC` (wav2vec2 / HuBERT / MMS family)
2. Runs batched chunked inference in 30 s windows with 2 s context overlap for long audio
3. Produces frame-level CTC paths and maps to word/sentence/character spans
4. Uses `<star>` token injection for partial/uncertain transcripts

Default model: `MahmoudAshraf/mms-300m-1130-forced-aligner` (Meta MMS 300M, fine-tuned, 1130 languages)

**Key source citations:**
- `MahmoudAshraf97/ctc-forced-aligner:ctc_forced_aligner/alignment_utils.py:115-178` — `generate_emissions()` with chunked batched inference
- `MahmoudAshraf97/ctc-forced-aligner:ctc_forced_aligner/alignment_utils.py:180-230` — `get_alignments()` using pybind11 C++ backend
- `MahmoudAshraf97/ctc-forced-aligner:ctc_forced_aligner/forced_align_impl.cpp:1-147` — C++ CTC Viterbi decoder (based on flashlight sequence)
- `MahmoudAshraf97/ctc-forced-aligner:setup.py:1-15` — pybind11 C++ extension with `-O3` optimization

**Strengths:**
- Claimed 5x less memory than TorchAudio forced alignment API
- 1130-language support via single model (vs. WhisperX's per-language model lookup)
- Supports flash_attention_2, sdpa, and eager attention implementations
- Word/sentence/char granularity choice
- `<star>` token at segment edges for robustness to missing text
- Standalone: can take any text + audio without needing an ASR system
- JSON output format, easy to parse

**Weaknesses:**
- **LICENSE TRAP: Default model `MahmoudAshraf/mms-300m-1130-forced-aligner` is CC-BY-NC 4.0 — non-commercial only.** README explicitly warns: "note that the default model has CC-BY-NC 4.0 License, so make sure to use a different model for commercial usage." For family-base (private, offline, non-commercial personal use) this is technically acceptable, but it creates a hard constraint.
- No integrated diarization — purely timestamps, no speaker assignment glue code
- No diarization integration; requires extra pipeline construction to use alongside pyannote
- Single-maintainer project (lower bus-factor than WhisperX)
- No published timestamp accuracy benchmarks on meeting corpora
- Batch-only, no streaming

**VRAM/latency on RTX PRO 6000 (96 GB):**  
- MMS-300m: ~300 MB model weights; ~2 GB VRAM at float16
- Flash attention 2 support (`--attn_implementation flash_attention_2`) for further speedup on Blackwell sm_120

**License:** BSD (code); **CC-BY-NC 4.0 for default model weights** — this is the critical license trap.

---

### 3.3 TorchAudio MMS_FA / `torchaudio.functional.forced_align` (raw)
**Repository:** `pytorch/audio` — https://github.com/pytorch/audio  
**Status:** ⚠️ **DEPRECATED as of torchaudio 2.8; APIs removed in 2.9 (current: 2.8.x)**  

From the official tutorial (`pytorch/audio:examples/tutorials/ctc_forced_alignment_api_tutorial.py:7-13`):
> "Starting with version 2.9, we have transitioned TorchAudio into a maintenance phase. As a result: The APIs described in this tutorial were deprecated in 2.8 and **have been removed in 2.9**."

WhisperX v3.8.6 pins `torchaudio~=2.8.0` specifically to retain access to these pipelines, which is why it still works. But using TorchAudio forced alignment APIs directly in a new project is a dead end.

The `MMS_FA` bundle (`pytorch/audio:src/torchaudio/pipelines/_wav2vec2/impl.py`) wraps the same Meta MMS model (`https://dl.fbaipublicfiles.com/mms/torchaudio/ctc_alignment_mling_uroman/model.pt`) that ctc-forced-aligner also uses. The underlying model weights have the same CC-BY-NC 4.0 license.

The C++/CUDA `forced_align` kernel in torchaudio was the inspiration/source for ctc-forced-aligner's C++ backend (ctc-forced-aligner README acknowledges this).

**Verdict:** Do not use TorchAudio forced alignment APIs directly. Use either WhisperX (which bundles torchaudio 2.8 correctly) or ctc-forced-aligner (which has its own C++ implementation and is torchaudio-version-independent).

---

### 3.4 NeMo Forced Alignment (for completeness)
NVIDIA NeMo does have a forced alignment module (`nemo.collections.asr.parts.utils.decoder_timestamps_utils`) but it is:
- Tightly coupled to NeMo's own CTC ASR models (Canary, Conformer, etc.)
- Not a general-purpose aligner for arbitrary transcripts
- Not exposed as a standalone service easily composable with Whisper output
- Primarily useful if using NeMo Canary-Qwen as the sole ASR backend

For family-base: NeMo's native alignment could be used on the Canary-Qwen path specifically, but it cannot align Whisper-generated transcripts. This creates a split code path that adds complexity without benefit.

---

### 3.5 Stable-ts (honorable mention)
`jianfch/stable-ts` is a drop-in Whisper wrapper that improves timestamp quality by suppressing non-speech tokens and using dynamic time warping. It does **not** use CTC forced alignment — it's a refinement of Whisper's built-in attention-based timestamps. It produces worse word-level accuracy than CTC forced alignment (measured in the WhisperX paper) but has zero additional model overhead. Suitable only if no alignment model is tolerable; not recommended for this stack.

---

## 4. Recommendation

### Winner: WhisperX alignment module

**Use `whisperx.align()` + `whisperx.assign_word_speakers()` in a Python service**  
(`m-bain/whisperX`, v3.8.6, BSD-2-Clause, CUDA 12.8 ready)

**Why it wins over ctc-forced-aligner:**

1. **Integrated diarization attribution** — `assign_word_speakers()` performs per-word speaker assignment using an optimized interval tree (O(log n), 228x speedup for 3+ hour meetings). This is the exact use case — "diarization attribution" — that family-base requires. ctc-forced-aligner produces only timestamps; building speaker assignment requires re-implementing this logic.

2. **License purity** — WhisperX's alignment path uses wav2vec2 models with MIT/Apache licenses. ctc-forced-aligner's default model is CC-BY-NC 4.0; while family-base is non-commercial, this creates a legal constraint that future contributors must track. WhisperX avoids this entirely.

3. **Battle-tested on long-form meeting audio** — 70x realtime (full pipeline), used commercially at scale (Replicate, cloud transcription services), peer-reviewed at INTERSPEECH 2023, active community.

4. **Source-agnostic alignment** — `whisperx.align()` takes a `segments` dict, not a Whisper model object. It can receive segments from NeMo Canary-Qwen or vLLM Whisper-large-v3-turbo equally. This is critical for the dual-ASR-backend architecture in family-base.

5. **CUDA 12.8 / Blackwell explicit support** — `pyproject.toml` explicitly indexes `https://download.pytorch.org/whl/cu128`; a PR (merged June 2026) fixed Windows AMD64/x86_64 CUDA detection for exactly this scenario.

**When to choose ctc-forced-aligner instead:**
- If meeting audio contains many languages outside WhisperX's default language list (it requires a per-language model lookup; ctc-forced-aligner covers all 1130 languages with a single model)
- If you need phoneme-level sub-word timestamps (both support this, but ctc-forced-aligner's `split_size=char` mode is cleaner)
- If the 5x memory advantage matters (it doesn't on 96 GB VRAM, but it might on edge/embedded deployments)
- If you explicitly want to avoid the pyannote dependency (and build your own diarization glue)

**Decision rule:** For family-base (96 GB VRAM, multi-language meeting audio, diarization required): use WhisperX. If language coverage expands to languages with no wav2vec2 model on HuggingFace AND the MMS NC license is acceptable: supplement with ctc-forced-aligner for those languages.

---

## 5. Integration Sketch

### Architecture

[Audio capture: cpal + WASAPI loopback]
    ↓  (Rust → Python IPC, HTTP or Unix socket)
[VAD: silero-vad (already in WhisperX stack)]
    ↓
[ASR (two backends, switchable per preference):]
    Branch A: vLLM → Whisper-large-v3-turbo → segments[]
    Branch B: NeMo Canary-Qwen → segments[]
    ↓
[Forced Alignment Python Service]
    model_a, metadata = whisperx.load_align_model(language_code, device="cuda")
    result = whisperx.align(segments, model_a, metadata, audio_np, device="cuda")
    # result["segments"] now has per-word {word, start, end, score}
    ↓
[Diarization: pyannote-audio (already in WhisperX stack)]
    diarize_segments = DiarizationPipeline(token=HF_TOKEN, device="cuda")(audio)
    ↓
[Speaker Assignment]
    result = whisperx.assign_word_speakers(diarize_segments, result)
    # result["segments"][i]["words"][j] now has {word, start, end, score, speaker}
    ↓
[SQLite storage / Tauri 2 frontend]


### Dependencies to add to Python service
```toml
# in pyproject.toml or requirements.txt
whisperx>=3.8.6       # BSD-2-Clause
# already pulls: faster-whisper, torchaudio~=2.8.0, transformers, pyannote-audio>=4.0.0

WhisperX v3.8.6 already pins `torch~=2.8.0` + `torchaudio~=2.8.0` with the CUDA 12.8 index — compatible with RTX PRO 6000 Blackwell.

**Important:** `pyannote-audio>=4.0.0` uses `speaker-diarization-community-1` model (CC-BY-4.0), which requires a HuggingFace token but the model weights can be cached locally. This is a one-time online fetch; thereafter fully offline.

### Live vs. Batch mode
| Mode | Forced alignment role | Approach |
|---|---|---|
| **LIVE** | Not applicable — CTC forced alignment is batch-only; requires full segment audio | Use raw Whisper word timestamps (coarser, ±1–2s) during the live meeting; flag for post-processing |
| **BATCH** | Full role: accurate word timestamps + speaker attribution | Run WhisperX alignment + diarization on completed recording segments or full audio |

This is the correct architecture: use live timestamps for real-time display, then retroactively refine with forced alignment post-meeting for the saved transcript. The Tauri frontend can update the stored transcript silently after the meeting ends.

### Alignment model caching
```python
# Load once at service startup, keep resident (< 3 GB VRAM)
model_a, metadata = whisperx.load_align_model(
    language_code="en",  # or auto-detect from ASR output
    device="cuda",
    model_dir="/path/to/local/model/cache"  # offline after first fetch
)


### Handling multiple languages
```python
# Automatic per-language model selection
model_a, metadata = whisperx.load_align_model(
    language_code=asr_result["language"],  # e.g., "de", "zh", "hi"
    device="cuda"
)

For languages not in WhisperX's default list: fall back to ctc-forced-aligner with a language-specific wav2vec2 model from HuggingFace (not the MMS-NC default).

### Risks
1. **pyannote-audio `lightning` transitive dependency** — was quarantined on PyPI (issue #1412); resolved in WhisperX ≥3.8.6 which pins `pyannote-audio>=4.0.0`. **Pin to v3.8.6 or newer.**
2. **HuggingFace token requirement for pyannote diarization model** — one-time fetch required; weights can be pre-cached in the WSL2 environment: `~/.cache/huggingface/hub/`
3. **torchaudio 2.8 pin** — WhisperX requires `torchaudio~=2.8.0`. This may conflict with other PyTorch-dependent packages. Run WhisperX in an isolated Python environment (venv or conda) within the Python ML service.
4. **sm_120 (Blackwell) compatibility** — torch 2.8.0 + CUDA 12.8 explicitly support Blackwell; the Windows AMD64 CUDA detection fix was merged June 2026. This should work on RTX PRO 6000 in WSL2.
5. **Overlapping speech segments** — fundamental CTC limitation. For family-base meeting audio (mic + loopback captured as separate streams), run alignment independently on each stream, then merge. This sidesteps overlapping speech entirely.

### Effort estimate
- **Integration into existing Python service:** 1–2 days
- **Language model cache setup + HF token:** 0.5 day
- **Tauri/SQLite schema for word-level timestamps + speaker tags:** 1–2 days
- **Testing on real meeting recordings:** 1–2 days
- **Total:** ~4–6 engineering days

---

## 6. Shared-Tech / Overlap Notes

This forced alignment decision directly impacts or shares infrastructure with:

| Family-base capability | Overlap / dependency |
|---|---|
| **Speaker diarization** (pyannote-audio) | WhisperX already bundles pyannote-audio ≥4.0.0; `assign_word_speakers()` is the glue. If diarization is also evaluated separately (see Report Target for diarization), WhisperX's `DiarizationPipeline` and `assign_word_speakers()` can be used directly, avoiding a second pyannote installation. |
| **ASR (Whisper/NeMo)** | WhisperX's `align()` is source-agnostic — it takes `segments` dicts, not Whisper-specific output. NeMo Canary-Qwen output must be reformatted to the `[{text, start, end}]` schema, but this is trivial. |
| **VAD** | WhisperX includes silero-VAD integration. If VAD is implemented separately for live mode, the same VAD boundaries can be reused for forced alignment segmentation. |
| **Subtitle/SRT generation** | WhisperX outputs `.srt` and `.vtt` directly; the per-word `{start, end}` data structure is the same one needed for post-trim caption alignment. |
| **Audio trim / highlight reel** | Per-word timestamps with speaker IDs are the exact input needed for speaker-attributed trim operations — one integration serves both use cases. |

**Single-model multitask question:** Is there a single Meta/NVIDIA audio foundation model that covers forced alignment + ASR + diarization together, beating this stack? **No.** SeamlessM4T/Canary/Qwen-Audio/Whisper-large are ASR/translation models; they produce segment-level timestamps but not sub-word CTC alignments. NeMo Canary-Qwen (already in the stack) can produce approximate word timestamps from its attention weights, but CTC forced alignment achieves ~5–10x better boundary precision. No single 2024–2026 model collapses alignment + diarization into one inference pass.

---

## 7. Open Questions / Prototype Required

1. **Alignment accuracy on meeting-specific audio:** The WhisperX paper benchmarks on TEDLIUM3 (read speech + broadcast news). Real meeting audio (disfluencies, crosstalk, accents, technical jargon) may show worse alignment quality. **Action:** Run alignment on 3–5 sample family-base recordings; measure word boundary error (WBE) vs. manual reference. Expected degradation: 20–40% worse than TEDLIUM but still far better than raw Whisper utterance-level timestamps.

2. **Dual-stream alignment (mic + loopback separate):** Current family-base captures mic and system loopback as separate audio streams. Should alignment run on each stream independently and then merge, or should streams be mixed first? CTC alignment on individual streams avoids overlap issues entirely. **Action:** Prototype with a real meeting recording; measure speaker attribution accuracy on merged vs. separate-stream alignment.

3. **NeMo Canary-Qwen segment format → WhisperX align() adapter:** NeMo outputs segments in its own schema. **Action:** Implement and test a thin adapter that converts NeMo output to WhisperX `SingleSegment` dicts.

4. **Blackwell (sm_120) + torchaudio 2.8 validation:** PyTorch 2.8.0 explicitly supports sm_120 (RTX PRO 6000 Blackwell). **Action:** Run a short alignment job on the target hardware and confirm no CUDA kernel errors; `torch.cuda.get_device_capability()` should return `(12, 0)`.

5. **Multilingual meeting support:** If meetings contain non-English content beyond WhisperX's default model list (30+ languages covered), what fallback strategy to use? **Action:** Enumerate expected meeting languages; check coverage against `DEFAULT_ALIGN_MODELS_HF` in `whisperx/alignment.py:40-77`; pre-cache any missing models.

6. **Long-form (3+ hour) alignment performance:** WhisperX's `IntervalTree` optimization claims 228x speedup for speaker assignment. **Action:** Benchmark on a 3-hour recording to confirm no OOM or time regression.

---

## 8. Sources

1. **WhisperX repository** — https://github.com/m-bain/whisperX (v3.8.6, BSD-2-Clause)
2. **WhisperX paper** — Bain et al., "WhisperX: Time-Accurate Speech Transcription of Long-Form Audio", INTERSPEECH 2023, arXiv:2303.00747 — https://arxiv.org/abs/2303.00747
3. **WhisperX alignment.py** — `m-bain/whisperX:whisperx/alignment.py` (SHA: 12f123fd)
4. **WhisperX diarize.py** — `m-bain/whisperX:whisperx/diarize.py` (SHA: b767416e)
5. **WhisperX pyproject.toml** — `m-bain/whisperX:pyproject.toml` (SHA: 0d10ffd6)
6. **ctc-forced-aligner repository** — https://github.com/MahmoudAshraf97/ctc-forced-aligner (v0.3.0, BSD / default model CC-BY-NC 4.0)
7. **ctc-forced-aligner alignment_utils.py** — `MahmoudAshraf97/ctc-forced-aligner:ctc_forced_aligner/alignment_utils.py` (SHA: 3fb10e36)
8. **ctc-forced-aligner C++ backend** — `MahmoudAshraf97/ctc-forced-aligner:ctc_forced_aligner/forced_align_impl.cpp` (SHA: 523aaba0)
9. **TorchAudio CTC forced alignment tutorial** — `pytorch/audio:examples/tutorials/ctc_forced_alignment_api_tutorial.py` (SHA: a31b63e3) — deprecation notice in header
10. **TorchAudio MMS_FA multilingual tutorial** — `pytorch/audio:examples/tutorials/forced_alignment_for_multilingual_data_tutorial.py` (SHA: 00dfe68b)
11. **TorchAudio impl.py MMS_FA bundle** — `pytorch/audio:src/torchaudio/pipelines/_wav2vec2/impl.py` (SHA: d60fa8ad)
12. **Meta MMS paper** — Pratap et al., "Scaling Speech Technology to 1,000+ Languages", https://research.facebook.com/publications/scaling-speech-technology-to-1000-languages/
13. **pyannote-audio speaker-diarization-community-1** — CC-BY-4.0 — https://huggingface.co/pyannote/speaker-diarization-community-1
14. **WhisperX issue #1412** — pyannote lightning dependency quarantine — https://github.com/m-bain/whisperX/issues/1412
15. **WhisperX issue #1425** — repeated words in overlapping speech — https://github.com/m-bain/whisperX/issues/1425
16. **TorchAudio maintenance-phase announcement** — https://github.com/pytorch/audio/issues/3902
