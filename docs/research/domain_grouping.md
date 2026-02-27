# Domain Grouping: Lateral Organization of Knowledge Atoms

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry (docs/research/knowledge_atom_registry.md)

---

## Executive Summary

This document organizes knowledge atoms by technical domain (D1-D12), providing structured analysis for each domain including key techniques ranked by evidence strength, constraints, tools, combination recipes, failure modes, cross-domain links, and identified gaps. The lateral organization enables practitioners to identify relevant knowledge atoms for specific technical challenges.

---

## D1: Agent Architecture & Orchestration

**KNOWLEDGE ATOMS:** KA-001, KA-005, KA-007, KA-010, KA-026, KA-065, KA-066, KA-079, KA-080

**KEY TECHNIQUES (ranked):**

1. **KA-007 — Mixture-of-Agents** — HIGH: 8-12% improvement over single-agent systems through collaborative agent ensembles
2. **KA-010 — Conditional Multi-Stage Recovery** — HIGH: 19% higher success rate through staged retry mechanisms
3. **KA-001 — BDI Hybrid Architecture** — MEDIUM: Combines Belief-Desire-Intent with LLMs for audit-friendly explicit mental states
4. **KA-005 — System-Theoretic Decomposition** — MEDIUM: 5 subsystems with explicit interfaces for maintainable architecture
5. **KA-065 — Federated Clusters** — MEDIUM: 3x throughput with regional coordinators for distributed workloads
6. **KA-066 — Fair-Share Scheduling** — MEDIUM: 89% reduction in task starvation through equitable resource distribution

**KEY CONSTRAINTS:**

- KA-079 — **God Agent Anti-Pattern**: Single point of failure when all capabilities converge in one agent
- KA-080 — **Chatty Communication**: 10x cost and 5x latency when agents communicate excessively

**KEY TOOLS:**

- KA-001 — BDI Framework — Audit-friendly mental state representation
- KA-005 — System Theory Modeling — Interface-based decomposition

**COMBINATION RECIPES:**

- KA-007 + KA-010 — Mixture-of-Agents with conditional recovery creates robust multi-agent systems where agent failures trigger recovery cascades
- KA-005 + KA-065 — System-theoretic decomposition combined with federated clusters enables scalable distributed architecture

**FAILURE MODES:**

- KA-079 — **God Agent breaks** when single agent becomes bottleneck — **detect** through latency monitoring — **respond** by decomposing into specialized agents
- KA-080 — **Chatty Communication breaks** during high-frequency coordination — **detect** through cost tracking — **respond** by batching messages and using hierarchical communication

**CROSS-DOMAIN LINKS:**

- KA-026 (Layered Security) also relevant to D7
- KA-009 (Worktree Isolation) also relevant to D10
- KA-008 (Hierarchical Task Decomposition) also relevant to D2

**GAPS:**

- Missing research on agent lifecycle state machines
- No established patterns for trust scoring between agents
- Limited guidance on deadlock/livelock detection in agent swarms

---

## D2: Task Management & Decomposition

**KNOWLEDGE ATOMS:** KA-002, KA-003, KA-008, KA-009, KA-040, KA-043

**KEY TECHNIQUES (ranked):**

1. **KA-002 — 4-Phase Spec-Driven Workflow** — HIGH: 56% faster development through Specify→Plan→Tasks→Implement pipeline
2. **KA-008 — Hierarchical Task Decomposition** — HIGH: 2-3 levels for simple tasks, 5-7 levels for complex tasks
3. **KA-003 — Bidirectional Specifications** — MEDIUM: Agents update specs as they discover codebase realities
4. **KA-043 — Semantic Merge** — MEDIUM: 78% automatic resolution vs 45% traditional merge
5. **KA-009 — Worktree Isolation** — MEDIUM: 67% reduction in merge conflicts through isolated worktrees

**KEY CONSTRAINTS:**

- KA-040 — **Unlimited Planning Anti-Pattern**: Token runaway when agents are allowed unlimited planning time

**KEY TOOLS:**

- KA-002 — Spec-Driven Workflow Framework — Phase-gated development
- KA-009 — Git Worktree — Branch isolation for concurrent agent work

**COMBINATION RECIPES:**

- KA-002 + KA-003 — 4-phase workflow with bidirectional specifications enables adaptive planning that evolves with codebase discovery
- KA-008 + KA-009 — Hierarchical task decomposition combined with worktree isolation enables parallel agent execution without conflicts

**FAILURE MODE:**

- KA-040 — **Unlimited Planning breaks** when token budgets are exceeded — **detect** through token usage monitoring — **respond** by implementing planning budgets and timeouts

**CROSS-DOMAIN LINKS:**

- KA-002 also relevant to D5 (Code Intelligence)
- KA-003 also relevant to D3 (Context & Prompt Engineering)
- KA-008 also relevant to D1 (Agent Architecture)

**GAPS:**

- No established patterns for dependency detection and resolution
- Limited guidance on commit generation and branch management strategies
- Missing research on conflict resolution for concurrent agent work

---

## D3: Context & Prompt Engineering

**KNOWLEDGE ATOMS:** KA-012, KA-013, KA-015, KA-016, KA-018, KA-046

**KEY TECHNIQUES (ranked):**

