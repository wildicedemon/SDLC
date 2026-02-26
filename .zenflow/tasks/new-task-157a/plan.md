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

1. Review existing codebase to understand current architecture and patterns
2. Analyze the feature definition and identify unclear aspects
3. Ask the user for clarifications on aspects that significantly impact scope or user experience
4. Make reasonable decisions for minor details based on context and conventions
5. If user can't clarify, make a decision, state the assumption, and continue

Save the PRD to `{@artifacts_path}/requirements.md`.

### [x] Step: Technical Specification
<!-- chat-id: 2d819299-e496-4d21-a4dd-99bdbd01cd0c -->

Create a technical specification based on the PRD in `{@artifacts_path}/requirements.md`.

1. Review existing codebase architecture and identify reusable components
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

### [ ] Step: Project Scaffolding and Configuration

Set up the `corpus/` Python package, dependencies, configuration, and CLI skeleton.

- Create `corpus/pyproject.toml` with all dependencies from spec §1.3 (sqlalchemy, alembic, sentence-transformers, datasketch, numpy, chromadb, networkx, click, gitpython, pydantic, pytest, pytest-asyncio, openai, ruff, mypy)
- Create `corpus/src/corpus/__init__.py`
- Create `corpus/src/corpus/config.py` with `CorpusSettings(BaseSettings)` validating all env vars from spec §8.1
- Create `corpus/src/corpus/cli.py` with Click group and placeholder subcommands: `init`, `migrate`, `ingest`, `dedup`, `update-decisions`, `check-references`, `sync-derived`, `complete`, `run`, `review`, `query`, `rebuild-vectors`, `rebuild-graph`, `telemetry`, `status`
- Add `data/` to `.gitignore`
- Create `corpus/tests/conftest.py` with shared fixtures (tmp SQLite DB, tmp data dirs)
- **Verify**: `pip install -e corpus/` succeeds; `corpus --help` prints CLI help; `ruff check src/ tests/` passes; `mypy src/corpus/` passes

### [ ] Step: Relational Schema, Migrations, and Repository Layer

Implement the authoritative relational data layer per spec §3.1.

- Create `corpus/src/corpus/db/engine.py`: SQLite engine factory, connection management, session context manager
- Create `corpus/src/corpus/db/models.py`: SQLAlchemy ORM models for all 10 entities (`consolidation_runs`, `research_artifacts`, `artifact_chunks`, `decision_cards`, `drift_events`, `reference_rewrite_maps`, `reference_integrity_reports`, `human_review_queue`, `capability_mappings`, `telemetry_outcomes`)
- Create `corpus/src/corpus/db/migrations/runner.py`: forward/rollback migration runner using raw SQL versioned files
- Create `corpus/src/corpus/db/migrations/versions/001_initial.sql`: initial schema DDL
- Create `corpus/src/corpus/db/repository.py`: CRUD data-access layer for each entity (create, get_by_id, list, update, delete)
- Wire `corpus init` to create DB + run migrations, `corpus migrate` and `corpus migrate --rollback`
- Write unit tests in `corpus/tests/db/` for: model creation, repository CRUD per entity, migration forward/rollback
- **Verify**: `corpus init` creates DB with all tables; `corpus migrate --rollback` removes them; `pytest tests/db/ -v` passes

### [ ] Step: Ingestion and Normalization Pipeline

Implement raw branch/worktree content ingestion per spec §4.1 and Phase 2.

- Create `corpus/src/corpus/ingestion/enumerator.py`: enumerate changed files from a git branch/worktree via GitPython
- Create `corpus/src/corpus/ingestion/classifier.py`: classify files to domain/capability tags using canonical directory contract from `corpus_organization_standard.md`
- Create `corpus/src/corpus/ingestion/normalizer.py`: normalize content into canonical domain files (merge into existing pages)
- Create `corpus/src/corpus/ingestion/path_mapper.py`: record pre/post path mappings for moves/renames
- Wire `corpus ingest <branch-or-worktree>` CLI: create `consolidation_run`, enumerate, classify, normalize, store `research_artifacts` + `artifact_chunks` in DB
- Reject unclassified/orphan files (FR-2.6)
- Write unit tests in `corpus/tests/ingestion/` for: enumerator (mock git), classifier logic, normalizer, path_mapper
- **Verify**: `corpus ingest <branch>` creates run + artifact + chunk records; no unclassified files; `pytest tests/ingestion/ -v` passes

