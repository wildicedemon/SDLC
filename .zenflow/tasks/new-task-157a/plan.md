# Full SDD workflow

## Configuration
- **Artifacts Path**: {@artifacts_path} → `.zenflow/tasks/{task_id}`

---

## Agent Instructions

If you are blocked and need user clarification, mark the current step with `[!]` in plan.md before stopping.

---

## Workflow Steps

### [x] Step: Requirements
<!-- chat-id: 5499eaa3-7869-40ef-a174-7e47ff573671 -->

Create a Product Requirements Document (PRD) based on the feature description.

1. Review `docs/research/00_meta/knowledge_architecture_contract.md` and `confidence_policy.md` to extract functional requirements (greenfield project — no existing application code to review)
2. Analyze the feature definition and identify unclear aspects
3. Ask the user for clarifications on aspects that significantly impact scope or user experience
4. Make reasonable decisions for minor details based on context and conventions
5. If user can't clarify, make a decision, state the assumption, and continue

Save the PRD to `{@artifacts_path}/requirements.md`.

### [x] Step: Technical Specification
<!-- chat-id: 2d819299-e496-4d21-a4dd-99bdbd01cd0c -->

Create a technical specification based on the PRD in `{@artifacts_path}/requirements.md`.

1. Review `docs/research/00_meta/` policy documents and `scripts/` for conventions
2. Define the implementation approach

Save to `{@artifacts_path}/spec.md` with:
- Technical context (language, dependencies)
- Implementation approach referencing existing code patterns
- Source code structure changes
- Data model / API / interface changes
- Delivery phases (incremental, testable milestones)
- Verification approach using project lint/test commands

### [x] Step: Planning
<!-- chat-id: a8558048-d752-487b-8a1e-bba0788435c9 -->

Create a detailed implementation plan based on `{@artifacts_path}/spec.md`.

### [x] Step: Project Scaffolding and Configuration
<!-- chat-id: 5f17cc6d-1265-4aaa-901f-c7c0ed0c9206 -->

Set up the `corpus/` Python package, dependencies, configuration, and CLI skeleton.

- Create `corpus/pyproject.toml` with all dependencies from spec §1.3 (sqlalchemy, alembic, sentence-transformers, datasketch, numpy, chromadb, networkx, click, gitpython, pydantic, pytest, pytest-asyncio, openai, ruff, mypy)
- Create `corpus/src/corpus/__init__.py`
- Create `corpus/src/corpus/config.py` with `CorpusSettings(BaseSettings)` validating all env vars from spec §8.1
- Create `corpus/src/corpus/cli.py` with Click group and placeholder subcommands: `init`, `migrate`, `ingest`, `dedup`, `update-decisions`, `check-references`, `sync-derived`, `complete`, `run`, `review`, `query`, `rebuild-vectors`, `rebuild-graph`, `telemetry`, `status`
- Add `data/` to `.gitignore`
- Create `corpus/tests/conftest.py` with shared fixtures (tmp SQLite DB, tmp data dirs)
- **Verify**: `pip install -e corpus/` succeeds; `corpus --help` prints CLI help; `ruff check src/ tests/` passes; `mypy src/corpus/` passes

### [x] Step: Kilo Gateway + GLM-5 Integration Test
<!-- chat-id: 86ae89fd-99a7-4275-997f-4e10216569f7 -->

Verify AI arbitration backend connectivity before building pipeline components that depend on it. Uses Kilo AI Gateway (OpenAI-compatible) instead of direct OpenAI API.

- Write a standalone test in `corpus/tests/test_kilo_gateway.py` that:
  - Sends a `POST` to `https://api.kilo.ai/api/gateway/chat/completions` with model `z-ai/glm-5:free`
  - Uses **no auth** (anonymous access: 200 requests/hour/IP for free models)
  - Sends a minimal prompt: `{"model": "z-ai/glm-5:free", "messages": [{"role": "user", "content": "Reply with the word OK"}], "max_tokens": 10}`
  - Asserts HTTP 200 and non-empty `choices[0].message.content`
- Update `corpus/src/corpus/config.py`:
  - Replace `CORPUS_OPENAI_API_KEY` with `CORPUS_KILO_API_KEY` (optional — empty string for free models)
  - Set `CORPUS_LLM_BASE_URL` default to `https://api.kilo.ai/api/gateway`
  - Set `CORPUS_LLM_MODEL` default to `z-ai/glm-5:free`
- Verify the `openai` Python SDK works with `base_url="https://api.kilo.ai/api/gateway"` and `api_key=""` for free-tier access
- **Success criteria**: Test passes with HTTP 200 and a valid response body
- **If verification fails**: Check if `z-ai/glm-5:free` is listed at `GET https://api.kilo.ai/api/gateway/models`; if model unavailable, try `minimax/minimax-m2.1:free` as fallback; if gateway unreachable, mark step `[!]` and escalate

### [x] Step: Schema Models
<!-- chat-id: 0468e306-8f39-467b-9b03-d2f0d3fbb5b3 -->

Implement SQLAlchemy ORM models only — no migrations, no repository layer yet. Per spec §3.1.

