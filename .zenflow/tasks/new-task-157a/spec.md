# Technical Specification: Functional Hybrid Corpus System

## 1. Technical Context

### 1.1 Language and Runtime
- **Language**: Python 3.12+
- **Rationale**: Existing scripts (`run_all_prompts.py`, `split_prompts.py`, `test_single_prompt.py`) are Python 3.12+. The team is already using asyncio, dataclasses, and type hints. Staying in Python avoids a language split.

### 1.2 Project Structure (New)
```
corpus/                          # New Python package (root)
  pyproject.toml                 # Project metadata, dependencies, scripts
  src/
    corpus/
      __init__.py
      config.py                  # Runtime configuration (env vars, defaults)
      db/
        __init__.py
        engine.py                # SQLite engine factory + connection management
        migrations/
          __init__.py
          runner.py              # Forward/rollback migration runner
          versions/              # Numbered .sql migration files
        models.py                # SQLAlchemy ORM models (all canonical entities)
        repository.py            # Data-access layer (CRUD per entity)
      ingestion/
        __init__.py
        enumerator.py            # Git diff / worktree file enumeration
        classifier.py            # Domain/capability tag classifier
        normalizer.py            # Content normalization into canonical files
        path_mapper.py           # Pre/post path mapping for moves/renames
      dedup/
        __init__.py
        minhash.py               # Layer 1: MinHash LSH candidate generation
        embeddings.py            # Layer 2: Sentence embedding cosine filtering
        arbitrator.py            # Layer 3: AI arbitration for disagreements
        pipeline.py              # Orchestrates L1 -> L2 -> L3 -> human queue
      decisions/
        __init__.py
        card_updater.py          # Recompute impacted DecisionCards
        index_updater.py         # Update decision_index, capability_index, s2d map
        drift_detector.py        # Emit DriftEvents on confidence drop / contradiction
      references/
        __init__.py
        rewrite_mapper.py        # Generate reference_rewrite_map
        rewriter.py              # Rewrite all internal references
        integrity_validator.py   # Validate all links + source paths resolve
      sync/
        __init__.py
        vector_sync.py           # Build/refresh vector embeddings from relational
        graph_sync.py            # Build/refresh graph edges from relational
        health_checker.py        # Sync lag and tolerance checks
      retrieval/
        __init__.py
        orchestrator.py          # L0-L3 retrieval pipeline
        symbolic_filter.py       # Tag/constraint filtering
        reranker.py              # Policy reranking (trust, freshness, task fit)
        formatter.py             # Depth-based response formatting
      consolidation/
        __init__.py
        gate_runner.py           # Run validation gates
        run_controller.py        # Mark complete / fail / remediate
        branch_retirement.py     # Archive or delete source branch/worktree
      telemetry/
        __init__.py
        collector.py             # Capture (decision_id, timestamp, outcome) tuples
        calibrator.py            # Recompute confidence calibration
        metrics.py               # Operational metrics tracking
        compactor.py             # Archive superseded content
      cli.py                     # Click-based CLI entry point
  tests/
    conftest.py
    db/
    ingestion/
    dedup/
    decisions/
    references/
    sync/
    retrieval/
    consolidation/
    telemetry/
```

### 1.3 Dependencies

| Dependency | Purpose | Justification |
|---|---|---|
| `sqlalchemy>=2.0` | ORM + relational schema | Industry-standard Python ORM; supports SQLite and PostgreSQL without code changes |
| `alembic` | Schema migrations | Companion to SQLAlchemy; supports forward/rollback, versioned migrations |
| `sentence-transformers` | Sentence embeddings (Layer 2 dedup + vector index) | Best-in-class local embedding; avoids API dependency for core pipeline |
| `datasketch` | MinHash LSH (Layer 1 dedup) | Proven, lightweight library for near-duplicate detection |
| `numpy` | Cosine similarity, array ops | Transitive dependency of sentence-transformers; used directly for similarity math |
| `chromadb` | Vector index storage + query | Embedded-mode vector DB; no external process required; production-upgradeable to client/server |
| `networkx` | In-process graph layer | Lightweight graph library; no external DB required; serializable to JSON for persistence |
| `click` | CLI framework | Clean CLI with subcommands; no web server needed |
| `gitpython` | Git operations (diff, branch ops) | Enumerate changed files, manage branch retirement |
| `pydantic>=2.0` | Config validation, data schemas | Type-safe configuration and data transfer objects |
| `pytest` | Testing framework | Standard Python test runner |
| `pytest-asyncio` | Async test support | Existing code uses asyncio |
| `openai` | Layer-3 AI arbitration | Compatible with OpenAI/Azure/local LLM endpoints for arbitration |

