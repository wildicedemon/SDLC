# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.

# Task Architecture Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in task architecture for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Decomposition Patterns

### Hierarchical Task Decomposition

**Name**: Recursive Task Breakdown

**Description**: Break complex tasks into subtasks recursively until atomic units are reached. Each level of decomposition maintains parent-child relationships for traceability and aggregation.

**When to Use**:
- Complex SDLC workflows with multiple phases
- Tasks with natural hierarchical structure (project → feature → task → subtask)
- Systems requiring progress tracking at multiple levels

**Tradeoffs**:
- ✅ Clear structure and traceability
- ✅ Enables parallel execution at leaf levels
- ✅ Natural progress tracking through hierarchy
- ❌ Risk of over-decomposition
- ❌ Coordination overhead increases with depth
- ❌ May lose context at deep levels

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

### Goal-Directed Decomposition

**Name**: Backward Chaining from Objective

**Description**: Start from desired goal state and work backward to identify required preconditions and steps. Each step becomes a subtask until reaching tasks achievable with current capabilities.

**When to Use**:
- Tasks with well-defined end states
- Planning scenarios where outcome is clearer than process
- Systems with goal-state verification

**Tradeoffs**:
- ✅ Clear alignment with objectives
- ✅ Avoids unnecessary steps
- ✅ Natural verification through goal achievement
- ❌ May miss intermediate dependencies
- ❌ Requires clear goal definition
- ❌ Struggles with ambiguous objectives

**Confidence: MEDIUM** - Established in AI planning, limited agent-specific validation.

---

### Capability-Matched Decomposition

**Name**: Agent Capability Alignment

**Description**: Decompose tasks based on available agent capabilities, ensuring each subtask matches an agent's expertise. Avoid creating tasks that no agent can execute.

**When to Use**:
- Heterogeneous agent teams with specialized capabilities
- Systems with well-defined agent skill inventories
- Environments where capability matching is critical

**Tradeoffs**:
- ✅ Utilizes agent strengths
- ✅ Avoids capability mismatches
- ✅ Natural task assignment
- ❌ Limited by available capabilities
- ❌ May require capability discovery
- ❌ Can fragment tasks unnaturally

**Confidence: MEDIUM** - Practitioner-focused, limited formal study.

---

## Graph Patterns

### DAG-Based Task Graph

**Name**: Directed Acyclic Graph Execution

**Description**: Represent tasks as nodes and dependencies as directed edges in an acyclic graph. Execute tasks in topological order, with independent tasks running in parallel.

**When to Use**:
- Workflows with clear dependencies
- Systems requiring parallel execution
- Scenarios where cycle detection is important

**Tradeoffs**:
- ✅ Clear execution order
- ✅ Natural parallelization
- ✅ Cycle detection prevents deadlock
- ❌ Requires upfront dependency analysis
- ❌ Dynamic dependencies require graph updates
- ❌ Large graphs can be complex to manage

**Confidence: HIGH** - Standard pattern in workflow orchestration.

---

### Conditional Task Graph

**Name**: Branching Workflow

**Description**: Extend DAG with conditional edges that determine task execution based on runtime conditions. Enables adaptive workflows that respond to intermediate results.

**When to Use**:
- Workflows with decision points
- Systems requiring adaptive execution
- Scenarios with multiple possible paths

**Tradeoffs**:
- ✅ Adaptive to runtime conditions
- ✅ Reduces unnecessary task execution
- ✅ Enables complex workflow logic
- ❌ More complex to design and debug
- ❌ Harder to predict execution paths
- ❌ Requires condition evaluation logic

**Confidence: HIGH** - Implemented in LangGraph, Temporal [web:3].

---

### Event-Driven Task Graph

**Name**: Reactive Task Execution

**Description**: Tasks are triggered by events rather than explicit dependencies. Events can be task completion, external signals, or state changes.

**When to Use**:
- Systems with unpredictable event timing
- Event-sourced architectures
- Scenarios requiring real-time responsiveness

**Tradeoffs**:
- ✅ Responsive to events
- ✅ Loose coupling between tasks
- ✅ Natural integration with external systems
- ❌ Harder to track execution flow
- ❌ Requires event infrastructure
- ❌ Potential for event storms

**Confidence: MEDIUM** - Established pattern, limited agent-specific implementations.

---

## Atomic Task Patterns

### Single-Responsibility Task

**Name**: Focused Atomic Unit

**Description**: Each task has exactly one responsibility, making it easier to verify, rollback, and retry. Task boundaries align with single, clear objectives.

**When to Use**:
- All task types (foundational pattern)
- Systems requiring fine-grained control
- Environments with high failure rates