- Create `corpus/src/corpus/db/__init__.py`
- Create `corpus/src/corpus/db/engine.py`: SQLite engine factory (`create_engine`), `get_session` context manager
- Create `corpus/src/corpus/db/models.py`: SQLAlchemy 2.0 declarative models for all 10 entities (`ConsolidationRun`, `ResearchArtifact`, `ArtifactChunk`, `DecisionCard`, `DriftEvent`, `ReferenceRewriteMap`, `ReferenceIntegrityReport`, `HumanReviewQueue`, `CapabilityMapping`, `TelemetryOutcome`)
  - All PK/FK constraints, UNIQUE constraints, and CHECK constraints for status enums
  - JSON columns stored as TEXT with SQLAlchemy `JSON` type
- Tests in `corpus/tests/db/test_models.py`:
  - Assert: `Base.metadata.create_all()` creates exactly 10 tables
  - Assert: inserting a `ResearchArtifact` without `run_id` FK raises `IntegrityError`
  - Assert: inserting a `ConsolidationRun` with `status='invalid'` raises `IntegrityError` (CHECK constraint)
  - Assert: duplicate `UNIQUE(artifact_id, chunk_index)` on `ArtifactChunk` raises `IntegrityError`
- **Verify**: `pytest tests/db/test_models.py -v` — all 4+ assertions pass
- **If verification fails**: Fix constraint definitions; if SQLite doesn't enforce CHECK constraints by default, enable `PRAGMA foreign_keys=ON` in engine factory

### [x] Step: Migration Runner
<!-- chat-id: 5b89b6c0-b93e-4444-b450-791b21dc303a -->

Implement forward/rollback migration mechanism — no CRUD yet.

- Create `corpus/src/corpus/db/migrations/__init__.py`
- Create `corpus/src/corpus/db/migrations/runner.py`: reads numbered `.sql` files from `versions/`, executes in order; supports `--rollback` to reverse last applied version; tracks applied versions in a `_schema_versions` table
  - Single-version rollback with cascading foreign key deletes
  - Rollback deletes all data for the rolled-back schema version (clean slate, not surgical)
- Create `corpus/src/corpus/db/migrations/versions/001_initial.sql`: DDL for all 10 tables matching ORM models; includes `-- rollback:` section with `DROP TABLE` statements in FK-safe order
- Wire `corpus init` CLI to call `engine.create_all()` + migration runner; wire `corpus migrate` and `corpus migrate --rollback`
- Tests in `corpus/tests/db/test_migrations.py`:
  - Assert: `corpus init` on empty DB → `_schema_versions` contains `001`; all 10 tables exist via `PRAGMA table_info`
  - Assert: `corpus migrate --rollback` → `_schema_versions` is empty; all 10 tables are gone
  - Assert: re-running `corpus init` after rollback restores all tables (idempotent)
- **Verify**: `pytest tests/db/test_migrations.py -v` — all 3 assertions pass
- **If verification fails**: Check `DROP TABLE` order for FK dependency cycles; if circular, use `PRAGMA foreign_keys=OFF` during rollback

### [x] Step: Repository CRUD — Core Entities

Implement data-access layer for the 3 most-used entities: `consolidation_runs`, `research_artifacts`, `decision_cards`.

- Create `corpus/src/corpus/db/repository.py` with class `CorpusRepository`:
  - Constructor takes a `Session`
  - Methods per entity: `create_run()`, `get_run()`, `list_runs()`, `update_run_status()`; same pattern for `artifact` and `decision_card`
  - All writes flush and return the created/updated object
- Tests in `corpus/tests/db/test_repository_core.py`:
  - Assert: `create_run()` persists and `get_run()` retrieves with all fields matching
  - Assert: `create_artifact()` with valid `run_id` FK succeeds; with nonexistent `run_id` raises `IntegrityError`
  - Assert: `list_runs(status='pending')` returns only runs with that status
  - Assert: `update_run_status(run_id, 'completed')` changes status and `completed_at` is set
  - Assert: `create_decision_card()` persists; `get_decision_card()` returns with JSON fields deserialized
- **Verify**: `pytest tests/db/test_repository_core.py -v` — all 5 assertions pass
- **If verification fails**: Check Session lifecycle (commit vs flush); ensure JSON fields round-trip correctly through SQLite TEXT storage

### [x] Step: Repository CRUD — Supporting Entities
<!-- chat-id: 615e5cb9-6544-4ad7-b196-5f7c2f932202 -->

Implement data-access layer for remaining 7 entities: `artifact_chunks`, `drift_events`, `reference_rewrite_maps`, `reference_integrity_reports`, `human_review_queue`, `capability_mappings`, `telemetry_outcomes`.

- Extend `CorpusRepository` in `repository.py` with CRUD methods for each entity following the same pattern as core entities
- Tests in `corpus/tests/db/test_repository_supporting.py`:
  - Assert: `create_chunk()` enforces `UNIQUE(artifact_id, chunk_index)` — duplicate raises `IntegrityError`
  - Assert: `create_drift_event()` with valid `decision_id` and `run_id` FKs succeeds
  - Assert: `create_review_item()` with `disposition=NULL` → `list_unresolved_reviews(run_id)` returns it; after `resolve_review(id, 'approved_merge')` → `list_unresolved_reviews` returns empty
  - Assert: `create_capability_mapping()` enforces `UNIQUE(capability, decision_id)`
  - Assert: `create_telemetry_outcome()` persists and `list_outcomes(decision_id)` returns all for that decision
  - Assert: `create_rewrite_map_entry()` and `create_integrity_report_entry()` persist with correct `run_id` FK