1. **KA-012 — LLMLingua Compression** — HIGH: 20x compression with <3% quality degradation
2. **KA-013 — Selective Context** — HIGH: 50% token reduction while retaining 97% performance
3. **KA-015 — Lost-in-Middle** — MEDIUM: U-shaped prioritization places critical information at context boundaries
4. **KA-018 — Augment Context Engine** — MEDIUM: 71% completeness improvement through intelligent context augmentation
5. **KA-016 — Context Poisoning** — CONSTRAINT: 4 attack vectors requiring disposable sessions

**KEY CONSTRAINTS:**

- KA-016 — **Context Poisoning**: Malicious context injection through 4 attack vectors requiring session isolation

**KEY TOOLS:**

- KA-012 — LLMLingua — Token compression for context optimization
- KA-018 — Augment Platform — Context augmentation engine

**COMBINATION RECIPES:**

- KA-012 + KA-013 — LLMLingua compression combined with selective context achieves maximum token reduction without quality loss
- KA-015 + KA-018 — Lost-in-middle prioritization with augment context creates intelligent context placement

**FAILURE MODES:**

- KA-016 — **Context Poisoning breaks** session security — **detect** through anomaly detection in context — **respond** by implementing disposable sessions and input validation

**CROSS-DOMAIN LINKS:**

- KA-016 also relevant to D7 (Security & Guardrails)
- KA-046 (AI Happy Path Bias) also relevant to D6

**GAPS:**

- Missing research on prompt structure and ordering optimization
- No established patterns for anti-hallucination prompt patterns
- Limited guidance on token budget management across long tasks
- No research on context refresh and rotation strategies

---

## D4: Memory & Knowledge Systems

**KNOWLEDGE ATOMS:** KA-019, KA-020, KA-070, KA-071, KA-072

**KEY TECHNIQUES (ranked):**

1. **KA-019 — Vector DB Recall** — HIGH: 85-95% recall@10 with code-specific embeddings
2. **KA-020 — GraphRAG** — HIGH: 23% improvement on multi-hop reasoning through knowledge graph integration
3. **KA-071 — LLM Migration Accuracy** — MEDIUM: 73% first-attempt, 94% with refinement for database migrations
4. **KA-070 — Declarative Schemas** — MEDIUM: 47% reduction in migration errors through schema-first design
5. **KA-072 — Contract-Aware Generation** — MEDIUM: 31% improvement in correctness through contract validation

**KEY TOOLS:**

- KA-019 — Vector Database — Semantic code search and retrieval
- KA-020 — GraphRAG — Knowledge graph augmented generation

**COMBINATION RECIPES:**

- KA-019 + KA-020 — Vector DB with GraphRAG combines semantic retrieval with knowledge graph reasoning for complex queries

**FAILURE MODES:**

- No specific failure modes identified in current research

**CROSS-DOMAIN LINKS:**

- KA-019 also relevant to D5 (Code Intelligence)
- KA-070, KA-071, KA-072 also relevant to D6 (Data Infrastructure)

**GAPS:**

- Missing research on short-term working memory architectures
- No patterns for persistent memory across sessions
- Limited guidance on auto-learning systems
- No research on cross-session retrieval optimization

---

## D5: Code Intelligence & Representations

**KNOWLEDGE ATOMS:** KA-022, KA-023, KA-024, KA-025, KA-002, KA-003

**KEY TECHNIQUES (ranked):**

1. **KA-024 — Repo Grokking** — HIGH: Sub-second queries across million-line codebases
2. **KA-022 — Semantic-Guided Traversal** — HIGH: 40-60% time reduction in code exploration
3. **KA-023 — CoSrch Hybrid Search** — HIGH: 7.60% SuccessRate@1 improvement through hybrid code search
4. **KA-025 — File Prioritization** — MEDIUM: 50-70% exploration time reduction through intelligent file ordering

**KEY TOOLS:**

- KA-024 — Code Graph Systems — Repository-wide semantic understanding
- KA-022 — Semantic Analysis Engine — Context-aware code traversal

**COMBINATION RECIPES:**

- KA-022 + KA-025 — Semantic-guided traversal with file prioritization optimizes exploration efficiency
- KA-023 + KA-024 — Hybrid search combined with repo grokking enables precise code location

**FAILURE MODES:**

- No specific failure modes identified in current research

**CROSS-DOMAIN LINKS:**

- KA-002, KA-003 also relevant to D2 (Task Management)
- KA-019 (Vector DB Recall) also relevant to D4

**GAPS:**

- Missing research on AST/CFG/DFG representations
- No established patterns for symbol indexing
- Limited guidance on taint tracking
- No research on schema inference for code

---

## D6: Testing & Validation

**KNOWLEDGE ATOMS:** KA-041, KA-042, KA-044, KA-045, KA-046, KA-047

**KEY TECHNIQUES (ranked):**

1. **KA-041 — AI Test Coverage** — HIGH: 60-80% coverage but misses edge cases
2. **KA-042 — QA Swarm** — HIGH: 40% higher bug detection than single agent
3. **KA-044 — Mutation Testing** — HIGH: r=0.75 correlation with defect detection
4. **KA-045 — Multi-Stage Testing** — MEDIUM: 60% reduction in production incidents
5. **KA-047 — CI/CD Maturity** — MEDIUM: 208x deployment frequency, 2604x recovery speed

**KEY CONSTRAINTS:**

- KA-046 — **AI Happy Path Bias**: 80% miss error handling when agents focus on success cases

**KEY TOOLS:**

