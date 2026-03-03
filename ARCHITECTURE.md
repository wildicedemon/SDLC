# Architecture — Corpus Pipeline

> Technical reference for the corpus-pipeline system design, data flow, and module responsibilities.

## System Overview

The corpus pipeline is a self-contained Python package (`corpus`) that transforms raw research documents into a searchable, deduplicated, indexed knowledge corpus. It operates as a six-stage pipeline orchestrated by a Click CLI, backed by SQLite (via SQLAlchemy ORM), ChromaDB (vector store), and NetworkX (knowledge graph).

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           CORPUS PIPELINE                                   │
│                                                                             │
│  Drop-Folder / Git Branch                                                   │
│        │                                                                    │
│        ▼                                                                    │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐ │
│  │ 1.Ingest │──▶│ 2.Dedup  │──▶│3.Decide  │──▶│ 4.Refs   │──▶│ 5.Sync   │ │
│  │          │   │ L1→L2→L3 │   │ LLM gen  │   │ rewrite  │   │ vec+graph│ │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘ │
│        │                                                            │       │
│        └────────────── SQLite (relational) ─────────────────────────┘       │
│                               │                                             │
│                    ┌──────────┴──────────┐                                  │
│                    │    6. Quality Gates  │                                  │
│                    │ (complete / failed)  │                                  │
│                    └─────────────────────┘                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Directory Structure

