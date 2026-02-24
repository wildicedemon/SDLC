# Technical Specification: Research Distillation & Synthesis

## 1. Technical Context

### Language & Runtime
- **Input format**: Markdown (`.md` files)
- **Output format**: Markdown (`.md` files)
- **Processing**: AI agent-driven text analysis and synthesis (no custom code tooling)
- **Dependencies**: None (pure markdown-in, markdown-out)

### Input Artifacts
| File | Lines | Content |
|------|-------|---------|
| `Research.md` | ~1200 | Research engine prompt: 12-domain taxonomy (I-XII), 100+ topics, tiered prioritization, source requirements |
| `start_prompt.md` | ~705 | Build prompt: framework config, LangGraph, CLI, custom modes, Deep Scanner, waste detection, webhooks, bootstrap |

### Output Location
- All outputs under `.zenflow/tasks/new-task-97b2/`

## 2. Implementation Approach

### Core Strategy
Perform a three-phase sequential distillation of the two input artifacts:

1. **Inventory & Tag** - Parse both documents, extract discrete assertions/patterns/requirements, tag by domain
2. **Deduplicate & Synthesize** - Merge overlapping concepts, eliminate redundancy, cross-reference dependencies
3. **Generate Reports** - Produce master report + 6 domain reports + decision log

### Domain Taxonomy (Canonical 12 → Focused 6)
The 12 taxonomy domains from `Research.md` map to 6 focused report domains:

| Focused Report | Taxonomy Sources |
|---------------|-----------------|
| Orchestration & Workflow | II (Agent & Orchestration), VI-Task, VII-Distributed |
| Testing & Validation | V (SDLC Automation - Testing), V-Observability |
| Environment & Infrastructure | VI (Data & Infrastructure), V-CI/CD |
| Security & Compliance | I-Security, I-Governance |
| Performance & Optimization | I-Economic, VI-Infrastructure |
| Documentation & Knowledge | IV-Specification, IV-Code Intelligence |

Remaining domains (III-Context/Memory, VIII-Model, IX-Research, X-Scaling, XI-Advanced, XII-Meta-Control) are covered in the master report only.

### Deduplication Rules
- Each concept gets ONE canonical location
- Cross-references replace duplicates
- When `Research.md` and `start_prompt.md` describe the same concept, merge into a single canonical statement with source attribution
- Retain the most illustrative example per concept

## 3. Source Code Structure Changes

No source code changes. All work produces markdown files:

```
.zenflow/tasks/new-task-97b2/
  sdlc_framework_master_report.md    # Master synthesis (all 12 domains)
  decision_log.md                     # Consolidated decisions
  reports/
    orchestration_workflow.md          # Domain: Orchestration & Workflow
    testing_validation.md              # Domain: Testing & Validation
    environment_infrastructure.md      # Domain: Environment & Infrastructure
    security_compliance.md             # Domain: Security & Compliance
    performance_optimization.md        # Domain: Performance & Optimization
    documentation_knowledge.md         # Domain: Documentation & Knowledge
```

**Total: 8 files** (1 master + 6 domain + 1 decision log)

## 4. Data Model / Interface

### Master Report Structure
```markdown
# SDLC Framework Master Report
## 1. Framework Architecture
## 2. Core Components
## 3. Technology Stack
## 4. Workflow Lifecycle
## 5. Integration Points
## 6. Performance & Compliance
## 7. Critical Decisions
## 8. Implementation Roadmap (Now / Next / Later)
```

### Per-Domain Report Structure
```markdown
# [Domain Name]
## A. Executive Summary          (3-5 sentences)
## B. Core Concepts              (deduplicated bullets)
## C. Implementation Guidance    (what/how/why/dependencies)
## D. Validation Criteria        (tests, metrics, requirements)
## E. Known Gaps & Risks         (missing capabilities, unresolved items)
## F. Decision Log               (choices, alternatives, open questions)
```

### Decision Log Structure
```markdown
# Decision Log
## Resolved Decisions
| ID | Decision | Rationale | Alternatives Considered |
## Open Decisions
| ID | Question | Options | Trade-offs | Recommendation |
```

## 5. Delivery Phases

### Phase 1: Inventory & Extraction
- Parse `Research.md` sections I-XII, extract assertions per domain
- Parse `start_prompt.md` sections 2-7, extract build requirements per component
- Tag each extraction by canonical domain
- Flag cross-source overlaps

**Milestone**: Internal working inventory of all extracted items, tagged and flagged.

### Phase 2: Deduplication & Synthesis
- Merge identical concepts across sources
- Consolidate similar patterns with variance notes
- Assign each concept to exactly one canonical domain
- Build cross-reference map for concepts touching multiple domains
- Extract decisions (resolved + open) into decision log draft

**Milestone**: Deduplicated concept set with canonical assignments.

### Phase 3a: Master Report
- Generate `sdlc_framework_master_report.md` with all 8 sections
- Cover all 12 taxonomy domains
- Include Implementation Roadmap with Now/Next/Later prioritization

**Milestone**: Master report file exists, all 8 sections non-empty.

### Phase 3b: Domain Reports
- Generate 6 focused domain reports, each with sections A-F
- Each report references source documents for traceability
- No concept duplicated across domain reports

**Milestone**: All 6 domain report files exist, all subsections non-empty.

### Phase 3c: Decision Log
- Generate consolidated `decision_log.md`
- Include both resolved decisions (with rationale) and open decisions (with options/trade-offs)

**Milestone**: Decision log file exists with both resolved and open sections populated.

## 6. Verification Approach

### Structural Verification (automated check)
- All 8 output files exist at specified paths
- Master report contains all 8 section headers
- Each domain report contains all 6 subsection headers (A-F)
- Decision log contains both Resolved and Open sections
- No broken internal cross-references

### Quality Verification (manual review)
- No sentence exceeds 20 words (unless citing code/config)
- Every recommendation maps to a buildable component or action
- No concept repeated across report sections
- Critical items flagged with priority markers
- Source references (Research.md section or start_prompt.md section) present for traceability
- Open questions framed with options and trade-offs

### Completeness Verification
- All 12 taxonomy domains represented in master report
- All 6 focused domain reports cover their mapped taxonomy sections
- Key architectural decisions from both sources captured in decision log
- Implementation Roadmap has entries in all three buckets (Now/Next/Later)

## 7. Constraints
- No external dependencies or runtime services
- No code, configuration, or infrastructure artifacts produced
- All output is valid markdown
- Reports are self-contained (no references to non-existent files)
- Maximum ~20 words per sentence unless citing code/config
- One-time batch operation, not a service

## 8. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Input artifacts are prompts/instructions, not completed research data | Frame reports around defined requirements, patterns, and decisions rather than empirical findings |
| Domain overlap causes residual duplication | Assign each concept to exactly one canonical domain; cross-reference from others |
| Scope blur between "research distillation" and "framework implementation" | Each report section separates "what was researched" from "what to build" |
| Large input volume (~1900 lines) may cause context loss | Process in phases; verify each output against source sections systematically |