- KA-041 — Test Generation Frameworks — AI-powered unit and integration test creation
- KA-044 — Mutation Testing Tools — Defect detection through code mutation

**COMBINATION RECIPES:**

- KA-041 + KA-042 — AI test coverage with QA swarm combines generation with multi-agent validation
- KA-044 + KA-045 — Mutation testing with multi-stage validation creates comprehensive quality gates

**FAILURE MODES:**

- KA-046 — **AI Happy Path Bias breaks** test quality — **detect** through edge case coverage analysis — **respond** by requiring explicit error path testing

**CROSS-DOMAIN LINKS:**

- KA-045 also relevant to D9 (CI/CD & DevOps)
- KA-047 also relevant to D9

**GAPS:**

- Missing research on property-based testing for AI-generated code
- No established patterns for behavioral testing
- Limited guidance on E2E testing for autonomous agents

---

## D7: Security & Guardrails

**KNOWLEDGE ATOMS:** KA-026, KA-027, KA-032, KA-033, KA- TECHNIQUES (ranked):**

1. **KA016

**KEY-026 — Layered Security** — HIGH: 5+ control points mandatory — no single mechanism blocks all attacks
2. **KA-027 — Hallucination Impact** — HIGH: 19.7% fabricated packages, 40-45% vulnerable code, 43% API misuse
3. **KA-033 — Over-Privileged MCP Anti-Pattern** — CONSTRAINT: Enables lateral movement when MCP has excessive privileges

**KEY CONSTRAINTS:**

- KA-032 — **Prompt-Only Security**: Easily bypassed without additional guardrails
- KA-033 — **Over-Privileged MCP**: Enables lateral movement through excessive permissions

**KEY TOOLS:**

- KA-026 — Multi-Layer Security Framework — Defense in depth implementation

**COMBINATION RECIPES:**

- KA-026 + KA-027 — Layered security with hallucination awareness creates comprehensive threat coverage

**FAILURE MODES:**

- KA-032 — **Prompt-Only Security breaks** under adversarial prompts — **detect** through red-team testing — **respond** by adding technical controls
- KA-033 — **Over-Privileged MCP breaks** when compromised — **detect** through privilege audit — **respond** by implementing least-privilege

**CROSS-DOMAIN LINKS:**

- KA-016 (Context Poisoning) also relevant to D3
- KA-027 also relevant to D8 (Model Management)

**GAPS:**

- Missing research on package verification (slopsquatting)
- No established patterns for sandboxing and isolation
- Limited guidance on secret management
- No research on MCP privilege isolation best practices

---

## D8: Model Management & Routing

**KNOWLEDGE ATOMS:** KA-036, KA-027, KA-039

**KEY TECHNIQUES (ranked):**

1. **KA-036 — Cascade Routing** — HIGH: 40-87% cost reduction through intelligent model escalation
2. **KA-027 — Hallucination Impact** — CONSTRAINT: Model-specific hallucination rates affect routing decisions

**KEY CONSTRAINTS:**

- KA-039 — **One-Model-for-Everything Anti-Pattern**: Cost inflation when premium models are used for simple tasks

**KEY TOOLS:**

- KA-036 — Model Routing Framework — Cost-aware model selection

**COMBINATION RECIPES:**

- KA-036 + KA-039 — Cascade routing prevents one-model-for-everything by routing to appropriate model tier

**FAILURE MODES:**

- KA-039 — **One-Model-for-Everything breaks** budget — **detect** through cost monitoring — **respond** by implementing cascade routing

**CROSS-DOMAIN LINKS:**

- KA-027 also relevant to D7 (Security)
- KA-036 also relevant to D1 (for multi-agent model selection)

**GAPS:**

- Missing research on model capability matrices
- No established patterns for confidence-based routing
- Limited guidance on temperature optimization per task type
- No research on multi-model adversarial review

---

## D9: CI/CD &KNOWLEDGE DevOps

** ATOMS:** KA-045, KA-047, KA-043

**KEY TECHNIQUES (ranked):**

1. **KA-047 — CI/CD Maturity** — HIGH: 208x deployment frequency, 2604x recovery speed
2. **KA-045 — Multi-Stage Testing** — MEDIUM: 60% reduction in production incidents
3. **KA-043 — Semantic Merge** — MEDIUM: 78% automatic resolution vs 45% traditional

**KEY TOOLS:**

- KA-047 — CI/CD Pipeline Frameworks — Deployment automation
- KA-043 — Semantic Merge Tools — Intelligent conflict resolution

**COMBINATION RECIPES:**

- KA-045 + KA-047 — Multi-stage testing with CI/CD maturity creates reliable deployment pipelines

**FAILURE MODES:**

- No specific failure modes identified in current research

**CROSS-DOMAIN LINKS:**

- KA-045 also relevant to D6 (Testing)
- KA-043 also relevant to D2 (Task Management)

**GAPS:**

- Missing research on self-healing pipelines
- No established patterns for canary/blue-green deployments for agent outputs
- Limited guidance on container orchestration for agents
- No research on observability integration for autonomous systems

---

## D10: Workspace & Infrastructure Management

**KNOWLEDGE ATOMS:** KA-009, KA-070

**KEY TECHNIQUES (ranked):**

1. **KA-009 — Worktree Isolation** — MEDIUM: 67% reduction in merge conflicts
2. **KA-070 — Declarative Schemas** — MEDIUM: 47% reduction in migration errors

**KEY TOOLS:**