### 1.4 Database Engine
- **Primary**: SQLite (via SQLAlchemy).
- **Rationale**: No existing database infrastructure. SQLite is zero-config, file-based, and sufficient for a single-operator corpus system. The SQLAlchemy abstraction allows migration to PostgreSQL later without code changes.
- **File location**: `data/corpus.db` (gitignored).

### 1.5 Vector Engine
- **Primary**: ChromaDB in embedded mode.
- **Rationale**: Runs in-process (no external server), persists to local directory, supports incremental upsert and metadata filtering. Upgrade path to client/server mode exists.
- **Persistence**: `data/chroma/` (gitignored).

### 1.6 Graph Engine
- **Primary**: NetworkX in-process with JSON file persistence.
- **Rationale**: Corpus size is moderate (hundreds to low thousands of nodes/edges). NetworkX avoids external database dependency. Graph is serialized to `data/graph.json` and rebuilt from relational source on demand.

### 1.7 Embedding Model
- **Model**: `all-MiniLM-L6-v2` (via sentence-transformers).
- **Rationale**: 384-dim embeddings, fast inference on CPU, well-suited for semantic dedup and retrieval at this corpus scale. Can be upgraded to larger models later.

### 1.8 Deployment Model
- **Local-first CLI application**. No web server. Operators run consolidation pipelines and retrieval queries via CLI commands. This aligns with the existing script-based workflow.

---

## 2. Implementation Approach

### 2.1 Architecture Pattern
The system follows a **pipeline architecture** with a relational core:

```
[Git Source] -> Ingestion -> Dedup -> Decision Update -> Reference Integrity
     |                                                         |
     v                                                         v
  Relational DB  <-- authoritative state -->  Consolidation Gate
     |                                                         |
     +---> Vector Sync ---> ChromaDB                           |
     +---> Graph Sync  ---> NetworkX                           |
     |                                                         v
     +---------- Retrieval Orchestrator <----- [CLI Query]  Complete/Fail
```

All pipeline stages read/write the relational layer. Derived layers (vector, graph) are populated via sync jobs triggered after relational writes. The consolidation gate checks all layers before marking a run complete.

### 2.2 Key Design Decisions

| Decision | Choice | Rationale |
|---|---|---|
| Relational is authoritative | Enforced by architecture | All gates, lifecycle, and governance checks query relational only |
| Derived layers are rebuildable | Full rebuild commands in CLI | `corpus rebuild-vectors` and `corpus rebuild-graph` reconstruct from relational |
| Idempotent runs | Consolidation runs keyed by deterministic `run_id` | Re-running with same inputs converges to same state |
| Incremental processing | Only impacted entities recomputed | Artifact change sets drive scoped updates |
| Human queue blocks completion | Gate check queries `human_review_queue` for unresolved items | Run cannot complete until all items disposed |

### 2.3 Existing Code Reuse
- The `scripts/` directory and `docs/research/` structure remain untouched.
- The new `corpus/` package is additive. It reads from `docs/research/` as corpus source and writes to `data/` for runtime state.
- Existing `scripts/run_all_prompts.py` continues to be the research ingestion tool; the corpus system ingests its outputs.

---

## 3. Data Model

### 3.1 Relational Schema (SQLAlchemy Models)

#### `consolidation_runs`
```
run_id              TEXT PRIMARY KEY       -- cr_<purpose>_<YYYY_MM_DD>
source_branch       TEXT NOT NULL
source_worktree     TEXT
started_at          TEXT NOT NULL          -- ISO-8601
completed_at        TEXT
status              TEXT NOT NULL          -- enum: pending, running, completed, failed
artifacts_ingested  INTEGER DEFAULT 0
artifacts_deduped   INTEGER DEFAULT 0
decisions_impacted  INTEGER DEFAULT 0
drift_events_count  INTEGER DEFAULT 0
retirement_action   TEXT                   -- archived, deleted, n/a
remediation_report  TEXT                   -- populated on failure
```

