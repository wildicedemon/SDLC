# Product Requirements Document: Functional Hybrid Corpus System

## 1. Overview

### 1.1 Problem Statement
The SDLC research corpus exists as a set of policy documents, organizational standards, and bootstrapped indices. No runtime infrastructure exists to ingest, deduplicate, validate, or serve research content programmatically. All operations are manual and cannot scale.

### 1.2 Product Summary
Build a functional hybrid corpus platform (relational + vector + graph) that continuously ingests research from ephemeral branches/worktrees, normalizes content into canonical structure, deduplicates via a 3-layer pipeline, maintains reference integrity, and serves DecisionCard-based retrieval at four depth levels (L0-L3).

### 1.3 Target Users
- AI agents consuming decision-first retrieval for SDLC tasks
- Human reviewers resolving dedup conflicts and low-confidence arbitration
- System operators monitoring corpus health and calibration

---

## 2. Current State

### 2.1 What Exists
- **Policy documents** (`docs/research/00_meta/`): knowledge architecture contract, hybrid storage architecture, corpus organization standard, reference integrity policy, update lifecycle, confidence policy, skill workflow design guide, practical implications assessment.
- **Bootstrapped indices** (`docs/research/03_indices/`): 10 DecisionCards from `research_benchmarking_framework` domain, 6 capabilities mapped, 1 completed consolidation run (`cr_bootstrap_2026_02_26`).
- **12 domain directories** (`01_*` through `12_*`) with `overview.md`, `patterns.md`, `comparisons.md`, `references.md` per subdomain.
- **Python scripts** (`scripts/`) for batch Perplexity API research prompt execution.
- **No package manager, application framework, or runtime code.**

### 2.2 What Does Not Exist
- Relational database schema or persistence layer.
- Vector index or embedding pipeline.
- Graph storage or traversal layer.
- Ingestion, normalization, or dedup pipelines.
- Reference integrity automation.
- Retrieval API/service.
- Telemetry or calibration infrastructure.

---

## 3. Functional Requirements

### FR-1: Relational Data Layer (Authoritative)
- **FR-1.1**: Implement schema for: `decision_cards`, `research_artifacts`, `artifact_chunks`, `consolidation_runs`, `drift_events`, `reference_rewrite_maps`, `reference_integrity_reports`, `human_review_queue`, `capability_mappings`.
- **FR-1.2**: Enforce PK/FK constraints, uniqueness, and lifecycle state enums (`candidate`, `active`, `superseded`, `archived`).
- **FR-1.3**: Provide a repository/data-access layer for CRUD operations on all canonical entities.
- **FR-1.4**: Support schema migrations with rollback capability.

### FR-2: Ingestion and Normalization Pipeline
- **FR-2.1**: Enumerate changed files from a source branch or worktree.
- **FR-2.2**: Classify artifacts to domain/capability tags using the canonical directory contract.
- **FR-2.3**: Normalize content into canonical domain files (merge into existing pages, not parallel duplicates).
- **FR-2.4**: Record pre/post path mappings for all moved/renamed files.
- **FR-2.5**: Store artifact metadata and content chunks in the relational layer.
- **FR-2.6**: Reject unclassified/orphan files — all must be resolved before run completion.

### FR-3: Three-Layer Deduplication Pipeline
- **FR-3.1**: Layer 1 — Generate near-duplicate candidate pairs using MinHash signatures with LSH buckets.
- **FR-3.2**: Layer 2 — Score Layer-1 pairs using sentence embedding cosine similarity.
- **FR-3.3**: Layer 3 — Invoke AI arbitration only when Layer 1 and Layer 2 disagree.
- **FR-3.4**: Route arbitration outputs with confidence < 0.70 to the human review queue.
- **FR-3.5**: Generate a dedup report per run with candidate counts, merge actions, and arbitration stats.
- **FR-3.6**: Monitor Layer-3 call rate; if > 20% of Layer-1 candidates, flag for threshold tuning.

### FR-4: Human Review Queue
- **FR-4.1**: Accept items routed from dedup arbitration (confidence < 0.70).
- **FR-4.2**: Track disposition (approved merge, rejected merge, deferred).
- **FR-4.3**: Block run completion until all queued items are resolved.

### FR-5: DecisionCard and Index Updates
- **FR-5.1**: Recompute only DecisionCards impacted by current run's artifacts.
- **FR-5.2**: Update confidence scores using the defined formula (source diversity, recency, downstream success, contradiction penalty).
- **FR-5.3**: Update `decision_index`, `capability_index`, `source_to_decision_map`.
- **FR-5.4**: Emit `DriftEvent` records when confidence drops or contradictions emerge.
- **FR-5.5**: Surface contradictions visibly (`has_unresolved_contradiction` flag), never bury them.