- KA-009 — Git Worktree — Branch and workspace isolation
- KA-070 — Schema Migration Tools — Declarative infrastructure

**COMBINATION RECIPES:**

- KA-009 + KA-070 — Worktree isolation with declarative schemas enables safe concurrent agent work

**FAILURE MODES:**

- No specific failure modes identified in current research

**CROSS-DOMAIN LINKS:**

- KA-009 also relevant to D2 (Task Management)

**GAPS:**

- Missing research on file organization during task execution
- No established patterns for state persistence
- Limited guidance on artifact management
- No research on environment provisioning for agents

---

## D11: Human Interaction

**KNOWLEDGE ATOMS:** KA-056, KA-057, KA-058, KA-060, KA-061, KA-062, KA-063, KA-064

**KEY TECHNIQUES (ranked):**

1. **KA-058 — HITL Effectiveness** — HIGH: 70-80% intervention reduction while improving success rates
2. **KA-057 — Confidence-Based Escalation** — HIGH: 70% cost reduction through intelligent escalation
3. **KA-056 — Autonomy Levels** — MEDIUM: 5 levels from operator to observer
4. **KA-060 — Auto-Approval Gateway** — MEDIUM: Risk-based action approval
5. **KA-063 — Cognitive Load Optimization** — MEDIUM: Batching, summarization, filtering to reduce human overload
6. **KA-062 — Apprise Notifications** — MEDIUM: 80+ service integration for alerts

**KEY CONSTRAINTS:**

- KA-064 — **Opaque AI Decisions Anti-Pattern**: User distrust when AI reasoning is not visible

**KEY TOOLS:**

- KA-061 — Structured Clarification Tool — ask_followup_question framework for ambiguous requests
- KA-062 — Apprise — Multi-channel notification system

**COMBINATION RECIPES:**

- KA-057 + KA-060 — Confidence-based escalation with auto-approval creates efficient human oversight
- KA-058 + KA-063 — HITL with cognitive load optimization maximizes human effectiveness

**FAILURE MODES:**

- KA-064 — **Opaque AI Decisions break** user trust — **detect** through user feedback — **respond** by implementing explainable AI

**CROSS-DOMAIN LINKS:**

- KA-056 also relevant to D1 (Agent Architecture)
- KA-057 also relevant to D8 (Model Management)

**GAPS:**

- Missing research on explainable plan visualization
- No established patterns for notification prioritization
- Limited guidance on approval gateway thresholds

---

## D12: Self-Improvement & Optimization

**KNOWLEDGE ATOMS:** KA-036 (implicit cost optimization), KA-051

**KEY TECHNIQUES (ranked):**

1. **KA-051 — Compliance Envelope** — MEDIUM: Standardized evidence per run for audit trails
2. **KA-036 — Cascade Routing** — IMPLICIT: Cost optimization through model selection

**KEY TOOLS:**

- KA-051 — Compliance Tracking System — Evidence collection for audits

**COMBINATION RECIPES:**

- KA-036 + KA-051 — Cost optimization with compliance tracking enables efficient self-improvement

**FAILURE MODES:**

- No specific failure modes identified in current research

**CROSS-DOMAIN LINKS:**

- KA-036 also relevant to D8 (Model Management)
- KA-051 also relevant to D7 (Security - governance)

**GAPS:**

- Missing research on prompt optimization loops
- No established patterns for agent performance regression detection
- Limited guidance on workflow A/B testing
- No research on skill enable/disable for token efficiency

---

## Summary Statistics

| Domain | Atom Count | Primary Focus |
|--------|------------|----------------|
| D1: Agent Architecture & Orchestration | 9 | Multi-agent design patterns |
| D2: Task Management & Decomposition | 6 | Work breakdown and isolation |
| D3: Context & Prompt Engineering | 6 | Token optimization, security |
| D4: Memory & Knowledge Systems | 5 | Retrieval and knowledge graphs |
| D5: Code Intelligence & Representations | 6 | Code exploration and search |
| D6: Testing & Validation | 6 | AI test generation, quality gates |
| D7: Security & Guardrails | 5 | Defense in depth, hallucination |
| D8: Model Management & Routing | 3 | Cost optimization, cascade routing |
| D9: CI/CD & DevOps | 3 | Deployment automation |
| D10: Workspace & Infrastructure | 2 | Isolation, declarative infra |
| D11: Human Interaction | 8 | HITL, escalation, notifications |
| D12: Self-Improvement | 2 | Optimization, compliance |

---

## Recommended Next Subtasks

1. **Cross-Domain Integration Analysis**: Map how atoms from different domains interact in real-world scenarios
2. **Gap Prioritization**: Rank identified gaps by impact and feasibility of research
3. **Pattern Extraction**: Identify combination recipes that span multiple domains
4. **Tool Evaluation**: Deep-dive into specific tools for each domain with capability matrices

---

## Sources

- docs/research/knowledge_atom_registry.md - Primary knowledge atom source
- docs/research/01_meta_architecture/ - System design, security, economics
- docs/research/02_agent_orchestration/ - Agent design, distributed systems
- docs/research/03_context_memory_intelligence/ - Context, memory, reasoning
- docs/research/04_code_intelligence/ - Code exploration, specification
- docs/research/05_sdlc_automation/ - Testing, CI/CD, observability
- docs/research/06_data_infrastructure/ - Database, infrastructure
- docs/research/07_human_interaction/ - Human-in-the-loop systems