#### `research_artifacts`
```
artifact_id         TEXT PRIMARY KEY       -- ra_<domain>_<nnn>
title               TEXT NOT NULL
content             TEXT NOT NULL
domain_tags         TEXT NOT NULL          -- JSON array
capability_tags     TEXT NOT NULL          -- JSON array
source_branch       TEXT NOT NULL
source_worktree     TEXT
source_path         TEXT NOT NULL
source_commit       TEXT
captured_at         TEXT NOT NULL          -- ISO-8601
run_id              TEXT NOT NULL REFERENCES consolidation_runs(run_id)
evidence_type       TEXT                   -- theory, experiment, benchmark, postmortem
source_reliability  REAL DEFAULT 0.0
freshness_days      INTEGER DEFAULT 0
status              TEXT NOT NULL DEFAULT 'active'  -- candidate, active, superseded, archived
```

#### `artifact_chunks`
```
chunk_id            TEXT PRIMARY KEY
artifact_id         TEXT NOT NULL REFERENCES research_artifacts(artifact_id)
chunk_index         INTEGER NOT NULL
content             TEXT NOT NULL
embedding_synced    BOOLEAN DEFAULT FALSE
UNIQUE(artifact_id, chunk_index)
```

#### `decision_cards`
```
decision_id         TEXT PRIMARY KEY       -- dc_<domain>_<nnn>
question            TEXT NOT NULL
capability          TEXT NOT NULL
constraints         TEXT                   -- JSON object
recommendation      TEXT NOT NULL          -- JSON object (summary, use_when, avoid_when)
alternatives        TEXT                   -- JSON array
confidence_score    REAL NOT NULL
confidence_level    TEXT NOT NULL          -- high, medium, low
confidence_explanation TEXT
has_unresolved_contradiction BOOLEAN DEFAULT FALSE
provenance_refs     TEXT NOT NULL          -- JSON array of artifact_ids
last_validated_at   TEXT NOT NULL          -- ISO-8601
revisit_triggers    TEXT                   -- JSON array
status              TEXT NOT NULL DEFAULT 'active'  -- active, superseded, archived
```

#### `drift_events`
```
event_id            TEXT PRIMARY KEY       -- de_<uuid>
decision_id         TEXT NOT NULL REFERENCES decision_cards(decision_id)
trigger             TEXT NOT NULL          -- new_conflicting_artifact, confidence_drop, etc.
confidence_delta    REAL
affected_sections   TEXT                   -- JSON array
status              TEXT NOT NULL          -- pending_revalidation, resolved, dismissed
run_id              TEXT NOT NULL REFERENCES consolidation_runs(run_id)
created_at          TEXT NOT NULL          -- ISO-8601
```

#### `reference_rewrite_maps`
```
id                  INTEGER PRIMARY KEY AUTOINCREMENT
run_id              TEXT NOT NULL REFERENCES consolidation_runs(run_id)
old_path            TEXT NOT NULL
new_path            TEXT NOT NULL
rewritten           BOOLEAN DEFAULT FALSE
```

#### `reference_integrity_reports`
```
id                  INTEGER PRIMARY KEY AUTOINCREMENT
run_id              TEXT NOT NULL REFERENCES consolidation_runs(run_id)
check_type          TEXT NOT NULL          -- internal_link, source_path, index_ref
target_path         TEXT NOT NULL
resolved            BOOLEAN NOT NULL
error_detail        TEXT
```

#### `human_review_queue`
```
id                  INTEGER PRIMARY KEY AUTOINCREMENT
run_id              TEXT NOT NULL REFERENCES consolidation_runs(run_id)
item_type           TEXT NOT NULL          -- dedup_arbitration
artifact_a_id       TEXT NOT NULL REFERENCES research_artifacts(artifact_id)
artifact_b_id       TEXT NOT NULL REFERENCES research_artifacts(artifact_id)
ai_confidence       REAL
ai_recommendation   TEXT                   -- merge, keep_both, discard_one
disposition         TEXT                   -- approved_merge, rejected_merge, deferred, NULL=unresolved
resolved_at         TEXT
resolved_by         TEXT
```

