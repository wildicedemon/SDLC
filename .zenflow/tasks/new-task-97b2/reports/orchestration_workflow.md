# Domain Report: Orchestration & Workflow Management

## A. Executive Summary

This report synthesizes orchestration and workflow patterns for the AI Agentic Autonomous SDLC Framework. The framework adopts a hierarchical task decomposition model (Initiative > Phase > Stage > Task > Atomic Action) driven by LangGraph state machines, with Kilo Code providing multi-mode agent execution. Key findings indicate that deterministic mode transitions, checkpoint-based progress verification, and unidirectional control flow are essential for reliable autonomous operation. Critical gaps remain in automated rollback on quality gate failure and multi-agent conflict resolution strategy.

*Sources: Research.md §II (Agent & Orchestration Architecture), §2.3 (SDLC Workflow Framework); start_prompt.md §2.3, §2.6, §4.2, §4.3*

## B. Core Concepts

- **Five-level hierarchy**: Initiative > Phase > Stage > Task > Atomic Action; each level inherits parent context and reports status upward *(Research.md §II.6; start_prompt.md §4.2)*
- **LangGraph state graph**: SDLC phases modeled as directed graph nodes with persisted state between transitions *(start_prompt.md §4.4.2)*
- **Dual orchestrator model**: Zenflow manages task lifecycle; Kilo Code executes via Orchestrator, Architect, Code, Debug, Review modes *(start_prompt.md §2.6)*
- **Deterministic mode transitions**: Planning outputs trigger Architect mode; designs trigger Code mode; failures trigger Debug mode *(start_prompt.md §6.3)*
- **Checkpoint protocol**: Mandatory verification every 5 tasks, at 50% budget, before architectural decisions, on risk detection *(start_prompt.md §4.3)*
- **Self-directed task selection**: Agent selects next task by priority and dependency resolution without per-step approval *(start_prompt.md §4.3)*
- **Adaptive replanning**: Blocked tasks trigger replanning; escalation only on blocking failures or budget overruns *(start_prompt.md §4.3)*
- **Context passing between modes**: Each mode receives structured context from predecessor; no implicit state *(Research.md §2.3)*
- **Task dependency graph**: DAG-based sequencing with parallelizable work identification *(start_prompt.md §4.2)*
- **Branch isolation**: Feature branches for all framework work; no direct commits to main *(start_prompt.md §2.1)*
- **Work tree lifecycle management**: Git worktrees enable parallel agent execution on separate branches *(Research.md §II.6)*
- **Background/async agents**: Daemon agents for continuous operations like scanning *(Research.md §II.7)*

## C. Implementation Guidance

### What to Build

| Component | Location | Purpose |
|-----------|----------|---------|
| LangGraph SDLC graph | `src/framework/graph.ts` | State machine for phase transitions |
| CLI wrapper | `src/framework/cli.ts` | Entry point: `framework start\|status\|scan\|bootstrap` |
| Task decomposition engine | `src/framework/task-decomposer.ts` | Automated breakdown with dependency graphing |
| Mode transition controller | `src/framework/mode-controller.ts` | Deterministic Orchestrator > Specialist handoffs |
| Kilo custom modes | `.kilo/modes/*.yaml` | Requirements, Scanner, Review YAML definitions |
| Progress tracker | `src/framework/progress.ts` | Checkpoint enforcement and status reporting |

### How to Build It

- **LangGraph integration**: Define graph nodes for Research, Planning, Implementation, Verification; persist state between transitions; wrap existing LangGraph CLI rather than reimplementing *(start_prompt.md §4.4.2)*
- **Task decomposition**: Parse requirements into DAG; identify parallelizable subtasks; assign to appropriate execution modes *(start_prompt.md §4.2)*
- **Mode transitions**: Implement as deterministic state machine: Research > Planning > Architect > Code > Review; failures route to Debug mode with remediation subtask creation *(start_prompt.md §6.3)*
- **Custom modes**: Each YAML defines `roleDefinition`, `groups`, `tools`, `customInstructions`, `description`; three custom + built-in Orchestrator *(start_prompt.md §4.4.3)*
- **Checkpoint logic**: After every 5 tasks: compile and test; at phase boundary: integration tests; before completion: full suite *(start_prompt.md §6.2)*

