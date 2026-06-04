# Family-Base Meeting Assistant: Consolidated Research Synthesis

## Component Winners Summary

### Target 1
**Two-winner answer (functionally distinct roles):**
- **Noise Suppression (primary):** DeepFilterNet3 — MIT/Apache, 48 kHz native, causal/streaming, ONNX + native Rust (`libdf` crate), ~2M parameters, runs at <1× RTF on CPU, leaving the RTX PRO 6000 fully free for ASR/LLM.
- **Acoustic Echo Cancellation (AEC):** `tonarino/webrtc-audio-processing` (Rust crate wrapping WebRTC AEC3) — the only candidate that performs true algorithmic echo cancellation using the system loopback as reference. It als...

### Target 2
— The Winner

**DTLN-aec (512-unit / ONNX)** for both LIVE and BATCH modes, combined with a **lightweight coherence-based dedup guard** as a complementary second layer.

DTLN-aec is the only open-source, MIT-licensed, locally-runnable model that has verifiable AEC-Challenge benchmark numbers (Overall MOS 3.98 clean, ranked 3rd out of 18 teams at ICASSP 2021, AEC3/WebRTC baseline only achieved 3.68). Its ONNX format eliminates the TF runtime requirement, it runs in <1 ms/frame on any modern x86 C...

### Target 3
**Winner: MossFormer2 (via ClearerVoice-Studio) for BATCH post-meeting separation.**  
It is the only candidate that (a) is purpose-built for speech separation at meeting-quality sample rates, (b) ships an actively-maintained pip package with a three-line numpy API, (c) covers enhancement, separation, AND target-speaker extraction in one install, and (d) posts competitive benchmark numbers as a single unified 16 kHz model — without the quadratic memory blowup of SepFormer, without the wrong-task...

### Target 4
**Winner: NeMo Sortformer-streaming v2.1 (LIVE) + NeMo Sortformer-batch (BATCH) + NeMo TitaNet-Large (embeddings/enrollment) — with pyannote `community-1` as BATCH fallback for >4-speaker meetings, and WeSpeaker ResNet293-LM as optional higher-accuracy enrollment/verification model.**

Rationale in one sentence: Sortformer is already inside NeMo (the existing Canary-Qwen ASR stack), Apache 2.0 licensed, covers both LIVE streaming (AOSC, ~0.48 s latency) and BATCH, and produces speaker-ordered pr...

### Target 5
**Winner: Silero VAD v6 (ONNX) + the `SpeechTimestampsMap` remap design from `SYSTRAN/faster-whisper`.**  
It achieves the best published benchmark numbers on meeting-domain audio (ROC-AUC 0.97 on multi-domain validation, 0.96 on AliMeeting), is MIT-licensed, ships as a 2 MB ONNX file, runs at ~165× real-time on a single CPU thread, has an official Rust example (ONNX Runtime), and is already embedded inside the `faster-whisper` backend the stack already runs — meaning zero additional integration...

### Target 6
**Winner: WhisperX alignment module (wav2vec2-based, m-bain/whisperX v3.8.6)**  
It is the only option that delivers a battle-tested, fully-integrated pipeline from ASR output → accurate word timestamps → pyannote diarization speaker assignment in a single Python package (BSD-2-clause), runs on any NVIDIA GPU, is actively maintained (commit June 2026), and is specifically designed for long-form meeting audio — the exact family-base use case.

---...

### Target 7
**Winner: A staged, layered accuracy pipeline** — Canary-Qwen-2.5b (SALM, BATCH) + Parakeet-TDT-0.6b-v2 (LIVE) as base ASR, augmented by NeMo GPU-accelerated Phrase Boosting (GPU-PB) for meeting-vocabulary biasing, `condition_on_previous_text` + Whisper `initial_prompt` / `hotwords` for rolling context, and a two-pass generative error correction (GEC) step using the already-present local LLM. ROVER and standalone Whispering-LLaMA/HyPoradise GEC models do not justify their added complexity for th...

### Target 8
— The Winner + One-Line Why

**Winner: Qwen2.5-72B-Instruct (INT4/GPTQ) via vLLM with xgrammar-backed guided-decoding + a custom 3-tier hierarchical pipeline (segment → topic → meeting).**

It maximises extraction quality and instruction-following on the structured work-log schema, runs entirely offline in ~40–42 GB VRAM (fits the 96 GB RTX PRO 6000 with ample KV-cache headroom), and vLLM's native `response_format: json_schema` (xgrammar backend) eliminates brittle post-parse steps. All without ...

### Target 9
**Winner: BGE-M3 (embedding) + LanceDB (store+FTS) + RRF hybrid (retrieval)**

BGE-M3's single forward pass yields dense + sparse (lexical weights) + ColBERT multi-vector embeddings simultaneously — this is the only model that natively collapses the BM25+vector hybrid into one inference call without a separate keyword-index pipeline. LanceDB is the only embedded store (no server, Rust+Python native, Apache 2.0) that ships tantivy-BM25 FTS, HNSW vector search, and RRF/cross-encoder reranking in o...

### Target 10
**Two-winner answer (functionally non-overlapping tasks):**

- **Sound-event classification → BEATs_iter3+ (AS2M)**: MIT license, ~0.498 mAP on AudioSet (highest single-model score as of 2023), 16 kHz, ~90M params, ~500 MB VRAM. Deploy as a BATCH Python service; also viable LIVE on 1–2 s windows given the RTX PRO 6000.
- **Emotion classification → emotion2vec+ large**: MIT license, SOTA on IEMOCAP 4-class SER, 9-class output, 70–80 ms per utterance on GPU after warmup (~300 M params, ~1–2 GB VRA...

### Target 11
**Winner: Seed-VC v2** (`Plachtaa/seed-vc`, arXiv:2411.09943) — the only open-source, locally-runnable system with an explicit accent/style conversion mode (`--convert-style true`) and active maintenance; run as a batch Python service post-meeting. Real accent conversion (L2→L1 while preserving speaker identity) remains research-incomplete; every other system is either voice-identity cloning (not accent), non-commercial only, or cloud-only. **Do not expect production fidelity; prototype before c...

### Target 12
**Winner: openWakeWord** — the only option purpose-built for Python desktop/server deployment; integrates Silero VAD and Speex noise suppression natively; runs in <1 ms per 80 ms frame on any x86 CPU, consumes zero VRAM.
**Critical license caveat:** The pre-trained model *weights* are CC-BY-NC-SA 4.0 (non-commercial). The training code is Apache 2.0, so training a custom wake word ("hey family-base") produces fully permissive weights.

---...

### Target 13
**Winner: CSS custom-property density system (Tailwind v4 `@theme` + `data-density` on `<html>`) + shadcn/ui primitives (Accordion, Tooltip/HoverCard, Command/cmdk) + Tauri 2 `WebviewWindowBuilder` mini-window.** This combination is zero-dependency-overhead on the existing stack, fully offline, and covers every listed interaction model without introducing any new framework. The runner-up for full-text transcript search is **FlexSearch** (in-browser) vs **SQLite FTS5** (already available in Rust)...

### Target 14
**Verdict: The specialized stack wins, and cannot be replaced by any single audio foundation model today.**

For tasks #1–#11 of the family-base pipeline, no unified model covers more than two of them (primarily just ASR). Signal-processing tasks (#1 enhancement, #2 AEC, #3 source separation, #4 diarization, #5 VAD, #6 forced alignment) are structurally incompatible with text-output generative models; they require waveform I/O, reference signals, and millisecond-granularity decisions that LLM de...

