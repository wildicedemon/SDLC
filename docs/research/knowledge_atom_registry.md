# Knowledge Atom Registry: Autonomous AI Coding Systems Research

**Generated:** February 24, 2026  
**Source:** SDLC Research Corpus (docs/research/)

---

## Executive Summary

This registry contains knowledge atoms extracted from 7 major research directories covering 30+ subdirectories of research on autonomous AI coding systems. The atoms span 9 types: TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, and RECIPE.

Key findings include:
- Context management achieves 40-70% token reduction while maintaining accuracy
- Hierarchical multi-agent orchestration outperforms flat designs by 12-23%
- Security requires layered defense with 5+ control points
- Human-in-the-loop systems reduce intervention by 70-80% while improving success rates
- LLM-generated tests achieve 60-80% coverage but miss edge cases
- Cost reduction of 40-87% through cascade routing

---

## Knowledge Atoms Summary

| Type | Count |
|------|-------|
| TECHNIQUE | 35 |
| METRIC | 15 |
| CONSTRAINT | 5 |
| TOOL | 8 |
| FAILURE_MODE | 3 |
| ANTI_PATTERN | 12 |
| RECIPE | 2 |
| **TOTAL** | **80+** |

---

## Domain Coverage (D1-D12)

- D1: Agent Architecture & Orchestration - 15 atoms
- D2: Task Management & Decomposition - 8 atoms
- D3: Context & Prompt Engineering - 12 atoms
- D4: Memory & Knowledge Systems - 5 atoms
- D5: Code Intelligence & Representations - 6 atoms
- D6: Testing & Validation - 8 atoms
- D7: Security & Guardrails - 12 atoms
- D8: Model Management & Routing - 6 atoms
- D9: CI/CD & DevOps - 6 atoms
- D10: Workspace & Infrastructure Management - 4 atoms
- D11: Human Interaction - 10 atoms
- D12: Self-Improvement & Optimization - 4 atoms

---

## Key Findings by Research Area

### 01_meta_architecture (System Design, Security, Governance, Economics)

1. **BDI Hybrid Architecture** (KA-001): Combines Belief-Desire-Intent with LLMs for audit-friendly explicit mental states
2. **4-Phase Spec-Driven Workflow** (KA-002): Specify→Plan→Tasks→Implement achieves 56% faster development
3. **Bidirectional Specifications** (KA-003): Agents update specs as they discover codebase realities
4. **Layered Security** (KA-026): 5+ control points mandatory - no single mechanism blocks all attacks
5. **Hallucination Impact** (KA-027): 19.7% fabricated packages, 40-45% vulnerable code, 43% API misuse
6. **Cascade Routing** (KA-036): 40-87% cost reduction through model escalation
7. **Compliance Envelope** (KA-051): Standardized evidence per run for audit trails

### 02_agent_orchestration (Agent Design, Task Architecture, Distributed)

1. **System-Theoretic Decomposition** (KA-005): 5 subsystems with explicit interfaces
2. **Mixture-of-Agents** (KA-007): 8-12% improvement over single-agent
3. **Conditional Multi-Stage Recovery** (KA-010): 19% higher success rate
4. **Hierarchical Task Decomposition** (KA-008): 2-3 levels simple, 5-7 complex tasks
5. **Worktree Isolation** (KA-009): 67% reduction in merge conflicts
6. **Federated Clusters** (KA-065): 3x throughput with regional coordinators
7. **Fair-Share Scheduling** (KA-066): 89% reduction in task starvation

### 03_context_memory_intelligence (Context, Memory, Reasoning)

1. **LLMLingua Compression** (KA-012): 20x compression with <3% degradation
2. **Selective Context** (KA-013): 50% token reduction, 97% performance retention
3. **Lost-in-Middle** (KA-015): U-shaped prioritization for context placement
4. **Context Poisoning** (KA-016): 4 attack vectors requiring disposable sessions
5. **Augment Context Engine** (KA-018): 71% completeness improvement
6. **GraphRAG** (KA-020): 23% improvement on multi-hop reasoning
7. **Vector DB Recall** (KA-019): 85-95% recall@10 with code-specific embeddings

### 04_code_intelligence (Exploration, Specification, Refactoring)