- **Verify**: `pytest tests/db/test_repository_supporting.py -v` — all 6 assertions pass
- **If verification fails**: Check FK references exist (parent records must be created first in test fixtures)

### [x] Step: Smoke Test — DB Round-Trip
<!-- chat-id: ea469ded-62e0-4cb4-96c5-4f5715ab5f07 -->

Integration checkpoint: verify the full relational stack works end-to-end before building ingestion.

- Create `corpus/tests/integration/test_db_roundtrip.py`:
  - Use a tmp SQLite DB (not the production path)
  - Run migration forward → create a `ConsolidationRun` → create 2 `ResearchArtifact`s linked to it → create 3 `ArtifactChunk`s → create 1 `DecisionCard` → create 1 `CapabilityMapping` → create 1 `DriftEvent`
  - Assert: all records retrievable by ID with correct FK relationships
  - Assert: rollback migration → all tables gone → re-migrate → tables restored (empty)
  - Assert: `list_runs()` returns 0 after rollback+re-migrate (data wiped)
- **Verify**: `pytest tests/integration/test_db_roundtrip.py -v` passes
- **If verification fails**: This indicates a fundamental schema or repository bug — fix before proceeding; do not continue to ingestion with a broken data layer
- Run `ruff check src/ tests/` and `mypy src/corpus/` — fix any issues

### [x] Step: Git Enumerator
<!-- chat-id: 99c98976-8039-4ea2-9052-64e328d5edce -->

Implement file enumeration from git branches/worktrees. Mock-friendly, no other ingestion components yet.

- Create `corpus/src/corpus/ingestion/__init__.py`
- Create `corpus/src/corpus/ingestion/enumerator.py`:
  - `enumerate_changes(repo_path, source_branch, base_branch='main') -> list[ChangedFile]`
  - `ChangedFile` dataclass: `path`, `change_type` (added/modified/deleted), `content` (bytes or None for deleted)
  - Uses GitPython to diff `base_branch...source_branch`
  - Filters to `.md` files only (corpus is markdown-based)
- Tests in `corpus/tests/ingestion/test_enumerator.py`:
  - Use a tmp git repo fixture (init, commit base files, create branch, add/modify/delete files)
  - Assert: added file appears with `change_type='added'` and non-empty `content`
  - Assert: modified file appears with `change_type='modified'`
  - Assert: deleted file appears with `change_type='deleted'` and `content=None`
  - Assert: non-.md files are excluded
  - Assert: nonexistent branch raises `ValueError` with descriptive message
- **Verify**: `pytest tests/ingestion/test_enumerator.py -v` — all 5 assertions pass
- **If verification fails**: Check GitPython diff API (`repo.git.diff('--name-status', ...)`); ensure tmp repo fixture creates proper commits

### [x] Step: Classifier
<!-- chat-id: 9a5825f4-7c91-4218-ba77-1bfe55630488 -->

Implement domain/capability tag classification from file paths. Hardcoded rules first based on canonical directory contract.

- Create `corpus/src/corpus/ingestion/classifier.py`:
  - `classify(path: str) -> Classification` where `Classification` has `domain_tags: list[str]`, `capability_tags: list[str]`, `is_classified: bool`
  - Rules derived from `docs/research/00_meta/corpus_organization_standard.md`: map directory prefixes (`01_meta_architecture/security_architecture/` → domain=`security_architecture`, capability from filename convention)
  - Return `is_classified=False` for paths that don't match any known domain directory
- Tests in `corpus/tests/ingestion/test_classifier.py`:
  - Assert: `docs/research/01_meta_architecture/security_architecture/patterns.md` → `domain_tags=['security_architecture']`, `is_classified=True`
  - Assert: `docs/research/09_research_discipline/research_benchmarking_framework/overview.md` → `domain_tags=['research_benchmarking_framework']`, `is_classified=True`
  - Assert: `random/unknown/file.md` → `is_classified=False`
  - Assert: `docs/research/00_meta/confidence_policy.md` → classified as meta (not a domain artifact, but still classified)
  - Assert: all 12 domain directories (`01_*` through `12_*`) have at least one matching rule
- **Verify**: `pytest tests/ingestion/test_classifier.py -v` — all 5 assertions pass
- **If verification fails**: Cross-reference directory listing from `docs/research/` against classifier rules; add missing patterns

### [x] Step: Normalizer
<!-- chat-id: ab89a93f-8a64-4a12-b2a3-f350fddbcecc -->

Implement content normalization — single-file first, then multi-file merge into canonical pages.

- Create `corpus/src/corpus/ingestion/normalizer.py`:
  - `normalize(content: str, domain: str, canonical_path: str) -> NormalizedResult`
  - `NormalizedResult`: `chunks: list[str]` (split by heading sections), `title: str`, `merged: bool` (whether content was appended to existing file)
  - Chunking strategy: split on `## ` headings; each chunk is a self-contained section
  - If `canonical_path` exists, append new sections (merge); otherwise create new file
- Tests in `corpus/tests/ingestion/test_normalizer.py`:
  - Assert: single markdown file → splits into N chunks at `## ` boundaries; each chunk is non-empty
  - Assert: file with no `## ` headings → single chunk containing full content
  - Assert: merge mode — existing canonical file gets new sections appended, not overwritten
  - Assert: chunk count matches heading count + 1 (preamble before first heading)
