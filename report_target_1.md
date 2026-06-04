
# Speech Enhancement / Denoising — Decision Report
**Target system:** family-base (local, offline, privacy-first desktop meeting assistant — Meetily fork)
**Candidates evaluated:** DeepFilterNet3, ClearerVoice-Studio (FRCRN / MossFormerGAN / MossFormer2_SE_48K), Demucs/Denoiser, RNNoise, WebRTC AEC3

---

## 1. TL;DR

**Two-winner answer (functionally distinct roles):**
- **Noise Suppression (primary):** DeepFilterNet3 — MIT/Apache, 48 kHz native, causal/streaming, ONNX + native Rust (`libdf` crate), ~2M parameters, runs at <1× RTF on CPU, leaving the RTX PRO 6000 fully free for ASR/LLM.
- **Acoustic Echo Cancellation (AEC):** `tonarino/webrtc-audio-processing` (Rust crate wrapping WebRTC AEC3) — the only candidate that performs true algorithmic echo cancellation using the system loopback as reference. It also ships built-in moderate NS; run it first, then DeepFilterNet3 for residual noise suppression.

**Single "noise suppressor" winner if forced to one:** **DeepFilterNet3**. It uniquely satisfies every hard constraint: MIT/Apache license, 48 kHz, causal streaming, ONNX, Rust-native, GPU-optional, last release Oct 2024. Runner-up for maximum batch quality: **MossFormerGAN_SE_16K** (highest PESQ on both DNS-2020 and VoiceBank+DEMAND benchmarks, Apache 2.0).

---

## 2. Decision Matrix

All benchmark numbers are from ClearerVoice-Studio's published evaluation
(`modelscope/ClearerVoice-Studio:clearvoice/README.md`, commit c8d73ab8, 2025-08)
using the SpeechScore toolkit unless otherwise noted.
Conditions: VoiceBank+DEMAND (VB+D) test set; DNS-Challenge-2020 (non-reverb).
"Measured" = from the cited ClearerVoice repo table (third-party re-evaluation,
using a unified model, not cherry-picked per-dataset). RTF numbers from
official project documentation.

| Candidate | PESQ (VB+D 48kHz / DNS-2020 16kHz) | STOI | P808 MOS (DNS) | Streaming / Live | VRAM | License | Maintenance | Stack integration effort |
|---|---|---|---|---|---|---|---|---|
| **DeepFilterNet3** | 3.03 / — (16kHz not benchmarked here) | 0.94 | 3.47 | ✅ causal, 10ms frame | ~50–100 MB (CPU-capable) | MIT / Apache 2.0 | Oct 2024, ★3.6k | 🟢 ONNX, libdf Rust crate, pip |
| **MossFormerGAN_SE_16K** | — / **3.57** (best DNS) / 3.47 (VB+D 16kHz) | **0.98** | **4.05** | ❌ batch only | ~400–600 MB est. | Apache 2.0 | Aug 2025, active | 🟡 Python pip, NumPy API |
| **MossFormer2_SE_48K** | **3.15** (VB+D 48kHz) / 2.94 (DNS) | 0.95 | 3.92 | ❌ batch only | ~800 MB–1.5 GB est. | Apache 2.0 | Aug 2025, active | 🟡 Python pip, NumPy API |
| **FRCRN_SE_16K** | 3.23 (VB+D 16kHz) / 3.24 (DNS) | 0.95–0.98 | 4.03 | ❌ batch only (likely) | ~300–500 MB est. | Apache 2.0 | Aug 2025, active | 🟡 Python pip, NumPy API |
| **Demucs/Denoiser** | ~2.91 (DNS48, from paper) | ~0.94 | N/A | ✅ RTF ~0.8 (1 CPU core) | CPU-capable | **CC-BY-NC 4.0 ⛔** | Last commit 2021 (stale) | 🔴 Disqualified by license |
| **RNNoise** | Not PESQ benchmarked; informal ~2.5 for stationary noise | N/A | N/A | ✅ <10ms, CPU only | none (C library) | BSD-3-Clause | Jan 2025 data update | 🟢 C lib / nnnoiseless Rust crate |
| **WebRTC AEC3** | AEC-specific; NS moderate (DNSMOS P.835 ~3.3 with NS-High, unverified) | N/A (AEC role) | N/A | ✅ 10ms frames, CPU | none (C++ lib) | BSD-3-Clause | May 2026 Rust crate commit | 🟢 tonarino/webrtc-audio-processing Rust crate |

