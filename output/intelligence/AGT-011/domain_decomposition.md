> code · sonar-reasoning-pro

<think>
The user is asking me to execute a prompt from a file. Let me understand what they're asking:

1. They provided a file `c:\Users\Ice\Desktop\Dev\SDLC\SDLC\logs\AGT-011_prompt.md`
2. The file contains a system directive for "Context & Prompt Agent (AGT-011)"
3. They want me to "Execute the architect agent prompt from the attached file" and output to `output/intelligence/AGT-011`

This is asking me to act as AGT-011 and perform the domain decomposition task described in the prompt. The prompt is asking me to decompose the "Context Management & Prompt Engineering" domain into 16 categories with specific structure.

However, I need to be careful here. This is a very large task that would require me to:
- Define 16 different categories of decomposition
- Recursively expand subdomains up to 4 levels deep
- Create comprehensive output artifacts

Given my instructions to be concise and not do unnecessary work, I should:
1. Understand what the task is asking
2. Execute it properly but efficiently
3. Output the results to the specified directory

Let me check the search results provided. They are about context engineering and prompt engineering - which is directly relevant to this task. The search results define:
- Context engineering vs prompt engineering
- Strategies for context management
- Prompt optimization techniques
- Context window management

Now I need to execute the AGT-011 prompt by performing the complete domain decomposition. This is a substantial task, but the user is explicitly asking me to do it.

I should:
1. Read/understand the full directive
2. Perform the decomposition into all 16 categories
3. Output structured YAML files to output/intelligence/AGT-011/

Let me structure this response to execute the architect agent prompt comprehensively.
</think>

I'll execute the AGT-011 Context & Prompt Agent prompt and generate the complete domain decomposition with output artifacts.
<function_calls>
<invoke name="bash">
<parameter name="command">mkdir -p "c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\intelligence\AGT-011"</parameter>
</invoke>
</function_calls>

Now generating comprehensive domain decomposition artifacts:
<function_calls>
<invoke name="write_file">
<parameter name="path">c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\intelligence\AGT-011\context_strategies.yaml</parameter>
<parameter name="content">domain_id: DOM-011
domain_name: Context Management & Prompt Engineering
execution_phase: Phase 2 (Core)
generated_date: 2026-03-01

skills:
  - skill_id: DOM-011-SK-001
    name: Context Window Optimization
    description: Analyzes model capabilities and assembles context within dynamic window constraints, applying partitioning strategies for optimal token allocation.
    inputs: [model_config, task_complexity, available_context]
    outputs: [partitioned_context, window_allocation_plan]
    complexity: High
    
  - skill_id: DOM-011-SK-002
    name: Semantic Caching
    description: Implements semantic caching for repeated context patterns, reducing redundant context assembly and improving inference latency.
    inputs: [context_patterns, usage_history, ttl_config]
    outputs: [cache_entries, invalidation_rules]
    complexity: High
    
  - skill_id: DOM-011-SK-003
    name: Prompt Compression
    description: Applies lossless and lossy compression techniques to prompts while preserving semantic meaning and critical instructions.
    inputs: [prompt_text, compression_ratio_target, semantic_threshold]
    outputs: [compressed_prompt, compression_metadata]
    complexity: High
    
  - skill_id: DOM-011-SK-004
    name: Token Budget Calculation
    description: Decomposes total model token budget across prompt sections (system, user, context, output) with per-task allocation.
    inputs: [model_max_tokens, task_requirements, output_reservation]
    outputs: [budget_allocation_table, enforcement_rules]
    complexity: Medium
    
  - skill_id: DOM-011-SK-005
    name: Prompt Template Authoring
    description: Designs reusable, parameterized prompt templates with clear section organization and performance metadata.
    inputs: [task_specification, organizational_standards, example_tasks]
    outputs: [template_library, parameter_definitions]
    complexity: Medium
    
  - skill_id: DOM-011-SK-006
    name: A/B Variant Testing
    description: Conducts structured testing of prompt variants to identify performance-optimal templates and configurations.
    inputs: [variant_set, test_cases, success_metrics]
    outputs: [performance_comparison, recommendation]
    complexity: Medium
    
  - skill_id: DOM-011-SK-007
    name: Context Relevance Scoring
    description: Ranks and filters context fragments by relevance to current task, optimizing information density within budget.
    inputs: [context_fragments, task_query, relevance_model]
    outputs: [ranked_context, relevance_scores]
    complexity: Medium
    
  - skill_id: DOM-011-SK-008
    name: Dynamic Context Window Resizing
    description: Adjusts context window allocation at runtime based on task progress and remaining token budget.
    inputs: [current_usage, task_progress, model_config]
    outputs: [new_window_config, reallocation_plan]
    complexity: High

