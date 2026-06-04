# Report 12: Keyword Spotting / Wake Words (Hands-Free Triggers)
## openWakeWord vs. microWakeWord — Decision-Grade Comparison
**Target system:** family-base (local, offline, privacy-first desktop meeting assistant — Meetily fork)
**Candidates evaluated:** openWakeWord, microWakeWord; Porcupine/Snowboy/Mycroft Precise/NeMo MatchboxNet (evaluated and excluded)
**Compiled:** 2026-06

---

## 1. TL;DR

**Winner: openWakeWord** — the only option purpose-built for Python desktop/server deployment; integrates Silero VAD and Speex noise suppression natively; runs in <1 ms per 80 ms frame on any x86 CPU, consumes zero VRAM.
**Critical license caveat:** The pre-trained model *weights* are CC-BY-NC-SA 4.0 (non-commercial). The training code is Apache 2.0, so training a custom wake word ("hey family-base") produces fully permissive weights.

---

## 2. Decision Matrix

| Criterion | **openWakeWord** | **microWakeWord** |
|---|---|---|
| **Quality / accuracy** | <5% FRR, <0.5 FA/hr (DipCo 5.5h far-field party corpus); ~97.5% on Fluent Speech Commands SLU; beats Porcupine on "Alexa" benchmark. Author-reported; small test sets; caveat noted. | ROC curves published (alexa, hey_jarvis, okay_nabu) but no numeric table. Self-described as "real-world, low FA/FR." Comparable to openWakeWord per upstream comparisons. |
| **Local/offline feasibility** | ✅ Fully local. CPU-only default. <1 ms / 80 ms frame. Pi 3 single core runs 15–20 models in real-time. ONNX CUDAExecutionProvider available but unnecessary. Embedding ~1–2 MB, per-word classifier ~0.4 MB. | ✅ Fully local. TFLite, CPU-only. v2 models 52–60 KB (int8). Inference every 30 ms. Designed for ESP32; trivially fast on x86. |
| **License** | Code: Apache 2.0. **Pre-trained models: CC-BY-NC-SA 4.0 (non-commercial).** Training pipeline: Apache 2.0 → custom models fully permissive. | Code: Apache 2.0. **Pre-trained models (esphome/micro-wake-word-models): Apache 2.0.** Fully permissive. |
| **Maturity & maintenance** | v0.6.0 (2024-02-11); last commit 2025-12-30; 2.3k stars; 107 open issues (training pipeline Colab breakage in 2025–2026 confirmed). Active Home Assistant / Wyoming community. | "Early release" per own README; last commit 2025-12-21; moved kahrendt → OHF-Voice; ESPHome / Nabu Casa backed. Training described as "still very difficult." |
| **Integration effort** | Low. `pip install openwakeword`. 3-line API. ONNX+TFLite. Wyoming TCP server. Docker image. C++ wrapper. Streams 16-bit 16 kHz PCM in 80 ms frames. | Medium. `pip install microwakeword`. Python via `ai_edge_litert`. No Wyoming server (MCU-focused). No desktop integration examples. Custom shim needed for streaming pipeline. |
| **Robustness on real meeting audio** | Good. DipCo far-field corpus test. Handles whispered speech, variable speed, phrase variation. Silero VAD + Speex gate FA. Custom verifier models for speaker adaptation. English-only. | Limited desktop evidence. PCAN+AGC preprocessor designed for ESP32 mics; behavior on PC loopback audio uncharacterized. No verifier models. English-only. |

---

## 3. Per-Candidate Notes

### 3.1 openWakeWord (`dscripka/openWakeWord`)

**Repository:** https://github.com/dscripka/openWakeWord  
**Stars/forks:** 2.3k / 281 · **Last commit:** 2025-12-30 (commit `368c037`)  
**License:** Apache 2.0 (code) | CC-BY-NC-SA 4.0 (pre-trained weights)

**Architecture** (three independent stages, each a separate model file):

1. **Melspectrogram model** — ONNX implementation of Torch's MelSpectrogram with fixed parameters; ensures consistent behavior across platforms.
2. **Google Speech Embedding backbone** — a series of convolutional blocks pre-trained on large speech corpora (Apache 2.0, TFHub). Shared across all wake word models. This backbone is the core enabler: it provides rich speech representations from which tiny classifiers can learn from 100% synthetic TTS training data.
3. **Per-word classifier** — ~102K-parameter, 3-layer FC network (~0.4 MB) or 2-layer RNN. One per wake word. Processes embeddings for each 80 ms input frame.