```
├── pyproject.toml                              # Build config, dependencies, CLI entry point
├── README.md                                   # User-facing documentation
├── ARCHITECTURE.md                             # This file
├── .gitignore
│
├── src/corpus/
│   ├── __init__.py                             # Package docstring, __version__ = "0.1.0"
│   ├── cli.py                                  # Click CLI: 20+ commands/subgroups
│   ├── config.py                               # CorpusSettings (pydantic-settings, env prefix CORPUS_)
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── engine.py                           # create_db_engine(), get_session(), make_session_factory()
│   │   ├── models.py                           # 10 ORM models on DeclarativeBase
│   │   ├── repository.py                       # CorpusRepository — unified data-access layer
│   │   └── migrations/
│   │       ├── __init__.py
│   │       ├── runner.py                       # migrate_forward(), migrate_rollback()
│   │       └── versions/
│   │           └── 001_initial.sql             # Initial schema (10 tables)
│   │
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── parsers.py                          # parse_file() → ParsedDocument
│   │   ├── watcher.py                          # watch(), CorpusEventHandler
│   │   ├── pipeline.py                         # run_ingest(), ingest_file()
│   │   ├── classifier.py                       # classify() → Classification
│   │   ├── enumerator.py                       # enumerate_changes() → list[ChangedFile]
│   │   ├── normalizer.py                       # normalize() → NormalizedResult
│   │   └── path_mapper.py                      # record_mapping()
│   │
│   ├── dedup/
│   │   ├── __init__.py
│   │   ├── pipeline.py                         # run_dedup() → DedupReport
│   │   ├── minhash.py                          # generate_candidates() → list[CandidatePair]
│   │   ├── embeddings.py                       # filter_candidates() → (confirmed, disagreements)
│   │   └── arbitrator.py                       # arbitrate() → list[ArbitrationResult]
│   │
│   ├── decisions/
│   │   ├── __init__.py
│   │   ├── generator.py                        # generate_decisions() → GenerationReport
│   │   ├── card_updater.py                     # update_impacted_cards() → list[str]
│   │   ├── drift_detector.py                   # detect_drift() → list[str]
│   │   └── index_updater.py                    # update_indices()
│   │
│   ├── references/
│   │   ├── __init__.py
│   │   ├── rewriter.py                         # rewrite_references() → int
│   │   ├── rewrite_mapper.py                   # generate_rewrite_map() → list[ReferenceRewriteMap]
│   │   └── integrity_validator.py              # validate_integrity() → IntegrityReport
│   │
│   ├── sync/
│   │   ├── __init__.py
│   │   ├── vector_sync.py                      # sync_vectors(), rebuild_vectors() → VectorSyncResult
│   │   ├── graph_sync.py                       # sync_graph(), rebuild_graph() → GraphSyncResult
│   │   └── health_checker.py                   # check_sync_health() → SyncHealthReport
│   │
│   ├── consolidation/
│   │   ├── __init__.py
│   │   ├── run_controller.py                   # complete_run() → bool
│   │   ├── gate_runner.py                      # run_gates() → GateReport
│   │   └── branch_retirement.py                # retire_branch()
│   │
│   ├── retrieval/
│   │   ├── __init__.py
│   │   ├── orchestrator.py                     # query() → RetrievalResponse
│   │   ├── reranker.py                         # rerank() → list[ScoredChunk]
│   │   ├── formatter.py                        # format_response()
│   │   └── symbolic_filter.py                  # extract_constraints()
│   │
│   └── telemetry/
│       ├── __init__.py
│       ├── collector.py                        # record_outcome()
│       ├── calibrator.py                       # calibrate() → CalibrationReport
│       ├── compactor.py                        # compact_telemetry()
│       └── metrics.py                          # compute_metrics() → CorpusMetrics
│
├── tests/                                      # Mirrors src/ structure
│   ├── conftest.py                             # Shared fixtures (in-memory DB, etc.)
│   ├── test_kilo_gateway.py
│   ├── ingestion/
│   │   ├── test_parsers.py
│   │   ├── test_watcher.py
│   │   ├── test_classifier.py
│   │   ├── test_enumerator.py
│   │   ├── test_normalizer.py
│   │   ├── test_path_mapper.py
│   │   └── test_ingest_integration.py
│   ├── dedup/
│   │   ├── test_minhash.py
│   │   ├── test_embeddings.py
│   │   ├── test_arbitrator.py
│   │   └── test_pipeline.py
│   ├── decisions/
│   │   ├── test_card_updater.py
│   │   ├── test_drift_detector.py
│   │   └── test_index_updater.py
│   ├── references/
│   │   ├── test_integrity_validator.py
│   │   └── test_rewriter.py
│   ├── sync/
│   │   ├── test_vector_sync.py
│   │   ├── test_graph_sync.py
│   │   └── test_health_checker.py
│   ├── consolidation/
│   │   ├── test_branch_retirement.py
│   │   ├── test_gate_runner.py
│   │   └── test_run_controller.py
│   ├── retrieval/
│   │   ├── test_orchestrator.py
│   │   ├── test_reranker.py
│   │   ├── test_formatter.py
│   │   └── test_symbolic_filter.py
│   ├── telemetry/
│   │   ├── test_calibrator.py
│   │   ├── test_collector.py
│   │   ├── test_compactor.py
│   │   └── test_metrics.py
│   ├── db/
│   │   ├── test_migrations.py
│   │   ├── test_models.py
│   │   ├── test_repository_core.py
│   │   └── test_repository_supporting.py
│   └── integration/
│       ├── test_core_pipeline_smoke.py
│       ├── test_db_roundtrip.py
│       ├── test_e2e_scaled.py
│       ├── test_full_pipeline_smoke.py
│       └── test_ingest_smoke.py
│
└── scripts/
    ├── bootstrap_corpus.py                     # One-shot bootstrap for initial corpus
    └── run_full_ingestion.py                   # Scripted full ingestion run
```

## Configuration

All settings are defined in [`CorpusSettings`](src/corpus/config.py:7), a `pydantic_settings.BaseSettings` subclass with the `CORPUS_` environment-variable prefix.

