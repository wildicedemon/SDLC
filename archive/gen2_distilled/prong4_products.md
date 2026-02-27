# Prong 4 - PRODUCT MAPPING (Top-Down Assignment)

Atoms assigned to PC1-PC10 based on explicit PRODUCTS tags in prong1_master_atoms.md (66 tags across 68 atoms), supplemented by relevant atoms from prong2_domains.md (D1-D12 groupings) and prong3_phases.md (P1-P8 workflows). 2-5 instances per category, derived from prominent atoms (STRONG evidence prioritized). Instances named specifically from atom content/research (e.g., 'Mode: SemanticCache'). 

YAML templates standardized per category, filled completely with atom references. Techniques ranked by evidence>specificity>cost-efficiency. Combos step-by-step, cost-aware (e.g., cheap retrieval before expensive reasoning). Gaps flagged where data sparse (e.g., PC6/PC10).

## PC1: MODES

### INSTANCE: SemanticCacheMode
KNOWLEDGE ATOMS CONSUMED: [KA-002, KA-036]
DRAFT SPEC:
```yaml
mode: semantic_cache_mode
purpose: Reduce redundant token processing by 31-90% via embedding-based intent matching and prompt compression.
description: Activates semantic caching for repeated queries; compresses prompts with LLMLingua before flagship model use.
entry_conditions:
  - Repeated task patterns detected
  - Context exceeds 70% window
techniques:
  - rank1: KA-002 (semantic caching, STRONG, low-cost embeddings)
  - rank2: KA-036 (LLMLingua compression, STRONG, 20x ratio)
combos_step_by_step:
  1. Embed query (cheap)
  2. Cache hit? Return
  3. Compress + route to model
cost_awareness: Prioritizes embedding API (<$0.01) over full LLM calls.
tools: [read_file, search_files]
phases: P1
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: PromptCompressorMode
KNOWLEDGE ATOMS CONSUMED: [KA-036]
DRAFT SPEC:
```yaml
mode: prompt_compressor_mode
purpose: Achieve 20x prompt compression with <3% reasoning degradation.
description: Automatically compresses long contexts for efficiency in analysis phases.
entry_conditions:
  - Token count > threshold
techniques:
  - rank1: KA-036 (LLMLingua, STRONG)
combos_step_by_step:
  1. Detect long prompt
  2. Apply compression
  3. Verify coherence
cost_awareness: Saves 95% tokens upfront.
tools: []
phases: P1, P3
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: [Dynamic threshold tuning]

### INSTANCE: CostOptimizerMode
KNOWLEDGE ATOMS CONSUMED: [KA-002]
DRAFT SPEC:
```yaml
mode: cost_optimizer_mode
purpose: Dynamically manage context to minimize costs during onboarding.
description: Combines caching with model routing for discovery.
entry_conditions:
  - New workspace scan
techniques:
  - rank1: KA-002 (semantic caching, STRONG)
combos_step_by_step:
  1. Cache file reads
  2. Compress summaries
cost_awareness: Targets $5-8/task unconstrained baseline reduction.
tools: [list_files]
phases: P1
confidence: MED
```
CONFIDENCE: MED
GAPS: [Integration with routing]

## PC2: SKILLS

### INSTANCE: CascadeRouter
KNOWLEDGE ATOMS CONSUMED: [KA-001, KA-003, KA-011]
DRAFT SPEC:
```yaml
skill: cascade_router
purpose: Route tasks to optimal models, achieving 40-87% cost reduction.
description: Confidence-based escalation from cheap to flagship models.
entry_conditions:
  - Task classification complete
techniques:
  - rank1: KA-003 (Cascade Router, STRONG)
  - rank2: KA-001 (dynamic routing, STRONG)
metrics: KA-011 (unconstrained $5-8/task)
combos_step_by_step:
  1. Classify task (cheap model)
  2. Confidence low? Escalate
  3. Verify output
cost_awareness: Budget decomposition per step.
tools: []
domains: D1, D8
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: ModelEscalator
KNOWLEDGE ATOMS CONSUMED: [KA-003]
DRAFT SPEC:
```yaml
skill: model_escalator
purpose: Escalate based on verifier scores for 40-80% savings.
description: Verifier-first low-cost routing.
techniques:
  - rank1: KA-003 (confidence escalation, STRONG)
combos_step_by_step:
  1. Low-cost attempt
  2. Verifier check
  3. Escalate if fail
cost_awareness: Verifier <1% full cost.
phases: P1
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: [Verifier definition]