### FR-6: Reference Integrity and Reorganization Safety
- **FR-6.1**: Generate `reference_rewrite_map_<run_id>.md` for every file move/rename.
- **FR-6.2**: Rewrite all internal markdown links, index references, and run-report citations using the rewrite map.
- **FR-6.3**: Validate all internal links resolve post-rewrite.
- **FR-6.4**: Validate all `source_path` entries in `source_to_decision_map` point to existing content.
- **FR-6.5**: Generate `reference_integrity_report_<run_id>.md`.
- **FR-6.6**: Block run completion if any unresolved broken link or stale path remains.

### FR-7: Derived Layer Sync (Vector + Graph)
- **FR-7.1**: Build incremental embedding index from canonical relational records.
- **FR-7.2**: Build graph edges: artifact-to-decision, decision-to-capability, artifact-to-conflict.
- **FR-7.3**: Emit change events from relational writes to trigger derived-layer refresh.
- **FR-7.4**: Run sync health checks; block run completion if lag exceeds tolerance.
- **FR-7.5**: Derived layers must be fully rebuildable from relational source-of-truth.

### FR-8: Retrieval Runtime (L0-L3)
- **FR-8.1**: Implement retrieval pipeline: symbolic filter -> vector candidate retrieval -> graph expansion -> policy reranking -> depth formatting.
- **FR-8.2**: Return L1 Brief by default.
- **FR-8.3**: Auto-escalate to L2 when confidence < 0.70.
- **FR-8.4**: Auto-escalate to L3 when confidence < 0.50 or `has_unresolved_contradiction=true`.
- **FR-8.5**: Include provenance references and confidence metadata in all responses.
- **FR-8.6**: Support explicit depth override by caller.

#### Response Formats
- **L0 Snapshot**: One recommendation, confidence score, short rationale, use-when/avoid-when.
- **L1 Brief**: Recommendation + alternatives, tradeoffs, constraints, evidence summary, contradiction flags.
- **L2 Evidence Pack**: Source-by-source comparison, experimental outcomes, merge rationale, conflict notes.
- **L3 Raw Provenance**: Full extraction lineage, original snippets, scoring inputs.

### FR-9: Consolidation Gate and Run Completion
- **FR-9.1**: Run validation gates before marking any run as `completed`:
  - Query 3 capabilities affected by new artifacts; block if any previously populated capability returns empty.
  - Human review queue fully resolved.
  - All artifacts placed in canonical directories (no orphans).
  - Reference integrity passes (zero broken links, zero stale paths).
  - Derived-layer sync health within tolerance.
- **FR-9.2**: On pass, mark run complete and append to `consolidation_log`.
- **FR-9.3**: Archive or delete source branch/worktree and record retirement action.
- **FR-9.4**: On failure, block completion and produce remediation report.

### FR-10: Telemetry and Calibration
- **FR-10.1**: Capture telemetry tuples: `(decision_id, timestamp, outcome: success|failure)`.
- **FR-10.2**: Recompute confidence calibration when `usage_count >= 5`.
- **FR-10.3**: Track operational metrics: L1 resolution rate, L2/L3 escalation rate, contradiction density, dedup compression ratio, time-to-revalidate, sync lag.
- **FR-10.4**: Run periodic compaction/archive for superseded content.

---

## 4. Non-Functional Requirements

### NFR-1: Authority Model
- Relational layer is the sole system-of-record for governance and completion decisions.
- Vector and graph layers are derived, never authoritative.

