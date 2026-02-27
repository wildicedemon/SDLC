# Spec and build

## Configuration
- **Artifacts Path**: {@artifacts_path} → `.zenflow/tasks/{task_id}`

---

## Agent Instructions

Ask the user questions when anything is unclear or needs their input. This includes:
- Ambiguous or incomplete requirements
- Technical decisions that affect architecture or user experience
- Trade-offs that require business context

Do not make assumptions on important decisions — get clarification first.

If you are blocked and need user clarification, mark the current step with `[!]` in plan.md before stopping.

---

## Workflow Steps

### [x] Step: Technical Specification
<!-- chat-id: cc80d14e-4bb6-4948-92ba-e8b60d4c351e -->

Difficulty: **Medium-Hard**. Full spec saved to `spec.md`.

Key findings:
- 3 generations of distillation outputs scattered across 6+ locations (36 → 68 → 372 atoms)
- `docs/distillation/` (Gen 3, 372 atoms) is the canonical/authoritative version
- 5 files have internal content duplication (sections copy-pasted twice within same file)
- Root-level artifact sprawl (~15 intermediate files)
- Kimi-Research partially integrated
- Operational code must remain untouched

---

### [x] Step: Fix Internal Duplication
<!-- chat-id: 9c6c7faa-24ad-4618-9cba-20b9241d0dcb -->

Remove duplicated content blocks within individual files:
- `distilled/final_summary.md` — remove duplicated Outputs + Quality Gates sections
- `distilled/validation_report.md` — remove duplicated entire report
- `distilled/gap_report.md` — remove duplicated sections
- `docs/research/00_meta/consolidation_log.md` — remove duplicated table
- `docs/research/00_meta/corpus_organization_standard.md` — remove duplicated document

Verification: confirm each file has no repeated sections after edit.

---

### [x] Step: Archive Superseded Distillation Outputs
<!-- chat-id: f7b3bc72-9071-4678-a1c8-d4609e96e669 -->

**Pre-step**: Create staging area: `mkdir -p .staging/archive-$(date +%Y%m%d)/`

**Execution** (stage → verify → commit):
1. Move files to staging first (per target subdirectory):
   - `.staging/archive-*/gen1_root_extraction/` ← root-level Gen 1 files (~15 files: `gap_report.md`, `validation_report.md`, `knowledge_atom_registry.json`, `domain_knowledge_grouping.*`, `sdlc_phase_knowledge_mapping.*`, `product_specs*`, `registry_simple.json`, `atoms_list.txt`, `knowledge_atom_extraction_report.md`, `master_knowledge_atoms.json`, `dummy_research.md`)
   - `.staging/archive-*/gen2_distilled/` ← `distilled/` directory contents (7 files)
   - `.staging/archive-*/intermediate_prongs/` ← `distillation/prong*.md` files (5 files)
   - `.staging/archive-*/research_distilled_drafts/` ← `docs/research/_distilled/` contents (4 files)
   - `.staging/archive-*/docs_distilled/` ← `docs/distilled/` contents (2 files)
   - `.staging/archive-*/output_test_artifacts/` ← `output/distilled/` contents (5 YAML test outputs)
2. Verify staging integrity: confirm all expected files present in `.staging/archive-*/`
3. Atomic commit to final location: `move .staging/archive-* archive/`
4. Clean up staging: `rmdir .staging/`

**Verification**: Confirm `docs/distillation/master_index.md` links still resolve; no operational code moved.

---

### [x] Step: Consolidate Kimi-Research into Canonical Structure
<!-- chat-id: 4bd88383-5617-4e99-bc8d-c0933d05e714 -->

- Move unique Kimi-Research domain research into corresponding `docs/research/` subdirectories
- Move Kimi-Research summary docs to `docs/research/00_meta/kimi_research/`
- Move CSV paper search results to `docs/research/_indices/kimi_papers/`
- Update `docs/research/kimi_integration_summary.md`

Verification: no research content lost; Kimi-Research findings accessible from canonical paths.

---

### [x] Step: Establish Canonical Authority & Update Indices
<!-- chat-id: be6c9d21-d595-4408-b215-aacf6657eb38 -->

- Mark `docs/distillation/` as authoritative in `master_index.md`
- Update `docs/research/index.md` to link to canonical distillation outputs
- Update `docs/research/_progress/completion_tracker.md` to reflect actual research status
- Update `docs/research/00_meta/consolidation_log.md` with this consolidation run entry
- Verify cross-reference indices in `docs/research/_indices/`

Verification: all internal links resolve; `git diff` confirms no operational code modified.

Completed 2026-02-27:
- Added CANONICAL AUTHORITY blockquote to `docs/distillation/master_index.md` header
- Removed internal duplication in master_index.md (entire second half was duplicate)
- Updated footer to Version 1.1, Status: Canonical / Authoritative
- Added "Canonical Distillation Outputs" section to `docs/research/index.md` with table linking all prong docs
- Added "Additional Indices" section linking kimi_integration_summary, cross_reference_validation_report, knowledge_atom_registry, consolidation_log
- Rewrote `docs/research/_progress/completion_tracker.md` — all 28 subdirectories now show COMPLETE (was showing 1/100+ with most NOT_STARTED)
- Added consolidation run `cr_consolidation_2026_02_27` to consolidation_log.md
- Deduped 3 files in `docs/research/03_indices/` (capability_index, decision_index, source_to_decision_map)
- Verified all 27 subdirectory README.md targets exist for cross-reference index links
- Verified all distillation prong files exist for master_index links
- `git diff` confirms only docs/research and docs/distillation files modified; zero operational code changes
