# Technical Specification: Multi-Prong Research Distillation Pipeline

## 1. Technical Context

### 1.1 Language & Runtime
- **Language**: Python 3.12+
- **Existing infrastructure**: `scripts/` directory with `run_all_prompts.py`, `split_prompts.py`, `test_single_prompt.py` — all use `pathlib.Path`, `json`, `asyncio`, `dataclass`, UTF-8 Windows compatibility wrappers
- **No package manager config**: No `pyproject.toml`, `requirements.txt`, or `setup.py` exists. The pipeline will use Python stdlib plus `pyyaml` for YAML output
- **No test framework**: No pytest or unittest infrastructure. Tests will be standalone scripts following the existing `scripts/test_*.py` pattern

### 1.2 Input Corpus (on disk)
| Source | Count | Location Pattern |
|--------|-------|-----------------|
| Perplexity research files | 38 | `docs/research/**/perplexityai_research_overview*.md` |
| Topic overviews | 26 | `docs/research/**/overview.md` |
| Cross-topic indices | 12 | `docs/research/_indices/*.md` |
| Kimi-Research taxonomy docs | ~52 | `Kimi-Research/docs/research/{01..12}_*/` |
| Kimi-Research top-level guides | ~30 | `Kimi-Research/docs/research/*.md` (ARCHITECTURE_OVERVIEW, ANTI_PATTERNS, BENCHMARKS, etc.) |
| Kimi-Research CSV datasets | ~18 | `Kimi-Research/*.csv` + `Kimi-Research/research/*.csv` |
| Root research files | 4 | `Research.md`, `Perplexity_Thread.md`, `Prompt_thread.md`, `start_prompt.md` |
| Prompt config | 1 | `scripts/prompts/config.json` |

### 1.3 Dependencies
- **stdlib**: `pathlib`, `json`, `re`, `hashlib`, `dataclasses`, `typing`, `collections`, `csv`, `textwrap`, `argparse`
- **external**: `pyyaml` (YAML serialization for product specs)

## 2. Implementation Approach

### 2.1 Architecture: Single-Pass Pipeline with Staged Output

The pipeline is a **batch CLI tool** (`scripts/distill.py`) that reads all research files, processes them through four prongs sequentially, and writes structured output to `distillation/`.

```
scripts/distill.py
  ├── Step 1: Corpus scanning (discover all input files)
  ├── Step 2: Extraction (parse each file → raw knowledge atoms)
  ├── Step 3: Deduplication & ranking (merge duplicates, sort)
  ├── Step 4: Tagging (assign domains D1-D12, phases P1-P8, products PC1-PC10)
  ├── Step 5: Domain grouping (Prong 2 output)
  ├── Step 6: SDLC phase mapping (Prong 3 output)
  ├── Step 7: Product assembly (Prong 4 output)
  └── Step 8: Validation & gap report
```

### 2.2 Key Design Decisions

1. **No LLM calls during distillation**: The extraction uses heuristic/rule-based parsing of markdown structure (headers, bullet points, tables, bold text, metrics patterns). LLM-based extraction is explicitly out of scope — the pipeline extracts structural signals.

2. **Two-phase extraction**: First, a structural parser identifies candidate atoms from markdown (sections with metrics, tool names, techniques, numbered steps). Second, a classifier assigns TYPE based on content patterns (numbers → METRIC, "when...use" → TRADEOFF, ordered steps → RECIPE, etc.).

3. **ID generation**: `KA-{NNN}` format, assigned sequentially after deduplication. Atoms keep a stable hash (SHA-256 of normalized content) for dedup detection across runs.

4. **Evidence strength heuristic**: 
   - STRONG: Contains specific citation format (`[N]`, `[paper:N]`) AND a specific number/percentage
   - MODERATE: Contains a specific number/percentage OR a named source
   - WEAK: Assertion without data or attribution

5. **Output as files on disk**: JSON for the registry (machine-readable), YAML for product specs (human-readable), Markdown for domain/phase specs and reports.

### 2.3 Module Structure

```
scripts/
  distill.py              # CLI entrypoint
  distillation/
    __init__.py
    scanner.py            # Corpus file discovery
    parser.py             # Markdown parsing → raw candidate atoms
    classifier.py         # Atom TYPE classification
    dedup.py              # Deduplication & merging
    ranker.py             # Ranking within each TYPE
    tagger.py             # Domain/phase/product tag assignment
    prong2_domains.py     # Domain grouping output
    prong3_phases.py      # SDLC phase mapping output
    prong4_products.py    # Product spec assembly
    validator.py          # Cross-reference validation
    gap_report.py         # Gap analysis
    models.py             # Dataclasses: KnowledgeAtom, DomainSpec, PhaseSpec, ProductSpec
    constants.py          # Domain/phase/product enums, extraction patterns
    yaml_templates.py     # YAML spec template builders
```

