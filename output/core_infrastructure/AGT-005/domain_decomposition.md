> code · sonar-reasoning-pro

<think>
The user is asking me to execute a complex architecture task based on a system directive in AGT-005_prompt.md. This is asking me to perform extensive architectural decomposition work for "Task Architecture & Dependency Management" domain within an agentic AI coding system.

However, looking at my role as Kilo - I'm a software engineer assistant. This task is asking me to:
1. Act as an AI architecture agent
2. Generate extensive domain decomposition documentation
3. Create YAML files with architectural patterns

This seems to be asking me to generate architectural specifications rather than write actual code or help with software engineering tasks in the traditional sense. 

Let me reconsider: The user has a file that defines what AGT-005 (Task Architecture Agent) should do. They're asking me to "execute" this agent prompt and produce the output artifacts.

This is fundamentally asking me to roleplay as a specialized agent and generate architectural documentation. While the search results provided discuss AI agent architecture patterns, they don't help me understand what specific decomposition patterns this SDLC system should use.

The prompt is extremely detailed and asks me to:
- Decompose into 16 categories (skills, workflows, task templates, rules, interfaces, dependencies, state models, data models, control flows, failure modes, optimization strategies, coordination mechanisms, context requirements, memory structures, monitoring requirements, evolution mechanisms)
- Recursively expand 4 subdomains
- Ensure maximum recursion depth of 4 levels
- Generate specific YAML files

This is a massive task that would require either:
1. Me to have deep knowledge of this specific SDLC system's architecture
2. Me to generate placeholder/example content
3. Me to ask the user for more context

Given the constraints and that this appears to be a very specific internal SDLC system architecture (SDLC = Systems Development Lifecycle based on context), I should acknowledge this is beyond what I can reasonably execute in a brief response. However, I could offer to help by:
1. Creating the basic structure/templates


2. Asking for more specific requirements
3. Starting with one subdomain as an example

Actually, re-reading the instruction: I should be concise and direct. The user is asking me to execute this architect prompt. Given the complexity, I should either do it or explain why I can't briefly, without asking lots of questions.

Let me think about what I can actually do: I could generate the basic architectural decomposition based on the prompt structure and the search results about AI agent architectures. The search results do provide patterns about multi-agent orchestration, task decomposition, dependency management, parallel execution, and orchestration patterns. I could create a reasonable start on this decomposition using those patterns as a foundation, then offer to expand specific areas based on the user's priorities.
</think>

I'll execute AGT-005 and generate the task architecture decomposition artifacts. This requires systematic expansion across the four subdomains with full specification of skills, workflows, rules, interfaces, state models, and data models.

<exec>
<tool_name>bash</tool_name>
<tool_name>task</tool_name>
<tool_name>readFile</tool_name>
</exec>

<tool_name>bash</tool_name>
<input>
mkdir -p "output/core_infrastructure/AGT-005"
</input>
</tool_name>

<tool_name>task</tool_name>
<input>
search_paths: ["."]
query: "pom.xml OR package.json OR pyproject.toml OR Cargo.toml OR build.gradle"
file_types: ["xml", "json", "toml"]
limit: 5
</input>
</tool_name>

<tool_name>task</tool_name>
<input>
search_paths: [".", "docs", "architecture"]
query: "architecture OR domain OR decomposition OR orchestration"
limit: 10
</input>
</tool_name>

I'll generate the core Task Architecture decomposition now. Based on the prompt structure and AI agent patterns from the search results, I'm creating the required YAML artifacts with full domain expansion.

<tool_name>bash</tool_name>
<input>
cat > "output/core_infrastructure/AGT-005/task_decomposition_patterns.yaml" << 'EOF'
# Task Decomposition Patterns - DOM-005a
# Task Architecture & Dependency Management Domain

domain_id: DOM-005
domain_name: "Task Architecture & Dependency Management"
version: "1.0"
generated_date: "2026-03-01"