#### `capability_mappings`
```
id                  INTEGER PRIMARY KEY AUTOINCREMENT
capability          TEXT NOT NULL
decision_id         TEXT NOT NULL REFERENCES decision_cards(decision_id)
domain              TEXT NOT NULL
UNIQUE(capability, decision_id)
```

#### `telemetry_outcomes`
```
id                  INTEGER PRIMARY KEY AUTOINCREMENT
decision_id         TEXT NOT NULL REFERENCES decision_cards(decision_id)
timestamp           TEXT NOT NULL          -- ISO-8601
outcome             TEXT NOT NULL          -- success, failure
```

### 3.2 Vector Layer (ChromaDB)

Single collection: `corpus_chunks`
- **ID**: `chunk_id`
- **Embedding**: 384-dim float vector from `all-MiniLM-L6-v2`
- **Document**: chunk content text
- **Metadata**: `artifact_id`, `domain_tags`, `capability_tags`, `decision_ids`, `status`

### 3.3 Graph Layer (NetworkX)

Node types:
- `artifact` (keyed by `artifact_id`)
- `decision` (keyed by `decision_id`)
- `capability` (keyed by capability name)

Edge types:
- `artifact -> decision` (label: `supports`, weight: source_reliability)
- `decision -> capability` (label: `addresses`)
- `artifact -> artifact` (label: `conflicts_with`)
- `decision -> decision` (label: `contradicts`, when `has_unresolved_contradiction`)

Persisted as `data/graph.json` via `networkx.node_link_data()` / `node_link_graph()`.

---

## 4. Interface Design

### 4.1 CLI Commands (Click)

```
corpus init                           # Initialize DB, run migrations, create data dirs
corpus migrate                        # Run pending schema migrations
corpus migrate --rollback             # Rollback last migration

corpus ingest <branch-or-worktree>    # Start consolidation run: enumerate, classify, normalize
corpus dedup <run-id>                 # Run 3-layer dedup pipeline for a run
corpus update-decisions <run-id>      # Recompute impacted DecisionCards and indices
corpus check-references <run-id>      # Validate reference integrity
corpus sync-derived <run-id>          # Sync vector + graph layers from relational
corpus complete <run-id>              # Run all gates and mark run complete/fail

corpus run <branch-or-worktree>       # Full pipeline: ingest -> dedup -> update -> check -> sync -> complete

corpus review list                    # List unresolved human review items
corpus review resolve <id> <disposition>  # Resolve a review item

corpus query "<question>"             # Retrieval query (default L1)
corpus query "<question>" --depth L0  # Explicit depth override
corpus query "<question>" --depth L3

corpus rebuild-vectors                # Full vector rebuild from relational
corpus rebuild-graph                  # Full graph rebuild from relational

corpus telemetry record <decision-id> <outcome>  # Record success/failure
corpus telemetry calibrate            # Recompute confidence calibration
corpus telemetry metrics              # Print operational metrics

corpus status                         # Show current run status, queue, sync health
```

### 4.2 Retrieval Pipeline Flow

```
query(question, depth_override=None)
  1. symbolic_filter(question) -> constraint_set
  2. vector_candidates = chroma.query(question_embedding, filter=constraint_set, n=20)
  3. graph_expansion = graph.expand(vector_candidates, hops=2)
  4. merged_candidates = union(vector_candidates, graph_expansion)
  5. ranked = policy_rerank(merged_candidates, trust + freshness + task_fit)
  6. depth = resolve_depth(depth_override, confidence, contradictions)
  7. response = format_response(ranked, depth)  # L0/L1/L2/L3
  8. attach provenance + confidence metadata
  return response
```

### 4.3 Escalation Logic
```python
def resolve_depth(override, confidence, has_contradiction):
    if override: return override
    if confidence < 0.50 or has_contradiction: return "L3"
    if confidence < 0.70: return "L2"
    return "L1"  # default
```

---

## 5. Source Code Structure Changes

### 5.1 New Files (All Under `src/corpus/`)
All modules listed in Section 1.2 project structure are new. No existing files are modified.

### 5.2 New Top-Level Files
- `pyproject.toml` — Package definition, dependencies, CLI entry point
- `.gitignore` additions — `data/`, `*.db`, `.chroma/`

### 5.3 Runtime Data (Gitignored)
```
data/
  corpus.db          # SQLite database
  chroma/            # ChromaDB persistence
  graph.json         # NetworkX graph snapshot
  models/            # Cached sentence-transformer model files
```

