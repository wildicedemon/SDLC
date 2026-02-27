# Knowledge Architecture Contract (Draft)

## Purpose
Define a machine-operable structure for consolidating SDLC research so AI agents can retrieve high-value decisions quickly, escalate depth when needed, and continuously update recommendations as new research arrives.

## Design Goals
1. **Decision-first retrieval:** Answers should return recommended paths, not raw document dumps.
2. **Progressive depth:** Default concise output with optional escalation into deeper evidence tiers.
3. **Provenance + confidence:** Every claim and recommendation is traceable and scored.
4. **Continuous evolution:** New research updates existing decisions incrementally.
5. **AI-native operation:** Retrieval and reranking are designed for agent consumers without requiring UI workflows.
6. **Single-source repository posture:** `main`/`master` is the authoritative knowledge branch; auxiliary branches/worktrees are temporary ingestion vehicles only.

## Branch and Worktree Consolidation Policy
Use short-lived research branches/worktrees, then fully absorb and retire them.

### Policy Statements
- Maintain one authoritative knowledge corpus on `main`/`master`.
- Treat research branches/worktrees as **ephemeral staging environments**.
- Before merge, all candidate research must be:
  1. extracted,
  2. deduplicated semantically,
  3. mapped to domains/capabilities,
  4. provenance-linked,
  5. confidence-scored,
  6. reranked against current recommendations.
- After successful consolidation, the source branch/worktree must be archived or deleted and not reused.

### Merge Validation (Required)
Every research merge into `main`/`master` must pass one blocking validation:
- Query 3 capabilities affected by new artifacts.
- If any previously populated capability returns empty results, block completion.
- New capabilities with no prior DecisionCards are exempt.

Additionally, the human review queue must be fully resolved before consolidation status can be set to `completed`.

### Three-Layer Deduplication Method (Required)
Deduplication is executed as a staged pipeline:

1. **Layer 1 — Lexical candidate generation (MinHash LSH)**
   - Build near-duplicate candidate pairs using MinHash signatures + LSH buckets.
2. **Layer 2 — Semantic similarity filtering (Embeddings)**
   - Score Layer-1 pairs using sentence embedding cosine similarity.
3. **Layer 3 — AI arbitration (disagreements only)**
   - Invoke AI arbitration only when Layer 1 and Layer 2 disagree.
4. **Human review queue**
   - Route arbitration outputs to human review when AI confidence `< 0.70`.

Monitoring requirement:
- If Layer-3 arbitration calls exceed **20%** of Layer-1 candidates in a run, tune dedup thresholds before the next run.

### Provenance Retention After Branch Deletion
Branch deletion is allowed only if provenance remains recoverable in canonical metadata:
- source branch/worktree id
- source commit hash
- source path
- extraction timestamp
- consolidation run id

This preserves lineage while avoiding long-term branch/worktree sprawl.


## Corpus Organization and Normalization Policy
To prevent organizational drift and uncontrolled corpus growth:
- All research artifacts must be normalized into canonical domain files before run completion.
- Parallel duplicate topic files are not allowed in active corpus; merge into a single canonical section.
- Every run must update domain organization status in `domain_coverage_matrix.md`.
- Unclassified artifacts must be resolved (classified, merged, or archived) before `completed` status.

Refer to `docs/research/00_meta/corpus_organization_standard.md` for directory contract, naming rules, and organization gates.
Reference updates after reorganization are mandatory and governed by `docs/research/00_meta/reference_integrity_policy.md`.


## Storage and Retrieval Backend Policy (Hybrid Default)
Use a hybrid backend architecture by default:
- **Relational layer (authoritative):** canonical state, provenance, lifecycle gates, integrity reports.
- **Vector layer (derived):** semantic candidate retrieval for L1/L2.
- **Graph layer (derived):** relationship expansion, contradiction traversal, and impact analysis.

Governance and completion decisions must be made from relational source-of-truth records. Vector/graph layers are optimization and reasoning layers, not policy authority.

See `docs/research/00_meta/hybrid_storage_architecture.md` for details.

## Retrieval Hierarchy (L0-L3)
Use a strict escalation model to balance speed and rigor.

- **L0 Snapshot**
  - One recommended option
  - Confidence score + rationale (short)
  - "Use when" / "Do not use when"