---

*Generated: February 24, 2026*

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry (docs/research/knowledge_atom_registry.md)

---

## Executive Summary

This document organizes knowledge atoms by technical domain (D1-D12), providing structured analysis for each domain including key techniques ranked by evidence strength, constraints, tools, combination recipes, failure modes, cross-domain links, and identified gaps. The lateral organization enables practitioners to identify relevant knowledge atoms for specific technical challenges.

---

## D1: Agent Architecture & Orchestration

**KNOWLEDGE ATOMS:** KA-001, KA-005, KA-007, KA-010, KA-026, KA-065, KA-066, KA-079, KA-080

**KEY TECHNIQUES (ranked):**

1. **KA-007 — Mixture-of-Agents** — HIGH: 8-12% improvement over single-agent systems through collaborative agent ensembles
2. **KA-010 — Conditional Multi-Stage Recovery** — HIGH: 19% higher success rate through staged retry mechanisms
3. **KA-001 — BDI Hybrid Architecture** — MEDIUM: Combines Belief-Desire-Intent with LLMs for audit-friendly explicit mental states
4. **KA-005 — System-Theoretic Decomposition** — MEDIUM: 5 subsystems with explicit interfaces for maintainable architecture
5. **KA-065 — Federated Clusters** — MEDIUM: 3x throughput with regional coordinators for distributed workloads
6. **KA-066 — Fair-Share Scheduling** — MEDIUM: 89% reduction in task starvation through equitable resource distribution

**KEY CONSTRAINTS:**

- KA-079 — **God Agent Anti-Pattern**: Single point of failure when all capabilities converge in one agent
- KA-080 — **Chatty Communication**: 10x cost and 5x latency when agents communicate excessively

**KEY TOOLS:**

- KA-001 — BDI Framework — Audit-friendly mental state representation
- KA-005 — System Theory Modeling — Interface-based decomposition

**COMBINATION RECIPES:**

- KA-007 + KA-010 — Mixture-of-Agents with conditional recovery creates robust multi-agent systems where agent failures trigger recovery cascades
- KA-005 + KA-065 — System-theoretic decomposition combined with federated clusters enables scalable distributed architecture

**FAILURE MODES:**

- KA-079 — **God Agent breaks** when single agent becomes bottleneck — **detect** through latency monitoring — **respond** by decomposing into specialized agents
- KA-080 — **Chatty Communication breaks** during high-frequency coordination — **detect** through cost tracking — **respond** by batching messages and using hierarchical communication

**CROSS-DOMAIN LINKS:**

- KA-026 (Layered Security) also relevant to D7
- KA-009 (Worktree Isolation) also relevant to D10
- KA-008 (Hierarchical Task Decomposition) also relevant to D2

**GAPS:**

- Missing research on agent lifecycle state machines
- No established patterns for trust scoring between agents
- Limited guidance on deadlock/livelock detection in agent swarms

---

## D2: Task Management & Decomposition

**KNOWLEDGE ATOMS:** KA-002, KA-003, KA-008, KA-009, KA-040, KA-043

**KEY TECHNIQUES (ranked):**

1. **KA-002 — 4-Phase Spec-Driven Workflow** — HIGH: 56% faster development through Specify→Plan→Tasks→Implement pipeline
2. **KA-008 — Hierarchical Task Decomposition** — HIGH: 2-3 levels for simple tasks, 5-7 levels for complex tasks
3. **KA-003 — Bidirectional Specifications** — MEDIUM: Agents update specs as they discover codebase realities
4. **KA-043 — Semantic Merge** — MEDIUM: 78% automatic resolution vs 45% traditional merge
5. **KA-009 — Worktree Isolation** — MEDIUM: 67% reduction in merge conflicts through isolated worktrees

**KEY CONSTRAINTS:**

- KA-040 — **Unlimited Planning Anti-Pattern**: Token runaway when agents are allowed unlimited planning time

**KEY TOOLS:**

- KA-002 — Spec-Driven Workflow Framework — Phase-gated development
- KA-009 — Git Worktree — Branch isolation for concurrent agent work

**COMBINATION RECIPES:**

- KA-002 + KA-003 — 4-phase workflow with bidirectional specifications enables adaptive planning that evolves with codebase discovery
- KA-008 + KA-009 — Hierarchical task decomposition combined with worktree isolation enables parallel agent execution without conflicts

**FAILURE MODE:**

- KA-040 — **Unlimited Planning breaks** when token budgets are exceeded — **detect** through token usage monitoring — **respond** by implementing planning budgets and timeouts

**CROSS-DOMAIN LINKS:**

- KA-002 also relevant to D5 (Code Intelligence)
- KA-003 also relevant to D3 (Context & Prompt Engineering)
- KA-008 also relevant to D1 (Agent Architecture)

**GAPS:**

- No established patterns for dependency detection and resolution
- Limited guidance on commit generation and branch management strategies
- Missing research on conflict resolution for concurrent agent work

---

## D3: Context & Prompt Engineering

**KNOWLEDGE ATOMS:** KA-012, KA-013, KA-015, KA-016, KA-018, KA-046

**KEY TECHNIQUES (ranked):**

