# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.

# Implementation Execution Plan: Functional Hybrid Corpus System

## Purpose
Define the full execution order to move from documentation/policy state to a functional hybrid corpus platform (relational + vector + graph) that continuously ingests, organizes, deduplicates, validates, and serves DecisionCard-based retrieval.

## Intended Outcome
At completion, the system can:
1. ingest new research from ephemeral branches/worktrees,
2. normalize/organize corpus content into canonical structure,
3. deduplicate via 3-layer pipeline,
4. maintain reference integrity,
5. update DecisionCards and indices,
6. sync relational/vector/graph layers,
7. pass lifecycle gates,
8. publish retrieval-ready outputs (L0-L3),
9. retire source branch/worktree safely.

---

## Non-Goals
- Building production UI.
- Rewriting entire research corpus in one pass before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.

---

## Canonical Constraints (Must Hold)
- Relational layer is authoritative system-of-record.
- Vector and graph layers are derived and rebuildable.
- Run completion is blocked on validation gates and reference-integrity checks.
- New artifacts must conform to canonical corpus organization rules.

---

## Required Inputs
1. Existing policy docs under `docs/research/00_meta/`.
2. Current indices under `docs/research/03_indices/`.
3. Access to repository branches/worktrees for ingestion.
4. Database/runtime environment for:
   - relational engine,
   - vector indexing,
   - graph storage/query.

---

## Deliverables
1. Operational data model implementation (tables/collections/edge schemas).
2. Ingestion + normalization pipeline.
3. Dedup pipeline (Layer 1/2/3 + human queue routing).
4. Reference rewrite and integrity validator.
5. Decision/Index updater.
6. Derived-layer sync orchestrator (relational → vector/graph).
7. Run-gate validator and completion controller.
8. Retrieval API/service implementing L0-L3 depth behavior.
9. Telemetry + calibration jobs.
10. Runbooks and failure recovery playbooks.

---

## Phase Plan (Execution Order)

## Phase 0 — Environment and Baseline Lock
### Goals
- Freeze baseline policies and initial index schema.
- Ensure deterministic run IDs and naming conventions are enforced.

### Steps
1. Snapshot current `00_meta` and `03_indices` as baseline.
2. Define runtime configuration contract (env vars, secrets, endpoints).
3. Define migration/versioning strategy for schemas.

### Exit Criteria
- Baseline version tag created.
- Schema migration mechanism selected and tested.

---

## Phase 1 — Canonical Data Layer (Relational)
### Goals
- Implement authoritative persistence for corpus state and governance records.

### High-Level Schema
- `decision_cards`
- `research_artifacts`
- `artifact_chunks`
- `consolidation_runs`
- `drift_events`
- `reference_rewrite_maps`
- `reference_integrity_reports`
- `human_review_queue`
- `capability_mappings`

### Steps
1. Create relational schema + constraints (PK/FK/uniqueness/state enums).
2. Implement write/read repository layer.
3. Add migration tests and rollback validation.

### Exit Criteria
- Canonical entities persist with constraints enforced.
- Rollback tested for at least one migration.

---

## Phase 2 — Ingestion and Normalization
### Goals
- Convert raw branch/worktree inputs into canonical artifact records and organized corpus updates.

### Steps
1. Enumerate changed files from source branch/worktree.
2. Classify to domain/capability tags.
3. Normalize content into canonical domain files.
4. Record pre/post path mapping for renamed/moved files.
5. Store artifact metadata and content chunks.

### Exit Criteria
- All new artifacts mapped to canonical domains.
- No unclassified/orphan files remain.

---

## Phase 3 — Dedup and Arbitration Pipeline
### Goals
- Remove redundancy while preserving meaningful alternatives.

### Steps
1. Layer 1: MinHash LSH candidate generation.
2. Layer 2: Embedding cosine filtering.
3. Layer 3: AI arbitration for Layer-1/2 disagreements.
4. Route low-confidence arbitration (`<0.70`) to human queue.
5. Enforce monitoring threshold (Layer 3 calls <= 20% Layer 1 candidates) or trigger tuning.

### Exit Criteria
- Dedup report generated.
- Arbitration and human queue disposition recorded.

---

## Phase 4 — DecisionCard and Index Update
### Goals
- Update decision surface and traceability maps.