- **Verify**: `pytest tests/ingestion/test_normalizer.py -v` — all 4 assertions pass
- **If verification fails**: Check heading regex; ensure merge doesn't duplicate existing sections

### [x] Step: Path Mapper + Ingestion Integration
<!-- chat-id: 7d779109-9099-4b1d-bc59-317d822e4ce5 -->

Wire all ingestion components together with path mapping and the `corpus ingest` CLI command.

- Create `corpus/src/corpus/ingestion/path_mapper.py`:
  - `record_mapping(old_path: str, new_path: str, run_id: str) -> None`
  - Stores mappings in `reference_rewrite_maps` table via repository
- Wire `corpus ingest <branch-or-worktree>` CLI command:
  - Create `ConsolidationRun` with `status='running'`
  - Call enumerator → classifier → normalizer → path_mapper
  - Store `ResearchArtifact` + `ArtifactChunk` records in DB
  - If any files have `is_classified=False`: print error listing unclassified files, set run `status='failed'`, exit with code 1 (FR-2.6)
  - On success: print summary (artifacts ingested, chunks created)
- Tests in `corpus/tests/ingestion/test_path_mapper.py`:
  - Assert: `record_mapping('old/path.md', 'new/path.md', run_id)` → retrievable from DB
  - Assert: multiple mappings for same `run_id` all persist
- Tests in `corpus/tests/ingestion/test_ingest_integration.py`:
  - Assert: `corpus ingest <test-branch>` → `consolidation_runs` has 1 record with `status='running'`; `research_artifacts` has N records; `artifact_chunks` has M records (M >= N)
  - Assert: ingest with unclassified file → run `status='failed'`, exit code 1
- **Verify**: `pytest tests/ingestion/ -v` — all tests pass
- **If verification fails**: Check that enumerator→classifier→normalizer chain passes data correctly; verify repository FK constraints satisfied (run must exist before artifacts)

### [x] Step: Smoke Test — Ingest to DB
<!-- chat-id: 0f3628e4-adbe-4ec5-b2e7-f401c51a551f -->

Integration checkpoint: verify ingestion produces queryable relational state.

- Create `corpus/tests/integration/test_ingest_smoke.py`:
  - Set up tmp git repo with a branch containing 3 markdown files in `docs/research/01_meta_architecture/` and 1 in `09_research_discipline/`
  - Run `corpus init` + `corpus ingest <branch>`
  - Assert: `consolidation_runs` has 1 record, `artifacts_ingested >= 4`
  - Assert: `research_artifacts` has 4 records, each with non-empty `domain_tags`
  - Assert: `artifact_chunks` has at least 4 records (1+ per artifact)
  - Assert: no unclassified files (all `is_classified=True`)
- **Verify**: `pytest tests/integration/test_ingest_smoke.py -v` passes
- **If verification fails**: This blocks all downstream steps — fix ingestion before proceeding
- Run `ruff check src/ tests/` and `mypy src/corpus/` — fix any issues

### [x] Step: Dedup Pipeline and Human Review Queue
<!-- chat-id: ff2e7f57-6dfd-4b2d-b9b1-7168a3fd9db4 -->

Implement 3-layer dedup per FR-3 and human review queue per FR-4. AI arbitration uses Kilo Gateway (`z-ai/glm-5:free`).

- Create `corpus/src/corpus/dedup/__init__.py`
- Create `corpus/src/corpus/dedup/minhash.py`:
  - `generate_candidates(chunks: list[ArtifactChunk], threshold: float) -> list[CandidatePair]`
  - Uses `datasketch.MinHash` + `MinHashLSH`; threshold from `CORPUS_DEDUP_L1_THRESHOLD` (default 0.5)
- Create `corpus/src/corpus/dedup/embeddings.py`:
  - `filter_candidates(pairs: list[CandidatePair], threshold: float) -> tuple[list[ConfirmedDup], list[Disagreement]]`
  - Uses `sentence-transformers` with `all-MiniLM-L6-v2`; cosine similarity threshold from `CORPUS_DEDUP_L2_THRESHOLD` (default 0.85)
  - Returns `ConfirmedDup` (L1+L2 agree) and `Disagreement` (L1 says dup, L2 says not)
- Create `corpus/src/corpus/dedup/arbitrator.py`:
  - `arbitrate(disagreements: list[Disagreement]) -> list[ArbitrationResult]`
  - Calls Kilo Gateway at `CORPUS_LLM_BASE_URL` with model `CORPUS_LLM_MODEL` via `openai` Python SDK
  - Returns `ArbitrationResult` with `confidence: float`, `recommendation: merge|keep_both|discard_one`
  - If API call fails: log warning, route all disagreements to human queue (graceful degradation)
- Create `corpus/src/corpus/dedup/pipeline.py`:
  - `run_dedup(run_id: str) -> DedupReport`
  - Orchestrates L1 → L2 → L3 → human queue routing (confidence < 0.70 → `human_review_queue`)
  - Computes L3 call rate: if > 20% of L1 candidates, log warning and set `l3_rate_alert=True` in report
  - Generates `DedupReport` dataclass with candidate_count, confirmed_dups, arbitrated, human_queued, l3_rate, l3_rate_alert
- Wire `corpus dedup <run-id>` CLI command
- Wire `corpus review list` and `corpus review resolve <id> <disposition>` CLI commands
- Tests in `corpus/tests/dedup/test_minhash.py`:
  - Assert: two identical chunks → candidate pair generated
  - Assert: two completely different chunks → no candidate pair
  - Assert: near-duplicate (80% overlap) → candidate pair generated at threshold 0.5
