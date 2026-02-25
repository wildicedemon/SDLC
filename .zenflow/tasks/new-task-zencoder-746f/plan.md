# Full SDD workflow

## Configuration
- **Artifacts Path**: {@artifacts_path} → `.zenflow/tasks/{task_id}`

---

## Agent Instructions

If you are blocked and need user clarification, mark the current step with `[!]` in plan.md before stopping.

---

## Workflow Steps

### [x] Step: Requirements
<!-- chat-id: 6762708b-8e21-44cd-9ecb-675ec2926548 -->

Create a Product Requirements Document (PRD) based on the feature description.

1. Review existing codebase to understand current architecture and patterns
2. Analyze the feature definition and identify unclear aspects
3. Ask the user for clarifications on aspects that significantly impact scope or user experience
4. Make reasonable decisions for minor details based on context and conventions
5. If user can't clarify, make a decision, state the assumption, and continue

Save the PRD to `{@artifacts_path}/requirements.md`.

### [x] Step: Technical Specification
<!-- chat-id: 93eebff7-8d54-4cfe-8af5-41bfac8f1d85 -->

Create a technical specification based on the PRD in `{@artifacts_path}/requirements.md`.

1. Review existing codebase architecture and identify reusable components
2. Define the implementation approach

Save to `{@artifacts_path}/spec.md` with:
- Technical context (language, dependencies)
- Implementation approach referencing existing code patterns
- Source code structure changes
- Data model / API / interface changes
- Delivery phases (incremental, testable milestones)
- Verification approach using project lint/test commands

### [x] Step: Planning
<!-- chat-id: 97a99f6f-9b9b-4194-b0b0-7164d3c16c95 -->

Plan created below. Each step is a coherent unit of work with its own verification.

### [x] Step: Foundation — Data Models, Constants, and Package Scaffold
<!-- chat-id: c0edf0a5-453a-4679-abfb-d3dcd0250a5d -->

Create `scripts/distillation/` package with core data structures and enums.

- Create `scripts/distillation/__init__.py` (empty package init)
- Create `scripts/distillation/models.py`: `KnowledgeAtom`, `DomainSpec`, `PhaseSpec`, `ProductSpec` dataclasses per spec §4
- Create `scripts/distillation/constants.py`: `AtomType`, `EvidenceStrength`, `Domain`, `SDLCPhase`, `ProductCategory` enums; domain keyword vocabularies (D1-D12), phase keyword vocabularies (P1-P8), product keyword vocabularies (PC1-PC10); known tool names list; extraction/discard regex patterns
- Verification: `python -c "from scripts.distillation.models import KnowledgeAtom; from scripts.distillation.constants import AtomType, Domain"` succeeds

### [x] Step: Corpus Scanner
<!-- chat-id: 17964139-fe0f-4327-bb46-e539eca5f054 -->

Implement file discovery for the research corpus.

- Create `scripts/distillation/scanner.py`: `scan_corpus(root: Path) -> dict[str, list[Path]]` that discovers all input files categorized by source type (perplexity, overviews, indices, kimi_docs, kimi_csv, root_files)
- Match patterns from spec §1.2: `docs/research/**/perplexityai_research_overview*.md`, `docs/research/**/overview.md`, `docs/research/_indices/*.md`, `Kimi-Research/docs/research/**/*.md`, `Kimi-Research/**/*.csv`, root `.md` files
- Add inline test in `scripts/test_distill.py`: verify scanner finds files in each category (>0 count for each populated category)
- Verification: `python scripts/test_distill.py` passes scanner checks

### [x] Step: Markdown Parser and Atom Extraction
<!-- chat-id: 6a82057d-0df0-4a61-9531-9b72bb7a684d -->

Implement section-level extraction of candidate atoms from markdown files.

- Create `scripts/distillation/parser.py`: `parse_file(path: Path) -> list[RawAtom]`
  - Split markdown by `##` headers into sections
  - Extract bullet points, table rows, bold text, numbered lists, metrics patterns per spec §5.1
  - Apply DISCARD filters (scaffolding, "See also", methodology, aspirational, low-confidence)
  - Each meaningful section chunk becomes a `RawAtom` (content + source_path + raw_section)