### Steps
1. Recompute impacted DecisionCards only.
2. Update decision confidence + contradiction visibility.
3. Update `decision_index`, `capability_index`, `source_to_decision_map`.
4. Write drift events where contradictions or confidence drops occur.

### Exit Criteria
- Indexes and DecisionCards synchronized to latest run.
- All affected capabilities queryable.

---

## Phase 5 — Reference Integrity and Reorganization Safety
### Goals
- Ensure no references break after normalization/restructuring.

### Steps
1. Generate `reference_rewrite_map_<run_id>.md`.
2. Rewrite all known references.
3. Execute internal link validation.
4. Validate source/index references resolve.
5. Generate `reference_integrity_report_<run_id>.md`.

### Exit Criteria
- Zero unresolved broken links.
- Zero stale source/index paths.

---

## Phase 6 — Derived Layers (Vector + Graph)
### Goals
- Enable high-quality semantic retrieval and relationship traversal while preserving relational authority.

### Steps
1. Build incremental embedding index from canonical records.
2. Build graph edges (artifact↔decision↔capability↔conflict).
3. Run sync health checks and lag thresholds.
4. Block completion if sync health fails tolerance.

### Exit Criteria
- Derived layers reflect current canonical run state.
- Sync health report recorded.

---

## Phase 7 — Retrieval Runtime (L0-L3)
### Goals
- Serve decision-first responses with progressive depth and escalation.

### Steps
1. Implement retrieval flow:
   - symbolic constraints,
   - vector candidate retrieval,
   - graph expansion,
   - policy reranking,
   - depth formatting.
2. Implement escalation triggers (confidence, contradictions, score margins).
3. Add trace payload with provenance references.

### Exit Criteria
- Retrieval test suite passes for L0-L3 pathways.
- Responses include provenance and confidence metadata.

---

## Phase 8 — Consolidation Gate and Run Completion
### Goals
- Enforce governance rules before run marked completed.

### Steps
1. Run validation gates:
   - affected capability query checks,
   - human queue resolved,
   - organization checks,
   - reference integrity checks,
   - derived-layer sync health checks.
2. If pass, mark run complete and append to `consolidation_log`.
3. Archive/delete source branch/worktree and record retirement.

### Exit Criteria
- Run status = completed.
- Retirement action recorded.

---

## Phase 9 — Telemetry, Calibration, and Continuous Operations
### Goals
- Keep system quality stable as corpus grows.

### Steps
1. Capture telemetry tuple: `(decision_id, timestamp, outcome)`.
2. Recompute success rates and confidence calibration.
3. Track operational metrics:
   - L1 resolution rate,
   - L2/L3 escalation rate,
   - contradiction density,
   - dedup compression ratio,
   - time-to-revalidate,
   - sync lag.
4. Run periodic compaction/archive workflows for superseded content.

### Exit Criteria
- Calibration job scheduled and producing reports.
- Growth controls active and monitored.

---

## Implementation Requirements Checklist
- [ ] Relational schema and migrations
- [ ] Ingestion classifier + normalizer
- [ ] 3-layer dedup pipeline
- [ ] Human review queue integration
- [ ] Decision/index update service
- [ ] Reference rewrite + integrity validator
- [ ] Vector indexer + query service
- [ ] Graph builder + traversal service
- [ ] Retrieval orchestrator (L0-L3)
- [ ] Consolidation gate runner
- [ ] Telemetry/calibration jobs
- [ ] Runbooks + recovery docs

---

## Risks and Mitigations
1. **Reference breakage during reorganization**
   - Mitigation: rewrite map + blocking integrity gate.
2. **Derived layer drift from canonical state**
   - Mitigation: sync health thresholds + completion block.
3. **Dedup false merges**
   - Mitigation: disagreement arbitration + human queue.
4. **Corpus growth outpacing utility**
   - Mitigation: archive/supersede lifecycle and growth metrics.
5. **Confidence miscalibration**
   - Mitigation: telemetry-driven recalibration schedule.

---

## AI Agent Execution Notes
- Treat this plan as an ordered state machine; do not skip phases.
- Prefer incremental domain rollout (start with one high-signal domain, then expand).
- If any blocking gate fails, halt completion and produce remediation report.
- Never mark completion if references, indices, or derived-layer sync are stale.

---

## Definition of Fully Functional
System is considered fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and reported.