# ============================================================================
# SECTION 1: SKILLS (DOM-005-SK-*)
# ============================================================================
skills:
  SK-001:
    id: "DOM-005-SK-001"
    name: "Hierarchical Task Decomposition"
    description: "Break complex goals into recursive task hierarchies with bounded depth, applying domain-specific heuristics for each decomposition level."
    inputs:
      - parent_task_definition
      - decomposition_heuristics
      - domain_context
    outputs:
      - task_tree_structure
      - leaf_task_definitions
      - dependency_skeleton
    complexity: "High"
    prevents_failure_mode: "KA-017"

  SK-002:
    id: "DOM-005-SK-002"
    name: "Dependency Graph Construction"
    description: "Build acyclic directed graphs representing inter-task dependencies, including data flow, temporal ordering, and resource constraints."
    inputs:
      - task_definitions_list
      - dependency_specifications
      - resource_requirements
    outputs:
      - dependency_dag
      - critical_path_nodes
      - cycle_check_report
    complexity: "High"
    prevents_failure_mode: "KA-039"

  SK-003:
    id: "DOM-005-SK-003"
    name: "Critical Path Analysis"
    description: "Identify longest dependency chains and critical tasks that control project completion time."
    inputs:
      - task_dag
      - duration_estimates
      - parallelism_constraints
    outputs:
      - critical_path_sequence
      - slack_calculations
      - schedule_metrics
    complexity: "Medium"

  SK-004:
    id: "DOM-005-SK-004"
    name: "Parallel Execution Planning"
    description: "Partition independent tasks for concurrent execution while managing shared resources and synchronization barriers."
    inputs:
      - dependency_dag
      - resource_inventory
      - concurrency_limits
    outputs:
      - parallel_execution_plan
      - synchronization_points
      - resource_allocation_map
    complexity: "High"
    prevents_failure_mode: "KA-042"

  SK-005:
    id: "DOM-005-SK-005"
    name: "Atomic Commit Orchestration"
    description: "Coordinate all-or-nothing task completion with transaction boundaries, rollback logic, and consistency guarantees."
    inputs:
      - completed_task_results
      - transaction_boundaries
      - rollback_state_vectors
    outputs:
      - commit_transaction_record
      - rollback_recovery_plan
      - consistency_proof
    complexity: "High"

  SK-006:
    id: "DOM-005-SK-006"
    name: "Recursion Depth Enforcement"
    description: "Monitor and enforce bounded recursion during task decomposition to prevent planning spirals."
    inputs:
      - current_decomposition_depth
      - maximum_allowed_depth
      - decomposition_stack
    outputs:
      - depth_validation_report
      - decomposition_halt_signals
    complexity: "Low"
    prevents_failure_mode: "KA-017"

  SK-007:
    id: "DOM-005-SK-007"
    name: "Task Estimation & Sizing"
    description: "Estimate computational cost, duration, and resource requirements for tasks based on type, complexity, and historical data."
    inputs:
      - task_specification
      - historical_task_metrics
      - complexity_factors
    outputs:
      - cost_estimate
      - duration_estimate
      - resource_requirements
    complexity: "Medium"

  SK-008:
    id: "DOM-005-SK-008"
    name: "Distributed Coordination Prevention"
    description: "Enforce timeouts and failure detection to prevent indefinite waits in distributed task orchestration."
    inputs:
      - coordination_operations
      - timeout_policies
      - heartbeat_configurations
    outputs:
      - timeout_enforced_plan
      - failure_detection_rules
      - coordination_bounds
    complexity: "Medium"
    prevents_failure_mode: "KA-041"

  SK-009:
    id: "DOM-005-SK-009"
    name: "Task Template Instantiation"
    description: "Create concrete task instances from reusable templates with parameter binding and context injection."
    inputs:
      - task_template
      - parameter_values
      - execution_context
    outputs:
      - concrete_task_instance
      - bound_dependencies
      - assigned_executor
    complexity: "Low"

  SK-010:
    id: "DOM-005-SK-010"
    name: "Cycle Detection & Prevention"
    description: "Detect circular dependencies in task graphs and prevent their creation during decomposition."
    inputs:
      - dependency_graph
      - new_dependency_proposals
    outputs:
      - cycle_detection_report
      - cycle_prevention_constraints
    complexity: "Medium"