Source: `dscripka/openWakeWord:openwakeword/model.py:32-100`, `docs/models/alexa.md:1-30`

**Pre-trained models (English only, CC-BY-NC-SA 4.0):**
- `alexa`, `hey_mycroft`, `hey_jarvis`, `hey_rhasspy`, `current_weather`, `timers`

**Performance metrics (author-reported):**
- Target: <5% false-reject rate (FRR), <0.5 false-accepts/hour (FAR)
- Evaluated on: DipCo Dinner Party Corpus (~5.5h far-field speech+music+noise)
- Positive test: Picovoice benchmark data mixed with DEMAND HOME noise (SNR 10 dB) + simulated RIR reverberation
- "Alexa" model: beats Picovoice Porcupine v2 on this specific test set (author-reported; small sample; Porcupine evaluation had known issues cited by openWakeWord)
- Fluent Speech Commands (SLU): ~97.5% vs 94.9% encoder-decoder baseline (both trained on synthetic data; not directly comparable)
- **Sanity check**: Results are in-domain (test data augmented similarly to training data). Third-party independent benchmark does not exist. Treat as directionally correct rather than exact.

**Key features relevant to family-base:**
- `vad_threshold=0.5` enables Silero VAD gate — only returns detections when VAD score > threshold. Critical for meeting audio where speech is continuous.
- `enable_speex_noise_suppression=True` — SpeexDSP noise suppression (Linux x86 only, lightweight).
- **Custom verifier models** (`docs/custom_verifier_models.md`): second-stage speaker-specific classifier trained on ~minutes of target speaker audio. Reduces FA rate when others are speaking.
- Debounce logic (v0.6.0).
- `bulk_predict()` with multiprocessing for offline scanning of recordings.
- Wyoming TCP microservice: `rhasspy/wyoming-openwakeword` — `script/run --uri tcp://0.0.0.0:10400`
- ONNX GPU: `device='gpu'` argument → `CUDAExecutionProvider` (`utils.py:85`). Overkill, CPU is sufficient.

**ONNX GPU support confirmed in source:**
```python
# dscripka/openWakeWord:openwakeword/utils.py:84-85
self.melspec_model = ort.InferenceSession(melspec_model_path, sess_options=sessionOptions,
    providers=["CUDAExecutionProvider"] if device == "gpu" else ["CPUExecutionProvider"])


**Known issues (active in 2025–2026):**
- Colab training notebook broken: `ai-edge-litert` / `onnx2tf` / `torchaudio` version conflicts (issues #296, #331, #322). Local WSL2 install is more stable.
- Install on some ARM/Pi platforms fails due to `speexdsp-ns` wheel (issue #322).
- These are training-pipeline issues, not inference issues. Pre-trained model inference is unaffected.

**Weaknesses:**
- Pre-trained weights NC (workaround: train custom)
- English-only
- Training Colab broken (workaround: local WSL2 or Docker trainer)

---

### 3.2 microWakeWord (`OHF-Voice/micro-wake-word`)

**Repository:** https://github.com/OHF-Voice/micro-wake-word (formerly `kahrendt/microWakeWord`)  
**Last commit:** 2025-12-21 · **Backed by:** Open Home Foundation / Nabu Casa / ESPHome  
**License:** Apache 2.0 (code + pre-trained models at `esphome/micro-wake-word-models`)

**Architecture** (designed for TFLite Micro / microcontrollers):

1. **micro_speech preprocessor**: 40 spectrogram features per 10 ms stride, 30 ms window. PCAN (Per-Channel Energy Normalization) + noise reduction + AGC. Same as TFLite Micro `micro_speech` example.
2. **MixedNet streaming model**: MixConv mixed depthwise convolutions ([arXiv:1907.09595](https://arxiv.org/abs/1907.09595)); trained non-streaming → converted to streaming via state injection. Based on "Streaming Keyword Spotting on Mobile Devices" ([arXiv:2005.06720](https://arxiv.org/abs/2005.06720)). Inference every 30 ms.
3. **Sliding window averaging**: probability must exceed cutoff (0.9–0.97 for v2 models) over a window of 5 consecutive inferences before triggering.

Source: `OHF-Voice/micro-wake-word:README.md`, `microwakeword/inference.py`

**Pre-trained models (Apache 2.0)** at `esphome/micro-wake-word-models`:
- v1: `alexa.tflite` (115 KB), `hey_jarvis.tflite` (115 KB), `okay_nabu.tflite` (115 KB)
- v2: `alexa.tflite` (55.9 KB), `hey_jarvis.tflite` (51.1 KB), `okay_nabu.tflite` (58.9 KB), `hey_mycroft.tflite` (55.9 KB), `vad.tflite` (33.5 KB)

Source: `esphome/micro-wake-word-models:models/v2/alexa.json:1-14`

**Python inference:**
```python
from microwakeword.inference import Model
model = Model("alexa.tflite")
predictions = model.predict_clip(audio_data_int16, step_ms=20)