## PC3: WORKFLOWS

### INSTANCE: MoAVotingWorkflow
KNOWLEDGE ATOMS CONSUMED: [KA-030, KA-042, KA-039]
DRAFT SPEC:
```yaml
workflow: moa_voting
purpose: 8-12% perf gain via Mixture-of-Agents layered voting.
description: Multiple agents vote on outputs for coding tasks.
entry_conditions:
  - Complex implementation needed
techniques:
  - rank1: KA-030 (MoA, STRONG)
  - rank2: KA-042 (tradeoff 3-5x compute, STRONG)
metrics: KA-039 (83% GAIA accuracy)
combos_step_by_step:
  1. Parallel agents generate
  2. Vote/majority
  3. Critic verify
cost_awareness: Parallel cheap models first.
tools: [execute_command]
domains: D2
phases: P3, P4
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: ExplicitModeSwitching
KNOWLEDGE ATOMS CONSUMED: [KA-029]
DRAFT SPEC:
```yaml
workflow: explicit_mode_switch
purpose: Reduce task drift by 34% with boundary switching.
description: Strict mode transitions (architect -> code).
techniques:
  - rank1: KA-029 (explicit boundaries, STRONG)
combos_step_by_step:
  1. Check mode fit
  2. Switch via tool
  3. Confirm
cost_awareness: Mode-specific optimization.
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: WorktreeIsolation
KNOWLEDGE ATOMS CONSUMED: [KA-034]
DRAFT SPEC:
```yaml
workflow: worktree_isolation
purpose: 67% merge conflict reduction via branch-per-task.
description: Task-specific worktrees.
techniques:
  - rank1: KA-034 (worktree, STRONG)
combos_step_by_step:
  1. Create worktree
  2. Work in isolation
  3. Merge/PR
cost_awareness: Git ops low cost.
tools: [mcp_github_create_branch]
phases: P4, P7
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: ClarificationLoop
KNOWLEDGE ATOMS CONSUMED: [KA-033]
DRAFT SPEC:
```yaml
workflow: clarification_loop
purpose: 23% higher success via structured questions.
description: ask_followup_question integration.
techniques:
  - rank1: KA-033 (structured prompting, STRONG)
combos_step_by_step:
  1. Detect ambiguity
  2. Ask with options
  3. Incorporate response
cost_awareness: Human loop only when needed.
tools: [ask_followup_question]
domains: D2, D7, D11
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: SpecDrivenGates
KNOWLEDGE ATOMS CONSUMED: [KA-006]
DRAFT SPEC:
```yaml
workflow: spec_driven_gates
purpose: 56% dev time reduction with 4-phase gates.
description: Specify-Architect-Code-Review.
techniques:
  - rank1: KA-006 (4-phase, STRONG)
combos_step_by_step:
  1. Specify
  2. Plan/todo
  3. Implement
  4. Gates
phases: P1-P4
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

## PC4: PROMPTS

### INSTANCE: GraphRAGPrompt
KNOWLEDGE ATOMS CONSUMED: [KA-035]
DRAFT SPEC:
```yaml
prompt: graph_rag
purpose: 23% multi-hop reasoning improvement.
description: KG + vector retrieval in prompt.
techniques:
  - rank1: KA-035 (GraphRAG, STRONG)
combos_step_by_step:
  1. Build KG
  2. Retrieve
  3. Inject context
cost_awareness: Retrieval cheap.
domains: D3
phases: P3
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: HybridRetrievalPrompt
KNOWLEDGE ATOMS CONSUMED: [KA-037]
DRAFT SPEC:
```yaml
prompt: hybrid_semantic_syntactic
purpose: 7.6% better code retrieval.
description: CoSrch structure-aware.
techniques:
  - rank1: KA-037 (hybrid search, STRONG)
combos_step_by_step:
  1. Semantic match
  2. Syntactic refine
cost_awareness: Local compute.
phases: P4
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: SelfConsistencyPrompt
KNOWLEDGE ATOMS CONSUMED: [KA-008]
DRAFT SPEC:
```yaml
prompt: self_consistency
purpose: Reduce stochastic errors 7-19%.
description: Multiple paths, majority vote.
techniques:
  - rank1: KA-008 (self-consistency, MODERATE)
combos_step_by_step:
  1. Sample N paths
  2. Vote
