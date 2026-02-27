# Product Mapping: Knowledge Atoms to Deliverable Products

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

# Product Mapping: Knowledge Atoms to Deliverable Products

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

# Product Mapping: Knowledge Atoms to Deliverable Products

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

# Product Mapping: Knowledge Atoms to Deliverable Products

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

# Product Mapping: Knowledge Atoms to Deliverable Products

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

# Product Mapping: Knowledge Atoms to Deliverable Products

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

# Product Mapping: Knowledge Atoms to Deliverable Products

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

# Product Mapping: Knowledge Atoms to Deliverable Products

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

# Product Mapping: Knowledge Atoms to Deliverable Products

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

# Product Mapping: Knowledge Atoms to Deliverable Products

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

# Product Mapping: Knowledge Atoms to Deliverable Products

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

**Generated:** February 24, 2026  
**Source:** Knowledge Atom Registry, Domain Grouping, SDLC Phase Mapping

---

## Executive Summary

This document maps knowledge atoms to the 10 product categories defined in the research framework. Each product spec consumes specific knowledge atoms and transforms them into actionable artifacts for the autonomous AI coding system. The mapping prioritizes Mode, Skill, and Context Strategy as foundational products, with additional coverage of Workflows and Techniques.

---

## PC1: MODES (Agent Operational Personas)

### PRODUCT: PC1 - Mode Specification

