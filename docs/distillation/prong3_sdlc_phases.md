# Prong 3: SDLC Phase Mapping - Temporal Organization

**Prong**: 3 of 4 (Temporal/Phase Organization)  
**Input**: 372 knowledge atoms from Prong 1 extractions  
**Output**: Phase-based temporal organization with execution sequences  
**Date**: 2026-02-24  

---

## Executive Summary

This document maps 372 knowledge atoms to 8 SDLC phases (P1-P8) for the multi-agent autonomous coding platform. Each phase includes sequenced techniques, applicable constraints, required tools, failure modes to monitor, and transition conditions.

**Atom Distribution by Phase:**
| Phase | Primary Atoms | Cross-Cutting Atoms | Total |
|-------|--------------|---------------------|-------|
| P1 Discovery | 35 | 85 | 120 |
| P2 Planning | 42 | 78 | 120 |
| P3 Implementation | 68 | 52 | 120 |
| P4 Testing | 54 | 45 | 99 |
| P5 Code Review | 48 | 38 | 86 |
| P6 Debugging | 39 | 42 | 81 |
| P7 Deployment | 52 | 35 | 87 |
| P8 Maintenance | 38 | 48 | 86 |

*Note: Atoms appear in multiple phases when relevant to multiple stages*

---

## P1: Discovery & Onboarding

**WHAT THE AGENT IS DOING:**
The agent scans the codebase to build comprehensive understanding through semantic analysis, extracting architecture patterns, entrypoints, dependencies, and context. This phase establishes the foundation for all subsequent work by creating a knowledge graph of the codebase structure.

---

**KNOWLEDGE ATOMS:**
KA-META-018, KA-META-029, KA-META-038, KA-META-049, KA-META-053, KA-CMI-007, KA-CMI-008, KA-CMI-013, KA-CMI-016, KA-CMI-019, KA-CMI-021, KA-CMI-023, KA-CMI-025, KA-CMI-052, KA-CODE-002, KA-CODE-003, KA-CODE-020, KA-CODE-021, KA-CODE-022, KA-CODE-023, KA-CODE-024, KA-CODE-030, KA-CODE-040, KA-CODE-042, KA-CODE-048, KA-CODE-049, KA-CODE-051, KA-CODE-052, KA-CODE-057, KA-AGENT-006, KA-AGENT-008, KA-AGENT-015, KA-AGENT-024, KA-AGENT-027, KA-SDLC-009, KA-SDLC-028, INFRA-011, HUMAN-008

---

**TECHNIQUES TO USE (ranked, by step):**

**Step 1 — Initialize codebase access and cold start mitigation:**
KA-META-018 (Cold start mitigation), KA-CMI-025 (Vector database selection), KA-CODE-051 (Zencoder Repo Grokking), KA-CODE-052 (Augment Context Engine)

**Step 2 — Parse and index codebase structure:**
KA-CMI-007 (Semantic chunking), KA-CMI-008 (Code-aware chunking overlap), KA-CMI-016 (Multi-representation fusion AST+CFG+DFG), KA-CMI-019 (Sourcegraph/Kythe indexing), KA-CODE-040 (Tree-sitter incremental parsing)

**Step 3 — Identify entrypoints and active code paths:**
KA-CODE-003 (Entrypoint-first exploration), KA-CODE-020 (Call chain verification), KA-CODE-021 (Static call graph precision), KA-CODE-023 (Design pattern detection)

**Step 4 — Build dependency and relationship graphs:**
KA-CMI-021 (SSA form for data flow), KA-CODE-022 (Incremental dependency tracking), KA-CODE-030 (Dual-database architecture), KA-CODE-042 (Entrypoint+Semantic+Pattern+DualDB combo)

**Step 5 — Extract architectural patterns and conventions:**
KA-CODE-023 (Design pattern detection), KA-META-029 (Semantic Codebase Understanding), KA-META-049 (Progressive Disclosure Architecture), KA-AGENT-027 (System-Theoretic Agent Decomposition)

**Step 6 — Prioritize files by relevance:**
KA-CODE-002 (Semantic-guided traversal), KA-CODE-024 (Intelligent file prioritization), KA-CMI-013 (Hybrid search vector+BM25)

**Step 7 — Cache and store grokked context:**
KA-CMI-052 (Context staleness prevention), KA-CODE-048 (Stale exploration cache failure prevention), KA-CMI-023 (Incremental representation updates)

---

**CONSTRAINTS IN EFFECT:**
- KA-META-053 (Complexity scoring metrics limitations)
- KA-CODE-041 (Code property graph computational overhead)
- KA-CODE-057 (Unbounded exploration scope prevention)
- KA-CMI-052 (Context staleness thresholds)
- INFRA-024 (Kubernetes node scaling limits)

---

**TOOLS NEEDED:**
- KA-CMI-019 (Sourcegraph/Kythe/LSIF)
- KA-CMI-025 (Vector database - Pinecone/Weaviate/Qdrant)
- KA-CODE-040 (Tree-sitter)
- KA-CODE-051 (Zencoder Repo Grokking)
- KA-CODE-052 (Augment Context Engine MCP)
- KA-SDLC-028 (Kubernetes)

---

**FAILURE MODES TO WATCH FOR:**
- KA-META-038 (System design anti-patterns: Shallow repo understanding)
- KA-CODE-031 (Static-only dependency analysis misses)
- KA-CODE-032 (Shallow call graph analysis)
- KA-CODE-048 (Stale exploration cache)
- KA-CODE-049 (Pattern blindness)
- KA-CODE-057 (Unbounded exploration scope)
- KA-AGENT-024 (Monolithic FM-Centric Design)
- KA-CMI-053 (Blind code comment trust)

---

**TRANSITIONS:**

**Exit to P2 (Planning) when:**
- Entrypoints identified and catalogued (KA-CODE-003)
- Dependency graph built with >85% coverage (KA-CODE-022)
- Pattern library extracted (KA-CODE-023)
- Vector index populated and searchable (KA-CMI-025)
- Confidence score >0.8 on codebase understanding

**Fallback to P1 (self) when:**
- Stale cache detected (KA-CMI-052)
- Significant code changes invalidate grokking (>20% files changed)
- Pattern detection fails (KA-CODE-049)
- Context poisoning detected (KA-CMI-005)

---
---

## P2: Planning & Design

**WHAT THE AGENT IS DOING:**
The agent decomposes tasks into atomic subtasks, sequences dependencies, creates specifications, and designs implementation approaches. This phase translates intent into actionable plans with clear success criteria and rollback strategies.

---

**KNOWLEDGE ATOMS:**
KA-META-009, KA-META-026, KA-META-027, KA-META-029, KA-META-038, KA-META-044, KA-META-048, KA-META-050, KA-META-053, KA-META-054, KA-AGENT-002, KA-AGENT-006, KA-AGENT-008, KA-AGENT-015, KA-AGENT-019, KA-AGENT-020, KA-AGENT-026, KA-AGENT-030, KA-AGENT-031, KA-AGENT-036, KA-AGENT-037, KA-AGENT-038, KA-CMI-009, KA-CMI-010, KA-CMI-034, KA-CMI-035, KA-CMI-048, KA-CODE-014, KA-CODE-029, KA-CODE-035, KA-CODE-036, KA-CODE-054, KA-CODE-055, KA-SDLC-018, KA-SDLC-032, KA-SDLC-061, DATA-001, DATA-004, DATA-012, DATA-013, DATA-014, DATA-018, HUMAN-002, HUMAN-020

---

**TECHNIQUES TO USE (ranked, by step):**

**Step 1 — Parse and clarify requirements:**
KA-AGENT-006 (Clarification capabilities), KA-META-044 (Intent verification checkpoint), HUMAN-008 (Structured follow-up questions), KA-CODE-029 (Intent-driven development)

**Step 2 — Decompose task into atomic subtasks:**
KA-AGENT-020 (Optimal task decomposition depth), KA-AGENT-031 (Atomic Task Creation), KA-AGENT-036 (Hierarchical decomposition), KA-AGENT-037 (AdaptOrch topology routing), KA-META-039 (Budget-Aware Task Decomposition)

**Step 3 — Analyze dependencies and build task graph:**
KA-AGENT-019 (Async DAG execution), KA-AGENT-030 (Cycle detection in task graphs), KA-CODE-022 (Incremental dependency tracking), KA-AGENT-016 (Worktree isolation)

**Step 4 — Select architectural pattern:**
KA-META-048 (Pattern Selection Guide), KA-META-050 (Key architectural tradeoffs), KA-META-026 (Spec-Driven vs Intent-Driven), KA-AGENT-027 (System-Theoretic Decomposition)

**Step 5 — Create specifications:**
KA-META-009 (Spec-driven 4-phase workflow), KA-META-027 (Bidirectional Specifications), KA-CODE-014 (Scope boundary documentation), KA-CODE-036 (Over-specification prevention), DATA-004 (Contract-Aware Code Generation)

**Step 6 — Allocate budgets and resources:**
KA-META-039 (Budget-Aware Task Decomposition), KA-META-054 (Complexity Budget Framework), KA-CMI-009 (Context window partitioning), KA-META-001 (Cost modeling per task)

**Step 7 — Plan validation approach:**
KA-SDLC-018 (BDD with Gherkin), KA-SDLC-032 (TDD red-green-refactor), KA-CODE-005 (TDD defect reduction), KA-CMI-034 (Chain-of-Thought for planning)

---

**CONSTRAINTS IN EFFECT:**
- KA-AGENT-020 (Optimal decomposition: 2-3 levels simple, 5-7 complex)
- KA-META-054 (Complexity Budget Framework)
- KA-CODE-014 (Scope creep prevention)
- KA-CODE-036 (Over-specification limits)
- KA-AGENT-030 (3-8% task graphs contain cycles)
- DATA-012 (Shared database anti-pattern)
- DATA-013 (God table anti-pattern)

---

**TOOLS NEEDED:**
- KA-AGENT-037 (AdaptOrch topology routing)
- KA-META-006 (Cost modeling frameworks)
- DATA-001 (Declarative Schema as Code tools)
- HUMAN-002 (Five-Level Agent Autonomy Framework)
- KA-CMI-025 (Vector DB for context retrieval)

---

**FAILURE MODES TO WATCH FOR:**
- KA-META-038 (Vibe Coding anti-pattern)
- KA-META-053 (Complexity metrics limitations)
- KA-AGENT-026 (Over-Delegation)
- KA-AGENT-030 (Task graph cycles)
- KA-CODE-035 (Spec rot)
- KA-CODE-036 (Over-specification)
- KA-CODE-054 (Specification rigidity)
- DATA-012 (Shared database coupling)
- DATA-013 (God table accumulation)
- DATA-014 (Implicit schema)

---

**TRANSITIONS:**

**Exit to P3 (Implementation) when:**
- Task decomposition complete with 2-7 depth levels (KA-AGENT-020)
- Specifications created with acceptance criteria (KA-META-009)
- Dependency graph validated (no cycles) (KA-AGENT-030)
- Budgets allocated per subtask (KA-META-039)
- Test plan defined (KA-SDLC-032)

**Fallback to P1 (Discovery) when:**
- Insufficient codebase understanding for task (KA-CODE-057)
- Missing dependencies detected during planning
- Context stale (>threshold) (KA-CMI-052)

**Fallback to self (P2) when:**
- Cycle detected in task graph (KA-AGENT-030)
- Scope creep detected (KA-CODE-014)
- Specification conflicts require replanning

---
---

## P3: Implementation

**WHAT THE AGENT IS DOING:**
The agent generates code following specifications while managing context windows, applying patterns, and maintaining style consistency. This phase produces actual code changes with continuous validation and compression.

---

