# Domain Report: Documentation & Knowledge Management

## A. Executive Summary

This report covers automated documentation, API documentation standards, changelog management, knowledge representation, code intelligence, and MCP resource specifications for the SDLC Framework. Research identifies documentation as a dual concern: both a quality gate artifact (inline docs, ADRs, READMEs) and a knowledge system enabling code intelligence (AST, symbol graphs, semantic search). The framework requires documentation synchronized with implementation, deferred-creation strategies to avoid premature spec writing, and MCP-based code graph navigation for agent context. Critical gaps include no automated doc-sync mechanism, undefined ADR templates, and no changelog generation tooling.

*Sources: Research.md §IV.12-13 (Code Intelligence & Exploration, Specification & Design), §III.9-11 (Memory & Knowledge Representation); start_prompt.md §6.5 (Documentation Standards), §4.4.4 (Deep Scanner MCP client)*

## B. Core Concepts

- **Inline code documentation**: All modules must include inline docs; quality gate enforces presence before phase promotion *(start_prompt.md §6.5; see [Master Report §1 Quality Gates](../sdlc_framework_master_report.md#quality-gates))*
- **Architecture Decision Records (ADRs)**: Record significant architectural decisions with rationale, alternatives, and consequences *(start_prompt.md §6.5)*
- **README per major component**: Each framework component requires a README with setup, usage, and configuration *(start_prompt.md §6.5)*
- **Deferred documentation strategy**: Avoid writing extensive documentation before implementation; docs follow code, not precede it *(start_prompt.md §6.1; Research.md §I.1)*
- **Documentation accuracy requirement**: Docs must be accurate to current implementation; stale docs are treated as defects *(start_prompt.md §6.5)*
- **CodeGraphContext MCP for code navigation**: Provides AST access, symbol indexing, and call graph analysis to agents *(start_prompt.md §4.4.4; Research.md §IV.12)*
- **Symbol indexing platforms**: Full code graph enables semantic code navigation, relationship chain verification, and dependency mapping *(Research.md §IV.12)*
- **Lossless Semantic Tree (LST)**: Rich code representation preserving formatting, comments, and type information for precise code transformations *(Research.md §III.11)*
- **Repo grokking**: Automated codebase understanding via deep scanning and pattern extraction *(Research.md §IV.12; seed source: Zencoder repo grokking blog)*
- **Semantic search for agent memory**: Vector DB-backed retrieval of prior decisions, patterns, and knowledge *(Research.md §III.9; see [Master Report §5.2](../sdlc_framework_master_report.md#52-mcp-model-context-protocol-servers))*
- **Scanner repertoire learning**: Deep Scanner persists learned patterns to `.framework/scanner-repertoire.md` for reuse *(start_prompt.md §4.4.4)*
- **Documentation templates and formatting standards**: Consistent structure for all artifact types *(Research.md §IV.13)*
- **Docstrings best practices**: Language-appropriate docstring conventions for Python (Google/NumPy style) and TypeScript (JSDoc/TSDoc) *(Research.md §IV.13)*
- **API flow diagrams**: Visual documentation of API interaction paths and endpoint maps *(Research.md §IV.13)*
- **Changelog management**: Track changes per release for upstream contribution readiness *(start_prompt.md §4.9)*
- **Context-engine MCP paradigm**: MCP servers as documentation and knowledge interfaces for agents *(Research.md §IV.12; seed source: AugmentCode context engine MCP blog)*

## C. Implementation Guidance

### What to Build

| Component | Location | Purpose |
|-----------|----------|---------|
| Documentation gate checker | `src/framework/quality-gates.ts` (extension) | Verifies inline docs, ADRs, READMEs exist |
| ADR template | `.framework/templates/adr-template.md` | Consistent format for architecture decisions |
| Scanner MCP client | `src/scanner/mcp-client.ts` | Invokes CodeGraphContext for code graph access |
| Scanner repertoire store | `.framework/scanner-repertoire.md` | Persists learned patterns from scanner passes |
| Changelog generator config | `.framework/config.yaml` (changelog section) | Configures changelog format and commit conventions |
| Docstring linter config | Lint config files | Enforces docstring presence and format |

### How to Build It

- **Documentation gate**: Extend quality gate runner to check: (1) all `.ts`/`.py` files have module-level doc comments, (2) ADR directory contains entries for major decisions, (3) each `src/` subdirectory has a README; fail gate with specific missing-doc report *(start_prompt.md §6.5)*
- **ADR template**: Create template with sections: Title, Status, Context, Decision, Consequences, Alternatives Considered; store in `.framework/templates/`; reference in contribution guide *(start_prompt.md §6.5)*
- **Scanner MCP client**: Connect to CodeGraphContext MCP server; query symbol index, call graphs, dependency trees; provide results to scanner passes for architecture and anti-pattern analysis *(start_prompt.md §4.4.4)*
- **Repertoire learning**: After each scanner cycle, extract new patterns found; append to `.framework/scanner-repertoire.md` with timestamp, pattern description, and confidence; deduplicate against existing entries *(start_prompt.md §4.4.4)*
- **Changelog**: Follow Keep a Changelog format; derive entries from commit messages using conventional commits convention; generate per-release section *(start_prompt.md §4.9)*
- **Docstring linting**: Configure ESLint (jsdoc plugin) for TypeScript and pydocstyle/ruff for Python; enforce in CI pipeline *(Research.md §IV.13)*

### Why This Approach

- Documentation gate as part of existing quality gate system avoids separate tooling *(see [Testing Report §C](./testing_validation.md#c-implementation-guidance))*
- ADR templates ensure consistency without prescribing content; lightweight process
- CodeGraphContext MCP is already a required dependency; leveraging it for documentation intelligence avoids additional tools *(see [Master Report §5.2](../sdlc_framework_master_report.md#52-mcp-model-context-protocol-servers))*
- Deferred documentation prevents premature specs that drift from implementation
- Conventional commits enable automated changelog generation

### Dependencies

- CodeGraphContext MCP server must be installed (via bootstrap) *(see [Environment Report §C](./environment_infrastructure.md#c-implementation-guidance))*
- rag-memory-mcp for semantic search of prior knowledge *(see [Master Report §5.2](../sdlc_framework_master_report.md#52-mcp-model-context-protocol-servers))*
- Quality gate runner must support extensible gate definitions *(see [Testing Report §C](./testing_validation.md#c-implementation-guidance))*
- Lint tooling (ESLint, ruff/pydocstyle) must be configured in CI
- Git conventional commits convention must be adopted for changelog automation

## D. Validation Criteria

| Criterion | Metric | Method |
|-----------|--------|--------|
| Inline docs present | All public modules have doc comments | Documentation gate check in CI |
| ADRs recorded | ADR exists for each resolved decision in decision log | Count ADR files vs. decision log entries |
| READMEs present | Each `src/` subdirectory has README | Documentation gate directory scan |
| Docs accurate | No stale references to renamed/removed code | Periodic link/reference validation script |
| CodeGraphContext integration | Symbol queries return valid results | Integration test: query known symbols, verify response |
| Scanner repertoire | New patterns appended after scan cycle | Integration test: run scan, verify repertoire file updated |
| Docstring linting | Lint passes with zero docstring violations | CI lint step with jsdoc/pydocstyle rules |
| Changelog generated | Release section contains entries from commits | Script test: conventional commits produce changelog entries |
| ADR template valid | Template renders with all required sections | Unit test: template has Title, Status, Context, Decision, Consequences |
| Knowledge retrieval | Semantic search returns relevant prior decisions | Integration test: query rag-memory-mcp for known stored decision |

## E. Known Gaps & Risks

| Gap/Risk | Severity | Mitigation |
|----------|----------|------------|
| No automated doc-sync mechanism | Medium | Docs can drift from implementation; manual review at quality gates until automated sync built |
| ADR template not yet created | Low | Template is straightforward to author; not blocking other work |
| Changelog generation tooling not selected | Medium | Conventional-changelog, standard-version, or custom script needed; not yet evaluated |
| Docstring linter not configured | Low | ESLint jsdoc plugin and ruff/pydocstyle available; requires CI pipeline integration |
| No API documentation generation | Medium | No tool selected for generating API docs from code (e.g., TypeDoc, Sphinx); manual docs only |
| Scanner repertoire deduplication undefined | Low | Append-only approach risks duplicates; deduplication logic deferred |
| Knowledge graph construction absent | Medium | Graph-based knowledge representation researched (Research.md §III.11) but not in scope for initial delivery |
| LST implementation not planned | Low | Lossless Semantic Tree is a research concept; standard AST via CodeGraphContext sufficient initially |
| Org-wide knowledge base not designed | Low | Organization-level knowledge sharing deferred to scaling phase *(Research.md §III.9)* |
| Spec-driven vs. intent-driven tension unresolved | Low | Research documents both approaches; framework defaults to deferred docs *(Research.md §I.1; seed source: AugmentCode spec-driven critique)* |

## F. Decision Log

### Resolved Decisions

| ID | Decision | Rationale |
|----|----------|-----------|
| K-1 | Deferred documentation strategy | Avoids premature specs that drift; docs follow code *(start_prompt.md §6.1)* |
| K-2 | ADRs for architectural decisions | Lightweight, widely adopted format; captures rationale and alternatives *(start_prompt.md §6.5)* |
| K-3 | CodeGraphContext MCP for code intelligence | Already a required dependency; provides AST, symbol index, call graphs *(start_prompt.md §4.4.4)* |
| K-4 | Markdown for scanner state and repertoire | Human-readable, git-friendly, no database dependency *(see [Master Report §7 D-5](../sdlc_framework_master_report.md#resolved-decisions))* |
| K-5 | Documentation as quality gate | Enforces docs exist before phase promotion; prevents undocumented code from advancing *(start_prompt.md §6.5)* |
| K-6 | rag-memory-mcp for agent knowledge retrieval | Provides persistent memory and semantic search without custom vector DB setup *(start_prompt.md §4.4.7)* |

### Open Decisions

| ID | Question | Options | Recommendation |
|----|----------|---------|----------------|
| K-O1 | API documentation generator | TypeDoc, Sphinx, custom Markdown, none initially | TypeDoc for TypeScript; Sphinx for Python; defer until APIs stabilize |
| K-O2 | Changelog tooling | conventional-changelog, standard-version, release-please, manual | conventional-changelog with conventional commits; automate in CI |
| K-O3 | Docstring style for Python | Google style, NumPy style, Sphinx style | Google style (concise, widely adopted) |
| K-O4 | Knowledge graph implementation | Neo4j, NetworkX, custom graph, defer | Defer; CodeGraphContext MCP sufficient for code navigation initially |
| K-O5 | Spec-driven vs. deferred docs default | Spec-first, deferred-docs, configurable per project | Deferred-docs default; configurable override in `.framework/config.yaml` |

*Cross-references: See [Master Report §2.4](../sdlc_framework_master_report.md#24-deep-scanner) for scanner component overview; [Master Report §5.2](../sdlc_framework_master_report.md#52-mcp-model-context-protocol-servers) for MCP server integration; [Testing Report §C](./testing_validation.md#c-implementation-guidance) for quality gate runner details; [Security Report §C](./security_compliance.md#c-implementation-guidance) for audit logging as documentation.*
