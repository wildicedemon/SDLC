# Prong 1: Agent Orchestration Knowledge Atoms

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

# Prong 1: Agent Orchestration Knowledge Atoms

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

# Prong 1: Agent Orchestration Knowledge Atoms

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

# Prong 1: Agent Orchestration Knowledge Atoms

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

# Prong 1: Agent Orchestration Knowledge Atoms

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

# Prong 1: Agent Orchestration Knowledge Atoms

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

# Prong 1: Agent Orchestration Knowledge Atoms

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

# Prong 1: Agent Orchestration Knowledge Atoms

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

# Prong 1: Agent Orchestration Knowledge Atoms

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

# Prong 1: Agent Orchestration Knowledge Atoms

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

# Prong 1: Agent Orchestration Knowledge Atoms

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

**Extraction Date**: 2026-02-24  
**Research Domain**: Agent Orchestration (02_agent_orchestration)  
**Sources**: agent_system_design/, distributed_orchestration/, task_architecture/  
**Total Atoms**: 42 (STRONG: 22, MODERATE: 15, WEAK: 5)

---

## STRONG Evidence Atoms

### KA-AGENT-001
**TYPE**: METRIC  
**CONTENT**: Explicit mode switching reduces task drift by 34% compared to implicit switching, though it introduces latency from context reloading.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D3  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC7

---

### KA-AGENT-002
**TYPE**: TECHNIQUE  
**CONTENT**: Conditional multi-stage prompting chains through diagnosis → planning → recovery stages using zero-shot prompting, achieving 19% higher success rates on Tasks-from-Description benchmarks compared to single-stage recovery.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D5  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-003
**TYPE**: TECHNIQUE  
**CONTENT**: The TEA (Task-Environment-Agent) Protocol achieves 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents, modeling three explicit components with clear interfaces.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-004
**TYPE**: TECHNIQUE  
**CONTENT**: Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks at the cost of 3-5x compute overhead. Each layer receives outputs from the previous layer and produces refined outputs.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-005
**TYPE**: TECHNIQUE  
**CONTENT**: Adversarial review patterns with dedicated critic agents achieve 40% higher bug detection rates compared to single-agent review, validated in code review research.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-006
**TYPE**: METRIC  
**CONTENT**: Agents with clarification capabilities (ask_followup_question pattern) achieve 23% higher task success rates by preventing incorrect assumptions from ambiguous task specifications.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-007
**TYPE**: FAILURE_MODE  
**CONTENT**: Deadlock rates of 2-7% occur in complex multi-agent coding workflows without explicit prevention mechanisms. Detection strategies include wait-for graphs, timeout-based detection, and dependency analysis.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-008
**TYPE**: TECHNIQUE  
**CONTENT**: Hierarchical multi-agent orchestration organizes agents in tree structures with planner/manager at root decomposing tasks for specialist sub-agents, achieving 25% error reduction in dependency-heavy tasks. Validated in ChatDev, MetaGPT, and AgentOrchestra.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_01.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-009
**TYPE**: TRADEOFF  
**CONTENT**: Specialist agents outperform generalist agents by 2-3x on scoped SDLC subtasks, achieving 28% improvement on SWE-bench; however, specialization introduces coordination overhead and potential single points of failure.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-010
**TYPE**: METRIC  
**CONTENT**: Federated cluster architecture with regional coordinators achieves 3x throughput improvement over single-coordinator architectures for geographically distributed teams, while maintaining low latency for local operations.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5, PC8

---

### KA-AGENT-011
**TYPE**: METRIC  
**CONTENT**: Fair-share scheduling reduces task starvation by 89% compared to simple priority queues in multi-agent coding systems, ensuring equitable resource distribution across users/projects.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-012
**TYPE**: METRIC  
**CONTENT**: Adaptive throttling maintains 95th percentile latency within 2x baseline under 5x load, while shed-load approaches see 10x latency degradation.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-013
**TYPE**: METRIC  
**CONTENT**: CLI-based multi-agent systems show 2.5x throughput improvement over single-agent execution for parallel tasks, with worktree isolation enabling headless orchestration.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/comparisons.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-014
**TYPE**: CONSTRAINT  
**CONTENT**: Byzantine fault tolerance requires 3f+1 nodes to tolerate f Byzantine failures. This applies to security-critical multi-agent systems requiring guaranteed correctness despite malicious behavior.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/overview.md, docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D1, D2, D11  
**SDLC_PHASES**: P7-P8  
**PRODUCTS**: PC1, PC5, PC9