Uses `ai_edge_litert.interpreter.Interpreter` — same library as openWakeWord v0.6.0 TFLite mode.

**Performance:** 
- ROC curves published as PNG for alexa, hey_jarvis, okay_nabu (repo `benchmarks/` directory)
- No numeric FA/FR table
- Probability cutoffs v2: alexa=0.9, okay_nabu=0.97 (high thresholds reflect tuning for low FAR)

**Strengths:**
- 100% Apache 2.0 including pre-trained weights — cleanest license of all options
- Ultra-small models (< 60 KB) — irrelevant for desktop but future-proof for embedded
- Built-in VAD in v2 model set
- ESPHome / Nabu Casa backing — durable long-term maintenance

**Weaknesses:**
- Primary use case: ESP32-S3; no desktop assistant deployment examples
- Training: "still very difficult, requires a lot of experimentation" (README)
- No Wyoming server, no Speex, no verifier models
- Python inference code uses same `ai_edge_litert` as openWakeWord but fewer integration helpers
- PCAN preprocessor designed for MCU microphones — behavior on PC loopback audio not characterized

---

### 3.3 Excluded alternatives

| Candidate | Reason for exclusion |
|---|---|
| **Picovoice Porcupine** | Commercial SDK. Free tier requires cloud-registered API key even for local inference. Privacy-incompatible. |
| **Snowboy (Kitt-AI)** | Unmaintained. Kitt-AI shut down. openWakeWord README: "performance significantly below Porcupine." |
| **Mycroft Precise** | Archived. Mycroft AI ceased operations 2023. |
| **NVIDIA NeMo MatchboxNet/MarbleNet** | KWS models exist but: no pre-trained English wake word model; non-streaming classification architecture; requires full training from scratch; higher engineering overhead vs. openWakeWord with no quality advantage for wake word use case. |
| **Whisper-based keyword detection** | ~1–5s latency per chunk — 30–100× too slow for real-time wake word detection. |
| **Azure / Google / Amazon speech** | Cloud-only or cloud-registration required. Out of scope. |

---

## 4. Recommendation

### Winner: openWakeWord

**Use openWakeWord** for the family-base meeting assistant.

**Why it beats microWakeWord for this specific use case:**

1. **Platform fit**: openWakeWord is explicitly designed for Python desktop/server deployment. microWakeWord is designed for ESP32 microcontrollers. Running microWakeWord on a Threadripper workstation to detect wake words provides no architectural advantage and loses all the desktop-focused features.

2. **Meeting audio robustness tooling**: Silero VAD integration (critical in continuous-speech meeting scenarios) + Speex noise suppression + custom verifier models for speaker adaptation are all absent in microWakeWord but present in openWakeWord.

3. **Integration ecosystem**: Wyoming protocol TCP server, Docker image, C++ wrapper, and a large community of real-world deployments (Home Assistant, Rhasspy). microWakeWord has none of these for desktop.

4. **microWakeWord's advantages don't apply here**: Apache 2.0 pre-trained models are an advantage, but family-base is private/non-commercial (CC-BY-NC-SA OK for personal use per Creative Commons terms). Model size (55 KB vs 0.4 MB) is irrelevant on a machine with 96 GB VRAM.

### Runner-up: microWakeWord

**Choose microWakeWord instead if:**
- The project goes commercial and you need Apache 2.0 weights without custom training
- You need to run the same wake word engine on both an embedded satellite device AND the desktop server (uniform stack)

### Decision Rule

