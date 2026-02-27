# Knowledge Architecture Contract — Practical Implications Assessment

## Intent
This document evaluates the practical implications of the existing contract without modifying the contract itself. It is meant to guide execution planning, operational expectations, and risk controls.

## Executive Summary
The current contract is practical and strong for AI-agent consumption if execution discipline is high. Its biggest strengths are deterministic retrieval depth, provenance traceability, and incremental update flow. Its biggest risks are ingestion-quality drift, confidence inflation, and operational overhead from unresolved conflicts.

## Practical Benefits in Day-to-Day Operation
1. **Lower repeat-analysis cost:** L1-first retrieval prevents full-corpus rereads for most decisions.
2. **Faster convergence:** DecisionCard + alternatives framing narrows option space quickly.
3. **Safer branch hygiene:** ephemeral branch/worktree policy reduces long-lived repo sprawl.
4. **Auditable decisions:** provenance plus confidence enables reversible, explainable agent actions.
5. **Incremental maintenance:** update lifecycle supports partial recomputation instead of full rebuilds.

## Practical Burden Estimates
Use this as an order-of-magnitude guide for AI-only operations.

### Per-query retrieval burden
- **Low burden (majority path):** constraint filter + vector retrieval + rerank, answer at L1.
- **Medium burden:** L2 escalation due to close alternatives or moderate contradiction.
- **High burden:** L3 escalation for conflict arbitration/audit-sensitive decisions.

### Ongoing maintenance burden
- **Low:** simple ingestion where evidence agrees with existing decisions.
- **Medium:** ingestion requiring dedup merges across overlapping domains.
- **High:** ingestion that introduces broad contradictions across many DecisionCards.

## Conditions Required for Effectiveness
The contract remains effective when these are enforced:
- strict semantic dedup during ingestion
- consistent domain/capability tags
- confidence scoring tied to evidence diversity and recency
- automatic drift event generation on contradictions
- versioned snapshots and clear retirement logs for ephemeral branches/worktrees

## Failure Modes and Early Warning Signals
1. **Confidence inflation**
   - Signal: high-confidence decisions with weak source diversity.
2. **Taxonomy drift**
   - Signal: semantically similar artifacts split across inconsistent tags.
3. **Escalation overuse**
   - Signal: high percentage of queries reaching L2/L3.
4. **Decision staleness**
   - Signal: old validated dates despite frequent new ingestion.
5. **Backlog misuse**
   - Signal: backlog seeds treated as canonical policy.

## Recommended Operating Metrics
Track these continuously:
- L1 resolution rate (target high)
- L2/L3 escalation rate (target bounded)
- contradiction density by domain
- dedup compression ratio (raw artifacts -> canonical artifacts)
- median time to revalidate impacted DecisionCards
- confidence calibration error (predicted confidence vs downstream outcomes)

## Is a Separate Design Guide Needed?
Yes. The corpus alone is not enough to consistently produce high-quality skills/workflows. A stable design guide is needed to provide invariant architecture rules and composition defaults.

### Why this matters in practice
Without a guide, two agents can read the same corpus and still produce incompatible skill boundaries, orchestration patterns, and quality gates.

### What the guide should do (without replacing the corpus)
- define architecture invariants for skills/workflows
- define decomposition and orchestration defaults
- define prompt-evolution guardrails
- define model/tool routing policy
- define minimum validation gates

## Recommended Adoption Path
1. Keep the contract unchanged as canonical policy.
2. Add the design guide as a companion, not a replacement.
3. Pilot on 1-2 high-value capabilities and measure retrieval burden metrics.
4. Tune thresholds (confidence/escalation) based on observed telemetry.
5. Expand to full-corpus operation after calibration.

## Bottom Line
Your current plan is practical and directionally strong. The main execution risk is not architecture quality but operational discipline in ingestion, scoring, and drift management. With metric-driven calibration and a companion design guide, this approach should scale for AI-first skill/workflow generation.


## Is There a Superior Method?
Yes—there is a potentially superior variant for scale: a **Two-Tier Knowledge System**.

### Two-Tier Method (Recommended Upgrade Path)
Instead of only one canonical corpus, split storage and retrieval into two tiers:

1. **Tier A: Canonical Decision Layer (small, high-signal)**
   - DecisionCards, active alternatives, current confidence, and policy constraints.
   - Optimized for fast L1 answers and low cognitive/load burden.
2. **Tier B: Evidence Lake (large, append-heavy)**
   - Full extracted artifacts, lineage, historical conflicts, and superseded variants.
   - Optimized for deep auditability, re-ranking, and model retraining inputs.

### Why this can outperform the current baseline
- Reduces retrieval noise by keeping default queries in Tier A.
- Preserves full history without polluting default recommendation paths.
- Enables cheaper incremental updates: append to Tier B, selectively promote to Tier A.
- Makes branch/worktree retirement safer because evidence survives independently of active decision surface.

### Tradeoffs
- Additional orchestration complexity (promotion/demotion between tiers).
- Requires explicit lifecycle states (`candidate`, `active`, `superseded`, `archived`).
- Needs stronger automation to prevent stale decisions in Tier A.

### When to adopt
Adopt this upgrade if any two are true:
- L2/L3 escalation rate remains high after calibration.
- Contradiction density keeps rising with new research ingestion.
- Canonical layer size grows enough that L1 precision declines.

### Minimal migration strategy
1. Keep current contract as-is for governance continuity.
2. Mark DecisionCards as Tier A and raw `ResearchArtifact` corpus as Tier B.
3. Add promotion rules: only evidence-backed, revalidated recommendations can enter Tier A.
4. Add demotion rules: contradicted/stale recommendations move to superseded state.
5. Keep one authoritative branch while storing Tier B as structured append-only datasets in-repo or artifact storage.


## Hybrid Backend Decision (Adopted)
Adopt a hybrid backend for this project:
- relational database as canonical system-of-record,
- vector retrieval for semantic candidate generation,
- graph layer for relationship/contradiction traversal.

### Why this is the right fit here
- aligns with strict lifecycle and integrity gates already defined,
- improves retrieval quality without sacrificing governance,
- supports scalable contradiction and impact analysis.

### Implementation sequence
1. Phase 1: relational + vector.
2. Phase 2: add graph expansion for heavy multi-hop reasoning domains.
3. Keep completion gates tied to relational state across phases.
