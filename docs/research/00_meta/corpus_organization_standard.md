# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.

# Corpus Organization Standard

## Purpose
Define strict organization rules so research remains navigable as corpus volume grows.

## Canonical Directory Contract
All research content must map to this structure:

- `docs/research/00_meta/` — governance, lifecycle, policy, run artifacts.
- `docs/research/01_*/ ... 12_*/` — domain research content.
- `docs/research/03_indices/` — retrieval indices and source mappings.

No additional top-level research directories may be introduced without updating this standard.

## Domain Folder Requirements
Each domain/subdomain folder should contain:
- `overview.md` (scope + synthesis)
- `patterns.md` (actionable patterns)
- `comparisons.md` (alternatives + tradeoffs)
- `references.md` (source evidence)

If any file is missing, mark it in `domain_coverage_matrix.md` and queue remediation.

## Artifact Placement Rules
- Decision-oriented metadata belongs in `00_meta` or `03_indices`, not inside domain research folders.
- Raw/ad hoc notes from ingestion runs must be normalized into canonical domain files before consolidation completion.
- Deprecated or superseded notes must be moved to an archive section/file, not left mixed with active synthesis.

## Naming Rules
- Use lowercase snake_case filenames.
- Use deterministic IDs for run artifacts: `cr_<purpose>_<YYYY_MM_DD>`.
- Use deterministic IDs for decisions/sources: `dc_<domain>_<nnn>`, `ra_<domain>_<nnn>`.

## Organization Gates (Blocking)
A consolidation run cannot be set to `completed` unless:
1. New artifacts are placed in canonical directories.
2. `03_indices` entries are updated for each affected DecisionCard.
3. `domain_coverage_matrix.md` is updated if domain completeness changed.
4. No orphan files remain in staging/unclassified locations.

## Drift and Inflation Controls
- Keep active decision surface in indices concise; archive superseded decisions explicitly.
- Track per-domain growth and require justification if growth outpaces new decision utility.
- Prefer updating existing canonical pages over creating new parallel pages for same topic.


## Reference Integrity Requirements
- Every move/rename during organization must update links, index references, and run-report citations in the same run.
- Maintain a per-run rewrite map and integrity report as required artifacts.
- Do not finalize organization-only changes without passing reference integrity validation.

See `reference_integrity_policy.md` for the validation contract.