## 3. Source Code Structure Changes

### 3.1 New Files

| File | Purpose |
|------|---------|
| `scripts/distill.py` | CLI entry point — orchestrates the pipeline |
| `scripts/distillation/__init__.py` | Package init |
| `scripts/distillation/models.py` | Core data models (`KnowledgeAtom`, `DomainSpec`, `PhaseSpec`, `ProductSpec`, enums) |
| `scripts/distillation/constants.py` | Enums for atom types, domains (D1-D12), phases (P1-P8), products (PC1-PC10); keyword/pattern maps for classification and tagging |
| `scripts/distillation/scanner.py` | Discovers all input files, returns categorized file list |
| `scripts/distillation/parser.py` | Parses markdown files into raw candidate atoms (section-level extraction) |
| `scripts/distillation/classifier.py` | Classifies raw atoms into the 9 TYPE categories using pattern matching |
| `scripts/distillation/dedup.py` | Content-hash-based deduplication, merging complementary sources |
| `scripts/distillation/ranker.py` | Ranks atoms within each TYPE by evidence strength, specificity, agent-specificity |
| `scripts/distillation/tagger.py` | Assigns DOMAINS, SDLC_PHASES, PRODUCTS tags using keyword matching against domain/phase/product vocabularies |
| `scripts/distillation/prong2_domains.py` | Generates 12 domain spec files from tagged atoms |
| `scripts/distillation/prong3_phases.py` | Generates 8 phase spec files from tagged atoms |
| `scripts/distillation/prong4_products.py` | Assembles product YAML specs from tagged atoms using templates |
| `scripts/distillation/validator.py` | Cross-reference validation (orphan detection, reference integrity) |
| `scripts/distillation/gap_report.py` | Gap analysis report generation |
| `scripts/distillation/yaml_templates.py` | YAML template builders for each product category (PC1-PC10) |
| `scripts/test_distill.py` | Verification script for the pipeline |

### 3.2 New Output Directory

```
distillation/
  registry/
    knowledge_atoms.json          # Master Knowledge Atom Registry (Prong 1)
  domains/
    D01_agent_architecture.md     # Domain specs (Prong 2)
    D02_task_management.md
    ...
    D12_self_improvement.md
  phases/
    P1_discovery_onboarding.md    # Phase specs (Prong 3)
    P2_planning_design.md
    ...
    P8_maintenance_monitoring.md
  products/
    modes/                        # Product specs (Prong 4) — YAML files
      *.yaml
    skills/
      *.yaml
    workflows/
      *.yaml
    prompts/
      *.yaml
    mcp_configurations/
      *.yaml
    rules/
      *.yaml
    context_strategies/
      *.yaml
    task_decomposition_patterns/
      *.yaml
    workspace_management/
      *.yaml
    techniques/
      *.yaml
  reports/
    validation_report.md          # Cross-reference validation
    gap_report.md                 # Gap analysis
```

### 3.3 Existing Files — No Modifications
The pipeline reads existing research files but never modifies them.

## 4. Data Model

### 4.1 KnowledgeAtom (core entity)

```python
@dataclass
class KnowledgeAtom:
    id: str                          # "KA-001"
    type: AtomType                   # Enum: TECHNIQUE, METRIC, CONSTRAINT, TOOL, etc.
    content: str                     # 1-5 sentences
    evidence_strength: EvidenceStrength  # Enum: STRONG, MODERATE, WEAK
    sources: list[str]               # File paths where found
    domains: list[str]               # ["D1", "D5"]
    sdlc_phases: list[str]           # ["P1", "P3"]
    products: list[str]              # ["PC2", "PC6"]
    content_hash: str                # SHA-256 for dedup
    raw_section: str                 # Original markdown section (for traceability)
```

### 4.2 Enums