cost_awareness: N=3-5 low temp.
domains: D3
confidence: MED
```
CONFIDENCE: MED
GAPS: [Optimal N tuning]

## PC5: MCP CONFIGS

### INSTANCE: AdversarialCriticMCP
KNOWLEDGE ATOMS CONSUMED: [KA-032]
DRAFT SPEC:
```yaml
mcp_config: adversarial_critic
purpose: 40% higher bug detection.
description: Dedicated critic server/agent.
techniques:
  - rank1: KA-032 (adversarial review, STRONG)
server_type: local/remote
tools_provided: [review_code]
domains: D2, D4
phases: P4, P5
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: APRToolMCP
KNOWLEDGE ATOMS CONSUMED: [KA-038]
DRAFT SPEC:
```yaml
mcp_config: automated_repair
purpose: 70-85% single-line bug fix.
description: APR server with test feedback.
techniques:
  - rank1: KA-038 (APR, STRONG)
combos_step_by_step:
  1. Diagnose
  2. Propose patches
  3. Test/apply
phases: P4, P5
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: [Test suite req]

## PC6: RULES
*(Sparse tags; inferred from D1 policy-as-code KA-009, guardrails KA-005)*

### INSTANCE: PolicyAdjudicationRule
KNOWLEDGE ATOMS CONSUMED: [KA-009, KA-005]
DRAFT SPEC:
```yaml
rule: policy_adjudication
purpose: Runtime policy enforcement at tool boundaries.
description: Preflight + runtime checks.
techniques:
  - rank1: KA-009 (policy-as-code, MODERATE)
  - rank2: KA-005 (layered guardrails, STRONG)
enforcement: deny-by-default
domains: D1, D7
confidence: MED
```
CONFIDENCE: MED
GAPS: [Specific rule syntax]

### INSTANCE: CredentialBrokerRule
KNOWLEDGE ATOMS CONSUMED: [KA-010]
DRAFT SPEC:
```yaml
rule: ephemeral_creds
purpose: Least-privilege short-lived creds.
description: Broker per invocation.
techniques:
  - rank1: KA-010 (scoped creds, MODERATE)
phases: P6
confidence: MED
```
CONFIDENCE: MED
GAPS: [Integration details]

## PC7: CONTEXT STRATS

### INSTANCE: EventSourcedJournaling
KNOWLEDGE ATOMS CONSUMED: [KA-004] *(from phases P8)*
DRAFT SPEC:
```yaml
context_strategy: event_sourced_journal
purpose: Immutable audit trail for context.
description: Append-only logs with hashes/diffs.
techniques:
  - rank1: KA-004 (event-sourced, STRONG)
combos_step_by_step:
  1. Log input hash
  2. Tool calls
  3. Diffs
cost_awareness: Append cheap.
phases: P8
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

## PC8: TASK DECOMP

### INSTANCE: RecursivePlanningGate
KNOWLEDGE ATOMS CONSUMED: [KA-017, KA-006]
DRAFT SPEC:
```yaml
task_decomp: gated_recursive
purpose: Prevent runaway planning.
description: Depth-limited decomposition.
techniques:
  - rank1: KA-006 (spec-driven, STRONG)
  - rank2: KA-017 (anti-recursive, MODERATE)
max_depth: 5
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: [Dynamic depth]

## PC9: WORKSPACE MGMT

### INSTANCE: WorktreeCleanup
KNOWLEDGE ATOMS CONSUMED: [KA-034]
DRAFT SPEC:
```yaml
workspace_mgmt: worktree_ops
purpose: Branch-per-task with auto-cleanup.
description: Create/merge/delete worktrees.
techniques:
  - rank1: KA-034 (isolation, STRONG)
automation: post-PR delete
phases: P7, P8
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: BranchIsolation
KNOWLEDGE ATOMS CONSUMED: [KA-034]
DRAFT SPEC:
```yaml
workspace_mgmt: branch_isolation
purpose: Reduce conflicts 67%.
techniques:
  - rank1: KA-034
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

## PC10: TECHNIQUES
*(Inferred general; top techniques without specific PC, or combos)*

### INSTANCE: CostFirstStack
KNOWLEDGE ATOMS CONSUMED: [KA-023, KA-001]
DRAFT SPEC:
```yaml
technique: cost_first_stack
purpose: Cascade + cache + budget decomp.
description: Lowest spend workflow.
techniques:
  - rank1: KA-023 (stack, ?)
  - rank2: KA-001
combos_step_by_step:
  1. Cache check
  2. Cascade route
  3. Budget enforce