workflows:
  - workflow_id: DOM-011-WF-001
    name: Context Assembly Pipeline
    trigger: New task initiated with context requirements
    steps:
      - step: 1
        action: Gather context from all sources (knowledge base, user input, chat history)
        entry_criteria: Task metadata available
        exit_criteria: All potential context collected
      - step: 2
        action: Score and rank context by relevance to task
        entry_criteria: Context gathered
        exit_criteria: Relevance scores assigned, top candidates selected
      - step: 3
        action: Apply compression to selected context while preserving semantics
        entry_criteria: Context ranked, compression ratio target set
        exit_criteria: Compressed context meets semantic threshold
      - step: 4
        action: Fit compressed context into allocated window with system prompt and user input
        entry_criteria: Compressed context ready, token budget allocated
        exit_criteria: All components fit within window limit
      - step: 5
        action: Validate assembled context for poisoning, consistency, and semantic correctness
        entry_criteria: Context fitted into window
        exit_criteria: Validation passed or remediation completed
    completion_criteria: Context ready for model inference, all validation passed
    rollback_plan: If validation fails, return to step 2 with reduced relevance threshold; if compression fails, reduce context scope
    
  - workflow_id: DOM-011-WF-002
    name: Prompt Template Creation and Validation
    trigger: New task type identified without suitable template
    steps:
      - step: 1
        action: Analyze task requirements and define template sections
        entry_criteria: Task specification documented
        exit_criteria: Template structure designed
      - step: 2
        action: Draft template with parameterization and clear instructions
        entry_criteria: Template structure defined
        exit_criteria: Draft template completed
      - step: 3
        action: Create test cases and variant versions
        entry_criteria: Draft template completed
        exit_criteria: Test suite and variants ready
      - step: 4
        action: Execute A/B testing and measure performance
        entry_criteria: Test cases and variants ready
        exit_criteria: Performance metrics collected
      - step: 5
        action: Validate template meets performance threshold and document best practices
        entry_criteria: Performance metrics available
        exit_criteria: Template approved or rejected
    completion_criteria: Template versioned, performance baseline established, ready for production
    rollback_plan: Archive failed template, revert to previous version, escalate for manual review
    
  - workflow_id: DOM-011-WF-003
    name: Token Budget Planning
    trigger: New task initiated or budget exceeded
    steps:
      - step: 1
        action: Determine model max tokens and identify output reservation requirement
        entry_criteria: Model selected
        exit_criteria: Total available tokens calculated
      - step: 2
        action: Allocate tokens to system prompt section (base instructions, guidelines)
        entry_criteria: Total available tokens known
        exit_criteria: System prompt budget allocated
      - step: 3
        action: Allocate tokens to context section (retrieved knowledge, history)
        entry_criteria: System prompt budget set
        exit_criteria: Context budget allocated
      - step: 4
        action: Allocate tokens to user input section
        entry_criteria: Context budget set
        exit_criteria: User input budget allocated
      - step: 5
        action: Reserve remaining tokens for output generation
        entry_criteria: All input sections budgeted
        exit_criteria: Output reservation confirmed
    completion_criteria: All budget allocations set, total equals available tokens, enforcement rules activated
    rollback_plan: If budget exceeds available tokens, reduce context or user input allocations and replan
    
  - workflow_id: DOM-011-WF-004
    name: Semantic Cache Population and Invalidation
    trigger: Context pattern repeated, or cache TTL expires
    steps:
      - step: 1
        action: Hash and embed context pattern, check cache hit rate
        entry_criteria: Context assembled
        exit_criteria: Hit rate decision made
      - step: 2
        action: If cacheable, store in semantic cache with embedding and TTL
        entry_criteria: Pattern identified as cacheable
        exit_criteria: Cache entry created
      - step: 3
        action: Set invalidation triggers (time-based, event-based, dependency-based)
        entry_criteria: Cache entry created
        exit_criteria: Invalidation rules configured
      - step: 4
        action: Monitor cache usage and apply LRU eviction when capacity exceeded
        entry_criteria: Cache populated
        exit_criteria: Eviction rules enforced
      - step: 5
        action: Invalidate stale entries when triggers fire
        entry_criteria: Invalidation conditions met
        exit_criteria: Stale entries removed
    completion_criteria: Semantic cache operational, TTL and invalidation rules active
    rollback_plan: Clear cache on integrity failure, fall back to runtime context assembly
    
  - workflow_id: DOM-011-WF-005
    name: Prompt Optimization Cycle
    trigger: Performance degradation detected or periodic review triggered
    steps:
      - step: 1
        action: Collect performance metrics from template usage
        entry_criteria: Template active in production
        exit_criteria: Metrics analyzed, regression identified
      - step: 2
        action: Identify root cause (unclear instructions, missing examples, poor formatting)
        entry_criteria: Regression confirmed
        exit_criteria: Root cause documented
      - step: 3
        action: Create variant with targeted improvements
        entry_criteria: Root cause identified
        exit_criteria: Variant designed
      - step: 4
        action: Execute controlled A/B test
        entry_criteria: Variant ready
        exit_criteria: Performance comparison available
      - step: 5
        action: Promote improved variant or rollback to previous version
        entry_criteria: Test results available
        exit_criteria: Decision made and deployed
    completion_criteria: Template performance optimized or baseline confirmed, metrics tracked
    rollback_plan: Revert to previous template version, escalate for manual analysis