---

### KA-AGENT-015
**TYPE**: METRIC  
**CONTENT**: Spec-driven workflows reduce development time by 56% and scope creep by 56% through explicit specification boundaries and structured task decomposition.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D3, D5  
**SDLC_PHASES**: P1-P3  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-016
**TYPE**: METRIC  
**CONTENT**: Worktree isolation reduces merge conflicts by 67% compared to shared branch development in multi-agent coding systems, enabling parallel agent execution with git-based coordination.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D2, D9, D10  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-017
**TYPE**: METRIC  
**CONTENT**: Semantic merging with LLM assistance achieves 78% automatic resolution rate compared to 45% for traditional three-way merge, understanding code semantics for intelligent conflict resolution.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D4, D9  
**SDLC_PHASES**: P4-P8  
**PRODUCTS**: PC1, PC2, PC6

---

### KA-AGENT-018
**TYPE**: METRIC  
**CONTENT**: Multi-agent QA swarms achieve 40% higher bug detection than single-agent validation, deploying multiple agents with different focuses (correctness, security, performance, style).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-019
**TYPE**: METRIC  
**CONTENT**: Async DAG execution achieves 2.3x speedup over sequential execution for typical SDLC workflows through task-level parallelism and pipeline parallelism.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC6

---

### KA-AGENT-020
**TYPE**: CONSTRAINT  
**CONTENT**: Optimal task decomposition depth varies by complexity: 2-3 levels for simple tasks, 5-7 levels for complex SDLC workflows. Over-decomposition increases coordination overhead; under-decomposition creates unmanageable units.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-021
**TYPE**: TOOL  
**CONTENT**: Agent GPA framework scores Goal-Plan-Action phases with 95% error detection and 86% error localization, outperforming baselines by 1.8x on diverse tasks.  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/perplexityai_research_overview_29.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-022
**TYPE**: METRIC  
**CONTENT**: Framework-level design choices in multi-agent systems can increase latency by 100x, reduce planning accuracy by 30%, and lower coordination success from 90% to 30% (MAFBench unified evaluation findings).  
**EVIDENCE_STRENGTH**: STRONG  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:33)  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC5

---

## MODERATE Evidence Atoms

### KA-AGENT-023
**TYPE**: FAILURE_MODE  
**CONTENT**: Livelock occurs when agents remain active but make no progress, particularly problematic in systems with retry loops and self-correction mechanisms. Detection requires progress metrics and thresholds, not just activity monitoring.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-024
**TYPE**: ANTI_PATTERN  
**CONTENT**: Monolithic FM-Centric Design anti-pattern occurs when relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration, leading to world modeling failures and unpredictable behavior.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-025
**TYPE**: ANTI_PATTERN  
**CONTENT**: Silent State Drift anti-pattern allows agent state to drift without validation, leading to corrupted beliefs, stale context, and cascading errors from invalid assumptions. Remediation requires state validation, context sanitization, and lineage tracking.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D3, D8  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-026
**TYPE**: ANTI_PATTERN  
**CONTENT**: Over-Delegation anti-pattern decomposes tasks too finely, creating excessive coordination overhead and losing task coherence. Communication overhead dominates execution time with lost context between subtask handoffs.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-027
**TYPE**: RECIPE  
**CONTENT**: System-Theoretic Agent Decomposition pattern: Decompose into five subsystems (Reasoning, Perception, Action, Learning, Communication) with explicit interfaces enabling independent development, testing, and scaling.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P1-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-028
**TYPE**: RECIPE  
**CONTENT**: Lease-Based Distributed Lock pattern: Acquire locks with time-based leases that automatically expire, preventing deadlock from crashed agents holding locks indefinitely. Requires lease duration tuning.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-029
**TYPE**: ANTI_PATTERN  
**CONTENT**: Single Coordinator Bottleneck anti-pattern routes all coordination through a single central agent, creating scalability limits, single point of failure, and increased latency with cluster size.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/patterns.md  
**DOMAINS**: D2, D9  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC5, PC8

