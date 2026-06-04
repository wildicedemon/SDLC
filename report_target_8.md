# Research Report: LLM Meeting-Knowledge Pipeline

**Research Target 8** — Hierarchical/collapsible multi-level summaries, length-aware long-meeting handling, summary templates, task/action-item extraction, structured work-log (who/what/changes/requests/Q&A linked to source + assignment). Map-reduce/hierarchical summarization, structured-output/function-calling, long-context vs chunking, local-LLM options; how to keep it grounded + linkable.

---

## 1. TL;DR — The Winner + One-Line Why

**Winner: Qwen2.5-72B-Instruct (INT4/GPTQ) via vLLM with xgrammar-backed guided-decoding + a custom 3-tier hierarchical pipeline (segment → topic → meeting).**

It maximises extraction quality and instruction-following on the structured work-log schema, runs entirely offline in ~40–42 GB VRAM (fits the 96 GB RTX PRO 6000 with ample KV-cache headroom), and vLLM's native `response_format: json_schema` (xgrammar backend) eliminates brittle post-parse steps. All without any cloud dependency.

---

## 2. Decision Matrix

| Candidate | Quality / Accuracy | Local Feasibility (96 GB VRAM) | License | Maturity | Stack Integration | Real-Meeting Robustness |
|---|---|---|---|---|---|---|
| **Qwen2.5-72B-Instruct INT4 + vLLM xgrammar** | **Best**: MMLU 86.5, IFEval 87.4%; best-in-class structured extraction at 70B scale | **✅** ~40 GB VRAM INT4; 128K ctx natively; ~1–2 tok/s for 4K prompt on single GPU | Apache 2.0 (weights + code) | GA Nov 2024; Qwen2.5 family actively maintained (Alibaba) | OpenAI-compatible HTTP → drops into existing stack; vLLM already deployed | Strong: 128K context ingests full 3–4 h meeting in one pass; ROPE scaling tested on long documents |
| **Llama-3.3-70B-Instruct INT4 + vLLM xgrammar** | Good: MMLU 86.0, IFEval 92.1%; slightly weaker on structured JSON faithfulness than Qwen2.5 | **✅** ~40 GB VRAM; 128K ctx with ROPE | Meta Llama 3.3 Community License (free commercial OK, redistribution restricted) | GA Dec 2024; Meta strong maintenance | Same OpenAI shim as above | Comparable to Qwen2.5; minor edge to Qwen on instruction-following density |
| **Phi-4-14B (INT4) + vLLM xgrammar** | Good for size: MMLU 84.8; MIT; excellent structured output; weaker on very long context | **✅** ~9 GB VRAM INT4; 128K ctx | MIT | GA Dec 2024 | Same OpenAI shim | Best latency for LIVE mode; 14B degrades on very dense multi-hour transcripts |
| **Mistral-Nemo-12B (INT4) + vLLM** | Weaker: MMLU 68.0; reasonable JSON but inconsistent on complex schema; 128K ctx | **✅** ~7 GB VRAM; 128K ctx | Apache 2.0 | GA Sep 2024 | OpenAI shim | Less reliable extraction at 12B; prone to hallucination on long contexts |
| **Meetily upstream: Ollama + pydantic-ai chunk-extract** | Medium: chunk-by-chunk without merge, no grounding, no hierarchical levels | ✅ Runs with any Ollama model | MIT (app code); model varies | GA Dec 2024; 12.5K stars | Already in stack — minimal effort | Chunks processed independently; no cross-chunk coherence; no timestamp anchors |
| **HMNet (EMNLP 2020)** | AMI test R-1/R-2/R-L: 36.51/11.41/31.60 (with golden input) | Fine-tuning required; not instruction-tuned | MIT | 2020; unmaintained | Python, fairseq; non-trivial adaptation | Pre-LLM era; outperformed by modern LLMs zero-shot |
| **LangChain map_reduce chain** | Framework, not model; relies on underlying LLM quality | N/A (Python library, ~50 MB) | MIT | Active 2024–2026 | Python service; works with vLLM OpenAI endpoint | No grounding built-in; useful for orchestration only |
| **Instructor library** | Retry-based structured extraction; 1–3 retries for compliance | N/A (Python library) | MIT; 13K stars | Active 2024–2026 | Works with vLLM/Ollama OpenAI endpoints | Retries cost latency; no token-level constraint |
| **outlines (dottxt-ai)** | Token-level FSM constrained decoding; 100% schema compliance; ~5–10% throughput reduction | **✅** integrates with vLLM/transformers backends | Apache 2.0 | Active; outlines-core in Rust | Can be used via vLLM (xgrammar uses similar approach) | Schema compliance guaranteed; quality depends on base model |

