# Prong 2 - DOMAIN SPLIT (Lateral Organization)

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

# Prong 2 - DOMAIN SPLIT (Lateral Organization)

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

# Prong 2 - DOMAIN SPLIT (Lateral Organization)

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

# Prong 2 - DOMAIN SPLIT (Lateral Organization)

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

# Prong 2 - DOMAIN SPLIT (Lateral Organization)

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

# Prong 2 - DOMAIN SPLIT (Lateral Organization)

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

# Prong 2 - DOMAIN SPLIT (Lateral Organization)

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

# Prong 2 - DOMAIN SPLIT (Lateral Organization)

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

# Prong 2 - DOMAIN SPLIT (Lateral Organization)

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

# Prong 2 - DOMAIN SPLIT (Lateral Organization)

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

# Prong 2 - DOMAIN SPLIT (Lateral Organization)

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

**Atoms parsed**: 37 explicit KA from `distilled/prong1_master_atoms.md` (file claims 68 but lists ~37 with summaries; used all explicit IDs). Assignments based on content analysis, using tags as starting point, reassigning where better fit (e.g., model routing to D8, worktrees to D10). Multi-domain where applicable. All atoms referenced. Ranked by EVIDENCE_STRENGTH (STRONG > MODERATE), then relevance/ID.

## DOMAIN: D1: Agent Architecture & Orchestration (patterns, modes, delegation, consensus)

