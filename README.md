# Corpus Pipeline

> Drop files into a folder. Get a searchable, deduplicated, indexed knowledge corpus.

## Overview

A self-contained Python package that ingests raw documents (HTML, PDF, Markdown, plain text), parses them, classifies them by domain, deduplicates content using a 3-layer pipeline (MinHash → Embedding similarity → LLM arbitration), generates decision cards with confidence scoring, and syncs everything to vector (ChromaDB) and graph (NetworkX) stores for retrieval.

**Key capabilities:**

- **Multi-format ingestion** — Markdown, HTML, PDF, and plain-text files via drop-folder or CLI
- **3-layer deduplication** — MinHash LSH → sentence-transformer embeddings → LLM arbitration
- **Decision card synthesis** — LLM-generated architectural decision records with confidence scores
- **Hybrid retrieval** — semantic vector search + knowledge-graph expansion + symbolic filtering
- **Quality gates** — automated checks for completeness, reference integrity, and sync health
- **Telemetry** — outcome tracking, confidence calibration, and operational metrics

> **Note:** LLM features (dedup Layer 3, decision generation) require a `CORPUS_KILO_API_KEY`. The pipeline functions without one — L3 disagreements auto-resolve as `keep_both` and decision generation is skipped.

## Quick Start

### Prerequisites

- Python 3.12+
- pip

### Installation

```bash
# Clone and switch to the corpus-pipeline branch
git clone <repo-url>
git checkout corpus-pipeline

# Install in development mode
pip install -e ".[dev]"

# Initialize the database
corpus init
```

### Drop-Folder Workflow (Recommended)

The simplest way to use the corpus pipeline:

```bash
# Start watching C:\Users\Ice\scrape (default)
corpus watch

# Or specify a custom directory
corpus watch --dir /path/to/your/files

# Adjust poll interval (default 2 seconds)
corpus watch --poll-interval 5
```

Then just drop files into the watched folder:

- `.md`, `.markdown` — Markdown documents
- `.html`, `.htm` — HTML pages
- `.pdf` — PDF documents
- `.txt`, `.text`, `.log`, `.csv` — Plain text files

Files are automatically:

1. **Parsed** — format-specific extraction (title, content, metadata)
2. **Classified** — domain assignment based on path and content patterns
3. **Normalized & chunked** — H2-boundary splitting for Markdown, paragraph splitting for text
4. **Stored** in SQLite database as artifacts and chunks
5. **Moved** to `processed/` subdirectory to avoid re-ingestion

### Single File Ingestion

```bash
corpus ingest-file C:\path\to\document.pdf
```

### Git-Based Ingestion

For ingesting changes from a git branch (requires `pip install corpus[git]`):

```bash
corpus ingest my-feature-branch --base main --repo-path .
```

## CLI Reference

List all available commands:

```bash
corpus --help
```

### Core Commands

| Command | Description |
|---------|-------------|
| `corpus init` | Initialize database, run migrations, create data directories |
| `corpus watch` | Watch drop-folder for new files and auto-ingest |
| `corpus ingest-file <path>` | Ingest a single file (no git required) |
| `corpus ingest <branch>` | Ingest changed files from a git branch diff |
| `corpus dedup <run_id>` | Run 3-layer deduplication pipeline |
| `corpus generate-decisions <run_id>` | Generate decision cards via LLM deep research |
| `corpus update-decisions <run_id>` | Recompute impacted decision cards and drift events |
| `corpus check-references <run_id>` | Validate reference integrity and apply rewrites |
| `corpus sync-derived <run_id>` | Sync to ChromaDB vectors + NetworkX graph |
| `corpus complete <run_id>` | Run quality gates and finalize a run |
| `corpus run <branch>` | Execute full pipeline (ingest → dedup → decisions → refs → sync → gates) |
| `corpus query <text>` | Search the corpus with hybrid retrieval |
| `corpus status` | Show corpus health metrics and queue status |

### Maintenance Commands

| Command | Description |
|---------|-------------|
| `corpus migrate` | Run pending schema migrations |
| `corpus migrate --rollback` | Rollback the last migration |
| `corpus rebuild-vectors` | Full vector rebuild from relational store |
| `corpus rebuild-graph` | Full graph rebuild from relational store |

### Review Queue Commands

| Command | Description |
|---------|-------------|
| `corpus review list` | List unresolved human review items |
| `corpus review list --run-id <id>` | Filter review items by run |
| `corpus review resolve <id> <disposition>` | Resolve a review item |

### Telemetry Commands

| Command | Description |
|---------|-------------|
| `corpus telemetry record <decision_id> <outcome>` | Record a decision outcome |
| `corpus telemetry calibrate` | Recompute confidence calibration |
| `corpus telemetry metrics` | Print operational metrics |