domains: D1
confidence: MED
```
CONFIDENCE: MED
GAPS: [Full recipe details]

**Total Specs**: 24 across PC1-10. Prioritized STRONG atoms, cost-aware combos. Ready for refinement.


Atoms assigned to PC1-PC10 based on explicit PRODUCTS tags in prong1_master_atoms.md (66 tags across 68 atoms), supplemented by relevant atoms from prong2_domains.md (D1-D12 groupings) and prong3_phases.md (P1-P8 workflows). 2-5 instances per category, derived from prominent atoms (STRONG evidence prioritized). Instances named specifically from atom content/research (e.g., 'Mode: SemanticCache'). 

YAML templates standardized per category, filled completely with atom references. Techniques ranked by evidence>specificity>cost-efficiency. Combos step-by-step, cost-aware (e.g., cheap retrieval before expensive reasoning). Gaps flagged where data sparse (e.g., PC6/PC10).

## PC1: MODES

### INSTANCE: SemanticCacheMode
KNOWLEDGE ATOMS CONSUMED: [KA-002, KA-036]
DRAFT SPEC:
```yaml
mode: semantic_cache_mode
purpose: Reduce redundant token processing by 31-90% via embedding-based intent matching and prompt compression.
description: Activates semantic caching for repeated queries; compresses prompts with LLMLingua before flagship model use.
entry_conditions:
  - Repeated task patterns detected
  - Context exceeds 70% window
techniques:
  - rank1: KA-002 (semantic caching, STRONG, low-cost embeddings)
  - rank2: KA-036 (LLMLingua compression, STRONG, 20x ratio)
combos_step_by_step:
  1. Embed query (cheap)
  2. Cache hit? Return
  3. Compress + route to model
cost_awareness: Prioritizes embedding API (<$0.01) over full LLM calls.
tools: [read_file, search_files]
phases: P1
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: PromptCompressorMode
KNOWLEDGE ATOMS CONSUMED: [KA-036]
DRAFT SPEC:
```yaml
mode: prompt_compressor_mode
purpose: Achieve 20x prompt compression with <3% reasoning degradation.
description: Automatically compresses long contexts for efficiency in analysis phases.
entry_conditions:
  - Token count > threshold
techniques:
  - rank1: KA-036 (LLMLingua, STRONG)
combos_step_by_step:
  1. Detect long prompt
  2. Apply compression
  3. Verify coherence
cost_awareness: Saves 95% tokens upfront.
tools: []
phases: P1, P3
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: [Dynamic threshold tuning]

### INSTANCE: CostOptimizerMode
KNOWLEDGE ATOMS CONSUMED: [KA-002]
DRAFT SPEC:
```yaml
mode: cost_optimizer_mode
purpose: Dynamically manage context to minimize costs during onboarding.
description: Combines caching with model routing for discovery.
entry_conditions:
  - New workspace scan
techniques:
  - rank1: KA-002 (semantic caching, STRONG)
combos_step_by_step:
  1. Cache file reads
  2. Compress summaries
cost_awareness: Targets $5-8/task unconstrained baseline reduction.
tools: [list_files]
phases: P1
confidence: MED
```
CONFIDENCE: MED
GAPS: [Integration with routing]

## PC2: SKILLS

### INSTANCE: CascadeRouter
KNOWLEDGE ATOMS CONSUMED: [KA-001, KA-003, KA-011]
DRAFT SPEC:
```yaml
skill: cascade_router
purpose: Route tasks to optimal models, achieving 40-87% cost reduction.
description: Confidence-based escalation from cheap to flagship models.
entry_conditions:
  - Task classification complete
techniques:
  - rank1: KA-003 (Cascade Router, STRONG)
  - rank2: KA-001 (dynamic routing, STRONG)
metrics: KA-011 (unconstrained $5-8/task)
combos_step_by_step:
  1. Classify task (cheap model)
  2. Confidence low? Escalate
  3. Verify output
cost_awareness: Budget decomposition per step.
tools: []
domains: D1, D8
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: ModelEscalator
KNOWLEDGE ATOMS CONSUMED: [KA-003]
DRAFT SPEC:
```yaml
skill: model_escalator
purpose: Escalate based on verifier scores for 40-80% savings.
description: Verifier-first low-cost routing.
techniques:
  - rank1: KA-003 (confidence escalation, STRONG)
combos_step_by_step:
  1. Low-cost attempt
  2. Verifier check
  3. Escalate if fail
cost_awareness: Verifier <1% full cost.
phases: P1
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: [Verifier definition]

## PC3: WORKFLOWS

### INSTANCE: MoAVotingWorkflow
KNOWLEDGE ATOMS CONSUMED: [KA-030, KA-042, KA-039]
DRAFT SPEC:
```yaml
workflow: moa_voting
purpose: 8-12% perf gain via Mixture-of-Agents layered voting.
description: Multiple agents vote on outputs for coding tasks.
entry_conditions:
  - Complex implementation needed