# ============================================================================
# SECTION 2: WORKFLOWS (DOM-005-WF-*)
# ============================================================================
workflows:
  WF-001:
    id: "DOM-005-WF-001"
    name: "Task Decomposition Workflow"
    description: "Complete workflow for breaking down complex goals into executable task trees"
    trigger: "High-level goal or architectural contract from AGT-002"
    steps:
      - step_num: 1
        action: "Receive goal specification"
        entry_criteria: ["Goal has clear acceptance criteria"]
        exit_criteria: ["Goal parsed and validated"]
      - step_num: 2
        action: "Apply decomposition heuristics based on task domain"
        entry_criteria: ["Goal validated", "Decomposition strategy selected"]
        exit_criteria: ["Subtask candidates identified"]
      - step_num: 3
        action: "Enforce recursion depth bound"
        entry_criteria: ["Decomposition depth < MAX_DEPTH"]
        exit_criteria: ["Depth validation passed"]
      - step_num: 4
        action: "Create leaf task definitions"
        entry_criteria: ["Recursion bound satisfied"]
        exit_criteria: ["All tasks have estimated_cost, estimated_duration"]
      - step_num: 5
        action: "Build dependency skeleton"
        entry_criteria: ["Leaf tasks defined"]
        exit_criteria: ["Initial dependency relationships identified"]
      - step_num: 6
        action: "Resolve final task tree"
        entry_criteria: ["All tasks and dependencies specified"]
        exit_criteria: ["Task tree is complete and consistent"]
    completion_criteria:
      - "All tasks have unique IDs"
      - "All tasks have estimated_cost and estimated_duration"
      - "Root task decomposition is complete"
      - "Leaf tasks are atomic and undecomposable"
      - "No circular parent-child relationships"
    rollback_plan: "Revert to previous decomposition version; alert AGT-002 of decomposition failure"

  WF-002:
    id: "DOM-005-WF-002"
    name: "Dependency Graph Resolution Workflow"
    description: "Build and validate acyclic dependency DAG with cycle detection and critical path analysis"
    trigger: "Task tree completed (WF-001 completion)"
    steps:
      - step_num: 1
        action: "Extract all task dependencies from task definitions"
        entry_criteria: ["Task tree exists"]
        exit_criteria: ["Dependency list compiled"]
      - step_num: 2
        action: "Construct directed graph from dependencies"
        entry_criteria: ["Dependency list complete"]
        exit_criteria: ["DAG structure created"]
      - step_num: 3
        action: "Perform cycle detection"
        entry_criteria: ["DAG constructed"]
        exit_criteria: ["Cycle check completed; report generated"]
      - step_num: 4
        action: "Compute critical path"
        entry_criteria: ["DAG is acyclic"]
        exit_criteria: ["Critical path sequence identified"]
      - step_num: 5
        action: "Calculate task slack and scheduling flexibility"
        entry_criteria: ["Critical path computed"]
        exit_criteria: ["Slack values assigned to all tasks"]
      - step_num: 6
        action: "Validate dependency feasibility"
        entry_criteria: ["DAG complete; slack computed"]
        exit_criteria: ["Feasibility report generated"]
    completion_criteria:
      - "DAG is acyclic (no circular dependencies)"
      - "All dependencies are bidirectional where required"
      - "Critical path is identified"
      - "All tasks have slack calculations"
    rollback_plan: "Reject decomposition; return to task tree refinement phase"

  WF-003:
    id: "DOM-005-WF-003"
    name: "Parallel Execution Orchestration Workflow"
    description: "Plan concurrent task execution, allocate resources, establish synchronization barriers"
    trigger: "Dependency graph resolved (WF-002 completion)"
    steps:
      - step_num: 1
        action: "Identify independent task clusters"
        entry_criteria: ["Dependency DAG complete"]
        exit_criteria: ["Independent task sets identified"]
      - step_num: 2
        action: "Check shared resource requirements"
        entry_criteria: ["Independent clusters identified"]
        exit_criteria: ["Resource conflict matrix built"]
      - step_num: 3
        action: "Establish synchronization barriers"
        entry_criteria: ["Resource requirements known"]
        exit_criteria: ["Barrier points defined between dependent clusters"]
      - step_num: 4
        action: "Allocate available parallelism budget"
        entry_criteria: ["Barriers defined", "Concurrency limits known"]
        exit_criteria: ["Parallel execution plan created"]
      - step_num: 5
        action: "Validate consistency-parallelism tradeoff"
        entry_criteria: ["Execution plan created"]
        exit_criteria: ["Tradeoff validation report generated"]
    completion_criteria:
      - "All independent tasks are scheduled in parallel"
      - "All shared resources have exclusive access guards"
      - "Synchronization barriers are minimal"
      - "Parallelism ≤ available system capacity"
    rollback_plan: "Revert to sequential execution; reduce parallelism degree"

  WF-004:
    id: "DOM-005-WF-004"
    name: "Atomic Commit Workflow"
    description: "Coordinate all-or-nothing completion of task groups with rollback capability"
    trigger: "Task batch ready for commit (post-execution)"
    steps:
      - step_num: 1
        action: "Collect completed task results"
        entry_criteria: ["All tasks in batch have completed status"]
        exit_criteria: ["Results validated and staged"]
      - step_num: 2
        action: "Build rollback state vector"
        entry_criteria: ["Results staged"]
        exit_criteria: ["Pre-commit state snapshots created"]
      - step_num: 3
        action: "Validate commit preconditions"
        entry_criteria: ["State vectors created"]
        exit_criteria: ["Precondition validation passed"]
      - step_num: 4
        action: "Execute atomic commit"
        entry_criteria: ["Preconditions validated"]
        exit_criteria: ["Commit record created"]
      - step_num: 5
        action: "Verify consistency"
        entry_criteria: ["Commit executed"]
        exit_criteria: ["Post-commit consistency verified"]
    completion_criteria:
      - "All or no tasks in batch are committed"
      - "Rollback state is preserved"
      - "Commit transaction record exists"
    rollback_plan: "Execute rollback_steps in reverse order; return system to pre-commit state"

  WF-005:
    id: "DOM-005-WF-005"
    name: "Task Re-planning Workflow (Dependency Failure Recovery)"
    description