---

### KA-AGENT-030
**TYPE**: FAILURE_MODE  
**CONTENT**: 3-8% of automatically generated task graphs contain cycles requiring resolution. Cycle detection is critical as cycles indicate circular dependencies preventing task completion.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-031
**TYPE**: RECIPE  
**CONTENT**: Atomic Task Creation pattern defines tasks with single responsibility, self-contained context, verifiable success criteria, reversible changes, and idempotent execution enabling safe retries.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/overview.md, docs/research/02_agent_orchestration/task_architecture/patterns.md  
**DOMAINS**: D1, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-032
**TYPE**: TRADEOFF  
**CONTENT**: MCP standardization reduces integration effort and provides type safety through JSON Schema, but limits tool expressiveness to protocol capabilities and introduces protocol versioning challenges.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md, docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_04.md  
**DOMAINS**: D1, D2, D4  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-033
**TYPE**: TOOL  
**CONTENT**: AgentOps frameworks provide production monitoring dashboards with heartbeat monitoring, progress metrics, anomaly detection, and automatic intervention for agent health surveillance.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/overview.md, docs/research/02_agent_orchestration/agent_system_design/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-034
**TYPE**: RECIPE  
**CONTENT**: Multi-Stage Validation Pipeline executes validation in stages with increasing cost/precision: syntax (<1s), type checking (1-10s), linting (1-5s), unit tests (10s-5min), integration tests (1-30min), security scanning (10s-5min).  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/task_architecture/patterns.md, docs/research/02_agent_orchestration/task_architecture/comparisons.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-035
**TYPE**: TRADEOFF  
**CONTENT**: Reflection patterns boost self-critique accuracy by 35% but add compute overhead. Specialist depth vs generalist flexibility tradeoff: specialists win for SDLC by 28% on SWE-bench.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D7  
**SDLC_PHASES**: P6-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-036
**TYPE**: RECIPE  
**CONTENT**: Hierarchical decomposition dominates enterprise SDLC: Supervisor routes to specialists (Coder→Tester→Reviewer), reducing latency 25% vs single-agent. Swarm patterns excel for creative tasks via debate/consensus with 40% error reduction.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_26.md  
**DOMAINS**: D1, D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-037
**TYPE**: TECHNIQUE  
**CONTENT**: AdaptOrch topology routing algorithm maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time across four canonical topologies: parallel, sequential, hierarchical, hybrid.  
**EVIDENCE_STRENGTH**: MODERATE  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/references.md (kimi:16, kimi:5), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:5)  
**DOMAINS**: D2, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

## WEAK Evidence Atoms

### KA-AGENT-038
**TYPE**: TECHNIQUE  
**CONTENT**: Stigmergic coordination pattern enables agents to communicate indirectly through environment modifications (e.g., codebase, task queue), scaling to large agent counts without central coordinator but introducing emergent behavior unpredictability.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/patterns.md  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-039
**TYPE**: TECHNIQUE  
**CONTENT**: Agent Swarm self-directed parallel orchestration achieves 4.5x latency reduction over single-agent through dynamic task decomposition with heterogeneous sub-problem execution.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:12)  
**DOMAINS**: D1, D2  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-040
**TYPE**: TRADEOFF  
**CONTENT**: Observability adds 5-10% latency overhead but boosts Mean Time To Recovery (MTTR) by 70%. Full state logging risks privacy vs compliance needs.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D5, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