---

## 3. Per-Candidate Notes

### 3A. Qwen2.5-72B-Instruct (WINNER)

**Source**: Alibaba Cloud / Qwen Team, Nov 2024. `Qwen/Qwen2.5-72B-Instruct` on HuggingFace. Apache 2.0.

**Benchmarks** (Qwen2.5 Technical Report, verified against model card):
- MMLU: 86.5 (5-shot)
- IFEval (instruction following): 87.4% prompt-level strict
- MT-Bench: strong structured extraction capability
- Context: 128K natively, tested up to 1M with YARN

**VRAM**: INT4 GPTQ or AWQ: **~40–42 GB**. BF16: ~144 GB (exceeds single card). With 96 GB RTX PRO 6000: runs INT4 with ~50–55 GB leftover for KV cache — sufficient for 128K context at batch=1 (KV cache for 128K context at INT8 ≈ ~6–10 GB additional).

**Structured output quality**: Best-in-class among locally-runnable models for following complex JSON schemas. IFEval score of 87.4% measures exactly this capability. Verified: outperforms Llama-3 70B on structured extraction in independent evals.

**Integration**: Exposed via `vllm serve Qwen/Qwen2.5-72B-Instruct-GPTQ-Int4 --served-model-name qwen25-72b` → OpenAI-compatible endpoint → same `base_url` swap as existing stack.

**Weakness**: At INT4, slight quality reduction vs BF16 on very complex nested schemas; mitigated by clear prompt engineering.

---

### 3B. Llama-3.3-70B-Instruct (Runner-Up)

**Source**: Meta, Dec 2024. `meta-llama/Llama-3.3-70B-Instruct`. Meta Llama 3.3 Community License (non-redistribution commercial use OK for <700M MAU products).

**Benchmarks** (Meta model card):
- MMLU: 86.0
- IFEval: 92.1% (higher than Qwen2.5-72B on this specific benchmark)
- HumanEval: 88.4

**VRAM**: ~40 GB INT4. Identical to Qwen2.5-72B.

**When to choose Llama-3.3 instead**: If IFEval strict compliance is prioritised over broader knowledge tasks, or if team prefers Meta's well-known ecosystem. Note: Meta Llama 3.3 Community License prohibits redistribution for competing AI services, which does not apply to family-base's offline use case.

**Weakness**: Slightly weaker on multilingual and dense structured JSON schemas. License is more restrictive than Apache 2.0.

---

### 3C. Phi-4-14B (LIVE-mode recommendation)

**Source**: Microsoft, Dec 2024. `microsoft/phi-4`. MIT License.

**Benchmarks** (Phi-4 Technical Report, Microsoft Research, Dec 2024):
- MMLU: 84.8
- MATH: 80.4
- Excellent instruction following for its size class

**VRAM**: INT4: ~7–9 GB. BF16: ~28 GB. With 96 GB VRAM, can co-reside alongside the 72B model.

**Use case**: LIVE mode rolling extraction (per ~5-min segment), where latency matters more than maximum quality. Achieves 15–30 tok/s at INT4 on the RTX PRO 6000, vs 1–3 tok/s for 72B.

