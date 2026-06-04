## RESEARCH FINDINGS — Accent Conversion / Normalization

### Summary

Accent conversion (modifying a speaker's accent while preserving voice identity and content) is the most research-incomplete item in the family-base build. No open-source system today delivers true identity-preserving accent conversion at production quality. The best available approximation is **Seed-VC v2** (arXiv:2411.09943, GPL-3.0), which explicitly supports accent + style conversion via an autoregressive token prediction layer on top of a Consistency Flow Matching vocoder. **kNN-VC** is a cleaner codebase with better benchmark numbers but does NOT perform accent conversion — only speaker-voice conversion. SeamlessM4T/SeamlessExpressive is the only "foundation model" with cross-lingual expressivity transfer but is (a) non-commercial only (CC-BY-NC-4.0) and (b) a speech-to-speech translator, not an accent normalizer within a single language. For the meeting-assistant use case the most practical near-term implementation is Seed-VC v2 in batch mode; real-time accent conversion remains genuinely experimental.

---


Report: Accent Conversion / Normalization
Target: family-base (local, offline, privacy-first desktop meeting assistant)
Hardware: NVIDIA RTX PRO 6000 Blackwell, 96 GB VRAM, WSL2 Ubuntu
Date: 2025-06


---

# Accent Conversion / Normalization — Decision Report

## 1. TL;DR

**Winner: Seed-VC v2** (`Plachtaa/seed-vc`, arXiv:2411.09943) — the only open-source, locally-runnable system with an explicit accent/style conversion mode (`--convert-style true`) and active maintenance; run as a batch Python service post-meeting. Real accent conversion (L2→L1 while preserving speaker identity) remains research-incomplete; every other system is either voice-identity cloning (not accent), non-commercial only, or cloud-only. **Do not expect production fidelity; prototype before committing to this feature.**

---

## 2. Decision Matrix

| Candidate | Quality / Benchmarks | Local/Offline on RTX 6000 | License | Maturity | Integration Effort | Robustness on Meeting Audio |
|---|---|---|---|---|---|---|
| **Seed-VC v2** (arXiv:2411.09943) | SECS=0.8676, WER=11.99%, CER=2.92% on LibriTTS-test-clean (zero-shot VC); accent-specific benchmarks not published for v2 yet | ✅ 157M params (67M CFM + 90M AR), ~3–5 GB VRAM; batch ~25 diffusion steps; real-time mode (v1 tiny 25M) ~300ms algo latency | **GPL-3.0** (private local use OK, copyleft if distributed) | Active (last commit Apr 2025, 2024–2025 releases) | Python service; no Rust bindings; straightforward `inference_v2.py` CLI; needs HuBERT-large + Whisper-small as encoders | Moderate — designed for clean reference audio; tested on LibriTTS-clean; heavy noise or overlap will degrade ASTRAL quantizer |
| **kNN-VC** (Interspeech 2023, arXiv:2305.18975) | WER=6.29%, CER=2.34%, EER=35.73% on LibriSpeech dev-clean (voice conversion, NOT accent conversion) | ✅ WavLM-Large (317M) + HiFiGAN; ~4–6 GB VRAM; batch-only; no streaming | **MIT** | Stable (last commit 2025-05-24 minor); research project | 3 deps (torch, torchaudio, numpy); `torch.hub` load; simple API | Good speech quality on clean audio; does NOT change accent, only speaker voice |
| **OpenVoice V2** (arXiv:2312.01479) | Zero-shot voice cloning SECS~0.75; accent = base-speaker selection (not voice-to-voice accent conversion) | ✅ VITS-based, small (~100M); ~2 GB VRAM | **MIT** | Active (36K stars; Apr 2024 v2 release) | Python pip install; works as TTS only (needs text input, not audio-in) | Only relevant for TTS synthesis — cannot convert recorded meeting audio |
| **SeamlessM4T v2 / SeamlessExpressive** (arXiv:2308.11596, 2312.05187) | ASR-BLEU 27–42 across lang pairs; Vocal Style Sim 0.21–0.29; NOT an accent conversion benchmark | ✅ ~2.3B params; ~10–12 GB VRAM; batch and streaming modes | **CC-BY-NC-4.0 — NON-COMMERCIAL ONLY** | Active (Meta, NeurIPS 2023) | Python `fairseq2` + `seamless_communication`; Linux x86-64 pre-built wheels | Wrong task: cross-lingual S2ST, not same-language accent normalization; cannot strip accent |
| **RVC v2** (ContentVec + VITS + HiFiGAN) | ~SECS 0.73–0.78 per community evals; no published accent benchmark | ✅ ~1–3 GB VRAM; real-time via WebUI; needs ~5–10 min target-speaker audio | **MIT** | Community (RVC-Project); widely used, no formal paper | Python WebUI; simple REST; no accent conversion — speaker voice clone only | Widely tested on clean speech; real-time tested; noise pre-filtering recommended |
| **PPG-VC** (TASLP 2021, any-to-many) | MOS ~3.8 naturalness, ~3.6 similarity on VCTK (in-domain, 2021); outdated by today's standards | ✅ Conformer PPG + HiFiGAN; ~2 GB VRAM | **MIT** | Unmaintained (2021–2023) | Python; `liusongxiang/ppg-vc`; manual setup | Research project only; not tested on noisy meeting audio |

---

## 3. Per-Candidate Notes

### 3.1 Seed-VC v2 — **RECOMMENDED**

**Repo:** `Plachtaa/seed-vc` — https://github.com/Plachtaa/seed-vc  
**Paper:** arXiv:2411.09943 (Nov 2024)

**Architecture:** v2 uses a two-stage pipeline:
1. **ASTRAL quantizer** (HuBERT-large → ConvNeXtV2 bottleneck → Binary Spherical Quantization at 32 codes) extracts speaker-disentangled linguistic tokens — explicitly trained to discard speaker traits (`Plachtaa/ASTRAL-quantization`)  
2. **AR Transformer** (12-layer, 768-dim; 90M params) predicts style/accent tokens autoregressively from the reference audio's style embedding (CAMPPlus speaker encoder)  
3. **CFM Diffusion model** (DiT, 13-layer, 512-dim; 67M params) generates mel-spectrogram conditioned on ASTRAL tokens + AR style tokens  
4. **BigVGAN v2** vocoder (`nvidia/bigvgan_v2_22khz_80band_256x`) produces 22 kHz audio

The `--convert-style true` flag activates the AR model which explicitly targets "accent & emotion conversion" (`inference_v2.py:69`). Without this flag, only timbre (voice identity) is converted — essentially the same as RVC.

**Benchmarks (measured, LibriTTS-test-clean, zero-shot):**
- SECS: 0.8676 (vs OpenVoice 0.7547, CosyVoice 0.8440) ← speaker similarity
- WER: 11.99% (vs OpenVoice 15.46%, GT 8.02%) ← content preservation
- CER: 2.92%

⚠️ **Critical gap:** No published accent-specific evaluation (e.g., L2-ARCTIC, ACCENT-DB). The WER improvement over other VC systems is evidence of better content preservation, not direct evidence of better accent conversion. The AR model's accent conversion quality is asserted but not benchmarked on standard accent datasets.

**VRAM:** ~3–5 GB for v2 (67M + 90M params in fp16). On 96 GB this is trivial. The v1 tiny (25M XLSR-based) can run real-time at ~300ms end-to-end latency.

**License:** GPL-3.0. For private local use (family-base is not distributed), GPL-3.0 imposes no copyleft obligations. However, if family-base is ever distributed, the entire product must be GPL-3.0. Flag this for legal review before any public release.

**Maintenance:** Last commits April 2025; v2 model released Q1 2025. Active single-developer project (Plachtaa / liusongting07@gmail.com). No corporate backing — bus-factor risk.

**Weaknesses:**
- No identity-preserving accent conversion: the output sounds like the reference speaker, not the source speaker with a changed accent
- Requires a clean reference audio clip in the "target accent" (e.g., native American English speaker)
- v2 accent conversion quality not peer-reviewed or independently benchmarked as of mid-2025
- GPL-3.0 complicates any future distribution

---

### 3.2 kNN-VC — STRONG RUNNER-UP (voice quality, NOT accent)

**Repo:** `bshall/knn-vc` — https://github.com/bshall/knn-vc  
**Paper:** Baas et al., Interspeech 2023, arXiv:2305.18975

**Architecture:** WavLM-Large (layer 6 features) → kNN matching against reference speaker's features → HiFiGAN vocoder. The kNN step is non-parametric — no training needed beyond the vocoder.

**Benchmarks (measured, LibriSpeech dev-clean, any-to-any VC):**
- WER: 6.29%, CER: 2.34% — better than Seed-VC in content preservation
- EER: 35.73% — speaker similarity (lower WER is the key metric for meeting use)

**Important caveat:** kNN-VC performs **speaker voice conversion only** — it changes who the voice sounds like, not the accent. The WavLM features at layer 6 capture acoustic properties beyond pure phonemes (they retain some prosodic/accent-correlated information), so accent incidentally changes somewhat when converting to a native-accent reference speaker. But this is a side-effect, not a feature.

**License:** MIT  
**VRAM:** WavLM-Large ~4 GB in fp16; HiFiGAN negligible. Total ~4–5 GB.  
**Mode:** Batch only (kNN over reference set must be precomputed).

**Choose kNN-VC instead of Seed-VC v2 if:** You want robust, MIT-licensed voice conversion with minimal dependencies (3 packages) and don't need explicit accent/style control — e.g., you just want to normalize a speaker's voice quality, not specifically change their accent pattern.

---

### 3.3 OpenVoice V2 — OUT OF SCOPE FOR THIS TASK

**Repo:** `myshell-ai/OpenVoice` — https://github.com/myshell-ai/OpenVoice  
**Paper:** arXiv:2312.01479

OpenVoice is a **TTS system** that clones tone color from a reference clip and can generate speech in different pre-baked "accent" styles (American, British, Indian, Australian, Spanish English). It requires **text input** and generates speech from scratch. It cannot process recorded meeting audio (audio-in → audio-out). Excluded from meeting audio pipeline.

---

### 3.4 SeamlessM4T / SeamlessExpressive — EXCLUDED (wrong task + license)

**Repo:** `facebookresearch/seamless_communication` — https://github.com/facebookresearch/seamless_communication  
**Papers:** SeamlessM4T arXiv:2308.11596; Seamless arXiv:2312.05187

SeamlessExpressive preserves prosody and voice style during **cross-lingual speech-to-speech translation** (e.g., English speech → Spanish speech, keeping the speaker's voice style). It does NOT perform within-language accent normalization. Its license is **CC-BY-NC-4.0 (non-commercial only)** — confirmed from `facebookresearch/seamless_communication:LICENSE`. This is a hard disqualifier for any deployment.

SeamlessStreaming supports live ASR + translation but is a 2.3B parameter model requiring ~10–12 GB VRAM and operates as a translation system, not accent normalizer.

**Verdict:** Wrong task, wrong license. Mentioned only to exclude.

---

### 3.5 RVC v2 (Retrieval-based Voice Conversion) — EXCLUDED (no accent conversion)

**Repo:** `RVC-Project/Retrieval-based-Voice-Conversion-WebUI`  
**Architecture:** ContentVec (HuBERT-based) + VITS + HiFiGAN + RMVPE pitch extractor

RVC is the most widely deployed voice conversion tool in the community. It requires 5–30 minutes of target-speaker audio to fine-tune a speaker model, then converts any audio to that speaker's voice in real-time (~20–30 ms at standard settings). Like kNN-VC, RVC changes voice identity — it does not explicitly convert accent. MIT licensed. Excluded from primary recommendation because Seed-VC v2 benchmarks exceed RVC on all metrics and includes accent conversion capability.

---

### 3.6 Academic Accent Conversion Research (No Production Code)

The research field has several accent conversion papers (2022–2024) that are worth noting but have no production-ready public implementations:

- **AccentVC** (Kim et al., INTERSPEECH 2023): Disentangled accent conversion using HuBERT + accent-specific bottleneck; L2-ARCTIC evaluations. No public repo found.
- **UUVC / VAE-based accent conversion** (multiple groups): VAE disentanglement of content, accent, and speaker; evaluated on ARCTIC/L2-ARCTIC. None have production-grade implementations.
- **Neural Accent Conversion via CycleGAN / StarGAN**: Older approach (2020–2022); superseded by flow-matching methods.

The L2-ARCTIC corpus (Zhao et al., 2018; 24 L2 speakers, 6 native languages) is the standard eval set for accent conversion research. **No current public system reports L2-ARCTIC accent similarity + WER jointly in a production-usable form.**

---

## 4. Recommendation

### Winner: Seed-VC v2 (`--convert-style true`, batch mode)

**Why it beats kNN-VC (the runner-up):** kNN-VC has no accent conversion capability whatsoever — its explicit design is voice identity conversion. Seed-VC v2's autoregressive style-token module (`modules/v2/ar.py`) is the only open-source component specifically designed to predict and transfer accent/style from a reference speaker. Speaker similarity (SECS 0.8676 vs kNN-VC EER-based equivalent) and WER (11.99% vs 6.29%) are in the same order of magnitude; the gap in raw WER is a reasonable tradeoff for gaining explicit accent conditioning.

**The honest caveat:** Seed-VC v2 performs "voice + accent + style conversion toward a reference speaker." It does **not** perform "accent-only conversion preserving the source speaker's identity." If the meeting participant is a non-native English speaker and you convert their speech toward a native English reference, the result will sound like the reference speaker, not like them with a different accent. This changes speaker attribution (diarization labels remain correct, but audio for playback will be misleading).

**Decision rule:**

| Goal | Best choice |
|---|---|
| Normalize heavily accented speech **for better ASR accuracy** | ⚠️ Skip accent conversion entirely — Canary-Qwen and Whisper-large-v3-turbo are already highly accent-robust; voice conversion artifacts may hurt WER more than accent helps |
| Generate cleaner **playback audio** of accented speakers (with identity loss acceptable) | Seed-VC v2, batch, `--convert-style true`, reference = neutral native English |
| Preserve speaker identity while only changing accent | ❌ Not possible with any current open-source system |
| Voice conversion without accent (e.g., anonymization) | kNN-VC (MIT, simpler) or Seed-VC v1 (better quality) |

**Use kNN-VC instead** if: you want voice anonymization (not accent conversion), need MIT license for future distribution, and prefer minimal dependencies. kNN-VC is architecturally cleaner and its 2023 Interspeech paper is peer-reviewed.

---

## 5. Integration Sketch

### 5.1 Batch Mode (recommended, post-meeting)


[Meeting ends]
     ↓
[Per-speaker audio segments] (from diarization output)
     ↓
[accent_vc_service.py] — Python WSL2 service
   ├─ load Seed-VC v2 wrapper (HuBERT-large + ASTRAL + CFM + AR + BigVGAN)
   ├─ for each segment > 3s:
   │    inference_v2.py \
   │       --source <segment.wav> \
   │       --target reference_native_en.wav \
   │       --convert-style true \
   │       --diffusion-steps 30 \
   │       --similarity-cfg-rate 0.7 \
   │       --intelligibility-cfg-rate 0.7
   └─ write normalized_<segment>.wav
     ↓
[Store in SQLite alongside original] (both originals preserved for privacy)
     ↓
[Optional: re-run ASR on normalized audio; compare WER]


**Service design:** Single Python process, expose via localhost HTTP (similar to existing ASR servers). Load models once at startup (~10–15 seconds), then process segments on demand. With 96 GB VRAM the Seed-VC v2 models (≤6 GB) can co-reside with Canary-Qwen, Whisper, and LLM.

**Python dependencies** (`requirements.txt`):

torch>=2.0
torchaudio
hydra-core
omegaconf
soundfile
numpy
transformers  # for HuBERT-large, Whisper-small


### 5.2 Real-time Mode (experimental only)

For real-time, use Seed-VC v1 tiny (25M XLSR-based model, `seed-uvit-tat-xlsr-tiny`):
- Algorithm delay: ~300ms (stated by authors, not independently verified)
- Buffer: 200ms chunks → process → forward to output
- Integration: Rust audio capture (cpal+WASAPI) → shared memory queue → Python WebSocket consumer → Seed-VC v1 → output back to virtual sink

**Risks:** 300ms latency is at the threshold of perceived delay (>200ms is noticeable). Accent conversion quality of v1 tiny is significantly worse than v2 (no `--convert-style` in v1). Do not use for live meetings without pilot testing.

### 5.3 No Rust native integration path

There is no ONNX export for Seed-VC v2 (the AR + CFM pipeline uses dynamic-length generation). Rust integration must go through Python service (HTTP/WebSocket). This is consistent with the existing stack (NeMo, Whisper already run as Python HTTP services).

### 5.4 Reference audio management

The system needs at least one reference audio clip (10–30 seconds, clean, native English) to define the "target accent." Recommended: pre-bundle a high-quality TTS-generated reference clip (from CosyVoice or MeloTTS in standard American English) as the default target. Users should not need to supply this.

---

## 6. Shared-Tech / Overlap Notes

| Component | Already in stack | Shared with this feature |
|---|---|---|
| HuBERT-large | Not explicitly, but WavLM (kNN-VC) is similar; Canary-Qwen ASR uses NeMo encoder | ASTRAL quantizer backbone; can share checkpoint cache |
| Whisper-small encoder | vLLM runs Whisper-large-v3-turbo; Seed-VC v1 uses Whisper-small as content encoder | Separate checkpoint, small size; parallel with existing |
| BigVGAN v2 vocoder (`nvidia/bigvgan_v2_22khz_80band_256x`) | Not in stack | Also useful for TTS synthesis if that feature is added |
| Speaker embeddings (CAMPPlus / resemblyzer) | pyannote diarization uses ECAPA-TDNN speaker embeddings | Partial overlap; different embedding spaces |
| Python HTTP service pattern | ✅ Used for NeMo, Whisper | Direct reuse |

**Composition note:** If diarization (pyannote) is already running to produce per-speaker segments, those segments can be piped directly into the accent VC service without additional preprocessing. The combination `diarization → accent conversion → ASR` creates a clean pipeline for heavily accented multi-speaker meetings.

**Does SeamlessM4T cover this and neighboring tasks?** No. SeamlessM4T covers ASR + cross-lingual translation + S2ST, but its expressive model (SeamlessExpressive) specifically targets prosody preservation in *translation*, not same-language accent conversion. Furthermore, its CC-BY-NC-4.0 license disqualifies it. Do not use SeamlessM4T in this build.

---

## 7. Open Questions / Prototype Needed

1. **Does pre-conversion accent normalization actually improve ASR WER for the target accents?** Run: record 30 sentences from an L2 speaker → convert with Seed-VC v2 → run Canary-Qwen and Whisper-large-v3-turbo → compare WER. If improvement is <5% relative WER, the feature has no practical value for this stack and should be deprioritized.

2. **What is the acceptable latency for batch post-processing?** The full v2 pipeline (30 diffusion steps) on a 30-second segment needs to be benchmarked on the RTX PRO 6000. Expected: 2–5× real-time factor (RTF) = 6–15 seconds per 30s segment. Unverified.

3. **Does `--convert-style true` actually change accent vs just emotion?** The AR model documentation is vague. A controlled test: convert L2 Indian English → reference American English, measure phonological accent distance (e.g., GOPT score or accent classification confidence). Not done.

4. **GPL-3.0 distribution risk:** If family-base is ever distributed publicly, Seed-VC v2's GPL-3.0 license requires the entire product to be GPL-3.0. Legal review required before any public release plans.

5. **Identity-preserving accent conversion:** Monitor `arXiv cs.SD` for 2025 papers on disentangled accent conversion. The field is advancing rapidly (diffusion-based disentanglement papers emerging in 2024–2025). A late 2025 check-in is warranted.

6. **Reference audio selection:** Does the choice of reference speaker significantly affect accent conversion quality? Test with multiple reference speakers (formal broadcaster, neutral TTS voice, etc.) to find the most effective one.

---

## 8. Sources

1. Seed-VC repository: https://github.com/Plachtaa/seed-vc
2. Seed-VC paper: arXiv:2411.09943 — https://arxiv.org/abs/2411.09943
3. Seed-VC EVAL.md (benchmark tables): https://github.com/Plachtaa/seed-vc/blob/main/EVAL.md
4. Seed-VC v2 config: `Plachtaa/seed-vc:configs/v2/vc_wrapper.yaml`
5. ASTRAL quantization: https://github.com/Plachtaa/ASTRAL-quantization
6. kNN-VC repository: https://github.com/bshall/knn-vc
7. kNN-VC paper: Baas et al., Interspeech 2023 — arXiv:2305.18975 — https://www.isca-speech.org/archive/interspeech_2023/baas23_interspeech.html
8. kNN-VC README benchmarks: `bshall/knn-vc:README.md`
9. OpenVoice V2: https://github.com/myshell-ai/OpenVoice
10. OpenVoice paper: arXiv:2312.01479
11. SeamlessM4T: https://github.com/facebookresearch/seamless_communication
12. SeamlessM4T paper: arXiv:2308.11596
13. Seamless (unified model): arXiv:2312.05187
14. SeamlessExpressive README: `facebookresearch/seamless_communication:docs/expressive/README.md`
15. Seamless Communication License (CC-BY-NC-4.0): `facebookresearch/seamless_communication:LICENSE`
16. CosyVoice / Fun-CosyVoice 3.0: https://github.com/FunAudioLLM/CosyVoice — arXiv:2505.17589, arXiv:2412.10117
17. PPG-VC (any-to-many VC): https://github.com/liusongxiang/ppg-vc — Liu et al., IEEE/ACM TASLP 2021
18. RVC (Retrieval-based Voice Conversion): https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI
19. L2-ARCTIC corpus: Zhao et al., INTERSPEECH 2018 (standard accent conversion eval set)
20. BigVGAN v2 vocoder: https://huggingface.co/nvidia/bigvgan_v2_22khz_80band_256x

---

*Report produced by research subagent. All benchmarks cited from primary sources (repo READMEs, EVAL.md, and referenced papers). Accent-specific metrics for Seed-VC v2 could not be independently verified from published benchmarks as of mid-2025 — the accent conversion feature is asserted in the codebase but not evaluated on standard accent datasets (L2-ARCTIC, ACCENT-DB). Flag this gap for the prototype phase.*