**KNOWLEDGE ATOMS:**
KA-META-002, KA-META-003, KA-META-004, KA-META-009, KA-META-010, KA-META-013, KA-META-018, KA-META-019, KA-META-022, KA-META-023, KA-META-034, KA-META-039, KA-META-040, KA-META-041, KA-META-045, KA-META-047, KA-META-049, KA-META-058, KA-CMI-001, KA-CMI-002, KA-CMI-003, KA-CMI-004, KA-CMI-009, KA-CMI-010, KA-CMI-012, KA-CMI-014, KA-CMI-015, KA-CMI-034, KA-CMI-035, KA-CMI-036, KA-CMI-037, KA-CMI-040, KA-CMI-041, KA-CMI-042, KA-CMI-043, KA-CMI-044, KA-CMI-048, KA-CMI-049, KA-CMI-050, KA-CMI-051, KA-CMI-054, KA-CODE-005, KA-CODE-013, KA-CODE-016, KA-CODE-025, KA-CODE-027, KA-CODE-029, KA-CODE-037, KA-CODE-046, KA-CODE-047, KA-AGENT-002, KA-AGENT-031, KA-SDLC-029, KA-SDLC-044, DATA-002, DATA-004, DATA-006, HUMAN-004, HUMAN-005, HUMAN-010, INFRA-018

---

**TECHNIQUES TO USE (ranked, by step):**

**Step 1 — Retrieve relevant context:**
KA-CMI-010 (Task-conditioned context selection), KA-CMI-013 (Hybrid search), KA-CMI-003 (U-shaped context placement), KA-META-040 (Retrieval Compression Pipeline)

**Step 2 — Compress context to fit window:**
KA-CMI-001 (LLMLingua prompt compression), KA-CMI-002 (Selective Context), KA-CMI-012 (LLM summarization + observation masking), KA-CMI-014 (Context compression tradeoffs), KA-META-004 (Token efficiency techniques)

**Step 3 — Apply reasoning paradigm:**
KA-CMI-034 (Chain-of-Thought), KA-CMI-035 (Tree-of-Thought), KA-CMI-036 (Graph-of-Thought), KA-CMI-048 (Reasoning paradigm tradeoffs), KA-META-045 (Chain-of-Verification)

**Step 4 — Generate code with pattern adherence:**
KA-META-009 (Spec-driven workflow), KA-CODE-046 (Specification-driven generation combo), KA-CODE-047 (API development combo), KA-CODE-029 (Intent-driven development), KA-CODE-016 (Automated code formatting)

**Step 5 — Apply model cascade for efficiency:**
KA-META-002 (Model cascade routing), KA-META-010 (Provider cost comparison), KA-META-019 (Skill/Agent enablement), HUMAN-004 (Cascaded LLM decision)

**Step 6 — Validate generated code:**
KA-CMI-037 (Reflexion self-critique), KA-CMI-038 (Multi-model adversarial reasoning), KA-CMI-042 (Confidence scoring), KA-CMI-044 (Intent verification), KA-META-013 (Anti-hallucination guardrails)

**Step 7 — Apply normalization and budgets:**
KA-CODE-037 (AI code normalization), KA-CODE-011 (Complexity budgets), KA-CODE-013 (AI slop reduction), KA-META-039 (Budget-Aware decomposition)

---

**CONSTRAINTS IN EFFECT:**
- KA-META-003 (Semantic caching thresholds)
- KA-META-004 (Token efficiency targets)
- KA-META-007 (Budget enforcement mechanisms)
- KA-CMI-004 (<15% context waste target)
- KA-CMI-009 (20% system / 30% history / 40% retrieval / 10% working)
- KA-CMI-041 (Temperature 0.3-0.5 for coding)
- KA-CMI-043 (Max 2-3 refinement iterations)
- KA-CODE-011 (Complexity budget enforcement)
- KA-CMI-015 (No context stuffing)

---

**TOOLS NEEDED:**
- KA-META-002 (Model cascade router)
- KA-META-046 (Anti-hallucination tools: LangChain Guardrails, LM-Polygraph)
- KA-CMI-011 (Augment Context Engine MCP)
- KA-CMI-025 (Vector database)
- INFRA-018 (Tiered Model Serving)
- HUMAN-005 (Confidence-Calibrated Escalation)

---

