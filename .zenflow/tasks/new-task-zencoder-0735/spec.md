# Technical Specification: Research Knowledge Consolidation & Organization

## Difficulty: Medium-Hard

## Technical Context

- **Language**: Markdown/YAML research artifacts (content), Python (operational code — DO NOT MODIFY)
- **Scope**: Consolidate and organize scattered research/knowledge artifacts; leave all operational code (`distillation/`, `corpus/`, `scripts/`, `knowledge_atom_extractor/`, `tests/`, `*.py`, `*.js`, `pyproject.toml`) untouched.

## Problem Statement

Multiple research agents have written to this repo at different times, producing:
- **3 generations of distillation outputs** in different locations with overlapping/conflicting data
- **Internal content duplication** within individual files (entire sections copy-pasted twice)
- **No clear canonical location** for the authoritative distilled knowledge
- **Root-level artifact sprawl** — intermediate JSON/MD outputs cluttering the repo root
- **Incomplete Kimi-Research integration** — parallel research in `Kimi-Research/` not yet merged into canonical structure

## Current State Analysis

### Three Generations of Distillation Outputs

| Generation | Location | Atoms | Status |
|---|---|---|---|
| Gen 1 | Root-level files (`gap_report.md`, `validation_report.md`, `knowledge_atom_registry.json`, `domain_knowledge_grouping.*`, `sdlc_phase_knowledge_mapping.*`, `product_specs*`, `registry_simple.json`, `atoms_list.txt`, `knowledge_atom_extraction_report.md`, `master_knowledge_atoms.json`) | 36 | **Superseded** |
| Gen 2 | `distilled/` directory (7 files: `prong1-4`, `final_summary`, `gap_report`, `validation_report`) | 68 | **Superseded** |
| Gen 3 | `docs/distillation/` (12 files: `master_index`, 6 prong1 files, prong2-4, gap_report, validation_report) | 372 | **Canonical / Most comprehensive** |

### Additional Duplicated Locations

| Location | Content | Status |
|---|---|---|
| `distillation/prong*.md` (5 files, 107-128KB each) | Intermediate prong outputs inside the code package | Should be archived |
| `docs/research/_distilled/` (4 files) | Yet another set of prong2-4 specs | Should be archived |
| `docs/distilled/` (2 files: `domain_groupings.md`, `knowledge_atom_registry.md`) | Registry-style outputs | Should be consolidated into canonical |
| `output/distilled/` (5 YAML files) | Pipeline test output (1 atom from `dummy_research.md`) | Test artifact, archive |
| `output/products/` (8 YAML files) | Product YAML specs | Review and link from canonical |

### Files with Internal Duplication (content repeated verbatim within same file)

| File | Issue |
|---|---|
| `distilled/final_summary.md` | Outputs + Quality Gates sections duplicated |
| `distilled/validation_report.md` | Entire report content duplicated |
| `distilled/gap_report.md` | All sections duplicated |
| `docs/research/00_meta/consolidation_log.md` | Entire table + notes duplicated |
| `docs/research/00_meta/corpus_organization_standard.md` | Entire document duplicated |

### Kimi-Research Integration Status

- `Kimi-Research/docs/research/` mirrors the main taxonomy (01-12 domains) with additional research
- `Kimi-Research/` root has CSV files with academic paper search results
- `Kimi-Research/docs/research/` has 30+ summary documents (ARCHITECTURE_OVERVIEW, ROADMAP, BENCHMARKS, etc.)
- `docs/research/kimi_integration_summary.md` exists but integration is incomplete

### Existing Organization Standards (in `docs/research/00_meta/`)

- `knowledge_architecture_contract.md` — defines how knowledge should be structured
- `corpus_organization_standard.md` — defines canonical directory structure
- `reference_integrity_policy.md` — defines link validation requirements
- `consolidation_log.md` — tracks consolidation runs (only 1 entry)

## DO NOT MODIFY (Operational Code)

- `distillation/` Python package (except the `prong*.md` files inside it which are data, not code)
- `corpus/` package
- `scripts/` directory
- `knowledge_atom_extractor/` directory
- `tests/` directory
- Root-level `*.py` and `*.js` files
- `pyproject.toml`, `requirements.txt`
- `.kilocodemodes`, `.roomodes`, `.kilocode/`
- `venv/`

