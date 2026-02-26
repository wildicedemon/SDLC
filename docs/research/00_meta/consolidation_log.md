# Consolidation Log

Track each ingestion/consolidation cycle.

| run_id | date | source_branch_or_worktree | artifacts_ingested | artifacts_deduped | decisions_impacted | drift_events | status | retirement_action |
|---|---|---|---:|---:|---:|---:|---|---|
| cr_example_001 | 2026-01-01 | research/example-branch | 120 | 78 | 14 | 3 | completed | deleted branch |

## Notes
- `retirement_action` must be populated for every completed run.
- Keep this append-only.