**Tradeoffs**:
- ✅ Clear success criteria
- ✅ Easy to verify and rollback
- ✅ Natural retry boundaries
- ❌ May require many tasks for complex operations
- ❌ Coordination overhead between tasks
- ❌ Context passing between tasks

**Confidence: HIGH** - Fundamental software engineering principle.

---

### Self-Contained Task

**Name**: Context-Complete Task

**Description**: Each task includes all necessary context for execution, reducing dependency on external state and enabling independent execution.

**When to Use**:
- Distributed execution environments
- Systems with unreliable connectivity
- Scenarios requiring task portability

**Tradeoffs**:
- ✅ Independent execution
- ✅ Reduced external dependencies
- ✅ Natural for distributed systems
- ❌ Larger task payloads
- ❌ Potential context duplication
- ❌ Context stalency issues

**Confidence: HIGH** - Essential for distributed task execution.

---

### Idempotent Task

**Name**: Repeatable Execution

**Description**: Tasks can be executed multiple times with the same result. Enables safe retries without side effect accumulation.

**When to Use**:
- Systems with retry mechanisms
- Unreliable execution environments
- Scenarios requiring exactly-once semantics

**Tradeoffs**:
- ✅ Safe retries
- ✅ Simplifies error handling
- ✅ Enables at-least-once delivery
- ❌ Requires state checking logic
- ❌ Not all operations can be idempotent
- ❌ May require cleanup logic

**Confidence: HIGH** - Standard distributed systems pattern.

---

## Branch Management Patterns

### Branch-Per-Task Isolation

**Name**: Task-Dedicated Branch

**Description**: Create a dedicated git branch or worktree for each task. Changes are isolated until validated and merged, preventing interference between concurrent tasks.

**When to Use**:
- Parallel agent execution
- Tasks with potential file overlap
- Systems requiring isolation

**Tradeoffs**:
- ✅ 67% reduction in merge conflicts
- ✅ Clear task attribution
- ✅ Easy rollback per task
- ❌ Branch management overhead
- ❌ Merge coordination required
- ❌ May delay integration

**Confidence: HIGH** - Validated in multi-agent coding research [paper:5].

---

### Feature Branch Aggregation

**Name**: Related Task Grouping

**Description**: Group related tasks under a feature branch, with individual tasks as commits or sub-branches. Enables cohesive feature development with integrated testing.

**When to Use**:
- Feature development spanning multiple tasks
- Systems requiring feature-level validation
- Scenarios with related task dependencies

**Tradeoffs**:
- ✅ Cohesive feature delivery
- ✅ Feature-level testing
- ✅ Clear feature attribution
- ❌ Larger merge units
- ❌ Delayed integration feedback
- ❌ Feature branch maintenance

**Confidence: HIGH** - Standard git workflow pattern.

---

### Integration Branch Staging

**Name**: Pre-Merge Validation Branch

**Description**: Use integration branches for pre-merge validation. Tasks merge to integration branch for testing before final merge to main.

**When to Use**:
- Systems with strict quality gates
- Environments requiring comprehensive testing
- Scenarios with high merge risk

**Tradeoffs**:
- ✅ Comprehensive validation before main
- ✅ Catches integration issues early
- ✅ Protects main branch stability
- ❌ Additional merge step
- ❌ Delayed feedback to task authors
- ❌ Integration branch maintenance

**Confidence: HIGH** - Established CI/CD pattern.

---

## Conflict Resolution Patterns

### Semantic Merge with LLM

**Name**: Intelligent Conflict Resolution

**Description**: Use LLM to understand code semantics and generate intelligent merge resolutions. Goes beyond textual three-way merge to understand code meaning.

**When to Use**:
- Code conflicts requiring semantic understanding
- Systems with frequent merge conflicts
- Scenarios where manual resolution is costly

**Tradeoffs**:
- ✅ 78% automatic resolution rate
- ✅ Understands code semantics
- ✅ Reduces human intervention
- ❌ LLM inference cost
- ❌ May produce incorrect resolutions
- ❌ Requires validation

**Confidence: MEDIUM** - Emerging pattern, limited production validation [paper:6].

---

### Agent Negotiation Protocol

**Name**: Multi-Agent Conflict Resolution

**Description**: When conflicts arise, conflicting agents communicate to negotiate resolution. Each agent explains its changes and they jointly determine resolution.

**When to Use**:
- Multi-agent systems with communication capabilities
- Complex conflicts requiring context
- Scenarios where agents have change rationale

**Tradeoffs**:
- ✅ Preserves agent intent
- ✅ Leverages agent knowledge
- ✅ Can resolve complex conflicts
- ❌ Communication overhead
- ❌ Requires negotiation protocol
- ❌ May not reach agreement

**Confidence: LOW** - Research concept, limited implementation.