## Implementation Approach

### Step 1: Fix Internal Duplication in Existing Files

Remove duplicated content blocks in:
- `distilled/final_summary.md`
- `distilled/validation_report.md`
- `distilled/gap_report.md`
- `docs/research/00_meta/consolidation_log.md`
- `docs/research/00_meta/corpus_organization_standard.md`

### Step 2: Archive Superseded Distillation Outputs

Create `archive/` directory with clear subdirectories:
- `archive/gen1_root_extraction/` — move Gen 1 root-level MD/JSON artifacts
- `archive/gen2_distilled/` — move Gen 2 `distilled/` directory contents
- `archive/intermediate_prongs/` — move `distillation/prong*.md` intermediate outputs
- `archive/research_distilled_drafts/` — move `docs/research/_distilled/` contents

Root-level files to archive:
- `gap_report.md`, `validation_report.md`, `knowledge_atom_extraction_report.md`
- `domain_knowledge_grouping.json`, `domain_knowledge_grouping.md`
- `sdlc_phase_knowledge_mapping.json`, `sdlc_phase_knowledge_mapping.md`
- `product_specs_report.md`, `product_specs.json`
- `knowledge_atom_registry.json`, `master_knowledge_atoms.json`, `registry_simple.json`
- `atoms_list.txt`, `product_specs_report.md`
- `dummy_research.md`

Also archive:
- `output/distilled/` YAML files (test artifacts)
- `docs/distilled/` contents (superseded by `docs/distillation/`)

### Step 3: Consolidate Kimi-Research into Canonical Structure

- Move unique Kimi-Research findings from `Kimi-Research/docs/research/` subdirectories into corresponding `docs/research/` subdirectories as supplementary references
- Move Kimi-Research summary documents into `docs/research/00_meta/kimi_research/` for reference
- Move CSV paper search results to `docs/research/_indices/kimi_papers/`
- Update `docs/research/kimi_integration_summary.md` to reflect completed integration

### Step 4: Establish Canonical Authority

- Confirm `docs/distillation/` as the single authoritative distilled knowledge location
- Update `docs/distillation/master_index.md` header to clearly state it is the canonical reference
- Clean up `docs/distilled/` — merge any unique content into `docs/distillation/`, then archive remainder
- Ensure `output/products/` YAML specs are referenced from `docs/distillation/prong4_product_assembly.md`

### Step 5: Update Progress & Indices

- Update `docs/research/_progress/completion_tracker.md` to reflect actual research status
- Update `docs/research/index.md` to link to canonical distillation outputs
- Update `docs/research/00_meta/consolidation_log.md` with this consolidation run
- Verify cross-reference indices in `docs/research/_indices/` are current

## Source Code Structure Changes

No source code changes. All changes are to research/knowledge markdown, JSON, and YAML files.

### Files Created
- `archive/` directory tree (receiving archived artifacts)
- `docs/research/00_meta/kimi_research/` (Kimi summary docs)
- `docs/research/_indices/kimi_papers/` (Kimi CSV data)

### Files Modified
- 5 files with internal deduplication fixes
- `docs/distillation/master_index.md` (canonical authority marker)
- `docs/research/_progress/completion_tracker.md` (status update)
- `docs/research/index.md` (link to canonical distillation)
- `docs/research/00_meta/consolidation_log.md` (new run entry)
- `docs/research/kimi_integration_summary.md` (integration update)

### Files Moved (to archive/)
- ~15 root-level intermediate artifacts
- `distilled/` directory contents (7 files)
- `distillation/prong*.md` files (5 files)
- `docs/research/_distilled/` contents (4 files)
- `docs/distilled/` contents (2 files)
- `output/distilled/` contents (5 files)

## Verification Approach

1. After deduplication: confirm no duplicated sections remain in fixed files
2. After archival: confirm `docs/distillation/` master_index still references all 372 atoms correctly
3. After Kimi integration: confirm no research content was lost (only moved/consolidated)
4. After cleanup: confirm all internal links in `docs/research/index.md` and `docs/distillation/master_index.md` resolve to existing files
5. Verify no operational code files were modified (check with `git diff` against known code paths)