- Tests in `corpus/tests/dedup/test_embeddings.py`:
  - Assert: semantically similar pair → cosine > 0.85 → `ConfirmedDup` (use mock embeddings in unit test)
  - Assert: unrelated pair → cosine < 0.85 → `Disagreement`
- Tests in `corpus/tests/dedup/test_arbitrator.py`:
  - Assert: mock Kilo API returns confidence 0.80 → `ArbitrationResult` with `recommendation`
  - Assert: mock API failure → all disagreements routed to human queue
  - Assert: mock API returns confidence 0.60 → item routed to human queue
- Tests in `corpus/tests/dedup/test_pipeline.py`:
  - Assert: pipeline with 0 candidates → empty report, no L3 calls
  - Assert: pipeline with 5 L1 candidates, 3 confirmed by L2, 2 disagreements → 2 L3 calls
  - Assert: L3 rate > 20% → `l3_rate_alert=True` in report
  - Assert: human queue items created for confidence < 0.70
- **Verify**: `pytest tests/dedup/ -v` — all assertions pass
- **If L3 call rate > 20%**: Log warning in dedup report, continue current run, add TODO to tune L1/L2 thresholds before next run
- **If Kilo Gateway unreachable**: All disagreements go to human queue; dedup report notes `arbitration_fallback=True`; run proceeds (not blocked)

### [x] Step: DecisionCard and Index Updater
<!-- chat-id: 040361e6-2aa3-4d57-adc9-ed9ec0621e40 -->

Implement decision surface updates per FR-5.

- Create `corpus/src/corpus/decisions/__init__.py`
- Create `corpus/src/corpus/decisions/card_updater.py`:
  - `update_impacted_cards(run_id: str) -> list[str]` (returns list of updated `decision_id`s)
  - Finds artifacts from current run → maps to capabilities → finds DecisionCards for those capabilities
  - Recomputes confidence: `0.3 * source_diversity + 0.3 * recency + 0.2 * downstream_success + 0.2 * (1 - contradiction_penalty)` per `confidence_policy.md`
  - Only touches cards linked to current run's artifacts (scoped update)
- Create `corpus/src/corpus/decisions/index_updater.py`:
  - `update_indices(decision_ids: list[str]) -> None`
  - Updates `capability_mappings` table for affected decisions
- Create `corpus/src/corpus/decisions/drift_detector.py`:
  - `detect_drift(run_id: str, previous_scores: dict[str, float]) -> list[str]` (returns created `event_id`s)
  - Emits `DriftEvent` when: confidence drops > 0.1, or new artifact contradicts existing recommendation
  - Sets `has_unresolved_contradiction=True` on affected `DecisionCard`
- Wire `corpus update-decisions <run-id>` CLI command
- Tests in `corpus/tests/decisions/test_card_updater.py`:
  - Assert: card with 3 diverse sources, recent data, no contradictions → confidence > 0.7
  - Assert: card with 1 source, stale data → confidence < 0.5
  - Assert: only cards linked to run's artifacts are updated; unrelated cards untouched
- Tests in `corpus/tests/decisions/test_drift_detector.py`:
  - Assert: confidence drop from 0.8 to 0.6 → `DriftEvent` created with `trigger='confidence_drop'`
  - Assert: contradicting artifact → `has_unresolved_contradiction=True` on card
  - Assert: no change in confidence → no `DriftEvent`
- Tests in `corpus/tests/decisions/test_index_updater.py`:
  - Assert: new capability mapping created for new decision
  - Assert: existing mapping not duplicated
- **Verify**: `pytest tests/decisions/ -v` — all assertions pass
- **If confidence formula produces out-of-range values**: Clamp to [0.0, 1.0]; log warning if clamping was needed

### [x] Step: Reference Integrity
<!-- chat-id: f2d0867d-67bf-4c25-b753-fa30d24bccb5 -->

Implement reference safety per FR-6.

- Create `corpus/src/corpus/references/__init__.py`
- Create `corpus/src/corpus/references/rewrite_mapper.py`:
  - `generate_rewrite_map(run_id: str) -> list[RewriteEntry]`
  - Reads `reference_rewrite_maps` table entries for the run
- Create `corpus/src/corpus/references/rewriter.py`:
  - `rewrite_references(rewrite_map: list[RewriteEntry], corpus_root: str) -> int` (returns count of rewrites applied)
  - Scans all `.md` files in `docs/research/` for markdown links `[text](old_path)` and replaces with `new_path`
  - Also rewrites references in index files (`03_indices/`) and run reports (`00_meta/run_reports/`)
- Create `corpus/src/corpus/references/integrity_validator.py`:
  - `validate_integrity(run_id: str, corpus_root: str) -> IntegrityReport`
  - Checks: (1) all `[text](path)` links in `.md` files resolve, (2) all `source_path` in `research_artifacts` table point to existing files
  - `IntegrityReport`: `broken_links: list`, `stale_paths: list`, `total_checked: int`, `passed: bool`
- Wire `corpus check-references <run-id>` CLI command
- Tests in `corpus/tests/references/test_rewriter.py`:
  - Assert: file containing `[link](old/path.md)` → after rewrite → contains `[link](new/path.md)`
  - Assert: file with no matching links → unchanged
  - Assert: multiple links in same file all rewritten