### [ ] Step: Dedup Pipeline and Human Review Queue

Implement 3-layer dedup per spec §3 Phase 3 and human review queue per FR-4.

- Create `corpus/src/corpus/dedup/minhash.py`: Layer 1 MinHash LSH candidate generation via datasketch; threshold from `CORPUS_DEDUP_L1_THRESHOLD`
- Create `corpus/src/corpus/dedup/embeddings.py`: Layer 2 sentence embedding cosine filtering via sentence-transformers; threshold from `CORPUS_DEDUP_L2_THRESHOLD`
- Create `corpus/src/corpus/dedup/arbitrator.py`: Layer 3 AI arbitration via OpenAI-compatible API for L1/L2 disagreements
- Create `corpus/src/corpus/dedup/pipeline.py`: orchestrate L1 → L2 → L3 → human queue routing; generate dedup report; monitor L3 call rate (flag if > 20% of L1 candidates)
- Wire `corpus dedup <run-id>` CLI command
- Wire `corpus review list` and `corpus review resolve <id> <disposition>` CLI commands for human review queue
- Write unit tests in `corpus/tests/dedup/` for: each layer independently (mock embeddings/API in unit tests), pipeline orchestration, human queue routing, L3 rate monitoring
- **Verify**: `corpus dedup <run-id>` produces dedup report; low-confidence items in human queue; `pytest tests/dedup/ -v` passes

### [ ] Step: DecisionCard and Index Updater

Implement decision surface updates per spec Phase 4 and FR-5.

- Create `corpus/src/corpus/decisions/card_updater.py`: recompute only DecisionCards impacted by current run's artifacts; update confidence scores per formula in `confidence_policy.md`
- Create `corpus/src/corpus/decisions/index_updater.py`: update `decision_index`, `capability_index`, `source_to_decision_map`
- Create `corpus/src/corpus/decisions/drift_detector.py`: emit `DriftEvent` records when confidence drops or contradictions emerge; set `has_unresolved_contradiction` flag
- Wire `corpus update-decisions <run-id>` CLI command
- Write unit tests in `corpus/tests/decisions/` for: card updater (scoped recomputation), confidence scoring, index updates, drift detection
- **Verify**: `corpus update-decisions <run-id>` updates affected cards/indices; DriftEvents emitted for confidence drops; `pytest tests/decisions/ -v` passes

### [ ] Step: Reference Integrity

Implement reference safety per spec Phase 5 and FR-6.

- Create `corpus/src/corpus/references/rewrite_mapper.py`: generate `reference_rewrite_map` from path_mapper output for the run
- Create `corpus/src/corpus/references/rewriter.py`: rewrite all internal markdown links, index references, and run-report citations using the rewrite map
- Create `corpus/src/corpus/references/integrity_validator.py`: validate all internal links resolve; validate all `source_path` entries point to existing content; generate `reference_integrity_report`
- Wire `corpus check-references <run-id>` CLI command
- Write unit tests in `corpus/tests/references/` for: rewrite map generation, link rewriting, integrity validation (positive + broken link negative test)
- **Verify**: `corpus check-references <run-id>` produces report with zero unresolved items on valid state; detects broken links; `pytest tests/references/ -v` passes

### [ ] Step: Derived Layer Sync (Vector + Graph)

Implement derived layers per spec Phase 6, §3.2, §3.3, and FR-7.

- Create `corpus/src/corpus/sync/vector_sync.py`: build incremental embedding index from canonical relational records into ChromaDB (`corpus_chunks` collection); use `all-MiniLM-L6-v2` via sentence-transformers
- Create `corpus/src/corpus/sync/graph_sync.py`: build NetworkX graph with node types (artifact, decision, capability) and edge types (supports, addresses, conflicts_with, contradicts); persist to `data/graph.json`
- Create `corpus/src/corpus/sync/health_checker.py`: sync lag tolerance checks, completeness verification, sync health report
- Wire `corpus sync-derived <run-id>`, `corpus rebuild-vectors`, `corpus rebuild-graph` CLI commands
- Write unit tests in `corpus/tests/sync/` for: vector sync (small test data), graph sync (verify nodes/edges), health checker, rebuild equivalence
- **Verify**: `corpus sync-derived <run-id>` populates vector + graph; rebuilds from scratch produce equivalent results; sync health report generated; `pytest tests/sync/ -v` passes

