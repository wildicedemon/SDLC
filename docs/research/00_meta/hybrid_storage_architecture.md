# Hybrid Storage Architecture

## Purpose
Define the default storage architecture for the research corpus using a hybrid model:
- relational store for canonical integrity and lifecycle state,
- vector index for semantic retrieval,
- graph layer for relationship and contradiction traversal.

## System-of-Record Boundary
- **Relational DB (authoritative):** canonical tables for DecisionCards, ResearchArtifacts metadata, run lifecycle records, reference rewrite maps, and integrity reports.
- **Vector Index (derived):** embeddings for semantic candidate retrieval over canonical and archived evidence views.
- **Graph Layer (derived):** relationship graph for artifact↔decision↔capability↔conflict edges and multi-hop reasoning.

Only the relational layer is source-of-truth for completion gates and audit decisions.

## Responsibilities by Layer
### 1) Relational Layer
- enforce schema and foreign-key constraints
- store lifecycle states (`candidate`, `active`, `superseded`, `archived`)
- enforce run completion gates
- persist provenance and reference-integrity artifacts

### 2) Vector Layer
- support nearest-neighbor semantic retrieval
- return candidate evidence sets for reranking
- maintain separate indexes for active vs archived corpus windows

### 3) Graph Layer
- represent dependencies and contradictions
- support expansion for L2/L3 evidence paths
- support impact analysis when new artifacts arrive

## Synchronization Model
1. Write canonical updates to relational layer.
2. Emit change events for updated entities.
3. Rebuild/refresh affected vector and graph entries incrementally.
4. Run integrity checks; block completion if derived-layer lag exceeds tolerance.

## Operational Guardrails
- derived layers must be rebuildable from relational source-of-truth.
- retrieval can use vector/graph, but final completion and governance checks read relational records.
- stale derived entries must not override canonical relational state.

## Minimal Entity Map
- `decision_cards` (canonical)
- `research_artifacts` (canonical metadata + references)
- `artifact_content_chunks` (canonical chunk pointers)
- `consolidation_runs` (canonical)
- `drift_events` (canonical)
- `reference_integrity_reports` (canonical)
- `vector_embeddings` (derived)
- `graph_edges` (derived)

## Adoption Notes
- Start with relational + vector.
- Add graph layer when contradiction/relationship reasoning load increases.
- Keep retrieval API stable so backend layers can evolve independently.

# Hybrid Storage Architecture

## Purpose
Define the default storage architecture for the research corpus using a hybrid model:
- relational store for canonical integrity and lifecycle state,
- vector index for semantic retrieval,
- graph layer for relationship and contradiction traversal.

## System-of-Record Boundary
- **Relational DB (authoritative):** canonical tables for DecisionCards, ResearchArtifacts metadata, run lifecycle records, reference rewrite maps, and integrity reports.
- **Vector Index (derived):** embeddings for semantic candidate retrieval over canonical and archived evidence views.
- **Graph Layer (derived):** relationship graph for artifact↔decision↔capability↔conflict edges and multi-hop reasoning.

Only the relational layer is source-of-truth for completion gates and audit decisions.

## Responsibilities by Layer
### 1) Relational Layer
- enforce schema and foreign-key constraints
- store lifecycle states (`candidate`, `active`, `superseded`, `archived`)
- enforce run completion gates
- persist provenance and reference-integrity artifacts

### 2) Vector Layer
- support nearest-neighbor semantic retrieval
- return candidate evidence sets for reranking
- maintain separate indexes for active vs archived corpus windows

### 3) Graph Layer
- represent dependencies and contradictions
- support expansion for L2/L3 evidence paths
- support impact analysis when new artifacts arrive

## Synchronization Model
1. Write canonical updates to relational layer.
2. Emit change events for updated entities.
3. Rebuild/refresh affected vector and graph entries incrementally.
4. Run integrity checks; block completion if derived-layer lag exceeds tolerance.

## Operational Guardrails
- derived layers must be rebuildable from relational source-of-truth.
- retrieval can use vector/graph, but final completion and governance checks read relational records.
- stale derived entries must not override canonical relational state.

## Minimal Entity Map
- `decision_cards` (canonical)
- `research_artifacts` (canonical metadata + references)
- `artifact_content_chunks` (canonical chunk pointers)
- `consolidation_runs` (canonical)
- `drift_events` (canonical)
- `reference_integrity_reports` (canonical)
- `vector_embeddings` (derived)
- `graph_edges` (derived)

## Adoption Notes
- Start with relational + vector.
- Add graph layer when contradiction/relationship reasoning load increases.
- Keep retrieval API stable so backend layers can evolve independently.