1. **Semantic-Guided Traversal** (KA-022): 40-60% time reduction
2. **CoSrch Hybrid Search** (KA-023): 7.60% SuccessRate@1 improvement
3. **Repo Grokking** (KA-024): Sub-second queries across million-line codebases
4. **File Prioritization** (KA-025): 50-70% exploration time reduction

### 05_sdlc_automation (Testing, CI/CD, Observability)

1. **AI Test Coverage** (KA-041): 60-80% coverage but misses edge cases
2. **QA Swarm** (KA-042): 40% higher bug detection than single agent
3. **Semantic Merge** (KA-043): 78% automatic resolution vs 45% traditional
4. **Mutation Testing** (KA-044): r=0.75 correlation with defect detection
5. **Multi-Stage Testing** (KA-045): 60% reduction in production incidents
6. **CI/CD Maturity** (KA-047): 208x deployment frequency, 2604x recovery speed

### 06_data_infrastructure (Database, Infrastructure)

1. **Declarative Schemas** (KA-070): 47% reduction in migration errors
2. **LLM Migration Accuracy** (KA-071): 73% first-attempt, 94% with refinement
3. **Contract-Aware Generation** (KA-072): 31% improvement in correctness

### 07_human_interaction (HITL Systems)

1. **Autonomy Levels** (KA-056): 5 levels from operator to observer
2. **Confidence-Based Escalation** (KA-057): 70% cost reduction
3. **HITL Effectiveness** (KA-058): 70-80% intervention reduction
4. **Auto-Approval Gateway** (KA-060): Risk-based action approval
5. **ask_followup_question** (KA-061): Structured clarification tool
6. **Apprise Notifications** (KA-062): 80+ service integration
7. **Cognitive Load Optimization** (KA-063): Batching, summarization, filtering

---

## Notable Anti-Patterns

1. **Prompt-Only Security** (KA-032): Easily bypassed
2. **Over-Privileged MCP** (KA-033): Enables lateral movement
3. **One-Model-for-Everything** (KA-039): Cost inflation
4. **Unlimited Planning** (KA-040): Token runaway
5. **AI Happy Path Bias** (KA-046): 80% miss error handling
6. **Opaque AI Decisions** (KA-064): User distrust
7. **God Agent** (KA-079): Single point of failure
8. **Chatty Communication** (KA-080): 10x cost, 5x latency

---

## Key Tradeoffs

| Tradeoff | Options | Recommendation |
|----------|---------|----------------|
| Autonomy vs Control | High/Low | Risk-based with approval gates |
| Simplicity vs Capability | Simple/Complex | Start simple, add as needed |
| Cost vs Quality | Cheap/Premium | Task-dependent model selection |
| Latency vs Intelligence | Fast/Thorough | User-facing vs batch |
| Spec-Driven vs Intent-Driven | Rigid/Adaptive | Use bidirectional maintenance |

---

## Sources

- docs/research/01_meta_architecture/system_design_philosophy/ - System design patterns
- docs/research/01_meta_architecture/security_architecture/ - Security controls
- docs/research/01_meta_architecture/governance_compliance/ - Audit and compliance
- docs/research/01_meta_architecture/economic_optimization_modeling/ - Cost optimization
- docs/research/02_agent_orchestration/agent_system_design/ - Agent architecture
- docs/research/02_agent_orchestration/task_architecture/ - Task patterns
- docs/research/02_agent_orchestration/distributed_orchestration/ - Distributed systems
- docs/research/03_context_memory_intelligence/context_management/ - Context handling
- docs/research/03_context_memory_intelligence/memory_systems/ - Memory architecture
- docs/research/04_code_intelligence/code_exploration/ - Code understanding
- docs/research/05_sdlc_automation/testing_architecture/ - Testing strategies
- docs/research/05_sdlc_automation/cicd_devops/ - CI/CD patterns
- docs/research/06_data_infrastructure/database_data_engineering/ - Database engineering
- docs/research/07_human_interaction/human_in_the_loop_systems/ - HITL patterns

---

*This registry represents extracted knowledge atoms from the SDLC research corpus. Each atom includes type, content, evidence strength, source path, domain coverage (D1-D12), SDLC phase applicability (P1-P8), and product category relevance (PC1-PC10).*

