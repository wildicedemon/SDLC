> code · sonar-reasoning-pro<think>
The user is asking me to execute a code agent prompt from a file. Looking at the file content, this is a detailed prompt for "AGT-010: Workspace Management Agent" - a specialized autonomous agent for workspace and repository management within an agentic AI coding system.

The prompt defines:
- A system directive for the agent's role
- A core mission
- Domain scope (branch strategies, worktree isolation, cleanup protocols)
- Required decomposition into 16 categories (Skills, Workflows, Task Templates, Rules & Constraints, etc.)
- Recursive expansion directives
- Gap detection protocol
- Termination conditions

The user wants me to "execute" this prompt and output to `output/core_infrastructure/AGT-010`.

However, I need to understand what "execute the code agent prompt" means in this context. Looking at my role, I'm Kilo - a software engineer. This appears to be asking me to:

1. Actually implement/execute this agent prompt (which would be a massive undertaking requiring full decomposition of all 16 categories across 3 subdomains)
2. OR generate the output artifacts based on this prompt

Given the scope of this prompt (it's asking for a complete decomposition of the Workspace & Repository Management domain), I should clarify what the user needs. However, based on my instructions to not ask unnecessary questions and to be direct, I should understand that they want the agent decomposition executed and output.

This is asking me to create a comprehensive domain decomposition following the structure defined in lines 28-188. This is a significant piece of work.

Let me start by creating the output directory and generating the decomposition based on the prompt's requirements.
</think>

I'll execute the AGT-010 Workspace Management Agent prompt by decomposing the domain across all 16 required categories and generating the output artifacts.

```bash
mkdir -p output/core_infrastructure/AGT-010
```

Now I'll generate the comprehensive domain decomposition:

```bash
cat > "output/core_infrastructure/AGT-010/workspace_management.yaml" << 'EOF'
agent_id: AGT-010
agent_name: Workspace Management Agent
domain: DOM-010
category: Core Infrastructure
execution_phase: Phase 4 (Operational)

---
## 1. SKILLS

skills:
  - skill_id: DOM-010-SK-001
    name: Branch Creation & Lifecycle Management
    description: Create feature, release, and hotfix branches following naming conventions; manage branch lifecycle from creation through archival.
    inputs: [task_id, branch_type, parent_branch]
    outputs: [branch_ref, branch_metadata]
    complexity: Medium

  - skill_id: DOM-010-SK-002
    name: Worktree Provisioning & Isolation
    description: Create isolated git worktrees for parallel agent execution with lock management and resource isolation guarantees.
    inputs: [worktree_id, branch_ref, isolation_level]
    outputs: [worktree_path, lock_handle, isolation_token]
    complexity: High

  - skill_id: DOM-010-SK-003
    name: Repository Scaffolding
    description: Generate repository structure, initialize project templates, and configure baseline workflows for new projects.
    inputs: [project_name, template_type, config_overrides]
    outputs: [repo_path, scaffold_manifest]
    complexity: Medium

  - skill_id: DOM-010-SK-004
    name: Workspace Cleanup & Reclamation
    description: Remove stale worktrees, delete merged branches, clean temporary files, and reclaim workspace resources.
    inputs: [workspace_id, retention_policy, force_flag]
    outputs: [cleanup_report, reclaimed_resources]
    complexity: Medium

  - skill_id: DOM-010-SK-005
    name: Merge Conflict Detection & Resolution
    description: Detect merge conflicts, analyze conflict patterns, propose resolutions, and escalate complex conflicts.
    inputs: [source_branch, target_branch, merge_strategy]
    outputs: [conflict_report, resolution_proposals]
    complexity: High

  - skill_id: DOM-010-SK-006
    name: Stale Branch Identification
    description: Identify merged branches, detect dormant branches exceeding age thresholds, and flag branches for archival.
    inputs: [repository_ref, age_threshold_days, merge_status]
    outputs: [stale_branch_list, archival_recommendations]
    complexity: Low

  - skill_id: DOM-010-SK-007
    name: Git Lock Management
    description: Acquire/release git locks, detect deadlocks, manage lock timeouts, and prevent lock contention.
    inputs: [resource_id, lock_type, timeout_seconds]
    outputs: [lock_handle, lock_status]
    complexity: High

  - skill_id: DOM-010-SK-008
    name: Branch Strategy Validation
    description: Validate branch naming conventions, enforce branching model compliance, and audit branch operations.
    inputs: [branch_name, strategy_ruleset, operation_type]
    outputs: [validation_result, compliance_report]
    complexity: Medium

---
## 2. WORKFLOWS

workflows:
  - workflow_id: DOM-010-WF-001
    name: Agent Task Branch Creation Workflow
    trigger: Task architecture received from AGT-005
    steps:
      - step: 1
        action: Validate task architecture structure
        entry_criteria: Task manifest valid
        exit_criteria: All required fields present
      - step: 2
        action: Generate branch name from task_id and type
        entry_criteria: Task ID extracted
        exit_criteria: Branch name follows convention
      - step: 3
        action: Create feature branch from base
        entry_criteria: Parent branch identified
        exit_criteria: Branch exists in remote
      - step: 4
        action: Initialize branch metadata (owner, created_timestamp, task_ref)
        entry_criteria: Branch created
        exit_criteria: Metadata stored in git config
      - step: 5
        action: Register branch in workspace state
        entry_criteria: Metadata initialized
        exit_criteria: Branch tracked in DOM-010-DM-001
    completion_criteria: Branch ready for agent task execution
    rollback_plan: Delete branch, remove metadata, restore parent branch state

  - workflow_id: DOM-010-WF-002
    name: Worktree Provisioning & Teardown
    trigger: Agent requires isolated workspace or task completes
    steps:
      - step: 1
        action: Check worktree availability and locks
        entry_criteria: Request received
        exit_criteria: No lock conflicts detected
      - step: 2
        action: Provision new worktree at unique path
        entry_criteria: Lock acquired
        exit_criteria: Worktree directory exists, git state valid
      - step: 3
        action: Checkout target branch in worktree
        entry_criteria: Worktree provisioned
        exit_criteria: Branch HEAD set correctly
      - step: 4
        action: Record worktree metadata (owner, branch, lease_time)
        entry_criteria: Worktree initialized
        exit_criteria: Metadata in DOM-010-DM-002
      - step: 5
        action: On completion: Lock worktree, signal cleanup
        entry_criteria: Task complete signal
        exit_criteria: Cleanup workflow triggered
      - step: 6
        action: Remove worktree directory, release lock
        entry_criteria: Cleanup approved
        exit_criteria: Worktree deleted, resources freed
    completion_criteria: Worktree cleaned, locks released, state updated
    rollback_plan: Force-release locks, forcefully remove stale worktrees, restore parent branch

  - workflow_id: DOM-010-WF-003
    name: Workspace Cleanup Sweep
    trigger: Periodic timer (hourly) or manual trigger
    steps:
      - step: 1
        action: Scan all worktrees for stale/orphaned instances
        entry_criteria: Cleanup initiated
        exit_criteria: List of candidates identified
      - step: 2
        action: Validate cleanup prerequisites (no active locks, grace period passed)
        entry_criteria: Candidates identified
        exit_criteria: Safe-to-delete list generated
      - step: 3
        action: Remove stale worktrees and associated temporary files
        entry_criteria: Safe-to-delete list confirmed
        exit_criteria: Worktrees deleted
      - step: 4
        action: Scan branches for merge/stale status
        entry_criteria: Worktrees cleaned
        exit_criteria: Stale branch list generated
      - step: 5
        action: Archive stale branches older than threshold
        entry_criteria: Stale branch list confirmed
        exit_criteria: Branches moved to refs/archive/
      - step: 6
        action: Generate cleanup report and update metrics
        entry_criteria: Cleanup complete
        exit_criteria: Report stored, metrics updated
    completion_criteria: All cleanup tasks complete, report generated
    rollback_plan: Restore archived branches from git reflog, manually recreate accidentally deleted worktrees

  - workflow_id: DOM-010-WF-004
    name: Repository Scaffolding Workflow
    trigger: New project creation request
    steps:
      - step: 1
        action: Validate project configuration
        entry_criteria: Project spec provided
        exit_criteria: Config validated against schema
      - step: 2
        action: Create repository with initial commit
        entry_criteria: Config valid
        exit_criteria: Repo exists, main branch created
      - step: 3
        action: Apply project template (directory structure, config files)
        entry_criteria: Repo created
        exit_criteria: Template files committed
      - step: 4
        action: Initialize branch protection rules
        entry_criteria: Template applied
        exit_criteria: Rules enforced on main, develop
      - step: 5
        action: Configure CI/CD webhook triggers
        entry_criteria: Branch rules set
        exit_criteria: CI/CD pipeline integrated
    completion_criteria: Repo ready for development
    rollback_plan: Delete repository, clean up remote refs

  - workflow_id: DOM-010-WF-005
    name: Merge & Integration Workflow
    trigger: Feature branch ready for merge (all checks pass)
    steps:
      - step: 1
        action: Validate merge prerequisites (CI passing, reviews approved)
        entry_criteria: Merge requested
        exit_criteria: All gates passed
      - step: 2
        action: Check for merge conflicts
        entry_criteria: Prerequisites validated
        exit_criteria: Conflict status determined
      - step: 3a
        action: (If no conflicts) Fast-forward or squash merge
        entry_criteria: No conflicts
        exit_criteria: Merge commit created
      - step: 3b
        action: (If conflicts) Run conflict resolution (DOM-010-SK-005)
        entry_criteria: Conflicts detected
        exit_criteria: Resolution proposed or escalated
      - step: 4
        action: Update merge metadata, tag merge commit
        entry_criteria: Merge complete
        exit_criteria: Metadata stored
      - step: 5
        action: Trigger cleanup workflow for source branch
        entry_criteria: Merge committed
        exit_criteria: Cleanup initiated
    completion_criteria: Branch merged, cleanup triggered
    rollback_plan: Revert merge commit, restore branch state

---
## 3. TASK TEMPLATES

templates:
  - template_id: DOM-010-TT-001
    name: Feature Branch Task Template
    purpose: Standard template for agent task execution on feature branches
    structure: |
      {
        "branch_type": "feature",
        "task_id": "<task_ref>",
        "parent_branch": "develop",
        "branch_name": "feature/<domain>/<task_id>",
        "isolation": "worktree",
        "cleanup_on_merge": true
      }

  - template_id: DOM-010-TT-002
    name: Hotfix Branch Task Template
    purpose: Emergency fix workflow with direct merge to main
    structure: |
      {
        "branch_type": "hotfix",
        "task_id": "<task_ref>",
        "parent_branch": "main",
        "branch_name": "hotfix/<version>/<task_id>",
        "isolation": "worktree",
        "expedited_merge": true
      }

  - template_id: DOM-010-TT-003
    name: Parallel Development Task Template
    purpose: Multiple agents working on same project simultaneously
    structure: |
      {
        "branch_type": "feature",
        "task_id": "<task_ref>",
        "parent_branch": "develop",
        "worktree_isolation": "strict",
        "lock_type": "exclusive",
        "conflict_resolution_mode": "escalate"
      }

---
## 4. RULES & CONSTRAINTS

rules:
  - rule_id: DOM-010-RL-001
    constraint: Each agent task must operate in isolated branch or worktree
    rationale: Prevents cross-contamination, enables parallel execution, maintains CI/CD integrity
    enforcement: Workspace provisioning enforces isolation before task execution
    exceptions: None (hard requirement)

  - rule_id: DOM-010-RL-002
    constraint: Worktrees must be cleaned up within 24 hours of task completion
    rationale: Prevents resource exhaustion, reduces lock contention, maintains repository performance
    enforcement: Automatic cleanup sweep with hard deadline
    exceptions: Manual retention for post-mortem analysis (max 72 hours with flag)

  - rule_id: DOM-010-RL-003
    constraint: Branch naming must follow convention: {type}/{domain}/{task_id}
    rationale: Enables automated parsing, maintains consistency, simplifies lifecycle tracking
    enforcement: Branch creation rejects non-compliant names
    exceptions: Legacy branches only (prefixed with legacy/)

  - rule_id: DOM-010-RL-004
    constraint: Stale branches older than threshold must be auto-archived (threshold: 30 days)
    rationale: Reduces branch clutter, improves git performance, maintains clean repository state
    enforcement: Cleanup sweep identifies and archives stale branches
    exceptions: Protected branches (main, develop), branches with active locks

  - rule_id: DOM-010-RL-005
    constraint: Merge operations must pass all quality gates before integration
    rationale: Ensures code quality, prevents broken main/develop, maintains CI/CD reliability
    enforcement: Merge workflow validates CI passing, approvals, security checks
    exceptions: Emergency hotfixes (logged and reviewed post-merge)

  - rule_id: DOM-010-RL-006
    constraint: Worktree locks must timeout after 12 hours if not renewed
    rationale: Prevents deadlocks from crashed agents, enables recovery
    enforcement: Lock manager tracks creation time, forces release on timeout
    exceptions: Critical production operations (explicit timeout extension)

  - rule_id: DOM-010-RL-007
    constraint: All workspace operations must have documented cleanup protocols
    rationale: Ensures resource guarantee, prevents cascading failures
    enforcement: Workspace manager validates cleanup handlers before operation
    exceptions: Read-only queries (no cleanup required)

  - rule_id: DOM-010-RL-008
    constraint: Repository state must remain consistent (no orphaned refs/objects)
    rationale: Maintains git integrity, enables reliable recovery
    enforcement: Periodic git fsck, automatic garbage collection
    exceptions: None (hard database constraint)

---
## 5. INTERFACES

interfaces:
  - interface_id: DOM-010-IF-001
    connected_domain: DOM-005 (Task Architecture)
    protocol: Sync pull after AGT-005 completion
    contract: |
      Input: TaskArchitecture {task_id, decomposition[], resource_estimate}
      Output: WorkspaceConfig {branch_strategy, worktree_count, isolation_level}
      SLA: Response within 100ms

  - interface_id: DOM-010-IF-002
    connected_domain: DOM-021 (CI/CD Pipeline)
    protocol: Event-based (branch created/merged triggers CI/CD)
    contract: |
      Input: BranchEvent {branch_name, event_type, commit_sha}
      Output: CIPipelineConfig {trigger_ruleset, stage_gates}
      SLA: CI triggered within 5 seconds of branch event

  - interface_id: DOM-010-IF-003
    connected_domain: DOM-025 (Scaling Strategies)
    protocol: Query interface for workspace allocation
    contract: |
      Input: ScalingRequest {concurrent_tasks, resource_profile}
      Output: WorkspaceAllocation {worktree_slots, lock_distribution}
      SLA: Allocation within 50ms

  - interface_id: DOM-010-IF-004
    connected_domain: DOM-027 (Deployment)
    protocol: Branch reference provided to deployment agent
    contract: |
      Input: DeploymentRequest {branch_ref, target_environment}
      Output: DeploymentConfig