> **Private/non-commercial desktop Python service** → openWakeWord (pre-trained models OK under CC-BY-NC-SA for personal use)
>
> **Commercial release OR microcontroller co-deployment** → microWakeWord pre-trained models (Apache 2.0) or custom-trained openWakeWord models via Apache 2.0 training pipeline

**License risk mitigation**: If commercial potential exists, train a custom "hey family-base" model using openWakeWord's Apache 2.0 training pipeline *now*. The resulting model weights are yours, unlicensed. The `lgpearson1771/openwakeword-trainer` Docker image (WSL2+CUDA, last updated 2026-05-31) provides a working environment when Colab is broken.

---

## 5. Integration Sketch

### 5.1 Architecture in the family-base stack


[Rust/cpal audio capture — mic (WASAPI) + system loopback]
    |
    | 16-bit PCM, 16 kHz, chunked into 80 ms frames (1280 samples)
    | via TCP socket or shared memory to WSL2
    ↓
[Python WSL2 service: wake_word_service.py]

from openwakeword.model import Model

model = Model(
    wakeword_models=["hey_family_base.tflite"],  # custom trained, Apache 2.0
    vad_threshold=0.5,           # Silero VAD — gate to speech-only frames
    enable_speex_noise_suppression=True,  # for mic stream only
    inference_framework="tflite"
)

# Main loop
while True:
    frame = get_audio_frame()    # 1280 samples = 80 ms @ 16kHz
    prediction = model.predict(frame)
    if prediction["hey_family_base"] > 0.5:
        emit_event_to_tauri("wake_word_detected")
        model.reset()            # clear buffer after trigger

    ↓
[Tauri 2 frontend receives HTTP/WebSocket event]
    → Show listening UI
    → Start NeMo Canary-Qwen / Whisper ASR recording


**Resource budget:**
- CPU: <1 ms per 80 ms frame (single core). Runs on any idle CPU thread.
- RAM: ~10 MB total (embedding model + 1 custom classifier + Silero VAD)
- VRAM: 0 MB — GPU entirely free for Canary/Whisper/LLM

### 5.2 Two audio streams consideration