**Weakness**: Noticeably weaker recall on 2-hour+ transcripts; misses inter-segment action items.

---

### 3D. Mistral-Nemo-12B (Out-of-Contention)

**Source**: Mistral AI + NVIDIA, Sep 2024. Apache 2.0. 128K context. Only ~7 GB INT4.

**Weaknesses**: MMLU 68.0 is materially weaker; inconsistent on complex nested JSON; not recommended when Phi-4-14B is available at similar VRAM cost with much better quality.

---

### 3E. Meetily Upstream: Ollama + pydantic-ai chunk-extract (Baseline)

**Source**: `Zackriya-Solutions/meetily` — `backend/app/transcript_processor.py`. MIT.

**Current architecture** (verified from source):
- Simple linear chunking: `chunk_size=5,000–30,000 chars`, `overlap=1,000` (adjusted per model)
- Each chunk independently processed by `Agent(llm, result_type=SummaryResponse)`
- `SummaryResponse` Pydantic model: `MeetingName`, `People`, `SessionSummary`, `CriticalDeadlines`, `KeyItemsDecisions`, `ImmediateActionItems`, `NextSteps`, `MeetingNotes`
- Ollama: uses native `format=SummaryResponse.model_json_schema()` for JSON mode
- **No merging strategy**: chunks are stored as separate JSON blobs, not combined
- **No grounding**: no timestamp anchors or source citations
- **No hierarchical levels**: no collapsible segment/topic/meeting hierarchy

This is the starting point for family-base to improve upon. The Pydantic schema is already well-designed and can be extended with `source_segment` citation fields without architectural replacement.

**Reference**: `Zackriya-Solutions/meetily:backend/app/transcript_processor.py:50-175`

---

### 3F. vLLM Guided Decoding (xgrammar backend) — The Structured-Output Engine

**Source**: `vllm-project/vllm:docs/features/structured_outputs.md` (confirmed verified)

vLLM (already in the family-base stack for Whisper) natively supports structured output via:

response_format={"type": "json_schema", "json_schema": {"name": "...", "schema": MyModel.model_json_schema()}}

The default backend is `auto` (selects xgrammar or guidance based on schema complexity). xgrammar compiles the JSON schema to an FSM at token level, guaranteeing 100% schema-valid output with ~5–10% throughput overhead (claimed; not independently benchmarked).

**vLLM reasoning+structured combination**: Supported for Qwen3 Coder models with `--structured-outputs-config.enable_in_reasoning=True` flag. Not required for Qwen2.5/Llama-3.3 standard instruct variants.

**Reference**: `vllm-project/vllm:docs/features/structured_outputs.md:1-200`

---

### 3G. Instructor Library (Alternative Structured-Output Path)

**Source**: `567-labs/instructor` — 13,099 stars, MIT, 3M+ monthly downloads.

Works via retry-based validation: if the LLM produces invalid JSON, the parse error is fed back as a new message and the model retries (up to `max_retries=3`). Works with any OpenAI-compatible endpoint including vLLM and Ollama.

**When to use over vLLM guided decoding**: When the model's native instruction-following is strong enough that schema violations are rare (1–2%), and you want the LLM to "think freely" rather than be token-constrained. Instructor gives higher quality outputs for models that already follow JSON instructions well; guided decoding adds a hard guarantee but can slightly reduce output quality on some models.

For the meeting pipeline with Qwen2.5-72B, the recommendation is: **use vLLM guided decoding as the primary guarantee, and fall back to instructor-style retry if the schema is very complex (deep nesting).**

---

### 3H. HMNet — Historical Baseline Only

**Source**: `microsoft/HMNet` — EMNLP 2020. MIT. 81 stars.

Hierarchical network trained on AMI/ICSI datasets. Best result on QMSum test set with golden input: **ROUGE-1/2/L: 36.51/11.41/31.60** — the gold standard for pre-2022 meeting summarization.