- **L1 Brief (Default)**
  - Recommendation + top alternatives
  - Tradeoffs and key constraints
  - Evidence summary and contradiction flags
- **L2 Evidence Pack**
  - Source-by-source comparison
  - Experimental outcomes / failure cases
  - Merge rationale and conflict resolution notes
- **L3 Raw Provenance**
  - Extract lineage (branch/worktree/path/chunk)
  - Original snippets and extraction metadata
  - Full scoring inputs

### Escalation Rules
Escalate retrieval depth automatically when one or more conditions are met:
- Confidence below threshold
- Two or more viable alternatives within a small score margin
- Contradiction density above threshold
- User/agent requests deeper auditability

## Canonical Data Objects

### 1) `ResearchArtifact`
Raw extracted content unit.

```json
{
  "artifact_id": "ra_<uuid>",
  "title": "string",
  "content": "string",
  "domain_tags": ["prompting", "orchestration"],
  "capability_tags": ["repo_traversal"],
  "source": {
    "branch": "string",
    "worktree": "string",
    "consolidation_run_id": "cr_<uuid>",
    "ingested_into_ref": "main",
    "path": "string",
    "commit": "string",
    "captured_at": "ISO-8601"
  },
  "quality_signals": {
    "evidence_type": "theory|experiment|benchmark|postmortem",
    "source_reliability": 0.0,
    "freshness_days": 0
  }
}
```

### 2) `DecisionCard`
Canonical recommendation object for build-time use.

```json
{
  "decision_id": "dc_<uuid>",
  "question": "What should be used for X under Y constraints?",
  "context": {
    "capability": "repo_traversal",
    "constraints": {
      "latency_ms": 2000,
      "cost_tier": "medium",
      "repo_scale": "large"
    }
  },
  "recommendation": {
    "option_id": "opt_primary",
    "summary": "Use hybrid retrieval with policy reranking",
    "use_when": ["multi-source research", "high ambiguity"],
    "avoid_when": ["single small corpus"]
  },
  "alternatives": [
    {
      "option_id": "opt_vector_only",
      "status": "viable",
      "tradeoffs": ["simpler", "weaker relation reasoning"]
    }
  ],
  "confidence": {
    "score": 0.82,
    "level": "high",
    "explanation": "Diverse corroborating sources; low unresolved conflict"
  },
  "provenance_refs": ["ra_1", "ra_9", "ra_27"],
  "last_validated_at": "ISO-8601",
  "revisit_triggers": ["new contradictory benchmark", "major model release"]
}
```

### 3) `BacklogSeed`
Execution starter generated from Decision Cards (non-canonical).

```json
{
  "seed_id": "bs_<uuid>",
  "decision_id": "dc_<uuid>",
  "epics": [
    {
      "title": "Implement policy reranking pipeline",
      "tasks": [
        "Add metadata filter stage",
        "Add vector retrieval stage",
        "Add graph expansion stage",
        "Add final scoring and thresholding"
      ],
      "acceptance_criteria": [
        "Returns L1 brief in <2s p95",
        "Escalates to L2 when confidence < threshold"
      ]
    }
  ],
  "regeneration_policy": "regenerate_on_decision_change"
}
```

### 4) `DriftEvent`
Records when new evidence may invalidate existing decisions.

```json
{
  "event_id": "de_<uuid>",
  "decision_id": "dc_<uuid>",
  "trigger": "new_conflicting_artifact",
  "impact": {
    "confidence_delta": -0.18,
    "affected_sections": ["recommendation", "alternatives"]
  },
  "status": "pending_revalidation",
  "created_at": "ISO-8601"
}
```

## Confidence Model
Score each recommendation with weighted components:
- evidence strength
- source diversity
- recency
- contradiction penalty
- downstream success feedback

Example:

```text
confidence = 0.30*evidence_strength
           + 0.20*source_diversity
           + 0.20*recency
           + 0.20*downstream_success
           - 0.10*contradiction_penalty
```

Confidence bands:
- **High:** `>= 0.75`
- **Medium:** `0.50 - 0.74`
- **Low:** `< 0.50`

## Retrieval and Reranking Architecture
Use hybrid retrieval to support agent reasoning:
1. **Symbolic filter** (hard constraints, tags, confidence floors)
2. **Vector retrieval** (semantic similarity)
3. **Graph expansion** (related entities, dependencies, contradictory nodes)
4. **Policy reranking** (task fit + trust + freshness)
5. **Depth formatting** (L0-L3 response according to uncertainty)

## Update Lifecycle (Continuous Research Ingestion)
1. Create ephemeral research branch/worktree.
2. Ingest new artifacts with provenance and `consolidation_run_id`.
3. Semantic dedup against existing canonical artifacts.
4. Recompute affected Decision Cards only (incremental scope).
5. Emit DriftEvents when confidence drops or contradictions rise.
6. Revalidate Decision Cards and regenerate dependent BacklogSeeds.
7. Update indices/maps and publish a new versioned snapshot on `main`/`master`.
8. Archive or delete source branch/worktree and record retirement in consolidation log.

## Governance Rules
- Decision Cards are canonical and versioned.
- Backlog Seeds are disposable derivatives and should be regenerated.
- Unresolved contradictions cannot be hidden; they must remain queryable.
- All recommendations must include at least one provenance reference.
- Branch/worktree count should be minimized: only active in-flight research branches are allowed.
- Reusing previously retired research branches/worktrees is prohibited.

## Minimal File Layout

```text
docs/research/00_meta/
  knowledge_architecture_contract.md
  confidence_policy.md
  update_lifecycle.md
  consolidation_log.md
  unresolved_conflicts.md

docs/research/03_indices/
  decision_index.md
  capability_index.md
  source_to_decision_map.md
```

## Operational Defaults
- Default answer depth: **L1 Brief**
- Auto-escalation: enabled
- Trust posture: include all scored artifacts, filter by confidence for default responses
- Conflict posture: retain multiple viable options with "use-when" rules
- Handoff posture: produce both Decision Cards and Backlog Seeds

## Open Items
1. Final threshold values for escalation and contradiction density.
2. Standard tag vocabulary for domains/capabilities.
3. Hybrid backend implementation details (engine choices, sync tolerances, and rebuild procedures).
4. Feedback telemetry schema for downstream-success scoring.
5. Archival convention (`archive/*` branch vs external backup artifact store).

# Knowledge Architecture Contract (Draft)

## Purpose
Define a machine-operable structure for consolidating SDLC research so AI agents can retrieve high-value decisions quickly, escalate depth when needed, and continuously update recommendations as new research arrives.

## Design Goals
1. **Decision-first retrieval:** Answers should return recommended paths, not raw document dumps.
2. **Progressive depth:** Default concise output with optional escalation into deeper evidence tiers.
3. **Provenance + confidence:** Every claim and recommendation is traceable and scored.
4. **Continuous evolution:** New research updates existing decisions incrementally.
5. **AI-native operation:** Retrieval and reranking are designed for agent consumers without requiring UI workflows.
6. **Single-source repository posture:** `main`/`master` is the authoritative knowledge branch; auxiliary branches/worktrees are temporary ingestion vehicles only.

## Branch and Worktree Consolidation Policy
Use short-lived research branches/worktrees, then fully absorb and retire them.

### Policy Statements
- Maintain one authoritative knowledge corpus on `main`/`master`.
- Treat research branches/worktrees as **ephemeral staging environments**.
- Before merge, all candidate research must be:
  1. extracted,
  2. deduplicated semantically,
  3. mapped to domains/capabilities,
  4. provenance-linked,
  5. confidence-scored,
  6. reranked against current recommendations.
- After successful consolidation, the source branch/worktree must be archived or deleted and not reused.

### Merge Validation (Required)
Every research merge into `main`/`master` must pass one blocking validation:
- Query 3 capabilities affected by new artifacts.
- If any previously populated capability returns empty results, block completion.
- New capabilities with no prior DecisionCards are exempt.

Additionally, the human review queue must be fully resolved before consolidation status can be set to `completed`.

### Three-Layer Deduplication Method (Required)
Deduplication is executed as a staged pipeline:

1. **Layer 1 — Lexical candidate generation (MinHash LSH)**
   - Build near-duplicate candidate pairs using MinHash signatures + LSH buckets.
2. **Layer 2 — Semantic similarity filtering (Embeddings)**
   - Score Layer-1 pairs using sentence embedding cosine similarity.
3. **Layer 3 — AI arbitration (disagreements only)**
   - Invoke AI arbitration only when Layer 1 and Layer 2 disagree.
4. **Human review queue**
   - Route arbitration outputs to human review when AI confidence `< 0.70`.

Monitoring requirement:
- If Layer-3 arbitration calls exceed **20%** of Layer-1 candidates in a run, tune dedup thresholds before the next run.

### Provenance Retention After Branch Deletion
Branch deletion is allowed only if provenance remains recoverable in canonical metadata:
- source branch/worktree id
- source commit hash
- source path
- extraction timestamp
- consolidation run id

This preserves lineage while avoiding long-term branch/worktree sprawl.


## Corpus Organization and Normalization Policy
To prevent organizational drift and uncontrolled corpus growth:
- All research artifacts must be normalized into canonical domain files before run completion.
- Parallel duplicate topic files are not allowed in active corpus; merge into a single canonical section.
- Every run must update domain organization status in `domain_coverage_matrix.md`.
- Unclassified artifacts must be resolved (classified, merged, or archived) before `completed` status.

Refer to `docs/research/00_meta/corpus_organization_standard.md` for directory contract, naming rules, and organization gates.
Reference updates after reorganization are mandatory and governed by `docs/research/00_meta/reference_integrity_policy.md`.


## Storage and Retrieval Backend Policy (Hybrid Default)
Use a hybrid backend architecture by default:
- **Relational layer (authoritative):** canonical state, provenance, lifecycle gates, integrity reports.
- **Vector layer (derived):** semantic candidate retrieval for L1/L2.
- **Graph layer (derived):** relationship expansion, contradiction traversal, and impact analysis.

Governance and completion decisions must be made from relational source-of-truth records. Vector/graph layers are optimization and reasoning layers, not policy authority.

See `docs/research/00_meta/hybrid_storage_architecture.md` for details.

## Retrieval Hierarchy (L0-L3)
Use a strict escalation model to balance speed and rigor.

- **L0 Snapshot**
  - One recommended option
  - Confidence score + rationale (short)
  - "Use when" / "Do not use when"
- **L1 Brief (Default)**
  - Recommendation + top alternatives
  - Tradeoffs and key constraints
  - Evidence summary and contradiction flags
- **L2 Evidence Pack**
  - Source-by-source comparison
  - Experimental outcomes / failure cases
  - Merge rationale and conflict resolution notes
- **L3 Raw Provenance**
  - Extract lineage (branch/worktree/path/chunk)
  - Original snippets and extraction metadata
  - Full scoring inputs

### Escalation Rules
Escalate retrieval depth automatically when one or more conditions are met:
- Confidence below threshold
- Two or more viable alternatives within a small score margin
- Contradiction density above threshold
- User/agent requests deeper auditability

## Canonical Data Objects

### 1) `ResearchArtifact`
Raw extracted content unit.

```json
{
  "artifact_id": "ra_<uuid>",
  "title": "string",
  "content": "string",
  "domain_tags": ["prompting", "orchestration"],
  "capability_tags": ["repo_traversal"],
  "source": {
    "branch": "string",
    "worktree": "string",
    "consolidation_run_id": "cr_<uuid>",
    "ingested_into_ref": "main",
    "path": "string",
    "commit": "string",
    "captured_at": "ISO-8601"
  },
  "quality_signals": {
    "evidence_type": "theory|experiment|benchmark|postmortem",
    "source_reliability": 0.0,
    "freshness_days": 0
  }
}
```

### 2) `DecisionCard`
Canonical recommendation object for build-time use.

```json
{
  "decision_id": "dc_<uuid>",
  "question": "What should be used for X under Y constraints?",
  "context": {
    "capability": "repo_traversal",
    "constraints": {
      "latency_ms": 2000,
      "cost_tier": "medium",
      "repo_scale": "large"
    }
  },
  "recommendation": {
    "option_id": "opt_primary",
    "summary": "Use hybrid retrieval with policy reranking",
    "use_when": ["multi-source research", "high ambiguity"],
    "avoid_when": ["single small corpus"]
  },
  "alternatives": [
    {
      "option_id": "opt_vector_only",
      "status": "viable",
      "tradeoffs": ["simpler", "weaker relation reasoning"]
    }
  ],
  "confidence": {
    "score": 0.82,
    "level": "high",
    "explanation": "Diverse corroborating sources; low unresolved conflict"
  },
  "provenance_refs": ["ra_1", "ra_9", "ra_27"],
  "last_validated_at": "ISO-8601",
  "revisit_triggers": ["new contradictory benchmark", "major model release"]
}
```