| Field | Type | Default | Env Variable |
|-------|------|---------|-------------|
| `db_url` | `str` | `sqlite:///data/corpus.db` | `CORPUS_DB_URL` |
| `chroma_dir` | `str` | `data/chroma` | `CORPUS_CHROMA_DIR` |
| `graph_path` | `str` | `data/graph.json` | `CORPUS_GRAPH_PATH` |
| `embedding_model` | `str` | `all-MiniLM-L6-v2` | `CORPUS_EMBEDDING_MODEL` |
| `kilo_api_key` | `str` | `""` | `CORPUS_KILO_API_KEY` |
| `llm_base_url` | `str` | `https://api.kilo.ai/api/gateway` | `CORPUS_LLM_BASE_URL` |
| `llm_model` | `str` | `google/gemini-2.5-flash` | `CORPUS_LLM_MODEL` |
| `decision_model` | `str` | `perplexity/sonar-deep-research` | `CORPUS_DECISION_MODEL` |
| `max_arbitration_calls` | `int` | `500` | `CORPUS_MAX_ARBITRATION_CALLS` |
| `dedup_l1_threshold` | `float` | `0.5` | `CORPUS_DEDUP_L1_THRESHOLD` |
| `dedup_l2_threshold` | `float` | `0.85` | `CORPUS_DEDUP_L2_THRESHOLD` |
| `arbitration_confidence_min` | `float` | `0.70` | `CORPUS_ARBITRATION_CONFIDENCE_MIN` |
| `l3_rate_alert_threshold` | `float` | `0.20` | `CORPUS_L3_RATE_ALERT_THRESHOLD` |
| `sync_lag_tolerance_seconds` | `int` | `300` | `CORPUS_SYNC_LAG_TOLERANCE_SECONDS` |
| `watch_dir` | `str` | `C:\Users\Ice\scrape` | `CORPUS_WATCH_DIR` |
| `poll_interval` | `float` | `2.0` | `CORPUS_POLL_INTERVAL` |

Helper methods on [`CorpusSettings`](src/corpus/config.py:7):

- [`data_dir()`](src/corpus/config.py:27) — returns `Path("data")`
- [`ensure_data_dirs()`](src/corpus/config.py:30) — creates `data/` and `chroma_dir` directories

The singleton accessor [`get_settings()`](src/corpus/config.py:35) instantiates `CorpusSettings` from the current environment.

## Data Model

Ten SQLAlchemy ORM models defined in [`models.py`](src/corpus/db/models.py:1), all inheriting from a shared [`Base`](src/corpus/db/models.py:33) (`DeclarativeBase`):

| Model | Table | Purpose |
|-------|-------|---------|
| [`ConsolidationRun`](src/corpus/db/models.py:39) | `consolidation_runs` | Pipeline run lifecycle tracking (pending → running → completed/failed) |
| `ResearchArtifact` | `research_artifacts` | Ingested documents with domain/capability tags |
| `ArtifactChunk` | `artifact_chunks` | Content segments split for embedding and dedup |
| `DecisionCard` | `decision_cards` | LLM-generated architectural decisions with confidence scores |
| `DriftEvent` | `drift_events` | Confidence-score drift records between runs |
| `ReferenceRewriteMap` | `reference_rewrite_maps` | Old→new path mappings per run |
| `ReferenceIntegrityReport` | `reference_integrity_reports` | Link-integrity check results |
| `HumanReviewQueue` | `human_review_queue` | Items queued for manual triage |
| `CapabilityMapping` | `capability_mappings` | Decision ↔ capability associations |
| `TelemetryOutcome` | `telemetry_outcomes` | Success/failure telemetry records |

All date columns store ISO-8601 strings for SQLite portability.

### Entity Relationships

```
ConsolidationRun
  ├── 1:N → ResearchArtifact     (run_id FK)
  ├── 1:N → HumanReviewQueue     (run_id FK)
  ├── 1:N → ReferenceRewriteMap  (run_id FK)
  └── 1:N → ReferenceIntegrityReport (run_id FK)

ResearchArtifact
  └── 1:N → ArtifactChunk        (artifact_id FK)

DecisionCard
  ├── 1:N → DriftEvent           (decision_id FK)
  ├── 1:N → CapabilityMapping    (decision_id FK)
  └── 1:N → TelemetryOutcome     (decision_id FK)
```