```python
class AtomType(str, Enum):
    TECHNIQUE = "TECHNIQUE"
    METRIC = "METRIC"
    CONSTRAINT = "CONSTRAINT"
    TOOL = "TOOL"
    COMBINATION = "COMBINATION"
    FAILURE_MODE = "FAILURE_MODE"
    ANTI_PATTERN = "ANTI_PATTERN"
    TRADEOFF = "TRADEOFF"
    RECIPE = "RECIPE"

class EvidenceStrength(str, Enum):
    STRONG = "STRONG"
    MODERATE = "MODERATE"
    WEAK = "WEAK"

class Domain(str, Enum):
    D1 = "D1"   # Agent Architecture & Orchestration
    D2 = "D2"   # Task Management & Decomposition
    D3 = "D3"   # Context & Prompt Engineering
    D4 = "D4"   # Memory & Knowledge Systems
    D5 = "D5"   # Code Intelligence & Representations
    D6 = "D6"   # Testing & Validation
    D7 = "D7"   # Security & Guardrails
    D8 = "D8"   # Model Management & Routing
    D9 = "D9"   # CI/CD & DevOps
    D10 = "D10" # Workspace & Infrastructure Management
    D11 = "D11" # Human Interaction
    D12 = "D12" # Self-Improvement & Optimization

class SDLCPhase(str, Enum):
    P1 = "P1"   # Discovery & Onboarding
    P2 = "P2"   # Planning & Design
    P3 = "P3"   # Implementation
    P4 = "P4"   # Testing & Verification
    P5 = "P5"   # Code Review
    P6 = "P6"   # Debugging & Error Recovery
    P7 = "P7"   # Deployment & Release
    P8 = "P8"   # Maintenance & Monitoring

class ProductCategory(str, Enum):
    PC1 = "PC1"   # Modes
    PC2 = "PC2"   # Skills
    PC3 = "PC3"   # Workflows
    PC4 = "PC4"   # Prompts
    PC5 = "PC5"   # MCP Configurations
    PC6 = "PC6"   # Rules
    PC7 = "PC7"   # Context Management Strategies
    PC8 = "PC8"   # Task Decomposition Patterns
    PC9 = "PC9"   # Workspace Management
    PC10 = "PC10" # Techniques & Strategies
```

### 4.3 Output Spec Models

```python
@dataclass
class DomainSpec:
    domain: Domain
    name: str
    atom_ids: list[str]             # Ranked by evidence strength
    key_techniques: list[str]       # Atom IDs
    key_constraints: list[str]
    key_tools: list[str]
    combination_recipes: list[str]
    failure_modes: list[str]
    cross_domain_links: dict[str, list[str]]  # atom_id → other domains
    gaps: list[str]

@dataclass
class PhaseSpec:
    phase: SDLCPhase
    name: str
    description: str
    atom_ids: list[str]
    techniques_by_step: dict[str, list[str]]  # step_label → atom_ids
    constraints: list[str]
    tools: list[str]
    failure_modes: list[str]
    transitions: dict[str, str]               # condition → target phase

@dataclass
class ProductSpec:
    category: ProductCategory
    instance_name: str
    atom_ids: list[str]
    yaml_spec: dict                 # The filled YAML template
    confidence: str                 # HIGH | MEDIUM | LOW
    gaps: list[str]
```

## 5. Extraction & Classification Strategy

### 5.1 Markdown Parser (parser.py)

The parser processes each markdown file section-by-section:

1. Split file by `##` headers into sections
2. For each section, extract:
   - Bullet points (lines starting with `- ` or `* `)
   - Table rows (lines with `|`)
   - Bold text patterns (`**...**`)
   - Numbered lists
   - Metrics (regex: `\d+[\.\d]*[%x×]` or `\d+[-–]\d+%`)
3. Each meaningful section chunk becomes a **candidate atom**
4. Sections matching DISCARD rules are filtered: "See also", "Methodology", "Search Queries", confidence < 3 bullets, etc.

### 5.2 Classifier (classifier.py)

Pattern-based classification into the 9 types:

| Type | Detection Pattern |
|------|------------------|
| METRIC | Contains `\d+%` or `\d+x` or `\d+[-–]\d+%` range |
| TOOL | Contains a known tool name (Tree-sitter, Sourcegraph, Joern, CodeQL, Semgrep, etc.) with capability description |
| TECHNIQUE | Contains named method AND procedural verbs (parse, build, generate, verify, extract) |
| RECIPE | Contains ordered steps (numbered list ≥3 items with procedural content) |
| COMBINATION | Contains multiple tool/technique names with connective language (combine, together, unified, +) |
| CONSTRAINT | Contains "must", "never", "always", "invariant", "limit" with evidence |
| FAILURE_MODE | Contains "fail", "break", "attack", "vulnerability" with detection/response language |
| ANTI_PATTERN | Contains "don't", "avoid", "anti-pattern", "wrong", "doesn't work" |
| TRADEOFF | Contains "vs", "tradeoff", "when X use Y", comparative language |

Atoms that don't match any pattern are discarded. Atoms matching multiple patterns get the most specific type (RECIPE > TECHNIQUE > COMBINATION).

### 5.3 Tagger (tagger.py)

Keyword-vocabulary matching assigns domains, phases, and products:

- Each domain (D1-D12) has a keyword vocabulary (e.g., D5: "AST", "CFG", "DFG", "Tree-sitter", "symbol", "parse", "code graph")
- Each phase (P1-P8) has a keyword vocabulary (e.g., P1: "scan", "onboard", "discover", "map dependencies", "architecture extraction")
- Each product (PC1-PC10) has a keyword vocabulary (e.g., PC2: "skill", "technique", "procedure", "step-by-step", "capability")
- An atom is tagged with a domain/phase/product if it matches ≥2 keywords from that vocabulary

### 5.4 Deduplication (dedup.py)

1. Normalize content: lowercase, strip whitespace, remove citation markers
2. Compute SHA-256 of normalized content
3. Group atoms by hash
4. For groups with >1 atom: merge SOURCE lists, keep the version with highest evidence strength, merge complementary details

## 6. YAML Template Assembly (Prong 4)

Product specs are assembled by:

1. Collecting all atoms tagged with a given product category
2. Grouping atoms by sub-topic (inferred from domain + phase tags)
3. Identifying "instance" candidates — clusters of related atoms that form a coherent product (e.g., atoms about code traversal → Skill: Code Traversal)
4. Filling the YAML template for that product category using atom content
5. Setting confidence based on atom count and evidence strength

The 10 YAML templates from the PRD are implemented as Python dict builders in `yaml_templates.py`, one function per template (mode, skill, workflow, rule, context_strategy, technique, task_decomposition_pattern, mcp_configuration, prompt, workspace_management).

## 7. Delivery Phases

### Phase 1: Foundation (models, constants, scanner)
- `models.py`, `constants.py`, `scanner.py`
- Corpus discovery verified against expected file counts
- Testable: scanner finds all 38 Perplexity files, 26 overviews, 12 indices, Kimi files

### Phase 2: Extraction Pipeline (parser, classifier, dedup, ranker)
- `parser.py`, `classifier.py`, `dedup.py`, `ranker.py`
- Testable: parse a sample research file, verify atom extraction count > 0, types assigned, dedup merges duplicates

### Phase 3: Tagging & Prong 1 Output (tagger, registry writer)
- `tagger.py`, registry JSON output in `distill.py`
- Testable: every atom has ≥1 domain, ≥1 phase, ≥1 product tag. Registry JSON is valid and parseable.

### Phase 4: Prong 2 & 3 Output (domain specs, phase specs)
- `prong2_domains.py`, `prong3_phases.py`
- Testable: 12 domain files + 8 phase files generated, all reference valid atom IDs from registry

### Phase 5: Prong 4 Output (product specs)
- `prong4_products.py`, `yaml_templates.py`
- Testable: YAML files generated, valid YAML, conform to template structure

### Phase 6: Validation & Gap Report
- `validator.py`, `gap_report.py`
- Testable: validation report flags zero orphan atoms (or lists them), gap report categorizes coverage levels

### Phase 7: CLI Integration & End-to-End
- `distill.py` CLI with `--dry-run`, `--verbose`, `--output-dir` flags
- `scripts/test_distill.py` end-to-end verification
- Testable: full pipeline runs without error, all output files exist

## 8. Verification Approach

### 8.1 Structural Verification (test_distill.py)
- Registry JSON is valid JSON, all atoms have required fields
- All atom IDs are unique and follow `KA-NNN` pattern
- All atoms have ≥1 domain, ≥1 phase, ≥1 product
- 12 domain spec files exist with valid content
- 8 phase spec files exist with valid content
- Product YAML files are valid YAML
- Cross-references are consistent (atom IDs in domain/phase/product specs exist in registry)
- No orphan atoms
- File counts: registry contains atoms from all source files

### 8.2 Quality Verification (manual checklist from PRD §9)
- No textbook padding (spot-check: atoms reference AI-agent-specific knowledge)
- No unranked lists (techniques are ordered within each domain/phase)
- No vague procedures (atoms contain specific tool/action names)
- Combination recipes have numbered steps
- Constraints have enforcement
- Failure modes have responses
- Gaps are explicit

### 8.3 Lint/Type Check
- No formal linter configured in this project. Verification is via `python -c "import scripts.distillation"` (import check) and `scripts/test_distill.py` (runtime verification).

## 9. Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Heuristic extraction misses important atoms | Conservative extraction (keep more, filter in review); gap report flags thin areas |
| Dedup hash collisions (different atoms, same normalized text) | SHA-256 collision probability negligible; manual review of small duplicate groups |
| Keyword-based tagging assigns wrong domains/phases | Use narrow, specific keyword vocabularies; require ≥2 keyword matches |
| YAML template can't be fully filled from available atoms | Fill what's available, mark missing fields as `# GAP: [description]` |
| Large corpus causes slow processing | Pure file I/O + string processing; no LLM calls. Estimated runtime <60s for full corpus |
| CSV files in Kimi-Research contain useful data but different format | Scanner includes CSV files; parser extracts title/abstract columns as candidate atoms |