**FAILURE MODES TO WATCH FOR:**
- KA-META-011 (Prompt injection attacks)
- KA-META-012 (Hallucination: fabricated packages, vulnerabilities)
- KA-META-021 (Economic optimization anti-patterns)
- KA-CMI-005 (Context poisoning)
- KA-CMI-006 (Wake-up prompts don't work)
- KA-CMI-015 (Context stuffing)
- KA-CMI-030 (Catastrophic forgetting)
- KA-CMI-040 (Echo chamber self-review)
- KA-CMI-043 (Infinite refinement loops)
- KA-CODE-013 (AI slop: 30% more abstraction, 20% verbosity)
- KA-CODE-033 (Infinite repair loops)
- KA-SDLC-029 (LLM tests miss boundary conditions)

---

**TRANSITIONS:**

**Exit to P4 (Testing) when:**
- Code generates successfully with syntax validation
- Complexity budgets satisfied (KA-CODE-011)
- Confidence score >threshold (KA-CMI-042)
- Self-critique passes (KA-CMI-037)
- Specifications met (KA-META-009)

**Exit to P5 (Code Review) when:**
- Code passes local validation
- Ready for adversarial review (KA-CMI-038)

**Fallback to P2 (Planning) when:**
- Implementation reveals specification gaps
- Complexity budget exceeded (KA-CODE-011)
- Context poisoning detected (KA-CMI-005)
- Confidence below threshold requiring replanning

**Fallback to P1 (Discovery) when:**
- Missing critical codebase understanding
- Dependencies not fully grokked

---
---

## P4: Testing & Verification

**WHAT THE AGENT IS DOING:**
The agent generates and executes tests across multiple levels (unit, integration, E2E), validates behavior against specifications, applies mutation testing, and ensures sad path coverage. This phase provides confidence for deployment decisions.

---

**KNOWLEDGE ATOMS:**
KA-SDLC-015, KA-SDLC-016, KA-SDLC-017, KA-SDLC-018, KA-SDLC-019, KA-SDLC-020, KA-SDLC-021, KA-SDLC-022, KA-SDLC-023, KA-SDLC-024, KA-SDLC-029, KA-SDLC-030, KA-SDLC-032, KA-SDLC-036, KA-SDLC-037, KA-SDLC-038, KA-SDLC-039, KA-SDLC-043, KA-SDLC-044, KA-SDLC-046, KA-SDLC-051, KA-SDLC-052, KA-SDLC-053, KA-SDLC-056, KA-SDLC-057, KA-SDLC-058, KA-SDLC-060, KA-SDLC-070, KA-SDLC-071, KA-SDLC-072, KA-SDLC-074, KA-SDLC-077, KA-SDLC-078, KA-SDLC-080, KA-SDLC-082, KA-SDLC-083, KA-SDLC-084, KA-CODE-004, KA-CODE-005, KA-CODE-007, KA-CODE-008, KA-CODE-009, KA-CODE-010, KA-CODE-018, KA-CODE-032, KA-CODE-033, KA-CODE-034, KA-CODE-038, KA-CODE-044, KA-CODE-045, KA-CMI-038, KA-CMI-039, KA-AGENT-004, KA-AGENT-018, KA-AGENT-021, KA-AGENT-034, KA-META-013, KA-META-022, KA-META-023, KA-META-024, DATA-006, DATA-016

---

**TECHNIQUES TO USE (ranked, by step):**

**Step 1 — Generate test cases:**
KA-SDLC-044 (AI agent test generation workflow), KA-SDLC-018 (BDD with Gherkin), KA-CODE-005 (TDD approach), KA-SDLC-029 (LLM-generated test coverage)

**Step 2 — Ensure test pyramid proportions:**
KA-SDLC-057 (70% unit / 20% integration / 10% E2E), KA-SDLC-017 (E2E cost tradeoff), KA-SDLC-015 (Unit test isolation)

**Step 3 — Generate sad path coverage:**
KA-CODE-007 (60-70% failures from untested error paths), KA-CODE-034 (Happy path bias prevention), KA-SDLC-046 (Sad path testing requirements), KA-SDLC-030 (Fuzzing for vulnerabilities)

**Step 4 — Execute multi-stage validation:**
KA-SDLC-036 (Multi-stage validation gates), KA-SDLC-060 (Multi-stage validation pipeline), KA-AGENT-034 (Multi-Stage Validation Pipeline), KA-CODE-044 (Iterative repair + test-verified combo)

**Step 5 — Apply process supervision:**
KA-SDLC-037 (Process supervision), KA-SDLC-038 (Four-level testing hierarchy), KA-SDLC-050 (Outcome-only validation prevention)

**Step 6 — Measure coverage and quality:**
KA-SDLC-024 (80% line coverage minimum), KA-SDLC-058 (Coverage threshold constraint), KA-SDLC-020 (Mutation testing >80%), KA-SDLC-043 (Test quality improvement loop)

**Step 7 — Validate determinism:**
KA-SDLC-039 (Determinism-first testing), KA-SDLC-051 (Temperature 0.0-0.3 for reproducibility)

---

**CONSTRAINTS IN EFFECT:**
- KA-SDLC-057 (Test pyramid: 70/20/10 ratio)
- KA-SDLC-058 (80% line coverage minimum)
- KA-SDLC-020 (Mutation score >80%)
- KA-SDLC-024 (MC/DC for safety-critical)
- KA-SDLC-056 (1-10% sampling rate for tracing)
- KA-CODE-007 (Must test sad paths)
- KA-SDLC-053 (Guardrails vs flexibility balance)

---

**TOOLS NEEDED:**
- KA-SDLC-080 (MCP for tool abstraction testing)
- KA-META-046 (Anti-hallucination tools)
- DATA-016 (Synthetic data generation tools)
- KA-SDLC-070 (Contract testing with Pact)
- KA-SDLC-071 (LLM-as-judge validation)
- KA-SDLC-072 (Guardrails AI, Outlines, LMQL)

---

**FAILURE MODES TO WATCH FOR:**
- KA-SDLC-046 (Happy path bias: 80% AI tests cover happy paths)
- KA-SDLC-074 (Test interdependence)
- KA-SDLC-077 (Mock overuse)
- KA-SDLC-078 (Coverage gaming)
- KA-SDLC-084 (Trust without verification)
- KA-CODE-033 (Infinite repair loops)
- KA-CODE-034 (Happy path bias)
- KA-SDLC-049 (In-context reward hacking)
- KA-SDLC-050 (Outcome-only validation)

---

**TRANSITIONS:**

**Exit to P5 (Code Review) when:**
- All validation gates pass (KA-SDLC-036)
- Coverage thresholds met (KA-SDLC-058)
- Mutation score >80% (KA-SDLC-020)
- Determinism verified (KA-SDLC-039)

**Exit to P6 (Debugging) when:**
- Tests fail requiring repair (KA-CODE-008)
- Mutation testing identifies weak areas (KA-SDLC-043)

**Fallback to P3 (Implementation) when:**
- Coverage gaps require additional code (KA-SDLC-044)
- Sad paths not testable with current implementation (KA-CODE-007)

---
---

## P5: Code Review

**WHAT THE AGENT IS DOING:**
The agent performs multi-faceted code review using adversarial patterns, semantic diffing, security analysis, and style verification. This phase ensures code quality, security, and adherence to standards before merge.

---

**KNOWLEDGE ATOMS:**
KA-AGENT-004, KA-AGENT-005, KA-AGENT-018, KA-AGENT-021, KA-AGENT-035, KA-CMI-020, KA-CMI-038, KA-CMI-040, KA-CMI-047, KA-CODE-004, KA-CODE-011, KA-CODE-016, KA-CODE-020, KA-CODE-025, KA-CODE-038, KA-CODE-043, KA-CODE-045, KA-META-013, KA-META-015, KA-META-016, KA-META-022, KA-META-023, KA-META-024, KA-META-034, KA-META-035, KA-META-046, KA-META-047, KA-SDLC-009, KA-SDLC-010, KA-SDLC-012, KA-SDLC-025, KA-SDLC-026, KA-SDLC-035, KA-SDLC-069, KA-SDLC-071, DATA-010, HUMAN-011, HUMAN-012

---

**TECHNIQUES TO USE (ranked, by step):**

**Step 1 — Perform semantic diff analysis:**
KA-CMI-020 (Semantic diffs), KA-CODE-043 (Refactoring impact analysis combo), KA-CMI-016 (Multi-representation fusion for understanding)

**Step 2 — Execute adversarial review:**
KA-AGENT-005 (Adversarial review patterns), KA-AGENT-018 (Multi-agent QA swarms), KA-CMI-038 (Multi-model adversarial reasoning), KA-AGENT-004 (Mixture-of-Agents), KA-META-015 (Hallucination defense tradeoffs)

**Step 3 — Apply security scanning:**
KA-META-022 (Static analysis for hallucination), KA-META-023 (RAG for Code with Hybrid Retrieval), KA-META-016 (Security hardening checklist), KA-META-035 (Layered Guardrail Envelope), KA-CMI-017 (Code Property Graphs for security), HUMAN-012 (AI deception detection)

**Step 4 — Validate style and patterns:**
KA-CODE-016 (Automated code formatting), KA-CODE-011 (Complexity budgets), KA-CODE-025 (Readability improvements), KA-CODE-038 (Test-verified refactoring), KA-META-034 (Evidence-First Action Gating)

**Step 5 — Calculate quality scores:**
KA-SDLC-025 (Agent performance scoring), KA-SDLC-026 (Trust scoring), KA-AGENT-021 (Agent GPA framework), KA-META-013 (Anti-hallucination effectiveness)

**Step 6 — Generate review feedback:**
KA-CMI-047 (Multi-agent code review pattern), HUMAN-011 (HITL in code review), KA-SDLC-012 (Error fingerprinting)

---

**CONSTRAINTS IN EFFECT:**
- KA-CODE-011 (Complexity budgets enforced)
- KA-META-016 (Security hardening checklist)
- KA-META-020 (Security hardening requirements)
- KA-META-034 (Evidence threshold for high-impact actions)
- DATA-010 (API linting breaking change prevention)
- KA-SDLC-053 (Guardrails vs flexibility tradeoff)

---

**TOOLS NEEDED:**
- KA-META-046 (Anti-hallucination tools)
- KA-CMI-017 (Joern CPG platform)
- KA-CMI-019 (Sourcegraph)
- KA-AGENT-021 (Agent GPA framework)
- KA-SDLC-071 (LLM-as-judge)
- DATA-010 (API linting tools)

---

**FAILURE MODES TO WATCH FOR:**
- KA-META-012 (Hallucination impact: 40-45% vulnerabilities)
- KA-META-016 (Security anti-patterns)
- KA-CMI-040 (Echo chamber self-review)
- KA-CODE-049 (Pattern blindness in review)
- HUMAN-012 (AI deception bypassing HITL)
- HUMAN-023 (Review fatigue overwhelming humans)
- KA-SDLC-084 (Trust without verification)

---

**TRANSITIONS:**

**Exit to P6 (Debugging) when:**
- Issues found requiring repair (KA-CODE-008)
- Security vulnerabilities detected (KA-META-012)
- Quality scores below threshold (KA-SDLC-025)

**Exit to P7 (Deployment) when:**
- All review checks pass
- Adversarial consensus reached (KA-AGENT-005)
- Quality scores meet thresholds (KA-SDLC-025)
- Security scan clean (KA-META-016)

**Fallback to P3 (Implementation) when:**
- Fundamental design issues found
- Pattern violations requiring rewrite (KA-CODE-016)
- Complexity budget exceeded (KA-CODE-011)

---
---

## P6: Debugging & Error Recovery

**WHAT THE AGENT IS DOING:**
The agent diagnoses root causes of failures, generates repairs, validates fixes through testing, and manages rollback if needed. This phase handles both development-time debugging and production incident response.

---

**KNOWLEDGE ATOMS:**
KA-AGENT-002, KA-AGENT-033, KA-CMI-037, KA-CMI-046, KA-CODE-008, KA-CODE-009, KA-CODE-010, KA-CODE-012, KA-CODE-033, KA-CODE-038, KA-CODE-044, KA-CODE-055, KA-CODE-058, KA-META-002, KA-META-018, KA-META-045, KA-SDLC-001, KA-SDLC-002, KA-SDLC-004, KA-SDLC-006, KA-SDLC-007, KA-SDLC-009, KA-SDLC-012, KA-SDLC-013, KA-SDLC-020, KA-SDLC-031, KA-SDLC-033, KA-SDLC-034, KA-SDLC-035, KA-SDLC-041, KA-SDLC-042, KA-SDLC-049, KA-SDLC-052, KA-SDLC-073, KA-SDLC-075, DATA-003, DATA-007, DATA-008, DATA-011, DATA-015, INFRA-020, HUMAN-010

---

**TECHNIQUES TO USE (ranked, by step):**

**Step 1 — Collect and analyze error signals:**
KA-SDLC-009 (Structured logging), KA-SDLC-012 (Error fingerprinting), KA-SDLC-035 (Runtime inspection), KA-CMI-046 (Long-running debugging session pattern), KA-SDLC-033 (Observability integration)

**Step 2 — Perform root cause analysis:**
KA-AGENT-002 (Conditional multi-stage prompting diagnosis→planning→recovery), KA-CMI-037 (Reflexion self-critique), KA-CODE-044 (Bug fixing combo), KA-META-045 (Chain-of-Verification)

**Step 3 — Generate repair candidates:**
KA-CODE-008 (Iterative repair loops), KA-CODE-009 (Automated Program Repair), KA-CODE-038 (Test-verified refactoring), KA-SDLC-031 (Agent-driven auto-fix PRs)

**Step 4 — Validate repairs:**
KA-CODE-010 (Automated validation), KA-SDLC-020 (Mutation testing), KA-CODE-004 (Systematic refactoring with test verification), KA-SDLC-002 (Self-healing pipeline validation)

**Step 5 — Execute rollback if needed:**
KA-SDLC-004 (Automated rollback mechanisms), DATA-008 (Expand-Contract migration pattern), KA-SDLC-041 (Self-healing pipeline), HUMAN-010 (Checkpoint-Based Execution)

**Step 6 — Apply healing and recovery:**
KA-SDLC-002 (Self-healing CI/CD), KA-SDLC-041 (Self-healing implementation), KA-SDLC-034 (Automated optimization), INFRA-020 (Circuit Breaker for External Services)

---

**CONSTRAINTS IN EFFECT:**
- KA-CODE-008 (Iteration limits 3-5 for repair loops)
- KA-CODE-033 (Must detect infinite repair loops)
- KA-CODE-010 (Requires comprehensive test coverage)
- KA-SDLC-058 (Coverage gates for repair validation)
- KA-SDLC-002 (80% manual intervention reduction target)
- KA-SDLC-004 (90% MTTR reduction target)

---

**TOOLS NEEDED:**
- KA-AGENT-033 (AgentOps frameworks)
- KA-SDLC-035 (Runtime inspection: pprof, debug endpoints)
- KA-META-046 (Dr.Fix API misuse repair)
- KA-SDLC-009 (Structured logging systems)
- DATA-003 (AI-Assisted Schema Evolution Risk Prediction)
- HUMAN-010 (Checkpoint-Based Execution)

---

**FAILURE MODES TO WATCH FOR:**
- KA-CODE-033 (Infinite repair loops without progress)
- KA-CODE-058 (LLM repair introduces subtle regressions)
- KA-SDLC-073 (Snowflake environments)
- KA-SDLC-075 (Silent failures)
- KA-SDLC-049 (In-context reward hacking)
- KA-AGENT-007 (Deadlock 2-7% in multi-agent)
- KA-AGENT-023 (Livelock detection)
- DATA-007 (Migration rollback failures 22%)
- DATA-011 (Migration in deployment blocking)

---

**TRANSITIONS:**

**Exit to P5 (Code Review) when:**
- Repairs generated and validated (KA-CODE-010)
- Ready for re-review after fixes

**Exit to P7 (Deployment) when:**
- Hotfix validated and ready for emergency deployment
- Self-healing completes successfully (KA-SDLC-041)

**Fallback to P3 (Implementation) when:**
- Repair requires significant reimplementation
- Root cause indicates design flaw

**Fallback to P2 (Planning) when:**
- Architecture-level issues discovered
- Requires task decomposition adjustment

---
---

## P7: Deployment & Release

**WHAT THE AGENT IS DOING:**
The agent manages the deployment pipeline using Infrastructure as Code, executes canary releases with automated rollback triggers, and coordinates multi-stage validation. This phase ensures safe production releases with minimal downtime.

---

**KNOWLEDGE ATOMS:**
KA-SDLC-001, KA-SDLC-003, KA-SDLC-004, KA-SDLC-005, KA-SDLC-006, KA-SDLC-008, KA-SDLC-023, KA-SDLC-027, KA-SDLC-040, KA-SDLC-042, KA-SDLC-055, KA-SDLC-059, KA-SDLC-062, KA-SDLC-063, KA-SDLC-065, KA-SDLC-066, KA-SDLC-067, KA-SDLC-068, KA-SDLC-079, KA-CODE-006, KA-CODE-012, KA-CODE-018, KA-CODE-028, KA-CODE-047, KA-META-007, KA-META-017, KA-META-032, KA-META-060, KA-AGENT-014, KA-AGENT-029, KA-CMI-027, DATA-001, DATA-002, DATA-005, DATA-008, DATA-009, DATA-010, INFRA-001, INFRA-002, INFRA-003, INFRA-004, INFRA-005, INFRA-006, INFRA-007, INFRA-008, INFRA-009, INFRA-010, INFRA-011, INFRA-012, INFRA-013, INFRA-017, INFRA-018, INFRA-019, INFRA-021, INFRA-022, HUMAN-007

---

**TECHNIQUES TO USE (ranked, by step):**

**Step 1 — Generate infrastructure definitions:**
KA-SDLC-042 (IaC generation workflow), KA-CODE-028 (Infrastructure as Code), INFRA-001 (IaC adoption), DATA-001 (Declarative Schema as Code)

**Step 2 — Validate infrastructure:**
KA-SDLC-006 (IaC reduces incidents 60%), KA-SDLC-042 (Security scanning), DATA-010 (API linting), DATA-003 (Schema evolution risk prediction)

**Step 3 — Build and optimize containers:**
KA-SDLC-063 (Docker containers), KA-SDLC-067 (Container build optimization), INFRA-007 (Model pre-loading), INFRA-019 (Warm Pool with Dynamic Scaling)

**Step 4 — Configure canary deployment:**
KA-SDLC-003 (Canary deployments), KA-SDLC-059 (Canary traffic progression), KA-SDLC-005 (Feature flags), KA-SDLC-055 (Blue/Green vs Canary tradeoff)

**Step 5 — Deploy with GitOps:**
KA-SDLC-065 (GitOps pattern), KA-SDLC-066 (Merge queue), KA-SDLC-068 (Observability as code), KA-SDLC-062 (Automated merging)

**Step 6 — Monitor deployment health:**
KA-SDLC-040 (Monitor metrics), KA-SDLC-059 (Automated rollback triggers), INFRA-012 (Kubernetes GPU scale framework), KA-SDLC-028 (RED/USE metrics)

**Step 7 — Execute progressive rollout:**
KA-SDLC-003 (Traffic progression 1%→5%→25%→50%→100%), KA-SDLC-004 (Automated rollback), HUMAN-007 (Risk-Tiered Auto-Approval)

---

**CONSTRAINTS IN EFFECT:**
- KA-SDLC-059 (Traffic progression: 1%→5%→25%→50%→100%)
- KA-SDLC-059 (Rollback triggers: error+2%, p99+20%, business-10%)
- KA-SDLC-056 (1-10% sampling for tracing)
- KA-META-007 (Budget enforcement per deployment)
- KA-AGENT-014 (Byzantine fault tolerance 3f+1)
- INFRA-012 (K8s GPU scaling tiers)
- INFRA-024 (Vanilla K8s fails at ~5,000 nodes)

---

**TOOLS NEEDED:**
- KA-SDLC-027 (Kubernetes)
- DATA-009 (Schema migration frameworks: Flyway, Liquibase, Prisma)
- INFRA-021 (Model serving: vLLM, TensorRT-LLM, Triton)
- INFRA-022 (Vector databases: Pinecone, Weaviate, Qdrant)
- KA-SDLC-065 (ArgoCD/Flux for GitOps)
- KA-SDLC-063 (Docker/BuildKit)

---

**FAILURE MODES TO WATCH FOR:**
- KA-SDLC-003 (Deployment incidents without canary)
- KA-SDLC-073 (Snowflake environments)
- KA-SDLC-079 (Manual approval bottleneck)
- KA-SDLC-048 (Metric cardinality explosion)
- KA-SDLC-075 (Silent failures)
- DATA-007 (Migration conflicts 34%, rollback failures 22%)
- DATA-011 (Migration blocking deployment)
- INFRA-009 (Cache inconsistency from TTL)
- KA-AGENT-029 (Single Coordinator Bottleneck)

---

**TRANSITIONS:**

**Exit to P8 (Maintenance) when:**
- 100% traffic on new version
- Health metrics stable for defined period
- No rollback triggers activated (KA-SDLC-059)

**Fallback to P6 (Debugging) when:**
- Rollback triggered (KA-SDLC-004)
- Error rate thresholds breached (KA-SDLC-059)
- Silent failures detected (KA-SDLC-075)

**Fallback to P5 (Code Review) when:**
- Infrastructure validation fails
- Security scan identifies issues

---
---

## P8: Maintenance & Monitoring

**WHAT THE AGENT IS DOING:**
The agent monitors production systems, responds to incidents, manages dependency updates, generates postmortems, and feeds learnings back into improvement loops. This phase ensures long-term system health and continuous optimization.

---

**KNOWLEDGE ATOMS:**
KA-SDLC-004, KA-SDLC-009, KA-SDLC-010, KA-SDLC-011, KA-SDLC-013, KA-SDLC-014, KA-SDLC-025, KA-SDLC-026, KA-SDLC-028, KA-SDLC-034, KA-SDLC-047, KA-SDLC-049, KA-SDLC-069, KA-SDLC-076, KA-SDLC-081, KA-SDLC-082, KA-SDLC-084, KA-SDLC-085, KA-SDLC-086, KA-SDLC-087, KA-CODE-015, KA-CODE-025, KA-CODE-035, KA-CMI-029, KA-CMI-030, KA-CMI-031, KA-CMI-033, KA-META-017, KA-META-032, KA-META-042, KA-META-043, KA-META-055, KA-META-057, KA-AGENT-010, KA-AGENT-011, KA-AGENT-028, KA-AGENT-040, DATA-005, DATA-007, DATA-017, INFRA-008, INFRA-014, INFRA-015, INFRA-016, INFRA-020, INFRA-023, HUMAN-001, HUMAN-003, HUMAN-013, HUMAN-014, HUMAN-015, HUMAN-016, HUMAN-017, HUMAN-018, HUMAN-019, HUMAN-021, HUMAN-022

---

**TECHNIQUES TO USE (ranked, by step):**

**Step 1 — Collect and analyze telemetry:**
KA-SDLC-009 (Structured logging), KA-SDLC-010 (Telemetry pipelines), KA-SDLC-011 (Distributed tracing), KA-SDLC-028 (RED/USE metrics), DATA-005 (Data drift detection), DATA-017 (Drift detection tools)

**Step 2 — Detect anomalies and incidents:**
KA-SDLC-028 (Metrics-based alerting), KA-SDLC-012 (Error fingerprinting), KA-SDLC-047 (Alert fatigue prevention), KA-AGENT-040 (Observability vs Performance tradeoff)

**Step 3 — Generate automated postmortems:**
KA-SDLC-013 (Automated postmortem generation), KA-SDLC-069 (Error pattern learning), KA-META-017 (Event-sourced audit ledger)

**Step 4 — Execute learning feedback loops:**
KA-SDLC-014 (Feedback loops improve reliability 40%), KA-SDLC-082 (Continuous learning from test results), KA-SDLC-069 (Error pattern learning workflow), KA-CMI-029 (Auto-learning memory systems)

**Step 5 — Manage dependencies and updates:**
KA-CODE-035 (Spec rot prevention), KA-CMI-031 (Stale embeddings prevention), KA-META-032 (AI-Native SBOM Extension), DATA-007 (Migration issue management)

**Step 6 — Optimize based on telemetry:**
KA-SDLC-034 (Automated optimization), KA-META-042 (Cost-to-Value Telemetry Loop), INFRA-008 (Semantic caching), KA-AGENT-011 (Fair-share scheduling)

**Step 7 — Calibrate HITL thresholds:**
HUMAN-001 (HITL intervention reduction), HUMAN-003 (Human overestimation calibration), HUMAN-015 (Escalation threshold drift prevention), HUMAN-013 (Approval fatigue prevention)

---

**CONSTRAINTS IN EFFECT:**
- KA-SDLC-014 (Closed feedback cycle requirement)
- KA-SDLC-076 (Feedback loop ignorance prevention)
- KA-CMI-030 (Catastrophic forgetting prevention)
- KA-CMI-031 (Embedding freshness monitoring)
- HUMAN-015 (Continuous threshold calibration)
- KA-META-055 (Governance anti-patterns avoidance)

---

**TOOLS NEEDED:**
- KA-SDLC-087 (OpenTelemetry semantic conventions)
- KA-SDLC-086 (MCP standardization)
- KA-AGENT-033 (AgentOps frameworks)
- DATA-017 (Drift detection: Great Expectations, WhyLabs, Evidently)
- HUMAN-009 (Apprise multi-channel notification)
- HUMAN-019 (HITL Framework implementations)

---

**FAILURE MODES TO WATCH FOR:**
- KA-SDLC-047 (Alert fatigue)
- KA-SDLC-076 (Feedback loop ignorance)
- KA-SDLC-084 (Trust without verification)
- KA-CODE-035 (Spec rot)
- KA-CMI-031 (Stale embeddings)
- HUMAN-013 (Approval fatigue spiral)
- HUMAN-014 (Context poisoning from human input)
- HUMAN-015 (Escalation threshold drift)
- HUMAN-016 (Notification spam)
- KA-META-055 (Governance anti-patterns)
- INFRA-014 (GPU over-provisioning)
- INFRA-015 (Synchronous external calls)

---

**TRANSITIONS:**

**Exit to P6 (Debugging) when:**
- Incident detected requiring response
- Error thresholds breached (KA-SDLC-028)
- Anomaly detected in telemetry (DATA-005)

**Exit to P2 (Planning) when:**
- Architecture improvement identified
- Major dependency update required
- Specification updates needed (KA-CODE-035)

**Fallback to P7 (Deployment) when:**
- Hotfix required for production
- Rollback executed (KA-SDLC-004)
- Configuration drift detected

**Continuous loop to self (P8):**
- Monitoring never stops
- Continuous optimization (KA-SDLC-034)
- Feedback loop maintenance (KA-SDLC-014)

---
---

## Cross-Phase Atom Index

The following atoms appear across multiple phases due to their cross-cutting nature:

| Atom ID | Type | Phases | Description |
|---------|------|--------|-------------|
| KA-META-001 | METRIC | P1-P8 | Cost modeling per task |
| KA-META-002 | TECHNIQUE | P3, P6 | Model cascade routing |
| KA-META-007 | CONSTRAINT | P1-P8 | Budget enforcement |
| KA-META-011 | FAILURE_MODE | P1-P8 | Prompt injection attacks |
| KA-META-012 | FAILURE_MODE | P3-P6 | Hallucination impact |
| KA-META-013 | TECHNIQUE | P3-P6 | Anti-hallucination guardrails |
| KA-META-016 | ANTI_PATTERN | P1-P8 | Security anti-patterns |
| KA-META-017 | RECIPE | P1-P8 | Governance compliance envelope |
| KA-META-020 | CONSTRAINT | P1-P8 | Security hardening checklist |
| KA-CMI-005 | FAILURE_MODE | P3-P7 | Context poisoning |
| KA-CMI-025 | TOOL | P1-P8 | Vector database selection |
| KA-CMI-038 | TECHNIQUE | P3-P7 | Multi-model adversarial reasoning |
| KA-CMI-052 | ANTI_PATTERN | P1-P8 | Context staleness |
| KA-AGENT-008 | TECHNIQUE | P1-P8 | Hierarchical multi-agent orchestration |
| KA-SDLC-009 | METRIC | P5-P8 | Structured logging |
| KA-SDLC-010 | METRIC | P5-P8 | Telemetry pipelines |
| KA-SDLC-014 | METRIC | P5-P8 | Feedback loops |
| KA-SDLC-025 | METRIC | P5-P8 | Agent performance scoring |
| KA-SDLC-026 | METRIC | P5-P8 | Trust scoring |
| HUMAN-002 | TECHNIQUE | All | Five-Level Autonomy Framework |

---

## Summary Statistics

| Phase | Primary Atoms | Cross-Cutting | Total Unique |
|-------|--------------|---------------|--------------|
| P1 Discovery | 35 | 85 | 120 |
| P2 Planning | 42 | 78 | 120 |
| P3 Implementation | 68 | 52 | 120 |
| P4 Testing | 54 | 45 | 99 |
| P5 Code Review | 48 | 38 | 86 |
| P6 Debugging | 39 | 42 | 81 |
| P7 Deployment | 52 | 35 | 87 |
| P8 Maintenance | 38 | 48 | 86 |

**Grand Total: 372 knowledge atoms mapped**

---

## Knowledge Gaps

1. **Optimal phase transition thresholds**: Quantitative confidence thresholds for phase transitions need empirical calibration
2. **Cross-phase budget allocation**: No established methodology for distributing token budgets across phases
3. **Phase-specific failure recovery**: Limited research on optimal rollback strategies per phase
4. **Parallel phase execution**: When can phases execute concurrently vs sequentially

---

## Sources

All atoms extracted from:
- `docs/distillation/prong1_meta_architecture.md` (60 atoms)
- `docs/distillation/prong1_sdlc_automation.md` (87 atoms)
- `docs/distillation/prong1_agent_orchestration.md` (42 atoms)
- `docs/distillation/prong1_context_memory_intelligence.md` (58 atoms)
- `docs/distillation/prong1_code_intelligence.md` (58 atoms)
- `docs/distillation/prong1_data_human.md` (67 atoms)

**Total: 372 knowledge atoms mapped to 8 SDLC phases**

---

*Generated: 2026-02-24*  
*Prong: 3 of 4 (Temporal Organization)*  
*Next: Prong 4 (Product Specification Mapping)*

**Prong**: 3 of 4 (Temporal/Phase Organization)  
**Input**: 372 knowledge atoms from Prong 1 extractions  
**Output**: Phase-based temporal organization with execution sequences  
**Date**: 2026-02-24  

---

## Executive Summary

This document maps 372 knowledge atoms to 8 SDLC phases (P1-P8) for the multi-agent autonomous coding platform. Each phase includes sequenced techniques, applicable constraints, required tools, failure modes to monitor, and transition conditions.

**Atom Distribution by Phase:**
| Phase | Primary Atoms | Cross-Cutting Atoms | Total |
|-------|--------------|---------------------|-------|
| P1 Discovery | 35 | 85 | 120 |
| P2 Planning | 42 | 78 | 120 |
| P3 Implementation | 68 | 52 | 120 |
| P4 Testing | 54 | 45 | 99 |
| P5 Code Review | 48 | 38 | 86 |
| P6 Debugging | 39 | 42 | 81 |
| P7 Deployment | 52 | 35 | 87 |
| P8 Maintenance | 38 | 48 | 86 |

*Note: Atoms appear in multiple phases when relevant to multiple stages*

---

## P1: Discovery & Onboarding

**WHAT THE AGENT IS DOING:**
The agent scans the codebase to build comprehensive understanding through semantic analysis, extracting architecture patterns, entrypoints, dependencies, and context. This phase establishes the foundation for all subsequent work by creating a knowledge graph of the codebase structure.

---

**KNOWLEDGE ATOMS:**
KA-META-018, KA-META-029, KA-META-038, KA-META-049, KA-META-053, KA-CMI-007, KA-CMI-008, KA-CMI-013, KA-CMI-016, KA-CMI-019, KA-CMI-021, KA-CMI-023, KA-CMI-025, KA-CMI-052, KA-CODE-002, KA-CODE-003, KA-CODE-020, KA-CODE-021, KA-CODE-022, KA-CODE-023, KA-CODE-024, KA-CODE-030, KA-CODE-040, KA-CODE-042, KA-CODE-048, KA-CODE-049, KA-CODE-051, KA-CODE-052, KA-CODE-057, KA-AGENT-006, KA-AGENT-008, KA-AGENT-015, KA-AGENT-024, KA-AGENT-027, KA-SDLC-009, KA-SDLC-028, INFRA-011, HUMAN-008

---

**TECHNIQUES TO USE (ranked, by step):**

**Step 1 — Initialize codebase access and cold start mitigation:**
KA-META-018 (Cold start mitigation), KA-CMI-025 (Vector database selection), KA-CODE-051 (Zencoder Repo Grokking), KA-CODE-052 (Augment Context Engine)

**Step 2 — Parse and index codebase structure:**
KA-CMI-007 (Semantic chunking), KA-CMI-008 (Code-aware chunking overlap), KA-CMI-016 (Multi-representation fusion AST+CFG+DFG), KA-CMI-019 (Sourcegraph/Kythe indexing), KA-CODE-040 (Tree-sitter incremental parsing)

**Step 3 — Identify entrypoints and active code paths:**
KA-CODE-003 (Entrypoint-first exploration), KA-CODE-020 (Call chain verification), KA-CODE-021 (Static call graph precision), KA-CODE-023 (Design pattern detection)

**Step 4 — Build dependency and relationship graphs:**
KA-CMI-021 (SSA form for data flow), KA-CODE-022 (Incremental dependency tracking), KA-CODE-030 (Dual-database architecture), KA-CODE-042 (Entrypoint+Semantic+Pattern+DualDB combo)

**Step 5 — Extract architectural patterns and conventions:**
KA-CODE-023 (Design pattern detection), KA-META-029 (Semantic Codebase Understanding), KA-META-049 (Progressive Disclosure Architecture), KA-AGENT-027 (System-Theoretic Agent Decomposition)

**Step 6 — Prioritize files by relevance:**
KA-CODE-002 (Semantic-guided traversal), KA-CODE-024 (Intelligent file prioritization), KA-CMI-013 (Hybrid search vector+BM25)

**Step 7 — Cache and store grokked context:**
KA-CMI-052 (Context staleness prevention), KA-CODE-048 (Stale exploration cache failure prevention), KA-CMI-023 (Incremental representation updates)

---

**CONSTRAINTS IN EFFECT:**
- KA-META-053 (Complexity scoring metrics limitations)
- KA-CODE-041 (Code property graph computational overhead)
- KA-CODE-057 (Unbounded exploration scope prevention)
- KA-CMI-052 (Context staleness thresholds)
- INFRA-024 (Kubernetes node scaling limits)

---

**TOOLS NEEDED:**
- KA-CMI-019 (Sourcegraph/Kythe/LSIF)
- KA-CMI-025 (Vector database - Pinecone/Weaviate/Qdrant)
- KA-CODE-040 (Tree-sitter)
- KA-CODE-051 (Zencoder Repo Grokking)
- KA-CODE-052 (Augment Context Engine MCP)
- KA-SDLC-028 (Kubernetes)

---

**FAILURE MODES TO WATCH FOR:**
- KA-META-038 (System design anti-patterns: Shallow repo understanding)
- KA-CODE-031 (Static-only dependency analysis misses)
- KA-CODE-032 (Shallow call graph analysis)
- KA-CODE-048 (Stale exploration cache)
- KA-CODE-049 (Pattern blindness)
- KA-CODE-057 (Unbounded exploration scope)
- KA-AGENT-024 (Monolithic FM-Centric Design)
- KA-CMI-053 (Blind code comment trust)

---

**TRANSITIONS:**

**Exit to P2 (Planning) when:**
- Entrypoints identified and catalogued (KA-CODE-003)
- Dependency graph built with >85% coverage (KA-CODE-022)
- Pattern library extracted (KA-CODE-023)
- Vector index populated and searchable (KA-CMI-025)
- Confidence score >0.8 on codebase understanding

**Fallback to P1 (self) when:**
- Stale cache detected (KA-CMI-052)
- Significant code changes invalidate grokking (>20% files changed)
- Pattern detection fails (KA-CODE-049)
- Context poisoning detected (KA-CMI-005)

---
---

## P2: Planning & Design

**WHAT THE AGENT IS DOING:**
The agent decomposes tasks into atomic subtasks, sequences dependencies, creates specifications, and designs implementation approaches. This phase translates intent into actionable plans with clear success criteria and rollback strategies.

---

**KNOWLEDGE ATOMS:**
KA-META-009, KA-META-026, KA-META-027, KA-META-029, KA-META-038, KA-META-044, KA-META-048, KA-META-050, KA-META-053, KA-META-054, KA-AGENT-002, KA-AGENT-006, KA-AGENT-008, KA-AGENT-015, KA-AGENT-019, KA-AGENT-020, KA-AGENT-026, KA-AGENT-030, KA-AGENT-031, KA-AGENT-036, KA-AGENT-037, KA-AGENT-038, KA-CMI-009, KA-CMI-010, KA-CMI-034, KA-CMI-035, KA-CMI-048, KA-CODE-014, KA-CODE-029, KA-CODE-035, KA-CODE-036, KA-CODE-054, KA-CODE-055, KA-SDLC-018, KA-SDLC-032, KA-SDLC-061, DATA-001, DATA-004, DATA-012, DATA-013, DATA-014, DATA-018, HUMAN-002, HUMAN-020

---

**TECHNIQUES TO USE (ranked, by step):**

**Step 1 — Parse and clarify requirements:**
KA-AGENT-006 (Clarification capabilities), KA-META-044 (Intent verification checkpoint), HUMAN-008 (Structured follow-up questions), KA-CODE-029 (Intent-driven development)

**Step 2 — Decompose task into atomic subtasks:**
KA-AGENT-020 (Optimal task decomposition depth), KA-AGENT-031 (Atomic Task Creation), KA-AGENT-036 (Hierarchical decomposition), KA-AGENT-037 (AdaptOrch topology routing), KA-META-039 (Budget-Aware Task Decomposition)

**Step 3 — Analyze dependencies and build task graph:**
KA-AGENT-019 (Async DAG execution), KA-AGENT-030 (Cycle detection in task graphs), KA-CODE-022 (Incremental dependency tracking), KA-AGENT-016 (Worktree isolation)

**Step 4 — Select architectural pattern:**
KA-META-048 (Pattern Selection Guide), KA-META-050 (Key architectural tradeoffs), KA-META-026 (Spec-Driven vs Intent-Driven), KA-AGENT-027 (System-Theoretic Decomposition)

**Step 5 — Create specifications:**
KA-META-009 (Spec-driven 4-phase workflow), KA-META-027 (Bidirectional Specifications), KA-CODE-014 (Scope boundary documentation), KA-CODE-036 (Over-specification prevention), DATA-004 (Contract-Aware Code Generation)

**Step 6 — Allocate budgets and resources:**
KA-META-039 (Budget-Aware Task Decomposition), KA-META-054 (Complexity Budget Framework), KA-CMI-009 (Context window partitioning), KA-META-001 (Cost modeling per task)

**Step 7 — Plan validation approach:**
KA-SDLC-018 (BDD with Gherkin), KA-SDLC-032 (TDD red-green-refactor), KA-CODE-005 (TDD defect reduction), KA-CMI-034 (Chain-of-Thought for planning)

---

**CONSTRAINTS IN EFFECT:**
- KA-AGENT-020 (Optimal decomposition: 2-3 levels simple, 5-7 complex)
- KA-META-054 (Complexity Budget Framework)
- KA-CODE-014 (Scope creep prevention)
- KA-CODE-036 (Over-specification limits)
- KA-AGENT-030 (3-8% task graphs contain cycles)
- DATA-012 (Shared database anti-pattern)
- DATA-013 (God table anti-pattern)

---

**TOOLS NEEDED:**
- KA-AGENT-037 (AdaptOrch topology routing)
- KA-META-006 (Cost modeling frameworks)
- DATA-001 (Declarative Schema as Code tools)
- HUMAN-002 (Five-Level Agent Autonomy Framework)
- KA-CMI-025 (Vector DB for context retrieval)

---

**FAILURE MODES TO WATCH FOR:**
- KA-META-038 (Vibe Coding anti-pattern)
- KA-META-053 (Complexity metrics limitations)
- KA-AGENT-026 (Over-Delegation)
- KA-AGENT-030 (Task graph cycles)
- KA-CODE-035 (Spec rot)
- KA-CODE-036 (Over-specification)
- KA-CODE-054 (Specification rigidity)
- DATA-012 (Shared database coupling)
- DATA-013 (God table accumulation)
- DATA-014 (Implicit schema)

---

**TRANSITIONS:**

**Exit to P3 (Implementation) when:**
- Task decomposition complete with 2-7 depth levels (KA-AGENT-020)
- Specifications created with acceptance criteria (KA-META-009)
- Dependency graph validated (no cycles) (KA-AGENT-030)
- Budgets allocated per subtask (KA-META-039)
- Test plan defined (KA-SDLC-032)

**Fallback to P1 (Discovery) when:**
- Insufficient codebase understanding for task (KA-CODE-057)
- Missing dependencies detected during planning
- Context stale (>threshold) (KA-CMI-052)

**Fallback to self (P2) when:**
- Cycle detected in task graph (KA-AGENT-030)
- Scope creep detected (KA-CODE-014)
- Specification conflicts require replanning

---
---

## P3: Implementation

**WHAT THE AGENT IS DOING:**
The agent generates code following specifications while managing context windows, applying patterns, and maintaining style consistency. This phase produces actual code changes with continuous validation and compression.

---

**KNOWLEDGE ATOMS:**
KA-META-002, KA-META-003, KA-META-004, KA-META-009, KA-META-010, KA-META-013, KA-META-018, KA-META-019, KA-META-022, KA-META-023, KA-META-034, KA-META-039, KA-META-040, KA-META-041, KA-META-045, KA-META-047, KA-META-049, KA-META-058, KA-CMI-001, KA-CMI-002, KA-CMI-003, KA-CMI-004, KA-CMI-009, KA-CMI-010, KA-CMI-012, KA-CMI-014, KA-CMI-015, KA-CMI-034, KA-CMI-035, KA-CMI-036, KA-CMI-037, KA-CMI-040, KA-CMI-041, KA-CMI-042, KA-CMI-043, KA-CMI-044, KA-CMI-048, KA-CMI-049, KA-CMI-050, KA-CMI-051, KA-CMI-054, KA-CODE-005, KA-CODE-013, KA-CODE-016, KA-CODE-025, KA-CODE-027, KA-CODE-029, KA-CODE-037, KA-CODE-046, KA-CODE-047, KA-AGENT-002, KA-AGENT-031, KA-SDLC-029, KA-SDLC-044, DATA-002, DATA-004, DATA-006, HUMAN-004, HUMAN-005, HUMAN-010, INFRA-018

---

**TECHNIQUES TO USE (ranked, by step):**

**Step 1 — Retrieve relevant context:**
KA-CMI-010 (Task-conditioned context selection), KA-CMI-013 (Hybrid search), KA-CMI-003 (U-shaped context placement), KA-META-040 (Retrieval Compression Pipeline)

**Step 2 — Compress context to fit window:**
KA-CMI-001 (LLMLingua prompt compression), KA-CMI-002 (Selective Context), KA-CMI-012 (LLM summarization + observation masking), KA-CMI-014 (Context compression tradeoffs), KA-META-004 (Token efficiency techniques)

**Step 3 — Apply reasoning paradigm:**
KA-CMI-034 (Chain-of-Thought), KA-CMI-035 (Tree-of-Thought), KA-CMI-036 (Graph-of-Thought), KA-CMI-048 (Reasoning paradigm tradeoffs), KA-META-045 (Chain-of-Verification)

**Step 4 — Generate code with pattern adherence:**
KA-META-009 (Spec-driven workflow), KA-CODE-046 (Specification-driven generation combo), KA-CODE-047 (API development combo), KA-CODE-029 (Intent-driven development), KA-CODE-016 (Automated code formatting)

**Step 5 — Apply model cascade for efficiency:**
KA-META-002 (Model cascade routing), KA-META-010 (Provider cost comparison), KA-META-019 (Skill/Agent enablement), HUMAN-004 (Cascaded LLM decision)

**Step 6 — Validate generated code:**
KA-CMI-037 (Reflexion self-critique), KA-CMI-038 (Multi-model adversarial reasoning), KA-CMI-042 (Confidence scoring), KA-CMI-044 (Intent verification), KA-META-013 (Anti-hallucination guardrails)

**Step 7 — Apply normalization and budgets:**
KA-CODE-037 (AI code normalization), KA-CODE-011 (Complexity budgets), KA-CODE-013 (AI slop reduction), KA-META-039 (Budget-Aware decomposition)

---

**CONSTRAINTS IN EFFECT:**
- KA-META-003 (Semantic caching thresholds)
- KA-META-004 (Token efficiency targets)
- KA-META-007 (Budget enforcement mechanisms)
- KA-CMI-004 (<15% context waste target)
- KA-CMI-009 (20% system / 30% history / 40% retrieval / 10% working)
- KA-CMI-041 (Temperature 0.3-0.5 for coding)
- KA-CMI-043 (Max 2-3 refinement iterations)
- KA-CODE-011 (Complexity budget enforcement)
- KA-CMI-015 (No context stuffing)

---

**TOOLS NEEDED:**
- KA-META-002 (Model cascade router)
- KA-META-046 (Anti-hallucination tools: LangChain Guardrails, LM-Polygraph)
- KA-CMI-011 (Augment Context Engine MCP)
- KA-CMI-025 (Vector database)
- INFRA-018 (Tiered Model Serving)
- HUMAN-005 (Confidence-Calibrated Escalation)

---

**FAILURE MODES TO WATCH FOR:**
- KA-META-011 (Prompt injection attacks)
- KA-META-012 (Hallucination: fabricated packages, vulnerabilities)
- KA-META-021 (Economic optimization anti-patterns)
- KA-CMI-005 (Context poisoning)
- KA-CMI-006 (Wake-up prompts don't work)
- KA-CMI-015 (Context stuffing)
- KA-CMI-030 (Catastrophic forgetting)
- KA-CMI-040 (Echo chamber self-review)
- KA-CMI-043 (Infinite refinement loops)
- KA-CODE-013 (AI slop: 30% more abstraction, 20% verbosity)
- KA-CODE-033 (Infinite repair loops)
- KA-SDLC-029 (LLM tests miss boundary conditions)

---

**TRANSITIONS:**

**Exit to P4 (Testing) when:**
- Code generates successfully with syntax validation
- Complexity budgets satisfied (KA-CODE-011)
- Confidence score >threshold (KA-CMI-042)
- Self-critique passes (KA-CMI-037)
- Specifications met (KA-META-009)

**Exit to P5 (Code Review) when:**
- Code passes local validation
- Ready for adversarial review (KA-CMI-038)

**Fallback to P2 (Planning) when:**
- Implementation reveals specification gaps
- Complexity budget exceeded (KA-CODE-011)
- Context poisoning detected (KA-CMI-005)
- Confidence below threshold requiring replanning

**Fallback to P1 (Discovery) when:**
- Missing critical codebase understanding
- Dependencies not fully grokked

---
---

## P4: Testing & Verification

**WHAT THE AGENT IS DOING:**
The agent generates and executes tests across multiple levels (unit, integration, E2E), validates behavior against specifications, applies mutation testing, and ensures sad path coverage. This phase provides confidence for deployment decisions.

---

**KNOWLEDGE ATOMS:**
KA-SDLC-015, KA-SDLC-016, KA-SDLC-017, KA-SDLC-018, KA-SDLC-019, KA-SDLC-020, KA-SDLC-021, KA-SDLC-022, KA-SDLC-023, KA-SDLC-024, KA-SDLC-029, KA-SDLC-030, KA-SDLC-032, KA-SDLC-036, KA-SDLC-037, KA-SDLC-038, KA-SDLC-039, KA-SDLC-043, KA-SDLC-044, KA-SDLC-046, KA-SDLC-051, KA-SDLC-052, KA-SDLC-053, KA-SDLC-056, KA-SDLC-057, KA-SDLC-058, KA-SDLC-060, KA-SDLC-070, KA-SDLC-071, KA-SDLC-072, KA-SDLC-074, KA-SDLC-077, KA-SDLC-078, KA-SDLC-080, KA-SDLC-082, KA-SDLC-083, KA-SDLC-084, KA-CODE-004, KA-CODE-005, KA-CODE-007, KA-CODE-008, KA-CODE-009, KA-CODE-010, KA-CODE-018, KA-CODE-032, KA-CODE-033, KA-CODE-034, KA-CODE-038, KA-CODE-044, KA-CODE-045, KA-CMI-038, KA-CMI-039, KA-AGENT-004, KA-AGENT-018, KA-AGENT-021, KA-AGENT-034, KA-META-013, KA-META-022, KA-META-023, KA-META-024, DATA-006, DATA-016

---

**TECHNIQUES TO USE (ranked, by step):**

**Step 1 — Generate test cases:**
KA-SDLC-044 (AI agent test generation workflow), KA-SDLC-018 (BDD with Gherkin), KA-CODE-005 (TDD approach), KA-SDLC-029 (LLM-generated test coverage)

**Step 2 — Ensure test pyramid proportions:**
KA-SDLC-057 (70% unit / 20% integration / 10% E2E), KA-SDLC-017 (E2E cost tradeoff), KA-SDLC-015 (Unit test isolation)

**Step 3 — Generate sad path coverage:**
KA-CODE-007 (60-70% failures from untested error paths), KA-CODE-034 (Happy path bias prevention), KA-SDLC-046 (Sad path testing requirements), KA-SDLC-030 (Fuzzing for vulnerabilities)

**Step 4 — Execute multi-stage validation:**
KA-SDLC-036 (Multi-stage validation gates), KA-SDLC-060 (Multi-stage validation pipeline), KA-AGENT-034 (Multi-Stage Validation Pipeline), KA-CODE-044 (Iterative repair + test-verified combo)

**Step 5 — Apply process supervision:**
KA-SDLC-037 (Process supervision), KA-SDLC-038 (Four-level testing hierarchy), KA-SDLC-050 (Outcome-only validation prevention)

**Step 6 — Measure coverage and quality:**
KA-SDLC-024 (80% line coverage minimum), KA-SDLC-058 (Coverage threshold constraint), KA-SDLC-020 (Mutation testing >80%), KA-SDLC-043 (Test quality improvement loop)

**Step 7 — Validate determinism:**
KA-SDLC-039 (Determinism-first testing), KA-SDLC-051 (Temperature 0.0-0.3 for reproducibility)

---

**CONSTRAINTS IN EFFECT:**
- KA-SDLC-057 (Test pyramid: 70/20/10 ratio)
- KA-SDLC-058 (80% line coverage minimum)
- KA-SDLC-020 (Mutation score >80%)
- KA-SDLC-024 (MC/DC for safety-critical)
- KA-SDLC-056 (1-10% sampling rate for tracing)
- KA-CODE-007 (Must test sad paths)
- KA-SDLC-053 (Guardrails vs flexibility balance)

---

**TOOLS NEEDED:**
- KA-SDLC-080 (MCP for tool abstraction testing)
- KA-META-046 (Anti-hallucination tools)
- DATA-016 (Synthetic data generation tools)
- KA-SDLC-070 (Contract testing with Pact)
- KA-SDLC-071 (LLM-as-judge validation)
- KA-SDLC-072 (Guardrails AI, Outlines, LMQL)

---

**FAILURE MODES TO WATCH FOR:**
- KA-SDLC-046 (Happy path bias: 80% AI tests cover happy paths)
- KA-SDLC-074 (Test interdependence)
- KA-SDLC-077 (Mock overuse)
- KA-SDLC-078 (Coverage gaming)
- KA-SDLC-084 (Trust without verification)
- KA-CODE-033 (Infinite repair loops)
- KA-CODE-034 (Happy path bias)
- KA-SDLC-049 (In-context reward hacking)
- KA-SDLC-050 (Outcome-only validation)

---

**TRANSITIONS:**

**Exit to P5 (Code Review) when:**
- All validation gates pass (KA-SDLC-036)
- Coverage thresholds met (KA-SDLC-058)
- Mutation score >80% (KA-SDLC-020)
- Determinism verified (KA-SDLC-039)

**Exit to P6 (Debugging) when:**
- Tests fail requiring repair (KA-CODE-008)
- Mutation testing identifies weak areas (KA-SDLC-043)

**Fallback to P3 (Implementation) when:**
- Coverage gaps require additional code (KA-SDLC-044)
- Sad paths not testable with current implementation (KA-CODE-007)

---
---

## P5: Code Review

**WHAT THE AGENT IS DOING:**
The agent performs multi-faceted code review using adversarial patterns, semantic diffing, security analysis, and style verification. This phase ensures code quality, security, and adherence to standards before merge.

---

**KNOWLEDGE ATOMS:**
KA-AGENT-004, KA-AGENT-005, KA-AGENT-018, KA-AGENT-021, KA-AGENT-035, KA-CMI-020, KA-CMI-038, KA-CMI-040, KA-CMI-047, KA-CODE-004, KA-CODE-011, KA-CODE-016, KA-CODE-020, KA-CODE-025, KA-CODE-038, KA-CODE-043, KA-CODE-045, KA-META-013, KA-META-015, KA-META-016, KA-META-022, KA-META-023, KA-META-024, KA-META-034, KA-META-035, KA-META-046, KA-META-047, KA-SDLC-009, KA-SDLC-010, KA-SDLC-012, KA-SDLC-025, KA-SDLC-026, KA-SDLC-035, KA-SDLC-069, KA-SDLC-071, DATA-010, HUMAN-011, HUMAN-012

---

**TECHNIQUES TO USE (ranked, by step):**

**Step 1 — Perform semantic diff analysis:**
KA-CMI-020 (Semantic diffs), KA-CODE-043 (Refactoring impact analysis combo), KA-CMI-016 (Multi-representation fusion for understanding)

**Step 2 — Execute adversarial review:**
KA-AGENT-005 (Adversarial review patterns), KA-AGENT-018 (Multi-agent QA swarms), KA-CMI-038 (Multi-model adversarial reasoning), KA-AGENT-004 (Mixture-of-Agents), KA-META-015 (Hallucination defense tradeoffs)

**Step 3 — Apply security scanning:**
KA-META-022 (Static analysis for hallucination), KA-META-023 (RAG for Code with Hybrid Retrieval), KA-META-016 (Security hardening checklist), KA-META-035 (Layered Guardrail Envelope), KA-CMI-017 (Code Property Graphs for security), HUMAN-012 (AI deception detection)

**Step 4 — Validate style and patterns:**
KA-CODE-016 (Automated code formatting), KA-CODE-011 (Complexity budgets), KA-CODE-025 (Readability improvements), KA-CODE-038 (Test-verified refactoring), KA-META-034 (Evidence-First Action Gating)

**Step 5 — Calculate quality scores:**
KA-SDLC-025 (Agent performance scoring), KA-SDLC-026 (Trust scoring), KA-AGENT-021 (Agent GPA framework), KA-META-013 (Anti-hallucination effectiveness)

**Step 6 — Generate review feedback:**
KA-CMI-047 (Multi-agent code review pattern), HUMAN-011 (HITL in code review), KA-SDLC-012 (Error fingerprinting)

---

**CONSTRAINTS IN EFFECT:**
- KA-CODE-011 (Complexity budgets enforced)
- KA-META-016 (Security hardening checklist)
- KA-META-020 (Security hardening requirements)
- KA-META-034 (Evidence threshold for high-impact actions)
- DATA-010 (API linting breaking change prevention)
- KA-SDLC-053 (Guardrails vs flexibility tradeoff)

---

**TOOLS NEEDED:**
- KA-META-046 (Anti-hallucination tools)
- KA-CMI-017 (Joern CPG platform)
- KA-CMI-019 (Sourcegraph)
- KA-AGENT-021 (Agent GPA framework)
- KA-SDLC-071 (LLM-as-judge)
- DATA-010 (API linting tools)

---

**FAILURE MODES TO WATCH FOR:**
- KA-META-012 (Hallucination impact: 40-45% vulnerabilities)
- KA-META-016 (Security anti-patterns)
- KA-CMI-040 (Echo chamber self-review)
- KA-CODE-049 (Pattern blindness in review)
- HUMAN-012 (AI deception bypassing HITL)
- HUMAN-023 (Review fatigue overwhelming humans)
- KA-SDLC-084 (Trust without verification)

---

**TRANSITIONS:**

**Exit to P6 (Debugging) when:**
- Issues found requiring repair (KA-CODE-008)
- Security vulnerabilities detected (KA-META-012)
- Quality scores below threshold (KA-SDLC-025)

**Exit to P7 (Deployment) when:**
- All review checks pass
- Adversarial consensus reached (KA-AGENT-005)
- Quality scores meet thresholds (KA-SDLC-025)
- Security scan clean (KA-META-016)

**Fallback to P3 (Implementation) when:**
- Fundamental design issues found
- Pattern violations requiring rewrite (KA-CODE-016)
- Complexity budget exceeded (KA-CODE-011)

---
---

## P6: Debugging & Error Recovery

**WHAT THE AGENT IS DOING:**
The agent diagnoses root causes of failures, generates repairs, validates fixes through testing, and manages rollback if needed. This phase handles both development-time debugging and production incident response.

---

**KNOWLEDGE ATOMS:**
KA-AGENT-002, KA-AGENT-033, KA-CMI-037, KA-CMI-046, KA-CODE-008, KA-CODE-009, KA-CODE-010, KA-CODE-012, KA-CODE-033, KA-CODE-038, KA-CODE-044, KA-CODE-055, KA-CODE-058, KA-META-002, KA-META-018, KA-META-045, KA-SDLC-001, KA-SDLC-002, KA-SDLC-004, KA-SDLC-006, KA-SDLC-007, KA-SDLC-009, KA-SDLC-012, KA-SDLC-013, KA-SDLC-020, KA-SDLC-031, KA-SDLC-033, KA-SDLC-034, KA-SDLC-035, KA-SDLC-041, KA-SDLC-042, KA-SDLC-049, KA-SDLC-052, KA-SDLC-073, KA-SDLC-075, DATA-003, DATA-007, DATA-008, DATA-011, DATA-015, INFRA-020, HUMAN-010

---

**TECHNIQUES TO USE (ranked, by step):**

**Step 1 — Collect and analyze error signals:**
KA-SDLC-009 (Structured logging), KA-SDLC-012 (Error fingerprinting), KA-SDLC-035 (Runtime inspection), KA-CMI-046 (Long-running debugging session pattern), KA-SDLC-033 (Observability integration)

**Step 2 — Perform root cause analysis:**
KA-AGENT-002 (Conditional multi-stage prompting diagnosis→planning→recovery), KA-CMI-037 (Reflexion self-critique), KA-CODE-044 (Bug fixing combo), KA-META-045 (Chain-of-Verification)

**Step 3 — Generate repair candidates:**
KA-CODE-008 (Iterative repair loops), KA-CODE-009 (Automated Program Repair), KA-CODE-038 (Test-verified refactoring), KA-SDLC-031 (Agent-driven auto-fix PRs)

**Step 4 — Validate repairs:**
KA-CODE-010 (Automated validation), KA-SDLC-020 (Mutation testing), KA-CODE-004 (Systematic refactoring with test verification), KA-SDLC-002 (Self-healing pipeline validation)

**Step 5 — Execute rollback if needed:**
KA-SDLC-004 (Automated rollback mechanisms), DATA-008 (Expand-Contract migration pattern), KA-SDLC-041 (Self-healing pipeline), HUMAN-010 (Checkpoint-Based Execution)

**Step 6 — Apply healing and recovery:**
KA-SDLC-002 (Self-healing CI/CD), KA-SDLC-041 (Self-healing implementation), KA-SDLC-034 (Automated optimization), INFRA-020 (Circuit Breaker for External Services)

---

**CONSTRAINTS IN EFFECT:**
- KA-CODE-008 (Iteration limits 3-5 for repair loops)
- KA-CODE-033 (Must detect infinite repair loops)
- KA-CODE-010 (Requires comprehensive test coverage)
- KA-SDLC-058 (Coverage gates for repair validation)
- KA-SDLC-002 (80% manual intervention reduction target)
- KA-SDLC-004 (90% MTTR reduction target)

---

**TOOLS NEEDED:**
- KA-AGENT-033 (AgentOps frameworks)
- KA-SDLC-035 (Runtime inspection: pprof, debug endpoints)
- KA-META-046 (Dr.Fix API misuse repair)
- KA-SDLC-009 (Structured logging systems)
- DATA-003 (AI-Assisted Schema Evolution Risk Prediction)
- HUMAN-010 (Checkpoint-Based Execution)

---

**FAILURE MODES TO WATCH FOR:**
- KA-CODE-033 (Infinite repair loops without progress)
- KA-CODE-058 (LLM repair introduces subtle regressions)
- KA-SDLC-073 (Snowflake environments)
- KA-SDLC-075 (Silent failures)
- KA-SDLC-049 (In-context reward hacking)
- KA-AGENT-007 (Deadlock 2-7% in multi-agent)
- KA-AGENT-023 (Livelock detection)
- DATA-007 (Migration rollback failures 22%)
- DATA-011 (Migration in deployment blocking)

---

**TRANSITIONS:**

**Exit to P5 (Code Review) when:**
- Repairs generated and validated (KA-CODE-010)
- Ready for re-review after fixes

**Exit to P7 (Deployment) when:**
- Hotfix validated and ready for emergency deployment
- Self-healing completes successfully (KA-SDLC-041)

**Fallback to P3 (Implementation) when:**
- Repair requires significant reimplementation
- Root cause indicates design flaw

**Fallback to P2 (Planning) when:**
- Architecture-level issues discovered
- Requires task decomposition adjustment

---
---

## P7: Deployment & Release

**WHAT THE AGENT IS DOING:**
The agent manages the deployment pipeline using Infrastructure as Code, executes canary releases with automated rollback triggers, and coordinates multi-stage validation. This phase ensures safe production releases with minimal downtime.

---

**KNOWLEDGE ATOMS:**
KA-SDLC-001, KA-SDLC-003, KA-SDLC-004, KA-SDLC-005, KA-SDLC-006, KA-SDLC-008, KA-SDLC-023, KA-SDLC-027, KA-SDLC-040, KA-SDLC-042, KA-SDLC-055, KA-SDLC-059, KA-SDLC-062, KA-SDLC-063, KA-SDLC-065, KA-SDLC-066, KA-SDLC-067, KA-SDLC-068, KA-SDLC-079, KA-CODE-006, KA-CODE-012, KA-CODE-018, KA-CODE-028, KA-CODE-047, KA-META-007, KA-META-017, KA-META-032, KA-META-060, KA-AGENT-014, KA-AGENT-029, KA-CMI-027, DATA-001, DATA-002, DATA-005, DATA-008, DATA-009, DATA-010, INFRA-001, INFRA-002, INFRA-003, INFRA-004, INFRA-005, INFRA-006, INFRA-007, INFRA-008, INFRA-009, INFRA-010, INFRA-011, INFRA-012, INFRA-013, INFRA-017, INFRA-018, INFRA-019, INFRA-021, INFRA-022, HUMAN-007

---

**TECHNIQUES TO USE (ranked, by step):**

**Step 1 — Generate infrastructure definitions:**
KA-SDLC-042 (IaC generation workflow), KA-CODE-028 (Infrastructure as Code), INFRA-001 (IaC adoption), DATA-001 (Declarative Schema as Code)

**Step 2 — Validate infrastructure:**
KA-SDLC-006 (IaC reduces incidents 60%), KA-SDLC-042 (Security scanning), DATA-010 (API linting), DATA-003 (Schema evolution risk prediction)

**Step 3 — Build and optimize containers:**
KA-SDLC-063 (Docker containers), KA-SDLC-067 (Container build optimization), INFRA-007 (Model pre-loading), INFRA-019 (Warm Pool with Dynamic Scaling)

**Step 4 — Configure canary deployment:**
KA-SDLC-003 (Canary deployments), KA-SDLC-059 (Canary traffic progression), KA-SDLC-005 (Feature flags), KA-SDLC-055 (Blue/Green vs Canary tradeoff)

**Step 5 — Deploy with GitOps:**
KA-SDLC-065 (GitOps pattern), KA-SDLC-066 (Merge queue), KA-SDLC-068 (Observability as code), KA-SDLC-062 (Automated merging)

**Step 6 — Monitor deployment health:**
KA-SDLC-040 (Monitor metrics), KA-SDLC-059 (Automated rollback triggers), INFRA-012 (Kubernetes GPU scale framework), KA-SDLC-028 (RED/USE metrics)

**Step 7 — Execute progressive rollout:**
KA-SDLC-003 (Traffic progression 1%→5%→25%→50%→100%), KA-SDLC-004 (Automated rollback), HUMAN-007 (Risk-Tiered Auto-Approval)

---

**CONSTRAINTS IN EFFECT:**
- KA-SDLC-059 (Traffic progression: 1%→5%→25%→50%→100%)
- KA-SDLC-059 (Rollback triggers: error+2%, p99+20%, business-10%)
- KA-SDLC-056 (1-10% sampling for tracing)
- KA-META-007 (Budget enforcement per deployment)
- KA-AGENT-014 (Byzantine fault tolerance 3f+1)
- INFRA-012 (K8s GPU scaling tiers)
- INFRA-024 (Vanilla K8s fails at ~5,000 nodes)

---

**TOOLS NEEDED:**
- KA-SDLC-027 (Kubernetes)
- DATA-009 (Schema migration frameworks: Flyway, Liquibase, Prisma)
- INFRA-021 (Model serving: vLLM, TensorRT-LLM, Triton)
- INFRA-022 (Vector databases: Pinecone, Weaviate, Qdrant)
- KA-SDLC-065 (ArgoCD/Flux for GitOps)
- KA-SDLC-063 (Docker/BuildKit)

---

**FAILURE MODES TO WATCH FOR:**
- KA-SDLC-003 (Deployment incidents without canary)
- KA-SDLC-073 (Snowflake environments)
- KA-SDLC-079 (Manual approval bottleneck)
- KA-SDLC-048 (Metric cardinality explosion)
- KA-SDLC-075 (Silent failures)
- DATA-007 (Migration conflicts 34%, rollback failures 22%)
- DATA-011 (Migration blocking deployment)
- INFRA-009 (Cache inconsistency from TTL)
- KA-AGENT-029 (Single Coordinator Bottleneck)

---

**TRANSITIONS:**

**Exit to P8 (Maintenance) when:**
- 100% traffic on new version
- Health metrics stable for defined period
- No rollback triggers activated (KA-SDLC-059)

**Fallback to P6 (Debugging) when:**
- Rollback triggered (KA-SDLC-004)
- Error rate thresholds breached (KA-SDLC-059)
- Silent failures detected (KA-SDLC-075)

**Fallback to P5 (Code Review) when:**
- Infrastructure validation fails
- Security scan identifies issues

---
---

## P8: Maintenance & Monitoring

**WHAT THE AGENT IS DOING:**
The agent monitors production systems, responds to incidents, manages dependency updates, generates postmortems, and feeds learnings back into improvement loops. This phase ensures long-term system health and continuous optimization.

---

**KNOWLEDGE ATOMS:**
KA-SDLC-004, KA-SDLC-009, KA-SDLC-010, KA-SDLC-011, KA-SDLC-013, KA-SDLC-014, KA-SDLC-025, KA-SDLC-026, KA-SDLC-028, KA-SDLC-034, KA-SDLC-047, KA-SDLC-049, KA-SDLC-069, KA-SDLC-076, KA-SDLC-081, KA-SDLC-082, KA-SDLC-084, KA-SDLC-085, KA-SDLC-086, KA-SDLC-087, KA-CODE-015, KA-CODE-025, KA-CODE-035, KA-CMI-029, KA-CMI-030, KA-CMI-031, KA-CMI-033, KA-META-017, KA-META-032, KA-META-042, KA-META-043, KA-META-055, KA-META-057, KA-AGENT-010, KA-AGENT-011, KA-AGENT-028, KA-AGENT-040, DATA-005, DATA-007, DATA-017, INFRA-008, INFRA-014, INFRA-015, INFRA-016, INFRA-020, INFRA-023, HUMAN-001, HUMAN-003, HUMAN-013, HUMAN-014, HUMAN-015, HUMAN-016, HUMAN-017, HUMAN-018, HUMAN-019, HUMAN-021, HUMAN-022

---

**TECHNIQUES TO USE (ranked, by step):**

**Step 1 — Collect and analyze telemetry:**
KA-SDLC-009 (Structured logging), KA-SDLC-010 (Telemetry pipelines), KA-SDLC-011 (Distributed tracing), KA-SDLC-028 (RED/USE metrics), DATA-005 (Data drift detection), DATA-017 (Drift detection tools)

**Step 2 — Detect anomalies and incidents:**
KA-SDLC-028 (Metrics-based alerting), KA-SDLC-012 (Error fingerprinting), KA-SDLC-047 (Alert fatigue prevention), KA-AGENT-040 (Observability vs Performance tradeoff)

**Step 3 — Generate automated postmortems:**
KA-SDLC-013 (Automated postmortem generation), KA-SDLC-069 (Error pattern learning), KA-META-017 (Event-sourced audit ledger)

**Step 4 — Execute learning feedback loops:**
KA-SDLC-014 (Feedback loops improve reliability 40%), KA-SDLC-082 (Continuous learning from test results), KA-SDLC-069 (Error pattern learning workflow), KA-CMI-029 (Auto-learning memory systems)

**Step 5 — Manage dependencies and updates:**
KA-CODE-035 (Spec rot prevention), KA-CMI-031 (Stale embeddings prevention), KA-META-032 (AI-Native SBOM Extension), DATA-007 (Migration issue management)

**Step 6 — Optimize based on telemetry:**
KA-SDLC-034 (Automated optimization), KA-META-042 (Cost-to-Value Telemetry Loop), INFRA-008 (Semantic caching), KA-AGENT-011 (Fair-share scheduling)

**Step 7 — Calibrate HITL thresholds:**
HUMAN-001 (HITL intervention reduction), HUMAN-003 (Human overestimation calibration), HUMAN-015 (Escalation threshold drift prevention), HUMAN-013 (Approval fatigue prevention)

---

**CONSTRAINTS IN EFFECT:**
- KA-SDLC-014 (Closed feedback cycle requirement)
- KA-SDLC-076 (Feedback loop ignorance prevention)
- KA-CMI-030 (Catastrophic forgetting prevention)
- KA-CMI-031 (Embedding freshness monitoring)
- HUMAN-015 (Continuous threshold calibration)
- KA-META-055 (Governance anti-patterns avoidance)

---

**TOOLS NEEDED:**
- KA-SDLC-087 (OpenTelemetry semantic conventions)
- KA-SDLC-086 (MCP standardization)
- KA-AGENT-033 (AgentOps frameworks)
- DATA-017 (Drift detection: Great Expectations, WhyLabs, Evidently)
- HUMAN-009 (Apprise multi-channel notification)
- HUMAN-019 (HITL Framework implementations)

---

**FAILURE MODES TO WATCH FOR:**
- KA-SDLC-047 (Alert fatigue)
- KA-SDLC-076 (Feedback loop ignorance)
- KA-SDLC-084 (Trust without verification)
- KA-CODE-035 (Spec rot)
- KA-CMI-031 (Stale embeddings)
- HUMAN-013 (Approval fatigue spiral)
- HUMAN-014 (Context poisoning from human input)
- HUMAN-015 (Escalation threshold drift)
- HUMAN-016 (Notification spam)
- KA-META-055 (Governance anti-patterns)
- INFRA-014 (GPU over-provisioning)
- INFRA-015 (Synchronous external calls)

---

**TRANSITIONS:**

**Exit to P6 (Debugging) when:**
- Incident detected requiring response
- Error thresholds breached (KA-SDLC-028)
- Anomaly detected in telemetry (DATA-005)

**Exit to P2 (Planning) when:**
- Architecture improvement identified
- Major dependency update required
- Specification updates needed (KA-CODE-035)

**Fallback to P7 (Deployment) when:**
- Hotfix required for production
- Rollback executed (KA-SDLC-004)
- Configuration drift detected

**Continuous loop to self (P8):**
- Monitoring never stops
- Continuous optimization (KA-SDLC-034)
- Feedback loop maintenance (KA-SDLC-014)

---
---

## Cross-Phase Atom Index

The following atoms appear across multiple phases due to their cross-cutting nature:

| Atom ID | Type | Phases | Description |
|---------|------|--------|-------------|
| KA-META-001 | METRIC | P1-P8 | Cost modeling per task |
| KA-META-002 | TECHNIQUE | P3, P6 | Model cascade routing |
| KA-META-007 | CONSTRAINT | P1-P8 | Budget enforcement |
| KA-META-011 | FAILURE_MODE | P1-P8 | Prompt injection attacks |
| KA-META-012 | FAILURE_MODE | P3-P6 | Hallucination impact |
| KA-META-013 | TECHNIQUE | P3-P6 | Anti-hallucination guardrails |
| KA-META-016 | ANTI_PATTERN | P1-P8 | Security anti-patterns |
| KA-META-017 | RECIPE | P1-P8 | Governance compliance envelope |
| KA-META-020 | CONSTRAINT | P1-P8 | Security hardening checklist |
| KA-CMI-005 | FAILURE_MODE | P3-P7 | Context poisoning |
| KA-CMI-025 | TOOL | P1-P8 | Vector database selection |
| KA-CMI-038 | TECHNIQUE | P3-P7 | Multi-model adversarial reasoning |
| KA-CMI-052 | ANTI_PATTERN | P1-P8 | Context staleness |
| KA-AGENT-008 | TECHNIQUE | P1-P8 | Hierarchical multi-agent orchestration |
| KA-SDLC-009 | METRIC | P5-P8 | Structured logging |
| KA-SDLC-010 | METRIC | P5-P8 | Telemetry pipelines |
| KA-SDLC-014 | METRIC | P5-P8 | Feedback loops |
| KA-SDLC-025 | METRIC | P5-P8 | Agent performance scoring |
| KA-SDLC-026 | METRIC | P5-P8 | Trust scoring |
| HUMAN-002 | TECHNIQUE | All | Five-Level Autonomy Framework |

---

## Summary Statistics

| Phase | Primary Atoms | Cross-Cutting | Total Unique |
|-------|--------------|---------------|--------------|
| P1 Discovery | 35 | 85 | 120 |
| P2 Planning | 42 | 78 | 120 |
| P3 Implementation | 68 | 52 | 120 |
| P4 Testing | 54 | 45 | 99 |
| P5 Code Review | 48 | 38 | 86 |
| P6 Debugging | 39 | 42 | 81 |
| P7 Deployment | 52 | 35 | 87 |
| P8 Maintenance | 38 | 48 | 86 |

**Grand Total: 372 knowledge atoms mapped**

---

## Knowledge Gaps

1. **Optimal phase transition thresholds**: Quantitative confidence thresholds for phase transitions need empirical calibration
2. **Cross-phase budget allocation**: No established methodology for distributing token budgets across phases
3. **Phase-specific failure recovery**: Limited research on optimal rollback strategies per phase
4. **Parallel phase execution**: When can phases execute concurrently vs sequentially

---

## Sources

All atoms extracted from:
- `docs/distillation/prong1_meta_architecture.md` (60 atoms)
- `docs/distillation/prong1_sdlc_automation.md` (87 atoms)
- `docs/distillation/prong1_agent_orchestration.md` (42 atoms)
- `docs/distillation/prong1_context_memory_intelligence.md` (58 atoms)
- `docs/distillation/prong1_code_intelligence.md` (58 atoms)
- `docs/distillation/prong1_data_human.md` (67 atoms)

**Total: 372 knowledge atoms mapped to 8 SDLC phases**

---

*Generated: 2026-02-24*  
*Prong: 3 of 4 (Temporal Organization)*  
*Next: Prong 4 (Product Specification Mapping)*

