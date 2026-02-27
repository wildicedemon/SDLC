# Reference Integrity Policy

## Purpose
Ensure reorganizing or normalizing corpus content does not break references, source mappings, or retrieval paths.

## Scope
Applies to:
- markdown links inside `docs/research/**`
- source path references in `docs/research/03_indices/source_to_decision_map.md`
- primary source references in `docs/research/03_indices/decision_index.md`
- run report references in `docs/research/00_meta/run_reports/**`

## Required Controls
1. **Path Rewrite Map**
   - Every file move/rename must produce a rewrite map entry (`old_path -> new_path`).
2. **Reference Rewrite Pass**
   - All known references must be rewritten using the rewrite map before run completion.
3. **Link Integrity Check**
   - Validate that all internal markdown links resolve after rewrite.
4. **Index Integrity Check**
   - Validate that each `source_path` in source-to-decision map exists and each decision source anchor remains resolvable.
5. **Change Report**
   - Record modified reference count, unresolved references, and manual fixes in run report.

## Blocking Conditions
A consolidation run cannot be `completed` if:
- any unresolved broken internal link remains,
- any source-to-decision path points to non-existent content,
- any DecisionCard primary source references moved content without rewrite,
- rewrite map is missing for renamed/moved files.

## Standard Artifacts per Run
- `reference_rewrite_map_<run_id>.md`
- `reference_integrity_report_<run_id>.md`

## Operational Notes
- Prefer stable IDs (`dc_*`, `ra_*`) for logical identity; paths are transport-level pointers that can change.
- If anchors change during normalization, update both index references and run report citations in same run.

# Reference Integrity Policy

## Purpose
Ensure reorganizing or normalizing corpus content does not break references, source mappings, or retrieval paths.

## Scope
Applies to:
- markdown links inside `docs/research/**`
- source path references in `docs/research/03_indices/source_to_decision_map.md`
- primary source references in `docs/research/03_indices/decision_index.md`
- run report references in `docs/research/00_meta/run_reports/**`

## Required Controls
1. **Path Rewrite Map**
   - Every file move/rename must produce a rewrite map entry (`old_path -> new_path`).
2. **Reference Rewrite Pass**
   - All known references must be rewritten using the rewrite map before run completion.
3. **Link Integrity Check**
   - Validate that all internal markdown links resolve after rewrite.
4. **Index Integrity Check**
   - Validate that each `source_path` in source-to-decision map exists and each decision source anchor remains resolvable.
5. **Change Report**
   - Record modified reference count, unresolved references, and manual fixes in run report.

## Blocking Conditions
A consolidation run cannot be `completed` if:
- any unresolved broken internal link remains,
- any source-to-decision path points to non-existent content,
- any DecisionCard primary source references moved content without rewrite,
- rewrite map is missing for renamed/moved files.

## Standard Artifacts per Run
- `reference_rewrite_map_<run_id>.md`
- `reference_integrity_report_<run_id>.md`

## Operational Notes
- Prefer stable IDs (`dc_*`, `ra_*`) for logical identity; paths are transport-level pointers that can change.
- If anchors change during normalization, update both index references and run report citations in same run.