- Tests in `corpus/tests/references/test_integrity_validator.py`:
  - Assert: all links valid → `passed=True`, `broken_links` empty
  - Assert: introduce broken link → `passed=False`, `broken_links` contains the path
  - Assert: `source_path` pointing to deleted file → appears in `stale_paths`
- **Verify**: `pytest tests/references/ -v` — all assertions pass
- **If integrity check fails during a run**: Block run completion (do not mark `completed`); generate remediation report listing every broken link with file:line location; set run `status='failed'` with `remediation_report` populated

### [x] Step: Smoke Test — Ingest to Decision Update
<!-- chat-id: 47ed4a83-b4cd-42e4-ab39-f715f19be591 -->

Integration checkpoint: verify the core pipeline from ingestion through decision updates.

- Create `corpus/tests/integration/test_core_pipeline_smoke.py`:
  - Set up tmp git repo + DB; seed 2 existing DecisionCards with known capabilities
  - Create branch with 3 artifacts: 2 supporting existing capabilities, 1 near-duplicate pair
  - Run: `corpus init` → `corpus ingest <branch>` → `corpus dedup <run-id>` → `corpus update-decisions <run-id>`
  - Assert: dedup report shows 1 candidate pair
  - Assert: 2 DecisionCards updated (confidence recalculated)
  - Assert: if near-dup had low confidence arbitration → human queue has 1 item
  - Assert: `corpus review list` shows unresolved items (if any)
- **Verify**: `pytest tests/integration/test_core_pipeline_smoke.py -v` passes
- **If verification fails**: Indicates data flow break between components — check that artifact→capability→decision linkage is correct; fix before proceeding to derived layers
- Run `ruff check src/ tests/` and `mypy src/corpus/` — fix any issues

### [x] Step: Derived Layer Sync (Vector + Graph)
<!-- chat-id: 2f91763a-d77c-4adf-b026-9061481f85a3 -->

Implement derived layers per FR-7. These are rebuildable from relational source — no incremental rollback needed; rebuild commands wipe and recreate from scratch.

- Create `corpus/src/corpus/sync/__init__.py`
- Create `corpus/src/corpus/sync/vector_sync.py`:
  - `sync_vectors(run_id: str) -> SyncResult`: embed unsynced chunks → upsert into ChromaDB `corpus_chunks` collection → mark `embedding_synced=True`
  - `rebuild_vectors() -> SyncResult`: delete ChromaDB collection → re-embed all active chunks from relational
  - Uses `all-MiniLM-L6-v2` via `sentence-transformers`
- Create `corpus/src/corpus/sync/graph_sync.py`:
  - `sync_graph(run_id: str) -> SyncResult`: add/update nodes and edges for artifacts/decisions/capabilities touched by run
  - `rebuild_graph() -> SyncResult`: clear graph → rebuild all nodes/edges from relational → serialize to `data/graph.json`
  - Node types: `artifact`, `decision`, `capability`; edge types: `supports`, `addresses`, `conflicts_with`, `contradicts`
- Create `corpus/src/corpus/sync/health_checker.py`:
  - `check_sync_health() -> SyncHealthReport`: compare relational record counts vs vector/graph counts; check last sync timestamp vs `CORPUS_SYNC_LAG_TOLERANCE_SECONDS` (default 300)
  - `SyncHealthReport`: `vector_synced_pct: float`, `graph_node_count: int`, `lag_seconds: int`, `healthy: bool`
- Wire CLI: `corpus sync-derived <run-id>`, `corpus rebuild-vectors`, `corpus rebuild-graph`
- Tests in `corpus/tests/sync/test_vector_sync.py`:
  - Assert: 3 chunks synced → ChromaDB collection has 3 documents with 384-dim embeddings
  - Assert: `embedding_synced=True` on all 3 chunks after sync
  - Assert: rebuild produces same document count as incremental sync
- Tests in `corpus/tests/sync/test_graph_sync.py`:
  - Assert: 2 artifacts + 1 decision + 1 capability → graph has 4 nodes
  - Assert: artifact supporting decision → edge exists with label `supports`
  - Assert: rebuild from scratch produces identical graph structure
  - Assert: `data/graph.json` file created and loadable via `networkx.node_link_graph()`
- Tests in `corpus/tests/sync/test_health_checker.py`:
  - Assert: all chunks synced, graph current → `healthy=True`
  - Assert: 50% chunks unsynced → `healthy=False`, `vector_synced_pct=0.5`
- **Verify**: `pytest tests/sync/ -v` — all assertions pass
- **If sync health fails during a run**: Block run completion; report which layer is behind and by how much; operator can run `corpus rebuild-vectors` / `corpus rebuild-graph` to force recovery

### [x] Step: Retrieval Runtime (L0-L3)
<!-- chat-id: 14637af2-8161-4677-8eba-4effc320fbe4 -->

Implement retrieval pipeline per FR-8.

- Create `corpus/src/corpus/retrieval/__init__.py`
- Create `corpus/src/corpus/retrieval/symbolic_filter.py`:
  - `extract_constraints(query: str) -> ConstraintSet`: parse domain/capability tags from query text (e.g., `[domain:security]` syntax); return empty set if no explicit tags