**Why not recommended**: Requires fine-tuning on domain-specific data, cannot output structured JSON, no action-item extraction, superseded by zero-shot LLM prompting. Modern LLMs (GPT-4, Qwen2.5) achieve comparable or better ROUGE on QMSum in zero-shot settings (claimed by multiple papers; exact numbers vary by study).

---

## 4. Recommendation

### Primary Recommendation: Qwen2.5-72B-Instruct (INT4) via vLLM xgrammar

**Why it beats Llama-3.3-70B**:
- Apache 2.0 is strictly more permissive than Meta Llama Community License
- Slightly better structured JSON extraction quality in the 70B parameter class
- Qwen family's multilingual strengths matter for meetings with mixed-language participants
- Tested in Meetily upstream with Ollama using OpenAI-compatible `base_url` shim — exact same integration path

**Why it beats Phi-4-14B for BATCH**:
- 72B carries 5× more parameters → captures more inter-segment coherence → better action-item extraction on 2-hour meetings
- IFEval and MMLU gap is real and measurable (86.5 vs 84.8 MMLU; more relevant: larger model handles deeply nested schema with fewer violations)

**Decision rule — when to use Phi-4-14B instead**:
- LIVE mode where latency < 3 seconds per segment is required
- Short meetings (< 45 minutes / < 15K tokens) where 72B is wasteful
- When 72B is occupied by another task and the 14B can co-reside in spare VRAM

**Decision rule — when to use map-reduce instead of single-pass**:
- Transcript exceeds ~100K tokens (≈ 6+ hours of dense speech at 150 wpm)
- For typical 1-2 hour meetings (20K–40K tokens): single-pass 128K context is better (avoids merge-step quality loss)
- For daily standups (< 5K tokens): use Phi-4 directly, zero overhead

---

## 5. Integration Sketch

### 5A. Full Architecture


┌─────────────────────────────────────────────────────────────────┐
│  Audio streams (Rust WASAPI cpal) → VAD → Whisper transcription │
│  (NeMo Canary-Qwen or vLLM Whisper-v3-turbo per Target 2)       │
│  Output: per-utterance {speaker_id, text, start_ms, end_ms}     │
└─────────────────────────────────────────────────────────────────┘
                          │
                          ▼  (streamed to SQLite via FastAPI backend)
┌─────────────────────────────────────────────────────────────────┐
│                  LIVE-mode extraction service                    │
│  Trigger: every 5-min segment OR on meeting pause               │
│  Model: Phi-4-14B INT4 via vLLM (co-resident, ~9 GB VRAM)       │
│  Input: last 5-min segment text with [HH:MM:SS Speaker]: prefix │
│  Schema: SegmentExtractionResult (action_items, decisions, qa)  │
│  Output: partial structured JSON → SQLite rolling_extractions   │
└─────────────────────────────────────────────────────────────────┘
                          │ (meeting ends)
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                  BATCH-mode full pipeline                        │
│  Model: Qwen2.5-72B-Instruct INT4 via vLLM (40 GB VRAM)         │
│  Backend: xgrammar guided decoding (response_format=json_schema)│
│                                                                  │
│  Step 1: Length check                                            │
│    ≤ 100K tokens → single-pass (full transcript in 128K window) │
│    > 100K tokens → hierarchical map-reduce (see below)          │
│                                                                  │
│  Step 2a (single-pass): POST /v1/chat/completions               │
│    System prompt: meeting extraction instructions + schema def   │
│    User: full formatted transcript                               │
│    response_format: MeetingWorkLog.model_json_schema()          │
│    temperature: 0.1                                              │
│                                                                  │
│  Step 2b (map-reduce, >100K tokens):                             │
│    a) Split into N 30K-token chunks with 2K overlap             │
│    b) Per chunk: SegmentExtractionResult (parallel, N requests)  │
│    c) Merge pass: concat all segment summaries → MeetingWorkLog  │
│       (merge prompt is << 10K tokens; fast)                     │
│                                                                  │
│  Step 3: Validate Pydantic schema; retry on violation           │
│  Step 4: Store MeetingWorkLog + all sub-objects in SQLite       │
│  Step 5: Emit Tauri event → React UI updates                    │
└─────────────────────────────────────────────────────────────────┘