- Handle CSV files: extract title/abstract columns as candidate atoms
- Add parser tests in `scripts/test_distill.py`: parse a sample research file, verify atom count > 0, verify discard rules filter known noise
- Verification: `python scripts/test_distill.py` passes parser checks

### [x] Step: Classifier and Evidence Strength
<!-- chat-id: a40e10e7-888f-469c-8739-12b3a3a3ed15 -->

Implement atom TYPE classification and evidence strength scoring.

- Create `scripts/distillation/classifier.py`: `classify(atom: RawAtom) -> KnowledgeAtom | None`
  - Pattern-based classification into 9 types per spec §5.2 (METRIC, TOOL, TECHNIQUE, RECIPE, COMBINATION, CONSTRAINT, FAILURE_MODE, ANTI_PATTERN, TRADEOFF)
  - Priority: RECIPE > TECHNIQUE > COMBINATION when multiple patterns match
  - Evidence strength heuristic per spec §2.2 item 4 (STRONG/MODERATE/WEAK)
  - Return None for atoms matching no type pattern (discard)
- Add classifier tests in `scripts/test_distill.py`: verify known input strings classify to expected types
- Verification: `python scripts/test_distill.py` passes classifier checks

### [x] Step: Deduplication and Ranking
<!-- chat-id: c447071b-159f-444f-9f84-4b5bccb07c10 -->

Implement content-hash dedup and ranking within each atom type.

- Create `scripts/distillation/dedup.py`: `deduplicate(atoms: list[KnowledgeAtom]) -> list[KnowledgeAtom]`
  - Normalize content (lowercase, strip whitespace, remove citation markers)
  - SHA-256 hash for grouping
  - Merge groups: keep highest evidence strength, merge SOURCE lists, merge complementary details per spec §5.4
- Create `scripts/distillation/ranker.py`: `rank(atoms: list[KnowledgeAtom]) -> list[KnowledgeAtom]`
  - Sort within each TYPE by: evidence strength, specificity heuristic, agent-specificity heuristic per spec §4.5 ranking rules
  - Assign sequential `KA-NNN` IDs after ranking
- Add dedup/ranker tests in `scripts/test_distill.py`: verify duplicate atoms merge, verify ranking order is evidence-first
- Verification: `python scripts/test_distill.py` passes dedup+ranker checks

### [x] Step: Tagger — Domain, Phase, and Product Assignment
<!-- chat-id: 9c31acd5-02b5-49ee-aa8d-165694933655 -->

Implement keyword-vocabulary-based tag assignment.

- Create `scripts/distillation/tagger.py`: `tag(atoms: list[KnowledgeAtom]) -> list[KnowledgeAtom]`
  - For each atom, match content against domain keyword vocabularies (D1-D12), phase vocabularies (P1-P8), product vocabularies (PC1-PC10) from `constants.py`
  - Assign tag when ≥2 keywords match per spec §5.3
  - Ensure every atom gets ≥1 domain, ≥1 phase, ≥1 product (fallback: assign most generic match if threshold not met)
- Add tagger tests in `scripts/test_distill.py`: verify known atoms get expected tags
- Verification: `python scripts/test_distill.py` passes tagger checks

### [x] Step: Prong 2 — Domain Grouping Output
<!-- chat-id: 59a0db5a-4bcb-4c02-868d-570668db47b0 -->

Generate 12 domain spec markdown files.

- Create `scripts/distillation/prong2_domains.py`: `generate_domain_specs(atoms: list[KnowledgeAtom], output_dir: Path)`
  - Group atoms by domain tags
  - For each domain (D1-D12), produce a markdown file following the domain output format from spec §Prong 2
  - Include ranked key techniques, constraints, tools, combination recipes, failure modes, cross-domain links, gaps