---

## 6. Delivery Phases

### Phase 0: Project Scaffold and Environment
- Initialize `pyproject.toml` with dependencies.
- Create package structure under `src/corpus/`.
- Add `data/` to `.gitignore`.
- Verify `pip install -e .` works.
- **Verify**: `corpus --help` prints CLI help.

### Phase 1: Relational Data Layer
- Implement SQLAlchemy models for all 10 canonical entities.
- Implement Alembic migration runner with initial schema.
- Implement repository layer (CRUD operations per entity).
- Test rollback of initial migration.
- **Verify**: `corpus init` creates DB with all tables. `corpus migrate --rollback` removes them. Unit tests pass for repository CRUD.

### Phase 2: Ingestion and Normalization
- Implement git diff enumerator (GitPython).
- Implement domain/capability classifier against canonical directory contract.
- Implement content normalizer (merge into existing canonical files).
- Implement path mapper for moves/renames.
- Store artifacts + chunks in relational layer.
- **Verify**: `corpus ingest <branch>` creates `consolidation_run`, `research_artifacts`, and `artifact_chunks` records. No unclassified files remain. Unit tests for classifier and normalizer.

### Phase 3: Dedup Pipeline
- Implement MinHash LSH (datasketch) for Layer 1.
- Implement sentence embedding cosine similarity (sentence-transformers) for Layer 2.
- Implement AI arbitration stub for Layer 3 (OpenAI-compatible API).
- Implement human review queue routing for confidence < 0.70.
- Generate dedup report per run.
- Monitor Layer-3 call rate threshold.
- **Verify**: `corpus dedup <run-id>` produces dedup report. Low-confidence items appear in human review queue. Layer-3 rate flagging works. Unit tests for each layer.

### Phase 4: DecisionCard and Index Update
- Implement card updater (recompute impacted cards only).
- Implement confidence scoring per formula in `confidence_policy.md`.
- Implement index updater (decision_index, capability_index, source_to_decision_map).
- Implement drift detector (emit DriftEvents).
- **Verify**: `corpus update-decisions <run-id>` updates affected cards and indices. DriftEvents emitted for confidence drops. Unit tests.

### Phase 5: Reference Integrity
- Implement rewrite map generator from path mapper output.
- Implement reference rewriter (markdown links, index refs, run citations).
- Implement integrity validator (all links resolve, all source paths exist).
- Generate integrity report per run.
- **Verify**: `corpus check-references <run-id>` produces report with zero unresolved items on valid state. Detects broken links when introduced. Unit tests.

### Phase 6: Derived Layer Sync
- Implement vector sync (chunk embeddings -> ChromaDB).
- Implement graph sync (build nodes + edges from relational data).
- Implement sync health checker (lag tolerance, completeness).
- Implement full rebuild commands.
- **Verify**: `corpus sync-derived <run-id>` populates vector and graph. `corpus rebuild-vectors` and `corpus rebuild-graph` produce equivalent results from scratch. Sync health report generated. Unit tests.

### Phase 7: Retrieval Runtime
- Implement symbolic filter.
- Implement vector candidate retrieval via ChromaDB.
- Implement graph expansion via NetworkX.
- Implement policy reranker.
- Implement depth formatter (L0/L1/L2/L3 templates).
- Implement escalation logic.
- Attach provenance + confidence metadata.
- **Verify**: `corpus query` returns formatted responses at each depth level. Auto-escalation triggers at correct thresholds. Provenance refs present. Integration tests with seeded data.

### Phase 8: Consolidation Gate
- Implement gate runner (5 validation checks from FR-9.1).
- Implement run controller (complete / fail / remediation report).
- Implement branch retirement.
- **Verify**: `corpus complete <run-id>` passes on valid state, fails on broken references / unresolved queue / missing capabilities. Integration tests.

### Phase 9: Telemetry and Calibration
- Implement outcome recording.
- Implement confidence recalibration (when usage_count >= 5).
- Implement operational metrics collection.
- Implement compaction/archive for superseded content.
- **Verify**: `corpus telemetry record/calibrate/metrics` commands work. Calibration updates confidence scores. Unit tests.