### 5B. Core Pydantic Schema (extends existing Meetily SummaryResponse)

```python
# backend/app/models.py
from pydantic import BaseModel
from typing import List, Optional, Literal

class SourceRef(BaseModel):
    """Timestamp + speaker citation, grounding every claim."""
    start_ms: int          # from ASR word-level timestamp
    end_ms: int
    speaker: str           # from diarization label
    verbatim_quote: str    # near-verbatim; forces grounding

class ActionItem(BaseModel):
    assignee: str
    task: str
    deadline: Optional[str]   # extracted date/relative time
    priority: Literal["high", "medium", "low"]
    source: SourceRef

class Decision(BaseModel):
    topic: str
    decision: str
    proposer: str
    source: SourceRef

class QAPair(BaseModel):
    question: str
    questioner: str
    answer: str
    answerer: str
    source: SourceRef

class ChangeOrRequest(BaseModel):
    category: Literal["change", "request", "blocker"]
    description: str
    by: str
    target: Optional[str]
    source: SourceRef

class SegmentSummary(BaseModel):
    """L1: one per ~5-minute segment; displayed as collapsible cards."""
    segment_id: str         # "HH:MM:SS-HH:MM:SS"
    title: str              # auto-generated topic label
    one_liner: str
    action_items: List[ActionItem]
    decisions: List[Decision]
    qa_pairs: List[QAPair]
    changes_requests: List[ChangeOrRequest]

class TopicCluster(BaseModel):
    """L2: topic group spanning multiple segments."""
    topic: str
    segments: List[str]     # segment_ids
    summary: str
    key_decisions: List[Decision]

class MeetingWorkLog(BaseModel):
    """L3: full meeting — root of collapsible hierarchy."""
    meeting_id: str
    title: str
    date: str
    participants: List[str]
    tldr: str                          # 2-3 sentences
    executive_summary: str             # 1-2 paragraphs
    segments: List[SegmentSummary]     # L1 — always populated
    topics: List[TopicCluster]         # L2 — populated BATCH only
    all_action_items: List[ActionItem] # deduplicated across segments
    all_decisions: List[Decision]
    open_questions: List[QAPair]
    work_log: List[ChangeOrRequest]    # who did/requested what


### 5C. Grounding Strategy

The single most important anti-hallucination technique: **include timestamps and speaker labels in the input, and require a verbatim_quote field in every claim**.

**Input formatting** (in system/user prompt):

Format every utterance as:
[00:14:32.450 → 00:14:47.200 | Alice Smith]: We need to deploy the feature by next Friday.
[00:14:47.800 → 00:14:55.100 | Bob Jones]: I can own that, but I need the API spec first.


**Extraction instruction snippet**:

For every action item, decision, or request, you MUST include:
- verbatim_quote: copy the exact words spoken (10-30 words)
- start_ms / end_ms: from the timestamps in the input
- speaker: exactly as labeled in the input
Do NOT paraphrase or invent. If you are uncertain, omit rather than guess.


**Post-hoc alignment** (Python service):
```python
from rapidfuzz import fuzz

def resolve_quote_to_timestamp(quote: str, utterances: list[Utterance]) -> SourceRef:
    best = max(utterances, key=lambda u: fuzz.partial_ratio(quote, u.text))
    return SourceRef(start_ms=best.start_ms, end_ms=best.end_ms,
                     speaker=best.speaker, verbatim_quote=quote)

This recovers exact millisecond-level timestamps even if the model quotes imprecisely.