### Why This Approach

- LangGraph provides directed graph semantics with built-in state management; avoids custom state machine complexity *(Master Report D-1)*
- Wrapping LangGraph CLI avoids duplicating existing functionality *(Master Report D-2)*
- Three custom modes + built-in Orchestrator minimizes mode proliferation *(Master Report D-3)*
- Unidirectional control flow prevents circular dependencies between phases

### Dependencies

- LangGraph runtime and CLI must be installed (via bootstrap)
- Kilo Code extension must support custom mode YAML loading
- MCP servers (CodeGraphContext, rag-memory-mcp, TaskMaster) must be available for agent execution
- Zenflow task API for lifecycle management

## D. Validation Criteria

| Criterion | Metric | Method |
|-----------|--------|--------|
| Phase transitions | All 4 SDLC phases complete in sequence | E2E test: full pipeline run |
| Mode switching | Modes activate on correct triggers | Integration test: mode transition matrix |
| Task decomposition | Requirements decompose into valid DAG | Unit test: cycle detection, dependency resolution |
| Checkpoint enforcement | Progress verified at defined intervals | Unit test: checkpoint trigger conditions |
| CLI commands | All commands execute without errors | Integration test: `framework start\|status\|scan\|bootstrap` |
| State persistence | Graph state survives phase transitions | Unit test: state serialization/deserialization |
| Branch isolation | No direct commits to main branch | Git hook validation |
| Escalation triggers | Blocking failures escalate correctly | Unit test: escalation condition evaluation |

## E. Known Gaps & Risks

| Gap/Risk | Severity | Mitigation |
|----------|----------|------------|
| No automated rollback on quality gate failure | High | Current approach creates remediation subtasks; auto-revert for critical failures is deferred *(Master Report O-5)* |
| Multi-agent conflict resolution undefined | High | Queue-based serialization planned initially; merge-based concurrency deferred *(Master Report O-4)* |
| Distributed locking absent | Medium | Required for cross-repo agent orchestration; not yet designed *(Research.md §II.7)* |
| Backpressure handling not specified | Medium | Needed when task queue exceeds agent capacity *(Research.md §II.7)* |
| Agent watchdog/deadlock detection missing | Medium | No livelock or deadlock detection in current design *(Research.md §II.5)* |
| Scanner termination strategy undecided | Low | Configurable via config; defaulting to time-bounded *(Master Report O-6)* |
| Trust scoring between agents absent | Low | Future enhancement for multi-agent review *(Research.md §II.5)* |

## F. Decision Log

### Resolved Decisions

| ID | Decision | Rationale |
|----|----------|-----------|
| D-1 | LangGraph for SDLC state machine | Directed graph semantics + built-in state management; existing CLI wrappable *(start_prompt.md §4.4.2)* |
| D-2 | Wrap LangGraph CLI, don't rewrite | Avoids duplicating existing functionality *(start_prompt.md §4.4.2)* |
| D-3 | Three custom Kilo modes + built-in Orchestrator | Minimizes mode proliferation; Orchestrator configured via project rules *(start_prompt.md §4.4.3)* |
| D-7 | Feature branches for all framework work | Isolates experimental changes from main *(start_prompt.md §2.1)* |
| D-9 | Evidence-first completion protocol | Tests/artifacts must exist before marking done; prevents false progress *(Research.md §2.3)* |

### Open Decisions

| ID | Question | Options | Recommendation |
|----|----------|---------|----------------|
| O-4 | Multi-agent conflict resolution | Lock-based, merge-based, queue-based | Start queue-based; add merge support later |
| O-5 | Rollback on quality gate failure | Auto git revert, manual, remediation subtask | Remediation subtask now; auto-revert for critical failures later |
| O-6 | Scanner termination strategy | Time-bounded, resource-bounded, convergence-based | Configurable; default time-bounded |

*Cross-references: See [Master Report §1](./sdlc_framework_master_report.md#1-framework-architecture) for architectural context; [Master Report §4](./sdlc_framework_master_report.md#4-workflow-lifecycle) for lifecycle details.*