- Output to `distillation/domains/D01_agent_architecture.md` through `D12_self_improvement.md`
- Add test: verify 12 files generated, each contains valid atom ID references
- Verification: `python scripts/test_distill.py` passes domain output checks

### [ ] Step: Prong 3 — SDLC Phase Mapping Output
<!-- chat-id: 4d6df40f-473d-4a44-89ed-961017c8a5e9 -->

Generate 8 phase spec markdown files.

- Create `scripts/distillation/prong3_phases.py`: `generate_phase_specs(atoms: list[KnowledgeAtom], output_dir: Path)`
  - Group atoms by phase tags
  - For each phase (P1-P8), produce a markdown file following the phase output format from spec §Prong 3
  - Include sequenced techniques by step, constraints in effect, tools needed, failure modes, transitions
- Output to `distillation/phases/P1_discovery_onboarding.md` through `P8_maintenance_monitoring.md`
- Add test: verify 8 files generated, each contains valid atom ID references
- Verification: `python scripts/test_distill.py` passes phase output checks

### [ ] Step: Prong 4 — Product Spec Assembly (YAML Templates and Output)
<!-- chat-id: 71f531a0-a987-4c18-8018-ccac6c7bcd9a -->

Generate product YAML specs for all 10 categories.

- Create `scripts/distillation/yaml_templates.py`: one builder function per product category (PC1-PC10) — `build_mode_spec()`, `build_skill_spec()`, `build_workflow_spec()`, `build_rule_spec()`, `build_context_strategy_spec()`, `build_technique_spec()`, `build_task_decomposition_spec()`, `build_mcp_config_spec()`, `build_prompt_spec()`, `build_workspace_spec()`
  - Each builder takes a cluster of related atoms and fills the corresponding YAML template from spec §Spec Templates
  - Mark unfillable fields with `# GAP: [description]`
- Create `scripts/distillation/prong4_products.py`: `generate_product_specs(atoms: list[KnowledgeAtom], output_dir: Path)`
  - Collect atoms per product category
  - Cluster related atoms into product instances (e.g., code traversal atoms → Skill: Code Traversal)
  - Call template builders, write YAML files
- Output to `distillation/products/{category}/*.yaml`
- `pyyaml` dependency: add note in verification to `pip install pyyaml` if not present
- Add test: verify YAML files generated, valid YAML syntax, conform to template structure
- Verification: `python scripts/test_distill.py` passes product output checks

### [ ] Step: Validation, Gap Report, and CLI Entrypoint
<!-- chat-id: 14be2c41-c3e3-4076-be4e-77fdc2cd1f36 -->

Cross-reference validation, gap analysis, and CLI orchestration.

- Create `scripts/distillation/validator.py`: `validate(atoms, domain_specs, phase_specs, product_specs) -> ValidationReport`
  - Check every atom referenced by ≥1 domain, phase, product
  - Check cross-references (skills in modes exist, context strategies in modes exist, etc.)
  - Flag orphan atoms
- Create `scripts/distillation/gap_report.py`: `generate_gap_report(atoms, domain_specs, phase_specs, product_specs) -> str`
  - Categorize: strong backing (≥5 STRONG atoms), adequate (2-4 mixed), weak (<2 or WEAK only)
  - List orphan research, contradictions
- Create `scripts/distill.py`: CLI entrypoint orchestrating the full pipeline
  - `--dry-run`: scan + parse only, report counts
  - `--verbose`: log each step
  - `--output-dir`: default `distillation/`
  - Sequence: scan → parse → classify → dedup → rank → tag → write registry JSON → prong2 → prong3 → prong4 → validate → gap report
- Output reports to `distillation/reports/validation_report.md` and `distillation/reports/gap_report.md`
- Registry to `distillation/registry/knowledge_atoms.json`
- Create output directory structure (`distillation/registry/`, `domains/`, `phases/`, `products/{10 subdirs}/`, `reports/`)
- Add end-to-end test in `scripts/test_distill.py`: run full pipeline, verify all output files exist and are non-empty
- Verification: `python scripts/test_distill.py` passes all checks; `python scripts/distill.py --dry-run` succeeds