## Configuration

All settings are managed via environment variables (prefix `CORPUS_`) through Pydantic Settings. Defined in [`CorpusSettings`](src/corpus/config.py:7).

| Variable | Default | Description |
|----------|---------|-------------|
| `CORPUS_DB_URL` | `sqlite:///data/corpus.db` | Database connection string |
| `CORPUS_CHROMA_DIR` | `data/chroma` | ChromaDB storage directory |
| `CORPUS_GRAPH_PATH` | `data/graph.json` | NetworkX graph file path |
| `CORPUS_EMBEDDING_MODEL` | `all-MiniLM-L6-v2` | Sentence-transformer model |
| `CORPUS_WATCH_DIR` | `C:\Users\Ice\scrape` | Drop-folder path |
| `CORPUS_POLL_INTERVAL` | `2.0` | Watcher poll interval (seconds) |
| `CORPUS_KILO_API_KEY` | *(none)* | API key for LLM features |
| `CORPUS_LLM_BASE_URL` | `https://api.kilo.ai/api/gateway` | LLM API endpoint |
| `CORPUS_LLM_MODEL` | `google/gemini-2.5-flash` | LLM model for arbitration |
| `CORPUS_DECISION_MODEL` | `perplexity/sonar-deep-research` | LLM model for decision generation |
| `CORPUS_MAX_ARBITRATION_CALLS` | `500` | Max LLM calls per dedup run |
| `CORPUS_DEDUP_L1_THRESHOLD` | `0.5` | MinHash Jaccard similarity threshold |
| `CORPUS_DEDUP_L2_THRESHOLD` | `0.85` | Embedding cosine similarity threshold |
| `CORPUS_ARBITRATION_CONFIDENCE_MIN` | `0.70` | Minimum arbitration confidence |
| `CORPUS_L3_RATE_ALERT_THRESHOLD` | `0.20` | L3 escalation rate alert threshold |
| `CORPUS_SYNC_LAG_TOLERANCE_SECONDS` | `300` | Max acceptable sync lag |

## Project Structure

```
├── pyproject.toml                          # Package metadata and dependencies
├── README.md                               # This file
├── ARCHITECTURE.md                         # Detailed architecture documentation
│
├── src/corpus/
│   ├── __init__.py                         # Package root, version
│   ├── cli.py                              # Click CLI entry point
│   ├── config.py                           # CorpusSettings (pydantic-settings)
│   │
│   ├── db/                                 # Database layer
│   │   ├── engine.py                       # SQLAlchemy engine + session factory
│   │   ├── models.py                       # 10 ORM models (Base → ConsolidationRun, etc.)
│   │   ├── repository.py                   # CorpusRepository data-access class
│   │   └── migrations/
│   │       ├── runner.py                   # Forward/rollback migration runner
│   │       └── versions/
│   │           └── 001_initial.sql         # Initial schema DDL
│   │
│   ├── ingestion/                          # Stage 1: Document ingestion
│   │   ├── parsers.py                      # Multi-format parser (MD, HTML, PDF, TXT)
│   │   ├── watcher.py                      # Drop-folder watchdog observer
│   │   ├── pipeline.py                     # Git-based + single-file ingestion
│   │   ├── classifier.py                   # Path-based domain/capability classifier
│   │   ├── enumerator.py                   # Git diff enumerator
│   │   ├── normalizer.py                   # Content normalizer + H2 chunker
│   │   └── path_mapper.py                  # Source→canonical path mapper
│   │
│   ├── dedup/                              # Stage 2: 3-layer deduplication
│   │   ├── pipeline.py                     # Dedup orchestrator (L1→L2→L3)
│   │   ├── minhash.py                      # L1: MinHash LSH candidate generation
│   │   ├── embeddings.py                   # L2: Embedding cosine similarity
│   │   └── arbitrator.py                   # L3: LLM arbitration
│   │
│   ├── decisions/                          # Stage 3: Decision card management
│   │   ├── generator.py                    # LLM-based decision card generation
│   │   ├── card_updater.py                 # Recompute impacted cards per run
│   │   ├── drift_detector.py               # Confidence-score drift detection
│   │   └── index_updater.py                # Decision index rebuilder
│   │
│   ├── references/                         # Stage 4: Reference management
│   │   ├── rewriter.py                     # Apply path rewrites to files
│   │   ├── rewrite_mapper.py               # Generate rewrite maps per run
│   │   └── integrity_validator.py          # Validate link integrity
│   │
│   ├── sync/                               # Stage 5: Derived store sync
│   │   ├── vector_sync.py                  # ChromaDB vector upsert/rebuild
│   │   ├── graph_sync.py                   # NetworkX graph sync/rebuild
│   │   └── health_checker.py               # Sync health verification
│   │
│   ├── consolidation/                      # Stage 6: Run lifecycle
│   │   ├── run_controller.py               # Run completion + gate orchestration
│   │   ├── gate_runner.py                  # Quality gate battery
│   │   └── branch_retirement.py            # Post-merge branch cleanup
│   │
│   ├── retrieval/                          # Query subsystem
│   │   ├── orchestrator.py                 # Hybrid retrieval orchestrator
│   │   ├── reranker.py                     # Chunk reranking
│   │   ├── formatter.py                    # Response formatting
│   │   └── symbolic_filter.py              # Symbolic constraint extraction
│   │
│   └── telemetry/                          # Observability
│       ├── collector.py                    # Outcome recording
│       ├── calibrator.py                   # Confidence recalibration
│       ├── compactor.py                    # Telemetry compaction
│       └── metrics.py                      # Operational metrics
│
├── tests/                                  # Mirror of src/ structure
│   ├── conftest.py                         # Shared fixtures
│   ├── ingestion/                          # Ingestion unit + integration tests
│   ├── dedup/                              # Dedup unit tests
│   ├── decisions/                          # Decision card tests
│   ├── references/                         # Reference tests
│   ├── sync/                               # Sync tests
│   ├── consolidation/                      # Gate/controller tests
│   ├── retrieval/                          # Retrieval tests
│   ├── telemetry/                          # Telemetry tests
│   ├── db/                                 # DB model/repo/migration tests
│   └── integration/                        # End-to-end pipeline tests
│
└── scripts/
    ├── bootstrap_corpus.py                 # Bootstrap script for initial setup
    └── run_full_ingestion.py               # Full ingestion script
```