**Generated:** February 24, 2026  
**Source:** SDLC Research Corpus (docs/research/)

---

## Executive Summary

This registry contains knowledge atoms extracted from 7 major research directories covering 30+ subdirectories of research on autonomous AI coding systems. The atoms span 9 types: TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, and RECIPE.

Key findings include:
- Context management achieves 40-70% token reduction while maintaining accuracy
- Hierarchical multi-agent orchestration outperforms flat designs by 12-23%
- Security requires layered defense with 5+ control points
- Human-in-the-loop systems reduce intervention by 70-80% while improving success rates
- LLM-generated tests achieve 60-80% coverage but miss edge cases
- Cost reduction of 40-87% through cascade routing

---

## Knowledge Atoms Summary

| Type | Count |
|------|-------|
| TECHNIQUE | 35 |
| METRIC | 15 |
| CONSTRAINT | 5 |
| TOOL | 8 |
| FAILURE_MODE | 3 |
| ANTI_PATTERN | 12 |
| RECIPE | 2 |
| **TOTAL** | **80+** |

---

## Domain Coverage (D1-D12)

- D1: Agent Architecture & Orchestration - 15 atoms
- D2: Task Management & Decomposition - 8 atoms
- D3: Context & Prompt Engineering - 12 atoms
- D4: Memory & Knowledge Systems - 5 atoms
- D5: Code Intelligence & Representations - 6 atoms
- D6: Testing & Validation - 8 atoms
- D7: Security & Guardrails - 12 atoms
- D8: Model Management & Routing - 6 atoms
- D9: CI/CD & DevOps - 6 atoms
- D10: Workspace & Infrastructure Management - 4 atoms
- D11: Human Interaction - 10 atoms
- D12: Self-Improvement & Optimization - 4 atoms

---

## Key Findings by Research Area

### 01_meta_architecture (System Design, Security, Governance, Economics)

1. **BDI Hybrid Architecture** (KA-001): Combines Belief-Desire-Intent with LLMs for audit-friendly explicit mental states
2. **4-Phase Spec-Driven Workflow** (KA-002): Specify→Plan→Tasks→Implement achieves 56% faster development
3. **Bidirectional Specifications** (KA-003): Agents update specs as they discover codebase realities
4. **Layered Security** (KA-026): 5+ control points mandatory - no single mechanism blocks all attacks
5. **Hallucination Impact** (KA-027): 19.7% fabricated packages, 40-45% vulnerable code, 43% API misuse
6. **Cascade Routing** (KA-036): 40-87% cost reduction through model escalation
7. **Compliance Envelope** (KA-051): Standardized evidence per run for audit trails

### 02_agent_orchestration (Agent Design, Task Architecture, Distributed)

1. **System-Theoretic Decomposition** (KA-005): 5 subsystems with explicit interfaces
2. **Mixture-of-Agents** (KA-007): 8-12% improvement over single-agent
3. **Conditional Multi-Stage Recovery** (KA-010): 19% higher success rate
4. **Hierarchical Task Decomposition** (KA-008): 2-3 levels simple, 5-7 complex tasks
5. **Worktree Isolation** (KA-009): 67% reduction in merge conflicts
6. **Federated Clusters** (KA-065): 3x throughput with regional coordinators
7. **Fair-Share Scheduling** (KA-066): 89% reduction in task starvation

### 03_context_memory_intelligence (Context, Memory, Reasoning)

1. **LLMLingua Compression** (KA-012): 20x compression with <3% degradation
2. **Selective Context** (KA-013): 50% token reduction, 97% performance retention
3. **Lost-in-Middle** (KA-015): U-shaped prioritization for context placement
4. **Context Poisoning** (KA-016): 4 attack vectors requiring disposable sessions
5. **Augment Context Engine** (KA-018): 71% completeness improvement
6. **GraphRAG** (KA-020): 23% improvement on multi-hop reasoning
7. **Vector DB Recall** (KA-019): 85-95% recall@10 with code-specific embeddings

### 04_code_intelligence (Exploration, Specification, Refactoring)