1. **KA-012 — LLMLingua Compression** — HIGH: 20x compression with <3% quality degradation
2. **KA-013 — Selective Context** — HIGH: 50% token reduction while retaining 97% performance
3. **KA-015 — Lost-in-Middle** — MEDIUM: U-shaped prioritization places critical information at context boundaries
4. **KA-018 — Augment Context Engine** — MEDIUM: 71% completeness improvement through intelligent context augmentation
5. **KA-016 — Context Poisoning** — CONSTRAINT: 4 attack vectors requiring disposable sessions

**KEY CONSTRAINTS:**

- KA-016 — **Context Poisoning**: Malicious context injection through 4 attack vectors requiring session isolation

**KEY TOOLS:**

- KA-012 — LLMLingua — Token compression for context optimization
- KA-018 — Augment Platform — Context augmentation engine

**COMBINATION RECIPES:**

- KA-012 + KA-013 — LLMLingua compression combined with selective context achieves maximum token reduction without quality loss
- KA-015 + KA-018 — Lost-in-middle prioritization with augment context creates intelligent context placement

**FAILURE MODES:**

- KA-016 — **Context Poisoning breaks** session security — **detect** through anomaly detection in context — **respond** by implementing disposable sessions and input validation

**CROSS-DOMAIN LINKS:**

- KA-016 also relevant to D7 (Security & Guardrails)
- KA-046 (AI Happy Path Bias) also relevant to D6

**GAPS:**

- Missing research on prompt structure and ordering optimization
- No established patterns for anti-hallucination prompt patterns
- Limited guidance on token budget management across long tasks
- No research on context refresh and rotation strategies

---

## D4: Memory & Knowledge Systems

**KNOWLEDGE ATOMS:** KA-019, KA-020, KA-070, KA-071, KA-072

**KEY TECHNIQUES (ranked):**

1. **KA-019 — Vector DB Recall** — HIGH: 85-95% recall@10 with code-specific embeddings
2. **KA-020 — GraphRAG** — HIGH: 23% improvement on multi-hop reasoning through knowledge graph integration
3. **KA-071 — LLM Migration Accuracy** — MEDIUM: 73% first-attempt, 94% with refinement for database migrations
4. **KA-070 — Declarative Schemas** — MEDIUM: 47% reduction in migration errors through schema-first design
5. **KA-072 — Contract-Aware Generation** — MEDIUM: 31% improvement in correctness through contract validation

**KEY TOOLS:**

- KA-019 — Vector Database — Semantic code search and retrieval
- KA-020 — GraphRAG — Knowledge graph augmented generation

**COMBINATION RECIPES:**

- KA-019 + KA-020 — Vector DB with GraphRAG combines semantic retrieval with knowledge graph reasoning for complex queries

**FAILURE MODES:**

- No specific failure modes identified in current research

**CROSS-DOMAIN LINKS:**

- KA-019 also relevant to D5 (Code Intelligence)
- KA-070, KA-071, KA-072 also relevant to D6 (Data Infrastructure)

**GAPS:**

- Missing research on short-term working memory architectures
- No patterns for persistent memory across sessions
- Limited guidance on auto-learning systems
- No research on cross-session retrieval optimization

---

## D5: Code Intelligence & Representations

**KNOWLEDGE ATOMS:** KA-022, KA-023, KA-024, KA-025, KA-002, KA-003

**KEY TECHNIQUES (ranked):**

1. **KA-024 — Repo Grokking** — HIGH: Sub-second queries across million-line codebases
2. **KA-022 — Semantic-Guided Traversal** — HIGH: 40-60% time reduction in code exploration
3. **KA-023 — CoSrch Hybrid Search** — HIGH: 7.60% SuccessRate@1 improvement through hybrid code search
4. **KA-025 — File Prioritization** — MEDIUM: 50-70% exploration time reduction through intelligent file ordering

**KEY TOOLS:**

- KA-024 — Code Graph Systems — Repository-wide semantic understanding
- KA-022 — Semantic Analysis Engine — Context-aware code traversal

**COMBINATION RECIPES:**

- KA-022 + KA-025 — Semantic-guided traversal with file prioritization optimizes exploration efficiency
- KA-023 + KA-024 — Hybrid search combined with repo grokking enables precise code location

**FAILURE MODES:**

- No specific failure modes identified in current research

**CROSS-DOMAIN LINKS:**

- KA-002, KA-003 also relevant to D2 (Task Management)
- KA-019 (Vector DB Recall) also relevant to D4

**GAPS:**

- Missing research on AST/CFG/DFG representations
- No established patterns for symbol indexing
- Limited guidance on taint tracking
- No research on schema inference for code

---

## D6: Testing & Validation

**KNOWLEDGE ATOMS:** KA-041, KA-042, KA-044, KA-045, KA-046, KA-047

**KEY TECHNIQUES (ranked):**

1. **KA-041 — AI Test Coverage** — HIGH: 60-80% coverage but misses edge cases
2. **KA-042 — QA Swarm** — HIGH: 40% higher bug detection than single agent
3. **KA-044 — Mutation Testing** — HIGH: r=0.75 correlation with defect detection
4. **KA-045 — Multi-Stage Testing** — MEDIUM: 60% reduction in production incidents
5. **KA-047 — CI/CD Maturity** — MEDIUM: 208x deployment frequency, 2604x recovery speed

**KEY CONSTRAINTS:**

- KA-046 — **AI Happy Path Bias**: 80% miss error handling when agents focus on success cases

**KEY TOOLS:**

- KA-041 — Test Generation Frameworks — AI-powered unit and integration test creation
- KA-044 — Mutation Testing Tools — Defect detection through code mutation