---

### Last-Writer-Wins with Audit

**Name**: Simple Resolution with Traceability

**Description**: Resolve conflicts by accepting the last modification, but maintain full audit trail for potential rollback or review.

**When to Use**:
- Non-critical changes
- Systems with comprehensive logging
- Scenarios where simplicity outweighs precision

**Tradeoffs**:
- ✅ Simple implementation
- ✅ No blocking on conflicts
- ✅ Full audit trail
- ❌ May lose important changes
- ❌ Requires post-hoc review
- ❌ Not suitable for critical code

**Confidence: MEDIUM** - Simple pattern, limited applicability for critical systems.

---

## Validation Patterns

### Multi-Stage Pipeline

**Name**: Layered Quality Gates

**Description**: Execute validation in stages with increasing cost and precision. Early stages (syntax, linting) are fast and catch common issues; later stages (tests, security) are comprehensive.

**When to Use**:
- All production systems
- Tasks requiring quality assurance
- Environments with CI/CD integration

**Tradeoffs**:
- ✅ Early feedback on common issues
- ✅ Comprehensive validation
- ✅ Cost-effective (fail fast)
- ❌ Pipeline configuration complexity
- ❌ Stage coordination
- ❌ May delay feedback for late stages

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Multi-Agent QA Swarm

**Name**: Parallel Validation Agents

**Description**: Deploy multiple agents with different validation focuses (correctness, security, performance, style). Aggregate findings for comprehensive review.

**When to Use**:
- Quality-critical tasks
- Systems with diverse quality requirements
- Scenarios requiring comprehensive coverage

**Tradeoffs**:
- ✅ 40% higher bug detection
- ✅ Diverse perspective coverage
- ✅ Parallel execution
- ❌ Multiple agent coordination
- ❌ Finding aggregation complexity
- ❌ Potential conflicting recommendations

**Confidence: HIGH** - Validated in research [paper:7].

---

### Incremental Validation

**Name**: Change-Scoped Testing

**Description**: Run only tests affected by task changes, determined through dependency analysis. Reduces validation time for small changes.

**When to Use**:
- Large codebases with extensive test suites
- Systems with fast feedback requirements
- Scenarios with frequent small changes

**Tradeoffs**:
- ✅ Faster validation for small changes
- ✅ Reduced resource consumption
- ✅ Maintains coverage for affected areas
- ❌ Requires dependency analysis
- ❌ May miss indirect effects
- ❌ Complex to implement correctly

**Confidence: MEDIUM** - Established concept, implementation complexity.

---

## Parallelization Patterns

### Task-Level Parallelism

**Name**: Independent Task Execution

**Description**: Execute independent tasks concurrently, coordinating only at dependency boundaries. Maximizes throughput for task graphs with parallel paths.

**When to Use**:
- Task graphs with independent branches
- Systems with available parallel capacity
- Scenarios requiring fast completion

**Tradeoffs**:
- ✅ 2-4x speedup for independent tasks
- ✅ Simple coordination model
- ✅ Natural for DAG execution
- ❌ Requires dependency analysis
- ❌ Resource contention possible
- ❌ Coordination at merge points

**Confidence: HIGH** - Standard parallel execution pattern.

---

### Pipeline Parallelism

**Name**: Stage Overlap Execution

**Description**: Different tasks execute in different pipeline stages simultaneously. While task A is in testing, task B can be in implementation.

**When to Use**:
- Continuous workflows with multiple stages
- Systems with stage isolation
- Scenarios with steady task flow

**Tradeoffs**:
- ✅ 1.5-3x throughput improvement
- ✅ Continuous resource utilization
- ✅ Natural for CI/CD
- ❌ Stage coordination complexity
- ❌ Buffering between stages
- ❌ Backpressure handling needed

**Confidence: HIGH** - Standard pipeline pattern.

---

### Agent Parallelism

**Name**: Multi-Agent Concurrent Execution

**Description**: Multiple agents work on different tasks simultaneously, each with isolated context and resources.

**When to Use**:
- Multi-agent systems
- Tasks without dependencies
- Scenarios requiring diverse expertise

**Tradeoffs**:
- ✅ 2-5x speedup with multiple agents
- ✅ Utilizes diverse capabilities
- ✅ Fault isolation between agents
- ❌ Agent coordination overhead
- ❌ Resource contention
- ❌ Result aggregation complexity

**Confidence: HIGH** - Validated in multi-agent research.

---

## Anti-Patterns

### Over-Decomposition

**Name**: Excessive Task Fragmentation

**Description**: Breaking tasks into too many small units, creating coordination overhead that exceeds execution time.

**Failure Mode**:
- Coordination dominates execution time
- Context lost between tasks
- Increased failure points
- Difficult to maintain overall view