#### INSTANCE: Mode: Orchestrator Agent

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-001](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — BDI Hybrid Architecture
- [KA-005](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — System-Theoretic Decomposition
- [KA-007](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Mixture-of-Agents
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-056](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Autonomy Levels
- [KA-057](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/07_human_interaction/human_in_the_loop_systems/patterns.md) — Confidence-Based Escalation

**DRAFT SPEC:**

```yaml
mode: orchestrator
role_definition: |
  The Orchestrator Agent is the primary coordination hub for multi-agent AI coding systems. 
  It decomposes high-level tasks, delegates to specialized agents, aggregates results, and ensures 
  quality gates are met. It does NOT execute code directly; it orchestrates other agents to do so.
  It maintains explicit mental state for auditability and failure recovery.
perspective: |
  The Orchestrator approaches problems through hierarchical decomposition: breaking complex tasks 
  into manageable subtasks, assigning them to appropriate specialized agents, and coordinating 
  their execution. It prioritizes system coherence, traceability, and graceful degradation.
tools:
  enabled:
    - task_decomposition: KA-008 provides 2-3 levels for simple, 5-7 for complex tasks
    - agent_delegation: KA-007 enables 8-12% improvement via Mixture-of-Agents
    - recovery_mechanisms: KA-010 provides 19% higher success rate via multi-stage recovery
    - model_routing: KA-036 enables 40-87% cost reduction via cascade routing
  disabled:
    - direct_code_execution: Prevents bypassing delegation hierarchy
context_strategy: strategy: adaptive_context_management
skills_available:
  - code_exploration: When discovering new codebases or understanding existing structure
  - code_generation: When implementing new features or refactoring
  - testing: When validating implementations
  - security_review: When handling sensitive operations or external inputs
decision_authority:
  can_decide:
    - task decomposition strategy
    - agent selection for subtasks
    - retry attempts for failed subtasks
    - context compression decisions
  must_escalate:
    - ambiguous requirements requiring human clarification (KA-056, KA-057)
    - security-sensitive operations exceeding autonomy threshold
    - task scope changes requiring replanning
quality_criteria:
  - Subtask completion rate: target 95%+
  - Quality gate pass rate: target 90%+
  - Token budget adherence: within 10% of estimate
transition_triggers:
  - condition: All subtasks complete and quality gates passed
    target_mode: completion
    context_to_pass: Final artifacts, metrics, audit trail
  - condition: Subtask failure rate > 20%
    target_mode: recovery
    context_to_pass: Failure logs, attempted strategies
  - condition: Confidence score < 0.7 (KA-057)
    target_mode: human_escalation
    context_to_pass: Current state, decision points, options
custom_instructions: |
  The Orchestrator MUST maintain an explicit belief-desire-intent mental state (KA-001) for 
  auditability. It MUST decompose tasks using system-theoretic principles (KA-005) with 
  5 subsystems and explicit interfaces. When agents fail, it MUST attempt conditional 
  multi-stage recovery (KA-010) before escalating. Communication between agents MUST be 
  batched to avoid chatty communication anti-pattern (KA-080).
```

**CONFIDENCE:** HIGH

**GAPS:**
- Missing explicit trust scoring between agents (domain gap)
- No established deadlock/livelock detection patterns for agent swarms
- Limited guidance on commit generation strategies

---

## PC2: SKILLS (Specialized Capabilities)

### PRODUCT: PC2 - Skill Specification

#### INSTANCE: Skill: Code Exploration

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-022](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Semantic-Guided Traversal
- [KA-023](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — CoSrch Hybrid Search
- [KA-024](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — Repo Grokking
- [KA-025](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/04_code_intelligence/code_exploration/patterns.md) — File Prioritization
- [KA-019](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/memory_systems/patterns.md) — Vector DB Recall

**DRAFT SPEC:**

```yaml
skill: code_exploration
purpose: Efficiently understand and map unfamiliar codebases for autonomous operation
technique_stack:
  primary: Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  alternatives:
    - technique: Repo Grokking (KA-024)
      use_when: Querying across million-line codebases requiring sub-second response
      tradeoff: Higher indexing overhead vs. comprehensive coverage
    - technique: CoSrch Hybrid Search (KA-023)
      use_when: Need 7.60% improvement in first-attempt success rate
      tradeoff: Requires semantic embeddings vs. keyword search simplicity
    - technique: File Prioritization (KA-025)
      use_when: Large codebase with limited exploration budget
      tradeoff: May miss low-priority files vs. 50-70% time savings
  combination: |
    Use Repo Grokking (KA-024) for initial architecture extraction, then apply 
    Semantic-Guided Traversal (KA-022) for focused exploration. Use CoSrch Hybrid Search 
    (KA-023) when searching for specific patterns or implementation details. Apply 
    File Prioritization (KA-025) to stay within context window limits.
inputs:
  required:
    - codebase_path: Root directory or repository URL
    - exploration_goal: What to understand (architecture, dependencies, API surface)
  optional:
    - focus_areas: Specific directories or files to prioritize
    - exclusion_patterns: Files or patterns to skip
    - context_budget: Maximum tokens to use for exploration
procedure:
  1: Extract codebase architecture using Repo Grokking (KA-024) — identifies entry points, modules, dependencies
  2: Build semantic map using Vector DB Recall (KA-019) — 85-95% recall@10 with code embeddings
  3: Prioritize exploration targets using File Prioritization (KA-025) — reduces time by 50-70%
  4: Traverse codebase semantically using Semantic-Guided Traversal (KA-022) — 40-60% time reduction
  5: Validate understanding with Hybrid Search (KA-023) — 7.60% SuccessRate@1 improvement
outputs:
  - Codebase architecture diagram
  - Dependency graph
  - API surface summary
  - Key file locations with purposes
quality_check: |
  Verify coverage by checking: (1) All entry points identified, (2) Major dependencies mapped, 
  (3) Critical paths understood. Target: 90%+ coverage of high-priority areas. Use Vector DB 
  recall metrics to validate searchability.
when_to_use: |
  - New codebase onboarding (SDLC Phase P1)
  - Understanding dependency relationships
  - Locating specific implementations
  - Architecture extraction for refactoring
when_NOT_to_use: |
  - Small, well-understood codebases where simple file listing suffices
  - When exploration time exceeds value of understanding
cost_profile:
  tokens: Moderate — indexing overhead ~10K tokens, exploration ~5K tokens per 100 files
  latency: Fast for grokking (sub-second), moderate for semantic traversal
  when_to_skip: Small codebases (<50 files) where full exploration is wasteful
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for circular dependency detection during exploration
- Limited guidance on when to stop exploration vs. continue

---

## PC3: WORKFLOWS (Multi-Step Sequences)

### PRODUCT: PC3 - Workflow Specification

#### INSTANCE: Workflow: Spec-Driven Development

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-002](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — 4-Phase Spec-Driven Workflow
- [KA-003](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/system_design_philosophy/patterns.md) — Bidirectional Specifications
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-009](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Worktree Isolation

**DRAFT SPEC:**

```yaml
workflow: spec_driven_development
trigger: User provides high-level feature request or requirement
phases:
  - name: Specify
    mode: orchestrator
    skills: []
    entry_criteria: User requirement received
    steps:
      1: Parse requirement into explicit specification
      2: Validate specification completeness
      3: Identify gaps requiring clarification
    exit_criteria: Complete specification document
    quality_gate:
      checks:
        - All requirements mapped to acceptance criteria
        - No ambiguous statements
        - Testability verified
      on_failure: Retry specification with clarification
    artifacts_produced:
      - Feature specification document

  - name: Plan
    mode: orchestrator
    skills: [task_decomposition]
    entry_criteria: Specification complete
    steps:
      1: Decompose specification into tasks (KA-008: 2-3 levels simple, 5-7 complex)
      2: Identify dependencies between tasks
      3: Sequence tasks for optimal execution
      4: Estimate resource requirements
    exit_criteria: Task breakdown with dependencies
    quality_gate:
      checks:
        - All specification items covered by tasks
        - Dependencies resolved
        - No circular dependencies
      on_failure: Retry decomposition
    artifacts_produced:
      - Task breakdown document

  - name: Implement
    mode: executor
    skills: [code_exploration, code_generation, testing]
    entry_criteria: Task plan ready
    steps:
      1: Create worktree branch (KA-009: 67% conflict reduction)
      2: Execute tasks per plan
      3: Validate against specification
      4: Update specification if codebase reality diverges (KA-003)
    exit_criteria: All tasks complete, tests passing
    quality_gate:
      checks:
        - All acceptance criteria met
        - Tests pass
        - No security vulnerabilities introduced
      on_failure: Retry task or escalate
    artifacts_produced:
      - Implementation code
      - Unit tests
      - Integration tests

  - name: Verify
    mode: reviewer
    skills: [testing, security_review]
    entry_criteria: Implementation complete
    steps:
      1: Run full test suite
      2: Perform security review
      3: Validate against original specification
      4: Update bidirectional specification if needed (KA-003)
    exit_criteria: All gates passed
    quality_gate:
      checks:
        - 100% tests passing
        - Security scan clean
        - Specification alignment verified
      on_failure: Retry implementation or rollback
    artifacts_produced:
      - Test results
      - Security report
      - Final specification

completion_criteria: |
  All 4 phases complete with all quality gates passed. Final artifacts include:
  implementation, tests, and synchronized specification. Commit ready for review.

rollback_plan: |
  On failure at any phase:
  - Specify: Return to requirement clarification
  - Plan: Regenerate task breakdown with corrected specification
  - Implement: Revert worktree changes, restart from failed task
  - Verify: Re-run failed tests, revert to last stable commit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No explicit integration testing phase defined
- Missing rollback automation for complex multi-file changes

---

## PC4: PROMPTS (Instruction Templates)

### PRODUCT: PC4 - Prompt Template

#### INSTANCE: Prompt: Orchestrator Agent System Prompt

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle (context ordering)
- [KA-027](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Hallucination Impact (anti-hallucination)
- [KA-032](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/01_meta_architecture/security_architecture/patterns.md) — Prompt-Only Security (constraints)

**DRAFT SPEC:**

```yaml
prompt_template: orchestrator_system_prompt
structure: |
  You are an Orchestrator Agent for autonomous software development. Your role is to
  coordinate multiple specialized agents to complete complex development tasks.
  
  ## Your Responsibilities
  [Core responsibilities derived from KA-001, KA-005]
  
  ## Context Ordering
  [Based on KA-015: Critical information at boundaries, not middle]
  - System instructions: FIRST (highest priority)
  - Current task context: SECOND
  - Relevant code: THIRD (use U-shaped prioritization)
  - History: END (least retention)
  
  ## Anti-Hallucination Guidelines
  [Based on KA-027: 19.7% fabricated packages, 40-45% vulnerable code]
  - Always verify package names against dependency manifests
  - Never assume API behavior without documentation
  - Flag uncertainty explicitly rather than guessing
  
  ## Security Constraints
  [Based on KA-032: Prompt-only security is insufficient]
  - You CANNOT bypass security controls through persuasion
  - You MUST log all security-sensitive operations
  - You MUST escalate requests that require privileges you don't have
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- No empirical validation of prompt effectiveness
- Limited research on optimal context boundaries for orchestrator tasks

---

## PC7: CONTEXT MANAGEMENT STRATEGIES

### PRODUCT: PC7 - Context Strategy Specification

#### INSTANCE: Strategy: Adaptive Context Management

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-012](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — LLMLingua Compression
- [KA-013](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Selective Context
- [KA-015](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Lost-in-Middle
- [KA-016](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/03_context_memory_intelligence/context_management/patterns.md) — Context Poisoning

**DRAFT SPEC:**

```yaml
strategy: adaptive_context_management
applies_to: [orchestrator_mode, executor_mode, reviewer_mode]
window_partition:
  system_instructions: 10% — placement: top
  task_context: 25% — placement: after system
  relevant_code: 40% — placement: middle with U-shaped prioritization (KA-015)
  history: 15% — placement: end
  reserved_for_output: 10%
content_selection:
  include:
    - Current task specification
    - Active subtask context
    - Code relevant to current subtask
    - Recent agent communications (last 3 exchanges)
    - Quality gate status
  exclude:
    - Completed subtask details (summarize only)
    - Abandoned approaches
    - Speculative planning
compression_pipeline:
  1: LLMLingua Compression (KA-012) — 20x compression with <3% degradation; threshold: 80% of budget used
  2: Selective Context (KA-013) — 50% token reduction with 97% performance retention; threshold: 90% of budget used
  3: Summary + Key References — preserve critical paths; fallback when 95%+ budget used
ordering_rules:
  - Critical info at boundaries (KA-015): System instructions at top, history at end
  - U-shaped prioritization: Most relevant content at start and end of relevant_code section
  - Recent updates before older context
  - Dependencies before dependents
refresh_policy: |
  Rotate context when:
  - Subtask transitions (every 2-3 subtasks)
  - Token usage exceeds 80% of budget
  - New agent joins or leaves orchestration
  - Quality gate failure requires replanning
poisoning_checks:
  - Bidirectional Unicode detection (KA-016)
  - Hidden character detection (KA-016)
  - Injection pattern detection (KA-016)
  - Disposable session validation (KA-016)
```

**CONFIDENCE:** HIGH

**GAPS:**
- No specific guidance on compression for different task types
- Limited research on poisoning detection accuracy

---

## PC8: TASK DECOMPOSITION PATTERNS

### PRODUCT: PC8 - Task Decomposition Pattern

#### INSTANCE: Pattern: Hierarchical Task Decomposition

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-008](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Hierarchical Task Decomposition
- [KA-040](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/task_architecture/patterns.md) — Unlimited Planning (anti-pattern)

**DRAFT SPEC:**

```yaml
task_decomposition_pattern: hierarchical_task_decomposition
applies_to: [planning_phase, orchestration]
decomposition_rules:
  - Simple tasks (2-3 levels):
      - Level 1: User goal
      - Level 2: Major steps (3-7)
      - Level 3: Atomic actions per step
  - Complex tasks (5-7 levels):
      - Level 1: User goal
      - Level 2: Epics (2-5)
      - Level 3: Features (3-8)
      - Level 4: User stories (5-15)
      - Level 5: Tasks (10-30)
      - Level 6: Subtasks (20-60)
      - Level 7: Atomic actions
dependency_handling:
  - Identify all cross-level dependencies
  - Sequence dependent tasks serially
  - Execute independent tasks in parallel
  - Detect circular dependencies and flag for human review
budget_enforcement: |
  Prevent token runaway (KA-040) by:
  - Setting maximum planning time (e.g., 60 seconds)
  - Limiting decomposition depth iterations
  - Capping total planning tokens (e.g., 2000 tokens)
  - Using timeout + partial plan if budget exhausted
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for dependency detection automation
- Limited guidance on optimal branching factor

---

## PC10: TECHNIQUES & STRATEGIES (Situational Playbook)

### PRODUCT: PC10 - Technique Specification

#### INSTANCE: Technique: Conditional Multi-Stage Recovery

**KNOWLEDGE ATOMS CONSUMED:**
- [KA-010](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — Conditional Multi-Stage Recovery
- [KA-046](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/05_sdlc_automation/testing_architecture/patterns.md) — AI Happy Path Bias (anti-pattern)
- [KA-079](C:/Users/Ice/Desktop/Dev/SDLC/SDLC/docs/research/02_agent_orchestration/agent_system_design/patterns.md) — God Agent (anti-pattern)

**DRAFT SPEC:**

```yaml
technique: conditional_multi_stage_recovery
purpose: Automatically recover from agent failures with escalating strategies
trigger_condition: Agent subtask fails or returns error
stages:
  - stage: 1
    name: Retry Same Agent
    action: Re-execute failed subtask with same agent
    max_attempts: 2
    conditions:
      - Error is transient (timeout, rate limit)
      - Agent has not exceeded failure threshold
  - stage: 2
    name: Different Agent Same Capability
    action: Delegate to another agent with same skill set
    max_attempts: 2
    conditions:
      - Stage 1 exhausted
      - Error not due to skill gap
  - stage: 3
    name: Alternative Strategy
    action: Replan subtask using different approach
    max_attempts: 1
    conditions:
      - Stage 2 exhausted
      - Subtask still valid
  - stage: 4
    name: Escalate
    action: Bring to human attention with failure analysis
    max_attempts: 0
    conditions:
      - All previous stages exhausted
      - Task is blocked
detection_criteria: |
  Detect failure when:
  - Agent returns error status
  - Quality gate fails (KA-046: 80% miss error handling — be vigilant)
  - Timeout exceeded
  - Confidence score drops below threshold
anti_patterns_to_avoid: |
  - Avoid God Agent pattern (KA-079): Don't let single agent handle all recovery
  - Avoid infinite retry loops: Enforce max stage limits
  - Avoid silent failures: Always log and optionally notify
success_metrics: |
  Target: 19% higher success rate (KA-010)
  - Track: Recovery success rate per stage
  - Track: Average recovery time
  - Track: Escalation rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- No established patterns for partial success handling
- Limited guidance on recovery strategy selection heuristics

---

## Summary of Product Mapping

| Product Category | Instance | Key Atoms | Confidence |
|-----------------|----------|-----------|-------------|
| PC1: Mode | Orchestrator Agent | KA-001, KA-005, KA-007, KA-010, KA-056, KA-057 | HIGH |
| PC2: Skill | Code Exploration | KA-022, KA-023, KA-024, KA-025, KA-019 | HIGH |
| PC3: Workflow | Spec-Driven Development | KA-002, KA-003, KA-008, KA-009 | MEDIUM |
| PC4: Prompt | Orchestrator System Prompt | KA-015, KA-027, KA-032 | MEDIUM |
| PC7: Context Strategy | Adaptive Context Management | KA-012, KA-013, KA-015, KA-016 | HIGH |
| PC8: Task Decomposition | Hierarchical Decomposition | KA-008, KA-040 | HIGH |
| PC10: Technique | Conditional Multi-Stage Recovery | KA-010, KA-046, KA-079 | HIGH |

---

## Recommended Next Subtask

Complete mapping for remaining product categories:
- **PC5 (MCP Configurations)**: Map MCP security research atoms
- **PC6 (Rules)**: Map constraint and guardrail atoms  
- **PC9 (Workspace Management)**: Map branch strategy and worktree atoms

Additionally, validate each spec through:
1. Cross-referencing with source research documents
2. Checking atom IDs are valid and current
3. Verifying cross-product consistency

---

## Sources

- docs/research/knowledge_atom_registry.md — Atom definitions and evidence
- docs/research/domain_grouping.md — Lateral atom organization
- docs/research/sdlc_phase_mapping.md — Temporal atom organization
- docs/research/01_meta_architecture/system_design_philosophy/ — BDI, Spec-Driven patterns
- docs/research/02_agent_orchestration/agent_system_design/ — Mixture-of-Agents, Recovery
- docs/research/03_context_memory_intelligence/context_management/ — Compression, Poisoning
- docs/research/04_code_intelligence/code_exploration/ — Traversal, Grokking, Search
- docs/research/05_sdlc_automation/testing_architecture/ — Testing patterns
- docs/research/07_human_interaction/human_in_the_loop_systems/ — Autonomy, Escalation