## Pipeline Stages

The corpus pipeline executes six stages in sequence. The `corpus run` command runs all stages; individual stages can also be invoked separately.

### 1. Ingestion

Parse files, classify by domain, normalize content, split into chunks, and store as `ResearchArtifact` + `ArtifactChunk` records.

- **Parsers** ([`parsers.py`](src/corpus/ingestion/parsers.py:1)) — auto-detect format from extension; extract title, content, metadata
- **Classifier** ([`classifier.py`](src/corpus/ingestion/classifier.py:1)) — map file paths to domain/capability tags using a taxonomy
- **Normalizer** ([`normalizer.py`](src/corpus/ingestion/normalizer.py:1)) — H2-heading chunking for Markdown, paragraph chunking for text
- **Watcher** ([`watcher.py`](src/corpus/ingestion/watcher.py:1)) — `watchdog`-based observer with 2-second debounce and backlog processing

### 2. Deduplication

Three-layer pipeline that progressively filters duplicate content:

- **L1 — MinHash LSH** ([`minhash.py`](src/corpus/dedup/minhash.py:1)) — fast Jaccard similarity to generate candidate pairs (threshold: 0.5)
- **L2 — Embeddings** ([`embeddings.py`](src/corpus/dedup/embeddings.py:1)) — cosine similarity on sentence-transformer vectors to confirm/reject (threshold: 0.85)
- **L3 — LLM Arbitration** ([`arbitrator.py`](src/corpus/dedup/arbitrator.py:1)) — LLM resolves L1/L2 disagreements; routes low-confidence pairs to human review

### 3. Decision Generation

Create or update `DecisionCard` records from corpus content using LLM deep research. Cards carry confidence scores that are recalibrated based on telemetry outcomes.

### 4. Reference Management

Rewrite internal links when artifacts move to canonical paths. Validate that all cross-references resolve correctly.

### 5. Derived Store Sync

Push chunk embeddings to ChromaDB and build/update the NetworkX knowledge graph (artifact → decision → capability edges).

### 6. Quality Gates

Verify corpus consistency before finalizing a run:

- Capability tags are populated with decision-card mappings
- Human review queue is empty
- All artifacts are classified
- Reference integrity passes
- Vector/graph sync health is within tolerance

## Development

### Running Tests

```bash
# All tests
pytest tests/

# Specific module tests
pytest tests/ingestion/       # Ingestion tests
pytest tests/dedup/           # Dedup tests
pytest tests/decisions/       # Decision card tests
pytest tests/db/              # Database tests
pytest tests/sync/            # Sync tests
pytest tests/integration/     # End-to-end integration tests

# With coverage
pytest tests/ --cov=corpus --cov-report=term-missing

# Skip integration tests that need external services
pytest tests/ -m "not integration"
```

### Code Quality

```bash
# Lint
ruff check src/ tests/

# Type checking
mypy src/
```

## License

See LICENSE file.