techniques:
  - rank1: KA-030 (MoA, STRONG)
  - rank2: KA-042 (tradeoff 3-5x compute, STRONG)
metrics: KA-039 (83% GAIA accuracy)
combos_step_by_step:
  1. Parallel agents generate
  2. Vote/majority
  3. Critic verify
cost_awareness: Parallel cheap models first.
tools: [execute_command]
domains: D2
phases: P3, P4
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: ExplicitModeSwitching
KNOWLEDGE ATOMS CONSUMED: [KA-029]
DRAFT SPEC:
```yaml
workflow: explicit_mode_switch
purpose: Reduce task drift by 34% with boundary switching.
description: Strict mode transitions (architect -> code).
techniques:
  - rank1: KA-029 (explicit boundaries, STRONG)
combos_step_by_step:
  1. Check mode fit
  2. Switch via tool
  3. Confirm
cost_awareness: Mode-specific optimization.
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: WorktreeIsolation
KNOWLEDGE ATOMS CONSUMED: [KA-034]
DRAFT SPEC:
```yaml
workflow: worktree_isolation
purpose: 67% merge conflict reduction via branch-per-task.
description: Task-specific worktrees.
techniques:
  - rank1: KA-034 (worktree, STRONG)
combos_step_by_step:
  1. Create worktree
  2. Work in isolation
  3. Merge/PR
cost_awareness: Git ops low cost.
tools: [mcp_github_create_branch]
phases: P4, P7
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: ClarificationLoop
KNOWLEDGE ATOMS CONSUMED: [KA-033]
DRAFT SPEC:
```yaml
workflow: clarification_loop
purpose: 23% higher success via structured questions.
description: ask_followup_question integration.
techniques:
  - rank1: KA-033 (structured prompting, STRONG)
combos_step_by_step:
  1. Detect ambiguity
  2. Ask with options
  3. Incorporate response
cost_awareness: Human loop only when needed.
tools: [ask_followup_question]
domains: D2, D7, D11
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: SpecDrivenGates
KNOWLEDGE ATOMS CONSUMED: [KA-006]
DRAFT SPEC:
```yaml
workflow: spec_driven_gates
purpose: 56% dev time reduction with 4-phase gates.
description: Specify-Architect-Code-Review.
techniques:
  - rank1: KA-006 (4-phase, STRONG)
combos_step_by_step:
  1. Specify
  2. Plan/todo
  3. Implement
  4. Gates
phases: P1-P4
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

## PC4: PROMPTS

### INSTANCE: GraphRAGPrompt
KNOWLEDGE ATOMS CONSUMED: [KA-035]
DRAFT SPEC:
```yaml
prompt: graph_rag
purpose: 23% multi-hop reasoning improvement.
description: KG + vector retrieval in prompt.
techniques:
  - rank1: KA-035 (GraphRAG, STRONG)
combos_step_by_step:
  1. Build KG
  2. Retrieve
  3. Inject context
cost_awareness: Retrieval cheap.
domains: D3
phases: P3
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: HybridRetrievalPrompt
KNOWLEDGE ATOMS CONSUMED: [KA-037]
DRAFT SPEC:
```yaml
prompt: hybrid_semantic_syntactic
purpose: 7.6% better code retrieval.
description: CoSrch structure-aware.
techniques:
  - rank1: KA-037 (hybrid search, STRONG)
combos_step_by_step:
  1. Semantic match
  2. Syntactic refine
cost_awareness: Local compute.
phases: P4
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: SelfConsistencyPrompt
KNOWLEDGE ATOMS CONSUMED: [KA-008]
DRAFT SPEC:
```yaml
prompt: self_consistency
purpose: Reduce stochastic errors 7-19%.
description: Multiple paths, majority vote.
techniques:
  - rank1: KA-008 (self-consistency, MODERATE)
combos_step_by_step:
  1. Sample N paths
  2. Vote
cost_awareness: N=3-5 low temp.
domains: D3
confidence: MED
```
CONFIDENCE: MED
GAPS: [Optimal N tuning]

## PC5: MCP CONFIGS