### 3) `BacklogSeed`
Execution starter generated from Decision Cards (non-canonical).

```json
{
  "seed_id": "bs_<uuid>",
  "decision_id": "dc_<uuid>",
  "epics": [
    {
      "title": "Implement policy reranking pipeline",
      "tasks": [
        "Add metadata filter stage",
        "Add vector retrieval stage",
        "Add graph expansion stage",
        "Add final scoring and thresholding"
      ],
      "acceptance_criteria": [
        "Returns L1 brief in <2s p95",
        "Escalates to L2 when confidence < threshold"
      ]
    }
  ],
  "regeneration_policy": "regenerate_on_decision_change"
}
```

### 4) `DriftEvent`
Records when new evidence may invalidate existing decisions.

```json
{
  "event_id": "de_<uuid>",
  "decision_id": "dc_<uuid>",
  "trigger": "new_conflicting_artifact",
  "impact": {
    "confidence_delta": -0.18,
    "affected_sections": ["recommendation", "alternatives"]
  },
  "status": "pending_revalidation",
  "created_at": "ISO-8601"
}
```

## Confidence Model
Score each recommendation with weighted components:
- evidence strength
- source diversity
- recency
- contradiction penalty
- downstream success feedback

Example:

```text
confidence = 0.30*evidence_strength
           + 0.20*source_diversity
           + 0.20*recency
           + 0.20*downstream_success
           - 0.10*contradiction_penalty
```

Confidence bands:
- **High:** `>= 0.75`
- **Medium:** `0.50 - 0.74`
- **Low:** `< 0.50`

## Retrieval and Reranking Architecture
Use hybrid retrieval to support agent reasoning:
1. **Symbolic filter** (hard constraints, tags, confidence floors)
2. **Vector retrieval** (semantic similarity)
3. **Graph expansion** (related entities, dependencies, contradictory nodes)
4. **Policy reranking** (task fit + trust + freshness)
5. **Depth formatting** (L0-L3 response according to uncertainty)

## Update Lifecycle (Continuous Research Ingestion)
1. Create ephemeral research branch/worktree.
2. Ingest new artifacts with provenance and `consolidation_run_id`.
3. Semantic dedup against existing canonical artifacts.
4. Recompute affected Decision Cards only (incremental scope).
5. Emit DriftEvents when confidence drops or contradictions rise.
6. Revalidate Decision Cards and regenerate dependent BacklogSeeds.
7. Update indices/maps and publish a new versioned snapshot on `main`/`master`.
8. Archive or delete source branch/worktree and record retirement in consolidation log.

## Governance Rules
- Decision Cards are canonical and versioned.
- Backlog Seeds are disposable derivatives and should be regenerated.
- Unresolved contradictions cannot be hidden; they must remain queryable.
- All recommendations must include at least one provenance reference.
- Branch/worktree count should be minimized: only active in-flight research branches are allowed.
- Reusing previously retired research branches/worktrees is prohibited.

## Minimal File Layout

```text
docs/research/00_meta/
  knowledge_architecture_contract.md
  confidence_policy.md
  update_lifecycle.md
  consolidation_log.md
  unresolved_conflicts.md

docs/research/03_indices/
  decision_index.md
  capability_index.md
  source_to_decision_map.md
```

## Operational Defaults
- Default answer depth: **L1 Brief**
- Auto-escalation: enabled
- Trust posture: include all scored artifacts, filter by confidence for default responses
- Conflict posture: retain multiple viable options with "use-when" rules
- Handoff posture: produce both Decision Cards and Backlog Seeds

## Open Items
1. Final threshold values for escalation and contradiction density.
2. Standard tag vocabulary for domains/capabilities.
3. Hybrid backend implementation details (engine choices, sync tolerances, and rebuild procedures).
4. Feedback telemetry schema for downstream-success scoring.
5. Archival convention (`archive/*` branch vs external backup artifact store).