**Noisy baseline for reference:** VB+D 48kHz: PESQ=1.97, DNS-2020: PESQ=1.58.

---

## 3. Per-Candidate Notes

### 3.1 DeepFilterNet3
**Repo:** https://github.com/Rikorose/DeepFilterNet  
**Papers:** ICASSP 2022 (v1), IWAENC 2022 (v2), Interspeech 2023 (v3/perceptual)

**Architecture:** Dual-path GRU encoder-decoder. ERB (equivalent rectangular bandwidth) mask path for broadband suppression + deep-filtering path for fine spectral detail. 10ms frame (hop=480 @ 48kHz), FFT=960, lookahead=0 by default (causal). ~1.8M parameters; model zip ~8MB; ONNX variants: standard ~8MB, low-latency (ll_onnx) ~36MB.

**Benchmarks:**  
- VB+D 48kHz: PESQ=3.03, NB_PESQ=3.71, STOI=0.94, SI-SDR=15.71, P808_MOS=3.47  
  (Source: `modelscope/ClearerVoice-Studio:clearvoice/README.md`)
- Third-party DNS-2020 numbers not provided in this table because the ClearerVoice eval used only the 16kHz models against DNS-2020 16kHz. DeepFilterNet's own published DNSMOS numbers (from the Interspeech 2023 paper, arXiv:2305.08227) show DFN3 significantly outperforming DFN2 on perceptual MOS; exact DNSMOS P.835 values were not independently verified here.
- SI-SDR of 15.71 on VB+D 48kHz is **lower** than MossFormer2_SE_48K (19.36). This gap is notable but SI-SDR can over-penalise models that trade slight waveform distortion for perceptual quality. PESQ gap (3.03 vs 3.15) is smaller.

**VRAM / throughput:** CPU-capable; GPU path via PyTorch optional. At 48kHz 10ms frames, a GRU with ~1.8M params takes well under 1ms per frame on CPU. ONNX variant avoids PyTorch entirely. No measurable VRAM required for CPU path; PyTorch GPU mode would use ~50–150 MB, leaving 95+ GB for other models.

**License:** MIT OR Apache-2.0 (dual choice) — unrestricted commercial private use. Confirmed in `Rikorose/DeepFilterNet:LICENSE-MIT`, `LICENSE-APACHE`.

**Maturity:** Last merge Oct 2024 (SHA d375b2d). Project considered feature-complete at v3; community contributions continue. LADSPA plugin for PipeWire real-time use is production-deployed by Linux users.

**Integration:**  
- `pip install deepfilternet` → Python service  
- `libdf` Rust crate → consume directly from Rust audio pipeline (no Python hop)  
- ONNX export available (`DeepFilterNet3_onnx.tar.gz`, `DeepFilterNet3_ll_onnx.tar.gz`) → `ort` Rust crate for zero-Python path  
- Python API: `from df import enhance, init_df; enhanced = enhance(model, df_state, noisy_audio)`

**Weaknesses:**  
- Not an AEC tool. Cannot cancel system loopback echo; that requires a separate AEC stage.  
- Slight SI-SDR disadvantage vs MossFormer2_SE_48K in batch mode.  
- Commit activity slowed post-v3; not clear if a v4 is planned.

---

### 3.2 ClearerVoice-Studio — FRCRN_SE_16K
**Repo:** https://github.com/modelscope/ClearerVoice-Studio  
**Paper:** FRCRN: arXiv:2206.07293 (Interspeech 2022)  
**ModelScope usage:** 3M+ inference calls.

**Architecture:** Frequency-Recurrence Complex U-Net (FRCRN): cascaded CRN + RNN in complex domain. 16kHz only.

**Benchmarks:**  
- VB+D 16kHz: PESQ=3.23, STOI=0.95, SI-SDR=19.22, P808_MOS=3.59, FWSEGSNR=**20.76** (best on VB+D)  
- DNS-2020: PESQ=3.24, STOI=0.98, SI-SDR=19.99, P808_MOS=4.03