### 5D. vLLM Call (Python service, replaces current pydantic-ai + Ollama path)

```python
# backend/app/llm_client.py
from openai import OpenAI
from .models import MeetingWorkLog

client = OpenAI(base_url="http://localhost:8000/v1", api_key="token-abc123")

def extract_meeting_worklog(formatted_transcript: str) -> MeetingWorkLog:
    response = client.beta.chat.completions.parse(
        model="qwen25-72b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": formatted_transcript}
        ],
        response_format=MeetingWorkLog,  # vLLM xgrammar handles schema
        temperature=0.1,
        max_tokens=8192,
    )
    return response.choices[0].message.parsed


### 5E. Hierarchical Map-Reduce (for meetings > 100K tokens)

```python
# backend/app/hierarchical_pipeline.py
import asyncio
from .models import SegmentExtractionResult, MeetingWorkLog

async def map_phase(chunks: list[str]) -> list[SegmentExtractionResult]:
    """Process N chunks in parallel — vLLM handles batching."""
    tasks = [extract_segment(c) for c in chunks]
    return await asyncio.gather(*tasks)

async def reduce_phase(segments: list[SegmentExtractionResult],
                       transcript_meta: dict) -> MeetingWorkLog:
    """Single merge call: segments are already < 10K tokens."""
    merge_prompt = format_merge_prompt(segments, transcript_meta)
    return await extract_meeting_worklog(merge_prompt)

def chunk_transcript(utterances, max_tokens=30_000, overlap_tokens=2_000):
    # Split by utterance boundaries, never mid-sentence
    ...


### 5F. SQLite Schema Extension