### INSTANCE: AdversarialCriticMCP
KNOWLEDGE ATOMS CONSUMED: [KA-032]
DRAFT SPEC:
```yaml
mcp_config: adversarial_critic
purpose: 40% higher bug detection.
description: Dedicated critic server/agent.
techniques:
  - rank1: KA-032 (adversarial review, STRONG)
server_type: local/remote
tools_provided: [review_code]
domains: D2, D4
phases: P4, P5
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: APRToolMCP
KNOWLEDGE ATOMS CONSUMED: [KA-038]
DRAFT SPEC:
```yaml
mcp_config: automated_repair
purpose: 70-85% single-line bug fix.
description: APR server with test feedback.
techniques:
  - rank1: KA-038 (APR, STRONG)
combos_step_by_step:
  1. Diagnose
  2. Propose patches
  3. Test/apply
phases: P4, P5
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: [Test suite req]

## PC6: RULES
*(Sparse tags; inferred from D1 policy-as-code KA-009, guardrails KA-005)*

### INSTANCE: PolicyAdjudicationRule
KNOWLEDGE ATOMS CONSUMED: [KA-009, KA-005]
DRAFT SPEC:
```yaml
rule: policy_adjudication
purpose: Runtime policy enforcement at tool boundaries.
description: Preflight + runtime checks.
techniques:
  - rank1: KA-009 (policy-as-code, MODERATE)
  - rank2: KA-005 (layered guardrails, STRONG)
enforcement: deny-by-default
domains: D1, D7
confidence: MED
```
CONFIDENCE: MED
GAPS: [Specific rule syntax]

### INSTANCE: CredentialBrokerRule
KNOWLEDGE ATOMS CONSUMED: [KA-010]
DRAFT SPEC:
```yaml
rule: ephemeral_creds
purpose: Least-privilege short-lived creds.
description: Broker per invocation.
techniques:
  - rank1: KA-010 (scoped creds, MODERATE)
phases: P6
confidence: MED
```
CONFIDENCE: MED
GAPS: [Integration details]

## PC7: CONTEXT STRATS

### INSTANCE: EventSourcedJournaling
KNOWLEDGE ATOMS CONSUMED: [KA-004] *(from phases P8)*
DRAFT SPEC:
```yaml
context_strategy: event_sourced_journal
purpose: Immutable audit trail for context.
description: Append-only logs with hashes/diffs.
techniques:
  - rank1: KA-004 (event-sourced, STRONG)
combos_step_by_step:
  1. Log input hash
  2. Tool calls
  3. Diffs
cost_awareness: Append cheap.
phases: P8
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

## PC8: TASK DECOMP

### INSTANCE: RecursivePlanningGate
KNOWLEDGE ATOMS CONSUMED: [KA-017, KA-006]
DRAFT SPEC:
```yaml
task_decomp: gated_recursive
purpose: Prevent runaway planning.
description: Depth-limited decomposition.
techniques:
  - rank1: KA-006 (spec-driven, STRONG)
  - rank2: KA-017 (anti-recursive, MODERATE)
max_depth: 5
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: [Dynamic depth]

## PC9: WORKSPACE MGMT

### INSTANCE: WorktreeCleanup
KNOWLEDGE ATOMS CONSUMED: [KA-034]
DRAFT SPEC:
```yaml
workspace_mgmt: worktree_ops
purpose: Branch-per-task with auto-cleanup.
description: Create/merge/delete worktrees.
techniques:
  - rank1: KA-034 (isolation, STRONG)
automation: post-PR delete
phases: P7, P8
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

### INSTANCE: BranchIsolation
KNOWLEDGE ATOMS CONSUMED: [KA-034]
DRAFT SPEC:
```yaml
workspace_mgmt: branch_isolation
purpose: Reduce conflicts 67%.
techniques:
  - rank1: KA-034
confidence: HIGH
```
CONFIDENCE: HIGH
GAPS: []

## PC10: TECHNIQUES
*(Inferred general; top techniques without specific PC, or combos)*

### INSTANCE: CostFirstStack
KNOWLEDGE ATOMS CONSUMED: [KA-023, KA-001]
DRAFT SPEC:
```yaml
technique: cost_first_stack
purpose: Cascade + cache + budget decomp.
description: Lowest spend workflow.
techniques:
  - rank1: KA-023 (stack, ?)
  - rank2: KA-001
combos_step_by_step:
  1. Cache check
  2. Cascade route
  3. Budget enforce
domains: D1
confidence: MED
```
CONFIDENCE: MED
GAPS: [Full recipe details]

**Total Specs**: 24 across PC1-10. Prioritized STRONG atoms, cost-aware combos. Ready for refinement.