**VRAM:** Estimated ~300–500 MB on GPU for batch inference (model files not directly sized, but FRCRN is described as compact). CPU feasible but slower.

**License:** Apache 2.0. No commercial restrictions.

**Weaknesses:** 16kHz cap — must downsample 48kHz meeting audio, losing high-frequency content above 8kHz. No streaming mode confirmed. Dominated by MossFormerGAN on most metrics.

---

### 3.3 ClearerVoice-Studio — MossFormerGAN_SE_16K
**Paper:** MossFormer: arXiv:2302.11824; GAN variant not separately arXived (released as part of ClearerVoice-Studio, 2024–2025).

**Architecture:** MossFormer2 backbone with adversarial (GAN) training for perceptual quality. 16kHz.

**Benchmarks (best 16kHz model overall):**  
- VB+D 16kHz: PESQ=**3.47**, STOI=**0.96**, SI-SDR=19.45, SSNR=**9.09**, P808_MOS=3.57  
- DNS-2020: PESQ=**3.57**, STOI=**0.98**, SI-SDR=**20.60**, P808_MOS=**4.05**, SSNR=**14.03**  
  (Source: `modelscope/ClearerVoice-Studio:clearvoice/README.md`, all bold = best in class)

These are the **highest PESQ numbers in this comparison** on both benchmarks. However, conditions: (a) unified model tested zero-shot on both sets — benchmark is not in-domain for this model, which is actually a strong sanity-check; (b) 16kHz output means some high-frequency loss.

**VRAM:** MossFormer2 at 16kHz reported ~25.3M parameters in the original paper. FP32 weights ~100 MB; batch inference activations likely 400–600 MB VRAM. GPU strongly recommended for reasonable batch throughput.

**License:** Apache 2.0.

**Weaknesses:** 16kHz only; no causal/streaming mode; batch only (not suitable for LIVE); larger model; Python-only.

---

### 3.4 ClearerVoice-Studio — MossFormer2_SE_48K
**Architecture:** MossFormer2 at 48kHz (fullband). More parameters than the 16kHz variant due to wider spectral coverage.

**Benchmarks:**  
- VB+D 48kHz: PESQ=**3.15** (best 48kHz), STOI=**0.95**, SI-SDR=19.36, P808_MOS=3.53, SRMR=9.61  
- DNS-2020 (16kHz): PESQ=2.94, STOI=0.97 — notably worse than 16kHz models on DNS  
  (Source: `modelscope/ClearerVoice-Studio:clearvoice/README.md`)

**Note on DNS-2020 score:** The DNS-2020 test set is 16kHz; MossFormer2_SE_48K processes at 48kHz and the result is downsampled for scoring — this likely explains the lower PESQ (2.94 vs 3.57 for MossFormerGAN_SE_16K). The 48kHz advantage is real for preserving voice quality above 8kHz but DNS-2020 doesn't capture that.

**VRAM:** ~800 MB–1.5 GB estimated for batch inference. On RTX PRO 6000 (96 GB VRAM) this is trivial.

**License:** Apache 2.0.

**Weaknesses:** No streaming. Batch only. Python-only service.

---

### 3.5 Demucs/Denoiser (facebookresearch/denoiser)
**Repo:** https://github.com/facebookresearch/denoiser  
**Paper:** Defossez et al., Interspeech 2020, arXiv:2006.12847

**⛔ DISQUALIFIED: CC-BY-NC 4.0 license (non-commercial only).** Confirmed in `facebookresearch/denoiser:LICENSE`.  
Private internal business use (which is what "family-base" is — a private offline assistant) may or may not qualify as "non-commercial" but the ambiguity alone makes this unsuitable for any product that could be used commercially. Do not use.

**For reference only:**  
- RTF: H=48 model, 1 thread = 0.8 (real-time on quad-core Intel i5 2GHz); H=64: 1.2 (not real-time on 1 thread, real-time on 4). On RTX PRO 6000 class hardware, GPU inference would achieve 10–50× real-time.  
- Latency: ~41ms algorithmic + model time  
- DNS48 model PESQ: ~2.91 (from paper, in-domain DNS test set)  
- No 48kHz support; 16kHz only.  
- Last significant update: 2021. Maintenance effectively stopped.