- Create `corpus/src/corpus/retrieval/reranker.py`:
  - `rerank(candidates: list[ScoredChunk], query: str) -> list[ScoredChunk]`
  - Scoring: `0.4 * semantic_score + 0.3 * source_reliability + 0.2 * freshness + 0.1 * task_fit`
- Create `corpus/src/corpus/retrieval/formatter.py`:
  - `format_response(decisions: list[DecisionCard], depth: str) -> str`
  - L0 Snapshot: recommendation + confidence + rationale + use-when/avoid-when
  - L1 Brief: + alternatives + tradeoffs + evidence summary + contradiction flags
  - L2 Evidence Pack: + source-by-source comparison + experimental outcomes
  - L3 Raw Provenance: + full extraction lineage + original snippets + scoring inputs
- Create `corpus/src/corpus/retrieval/orchestrator.py`:
  - `query(question: str, depth_override: str | None = None) -> RetrievalResponse`
  - Pipeline: symbolic_filter → ChromaDB vector search (top 20) → graph expansion (follow edges 1 hop) → rerank → determine depth → format
  - Auto-escalation: default L1; if best confidence < 0.70 → L2; if < 0.50 or `has_unresolved_contradiction` → L3
  - `RetrievalResponse`: `content: str`, `depth: str`, `confidence: float`, `provenance: list[str]`, `escalation_reason: str | None`
- Wire `corpus query "<question>" [--depth L0|L1|L2|L3]` CLI command
- Tests in `corpus/tests/retrieval/test_symbolic_filter.py`:
  - Assert: `"[domain:security] best practices"` → `ConstraintSet(domains=['security'])`
  - Assert: `"how to test"` → empty `ConstraintSet`
- Tests in `corpus/tests/retrieval/test_reranker.py`:
  - Assert: high-reliability recent chunk ranks above low-reliability stale chunk
  - Assert: ranking is deterministic (same input → same output)
- Tests in `corpus/tests/retrieval/test_formatter.py`:
  - Assert: L0 output contains recommendation and confidence but NOT alternatives
  - Assert: L1 output contains alternatives and contradiction flags
  - Assert: L3 output contains provenance refs and scoring inputs
- Tests in `corpus/tests/retrieval/test_orchestrator.py`:
  - Assert: high-confidence decision → L1 response (no escalation)
  - Assert: confidence 0.65 → auto-escalate to L2, `escalation_reason` set
  - Assert: confidence 0.40 → auto-escalate to L3
  - Assert: `has_unresolved_contradiction=True` → auto-escalate to L3 regardless of confidence
  - Assert: explicit `--depth L0` overrides auto-escalation
  - Assert: all responses include non-empty `provenance` list
- **Verify**: `pytest tests/retrieval/ -v` — all assertions pass
- **If vector search returns 0 results**: Return empty response with `confidence=0.0` and message "No matching decisions found"; do not error

### [x] Step: Consolidation Gate and Run Completion
<!-- chat-id: 307066a4-ab3d-4bf3-9fed-9a0e5305731f -->

Implement governance gates per FR-9.

- Create `corpus/src/corpus/consolidation/__init__.py`
- Create `corpus/src/corpus/consolidation/gate_runner.py`:
  - `run_gates(run_id: str) -> GateResult`
  - Gate 1: query 3 capabilities affected by run's artifacts; fail if any previously populated capability now returns empty
  - Gate 2: `human_review_queue` has zero unresolved items for this `run_id`
  - Gate 3: all `research_artifacts` for this run have `is_classified=True` (no orphans)
  - Gate 4: `reference_integrity_reports` for this run show `resolved=True` for all entries
  - Gate 5: `sync_health_checker.check_sync_health().healthy == True`
  - `GateResult`: `passed: bool`, `failures: list[GateFailure]` (gate name + detail)
- Create `corpus/src/corpus/consolidation/run_controller.py`:
  - `complete_run(run_id: str) -> None`: run gates; if pass → `status='completed'`, `completed_at=now()`, append to consolidation log; if fail → `status='failed'`, `remediation_report` populated with failure details
- Create `corpus/src/corpus/consolidation/branch_retirement.py`:
  - `retire_branch(run_id: str, action: str) -> None`: `action='archived'` → `git tag archive/<branch>`; `action='deleted'` → `git branch -D`; record in `consolidation_runs.retirement_action`
  - Refuse to retire if run `status != 'completed'`
- Wire `corpus complete <run-id>` CLI command
- Tests in `corpus/tests/consolidation/test_gate_runner.py`:
  - Assert: all gates pass → `GateResult.passed=True`
  - Assert: unresolved human review item → gate 2 fails, `passed=False`
  - Assert: broken reference → gate 4 fails
  - Assert: unhealthy sync → gate 5 fails
  - Assert: multiple gate failures → all listed in `failures`
- Tests in `corpus/tests/consolidation/test_run_controller.py`:
  - Assert: gates pass → run `status='completed'`, `completed_at` set
  - Assert: gates fail → run `status='failed'`, `remediation_report` non-empty
- Tests in `corpus/tests/consolidation/test_branch_retirement.py`:
  - Assert: completed run → retirement succeeds, `retirement_action` recorded
  - Assert: non-completed run → retirement refused with error
- **Verify**: `pytest tests/consolidation/ -v` — all assertions pass
- **If any gate fails**: Run is blocked at `status='failed'`; remediation report lists each failure with actionable fix; operator must resolve and re-run `corpus complete <run-id>`
- **If human queue non-empty**: Gate 2 blocks; operator uses `corpus review resolve` to clear queue, then re-runs gate