1. **Semantic-Guided Traversal** (KA-022): 40-60% time reduction
2. **CoSrch Hybrid Search** (KA-023): 7.60% SuccessRate@1 improvement
3. **Repo Grokking** (KA-024): Sub-second queries across million-line codebases
4. **File Prioritization** (KA-025): 50-70% exploration time reduction

### 05_sdlc_automation (Testing, CI/CD, Observability)

1. **AI Test Coverage** (KA-041): 60-80% coverage but misses edge cases
2. **QA Swarm** (KA-042): 40% higher bug detection than single agent
3. **Semantic Merge** (KA-043): 78% automatic resolution vs 45% traditional
4. **Mutation Testing** (KA-044): r=0.75 correlation with defect detection
5. **Multi-Stage Testing** (KA-045): 60% reduction in production incidents
6. **CI/CD Maturity** (KA-047): 208x deployment frequency, 2604x recovery speed

### 06_data_infrastructure (Database, Infrastructure)

1. **Declarative Schemas** (KA-070): 47% reduction in migration errors
2. **LLM Migration Accuracy** (KA-071): 73% first-attempt, 94% with refinement
3. **Contract-Aware Generation** (KA-072): 31% improvement in correctness

### 07_human_interaction (HITL Systems)

1. **Autonomy Levels** (KA-056): 5 levels from operator to observer
2. **Confidence-Based Escalation** (KA-057): 70% cost reduction
3. **HITL Effectiveness** (KA-058): 70-80% intervention reduction
4. **Auto-Approval Gateway** (KA-060): Risk-based action approval
5. **ask_followup_question** (KA-061): Structured clarification tool
6. **Apprise Notifications** (KA-062): 80+ service integration
7. **Cognitive Load Optimization** (KA-063): Batching, summarization, filtering

---

## Notable Anti-Patterns

1. **Prompt-Only Security** (KA-032): Easily bypassed
2. **Over-Privileged MCP** (KA-033): Enables lateral movement
3. **One-Model-for-Everything** (KA-039): Cost inflation
4. **Unlimited Planning** (KA-040): Token runaway
5. **AI Happy Path Bias** (KA-046): 80% miss error handling
6. **Opaque AI Decisions** (KA-064): User distrust
7. **God Agent** (KA-079): Single point of failure
8. **Chatty Communication** (KA-080): 10x cost, 5x latency

---

## Key Tradeoffs

| Tradeoff | Options | Recommendation |
|----------|---------|----------------|
| Autonomy vs Control | High/Low | Risk-based with approval gates |
| Simplicity vs Capability | Simple/Complex | Start simple, add as needed |
| Cost vs Quality | Cheap/Premium | Task-dependent model selection |
| Latency vs Intelligence | Fast/Thorough | User-facing vs batch |
| Spec-Driven vs Intent-Driven | Rigid/Adaptive | Use bidirectional maintenance |

---

## Sources

- docs/research/01_meta_architecture/system_design_philosophy/ - System design patterns
- docs/research/01_meta_architecture/security_architecture/ - Security controls
- docs/research/01_meta_architecture/governance_compliance/ - Audit and compliance
- docs/research/01_meta_architecture/economic_optimization_modeling/ - Cost optimization
- docs/research/02_agent_orchestration/agent_system_design/ - Agent architecture
- docs/research/02_agent_orchestration/task_architecture/ - Task patterns
- docs/research/02_agent_orchestration/distributed_orchestration/ - Distributed systems
- docs/research/03_context_memory_intelligence/context_management/ - Context handling
- docs/research/03_context_memory_intelligence/memory_systems/ - Memory architecture
- docs/research/04_code_intelligence/code_exploration/ - Code understanding
- docs/research/05_sdlc_automation/testing_architecture/ - Testing strategies
- docs/research/05_sdlc_automation/cicd_devops/ - CI/CD patterns
- docs/research/06_data_infrastructure/database_data_engineering/ - Database engineering
- docs/research/07_human_interaction/human_in_the_loop_systems/ - HITL patterns

---

*This registry represents extracted knowledge atoms from the SDLC research corpus. Each atom includes type, content, evidence strength, source path, domain coverage (D1-D12), SDLC phase applicability (P1-P8), and product category relevance (PC1-PC10).*