## Database Layer

### Engine ([`engine.py`](src/corpus/db/engine.py:1))

- [`create_db_engine(url)`](src/corpus/db/engine.py:17) — creates a SQLAlchemy `Engine` with a `connect` event listener that issues `PRAGMA foreign_keys=ON` for SQLite referential integrity.
- [`make_session_factory(engine)`](src/corpus/db/engine.py:41) — returns a `sessionmaker` bound to the engine.
- [`get_session(engine)`](src/corpus/db/engine.py:54) — context manager yielding a transactional `Session` with auto-commit on clean exit and rollback on exception.

### Repository ([`repository.py`](src/corpus/db/repository.py:1))

[`CorpusRepository`](src/corpus/db/repository.py:1) is the unified data-access class wrapping all CRUD operations. It accepts a `Session` and exposes methods such as:

- `create_run()`, `get_run()`, `update_run_status()` — run lifecycle
- `create_artifact()`, `list_artifacts()` — artifact management
- `create_chunk()`, `get_chunk()`, `list_chunks()` — chunk access
- `list_decision_cards()`, `create_decision_card()` — decision CRUD
- `create_review_item()`, `list_unresolved_reviews()`, `resolve_review()` — human review queue
- `create_rewrite_map_entry()` — reference rewrite tracking

### Migrations ([`migrations/runner.py`](src/corpus/db/migrations/runner.py:1))

SQL-file-based migration system:

- [`migrate_forward(engine)`](src/corpus/db/migrations/runner.py:1) — applies all unapplied `.sql` files from `versions/` in lexicographic order.
- [`migrate_rollback(engine)`](src/corpus/db/migrations/runner.py:1) — rolls back the most recently applied migration.
- Tracks applied migrations in a `_migrations` meta-table.
- Initial schema: [`001_initial.sql`](src/corpus/db/migrations/versions/001_initial.sql:1) — creates all 10 tables with foreign keys and constraints.

## Stage 1 — Ingestion

### Parsers ([`parsers.py`](src/corpus/ingestion/parsers.py:1))

[`parse_file(path)`](src/corpus/ingestion/parsers.py:135) auto-detects format from extension and returns a [`ParsedDocument`](src/corpus/ingestion/parsers.py:27) dataclass:

| Extension | Handler | Title Strategy |
|-----------|---------|----------------|
| `.md`, `.markdown` | [`_parse_markdown()`](src/corpus/ingestion/parsers.py:40) | First `# heading` |
| `.html`, `.htm` | [`_parse_html()`](src/corpus/ingestion/parsers.py:57) | `<title>` → `<h1>` → filename |
| `.pdf` | [`_parse_pdf()`](src/corpus/ingestion/parsers.py:83) | PDF metadata title → first line |
| `.txt`, `.text`, `.log`, `.csv` | [`_parse_text()`](src/corpus/ingestion/parsers.py:120) | Filename stem |

- HTML parsing uses BeautifulSoup (`html.parser`)
- PDF parsing uses PyMuPDF (`fitz`)
- Unknown extensions fall back to plain-text with a warning

### Drop-Folder Watcher ([`watcher.py`](src/corpus/ingestion/watcher.py:1))

[`watch(watch_dir, poll_interval)`](src/corpus/ingestion/watcher.py:163) starts a `watchdog.Observer` that monitors a directory:

1. Creates `watch_dir/` and `watch_dir/processed/` if absent
2. Initialises the database (runs migrations)
3. Processes any **backlog** (existing files in the directory)
4. Enters the observation loop

[`CorpusEventHandler`](src/corpus/ingestion/watcher.py:29) responds to `on_created` and `on_modified` events:

- **Debounce**: 2-second `threading.Timer` per file path; resets on repeated events
- **Filter**: only `_SUPPORTED_EXTS` (`.md`, `.html`, `.pdf`, `.txt`, etc.); ignores `processed/` subdirectory
- **Process**: calls [`parse_file()`](src/corpus/ingestion/parsers.py:135) → [`ingest_file()`](src/corpus/ingestion/pipeline.py:146)
- **Move**: processed files are moved to `processed/` with dedup-safe naming (appends `_1`, `_2`, etc.)

### Git-Based Pipeline ([`pipeline.py`](src/corpus/ingestion/pipeline.py:1))

[`run_ingest(repo, repo_path, source_branch, base_branch)`](src/corpus/ingestion/pipeline.py:31) orchestrates git-based ingestion:

1. Creates a `ConsolidationRun` record
2. Calls [`enumerate_changes()`](src/corpus/ingestion/enumerator.py:1) to diff source vs. base branch
3. For each non-deleted file: classify → normalize → create artifact + chunks
4. Records path mappings via [`record_mapping()`](src/corpus/ingestion/path_mapper.py:15)
5. Returns an [`IngestResult`](src/corpus/ingestion/pipeline.py:23) with counts and unclassified file list

[`ingest_file()`](src/corpus/ingestion/pipeline.py:146) handles single-file ingestion (no git required):

1. Classifies the file path
2. Chunks content: H2-boundary for Markdown, paragraph-based (`~2000 char`) for other formats
3. Creates `ResearchArtifact` + `ArtifactChunk` records

### Classifier ([`classifier.py`](src/corpus/ingestion/classifier.py:1))

[`classify(path)`](src/corpus/ingestion/classifier.py:1) maps file paths to domain and capability tags using a taxonomy dictionary (`DOMAIN_DIRECTORIES`). Recognises:

- Research directories under `docs/research/` and `Kimi-Research/`
- Numbered domain folders (e.g. `01_meta_architecture/`)
- Special directories (`_distilled`, `_extractions`)
- Top-level knowledge prefixes (`distilled/`, `docs/distillation/`)

### Enumerator ([`enumerator.py`](src/corpus/ingestion/enumerator.py:1))

[`enumerate_changes(repo_path, source_branch, base_branch)`](src/corpus/ingestion/enumerator.py:1) uses GitPython to diff two branches and return a list of [`ChangedFile`](src/corpus/ingestion/enumerator.py:19) dataclasses (path, content bytes, change type).

### Normalizer ([`normalizer.py`](src/corpus/ingestion/normalizer.py:1))

[`normalize(content, domain, canonical_path)`](src/corpus/ingestion/normalizer.py:1) splits Markdown at `## ` (H2) heading boundaries, extracts the title from the first `# ` heading, and writes the result to a canonical path. If the target already exists, content is **merged** (appended) and re-chunked.

### Path Mapper ([`path_mapper.py`](src/corpus/ingestion/path_mapper.py:1))

[`record_mapping(repo, old_path, new_path, run_id)`](src/corpus/ingestion/path_mapper.py:15) persists source→canonical path mappings in the `ReferenceRewriteMap` table for downstream reference rewriting.

## Stage 2 — Deduplication

### Pipeline Orchestrator ([`dedup/pipeline.py`](src/corpus/dedup/pipeline.py:1))

[`run_dedup(session, run_id, settings)`](src/corpus/dedup/pipeline.py:67) executes the three layers in sequence and returns a [`DedupReport`](src/corpus/dedup/pipeline.py:34):