### NFR-2: Data Integrity
- All entities use deterministic IDs: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`, `cr_<purpose>_<YYYY_MM_DD>`.
- Provenance metadata preserved even after branch deletion (source branch, commit hash, path, timestamp, run ID).

### NFR-3: Idempotency
- Rerunning a consolidation run with the same inputs produces the same canonical state.
- Derived-layer rebuilds from relational data produce equivalent results.

### NFR-4: Incremental Processing
- Only impacted DecisionCards are recomputed per run.
- Only changed artifacts trigger embedding/graph updates.

### NFR-5: Observability
- Every run produces: consolidation summary, decision impact report, drift event report, dedup report, reference integrity report, sync health report, human review disposition report.

### NFR-6: Recoverability
- Schema migrations are reversible (rollback tested).
- Derived layers are rebuildable from relational source-of-truth.
- Failed runs are marked as failed with remediation guidance, never left in ambiguous state.

---

## 5. Canonical Constraints (Hard Rules)

1. Relational layer is authoritative system-of-record.
2. Vector and graph layers are derived and rebuildable.
3. Run completion is blocked on validation gates and reference-integrity checks.
4. New artifacts must conform to canonical corpus organization rules.
5. Unresolved contradictions must remain queryable; they cannot be hidden.
6. All recommendations must include at least one provenance reference.
7. Reusing previously retired branches/worktrees is prohibited.
8. DecisionCards are canonical and versioned; BacklogSeeds are disposable derivatives.

---

## 6. Non-Goals

- Building a production UI.
- Rewriting the entire research corpus before infrastructure exists.
- Allowing derived layers (vector/graph) to become governance authority.
- Migrating away from the existing `docs/research/` directory structure for policy/index content.

---

## 7. Data Model Summary

### Canonical Entities (Relational)
| Entity | Purpose |
|---|---|
| `decision_cards` | Canonical recommendation objects |
| `research_artifacts` | Extracted content units with provenance |
| `artifact_chunks` | Content chunks for granular retrieval |
| `consolidation_runs` | Run lifecycle and metadata |
| `drift_events` | Confidence/contradiction change records |
| `reference_rewrite_maps` | Path rewrite mappings per run |
| `reference_integrity_reports` | Link/index validation results per run |
| `human_review_queue` | Dedup arbitration items requiring human disposition |
| `capability_mappings` | Capability-to-decision-to-domain relationships |

### Derived Entities
| Entity | Layer | Purpose |
|---|---|---|
| `vector_embeddings` | Vector | Semantic candidate retrieval |
| `graph_edges` | Graph | Relationship/contradiction traversal |

### Key JSON Schemas (from Knowledge Architecture Contract)
- `ResearchArtifact`: `artifact_id`, `title`, `content`, `domain_tags`, `capability_tags`, `source` (branch, worktree, run_id, path, commit, timestamp), `quality_signals`.
- `DecisionCard`: `decision_id`, `question`, `context` (capability, constraints), `recommendation`, `alternatives`, `confidence` (score, level, explanation), `provenance_refs`, `last_validated_at`, `revisit_triggers`.
- `DriftEvent`: `event_id`, `decision_id`, `trigger`, `impact` (confidence_delta, affected_sections), `status`, `created_at`.

---

## 8. System Boundaries and Integrations

### Inputs
- Git branches/worktrees containing raw research content.
- Existing `docs/research/` corpus and indices.
- Perplexity API responses (via existing `scripts/` tooling).

### Outputs
- Updated relational records (decisions, artifacts, runs, drift events).
- Updated `docs/research/03_indices/` files.
- Updated `docs/research/00_meta/` run reports and logs.
- Retrieval API responses (L0-L3 depth).
- Telemetry and calibration reports.

### External Dependencies
- Relational database engine (to be selected).
- Embedding model / vector index engine (to be selected).
- Graph database or in-process graph library (to be selected).
- AI model for Layer-3 dedup arbitration and confidence scoring.

---

## 9. Phased Delivery

The system is delivered in 10 phases as defined in the implementation execution plan. Each phase has blocking exit criteria; phases must execute in order.

| Phase | Scope | Key Gate |
|---|---|---|
| 0 | Environment + baseline lock | Baseline tag created, migration mechanism tested |
| 1 | Relational data layer | Entities persist with constraints, rollback tested |
| 2 | Ingestion + normalization | All artifacts mapped, no orphans |
| 3 | Dedup pipeline | Dedup report generated, arbitration recorded |
| 4 | DecisionCard + index update | Indices synced, affected capabilities queryable |
| 5 | Reference integrity | Zero broken links, zero stale paths |
| 6 | Derived layers (vector + graph) | Sync health within tolerance |
| 7 | Retrieval runtime (L0-L3) | Test suite passes, provenance in responses |
| 8 | Consolidation gate + run completion | Run completes with all gates enforced |
| 9 | Telemetry + calibration | Calibration jobs running, growth controls active |

---

## 10. Acceptance Criteria (Definition of Done)

The system is fully functional when:
1. End-to-end consolidation runs complete automatically with all gates enforced.
2. Retrieval returns decision-first responses with valid provenance at L0-L3.
3. Reorganization operations do not leave broken references.
4. Derived layers remain within sync tolerance of relational source-of-truth.
5. Continuous telemetry and calibration loops are running and producing reports.

---

## 11. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Reference breakage during reorganization | Broken retrieval, stale data | Rewrite map + blocking integrity gate |
| Derived layer drift | Stale retrieval results | Sync health thresholds + completion block |
| Dedup false merges | Lost research content | Disagreement arbitration + human queue |
| Corpus growth outpacing utility | Degraded retrieval precision | Archive/supersede lifecycle + growth metrics |
| Confidence miscalibration | Misleading recommendations | Telemetry-driven recalibration schedule |

---

## 12. Open Decisions (To Resolve in Tech Spec)

1. **Relational engine choice**: SQLite (local-first), PostgreSQL (production-grade), or other.
2. **Vector index engine**: FAISS, ChromaDB, Qdrant, pgvector, or other.
3. **Graph layer**: NetworkX (in-process), Neo4j, or graph extension on chosen DB.
4. **AI model for Layer-3 arbitration**: Which model/API for dedup conflict resolution.
5. **Language/framework**: Python (aligns with existing scripts) vs. other.
6. **API surface**: REST, CLI, or library-based retrieval interface.
7. **Deployment model**: Local-first development vs. server deployment.
8. **Escalation thresholds**: Final values for confidence, contradiction density, score margins.
9. **Standard tag vocabulary**: Formal taxonomy for domain/capability tags.
10. **Archival strategy**: `archive/*` branch vs. external artifact store.