### [x] Step: Smoke Test — Full Pipeline on Test Branch
<!-- chat-id: 6310e312-4c55-4b2b-afcf-ea74a6ab2b52 -->

Integration checkpoint: verify the complete pipeline before adding telemetry.

- Create `corpus/tests/integration/test_full_pipeline_smoke.py`:
  - Set up tmp git repo + DB; seed 3 DecisionCards with capabilities
  - Create branch with 5 artifacts: 2 novel, 2 near-duplicates, 1 contradicting existing decision
  - Run full pipeline: `init` → `ingest` → `dedup` → `update-decisions` → `check-references` → `sync-derived` → `complete`
  - Assert: run `status='completed'` (all gates pass after resolving any human queue items programmatically)
  - Assert: dedup report generated with candidate pair
  - Assert: at least 1 DriftEvent created (contradiction)
  - Assert: vector index has chunks; graph has nodes/edges
  - Assert: `corpus query` returns L1+ response with provenance for a known capability
  - Assert: branch retirement recorded
- **Verify**: `pytest tests/integration/test_full_pipeline_smoke.py -v` passes
- **If verification fails**: Identifies architectural issues before final steps — fix before proceeding
- Run `ruff check src/ tests/` and `mypy src/corpus/` — fix any issues

### [x] Step: Telemetry and Calibration
<!-- chat-id: cf322d29-e9de-43ff-ad7e-ad0f04776367 -->

Implement operational telemetry per FR-10.

- Create `corpus/src/corpus/telemetry/__init__.py`
- Create `corpus/src/corpus/telemetry/collector.py`:
  - `record_outcome(decision_id: str, outcome: str) -> None`: persists `(decision_id, now(), outcome)` to `telemetry_outcomes`
- Create `corpus/src/corpus/telemetry/calibrator.py`:
  - `calibrate() -> CalibrationReport`: for each decision with `usage_count >= 5`, recompute confidence from actual `success_rate = successes / total`; update `DecisionCard.confidence_score` if delta > 0.05
  - `CalibrationReport`: `decisions_evaluated: int`, `decisions_recalibrated: int`, `adjustments: list[(decision_id, old_score, new_score)]`
- Create `corpus/src/corpus/telemetry/metrics.py`:
  - `compute_metrics() -> OperationalMetrics`: L1 resolution rate, L2/L3 escalation rate, contradiction density, dedup compression ratio, sync lag
- Create `corpus/src/corpus/telemetry/compactor.py`:
  - `compact() -> CompactionReport`: find artifacts with `status='superseded'` older than 90 days → set `status='archived'`; remove their chunks from vector index
- Wire CLI: `corpus telemetry record <decision-id> <outcome>`, `corpus telemetry calibrate`, `corpus telemetry metrics`
- Tests in `corpus/tests/telemetry/test_collector.py`:
  - Assert: `record_outcome('dc_001', 'success')` → record in DB with timestamp
  - Assert: 3 outcomes for same decision → `list_outcomes` returns 3
- Tests in `corpus/tests/telemetry/test_calibrator.py`:
  - Assert: decision with 5 outcomes (4 success, 1 failure) → new confidence reflects 80% success rate
  - Assert: decision with 3 outcomes (< 5 threshold) → not recalibrated
  - Assert: decision where delta < 0.05 → not recalibrated (avoids noise)
- Tests in `corpus/tests/telemetry/test_metrics.py`:
  - Assert: metrics returns all expected fields with numeric values
- Tests in `corpus/tests/telemetry/test_compactor.py`:
  - Assert: superseded artifact older than 90 days → `status='archived'` after compaction
  - Assert: active artifact → untouched by compaction
- **Verify**: `pytest tests/telemetry/ -v` — all assertions pass
- **If calibration produces out-of-range scores**: Clamp to [0.0, 1.0]; log warning

### [x] Step: End-to-End Pipeline and Scaled Integration Tests
<!-- chat-id: 26b88db7-1c9c-4810-95f7-cb0e728204b4 -->

Wire full pipeline orchestrator and run comprehensive validation. Per spec Phase 10.

- Wire `corpus run <branch-or-worktree>` as full pipeline orchestrator: ingest → dedup → update-decisions → check-references → sync-derived → complete; if any step fails, halt and report which step failed with details
- Wire `corpus status` to show: current/last run status, human review queue count, sync health summary, latest calibration report timestamp
- Create scaled integration test in `corpus/tests/integration/test_e2e_scaled.py`:
  - Seed fixture with 10 DecisionCards from bootstrap run (data from `docs/research/03_indices/`)
  - Create 3 test branches, each with different artifact profiles
  - Run full pipeline on each branch sequentially
  - Assert: all 3 runs complete with `status='completed'`
  - Assert: `corpus status` shows healthy state after all runs
  - Assert: `corpus query "research benchmarking"` returns response with provenance refs
  - Assert: `corpus telemetry metrics` returns non-zero values after 3 runs
- Run full verification suite:
  - `pytest tests/ -v` — all tests pass
  - `ruff check src/ tests/` — no lint errors
  - `ruff format --check src/ tests/` — formatting correct
  - `mypy src/corpus/` — no type errors
- **Verify**: All of the above pass
- **If any integration test fails**: Fix the specific component; re-run failed test in isolation first; then re-run full suite