**KNOWLEDGE ATOMS**: [KA-001, KA-003, KA-004, KA-006, KA-009, KA-010, KA-011, KA-012, KA-015, KA-016, KA-018, KA-019, KA-020, KA-021, KA-022, KA-023] (17 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-006 — Spec-driven workflows with 4-phase gates (Specify, Plan, Tasks, Implement) reduce development time by 56%. — STRONG
2. KA-004 — Event-sourced agent journaling with immutable append-only logs capturing input context hash, model/version, tool invocations, artifact diffs, and policy decisions. — STRONG
3. KA-009 — Policy-as-code with runtime adjudication combining preflight static checks with runtime policy decisions at tool boundaries. — MODERATE
4. KA-010 — Ephemeral scoped credential broker issuing short-lived least-privilege credentials per task/tool invocation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-019 — One-Model-for-Everything uses premium model for all tasks, causing unnecessary cost inflation.
 - KA-020 — Policy-in-Prompt Only relies on prompt instructions without runtime enforcement, easy bypass.
 - KA-022 — Strict determinism for compliance vs bounded stochasticity for agility tradeoff.

**KEY TOOLS**:
 - None explicit.

**COMBINATION RECIPES**:
 - KA-023 — Cost-first pattern stack: Cascade routing + semantic cache + budget decomposition for lowest spend with acceptable quality.

**FAILURE MODES**:
 - KA-018 — Action Logs Without Decision Context leads to weak audit defensibility and slow incident triage; mitigate with structured decision records. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-001 also relevant to D8
 - KA-002 also relevant to D3
 - KA-003 also relevant to D8

**GAPS**:
 - Specific delegation/consensus mechanisms (e.g., leader election, quorum voting).
 - Multi-agent coordination primitives (e.g., shared blackboards).

## DOMAIN: D2: Task Management & Decomposition (hierarchies, deps, parallel, commits)

**KNOWLEDGE ATOMS**: [KA-017, KA-029, KA-030, KA-031, KA-032, KA-033, KA-034, KA-039, KA-040, KA-041, KA-042] (11 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-029 — Explicit mode boundaries and switching reduce task drift by 34% compared to implicit context-based transitions. — STRONG
2. KA-030 — Mixture-of-Agents (MoA) layered voting architecture achieves 8-12% improvement over single-agent baselines on coding benchmarks. — STRONG
3. KA-031 — Conditional multi-stage prompting with zero-shot chaining (diagnosis-planning-recovery) achieves 19% higher success rates on TfD benchmarks. — STRONG
4. KA-032 — Adversarial review with dedicated critic agents achieves 40% higher bug detection rates compared to single-agent review. — STRONG
5. KA-033 — Structured clarification prompting (e.g., Kilo ask_followup_question) achieves 23% higher task success rates by preventing incorrect assumptions. — STRONG
6. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67% in multi-agent coding workflows. — STRONG

**KEY CONSTRAINTS**:
 - KA-042 — MoA architectures trade 3-5x compute overhead for 8-12% performance improvement on coding tasks. — STRONG

**KEY TOOLS**:
 - KA-033 — ask_followup_question — structured user clarification.

**FAILURE MODES**:
 - KA-017 — Unlimited Recursive Planning causes token runaway and missed SLAs; detect with depth thresholds, respond with early termination. — MODERATE
 - KA-041 — Deadlock in multi-agent workflows occurs at 2-7% rate without prevention; detect with wait-for graphs or timeouts. — MEDIUM

**CROSS-DOMAIN LINKS**:
 - KA-032 also relevant to D6
 - KA-033 also relevant to D7, D11

**GAPS**:
 - Dependency graph management for parallel execution.
 - Commit atomicity in distributed task hierarchies.

## DOMAIN: D3: Context & Prompt Engineering (window opt, compression, anti-halluc, token mgmt)

**KNOWLEDGE ATOMS**: [KA-002, KA-008, KA-035, KA-036] (4 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-002 — Semantic caching using embeddings achieves 31-90% reduction in redundant input tokens by matching intent rather than exact strings. — STRONG
2. KA-035 — GraphRAG (knowledge graphs + vector retrieval) achieves 23% improvement on multi-hop reasoning tasks. — STRONG
3. KA-036 — LLMLingua prompt compression achieves 20x compression ratio with <3% performance degradation on reasoning tasks. — STRONG
4. KA-008 — Self-consistency sampling multiple reasoning paths and selecting via majority vote reduces stochastic errors by 7-19%. — MODERATE

**CROSS-DOMAIN LINKS**:
 - KA-002 also relevant to D1, D4

**GAPS**:
 - Advanced anti-hallucination techniques beyond retrieval (e.g., fact-checking loops).
 - Dynamic token budget allocation across agent turns.

## DOMAIN: D4: Memory & Knowledge Systems (short/long mem, vector DB, KG)

**KNOWLEDGE ATOMS**: [KA-007, KA-013, KA-014] (3 atoms)

**KEY TECHNIQUES** (ranked):
1. KA-007 — BM25 + dense retrieval achieves 67% reduction in hallucinations for code generation. — MODERATE

**KEY CONSTRAINTS**:
 - KA-013 — 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting). — STRONG
 - KA-014 — 40-45% of AI-generated code contains exploitable security vulnerabilities. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-007 relevant to D3 (anti-halluc)

**GAPS**:
 - Long-term memory persistence strategies (e.g., vector DB sharding).
 - Knowledge graph construction/updates for codebases.

## DOMAIN: D5: Code Intelligence & Representations (AST/CFG/DFG/CPG, tools like Tree-sitter)

**KNOWLEDGE ATOMS**: [KA-037, KA-038] (reassigned based on content: code search/repair)

**KEY TECHNIQUES** (ranked):
1. KA-037 — Hybrid semantic-syntactic search (CoSrch structure-aware) achieves 7.6% improvement in SuccessRate@1 for code retrieval. — STRONG
2. KA-038 — Automated Program Repair (APR) achieves 70-85% success rates on single-line bugs with adequate test coverage. — STRONG

**GAPS**:
 - AST-based semantic understanding (Tree-sitter integration).
 - CFG/DFG for control/data flow analysis.

## DOMAIN: D6: Testing & Validation (test gen, mutation, quality gates)

**KNOWLEDGE ATOMS**: [] (none primary; KA-032 adversarial review cross-link)

**GAPS**:
 - Automated test generation techniques.
 - Mutation testing for agent-generated code.

## DOMAIN: D7: Security & Guardrails (injection def, halluc detect, sandbox)

**KNOWLEDGE ATOMS**: [KA-005, KA-033] (KA-005 reassigned: guardrails; KA-033 tagged)

**KEY TECHNIQUES** (ranked):
1. KA-005 — Layered guardrail envelope combining input filtering, tool-call policy validation, output schema checks, and post-action attestation. — STRONG

**CROSS-DOMAIN LINKS**:
 - KA-033 also relevant to D2, D11

**GAPS**:
 - Sandboxing for tool execution.
 - Injection defense specifics.

## DOMAIN: D8: Model Management & Routing (capability matrices, routing, temp opt)

**KNOWLEDGE ATOMS**: [KA-001, KA-003] (reassigned: model cascades/routing)

**KEY TECHNIQUES** (ranked):
1. KA-001 — Model cascades and dynamic routing achieve 40-87% cost reduction... — STRONG
2. KA-003 — Cascade Router with Confidence Escalation... — STRONG

**GAPS**:
 - Capability matrices for routing decisions.
 - Temperature optimization strategies.

## DOMAIN: D9: CI/CD & DevOps (pipelines, canary, observability)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Agentic CI/CD pipeline integration.
 - Canary deployments for AI changes.

## DOMAIN: D10: Workspace & Infra Mgmt (branches, worktrees, cleanup)

**KNOWLEDGE ATOMS**: [KA-034] (reassigned: worktree isolation)

**KEY TECHNIQUES** (ranked):
1. KA-034 — Worktree isolation (branch-per-task) reduces merge conflicts by 67%... — STRONG

**GAPS**:
 - Automated workspace cleanup protocols.
 - Multi-worktree orchestration.

## DOMAIN: D11: Human Interaction (escalation, approvals)

**KNOWLEDGE ATOMS**: [KA-033] (reassigned partial: clarification prompting)

**KEY TECHNIQUES** (ranked):
1. KA-033 — Structured clarification prompting... — STRONG

**GAPS**:
 - Escalation waterfalls and approval workflows.
 - Human-in-loop feedback loops.

## DOMAIN: D12: Self-Improvement (prompt opt, perf regression)

**KNOWLEDGE ATOMS**: [] 

**GAPS**:
 - Online learning for prompt optimization.
 - Performance regression detection.

**Verification**: All 37 atoms referenced at least once (some multi-domain)."