The Rust audio layer captures two streams: mic (WASAPI) + system loopback. Recommendations:
- **Mic stream**: Run openWakeWord WITH Speex + VAD — this is the intended use case
- **Loopback stream**: Skip wake word detection on loopback (the assistant shouldn't react to audio it played back); or run with a separate high-threshold instance to detect accidental triggers

### 5.3 Custom wake word training pipeline

1. **Generate synthetic speech** using Piper TTS:
   ```bash
   # piper-sample-generator to generate ~5,000-10,000 clips
   # of "hey family-base", "family base", variations, multiple voices
   

2. **Train using WSL2+CUDA-compatible trainer:**
   ```bash
   git clone https://github.com/lgpearson1771/openwakeword-trainer
   cd openwakeword-trainer
   # Follow Docker/conda setup for WSL2 + CUDA
   # Generates: hey_family_base.onnx (~0.4 MB) + hey_family_base.tflite
   

3. **Validate**: Run against DipCo or similar ambient corpus for FA rate; test FRR on mic recordings in meeting environment

4. **Deploy**: Drop `.tflite` file into service; no redeployment of other stack components needed

**Estimated effort**: 1–2 days (TTS data gen: 2–4h, training: 2–4h, validation+tuning: 4–8h)

### 5.4 Dependencies


# Inference only (no training)
pip install openwakeword         # installs ai-edge-litert + onnxruntime

# Optional noise suppression (Linux x86 only)
sudo apt-get install libspeexdsp-dev
pip install speexdsp-ns

# Optional GPU inference (unnecessary but available)
pip install onnxruntime-gpu      # replace onnxruntime


No GPU driver configuration needed for CPU inference. For GPU: `onnxruntime-gpu` + CUDA 12.8 (already installed) — works out of the box.

### 5.5 Risks and mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| Colab training notebook broken | Medium | Use `lgpearson1771/openwakeword-trainer` (Docker, WSL2+CUDA); local install on WSL2 |
| CC-BY-NC-SA pre-trained models (commercial risk) | Low (private use OK); Medium (if commercial) | Train custom model immediately; no NC restriction on training pipeline |
| High FAR in continuous-speech meeting | Medium | Enable Silero VAD (`vad_threshold=0.5`) + custom verifier model trained on user voice |
| `ai-edge-litert` version pinning | Low | Pin `ai-edge-litert==2.1.2`; test on fresh WSL2 venv |
| Loopback audio triggering false accepts | Medium | Disable wake word detection on loopback stream or use separate high-threshold instance |
| English-only | Low | Acceptable for meeting assistant context; note for non-English future work |

---

## 6. Shared-Tech / Overlap Notes

- **Silero VAD**: Included with openWakeWord as a gate (`vad.py`). If VAD is separately needed for ASR trigger detection or silence detection, the same Silero model is already in-process — reuse it rather than loading it again.

- **Audio pipeline**: 16-bit 16 kHz PCM is the format for all models in the stack (Canary-Qwen ASR, Whisper, openWakeWord). The Rust audio capture layer can fan-out the same PCM stream to the wake word service and the ASR service without format conversion.

- **Wyoming protocol microservice**: `rhasspy/wyoming-openwakeword` provides a battle-tested TCP server pattern (`--uri tcp://0.0.0.0:10400`) that is directly analogous to how other family-base services expose `localhost /v1/audio/transcriptions`. The Wyoming pattern is worth adopting for the wake word service as a consistent service interface.

- **C++ wrapper**: `rhasspy/openWakeWord-cpp` provides a path to calling openWakeWord directly from the Tauri Rust layer if the Python service introduces unacceptable IPC latency (unlikely, but available as fallback).

- **Speaker verification / verifier models**: Custom openWakeWord verifier models use speaker embeddings extracted from target voice samples. If a speaker identification model (TitaNet or similar) is already deployed in the stack, its embeddings are potentially reusable for verifier model training. This is a potential integration point with the diarization/speaker-ID component.

- openWakeWord does **not** cover ASR, diarization, NLP, summarization, or any other family-base capability. It is a pure binary trigger (0/1 per 80 ms frame). All other services remain in their respective components.

---

## 7. Open Questions / What Needs a Prototype to Settle

1. **FAR on system loopback audio**: DipCo covers far-field microphone recording in noisy environments. System audio loopback (the assistant playing back TTS or audio from a meeting) is a different failure mode. Does openWakeWord falsely activate when hearing its own synthesized voice say the wake word? Needs empirical test with actual family-base TTS output.

2. **Custom wake word training quality**: Training "hey family-base" (a novel phrase) using the automated pipeline — what FRR/FAR does it achieve on one engineer's voice vs. multiple speakers? The Colab notebook is broken; the Docker trainer claims WSL2+CUDA compatibility but this is unverified at the wake-word quality level.

3. **VAD threshold for continuous speech**: In a meeting, `vad_threshold=0.5` means the VAD gate is almost always open (speech is almost always present). Does this provide any FA reduction benefit, or should it be set higher (0.7–0.9) to gate only on loud foreground speech? Needs empirical calibration.

4. **Keyboard shortcut vs. wake word**: For a desktop meeting assistant, a keyboard shortcut (e.g., `Ctrl+Shift+Q`) may be more ergonomic and reliable than wake words for 90% of use cases. Wake words add value for hands-free scenarios (whiteboard, standing). Worth validating with users before investing in custom training.

5. **microWakeWord Python desktop FA behavior**: The PCAN preprocessor in microWakeWord was designed for MCU microphones with specific noise floor characteristics. Its behavior on high-quality PC microphones and loopback audio is uncharacterized. If Apache 2.0 licensing becomes critical, a parallel test of microWakeWord's FA/FR on meeting audio would be needed.

---

## 8. Sources

1. **openWakeWord repository** — README, model.py, utils.py, docs/models/alexa.md:
   https://github.com/dscripka/openWakeWord

2. **openWakeWord ONNX GPU support** (source code):
   `dscripka/openWakeWord:openwakeword/utils.py:84-93` (commit `368c037`)

3. **openWakeWord model architecture** (Alexa classifier):
   `dscripka/openWakeWord:docs/models/alexa.md:1-50`

4. **openWakeWord releases** (v0.1.1–v0.6.0):
   https://github.com/dscripka/openWakeWord/releases

5. **openWakeWord training pipeline breakage** (open issues 2025–2026):
   https://github.com/dscripka/openWakeWord/issues/296 · /331 · /251 · /322

6. **microWakeWord repository** (OHF-Voice):
   https://github.com/OHF-Voice/micro-wake-word

7. **microWakeWord Python inference code**:
   `OHF-Voice/micro-wake-word:microwakeword/inference.py` (commit `a70bd74`)

8. **microWakeWord pre-trained models** (ESPHome, Apache 2.0):
   https://github.com/esphome/micro-wake-word-models — `models/v2/alexa.json`, `okay_nabu.json`

9. **Wyoming openWakeWord server**:
   https://github.com/rhasspy/wyoming-openwakeword

10. **openWakeWord C++ wrapper**:
    https://github.com/rhasspy/openWakeWord-cpp

11. **Community WSL2+CUDA trainer** (openwakeword-trainer):
    https://github.com/lgpearson1771/openwakeword-trainer

12. **Community wake word model collection** (fwartner):
    https://github.com/fwartner/ha-openwakeword-installer

13. **MixConv paper** (microWakeWord backbone):
    Tan & Le, "MixConv: Mixed Depthwise Convolutional Kernels," BMVC 2019, arXiv:1907.09595
    https://arxiv.org/abs/1907.09595

14. **Streaming keyword spotting paper** (microWakeWord training basis):
    Rykabov et al., "Streaming Keyword Spotting on Mobile Devices," Interspeech 2020, arXiv:2005.06720
    https://arxiv.org/abs/2005.06720

15. **Google Speech Embedding backbone** (openWakeWord feature extractor):
    arXiv:2002.01322 — https://arxiv.org/abs/2002.01322
    TFHub model: https://tfhub.dev/google/speech_embedding/1

16. **SpecAugment** (used in microWakeWord training):
    Park et al., "SpecAugment: A Simple Data Augmentation Method for ASR," Interspeech 2019, arXiv:1904.08779
    https://arxiv.org/abs/1904.08779

17. **Picovoice Porcupine** (excluded — commercial/cloud-registered):
    https://picovoice.ai/platform/porcupine/

18. **Picovoice wake word benchmark** (test data used by openWakeWord evaluation):
    https://github.com/Picovoice/wake-word-benchmark

19. **DipCo Dinner Party Corpus** (false-accept evaluation corpus):
    https://www.amazon.science/publications/dipco-dinner-party-corpus

20. **Piper sample generator** (TTS data generation for custom training):
    https://github.com/rhasspy/piper-sample-generator

21. **openWakeWord HuggingFace demo**:
    https://huggingface.co/spaces/davidscripka/openWakeWord

22. **Creative Commons BY-NC-SA 4.0** (openWakeWord pre-trained model license):
    https://creativecommons.org/licenses/by-nc-sa/4.0/


---

## Summary of Findings for the Main Agent

**Repositories discovered:**
- `dscripka/openWakeWord` — primary wake word framework for Python desktop; 2.3k stars; active
- `OHF-Voice/micro-wake-word` — microcontroller-focused wake word; Apache 2.0 models; active
- `esphome/micro-wake-word-models` — pre-trained TFLite models (Apache 2.0, 52–115 KB)
- `rhasspy/wyoming-openwakeword` — Wyoming TCP server for openWakeWord
- `lgpearson1771/openwakeword-trainer` — WSL2+CUDA-compatible custom model trainer

**Key source files verified:**
- `dscripka/openWakeWord:README.md:1-279` — full architecture, performance, license documentation
- `dscripka/openWakeWord:openwakeword/utils.py:80-160` — CUDA support confirmed (line 85), AudioFeatures class
- `dscripka/openWakeWord:openwakeword/model.py:32-100` — Model class, inference_framework, vad_threshold, verifier models
- `dscripka/openWakeWord:docs/models/alexa.md` — model architecture (102K params, 0.4 MB), training data details
- `OHF-Voice/micro-wake-word:README.md` — MixConv streaming model, 40 features/10ms, "early release" warning, "very difficult" training
- `OHF-Voice/micro-wake-word:microwakeword/inference.py` — Python API via ai_edge_litert, predict_clip(), quantization handling
- `esphome/micro-wake-word-models:models/v2/alexa.json` — probability_cutoff=0.90, sliding_window_size=5, 22KB tensor arena

**Decision: openWakeWord wins** for desktop Python deployment due to feature set, integration ecosystem, and design intent; microWakeWord is runner-up for its cleaner Apache 2.0 pre-trained model license if commercial use is required.