```
All ArtifactChunks for run
        │
        ▼
  ┌─────────────────────┐
  │  L1: MinHash LSH    │  threshold = 0.5 (Jaccard)
  │  generate_candidates │
  └─────────┬───────────┘
            │ CandidatePair[]
            ▼
  ┌─────────────────────┐
  │  L2: Embeddings     │  threshold = 0.85 (cosine)
  │  filter_candidates  │
  └──┬──────────┬───────┘
     │          │
 Confirmed   Disagreement[]
 Dups           │
                ▼
  ┌─────────────────────┐
  │  L3: LLM Arbitrate  │  max_calls = 500
  │  arbitrate()        │
  └──┬──────────┬───────┘
     │          │
  Resolved   human_review → HumanReviewQueue
```

The L3 escalation rate is monitored: if `len(disagreements) / len(candidates)` exceeds `l3_rate_alert_threshold` (0.20), a warning is logged. If no API key is configured, all disagreements auto-resolve as `keep_both`.

### Layer 1 — MinHash ([`minhash.py`](src/corpus/dedup/minhash.py:1))

[`generate_candidates(chunks, threshold)`](src/corpus/dedup/minhash.py:1) builds a `datasketch.MinHashLSH` index over all chunk tokens and emits [`CandidatePair`](src/corpus/dedup/minhash.py:1) instances for pairs exceeding the Jaccard threshold.

### Layer 2 — Embeddings ([`embeddings.py`](src/corpus/dedup/embeddings.py:1))

[`filter_candidates(candidates, threshold, embed_fn)`](src/corpus/dedup/embeddings.py:1) computes sentence-transformer embeddings and cosine similarity for each candidate pair. Returns two lists:

- [`ConfirmedDup`](src/corpus/dedup/embeddings.py:1) — pairs above the cosine threshold
- [`Disagreement`](src/corpus/dedup/embeddings.py:1) — pairs below (L1 said yes, L2 said no)

Accepts an optional `embed_fn` override for testing.

### Layer 3 — LLM Arbitration ([`arbitrator.py`](src/corpus/dedup/arbitrator.py:1))

[`arbitrate(disagreements, base_url, api_key, model, max_calls)`](src/corpus/dedup/arbitrator.py:1) sends each disagreement pair to an LLM via the OpenAI-compatible API. The LLM returns a JSON verdict:

- `recommendation`: `merge`, `keep_both`, `discard_one`, or `human_review`
- `confidence`: float score

Fallback behaviour: if no API key is set or after consecutive failures, remaining disagreements are auto-resolved as `keep_both`. Items routed to `human_review` are enqueued in `HumanReviewQueue`.

## Stage 3 — Decision Generation

### Generator ([`decisions/generator.py`](src/corpus/decisions/generator.py:1))

[`generate_decisions(session, run_id, settings, domains, dry_run)`](src/corpus/decisions/generator.py:1) groups artifacts by domain, retrieves relevant chunks from ChromaDB, and calls an LLM (default: `perplexity/sonar-deep-research`) to synthesize decision cards. Each card includes a title, rationale, confidence score, and domain/capability tags.

### Card Updater ([`decisions/card_updater.py`](src/corpus/decisions/card_updater.py:1))

[`update_impacted_cards(session, run_id)`](src/corpus/decisions/card_updater.py:1) identifies decision cards affected by newly ingested or deduped artifacts and recomputes their confidence scores.

### Drift Detector ([`decisions/drift_detector.py`](src/corpus/decisions/drift_detector.py:1))

[`detect_drift(session, run_id, previous_scores)`](src/corpus/decisions/drift_detector.py:1) compares current decision confidence scores against their pre-run values and creates `DriftEvent` records for significant changes.

### Index Updater ([`decisions/index_updater.py`](src/corpus/decisions/index_updater.py:1))

[`update_indices(session, decision_ids)`](src/corpus/decisions/index_updater.py:1) rebuilds `CapabilityMapping` entries for the given decision IDs.

## Stage 4 — Reference Management

### Rewrite Mapper ([`references/rewrite_mapper.py`](src/corpus/references/rewrite_mapper.py:1))