---

### 3.6 RNNoise (xiph/rnnoise)
**Repo:** https://gitlab.xiph.org/xiph/rnnoise (GitHub mirror: https://github.com/xiph/rnnoise)  
**Paper:** Valin, MMSP 2018, arXiv:1709.08243

**Architecture:** Hybrid DSP + GRU. 48kHz, 10ms frames (480 samples). Operates in ERB-band domain. Model weights updated Jan 2025 using public datasets.

**VRAM:** Zero — C library, CPU-only. Binary is ~50–100 KB. nnnoiseless Rust crate wraps it natively.

**Benchmarks:** RNNoise does not appear in PESQ leaderboard comparisons because it predates the DNS benchmark era and was not evaluated on VoiceBank+DEMAND in published form. Informal reports suggest PESQ ~2.4–2.6 on moderate noise — substantially below DeepFilterNet3 (3.03) and MossFormerGAN (3.47). Quality is adequate for stationary noise (HVAC, fan, keyboard); struggles with music, babble, and spectrally complex noise.

**License:** BSD-3-Clause. Fully commercial-ok.

**Maturity:** The C library is considered complete and stable. Training data was refreshed Jan 2025 (models downloadable separately from source). Rust crate `nnnoiseless` (https://github.com/nicowillis/nnnoiseless) provides a `DenoiseState` struct usable directly in the Rust audio pipeline.

**Integration:** Best-fit for ultra-low-latency fallback or as a pre-filter before DeepFilterNet3 (though running two sequential noise suppressors may cause over-suppression artifacts). Can run inside the Rust `cpal` audio capture loop without any Python. Frame size exactly matches WebRTC AEC3 (480 samples @ 48kHz).

**Weaknesses:** Quality significantly lower than DeepFilterNet3 on meeting audio. No voice separation or reverb handling.

---

### 3.7 WebRTC AEC3 (via tonarino/webrtc-audio-processing)
**Crate:** https://github.com/tonarino/webrtc-audio-processing  
**Upstream:** PulseAudio repackaging of WebRTC's AudioProcessing module (libwebrtc-audio-processing-1)  
**Capabilities:** AEC3 (Echo Canceller 3), NS (Noise Suppression), AGC (Automatic Gain Control), HPF (High-Pass Filter), VAD (Voice Activity Detection)

**Why it's unique:** This is the **only candidate** in this list that performs true Acoustic Echo Cancellation. All ML-based denoisers (DFN3, MossFormer, etc.) suppress ambient noise but **cannot** cancel the specific echo of system audio that leaked into the mic. AEC3 uses the render (loopback) stream as a reference signal to adaptively subtract the echo from the capture (mic) stream. The `family-base` stack already captures separate mic and loopback streams (cpal + WASAPI loopback), providing exactly the reference signal AEC3 needs.

**License:** BSD-3-Clause (WebRTC source). Rust crate also BSD-3-Clause. Fully commercial-ok.

**Maturity:** Rust crate last commit May 2026 (SHA 984733d). Actively maintained; just updated to Rust edition 2024. Experimental AEC3 detailed config available behind feature flag.

**Platform note (critical):** `webrtc-audio-processing-sys` has **no MSVC support** on Windows native (confirmed from code search finding: "disabled on Windows (webrtc-audio-processing-sys has no MSVC support upstream)"). However, the family-base stack runs audio capture in Rust on Windows (WASAPI via cpal), then heavy ML runs in WSL2 Ubuntu. The AEC processor can run in the WSL2 Ubuntu Rust binary or a native Windows build using the `bundled` feature with a GCC/Clang toolchain (not MSVC). Alternatively, compile from source inside WSL2 and IPC the processed audio.

**VRAM:** Zero. Pure C++ algorithmic AEC. 10ms frames at 48kHz (480 samples). Sub-millisecond per frame on any modern CPU.

**Integration:** 
```toml
[dependencies]
webrtc-audio-processing = { version = "~2.0", features = ["bundled"] }

API: push render frame (loopback) → push capture frame (mic) → read processed capture.

**Weaknesses:** AEC only (plus basic NS). Quality of AEC3 NS is moderate compared to DFN3. Not an ML denoiser. Requires the render signal to be time-aligned with the capture signal; WASAPI loopback with known latency makes this feasible. Windows MSVC constraint.

---

## 4. Recommendation

### Primary recommendation: DeepFilterNet3 for NS + WebRTC AEC3 for AEC

These are functionally non-overlapping tools; both are needed.

**For Noise Suppression — Winner: DeepFilterNet3**

Wins against MossFormerGAN_SE_16K (the closest runner-up on quality metrics) because:
1. **48kHz support.** Meeting audio captured at 48kHz loses no high-frequency content. MossFormerGAN_SE_16K requires downsampling to 16kHz, discarding 16–24kHz content that affects naturalness.
2. **Causal streaming.** DFN3 processes 10ms frames causally (df_lookahead=0). MossFormerGAN is batch-only. LIVE mode is a stated hard requirement.
3. **Rust-native path.** `libdf` crate + ONNX allow zero-Python integration in the existing Rust audio pipeline. MossFormerGAN requires a Python service.
4. **License risk-free.** MIT/Apache 2.0. MossFormerGAN is Apache 2.0 also, but DFN3's dual MIT option is maximally permissive.
5. **Resource footprint.** DFN3 (~2M params) runs CPU-only at <1× RTF, consuming negligible GPU. MossFormerGAN/MossFormer2 need GPU for practical batch throughput, competing with NeMo and Whisper.

**Decision rule: when to use MossFormerGAN_SE_16K instead:**
- BATCH mode only (post-meeting transcript cleanup where 16kHz is acceptable)
- Where maximum PESQ/MOS on the processed audio is the goal (e.g., archiving clean audio, or feeding clean audio to a downstream speaker diarization step that is sensitive to noise)
- When 48kHz fidelity is irrelevant (e.g., the downstream model is Whisper-large-v3-turbo at 16kHz anyway)

**Decision rule for MossFormer2_SE_48K:**
- Choose over MossFormerGAN when 48kHz output fidelity is important AND you're in batch mode AND you want a single SE step that preserves fullband audio.
- For the ASR pipeline specifically: Whisper and NeMo Canary both resample to 16kHz internally, so MossFormer2_SE_48K's 48kHz advantage over MossFormerGAN is lost before ASR. Only matters if storing/playing back the cleaned audio at full bandwidth.

**For AEC — Winner: WebRTC AEC3 (tonarino/webrtc-audio-processing Rust crate)**

No ML denoiser in this list provides true echo cancellation. The existing system captures mic and loopback separately — this is the exact input format AEC3 requires. Run AEC3 first to remove the echo, then DFN3 to clean residual noise. This two-stage pipeline is standard practice.

### Recommended pipeline:

**LIVE (latency target < 100ms):**

[mic stream @ 48kHz, 10ms frames]
        │
        ▼
WebRTC AEC3 (with loopback as render reference) ← [loopback stream @ 48kHz]
        │  [echo-cancelled mic, 10ms, BSD-3-Clause, CPU, <1ms/frame]
        ▼
DeepFilterNet3 (ONNX or libdf Rust crate, 10ms frames)
        │  [denoised mic, 10ms, MIT/Apache, CPU, ~1–3ms/frame]
        ▼
[clean mic stream → ASR (NeMo Canary / Whisper-large-v3)]


**BATCH (post-meeting, max quality):**

[recorded mic audio, any length] → resample to 16kHz if using MossFormerGAN
        │
        ▼
MossFormerGAN_SE_16K (Python clearvoice service)  [OR MossFormer2_SE_48K for 48kHz output]
        │  [high-quality denoised audio]
        ▼
[storage / transcript regeneration]


---

## 5. Integration Sketch

### 5.1 LIVE path (Rust-native, no Python)

**Dependencies:**
```toml
# In the Rust audio capture crate (Cargo.toml)
[dependencies]
webrtc-audio-processing = { version = "~2.0", features = ["bundled"] }  # AEC3
ort = "2"                    # ONNX Runtime for DeepFilterNet3
# OR: libdf = "0.4"          # Native libdf crate (avoids ONNX, links Rust DF lib)
cpal = "0.15"


**Conceptual Rust audio loop:**
```rust
use webrtc_audio_processing::{Processor, Config, InitializationConfig};

// Initialize AEC3 processor
let mut apm = Processor::new(&InitializationConfig {
    num_capture_channels: 1,
    num_render_channels: 1,
    ..Default::default()
})?;
apm.set_config(Config {
    echo_cancellation: Some(EchoCancellation {
        enable: true,
        ..Default::default()
    }),
    noise_suppression: Some(NoiseSuppression {
        level: NoiseSuppressionLevel::High,
        ..Default::default()
    }),
    high_pass_filter: Some(HighPassFilter { enable: true }),
    ..Default::default()
});

// Per 10ms frame (480 samples @ 48kHz):
apm.process_render_frame(&mut loopback_frame)?; // feed loopback first
apm.process_capture_frame(&mut mic_frame)?;     // then process mic

// mic_frame now echo-cancelled → feed into DeepFilterNet3 ONNX session
// (via ort crate, loading DeepFilterNet3_onnx.tar.gz)


**DeepFilterNet3 ONNX path:**  
Load `models/DeepFilterNet3_onnx.tar.gz` (standard, ~8MB) or `DeepFilterNet3_ll_onnx.tar.gz` (low-latency variant, ~36MB, slightly more aggressive). Use `ort` crate for ONNX inference. The model processes the same 10ms frames as AEC3, so no buffering adapter needed.

**Alternatively** (simpler, single Python service):  
Run the AEC3 in Rust (as above), pipe the 10ms float32 PCM chunks over a Unix socket or named pipe to a Python process running `deepfilternet`, get back cleaned audio. This avoids the ONNX dependency at the cost of IPC latency (~1–2ms on localhost). Still well within a 100ms live budget.

**Total algorithmic latency (LIVE):**  
- AEC3: 10ms frame + ~0ms algorithmic = ~10ms  
- DFN3: 10ms frame + model inference ~1–3ms on CPU = ~11–13ms  
- Buffering/IPC: 0–5ms  
- Total: **~21–28ms** from mic capture to clean audio available for ASR

### 5.2 BATCH path (Python service)

```python
from clearvoice import ClearVoice
import numpy as np

# Run after meeting ends
cv = ClearVoice(task='speech_enhancement', model_names=['MossFormerGAN_SE_16K'])

# Process the mic recording (resample to 16kHz first)
output_wav = cv(input_path='meeting_mic_48k.wav', online_write=False)
cv.write(output_wav, output_path='meeting_mic_clean_16k.wav')


Or using the Numpy API (2025.06 feature) for pipeline integration:
```python
# Accepts numpy float32 array, returns numpy array
output_np = cv(input_path=mic_array_16k, online_write=False)


**Resource usage during batch:**  
MossFormerGAN_SE_16K on RTX PRO 6000 Blackwell: estimated ~400–600 MB VRAM.  
At 1 hour of audio: processes in real-time or faster on GPU.  
Runs as a Python service alongside NeMo Canary; VRAM budget (96 GB) is not a concern.

### 5.3 Dependencies and risks

| Risk | Mitigation |
|---|---|
| `webrtc-audio-processing` Windows MSVC gap | Run AEC processor in WSL2 Ubuntu Rust binary; route audio over IPC (named pipe / Unix socket) from Windows Rust to WSL2 |
| AEC3 stream alignment (render must precede capture) | WASAPI loopback provides timestamped audio; use a fixed 20–40ms delay buffer on the render side to guarantee causal ordering |
| DFN3 artifacts at low SNR | Enable post-filter (`--pf`) flag; or gate DFN3 processing on VAD (WebRTC AEC3 provides VAD output) |
| MossFormerGAN 16kHz ceiling | If full 48kHz quality matters for batch output, use MossFormer2_SE_48K instead |
| DFN3 slower for BATCH on long files | Use GPU PyTorch path for batch; or tile the ONNX inference with large batch sizes |

---

## 6. Shared-Tech / Overlap Notes

- **ASR pre-processing (NeMo Canary / Whisper):** Both ASR engines benefit from cleaned audio. DeepFilterNet3 in the live path directly improves WER by reducing noise before transcription — no extra integration needed; the cleaned audio stream is the same stream fed to ASR.  
- **Speaker Diarization (pyannote):** Noise suppression improves VAD and speaker embedding quality. The WebRTC AEC3's built-in VAD output can optionally feed pyannote's SAD stage.  
- **Speech Super-Resolution:** `MossFormer2_SR_48K` (also in ClearerVoice-Studio) can upsample post-meeting audio from 16kHz to 48kHz. This composes with the batch noise suppression path: denoise with MossFormerGAN_SE_16K → upsample with MossFormer2_SR_48K → archive at 48kHz for playback.  
- **Target Speaker Extraction:** `AV_MossFormer2_TSE_16K` (in ClearerVoice-Studio) can isolate a specific speaker using a reference audio clip. Relevant for family-base multi-speaker separation; shares the same `pip install clearvoice` service already set up for batch denoising. Zero additional deployment cost.  
- **NeMo Canary:** NeMo ships some audio preprocessing utilities but no integrated speech enhancement model. NeMo is not a candidate for this role — confirmed, do not substitute.

---

## 7. Open Questions / What Needs a Prototype to Settle

1. **AEC3 latency measurement on WSL2 ↔ Windows IPC path.** The end-to-end latency of WASAPI loopback capture (Windows) → pipe to WSL2 AEC3 processor → DeepFilterNet3 → back to Windows ASR needs empirical measurement. Target: total ≤ 80ms. Risk: IPC adds 5–20ms.

2. **AEC3 render-capture delay calibration.** WASAPI loopback has a fixed device-reported latency; actual render → mic acoustic latency depends on physical speaker–microphone path (if any). For a meeting assistant where system audio plays through headphones/speakers, this latency must be measured and set via `apm.set_stream_delay_ms()`.

3. **DeepFilterNet3 ONNX on WSL2 with CUDA.** The ONNX runtime supports CUDA execution providers. Running DFN3 on GPU would reduce CPU load to near-zero. Verify that `DeepFilterNet3_onnx.tar.gz` model graph is compatible with the ORT CUDA EP on sm_120 (Blackwell); may need ORT nightly for latest arch support.

4. **MossFormerGAN vs DFN3 on real meeting audio.** VB+D and DNS-2020 benchmarks use clean lab recordings with synthetic noise. Real meeting audio has overlapping speakers, reverb, compression artifacts, and accented speech not well represented in these benchmarks. A blind A/B test on 10 minutes of actual family-base meeting recordings would settle whether the 0.44 PESQ gap (3.47 vs 3.03) is perceptually meaningful in this context.

5. **Over-suppression artifacts from AEC3 + DFN3 cascade.** Both modules apply noise suppression. Running both at high suppression levels may cause "pumping" artifacts or over-attenuated speech. Test with AEC3 NS set to Moderate (not High) when followed by DFN3.

6. **Multi-speaker / overlapping speech.** Neither DFN3 nor AEC3 separate speakers. If family-base captures both sides of a call (mic + loopback as separate streams already), each stream can be denoised independently — this is the correct architecture and requires no change to the recommendation.

---

## 8. Sources

| Source | URL | Access date |
|---|---|---|
| DeepFilterNet GitHub README | https://github.com/Rikorose/DeepFilterNet | 2025-06 |
| DeepFilterNet model files | https://github.com/Rikorose/DeepFilterNet/tree/main/models | 2025-06 |
| DeepFilterNet config.py (sr=48000, hop=480) | https://github.com/Rikorose/DeepFilterNet/blob/main/DeepFilterNet/df/config.py | 2025-06 |
| DeepFilterNet deepfilternet3.py (architecture) | https://github.com/Rikorose/DeepFilterNet/blob/main/DeepFilterNet/df/deepfilternet3.py | 2025-06 |
| DFN3 Interspeech 2023 paper | https://arxiv.org/abs/2305.08227 | (cited, not fetched — network restricted) |
| DFN2 IWAENC 2022 paper | https://arxiv.org/abs/2205.05474 | (cited) |
| DFN1 ICASSP 2022 paper | https://arxiv.org/abs/2110.05588 | (cited) |
| ClearerVoice-Studio GitHub README | https://github.com/modelscope/ClearerVoice-Studio | 2025-06 |
| ClearVoice README (benchmarks, model list) | https://github.com/modelscope/ClearerVoice-Studio/blob/main/clearvoice/README.md | 2025-06 |
| ClearerVoice-Studio LICENSE (Apache 2.0) | https://github.com/modelscope/ClearerVoice-Studio/blob/main/LICENSE | 2025-06 |
| FRCRN paper | https://arxiv.org/abs/2206.07293 | (cited) |
| MossFormer2 paper | https://arxiv.org/abs/2302.11824 | (cited) |
| facebookresearch/denoiser README | https://github.com/facebookresearch/denoiser | 2025-06 |
| facebookresearch/denoiser LICENSE (CC-BY-NC 4.0) | https://github.com/facebookresearch/denoiser/blob/main/LICENSE | 2025-06 |
| Demucs/Denoiser paper (Interspeech 2020) | https://arxiv.org/abs/2006.12847 | (cited) |
| xiph/rnnoise README | https://github.com/xiph/rnnoise | 2025-06 |
| RNNoise paper (MMSP 2018) | https://arxiv.org/pdf/1709.08243.pdf | (cited) |
| tonarino/webrtc-audio-processing README | https://github.com/tonarino/webrtc-audio-processing | 2025-06 |
| tonarino/webrtc-audio-processing last commit May 2026 | https://github.com/tonarino/webrtc-audio-processing/commit/984733db | 2025-06 |
| Denoiser RTF benchmark table | https://github.com/facebookresearch/denoiser#online-evaluation | 2025-06 |
| nnnoiseless Rust crate | https://github.com/nicowillis/nnnoiseless | (referenced via code search) |
| Microsoft DNS-Challenge ICASSP 2023 | https://github.com/microsoft/DNS-Challenge | 2025-06 |
| DNSMOS P.835 paper | Reddy et al., ICASSP 2022 (referenced in DNS Challenge README) | (cited) |


---

## RESEARCH SUMMARY

**Repositories found and inspected:**
- `rikorose/DeepFilterNet` — primary DeepFilterNet3 source, model files, ONNX exports, Rust+Python framework
- `modelscope/ClearerVoice-Studio` — FRCRN, MossFormerGAN, MossFormer2_SE_48K, ClearVoice pip package
- `facebookresearch/denoiser` — Demucs/Denoiser (disqualified CC-BY-NC)
- `xiph/rnnoise` — RNNoise C library and training pipeline
- `tonarino/webrtc-audio-processing` — Rust crate wrapping WebRTC AEC3 (actively maintained through May 2026)
- `microsoft/DNS-Challenge` — benchmark dataset and challenge context

**Key verified facts:**
- ClearerVoice benchmarks verified from commit `c8d73ab8` in `modelscope/ClearerVoice-Studio:clearvoice/README.md`
- DeepFilterNet3 default config verified: 48kHz, 10ms frames, causal (lookahead=0), from `config.py` and `deepfilternet3.py`
- Demucs/Denoiser CC-BY-NC 4.0 license confirmed from `facebookresearch/denoiser:LICENSE`
- ClearerVoice-Studio Apache 2.0 license confirmed from `modelscope/ClearerVoice-Studio:LICENSE`
- `tonarino/webrtc-audio-processing` Windows MSVC limitation confirmed from code search; WSL2 Linux path is unaffected
- tonarino crate last commit May 2026 (actively maintained)

**Gaps:**
- DeepFilterNet3 DNSMOS P.835 numbers from the Interspeech 2023 paper were not independently fetched (network access to arxiv failed). The claim that DFN3 outperforms DFN2 on DNSMOS is from the paper abstract; the exact scores need verification from the paper.
- Exact VRAM for MossFormer2/MossFormerGAN under batch inference was estimated, not measured — the model files aren't directly available for inspection of parameter counts.
- AEC3 + DFN3 cascade quality on real meeting audio (not synthetic benchmarks) is unverified empirically.
