# Bootstrap Process (Minimum Viable Corpus)

## Purpose
Define the minimum process to bootstrap the corpus with real decision coverage and verify retrieval works end-to-end.

## Steps
1. Extract **10 DecisionCards** from existing framework docs (initial source: research benchmarking framework patterns).
2. Create corresponding `ResearchArtifact` records with provenance metadata.
3. Populate all three indices:
   - `docs/research/03_indices/decision_index.md`
   - `docs/research/03_indices/capability_index.md`
   - `docs/research/03_indices/source_to_decision_map.md`
4. Run one full consolidation cycle end-to-end using the update lifecycle.
5. Execute retrieval validation with 5 test queries across at least 3 capabilities.

## Retrieval Test Queries (Initial)
1. "What is the recommended method for hypothesis logging in formal studies?"
2. "How should stochastic benchmark comparisons be evaluated statistically?"
3. "What approach reduces production risk before rollout?"
4. "How should contamination risk be handled in benchmark reporting?"
5. "What is the recommended packaging strategy for reproducibility audits?"

## Completion Criteria
- `decision_index.md` has **>= 10** entries.
- `capability_index.md` has **>= 3** capabilities.
- Retrieval tests return a DecisionCard for each of the 5 queries.
- One consolidation run is recorded in `consolidation_log.md`.


## Current Execution Status
- Bootstrap extraction and index population: completed (`cr_bootstrap_2026_02_26`).
- Retrieval validation results: `docs/research/00_meta/bootstrap_validation_results.md`.
- Consolidation run report: `docs/research/00_meta/run_reports/cr_bootstrap_2026_02_26.md`.