[`generate_rewrite_map(session, run_id)`](src/corpus/references/rewrite_mapper.py:1) retrieves all `ReferenceRewriteMap` entries for a run that have not yet been applied.

### Rewriter ([`references/rewriter.py`](src/corpus/references/rewriter.py:1))

[`rewrite_references(rewrite_map, corpus_root)`](src/corpus/references/rewriter.py:1) scans Markdown files under `corpus_root` and replaces old paths with new paths as specified in the rewrite map. Returns the count of rewrites applied.

### Integrity Validator ([`references/integrity_validator.py`](src/corpus/references/integrity_validator.py:1))

[`validate_integrity(session, run_id, corpus_root)`](src/corpus/references/integrity_validator.py:1) checks all Markdown link references for the run against the filesystem and database. Returns an `IntegrityReport` with `broken_links`, `stale_paths`, and a `passed` flag.

## Stage 5 — Derived Store Sync

### Vector Sync ([`sync/vector_sync.py`](src/corpus/sync/vector_sync.py:1))

- [`sync_vectors(session, run_id, settings)`](src/corpus/sync/vector_sync.py:1) — embeds un-synced `ArtifactChunk` records using the configured sentence-transformer model and upserts them into a persistent ChromaDB collection. Batches at 5000 documents per upsert call.
- [`rebuild_vectors(session, settings)`](src/corpus/sync/vector_sync.py:1) — wipes and re-embeds the entire corpus.

### Graph Sync ([`sync/graph_sync.py`](src/corpus/sync/graph_sync.py:1))

- [`sync_graph(session, run_id, settings)`](src/corpus/sync/graph_sync.py:1) — updates a directed NetworkX graph with artifact → decision → capability edges. Serialised as `node_link_data` JSON at `graph_path`.
- [`rebuild_graph(session, settings)`](src/corpus/sync/graph_sync.py:1) — rebuilds the graph from scratch.

### Health Checker ([`sync/health_checker.py`](src/corpus/sync/health_checker.py:1))

[`check_sync_health(session, settings)`](src/corpus/sync/health_checker.py:1) verifies that the vector store and graph are sufficiently in sync with the relational database. Returns a `SyncHealthReport` with `healthy` flag and `vector_synced_pct`.

## Stage 6 — Consolidation & Quality Gates

### Run Controller ([`consolidation/run_controller.py`](src/corpus/consolidation/run_controller.py:1))

[`complete_run(session, run_id, corpus_root, settings)`](src/corpus/consolidation/run_controller.py:21) orchestrates the final stage:

1. Executes all quality gates via [`run_gates()`](src/corpus/consolidation/gate_runner.py:1)
2. On success: marks run `completed`
3. On failure: marks run `failed` with a remediation report

### Gate Runner ([`consolidation/gate_runner.py`](src/corpus/consolidation/gate_runner.py:1))

[`run_gates(session, run_id, corpus_root, settings)`](src/corpus/consolidation/gate_runner.py:1) executes five quality gates:

| Gate | Check |
|------|-------|
| `capability_populated` | Every capability tag has a decision-card mapping |
| `human_review_resolved` | No unresolved items in `HumanReviewQueue` |
| `all_classified` | Every artifact has at least one domain tag |
| `reference_integrity` | All markdown links resolve on disk |
| `sync_health` | Vector store and graph are within sync tolerance |

Returns a `GateReport` with per-gate pass/fail and a combined `passed` flag.

### Branch Retirement ([`consolidation/branch_retirement.py`](src/corpus/consolidation/branch_retirement.py:1))

[`retire_branch()`](src/corpus/consolidation/branch_retirement.py:1) handles post-merge branch cleanup after a run completes successfully.

## Retrieval Subsystem

### Orchestrator ([`retrieval/orchestrator.py`](src/corpus/retrieval/orchestrator.py:1))

[`query(session, question, depth_override, settings)`](src/corpus/retrieval/orchestrator.py:1) combines three retrieval strategies:

