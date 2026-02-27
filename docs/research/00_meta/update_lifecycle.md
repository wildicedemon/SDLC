# Update Lifecycle

## Purpose
Operationalize continuous research ingestion while keeping a single authoritative corpus.

## Workflow
1. Create ephemeral branch/worktree for new research.
2. Extract artifacts with provenance and `consolidation_run_id`.
3. Run three-layer deduplication:
   - **Layer 1 (lexical):** MinHash LSH candidate generation.
   - **Layer 2 (semantic):** sentence embedding cosine similarity filtering.
   - **Layer 3 (arbitration):** AI arbitration only for Layer-1/Layer-2 disagreements.
4. Route Layer-3 outputs with AI confidence `< 0.70` to the human review queue.
5. Recompute impacted DecisionCards only.
6. Emit DriftEvents for confidence drops/contradictions.
7. Revalidate DecisionCards and regenerate BacklogSeeds.
8. Update indices and publish snapshot on `main`/`master`.
9. Run reference integrity checks (rewrite map + link/index validation).
10. Record branch/worktree retirement and archive/delete source.

## Monitoring Requirement
- If Layer-3 arbitration calls exceed **20%** of Layer-1 candidates in a run, tune Layer-1/Layer-2 thresholds before the next run.

## Required Outputs per Run
- Consolidation summary
- Decision impact report
- Drift event report
- Index update confirmation
- Domain coverage matrix update (`domain_coverage_matrix.md`)
- Reference rewrite map (`reference_rewrite_map_<run_id>.md`)
- Reference integrity report (`reference_integrity_report_<run_id>.md`)
- Derived-layer sync health report (relational→vector/graph)
- Retirement record
- Human review queue disposition report

## Validation Gate (Single Blocking Check)
- Query 3 capabilities affected by new artifacts.
- If any previously populated capability returns empty results, block completion.
- New capabilities with no prior DecisionCards are exempt.
- Human review queue must be fully resolved before status is set to `completed`.
- New artifacts must conform to canonical directory contract and no unclassified orphan files may remain.
- No broken internal links or stale index references may remain after reorganization.

## Failure Handling
- If dedup pipeline fails: block merge and mark run as failed.
- If validation gate fails: block completion and reopen impacted DecisionCards.
- If index update fails: block merge.
- If reference integrity check fails: block completion until rewrites are applied.
- If derived-layer sync health fails tolerance, block completion until reindex/rebuild succeeds.
