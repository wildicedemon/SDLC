> code · sonar-reasoning-pro

<think>
The user is asking me to read and execute the architect agent prompt from the file they provided. This is AGT-006: Distributed Orchestration Agent.

Looking at the file, this is a prompt that describes what AGT-006 should do. The agent is supposed to:

1. Decompose the "Distributed & Multi-Repository Orchestration" domain
2. Receive input from AGT-004 (Agent Architecture Agent) and AGT-005 (Task Architecture Agent)
3. Produce distributed coordination protocols, multi-repo workflow definitions, and shared state protocols
4. Output artifacts to: `distributed_coordination.yaml`, multi-repo workflow definitions, shared state protocols, synchronization rules

The prompt asks the agent to fully decompose the domain into 16 categories:
1. Skills
2. Workflows
3. Task Templates
4. Rules & Constraints
5. Interfaces
6. Dependencies
7. State Models
8. Data Models
9. Control Flows
10. Failure Modes & Recovery
11. Optimization Strategies
12. Coordination Mechanisms
13. Context Requirements
14. Memory Structures
15. Monitoring Requirements
16. Evolution Mechanisms

The search results provided are about AI Agent Orchestration - which is relevant background information about what orchestration is.

The user wants me to execute this prompt and output to `output/core_infrastructure/AGT-006`.

However, I'm an interactive CLI tool meant to help with software engineering tasks. This prompt is asking me to act as if I'm an AI agent (AGT-006) and decompose a complex domain according to specific architecture rules. 

I should interpret this as: the user wants me to process this prompt file and generate the architectural decomposition it describes, outputting the results to the specified directory.

I need to:
1. Create the output directory structure
2. Generate the decomposition according to the 16 categories specified
3. Merge knowledge about distributed orchestration (from the search results and my knowledge)
4. Output YAML files with the required artifacts


5. Proceed with executing this as a legitimate software architecture documentation task.
</think>

I'll execute the AGT-006 Distributed Orchestration Agent prompt and generate the architectural decomposition. This requires creating comprehensive YAML artifacts for distributed multi-repository orchestration patterns.

Let me begin by creating the output directory and generating the decomposition across all 16 required categories.

```bash
mkdir -p "c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\core_infrastructure\AGT-006"
```

Now I'll generate the core orchestration artifacts:

```yaml
# output/core_infrastructure/AGT-006/distributed_coordination.yaml
agent_id: AGT-006
domain: DOM-006
name: Distributed Orchestration Agent
version: "1.0"

domain_scope:
  sd_006a: "Multi-Agent Coordination"
  sd_006b: "Multi-Repo Workflows"
  sd_006c: "Shared State Protocols"

# SECTION 1: SKILLS
skills:
  DOM-006-SK-001:
    name: Multi-Repo Workflow Construction
    description: Designs and constructs workflows that span multiple repositories with coordinated task execution and dependency management.
    inputs: [Repository topology, Task specifications, Dependency graph]
    outputs: [Workflow definition, Execution plan]
    complexity: High
    related_ka: KA-034

  DOM-006-SK-002:
    name: Distributed Agent Message Routing
    description: Routes and manages asynchronous messages between agents across repository boundaries with guaranteed delivery semantics.
    inputs: [Agent registry, Message queue, Routing rules]
    outputs: [Routed messages, Delivery acknowledgments]
    complexity: High

  DOM-006-SK-003:
    name: Shared State Synchronization
    description: Synchronizes shared state across agent boundaries using eventual consistency, conflict resolution, and optimistic locking.
    inputs: [State snapshots, Modification logs, Conflict metadata]
    outputs: [Synchronized state, Conflict resolution log]
    complexity: High
    related_ka: KA-041

  DOM-006-SK-004:
    name: Cross-Repository Atomic Commit Orchestration
    description: Coordinates atomic commits across multiple repositories using two-phase commit or saga patterns with rollback capability.
    inputs: [Repository states, Commit specifications, Rollback strategies]
    outputs: [Commit status, Transaction log]
    complexity: High

  DOM-006-SK-005:
    name: Distributed Consensus Execution
    description: Executes distributed consensus protocols (Raft, Paxos, quorum-based) to reach agreement across agent clusters.
    inputs: [Agent states, Decision requirements, Consensus parameters]
    outputs: [Consensus decision, Agreement proof]
    complexity: High

  DOM-006-SK-006:
    name: Coordination Failure Detection
    description: Detects and categorizes distributed coordination failures including timeouts, network partitions, and inconsistent states.
    inputs: [Agent heartbeats, Message delivery status, State checksums]
    outputs: [Failure diagnosis, Recovery recommendations]
    complexity: Medium
    related_ka: KA-041

  DOM-006-SK-007:
    name: Repository Topology Mapping
    description: Maps and maintains the topology of repository dependencies, relationships, and access patterns.
    inputs: [Repository metadata, Dependency declarations]
    outputs: [Topology graph, Dependency matrix]
    complexity: Medium

  DOM-006-SK-008:
    name: Cross-Repo Conflict Detection
    description: Detects conflicts when multiple agents modify shared code or state across repositories.
    inputs: [Modification logs, State snapshots, Merge metadata]
    outputs: [Conflict list, Conflict severity assessment]
    complexity: Medium

  DOM-006-SK-009:
    name: Workflow State Machine Management
    description: Manages state transitions and invariants for distributed workflows with recovery from partial failures.
    inputs: [Workflow specification, Event stream, State snapshots]
    outputs: [State transitions, Invariant validation results]
    complexity: Medium

  DOM-006-SK-010:
    name: Network Partition Recovery
    description: Recovers coordination after network partitions by reconciling divergent states and re-establishing consensus.
    inputs: [Partition metadata, Diverged states, Consensus log]
    outputs: [Reconciliation plan, Updated consensus state]
    complexity: High

# SECTION 2: WORKFLOWS
workflows:
  DOM-006-WF-001:
    name: Multi-Repo Change Propagation
    description: Coordinates changes across multiple repositories maintaining consistency and enabling rollback.
    trigger: "Change request targets multiple repositories"
    steps:
      - step_1: "Validate repository topology and access"
        exit_criteria: "All target repos identified and accessible"
      - step_2: "Decompose change into per-repo modifications"
        exit_criteria: "Per-repo change specifications generated"
      - step_3: "Acquire distributed locks on target repos"
        exit_criteria: "All locks acquired or timeout"
      - step_4: "Execute per-repo modifications in sequence/parallel"
        exit_criteria: "All modifications applied or detected failure"
      - step_5: "Validate state consistency across repos"
        exit_criteria: "Consistency verified or conflicts detected"
      - step_6: "Commit across all repos atomically"
        exit_criteria: "All commits successful or rollback initiated"
    completion_criteria: "All repos committed with consistent state"
    rollback_plan: "Two-phase rollback: prepare rollback on all repos, then execute in reverse order"

  DOM-006-WF-002:
    name: Distributed Agent Coordination Workflow
    description: Orchestrates execution of multiple agents on distributed tasks with synchronization points.
    trigger: "Complex task requires multiple specialized agents"
    steps:
      - step_1: "Decompose task into agent-appropriate subtasks"
        exit_criteria: "Subtask graph with dependencies generated"
      - step_2: "Select agents based on capability matching"
        exit_criteria: "Agent assignments determined"
      - step_3: "Initialize agent execution contexts"
        exit_criteria: "Execution contexts ready"
      - step_4: "Distribute subtasks respecting dependencies"
        exit_criteria: "All agents notified of their tasks"
      - step_5: "Monitor agent progress and detect failures"
        exit_criteria: "Continuous monitoring established"
      - step_6: "Synchronize at checkpoints and merge results"
        exit_criteria: "All agents reached checkpoint or failure detected"
    completion_criteria: "All subtasks complete with aggregated results"
    rollback_plan: "Send abort signal to all agents, revert shared state to checkpoint"

  DOM-006-WF-003:
    name: State Synchronization Workflow
    description: Synchronizes shared state across agent boundaries using conflict resolution.
    trigger: "State divergence detected or scheduled sync interval"
    steps:
      - step_1: "Collect state snapshots from all agents"
        exit_criteria: "All snapshots received within timeout"
      - step_2: "Compute state checksum and detect conflicts"
        exit_criteria: "Conflict analysis complete"
      - step_3: "Resolve conflicts using strategy (last-write-wins, merge, custom)"
        exit_criteria: "Conflict resolution completed"
      - step_4: "Distribute reconciled state to all agents"
        exit_criteria: "All agents acknowledged receipt"
      - step_5: "Verify consistency post-sync"
        exit_criteria: "Checksums match across all agents"
    completion_criteria: "All agents converged to consistent state"
    rollback_plan: "Restore previous known-good state snapshot"

  DOM-006-WF-004:
    name: Cross-Repo Conflict Resolution Workflow
    description: Detects and resolves conflicts when changes span multiple repositories.
    trigger: "Conflicting modifications detected across repos"
    steps:
      - step_1: "Isolate conflicting changes"
        exit_criteria: "Conflicting code sections identified"
      - step_2: "Analyze conflict severity and impact"
        exit_criteria: "Impact assessment completed"
      - step_3: "Apply conflict resolution strategy"
        exit_criteria: "Merged state produced"
      - step_4: "Validate merged state semantically"
        exit_criteria: "No compilation/semantic errors"
      - step_5: "Distribute resolved state to affected repos"
        exit_criteria: "All repos updated"
    completion_criteria: "Conflict resolved and state consistent"
    rollback_plan: "Revert to pre-conflict state snapshot"

  DOM-006-WF-005:
    name: Distributed Rollback Workflow
    description: Orchestrates rollback of changes across multiple repositories after failure.
    trigger: "Commit failure or inconsistency detection in multi-repo transaction"
    steps:
      - step_1: "Identify rollback scope (affected repos)"
        exit_criteria: "Rollback scope determined"
      - step_2: "Acquire rollback locks on all affected repos"
        exit_criteria: "All locks acquired"
      - step_3: "Execute rollback in reverse order of commit"
        exit_criteria: "All rollbacks successful or partial failure recorded"
      - step_4: "Verify state consistency post-rollback"
        exit_criteria: "All repos returned to pre-commit state"
      - step_5: "Release locks and notify stakeholders"
        exit_criteria: "Locks released, notifications sent"
    completion_criteria: "All repos successfully rolled back to pre-failure state"
    rollback_plan: "Force unlock if lock acquisition times out; restore from backup"

# SECTION 3: TASK TEMPLATES
task_templates:
  DOM-006-TT-001:
    name: Multi-Repo Task Template
    purpose: "Reusable pattern for tasks that span multiple repositories"
    structure: |
      {
        task_id: string,
        repos: [repository],
        modifications: [{repo, operations}],
        dependencies: [task_id],
        timeout: duration,
        rollback_strategy: enum
      }

  DOM-006-TT-002:
    name: Agent Coordination Task Template
    purpose: "Reusable pattern for coordinating multiple agents"
    structure: |
      {
        task_id: string,
        agents: [agent_id],
        subtasks: [{agent, specification}],
        synchronization_points: [checkpoint],
        aggregation_strategy: enum
      }

  DOM-006-TT-003:
    name: State Sync Task Template
    purpose: "Reusable pattern for state synchronization"
    structure: |
      {
        task_id: string,
        state_scope: string,
        consistency_model: enum,
        conflict_resolution: strategy,
        verification_rules: [rule]
      }

# SECTION 4: RULES & CONSTRAINTS
rules:
  DOM-006-RL-001:
    constraint: "All distributed operations must have timeout bounds"
    rationale: "Prevents indefinite blocking in case of network failures or agent unavailability"
    prevention_km: KA-041
    enforcement: "Timeout validation in orchestration layer; automatic abort on timeout"
    exceptions: "None - timeouts are mandatory"

  DOM-006-RL-002:
    constraint: "Cross-repo commits must be atomic or have defined partial-commit recovery"
    rationale: "Ensures no repos left in inconsistent state after multi-repo operations"
    prevention_km: KA-041
    enforcement: "Orchestrator validates commit completeness; triggers rollback on partial failure"
    exceptions: "Explicit partial-commit allowed only with documented recovery strategy"

  DOM-006-RL-003:
    constraint: "Shared state modifications must use optimistic locking or explicit coordination"
    rationale: "Prevents lost updates and race conditions in concurrent modifications"
    prevention_km: KA-041
    enforcement: "Orchestrator enforces locking protocol; detects and resolves conflicts"
    exceptions: "None for critical state; non-critical state may use eventual consistency with documented bounds"

  DOM-006-RL-004:
    constraint: "Repository topology must be declared before cross-repo workflows execute"
    rationale: "Enables dependency analysis and prevents circular dependencies"
    enforcement: "Topology validation gate in workflow initialization"
    exceptions: "Dynamic topology allowed only with explicit versioning and compatibility checks"

  DOM-006-RL-005:
    constraint: "All agent-to-agent communication must be asynchronous with retry semantics"
    rationale: "Prevents cascading failures and enables resilience to transient faults"
    enforcement: "Message router enforces asynchronous delivery with exponential backoff"
    exceptions: "Synchronous calls allowed only for critical coordination with explicit timeout"

  DOM-006-RL-006:
    constraint: "State synchronization conflicts must be detected and resolved within configured bounds"
    rationale: "Prevents divergent states from persisting indefinitely"
    enforcement: "Periodic conflict detection with automatic resolution strategy"
    exceptions: "Manual resolution allowed with operator intervention and audit trail"

# SECTION 5: INTERFACES
interfaces:
  DOM-006-IF-001:
    connected_domain: DOM-004
    name: "Agent Patterns → Distributed Agent Coordination"
    direction: Input
    protocol: "AGT-004 provides agent capability declarations; AGT-006 uses to assign tasks to agents"
    contract: |
      Input: Agent capability manifests with skill signatures
      Output: Agent selection decisions with task assignments
    data_format: YAML/JSON
    dependency_type: "Hard"

  DOM-006-IF-002:
    connected_domain: DOM-005
    name: "Task Decomposition → Distributed Task Assignment"
    direction: Input
    protocol: "AGT-005 provides task decomposition graph; AGT-006 maps to distributed execution plan"
    contract: |
      Input: Task dependency graph with execution constraints
      Output: Distributed execution plan with ordering and parallelism decisions
    data_format: YAML/JSON
    dependency_type: "Hard"

  DOM-006-IF-003:
    connected_domain: DOM-010
    name: "Multi-Repo Workflows → Workspace/Branch Management"
    direction: Output
    protocol: "AGT-006 produces multi-repo workflow definitions; DOM-010 manages branches and workspace state"
    contract: |
      Output: Multi-repo workflow with branch management requirements
      Input: Branch management capabilities and constraints
    data_format: YAML/JSON
    dependency_type: "Hard"

  DOM-006-IF-004:
    connected_domain: DOM-036
    name: "Coordination Failures → Distributed Error Recovery"
    direction: Output
    protocol: "AGT-006 detects coordination failures; DOM-036 provides recovery strategies"
    contract: |
      Output: Failure detection and diagnosis
      Input: Recovery actions and rollback specifications
    data_format: YAML/JSON
    dependency_type: "Hard"

  DOM-006-IF-005: