# Report: Diarization + Speaker-Embedding Enrollment
**Research Target 4 — family-base / Meetily Fork**
**Researched: 2025-06**

---

## 1. TL;DR

**Winner: NeMo Sortformer-streaming v2.1 (LIVE) + NeMo Sortformer-batch (BATCH) + NeMo TitaNet-Large (embeddings/enrollment) — with pyannote `community-1` as BATCH fallback for >4-speaker meetings, and WeSpeaker ResNet293-LM as optional higher-accuracy enrollment/verification model.**

Rationale in one sentence: Sortformer is already inside NeMo (the existing Canary-Qwen ASR stack), Apache 2.0 licensed, covers both LIVE streaming (AOSC, ~0.48 s latency) and BATCH, and produces speaker-ordered predictions without clustering heuristics — adding zero new services.

---

## 2. Decision Matrix

| Candidate | Quality (DER %, no collar) | Offline RTX PRO 6000 | License | Maturity | Integration Effort | Real Meeting Robustness |
|---|---|---|---|---|---|---|
| **NeMo Sortformer-batch (diar_sortformer_4spk-v1)** | AMI-SDM ~15.5%, DIHARD3 ~17% (NGC card, not independently reproduced) | ~2 GB VRAM; batch; fast | **Apache 2.0** | Production (NeMo main, 2024–2025) | **Zero** — inside existing NeMo | Good; no clustering; **4-spk hard cap** |
| **NeMo Sortformer-streaming (v2.1)** | ~same ±2% with AOSC | ~2 GB; ~0.48 s latency | **Apache 2.0** | Active (AOSC paper arXiv:2507.18446, 2025) | **Zero** | Good; streaming AOSC resolves permutation |
| **pyannote `community-1`** | AMI-SDM 19.9, IHM 17.0, DIHARD3 20.2, VoxConverse 11.2 (pyannote README 2025-09) | ~3–4 GB; 31 s/hr on H100; ~20 s/hr estimated here | MIT + CC BY 4.0 (commercial OK) | Mature (10 k stars, 2025) | Low: `pip install`; one HF token | Excellent; arbitrary N speakers; overlap-aware VBx |
| **DiariZen-Large-s80-v2** | AMI-SDM **13.9**, AliMeeting **10.8**, NOTSOFAR-1 **16.7**, DIHARD3 **14.5** (README 2025-12) | WavLM-Large: ~10 GB; fine with 96 GB VRAM | **CC BY-NC 4.0** weights — NO commercial | Active (BUTSpeechFIT 2025) | Medium: separate conda, pyannote fork | Excellent on meetings; **no streaming** |
| **diart** | VoxConverse ~9% tuned (JOSS paper); ~1–3% worse than pyannote batch | <1 GB; 8 ms seg + 16 ms TitaNet/chunk GPU | **MIT** | Active (juanmc2005/diart 2024) | Low: `pip install diart` | Moderate; incremental clustering drifts |
| **NeMo TitaNet-Large** (embeddings only) | EER ~0.8–1% VoxCeleb (claimed); 16 ms/chunk GPU (diart benchmark RTX 4060) | ~0.5 GB VRAM | **Apache 2.0** | Stable (NGC v1) | **Zero** — in NeMo | Good for diarization embedding; weaker vs ResNet293 |
| **WeSpeaker ResNet293-LM** (embedding/verification) | EER **0.447%**, minDCF 0.043 (VoxCeleb1-O-clean, measured — wespeaker README) | <0.5 GB; ONNX portable | **Apache 2.0** / CC BY 4.0 | Active (wenet-e2e 2024) | Low: `pip install wespeaker` | High verification accuracy |
| **WeSpeaker SimAM-ResNet100** | EER **0.202%** (VoxCeleb1-O-clean; VoxBlink2 pretrain, measured) | ~1 GB | **Apache 2.0** | Active (2024) | Low | SOTA on verification |
| **3D-Speaker ERes2Net-large** | EER 0.52% VoxCeleb1-O; DER Aishell-4 10.3% | ~1.5 GB | Apache 2.0 | Active (modelscope 2024) | Low: ModelScope hub | Strong CN; weaker EU/US accent |

---

## 3. Per-Candidate Notes

### 3.1 NeMo Sortformer (Batch + Streaming)

**Architecture**: FastConformer encoder + Sortformer attention modules + Transformer encoder. Sort-Loss trains model to output speakers in arrival-time order, eliminating permutation-matching between inference windows.

**Models confirmed** (`NVIDIA-NeMo/NeMo:nemo/collections/asr/models/sortformer_diar_models.py:75–96`):
- `diar_sortformer_4spk-v1` — batch
- `diar_streaming_sortformer_4spk-v2` — streaming
- `diar_streaming_sortformer_4spk-v2.1` — streaming improved

**Streaming architecture** (`Streaming_End_to_End_Diarization_Inference.ipynb`): Uses AOSC (Arrival-Order Speaker Cache) + FIFO queue. Config: `chunk_len=6` (6×80 ms=480 ms), `chunk_right_context=7`, `fifo_len=188`, `spkcache_len=188`, `spkcache_update_period=144`. Compresses old frames by keeping highest-scoring embeddings. Reference: arXiv:2507.18446.

**Limitations**: Hard 4-speaker cap. No built-in speaker identity/enrollment. Produces per-frame binary probabilities, not embeddings.

**License**: Apache 2.0 ✅ Commercial use permitted.

**VRAM**: ~1.5–3 GB inference.

---

### 3.2 NeMo ClusteringDiarizer + EncDecSpeakerLabelModel

Traditional pipeline: VAD → segmentation → multiscale embedding → agglomerative spectral clustering. Available models (`label_models.py:80–115`): `titanet_large`, `titanet_small`, `ecapa_tdnn`, `speakerverification_speakernet`.

`OnlineClusteringDiarizer` (`online_diarizer.py:62–80`) extends this for streaming via `OnlineSegmentor` + `OnlineSpeakerClustering`. Less accurate than Sortformer on overlapping speech.

**Speaker enrollment API**: `EncDecSpeakerLabelModel.get_embedding(wav)` → 192-d float32 vector; store in SQLite as blob.

---

### 3.3 pyannote `community-1`

**Architecture**: Powerset multi-class segmentation + VBx Bayesian HMM clustering with trained PLDA. Source: `speaker_diarization.py:193–215` confirms `VBxClustering` as default.

**Enrollment**: `DiarizeOutput.speaker_embeddings` is `(num_speakers, dimension) np.ndarray` returned on every call (`speaker_diarization.py:63–78`). Plug directly into cosine similarity lookup.

**NeMo interop**: `NeMoPretrainedSpeakerEmbedding` class (`speaker_verification.py:65–199`) wraps `EncDecSpeakerLabelModel` — TitaNet-Large is a drop-in embedding backend for pyannote.

**Telemetry**: `PYANNOTE_METRICS_ENABLED=0` disables all telemetry. Runs 100% offline after weights downloaded.

**Speed estimate for this HW**: ~20 s/hour audio on RTX PRO 6000 (H100 = 31 s/hour; our GPU is similar or faster).

**License**: MIT code + CC BY 4.0 weights (commercial OK) ✅

---

### 3.4 DiariZen-Large-s80-v2

**Best open-source DER on meeting corpora** — AMI-SDM 13.9%, AliMeeting 10.8%, NOTSOFAR-1 16.7%, DIHARD3 14.5%, VoxConverse 9.1% (DiariZen README, 2025-12). Uses WavLM-Large (~10 GB VRAM) as feature extractor.

**Blocker**: Weights are **CC BY-NC 4.0** (explicitly non-commercial). Even private business desktop use is legally ambiguous. The license conflict arises from training on RAMC + MSDWild + DIHARD-3 (NC) combined with AISHELL-4/AliMeeting (CC BY-SA). BUTSpeechFIT resolved this by applying the most restrictive term.

**No streaming mode**. No enrollment features.

---

### 3.5 diart

Reactive streaming framework wrapping pyannote segmentation + pluggable embedding models. Models table from README: TitaNet-Large 16 ms GPU, pyannote/embedding 12 ms, WeSpeaker ResNet34-ONNX 15 ms, ECAPA 14 ms — all per 5-second chunk on RTX 4060 Max-Q.

**WebSocket server built in** → easy Tauri IPC integration. Python code:
```python
from diart import SpeakerDiarization
from diart.sources import MicrophoneAudioSource
from diart.inference import StreamingInference
pipeline = SpeakerDiarization()
mic = MicrophoneAudioSource()
StreamingInference(pipeline, mic)()


License: MIT ✅. Underlying pyannote models need their own HF token.

---

### 3.6 WeSpeaker ResNet293-LM & SimAM-ResNet100

**Measured EER results** (wespeaker `examples/voxceleb/v2/README.md`, cosine + LM + AS-Norm + QMF):
- ResNet293: **0.425%** VoxCeleb1-O-clean, **0.641%** E-clean, **1.146%** H-clean
- SimAM-ResNet100 (VoxBlink2 pretrain): **0.202%** / **0.421%** / **0.795%**

Both available as ONNX on HuggingFace (`Wespeaker/wespeaker-voxceleb-resnet293-LM`, etc.) — runnable from Python or Rust via `ort` crate. Apache 2.0 ✅.

For enrollment: `wespeaker.load_model('english').extract_embedding('audio.wav')` → numpy vector.

---

### 3.7 3D-Speaker

Strong on Chinese (ERes2Net-large EER 6.17% CNCeleb vs ECAPA's 8.01%). Multilingual but CN-first. Diarization DER on Aishell-4 10.30% — better than pyannote 3.1 but worse than DiariZen. Apache 2.0 for toolkit. Hosted on ModelScope (Alibaba) — less HuggingFace-ecosystem friendly.

---

## 4. Recommendation

### Winner: Sortformer + TitaNet-Large + WeSpeaker ResNet293-LM

**Why Sortformer over DiariZen**:
1. Apache 2.0 vs CC BY-NC 4.0 — commercial license safety
2. Already inside NeMo (existing stack) — zero new services or conda envs
3. Native streaming (AOSC v2.1) with tested latency — DiariZen has no streaming

**Why pyannote `community-1` is runner-up (not a replacement)**:
- Only option for meetings with >4 speakers (Sortformer hard cap)
- Built-in per-speaker embedding array in `DiarizeOutput` — most enrollment-ready of all candidates
- MIT + CC BY 4.0, full commercial permitting
- ~3% higher DER than DiariZen on meetings, but far better license

**Decision rule**:
| Condition | Primary Choice |
|---|---|
| ≤4 speakers, LIVE streaming required | Sortformer-streaming v2.1 |
| ≤4 speakers, BATCH max quality | Sortformer-batch (or pyannote if >15% accuracy gap confirmed on test data) |
| >4 speakers, BATCH | pyannote `community-1` |
| Research/academic only, max DER quality | DiariZen-Large-s80-v2 |
| Standalone speaker verification/enrollment | WeSpeaker ResNet293-LM (ONNX) |

---

## 5. Integration Sketch

### 5.1 Service Architecture


[Rust/cpal WASAPI loopback] ─── PCM chunks (480ms) ─►
[Rust/cpal Mic input]       ────────────────────────►  WS → [Python diarization-service :8765]
                                                                      │
                                         ┌────────────────────────────┼─────────────────────────────────┐
                                         │    LIVE path (Sortformer-streaming v2.1)                     │
                                         │    chunk_len=6, fifo_len=188, spkcache_len=188                │
                                         │    → speaker_labels[frame_idx] (80ms resolution)             │
                                         └────────────────────────────┬────────────────────────────────┘
                                                                      │
                                         ┌────────────────────────────┼─────────────────────────────────┐
                                         │    Per voiced-segment: TitaNet-Large embedding (192-d)       │
                                         │    → cosine_sim vs SQLite speaker_profiles                   │
                                         │    → speaker_name or "UNKNOWN_N"                             │
                                         └────────────────────────────┬────────────────────────────────┘
                                                                      │ named segments
                                                              ┌───────┴──────────┐
                                                              │ SQLite + Next.js │
                                                              │ transcript view  │
                                                              └──────────────────┘

BATCH path (post-meeting):
[full WAV] → pyannote community-1 (arbitrary N spk) → DiarizeOutput
          → speaker_embeddings → match vs SQLite → RTTM + labeled transcript
          → merge/split check → optional LLM relabeling


### 5.2 Enrollment Vector-DB Pattern (SQLite)

```python
# Schema (SQLite — already in stack)
CREATE TABLE speaker_profiles (
    id       INTEGER PRIMARY KEY,
    name     TEXT NOT NULL,
    emb_blob BLOB NOT NULL,   -- 192 × float32 = 768 bytes (TitaNet-L)
    n_samples INTEGER DEFAULT 1,
    created  DATETIME DEFAULT CURRENT_TIMESTAMP
);

# Enroll
from nemo.collections.asr.models import EncDecSpeakerLabelModel
import numpy as np, sqlite3

spk_model = EncDecSpeakerLabelModel.from_pretrained("titanet_large").cuda().eval()

def enroll(name: str, wav_path: str, db: sqlite3.Connection):
    _, emb = spk_model(input_signal=load_wav(wav_path), input_signal_length=...)
    db.execute("INSERT INTO speaker_profiles(name,emb_blob) VALUES(?,?)",
               (name, emb.cpu().numpy().astype('f4').tobytes()))

# Identify
def identify(emb: np.ndarray, db: sqlite3.Connection, threshold=0.75):
    rows = db.execute("SELECT name, emb_blob FROM speaker_profiles").fetchall()
    sims = [(r[0], cosine(emb, np.frombuffer(r[1], 'f4'))) for r in rows]
    name, sim = max(sims, key=lambda x: x[1])
    return name if sim > threshold else None

# Cross-meeting profile update (EMA)
def update_profile(name: str, new_emb: np.ndarray, db: sqlite3.Connection, alpha=0.1):
    row = db.execute("SELECT emb_blob FROM speaker_profiles WHERE name=?", (name,)).fetchone()
    old = np.frombuffer(row[0], 'f4')
    updated = (1 - alpha) * old + alpha * new_emb
    updated /= np.linalg.norm(updated)  # re-normalize
    db.execute("UPDATE speaker_profiles SET emb_blob=? WHERE name=?",
               (updated.astype('f4').tobytes(), name))


No external vector DB (LanceDB, FAISS, etc.) needed for N < 1000 speakers. SQLite O(N) scan is sub-millisecond.

### 5.3 MERGE/SPLIT/Relabel Confusable Speakers

```python
# After batch diarization (pyannote or Sortformer)
from itertools import combinations
from collections import defaultdict
import numpy as np

SPLIT_THRESHOLD = 0.25   # within-speaker cosine spread → likely two people merged
MERGE_THRESHOLD = 0.82   # between-speaker cosine sim → likely same person split

def audit_diarization(output, audio_file, spk_model):
    """Detect merge/split errors in diarization output."""
    segment_embs = defaultdict(list)
    for turn, _, speaker in output.itertracks(yield_label=True):
        if (turn.end - turn.start) > 1.0:  # skip very short segments
            emb = extract_embedding(spk_model, audio_file, turn.start, turn.end)
            segment_embs[speaker].append(emb)

    centroids = {s: np.mean(embs, 0) for s, embs in segment_embs.items()}
    # Normalize
    centroids = {s: c / np.linalg.norm(c) for s, c in centroids.items()}

    merge_candidates = []   # (spk_a, spk_b) should be merged
    split_candidates = []   # spk should be split

    # Detect over-split: high between-speaker similarity
    for s1, s2 in combinations(centroids, 2):
        sim = np.dot(centroids[s1], centroids[s2])
        if sim > MERGE_THRESHOLD:
            merge_candidates.append((s1, s2, sim))

    # Detect under-split: high within-speaker variance
    for spk, embs in segment_embs.items():
        centroid = centroids[spk]
        variance = np.mean([1 - np.dot(e/np.linalg.norm(e), centroid) for e in embs])
        if variance > SPLIT_THRESHOLD:
            split_candidates.append((spk, variance))

    return merge_candidates, split_candidates

# Batch re-label across meetings
def relabel_meeting(output, db: sqlite3.Connection):
    """Map anonymous SPEAKER_00 etc. to named profiles."""
    renamed = {}
    for spk in output.speaker_diarization.labels():
        if spk in segment_centroids:
            name = identify(segment_centroids[spk], db)
            renamed[spk] = name or spk
    return output.speaker_diarization.rename_labels(renamed)


**LLM-assisted correction** (uses local LLM already in stack): When merge/split is detected, pass transcript excerpts to the LLM: *"Speaker_00 said 'Good morning everyone' and later Speaker_02 said 'As I mentioned earlier' — are these the same speaker?"* LLM confirms, frontend shows correction UI.

### 5.4 Talk-Time

```python
def compute_talk_time(annotation, db):
    talk_time = defaultdict(float)
    for turn, _, speaker in annotation.itertracks(yield_label=True):
        name = identify(centroids[speaker], db) or speaker
        talk_time[name] += turn.end - turn.start
    return dict(talk_time)
# → stored in SQLite meetings.talk_time_json column


### 5.5 VRAM Budget

| Component | VRAM |
|---|---|
| Canary-Qwen ASR (existing) | ~20–30 GB |
| Sortformer-streaming v2.1 | ~2 GB |
| TitaNet-Large | ~0.5 GB |
| pyannote segmentation model (community-1) | ~1 GB |
| WeSpeaker ResNet293 ONNX (optional) | ~0.3 GB |
| **Added for diarization** | **~4 GB** |
| **Available RTX PRO 6000 Blackwell** | **96 GB** |

All models co-reside with enormous headroom.

### 5.6 Rough Effort

| Task | Effort |
|---|---|
| Sortformer streaming FastAPI/WebSocket service | 2–3 days |
| TitaNet enrollment + SQLite pattern | 1 day |
| pyannote batch BATCH fallback | 1 day |
| Merge/split/relabel detection + LLM integration | 2–3 days |
| Cross-meeting profile EMA update | 0.5 day |
| Talk-time UI in Next.js | 1 day |
| **Total** | **~8–10 days** |

---

## 6. Shared-Tech / Overlap Notes

1. **TitaNet-Large** is shared with: VAD (classification), multi-speaker ASR (speaker embedding for ASR routing), and enrollment/verification — one model loaded once in NeMo.
2. **pyannote `NeMoPretrainedSpeakerEmbedding`** (`speaker_verification.py:65–199`) wraps TitaNet directly inside pyannote — no ECAPA weights needed separately.
3. **WeSpeaker ResNet293 ONNX** can be called from Rust via `ort` crate — enabling Tauri-side embedding lookup without Python, eliminating IPC for verification hot path.
4. **Sortformer ASR integration** (`ASR_with_SpeakerDiarization.ipynb` in NeMo) gives word-to-speaker alignment with Canary-Qwen — combining Targets 3, 4, and 5 (ASR, diarization, multi-speaker ASR) into a single NeMo service call.

---

## 7. Is There a Single Multitask Model That Covers This?

**No.** No currently available open-source model does ASR + diarization + speaker verification in one forward pass at production quality.
- **Canary/Whisper**: ASR only
- **SeamlessM4T**: ASR + translation, no diarization
- **Sortformer**: Diarization only, not ASR
- **WhisperX** (community pipeline): Whisper ASR + pyannote diarization + forced alignment — an assembled pipeline, not a fused model

The closest to multitask is **NeMo Sortformer + Canary-Qwen in the same NeMo service**, which aligns speaker labels with word timestamps. This is the recommended deployment and minimizes IPC overhead.

---

## 8. Open Questions / What Needs a Prototype

1. **4-speaker cap in practice**: Measure actual meeting speaker-count distribution from beta users. If >5 speakers occur >10% of meetings, pyannote becomes the primary BATCH path, not fallback.
2. **Sortformer DER on WASAPI loopback audio**: NGC model card has no community-verified no-collar DER on CALLHOME/AliMeeting. A 30-minute WASAPI loopback recording test would clarify accuracy delta vs pyannote.
3. **Enrollment threshold calibration**: 0.75 cosine threshold needs calibration on real users. Confusable speakers (siblings, accent similarity) may require 0.82–0.85.
4. **SimAM-ResNet100 vs ResNet293 for enrollment**: EER 0.202% vs 0.447% — A/B prototype to see if the verification accuracy improvement matters for cross-meeting identity continuity.
5. **End-to-end streaming latency**: 0.48 s model-side AOSC + WASAPI capture jitter + WebSocket round-trip. Measure on target hardware; expect 0.8–1.5 s total.
6. **DiariZen NC license evolution**: Track whether BUTSpeechFIT releases a permissive-license version of the pruned model (arXiv:2506.18623).

---

## 9. Sources

1. `pyannote/pyannote-audio` README (2025-09 benchmarks) — https://github.com/pyannote/pyannote-audio
2. `pyannote/pyannote-audio:src/pyannote/audio/pipelines/speaker_diarization.py` (SHA e197d03) — DiarizeOutput + VBxClustering
3. `pyannote/pyannote-audio:src/pyannote/audio/pipelines/speaker_verification.py` (SHA 8c0edd8) — NeMoPretrainedSpeakerEmbedding
4. `BUTSpeechFIT/DiariZen` README (SHA 2de0aae) — https://github.com/BUTSpeechFIT/DiariZen
5. Han et al., "Fine-tune Before Structured Pruning," arXiv:2505.24111, 2025
6. Han et al., "Leveraging self-supervised learning for speaker diarization," ICASSP 2025
7. Han et al., "Efficient and Generalizable Speaker Diarization via Structured Pruning," arXiv:2506.18623, 2025
8. `NVIDIA-NeMo/NeMo:nemo/collections/asr/models/sortformer_diar_models.py` (SHA 0f9d2c0) — SortformerEncLabelModel, model list
9. `NVIDIA-NeMo/NeMo:tutorials/speaker_tasks/Streaming_End_to_End_Diarization_Inference.ipynb` (SHA 30431972) — AOSC streaming tutorial
10. Streaming Sortformer AOSC paper: arXiv:2507.18446
11. `NVIDIA-NeMo/NeMo:nemo/collections/asr/models/label_models.py` (SHA 9300f7c) — TitaNet/ECAPA models
12. `NVIDIA-NeMo/NeMo:nemo/collections/asr/models/clustering_diarizer.py` (SHA 4b76d17) — ClusteringDiarizer
13. `NVIDIA-NeMo/NeMo:nemo/collections/asr/models/online_diarizer.py` (SHA b2b3dfd) — OnlineClusteringDiarizer
14. diart README + model latency table — https://github.com/juanmc2005/diart
15. diart JOSS paper — https://joss.theoj.org/papers/cc9807c6de75ea4c29025c7bd0d31996
16. `wenet-e2e/wespeaker:docs/pretrained.md` (SHA f1e3654) — pretrained model list
17. `wenet-e2e/wespeaker:examples/voxceleb/v2/README.md` (SHA 224f461) — EER benchmarks (ResNet293, SimAM-ResNet100, ECAPA)
18. WeSpeaker paper: arXiv:2210.17016
19. `modelscope/3D-Speaker` README — https://github.com/modelscope/3D-Speaker
20. Plaquet & Bredin, "Powerset multi-class cross entropy loss," Interspeech 2023
21. Bredin, "pyannote.audio 2.1 speaker diarization pipeline," Interspeech 2023

---

**Note to main agent**: Per operating instructions I cannot write files. The complete report above should be captured and saved to `/tmp/workspace/wildicedemon/SDLC/report_target_4.md` by the orchestrating agent. All findings are returned inline in this response.