### [ ] Step: Retrieval Runtime (L0-L3)

Implement retrieval pipeline per spec §4.2 and FR-8.

- Create `corpus/src/corpus/retrieval/symbolic_filter.py`: extract tag/constraint filters from query
- Create `corpus/src/corpus/retrieval/orchestrator.py`: full pipeline — symbolic filter → vector candidate retrieval (ChromaDB) → graph expansion (NetworkX) → policy reranking → depth formatting; attach provenance + confidence metadata
- Create `corpus/src/corpus/retrieval/reranker.py`: policy reranking by trust score, freshness, task fit
- Create `corpus/src/corpus/retrieval/formatter.py`: depth-based response formatting for L0 Snapshot, L1 Brief, L2 Evidence Pack, L3 Raw Provenance
- Implement auto-escalation: L2 when confidence < 0.70; L3 when confidence < 0.50 or `has_unresolved_contradiction=true`; support explicit depth override
- Wire `corpus query "<question>" [--depth L0|L1|L2|L3]` CLI command
- Write tests in `corpus/tests/retrieval/` for: symbolic filter, reranker, formatter (each depth), escalation logic, end-to-end retrieval with seeded data
- **Verify**: `corpus query` returns formatted responses at each depth; auto-escalation triggers correctly; provenance refs present; `pytest tests/retrieval/ -v` passes

### [ ] Step: Consolidation Gate and Run Completion

Implement governance gates per spec Phase 8 and FR-9.

- Create `corpus/src/corpus/consolidation/gate_runner.py`: run 5 validation checks — (1) affected capability query check, (2) human queue fully resolved, (3) all artifacts in canonical dirs, (4) reference integrity passes, (5) derived-layer sync health
- Create `corpus/src/corpus/consolidation/run_controller.py`: mark run complete/fail; append to consolidation_log; produce remediation report on failure
- Create `corpus/src/corpus/consolidation/branch_retirement.py`: archive or delete source branch/worktree; record retirement action
- Wire `corpus complete <run-id>` CLI command
- Write tests in `corpus/tests/consolidation/` for: each gate (positive + negative), run completion flow, failure + remediation report, branch retirement
- **Verify**: `corpus complete <run-id>` passes on valid state; fails and produces remediation on invalid state; `pytest tests/consolidation/ -v` passes

### [ ] Step: Telemetry and Calibration

Implement operational telemetry per spec Phase 9 and FR-10.

- Create `corpus/src/corpus/telemetry/collector.py`: capture `(decision_id, timestamp, outcome)` tuples
- Create `corpus/src/corpus/telemetry/calibrator.py`: recompute confidence calibration when `usage_count >= 5`
- Create `corpus/src/corpus/telemetry/metrics.py`: track operational metrics (L1 resolution rate, L2/L3 escalation rate, contradiction density, dedup compression ratio, time-to-revalidate, sync lag)
- Create `corpus/src/corpus/telemetry/compactor.py`: archive superseded content
- Wire `corpus telemetry record <decision-id> <outcome>`, `corpus telemetry calibrate`, `corpus telemetry metrics` CLI commands
- Write unit tests in `corpus/tests/telemetry/` for: outcome recording, calibration logic, metrics computation, compaction
- **Verify**: CLI commands work; calibration updates confidence scores; `pytest tests/telemetry/ -v` passes

### [ ] Step: End-to-End Pipeline and Integration Tests

Wire full pipeline and validate end-to-end per spec Phase 10.

- Wire `corpus run <branch-or-worktree>` as full pipeline orchestrator: ingest → dedup → update-decisions → check-references → sync-derived → complete
- Wire `corpus status` to show current run status, queue state, sync health
- Create integration test fixtures: seed fixture with 10 DecisionCards from bootstrap run; sample branch fixture with 5 new research artifacts (2 near-duplicates, 1 conflicting, 2 novel); pre-built reference map with intentional broken link
- Write end-to-end integration test: full pipeline on sample branch, verify all gates enforced, verify retrieval returns valid responses post-run
- Run full verification suite: `pytest tests/ -v`, `ruff check src/ tests/`, `ruff format --check src/ tests/`, `mypy src/corpus/`
- **Verify**: Full pipeline completes with all gates enforced; `corpus status` shows healthy state; all tests pass; lint and type checks pass