**COMBINATION RECIPES:**

- KA-041 + KA-042 — AI test coverage with QA swarm combines generation with multi-agent validation
- KA-044 + KA-045 — Mutation testing with multi-stage validation creates comprehensive quality gates

**FAILURE MODES:**

- KA-046 — **AI Happy Path Bias breaks** test quality — **detect** through edge case coverage analysis — **respond** by requiring explicit error path testing

**CROSS-DOMAIN LINKS:**

- KA-045 also relevant to D9 (CI/CD & DevOps)
- KA-047 also relevant to D9

**GAPS:**

- Missing research on property-based testing for AI-generated code
- No established patterns for behavioral testing
- Limited guidance on E2E testing for autonomous agents

---

## D7: Security & Guardrails

**KNOWLEDGE ATOMS:** KA-026, KA-027, KA-032, KA-033, KA- TECHNIQUES (ranked):**

1. **KA016

**KEY-026 — Layered Security** — HIGH: 5+ control points mandatory — no single mechanism blocks all attacks
2. **KA-027 — Hallucination Impact** — HIGH: 19.7% fabricated packages, 40-45% vulnerable code, 43% API misuse
3. **KA-033 — Over-Privileged MCP Anti-Pattern** — CONSTRAINT: Enables lateral movement when MCP has excessive privileges

**KEY CONSTRAINTS:**

- KA-032 — **Prompt-Only Security**: Easily bypassed without additional guardrails
- KA-033 — **Over-Privileged MCP**: Enables lateral movement through excessive permissions

**KEY TOOLS:**

- KA-026 — Multi-Layer Security Framework — Defense in depth implementation

**COMBINATION RECIPES:**

- KA-026 + KA-027 — Layered security with hallucination awareness creates comprehensive threat coverage

**FAILURE MODES:**

- KA-032 — **Prompt-Only Security breaks** under adversarial prompts — **detect** through red-team testing — **respond** by adding technical controls
- KA-033 — **Over-Privileged MCP breaks** when compromised — **detect** through privilege audit — **respond** by implementing least-privilege

**CROSS-DOMAIN LINKS:**

- KA-016 (Context Poisoning) also relevant to D3
- KA-027 also relevant to D8 (Model Management)

**GAPS:**

- Missing research on package verification (slopsquatting)
- No established patterns for sandboxing and isolation
- Limited guidance on secret management
- No research on MCP privilege isolation best practices

---

## D8: Model Management & Routing

**KNOWLEDGE ATOMS:** KA-036, KA-027, KA-039

**KEY TECHNIQUES (ranked):**

1. **KA-036 — Cascade Routing** — HIGH: 40-87% cost reduction through intelligent model escalation
2. **KA-027 — Hallucination Impact** — CONSTRAINT: Model-specific hallucination rates affect routing decisions

**KEY CONSTRAINTS:**

- KA-039 — **One-Model-for-Everything Anti-Pattern**: Cost inflation when premium models are used for simple tasks

**KEY TOOLS:**

- KA-036 — Model Routing Framework — Cost-aware model selection

**COMBINATION RECIPES:**

- KA-036 + KA-039 — Cascade routing prevents one-model-for-everything by routing to appropriate model tier

**FAILURE MODES:**

- KA-039 — **One-Model-for-Everything breaks** budget — **detect** through cost monitoring — **respond** by implementing cascade routing

**CROSS-DOMAIN LINKS:**

- KA-027 also relevant to D7 (Security)
- KA-036 also relevant to D1 (for multi-agent model selection)

**GAPS:**

- Missing research on model capability matrices
- No established patterns for confidence-based routing
- Limited guidance on temperature optimization per task type
- No research on multi-model adversarial review

---

## D9: CI/CD &KNOWLEDGE DevOps

** ATOMS:** KA-045, KA-047, KA-043

**KEY TECHNIQUES (ranked):**

1. **KA-047 — CI/CD Maturity** — HIGH: 208x deployment frequency, 2604x recovery speed
2. **KA-045 — Multi-Stage Testing** — MEDIUM: 60% reduction in production incidents
3. **KA-043 — Semantic Merge** — MEDIUM: 78% automatic resolution vs 45% traditional

**KEY TOOLS:**

- KA-047 — CI/CD Pipeline Frameworks — Deployment automation
- KA-043 — Semantic Merge Tools — Intelligent conflict resolution

**COMBINATION RECIPES:**

- KA-045 + KA-047 — Multi-stage testing with CI/CD maturity creates reliable deployment pipelines

**FAILURE MODES:**

- No specific failure modes identified in current research

**CROSS-DOMAIN LINKS:**

- KA-045 also relevant to D6 (Testing)
- KA-043 also relevant to D2 (Task Management)

**GAPS:**

- Missing research on self-healing pipelines
- No established patterns for canary/blue-green deployments for agent outputs
- Limited guidance on container orchestration for agents
- No research on observability integration for autonomous systems

---

## D10: Workspace & Infrastructure Management

**KNOWLEDGE ATOMS:** KA-009, KA-070

**KEY TECHNIQUES (ranked):**

1. **KA-009 — Worktree Isolation** — MEDIUM: 67% reduction in merge conflicts
2. **KA-070 — Declarative Schemas** — MEDIUM: 47% reduction in migration errors

**KEY TOOLS:**

- KA-009 — Git Worktree — Branch and workspace isolation
- KA-070 — Schema Migration Tools — Declarative infrastructure