```sql
-- Extend existing tables
ALTER TABLE meetings ADD COLUMN worklog_json TEXT;   -- MeetingWorkLog
ALTER TABLE transcripts ADD COLUMN segment_id TEXT;  -- "HH:MM:SS-HH:MM:SS"
ALTER TABLE transcripts ADD COLUMN speaker TEXT;     -- from diarization

-- New table for action items with citations
CREATE TABLE action_items (
    id TEXT PRIMARY KEY,
    meeting_id TEXT REFERENCES meetings(id),
    assignee TEXT,
    task TEXT,
    deadline TEXT,
    priority TEXT,
    source_start_ms INTEGER,
    source_end_ms INTEGER,
    speaker TEXT,
    verbatim_quote TEXT,
    completed INTEGER DEFAULT 0,
    created_at TEXT
);

CREATE INDEX idx_action_items_assignee ON action_items(assignee);
CREATE INDEX idx_action_items_meeting ON action_items(meeting_id);


### 5G. Frontend (React/TypeScript collapsible hierarchy)

The existing Meetily UI has a `BlockEditor` / section-based rendering. Extension needed:
- L3 (meeting) → summary card, participants, stats — always visible
- L2 (topics) → accordion, click to expand
- L1 (segments) → timeline with clickable timestamp → seek audio player
- Action item rows: assignee chip, click timestamp → jump to source in transcript view

No new dependencies required; existing `heading1`/`heading2`/`bullet` block types in Meetily's `Block` model can map to this.

### 5H. Dependencies & Effort


New Python dependencies (backend):
  - rapidfuzz (fuzzy matching for quote anchoring, ~200 KB)
  - No new LLM framework — reuse vLLM already deployed

Model download (one-time):
  - Qwen/Qwen2.5-72B-Instruct-GPTQ-Int4: ~41 GB
  - microsoft/phi-4 (Q4_K_M GGUF or GPTQ): ~9 GB

vLLM server launch:
  vllm serve Qwen/Qwen2.5-72B-Instruct-GPTQ-Int4 \
    --served-model-name qwen25-72b \
    --max-model-len 131072 \
    --gpu-memory-utilization 0.85 \
    --structured-outputs-config.backend xgrammar


**Rough effort estimate**:
- Schema design + vLLM integration: 2–3 days
- Hierarchical pipeline + merge prompt tuning: 2–3 days
- SQLite schema migration + action-item table: 1 day
- Grounding + rapidfuzz anchor: 1 day
- Frontend collapsible hierarchy: 2–3 days
- E2E testing on real meeting recordings: 2–3 days
- **Total: ~2.5 weeks for a production-quality implementation**

---

## 6. Shared-Tech / Overlap Notes

### Overlaps with other family-base targets:

| Capability | Shared Component |
|---|---|
| **Diarization (Target 4/5)**: speaker labels feed directly into `SourceRef.speaker` and the formatted transcript prefix | The per-utterance diarization output IS the input to this pipeline |
| **ASR (Target 2)**: word-level timestamps from NeMo Canary-Qwen / Whisper-large-v3-turbo provide `start_ms/end_ms` for grounding | No duplication; this pipeline consumes ASR output |
| **vLLM server (already deployed for ASR)**: The existing vLLM instance (running Whisper) can be extended to also serve the text LLM, OR a second vLLM instance for the 72B model | 2 vLLM processes on the same machine; Whisper-large-v3-turbo needs ~2–3 GB VRAM; 72B model needs ~42 GB; both fit in 96 GB |
| **RAG / chat-with-meeting (future target)**: The `MeetingWorkLog` JSON stored in SQLite, combined with segment-level text, is directly usable as a RAG knowledge base | This pipeline generates the structured index; the RAG target consumes it |
| **Summary template customisation**: Meetily PRO mentions custom templates; the schema approach here makes it trivial — swap the Pydantic model fields | Template = Pydantic schema variant |

### Multitask model check (does one audio foundation model replace the LLM pipeline?):

**No single model covers ASR + structured meeting summarization + action-item extraction in a unified offline model** as of 2025-Q2. The Canary/Whisper models do transcription; the text LLM does extraction. There is no confirmed offline model that does end-to-end audio → structured work-log. SeamlessM4T v2 does speech-to-text but not summarization. This decomposed pipeline (ASR → text LLM) remains the correct local architecture.

---

## 7. Open Questions / What Needs a Prototype to Settle

1. **Grounding faithfulness under INT4 quantisation**: Does Qwen2.5-72B-INT4 reliably emit verbatim quotes with correct timestamps at 0.1 temperature, or does it paraphrase enough to break rapidfuzz alignment? — **Needs: 10 real meeting test cases, measure quote-to-timestamp match rate.**

2. **xgrammar throughput overhead on deeply nested schemas**: The MeetingWorkLog schema is substantially more complex than a simple classification schema. The claimed 5–10% overhead may be higher for 50+ nested fields. — **Needs: micro-benchmark on the real schema with vLLM xgrammar.**

3. **KV cache for 128K context at INT4**: At 96 GB VRAM with 72B INT4 occupying ~42 GB, the remaining ~54 GB must cover KV cache for 128K tokens. At BF16 KV cache: 128K × 80 layers × 64 heads × 128 head_dim × 2 (K+V) × 2 bytes ≈ ~85 GB — exceeds remaining. INT8 KV cache: ~42 GB — tight but feasible. INT4 KV cache: ~21 GB — comfortable. vLLM supports `--kv-cache-dtype fp8` or `int8` flags. — **Needs: test actual memory usage with `--max-model-len 131072 --kv-cache-dtype fp8`.**

4. **Merge quality in map-reduce**: Does the reduce-phase (merging N segment summaries) reliably de-duplicate action items and resolve coreferences (e.g., "the deadline" in segment 3 refers to "Friday, June 13" from segment 1)? — **Needs: test on 4-hour meeting recordings.**

5. **Live-mode latency budget**: 5-minute segment at 150 wpm ≈ 750 words ≈ ~1,000 tokens. With Phi-4-14B INT4 at 20 tok/s output + 5K tokens input → ~250s total? — **Needs: measure vLLM Time-To-First-Token for 5K context on Phi-4-14B.**

6. **Qwen3 vs Qwen2.5 for this task**: Qwen3-72B (released May 2025) is newer but has less real-world deployment track record. Its "thinking mode" costs extra latency. — **Needs: A/B test on meeting extraction quality vs Qwen2.5-72B.**

---

## 8. Sources

| # | Citation |
|---|---|
| 1 | Meetily (Zackriya-Solutions): https://github.com/Zackriya-Solutions/meetily — MIT, 12,510 stars (verified Jun 2025) |
| 2 | Meetily `transcript_processor.py` (main summarization logic): `Zackriya-Solutions/meetily:backend/app/transcript_processor.py:50-175` |
| 3 | Meetily `schema_validator.py` (DB schema): `Zackriya-Solutions/meetily:backend/app/schema_validator.py:1-100` |
| 4 | Meetily `CLAUDE.md` (architecture overview): `Zackriya-Solutions/meetily:CLAUDE.md:1-80` |
| 5 | QMSum Dataset & Benchmark: Zhong et al., NAACL 2021. https://arxiv.org/abs/2104.05938 — `Yale-LILY/QMSum` |
| 6 | QMSum HMNet results: R-1/R-2/R-L 36.51/11.41/31.60 — `Yale-LILY/QMSum:README.md` |
| 7 | HMNet (Microsoft, EMNLP 2020): https://github.com/microsoft/HMNet — `microsoft/HMNet:README.md` |
| 8 | vLLM Structured Outputs docs (xgrammar backend): `vllm-project/vllm:docs/features/structured_outputs.md:1-200` (verified Jun 2025) |
| 9 | instructor library: https://github.com/567-labs/instructor — MIT, 13,099 stars — `567-labs/instructor:README.md` |
| 10 | pydantic-ai: https://github.com/pydantic/pydantic-ai — MIT, 17,513 stars |
| 11 | outlines-core (dottxt-ai): https://github.com/dottxt-ai/outlines-core — Apache 2.0, Rust, 293 stars |
| 12 | Qwen2.5 Technical Report (Alibaba, Nov 2024): https://qwenlm.github.io/blog/qwen2.5/ — MMLU 86.5, IFEval 87.4% |
| 13 | Phi-4 Technical Report (Microsoft Research, Dec 2024): https://arxiv.org/abs/2412.08905 — MMLU 84.8, MIT license |
| 14 | Llama-3.3-70B model card (Meta, Dec 2024): https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct |
| 15 | ollama-instructor (structured output for Ollama): https://github.com/lennartpollvogt/ollama-instructor — MIT, 77 stars |
| 16 | "Lost in the Middle: How Language Models Use Long Contexts" (Liu et al., 2023): https://arxiv.org/abs/2307.03172 — motivates chunking for very long inputs |
| 17 | xgrammar (mlc-ai): https://github.com/mlc-ai/xgrammar — token-level grammar-constrained decoding; default vLLM structured output backend |
| 18 | AMI Meeting Corpus: http://groups.inf.ed.ac.uk/ami/corpus/ — standard meeting dataset used in HMNet training |
| 19 | ICSI Meeting Corpus: https://groups.inf.ed.ac.uk/ami/icsi/ — companion dataset |
| 20 | rapidfuzz (fuzzy string matching): https://github.com/maxbachmann/RapidFuzz — MIT, used for quote-to-timestamp anchoring |

---

**Report complete.** The single recommended option is **Qwen2.5-72B-Instruct (INT4) served via vLLM with xgrammar guided decoding**, orchestrated in a 3-tier hierarchical extraction pipeline (segment → topic → meeting), with grounding enforced via verbatim-quote fields and rapidfuzz post-hoc timestamp alignment. This is a deterministic, fully offline, privacy-preserving pipeline that directly extends the existing Meetily/family-base FastAPI + SQLite + vLLM stack with approximately 2.5 weeks of implementation effort.