### Phase 10: End-to-End Pipeline
- Wire `corpus run <branch>` as full pipeline orchestrator.
- End-to-end integration test: ingest sample branch -> dedup -> update decisions -> check refs -> sync -> complete.
- **Verify**: Full pipeline completes with all gates enforced. `corpus status` shows healthy state.

---

## 7. Verification Approach

### 7.1 Test Commands
```bash
pytest tests/ -v                      # All unit + integration tests
pytest tests/ -v -k "test_db"         # Database tests only
pytest tests/ -v -k "test_dedup"      # Dedup pipeline tests only
```

### 7.2 Lint / Type Check
```bash
ruff check src/ tests/                # Linting
ruff format --check src/ tests/       # Format check
mypy src/corpus/                      # Type checking
```

### 7.3 Test Strategy Per Phase
- **Unit tests**: Every module gets tests in `tests/<module>/`. Repository CRUD, classifier logic, dedup layers, confidence scoring, reference validation, escalation logic.
- **Integration tests**: End-to-end pipeline tests with a temporary SQLite DB, seeded artifacts, and real ChromaDB/NetworkX instances.
- **Gate tests**: Verify each consolidation gate blocks on invalid state and passes on valid state.
- **Rebuild tests**: Verify derived layers rebuilt from relational produce equivalent results to incremental sync.

### 7.4 Test Fixtures
- Seed fixture with 10 existing DecisionCards from bootstrap run.
- Sample branch fixture with 5 new research artifacts (2 near-duplicates, 1 conflicting, 2 novel).
- Pre-built reference map with intentional broken link for negative testing.

---

## 8. Configuration

### 8.1 Environment Variables
```
CORPUS_DB_URL=sqlite:///data/corpus.db       # SQLAlchemy connection string
CORPUS_CHROMA_DIR=data/chroma                # ChromaDB persistence directory
CORPUS_GRAPH_PATH=data/graph.json            # NetworkX graph file
CORPUS_EMBEDDING_MODEL=all-MiniLM-L6-v2      # Sentence transformer model name
CORPUS_OPENAI_API_KEY=<key>                  # For Layer-3 AI arbitration
CORPUS_OPENAI_BASE_URL=<url>                 # Optional: custom LLM endpoint
CORPUS_DEDUP_L1_THRESHOLD=0.5               # MinHash similarity threshold
CORPUS_DEDUP_L2_THRESHOLD=0.85              # Cosine similarity threshold
CORPUS_ARBITRATION_CONFIDENCE_MIN=0.70       # Below this -> human queue
CORPUS_L3_RATE_ALERT_THRESHOLD=0.20          # Flag if L3 calls > 20% of L1 candidates
CORPUS_SYNC_LAG_TOLERANCE_SECONDS=300        # Max acceptable derived-layer lag
```

### 8.2 Pydantic Settings
All environment variables are validated at startup via a `CorpusSettings(BaseSettings)` class with defaults. Missing required values (e.g., `CORPUS_OPENAI_API_KEY` when running dedup) produce clear error messages.

---

## 9. Risks and Mitigations (Technical)

| Risk | Mitigation |
|---|---|
| SQLite concurrency limits | Single-operator design; upgrade path to PostgreSQL via SQLAlchemy |
| Embedding model download on first run | Cache in `data/models/`; document in CLI `init` output |
| ChromaDB version compatibility | Pin version in `pyproject.toml`; rebuild command available |
| NetworkX graph size at scale | Monitor node/edge counts in telemetry; migration path to Neo4j documented |
| AI arbitration API availability | Graceful degradation: queue all disagreements for human review if API fails |
| Test speed with real embeddings | Use small test corpus; mock embeddings in unit tests, real in integration |

---

## 10. Escalation Thresholds (Finalized)

| Parameter | Value | Source |
|---|---|---|
| L2 escalation confidence | < 0.70 | `confidence_policy.md` |
| L3 escalation confidence | < 0.50 | `confidence_policy.md` |
| L3 escalation contradiction | `has_unresolved_contradiction = true` | `confidence_policy.md` |
| Human queue routing | AI confidence < 0.70 | `knowledge_architecture_contract.md` |
| L3 rate alert | > 20% of L1 candidates | `update_lifecycle.md` |
| Downstream success threshold | `usage_count >= 5` | `confidence_policy.md` |
| Sync lag tolerance | 300 seconds | Operational default; configurable |