### KA-AGENT-041
**TYPE**: TOOL  
**CONTENT**: D3MAS hierarchical coordination framework achieves 47.3% knowledge duplication reduction and 8.7-15.6% accuracy improvement through task decomposition filtering irrelevant sub-problems early.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/distributed_orchestration/references.md (kimi:8), docs/research/02_agent_orchestration/task_architecture/references.md (kimi:3)  
**DOMAINS**: D2, D3, D6  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4

---

### KA-AGENT-042
**TYPE**: COMBINATION  
**CONTENT**: Multi-agent systems achieve 95% uptime in benchmarks using distributed heartbeats for failure detection, combining identity governance (Okta provisioning gates) with observability platforms for real-time anomalies.  
**EVIDENCE_STRENGTH**: WEAK  
**SOURCE**: docs/research/02_agent_orchestration/agent_system_design/perplexityai_research_overview_28.md  
**DOMAINS**: D1, D2, D7  
**SDLC_PHASES**: P2-P8  
**PRODUCTS**: PC1, PC2, PC4, PC7

---

## Deduplication Notes

1. **Mode Switching (KA-AGENT-001)**: Consolidated from overview.md and patterns.md - both cite 34% drift reduction.

2. **Conditional Multi-Stage Recovery (KA-AGENT-002)**: Merged findings from overview.md (19% TfD success) and patterns.md (zero-shot chaining).

3. **TEA Protocol (KA-AGENT-003)**: Consolidated 83% GAIA accuracy claim from multiple source references.

4. **Fair-Share Scheduling (KA-AGENT-011)**: Merged 89% starvation reduction from overview.md and patterns.md.

5. **Adversarial Review (KA-AGENT-005, KA-AGENT-018)**: Both cite 40% bug detection improvement; KA-AGENT-005 focuses on pattern, KA-AGENT-018 on multi-agent QA swarm validation implementation.

6. **Optimal Decomposition Depth (KA-AGENT-020)**: Consolidated from overview.md and comparisons.md depth guidelines.

## Knowledge Gaps

1. **Limited empirical data on deadlock/livelock rates in production coding agents** - Current estimates (2-7%) are framework-specific.

2. **Optimal mode granularity** - No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic).

3. **Trust scoring calibration** - No standard methodology for calibrating trust scores for new agents without historical data.

4. **Cross-repo context management at scale** - Limited standardization for managing context across 100+ repositories.

5. **Real-time observability for 100+ agent meshes** - Unvalidated approaches for large-scale swarm monitoring.

## Source Attribution Summary

| Source Directory | Primary Atom Count | Evidence Strength Distribution |
|-----------------|-------------------|-------------------------------|
| agent_system_design | 18 | STRONG: 12, MODERATE: 4, WEAK: 2 |
| distributed_orchestration | 14 | STRONG: 7, MODERATE: 5, WEAK: 2 |
| task_architecture | 10 | STRONG: 3, MODERATE: 6, WEAK: 1 |

## Domain/Phase/Product Tagging Legend

**Domains (D1-D12)**:
- D1: Agent Coordination & Multi-Agent Systems
- D2: Task Orchestration & Workflow
- D3: Context Management & Memory
- D4: Tool Use & MCP Integration
- D5: Quality Assurance & Validation
- D6: Architecture Patterns & Design
- D7: Performance & Optimization
- D8: Failure Modes & Recovery
- D9: Distributed Systems
- D10: Infrastructure & Scaling
- D11: Security & Compliance
- D12: Human-AI Interaction

**SDLC Phases (P1-P8)**:
- P1: Requirements & Planning
- P2: Architecture & Design
- P3: Implementation/Coding
- P4: Code Review
- P5: Testing
- P6: Integration
- P7: Deployment
- P8: Operations/Maintenance

**Products (PC1-PC10)**:
- PC1: Core Agent Framework
- PC2: Multi-Agent Orchestrator
- PC3: Context Management System
- PC4: Quality Assurance Engine
- PC5: Distributed Task Scheduler
- PC6: CI/CD Integration
- PC7: Monitoring & Observability
- PC8: Enterprise Scale Platform
- PC9: Security & Compliance Module
- PC10: Developer Experience Tools

---

*End of Prong 1 Agent Orchestration Knowledge Atom Extraction*

