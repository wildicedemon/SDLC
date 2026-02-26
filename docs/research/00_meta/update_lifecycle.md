# Update Lifecycle

## Purpose
Operationalize continuous research ingestion while keeping a single authoritative corpus.

## Workflow
1. Create ephemeral branch/worktree for new research.
2. Extract artifacts with provenance and `consolidation_run_id`.
3. Perform semantic dedup against canonical corpus.
4. Recompute impacted DecisionCards only.
5. Emit DriftEvents for confidence drops/contradictions.
6. Revalidate DecisionCards and regenerate BacklogSeeds.
7. Update indices and publish snapshot on `main`/`master`.
8. Record branch/worktree retirement and archive/delete source.

## Required Outputs per Run
- Consolidation summary
- Decision impact report
- Drift event report
- Index update confirmation
- Retirement record

## Failure Handling
- If dedup fails: block merge and mark run as failed.
- If unresolved contradictions exceed threshold: merge allowed only with explicit unresolved entry.
- If index update fails: block merge.