**Remediation**: Balance granularity with coordination cost; use appropriate decomposition depth.

**Confidence: HIGH** - Common failure mode in practice.

---

### Under-Specified Tasks

**Name**: Vague Task Definition

**Description**: Tasks lack clear objectives, success criteria, or context, leading to unpredictable execution and verification challenges.

**Failure Mode**:
- Agents interpret tasks differently
- Success cannot be verified
- Scope creep during execution
- Inconsistent results across runs

**Remediation**: Use structured task specifications with explicit objectives, constraints, and success criteria.

**Confidence: HIGH** - Common failure mode, addressed by clarification prompts [seed:Kilo-ask].

---

### Circular Dependencies

**Name**: Task Graph Cycles

**Description**: Task dependencies form cycles, preventing any valid execution order and causing deadlock.

**Failure Mode**:
- No valid execution order exists
- Tasks wait indefinitely
- System hangs or fails
- Difficult to detect in large graphs

**Remediation**: Implement cycle detection during graph construction; break cycles by removing or reversing dependencies.

**Confidence: HIGH** - Well-understood graph theory issue.

---

### Shared Mutable State

**Name**: Concurrent Modification Without Isolation

**Description**: Multiple tasks or agents modify shared state without proper isolation, leading to race conditions and inconsistent results.

**Failure Mode**:
- Race conditions
- Lost updates
- Inconsistent state
- Difficult to reproduce bugs

**Remediation**: Use branch-per-task isolation, locking mechanisms, or immutable data structures.

**Confidence: HIGH** - Standard concurrency anti-pattern.

---

### Validation Bypass

**Name**: Skipping Quality Gates

**Description**: Tasks bypass validation stages for speed, introducing defects into the codebase.

**Failure Mode**:
- Defects reach main branch
- Technical debt accumulation
- Reduced code quality over time
- Difficult to retroactively validate

**Remediation**: Enforce mandatory validation gates; make bypass explicit with justification.

**Confidence: HIGH** - Common pressure in fast-paced environments.

---

### Monolithic Task

**Name**: Undifferentiated Large Task

**Description**: Creating tasks that are too large to execute reliably, verify, or rollback.

**Failure Mode**:
- Partial completion on failure
- Difficult to verify correctness
- Large rollback impact
- Blocks parallel execution

**Remediation**: Decompose into smaller atomic tasks with clear boundaries.

**Confidence: HIGH** - Fundamental anti-pattern.

---

## Use-Case Patterns

### Feature Development Workflow

**Pattern**: Hierarchical Decomposition with Branch-Per-Task

**Description**: Decompose feature into tasks, create feature branch, spawn task branches for parallel agent work, validate incrementally, merge to feature branch for integration testing.

**Implementation Notes**:
- Use hierarchical decomposition for feature breakdown
- Implement branch-per-task for isolation
- Use multi-stage validation pipeline
- Aggregate commits with conventional commit messages

**Confidence: HIGH** - Standard feature development pattern.

---

### Bug Fix Workflow

**Pattern**: Goal-Directed Decomposition with Rapid Validation

**Description**: Start from bug description, identify fix location, implement minimal fix, validate with focused tests, merge quickly.

**Implementation Notes**:
- Use goal-directed decomposition for focused fix
- Implement incremental validation for affected tests
- Use semantic merge if conflicts arise
- Fast-track through validation pipeline

**Confidence: HIGH** - Standard bug fix pattern.

---

### Refactoring Workflow

**Pattern**: Atomic Tasks with Multi-Agent QA

**Description**: Break refactoring into atomic, behavior-preserving tasks. Use multi-agent QA swarm to verify behavior preservation.

**Implementation Notes**:
- Use atomic task pattern for incremental changes
- Implement multi-agent QA for comprehensive validation
- Use branch-per-task for isolation
- Validate behavior preservation at each step

**Confidence: MEDIUM** - Requires careful behavior verification.

---

## Summary

The patterns identified reveal key principles:

1. **Decomposition is essential but requires balance** - Over and under-decomposition both fail
2. **DAG-based graphs provide structure** - Clear dependencies enable parallelization
3. **Isolation prevents conflicts** - Branch-per-task dramatically reduces merge issues
4. **Validation must be comprehensive** - Multi-stage, multi-agent approaches catch more issues
5. **Parallelization requires coordination** - Task-level, pipeline, and agent parallelism each have tradeoffs
6. **Atomic tasks are foundational** - Single responsibility, self-contained, idempotent

**Confidence levels vary by pattern maturity** - Core patterns (DAG, atomic tasks, validation) HIGH confidence; emerging patterns (semantic merge, agent negotiation) MEDIUM to LOW.