**COMBINATION RECIPES:**

- KA-009 + KA-070 — Worktree isolation with declarative schemas enables safe concurrent agent work

**FAILURE MODES:**

- No specific failure modes identified in current research

**CROSS-DOMAIN LINKS:**

- KA-009 also relevant to D2 (Task Management)

**GAPS:**

- Missing research on file organization during task execution
- No established patterns for state persistence
- Limited guidance on artifact management
- No research on environment provisioning for agents

---

## D11: Human Interaction

**KNOWLEDGE ATOMS:** KA-056, KA-057, KA-058, KA-060, KA-061, KA-062, KA-063, KA-064

**KEY TECHNIQUES (ranked):**

1. **KA-058 — HITL Effectiveness** — HIGH: 70-80% intervention reduction while improving success rates
2. **KA-057 — Confidence-Based Escalation** — HIGH: 70% cost reduction through intelligent escalation
3. **KA-056 — Autonomy Levels** — MEDIUM: 5 levels from operator to observer
4. **KA-060 — Auto-Approval Gateway** — MEDIUM: Risk-based action approval
5. **KA-063 — Cognitive Load Optimization** — MEDIUM: Batching, summarization, filtering to reduce human overload
6. **KA-062 — Apprise Notifications** — MEDIUM: 80+ service integration for alerts

**KEY CONSTRAINTS:**

- KA-064 — **Opaque AI Decisions Anti-Pattern**: User distrust when AI reasoning is not visible

**KEY TOOLS:**

- KA-061 — Structured Clarification Tool — ask_followup_question framework for ambiguous requests
- KA-062 — Apprise — Multi-channel notification system

**COMBINATION RECIPES:**

- KA-057 + KA-060 — Confidence-based escalation with auto-approval creates efficient human oversight
- KA-058 + KA-063 — HITL with cognitive load optimization maximizes human effectiveness

**FAILURE MODES:**

- KA-064 — **Opaque AI Decisions break** user trust — **detect** through user feedback — **respond** by implementing explainable AI

**CROSS-DOMAIN LINKS:**

- KA-056 also relevant to D1 (Agent Architecture)
- KA-057 also relevant to D8 (Model Management)

**GAPS:**

- Missing research on explainable plan visualization
- No established patterns for notification prioritization
- Limited guidance on approval gateway thresholds

---

## D12: Self-Improvement & Optimization

**KNOWLEDGE ATOMS:** KA-036 (implicit cost optimization), KA-051

**KEY TECHNIQUES (ranked):**

1. **KA-051 — Compliance Envelope** — MEDIUM: Standardized evidence per run for audit trails
2. **KA-036 — Cascade Routing** — IMPLICIT: Cost optimization through model selection

**KEY TOOLS:**

- KA-051 — Compliance Tracking System — Evidence collection for audits

**COMBINATION RECIPES:**

- KA-036 + KA-051 — Cost optimization with compliance tracking enables efficient self-improvement

**FAILURE MODES:**

- No specific failure modes identified in current research

**CROSS-DOMAIN LINKS:**

- KA-036 also relevant to D8 (Model Management)
- KA-051 also relevant to D7 (Security - governance)

**GAPS:**

- Missing research on prompt optimization loops
- No established patterns for agent performance regression detection
- Limited guidance on workflow A/B testing
- No research on skill enable/disable for token efficiency

---

## Summary Statistics

| Domain | Atom Count | Primary Focus |
|--------|------------|----------------|
| D1: Agent Architecture & Orchestration | 9 | Multi-agent design patterns |
| D2: Task Management & Decomposition | 6 | Work breakdown and isolation |
| D3: Context & Prompt Engineering | 6 | Token optimization, security |
| D4: Memory & Knowledge Systems | 5 | Retrieval and knowledge graphs |
| D5: Code Intelligence & Representations | 6 | Code exploration and search |
| D6: Testing & Validation | 6 | AI test generation, quality gates |
| D7: Security & Guardrails | 5 | Defense in depth, hallucination |
| D8: Model Management & Routing | 3 | Cost optimization, cascade routing |
| D9: CI/CD & DevOps | 3 | Deployment automation |
| D10: Workspace & Infrastructure | 2 | Isolation, declarative infra |
| D11: Human Interaction | 8 | HITL, escalation, notifications |
| D12: Self-Improvement | 2 | Optimization, compliance |

---

## Recommended Next Subtasks

1. **Cross-Domain Integration Analysis**: Map how atoms from different domains interact in real-world scenarios
2. **Gap Prioritization**: Rank identified gaps by impact and feasibility of research
3. **Pattern Extraction**: Identify combination recipes that span multiple domains
4. **Tool Evaluation**: Deep-dive into specific tools for each domain with capability matrices

---

## Sources

- docs/research/knowledge_atom_registry.md - Primary knowledge atom source
- docs/research/01_meta_architecture/ - System design, security, economics
- docs/research/02_agent_orchestration/ - Agent design, distributed systems
- docs/research/03_context_memory_intelligence/ - Context, memory, reasoning
- docs/research/04_code_intelligence/ - Code exploration, specification
- docs/research/05_sdlc_automation/ - Testing, CI/CD, observability
- docs/research/06_data_infrastructure/ - Database, infrastructure
- docs/research/07_human_interaction/ - Human-in-the-loop systems

---

*Generated: February 24, 2026*