rules_and_constraints:
  - rule_id: DOM-011-RL-001
    constraint: Context window must never exceed model limit minus output reservation
    rationale: Prevents inference failure due to token overflow; ensures output generation space
    enforcement: Pre-assembly validation, hard limit enforcement at submission
    exceptions: None; this is a hard constraint
    
  - rule_id: DOM-011-RL-002
    constraint: Token budgets must be allocated before prompt assembly begins
    rationale: Ensures deterministic token allocation and prevents mid-execution budget conflicts
    enforcement: Workflow checkpoint enforcement; assembly blocked without budget plan
    exceptions: None; critical sequencing requirement
    
  - rule_id: DOM-011-RL-003
    constraint: Prompt compression must preserve semantic meaning above 85% threshold
    rationale: Prevents critical information loss that degrades model reasoning
    enforcement: Semantic similarity validation post-compression
    exceptions: May reduce to 75% for cost-critical tasks with explicit approval
    
  - rule_id: DOM-011-RL-004
    constraint: All prompt templates must be versioned and tested before production deployment
    rationale: Prevents unpredictable behavior changes; enables rollback on regression
    enforcement: Template registry validation; deployment workflow requirement
    exceptions: Emergency patches require post-deployment validation within 24 hours
    
  - rule_id: DOM-011-RL-005
    constraint: Semantic cache entries must have TTL and invalidation triggers
    rationale: Prevents stale cached context from producing incorrect responses
    enforcement: Cache entry validation; automatic eviction on TTL expiry or trigger fire
    exceptions: Evergreen context (stable organizational data) may have extended TTL with dependency tracking
    
  - rule_id: DOM-011-RL-006
    constraint: Context must be validated against poisoning before use
    rationale: Prevents adversarial or corrupted context from manipulating model behavior
    enforcement: Poisoning detection pipeline integration; automatic remediation or rejection
    exceptions: None; security critical
    
  - rule_id: DOM-011-RL-007
    constraint: System prompts must be clear and use direct language at the appropriate abstraction level
    rationale: Reduces failure modes from ambiguous instructions; optimizes token usage through clarity
    enforcement: Template review against clarity guidelines; testing validation
    exceptions: Domain-specific terminology acceptable when documented and defined

interfaces:
  - interface_id: DOM-011-IF-001
    connected_domain: DOM-002 (System Architect Agent)
    protocol: DOM-011 receives architecture contracts specifying model capabilities, task types, and system constraints
    contract: "Provided: {model_max_tokens, context_window_limits, supported_task_types, organizational_standards} → DOM-011 produces {context_architecture_constraints, prompt_strategies, token_allocation_rules}"
    
  - interface_id: DOM-011-IF-002
    connected_domain: DOM-012 (Memory Systems)
    protocol: DOM-011 provides context strategies and retrieval formatting; DOM-012 consumes context budgets and semantic cache patterns
    contract: "DOM-011 produces formatted retrieval queries and cache key patterns; DOM-012 returns ranked context fragments within budget"
    
  - interface_id: DOM-011-IF-003
    connected_domain: DOM-013 (Reasoning)
    protocol: DOM-011 manages context for reasoning chains; DOM-013 specifies reasoning chain length requirements
    contract: "DOM-011 allocates context budget for multi-step reasoning; DOM-013 provides step count and intermediate output requirements"
    
  - interface_id: DOM-011-IF-004
    connected_domain: DOM-015 (Code Explorer)
    protocol: DOM-011 provides context window budgets for code exploration depth
    contract: "DOM-011 allocates tokens for code file retrieval, dependency analysis, and context summarization"
    
  - interface_id: DOM-011-IF-005
    connected_domain: DOM-025 (Scaling Strategies)
    protocol: DOM-011 adapts context strategies for large codebase scenarios
    contract: "DOM-011 reduces per-task context overhead, increases semantic cache utilization, implements hierarchical context compression"
    
  - interface_id: DOM-011-IF-006
    connected_domain: DOM-028 (Security)
    protocol: DOM-011 implements sensitive content filtering in context assembly
    contract: "DOM-011 applies content classification and redaction rules before context submission"
    
  - interface_id: DOM-011-IF-007
    connected_domain: DOM-029 (Cost Optimization)
    protocol: DOM-011 receives cost targets and provides token budget enforcement
    contract: "DOM-011 provides token usage tracking and cost-aware compression recommendations"
    
  - interface_id: DOM-011-IF-008
    connected_domain: DOM-033 (Context Poisoning Defense)
    protocol: DOM-011 integrates poisoning detection hooks into context assembly pipeline
    contract: "DOM-011 submits context to poisoning validator before model submission; respects rejection and remediation recommendations"

state_models:
  - state_model_id: DOM-011-SM-001
    name: Context Assembly Pipeline States
    states:
      - state: Empty
        description: No context gathered
      - state: Gathering
        description: Collecting context from sources
      - state: Prioritizing
        description: Ranking context by relevance
      - state: Compressing