1. **Vector search** — ChromaDB semantic similarity on chunk embeddings
2. **Graph expansion** — NetworkX traversal to find related decisions and capabilities
3. **Decision-card matching** — direct lookup of relevant `DecisionCard` records

Automatically escalates response depth (L0 → L1 → L2 → L3) based on confidence and contradiction signals. Returns a [`RetrievalResponse`](src/corpus/retrieval/orchestrator.py:26) with `content`, `depth`, `confidence`, and optional `escalation_reason`.

### Reranker ([`retrieval/reranker.py`](src/corpus/retrieval/reranker.py:1))

[`rerank(chunks)`](src/corpus/retrieval/reranker.py:1) re-scores candidate chunks to improve relevance ordering. Returns `list[ScoredChunk]`.

### Formatter ([`retrieval/formatter.py`](src/corpus/retrieval/formatter.py:1))

[`format_response()`](src/corpus/retrieval/formatter.py:1) assembles the final human-readable response from ranked chunks and decision cards.

### Symbolic Filter ([`retrieval/symbolic_filter.py`](src/corpus/retrieval/symbolic_filter.py:1))

[`extract_constraints(question)`](src/corpus/retrieval/symbolic_filter.py:1) parses structured constraints (domain, capability, date ranges) from natural-language queries to pre-filter candidates.

## Telemetry Subsystem

### Collector ([`telemetry/collector.py`](src/corpus/telemetry/collector.py:1))

[`record_outcome(session, decision_id, outcome)`](src/corpus/telemetry/collector.py:1) persists success/failure outcomes for decisions to `TelemetryOutcome` records.

### Calibrator ([`telemetry/calibrator.py`](src/corpus/telemetry/calibrator.py:1))

[`calibrate(session)`](src/corpus/telemetry/calibrator.py:1) recomputes confidence scores for decision cards based on accumulated telemetry outcomes. Returns a `CalibrationReport` with `decisions_evaluated`, `decisions_recalibrated`, and individual `adjustments`.

### Compactor ([`telemetry/compactor.py`](src/corpus/telemetry/compactor.py:1))

[`compact_telemetry()`](src/corpus/telemetry/compactor.py:1) aggregates and prunes old telemetry records to prevent unbounded growth.

### Metrics ([`telemetry/metrics.py`](src/corpus/telemetry/metrics.py:1))

[`compute_metrics(session)`](src/corpus/telemetry/metrics.py:1) calculates operational metrics and returns a `CorpusMetrics` dataclass:

- `total_runs`, `completed_runs` — run counts
- `total_artifacts`, `total_chunks` — content volume
- `total_decisions`, `total_drift_events` — decision health
- `unresolved_reviews` — human queue depth
- `contradiction_density` — fraction of decisions with drift
- `vector_synced_pct` — vector store sync completeness

## Dependencies

Core runtime dependencies (from [`pyproject.toml`](pyproject.toml:1)):

| Package | Purpose |
|---------|---------|
| `sqlalchemy>=2.0` | ORM and database engine |
| `pydantic>=2.0` / `pydantic-settings>=2.0` | Configuration management |
| `click` | CLI framework |
| `sentence-transformers` | Embedding model for L2 dedup and vector sync |
| `datasketch` | MinHash LSH for L1 dedup |
| `numpy` | Numeric operations |
| `chromadb` | Vector store |
| `networkx` | Knowledge graph |
| `openai` | LLM API client (OpenAI-compatible) |
| `watchdog>=3.0` | Filesystem event monitoring |
| `beautifulsoup4>=4.12` | HTML parsing |
| `pymupdf>=1.24` | PDF parsing |

Optional:

| Package | Extra | Purpose |
|---------|-------|---------|
| `gitpython>=3.1` | `git` | Git-based branch diffing |
| `pytest`, `ruff`, `mypy` | `dev` | Testing and code quality |