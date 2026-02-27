# Agent System Design Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in agent system design for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Architectural Patterns

### System-Theoretic Decomposition

**Name**: System-Theoretic Agent Decomposition

**Description**: Decompose agent systems into five distinct subsystems: Reasoning, Perception, Action, Learning, and Communication. Each subsystem has explicit interfaces and can be developed, tested, and scaled independently.

**When to Use**:
- Large-scale agent deployments requiring modularity
- Systems with diverse capability requirements
- Environments where subsystems may be distributed across machines

**Tradeoffs**:
- ✅ Improved testability and maintainability
- ✅ Enables independent scaling of subsystems
- ✅ Clear boundaries for debugging and monitoring
- ❌ Integration complexity between subsystems
- ❌ Potential latency from inter-subsystem communication
- ❌ Overhead for simple agent systems

**Confidence: HIGH** - Based on established multi-agent systems theory [paper:3].

---

### Hierarchical Orchestration

**Name**: Hierarchical Multi-Agent Orchestration

**Description**: Organize agents in a tree structure with a planner/manager agent at the root decomposing tasks for specialist sub-agents at lower levels. Results aggregate upward with validation at each level.

**When to Use**:
- Complex tasks requiring multiple expertise areas
- Workflows with natural decomposition (e.g., SDLC phases)
- Systems needing progress tracking and checkpointing

**Tradeoffs**:
- ✅ Clear responsibility boundaries
- ✅ Natural progress tracking through hierarchy levels
- ✅ Enables parallel execution of independent subtasks
- ❌ Single point of failure at planner level
- ❌ Communication overhead increases with depth
- ❌ May over-decompose simple tasks

**Confidence: HIGH** - Validated in MetaGPT, ChatDev, AgentOrchestra [paper:1][paper:2][web:6].

---

### TEA Protocol Pattern

**Name**: Task-Environment-Agent Protocol

**Description**: Explicitly model three components: Task (what to accomplish), Environment (context and constraints), Agent (capabilities and state). Define clear interfaces between these components for interoperability.

**When to Use**:
- Multi-framework agent deployments
- Systems requiring agent portability across environments
- Standardized tool integration via MCP

**Tradeoffs**:
- ✅ Framework interoperability
- ✅ Clear separation of concerns
- ✅ Enables agent reuse across tasks
- ❌ Abstraction overhead
- ❌ May limit optimization opportunities
- ❌ Requires protocol compliance testing

**Confidence: MEDIUM** - Emerging pattern from AgentOrchestra [web:6].

---

### Mixture-of-Agents (MoA)

**Name**: Layered Voting Architecture

**Description**: Arrange multiple agents in layers where each layer receives outputs from the previous layer and produces refined outputs. Final layer aggregates through voting or weighted combination.

**When to Use**:
- Quality-critical tasks requiring high confidence
- Scenarios with diverse valid approaches
- Systems tolerant of compute overhead

**Tradeoffs**:
- ✅ 8-12% improvement over single-agent baselines
- ✅ Reduces impact of individual agent failures
- ✅ Captures diverse perspectives
- ❌ 3-5x compute overhead
- ❌ Increased latency
- ❌ May average out creative solutions

**Confidence: HIGH** - Empirically validated in benchmarks [web:7].

---

### Role-Based Specialization

**Name**: Software Company Simulation

**Description**: Define explicit roles (e.g., CEO, Architect, Engineer, QA) with specific responsibilities, expertise, and communication patterns. Agents role-play within defined boundaries.

**When to Use**:
- End-to-end software development tasks
- Scenarios mirroring human team structures
- Systems requiring clear handoff protocols

**Tradeoffs**:
- ✅ Clear responsibility assignment
- ✅ Mirrors proven human workflows
- ✅ Natural quality gates between roles
- ❌ Communication overhead between roles
- ❌ May miss cross-role optimizations
- ❌ Role boundary rigidity

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

## Operational Patterns

### Mode-Based Operation

**Name**: Explicit Mode Switching

**Description**: Define discrete operational modes (e.g., Code, Debug, Architect, Review) with distinct tool access, reasoning patterns, and output constraints. Switch modes explicitly based on task requirements.

**When to Use**:
- Multi-phase workflows with different requirements
- Systems serving diverse user intents
- Environments requiring clear state boundaries

**Tradeoffs**:
- ✅ 34% reduction in task drift
- ✅ Clear user expectations per mode
- ✅ Enables mode-specific optimization
- ❌ Context reloading latency on switch
- ❌ May require manual mode selection
- ❌ Mode boundary ambiguity for edge cases

**Confidence: HIGH** - Implemented in Kilo, Cline [seed:Kilo][web:2].

---

### Checkpoint-Based Execution

**Name**: Human-in-the-Loop Checkpoints

**Description**: Insert explicit checkpoints in agent workflows where execution pauses for human review, approval, or clarification. Checkpoints can be automatic (at phase boundaries) or triggered by confidence thresholds.

**When to Use**:
- High-stakes or irreversible operations
- Tasks with ambiguous requirements
- Systems building user trust

**Tradeoffs**:
- ✅ Prevents runaway execution
- ✅ Enables course correction
- ✅ Builds user trust through transparency
- ❌ Interrupts workflow flow
- ❌ Requires user availability
- ❌ May over-checkpoint simple tasks

**Confidence: HIGH** - Implemented in Cline, Kilo ask_followup_question [seed:Kilo-ask][web:2].

---

### Conditional Multi-Stage Recovery

**Name**: Zero-Shot Recovery Chaining

**Description**: On failure, chain through diagnosis → planning → recovery stages using zero-shot prompting. Each stage produces outputs consumed by the next, enabling adaptive recovery without pre-programmed strategies.

**When to Use**:
- Systems with diverse failure modes
- Environments where failures are costly
- Agents operating autonomously for extended periods

**Tradeoffs**:
- ✅ 19% higher success rate on TfD benchmarks
- ✅ Adaptive to novel failure modes
- ✅ No pre-programmed recovery logic needed
- ❌ Prompt brittleness
- ❌ Token overhead for multi-stage prompting
- ❌ May cascade failures if diagnosis is wrong

**Confidence: HIGH** - Empirically validated [paper:5].

---

### Stigmergic Coordination

**Name**: Environment-Mediated Communication

**Description**: Agents communicate indirectly through modifications to a shared environment (e.g., codebase, task queue, blackboard) rather than direct messages. Coordination emerges from environmental signals.

**When to Use**:
- Large agent swarms where direct communication doesn't scale
- Systems with shared work artifacts
- Environments requiring loose coupling

**Tradeoffs**:
- ✅ Scales to large agent counts
- ✅ No central coordinator bottleneck
- ✅ Robust to individual agent failures
- ❌ Emergent behavior unpredictability
- ❌ Difficult to debug coordination
- ❌ Potential for conflicting modifications

**Confidence: MEDIUM** - Biological inspiration, limited production validation.

---

## Integration Patterns

### MCP Tool Integration

**Name**: Model Context Protocol Standardization

**Description**: Use MCP for tool definitions, enabling standardized discovery, invocation, and validation. Tools are defined with JSON Schema for type safety.

**When to Use**:
- Multi-model agent systems
- Environments requiring tool portability
- Systems with evolving tool ecosystems

**Tradeoffs**:
- ✅ Standardization reduces integration effort
- ✅ Type safety through JSON Schema
- ✅ Growing ecosystem of MCP servers
- ❌ Limits tool expressiveness to protocol capabilities
- ❌ Protocol versioning challenges
- ❌ Overhead for simple tool integrations

**Confidence: HIGH** - Industry adoption accelerating [seed:Augment-MCP].

---

### Repo Grokking Integration

**Name**: Semantic Codebase Understanding

**Description**: Maintain a semantic model of the codebase through continuous analysis, enabling agents to query code relationships, dependencies, and patterns without full context loading.

**When to Use**:
- Large codebases exceeding context windows
- Tasks requiring cross-file understanding
- Systems needing consistent codebase awareness

**Tradeoffs**:
- ✅ Enables large codebase navigation
- ✅ Reduces context window pressure
- ✅ Provides consistent codebase model
- ❌ Compute overhead for semantic analysis
- ❌ Model stalency between updates
- ❌ May miss recent changes

**Confidence: MEDIUM** - Zencoder implementation, limited independent validation [seed:Zencoder].

---

## Monitoring Patterns

### Watchdog Monitoring

**Name**: Agent Health Surveillance

**Description**: Implement heartbeat monitoring, progress tracking, and anomaly detection for agent systems. Automatic intervention triggers when health metrics degrade.

**When to Use**:
- Production agent deployments
- Long-running autonomous tasks
- Systems requiring reliability guarantees

**Tradeoffs**:
- ✅ Early failure detection
- ✅ Enables automatic intervention
- ✅ Provides observability for debugging
- ❌ Monitoring infrastructure overhead
- ❌ False positive interventions
- ❌ May not detect subtle failures (livelock)

**Confidence: HIGH** - Established distributed systems pattern [web:8].

---

### Adversarial Review

**Name**: Critic-Based Quality Assurance

**Description**: Deploy dedicated critic agents to challenge, review, and validate outputs from worker agents. Critics have different objectives and success criteria.

**When to Use**:
- Quality-critical outputs (security, correctness)
- Systems with high cost of failure
- Scenarios benefiting from diverse perspectives

**Tradeoffs**:
- ✅ 40% higher bug detection rate
- ✅ Catches edge cases and assumptions
- ✅ Provides quality signal for trust scoring
- ❌ Additional agent overhead
- ❌ May slow iteration cycles
- ❌ Critic calibration challenges

**Confidence: HIGH** - Validated in code review research [paper:6].

---

## Anti-Patterns

### Monolithic FM-Centric Design

**Name**: Foundation Model Without Structure

**Description**: Relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration. The model handles all reasoning, planning, and execution implicitly.

**Failure Mode**:
- World modeling failures when context exceeds training
- No introspection or explainability
- Difficult to debug or improve specific capabilities
- Unpredictable behavior on edge cases

**Remediation**: Implement system-theoretic decomposition with explicit subsystems.

**Confidence: HIGH** - Well-documented failure mode [paper:3].

---

### Tight Vendor Coupling

**Name**: SDK Lock-In

**Description**: Building agent systems tightly coupled to a specific vendor's SDK, model, or API without abstraction layers.

**Failure Mode**:
- Migration costs when changing providers
- Vulnerability to vendor pricing/availability changes
- Limited to vendor's capability roadmap
- Difficulty incorporating multi-model approaches

**Remediation**: Use protocol abstractions (MCP) and vendor-agnostic interfaces.

**Confidence: HIGH** - Common practitioner complaint [community:1].

---

### Silent State Drift

**Name**: Unmonitored Context Corruption

**Description**: Allowing agent state to drift without validation, leading to corrupted beliefs, stale context, or poisoned reasoning chains.

**Failure Mode**:
- Cascading errors from invalid assumptions
- Context poisoning from malicious/low-quality inputs
- Difficulty attributing failures to specific state changes
- Unpredictable behavior after extended operation

**Remediation**: Implement state validation, context sanitization, and lineage tracking.

**Confidence: HIGH** - Documented in Roocode context poisoning [seed:Roocode].

---

### Over-Delegation

**Name**: Excessive Task Decomposition

**Description**: Decomposing tasks too finely, creating excessive coordination overhead and losing task coherence.

**Failure Mode**:
- Communication overhead dominates execution time
- Lost context between subtask handoffs
- Difficulty maintaining coherent overall strategy
- Increased failure points

**Remediation**: Balance decomposition granularity with coordination cost.

**Confidence: MEDIUM** - Observed in hierarchical systems, limited formal study.

---

### Under-Specified Intent

**Name**: Ambiguous Task Definition

**Description**: Providing agents with vague or incomplete task specifications, expecting them to infer missing details.

**Failure Mode**:
- Agents pursue incorrect interpretations
- Scope creep as agents add assumptions
- Inconsistent results across runs
- User frustration from unexpected outputs

**Remediation**: Use structured task specifications with explicit constraints; implement clarification prompts.

**Confidence: HIGH** - Common failure mode, addressed by Kilo ask_followup_question [seed:Kilo-ask].

---

### Retry Without Adaptation

**Name**: Identical Retry Loop

**Description**: Retrying failed operations with identical parameters, expecting different results without adaptation.

**Failure Mode**:
- Infinite retry loops
- Resource waste on unrecoverable failures
- Masking underlying issues
- Eventual timeout without resolution

**Remediation**: Implement adaptive retry with parameter variation or alternative approaches.

**Confidence: HIGH** - Basic engineering anti-pattern, common in simple agent implementations.

---

### Centralized Bottleneck

**Name**: Single Coordinator Overload

**Description**: Routing all agent coordination through a single central agent or service, creating a bottleneck.

**Failure Mode**:
- Scalability limits as agent count grows
- Single point of failure
- Increased latency for coordination
- Coordinator overload leading to failures

**Remediation**: Implement distributed coordination or hierarchical delegation.

**Confidence: HIGH** - Established distributed systems anti-pattern.

---

### Ignoring Livelock

**Name**: Activity Without Progress

**Description**: Monitoring agent activity (heartbeats, tool calls) without verifying actual progress toward task completion.

**Failure Mode**:
- Agents appear healthy but make no progress
- Resource consumption without value
- Difficult to detect without progress metrics
- May continue indefinitely

**Remediation**: Implement progress metrics and thresholds, not just activity monitoring.

**Confidence: MEDIUM** - Under-discussed in agent literature, observed in practitioner reports.

---

## Use-Case Patterns

### CI/CD Pipeline Integration

**Pattern**: CLI Agent Swarm for Continuous Integration

**Description**: Deploy multiple CLI agents (Kilo, Cline) in CI/CD pipelines for parallel code review, testing, and deployment tasks.

**Implementation Notes**:
- Use mode-based operation for task-specific behavior
- Implement checkpoint-based execution for human gates
- Monitor with watchdog pattern for pipeline reliability

**Confidence: HIGH** - Production deployments exist.

---

### Multi-File Refactoring

**Pattern**: IDE Agent with MCP Tools

**Description**: Use IDE-integrated agents (VS Code Agent Mode, Augment) with MCP tools for semantic codebase understanding during large-scale refactoring.

**Implementation Notes**:
- Leverage repo grokking for cross-file awareness
- Use hierarchical orchestration for complex refactorings
- Implement adversarial review for quality assurance

**Confidence: HIGH** - Common use case for IDE agents.

---

### Autonomous Bug Fixing

**Pattern**: Hierarchical Diagnosis and Repair

**Description**: Deploy planner agent for bug diagnosis, specialist agents for fix proposals, and critic agents for validation.

**Implementation Notes**:
- Use conditional multi-stage recovery for novel bugs
- Implement voting for fix selection
- Use checkpoint-based execution for human approval

**Confidence: MEDIUM** - Research prototypes exist, production validation limited.

---

### Code Review Automation

**Pattern**: Adversarial Review Swarm

**Description**: Deploy multiple reviewer agents with different focus areas (security, performance, style) and aggregate findings.

**Implementation Notes**:
- Use MoA pattern for comprehensive coverage
- Implement trust scoring for reviewer weighting
- Use clarification prompts for ambiguous issues

**Confidence: HIGH** - Validated in research, production implementations exist.

---

## Additional Patterns: Modes, Skills, and Workflows

*Source: Kimi-Research analysis (Modes, Skills, Workflows)*

### Progressive Disclosure Skill Architecture

**Description**: Three-level skill architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

| Level | Content | Token Estimate | Purpose |
|-------|---------|----------------|---------|
| **Level 1: Identity** | Name, description, triggers | ~100 tokens | Skill selection |
| **Level 2: Instructions** | Procedural knowledge, examples | ~1,000 tokens | Task execution |
| **Level 3: Resources** | Scripts, templates, references | Unbounded | Deep expertise |

**When to Use**:
- Large skill libraries with diverse capabilities
- Context-constrained environments
- Systems requiring dynamic skill loading

**Tradeoffs**:
- ✅ Minimizes context window usage
- ✅ Enables deep expertise access
- ❌ Multi-stage loading adds latency

---

### Mode-Specific Tool Access

**Description**: Different agent modes activate different tool sets, reducing context window usage and improving tool selection accuracy.

| Mode | Primary Use | Autonomy Level | Human Oversight |
|------|-------------|----------------|-----------------|
| **Code** | Implementation | Medium | Review required |
| **Ask** | Explanation | Low | Minimal |
| **Architect** | Design | High | Approval gates |
| **Debug** | Troubleshooting | Medium | Confirmation |
| **Orchestrator** | Coordination | Very High | Exception handling |

**When to Use**:
- Multi-purpose agent systems
- Tasks with varying risk profiles
- Systems requiring different expertise levels

---

### Skill Composition Pattern

**Description**: Complex tasks invoke multiple skills sequentially, with skills able to reference other skills for reusable capability building blocks.

**Skill Execution Lifecycle**:
1. **Trigger Detection**: User request matches skill description
2. **Context Injection**: Skill instructions loaded as hidden message
3. **Permission Activation**: Pre-approved tools enabled
4. **Execution**: Agent completes task with enriched context
5. **Cleanup**: Skill context removed

**When to Use**:
- Complex multi-step tasks
- Workflows requiring multiple expertise areas
- Systems with reusable capability components

---

### Workflow Templating Pattern

**Description**: Common workflows defined as reusable templates with explicit step sequencing and variables.

**When to Use**:
- Repeated task patterns
- Team standardization requirements
- Audit trail requirements

**Tradeoffs**:
- ✅ Reproducible execution
- ✅ Clear audit trail
- ❌ Reduced flexibility
- ❌ Template maintenance overhead

---

## Architecture Anti-Patterns

*Source: Kimi-Research analysis*

### Anti-Pattern: God Agent

**Description**: A single agent tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Remediation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Confidence: HIGH** - Common anti-pattern in early agent implementations.

---

### Anti-Pattern: Chatty Agent Communication

**Description**: Agents communicate excessively, causing latency and cost explosion.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Remediation**: Batch communications and use shared state instead of per-step confirmations.

**Confidence: HIGH** - Observed in production multi-agent systems.

---

### Anti-Pattern: Big Bang Deployment

**Description**: Deploying AI systems all at once without gradual rollout.

**Failure Mode**:
- Production failures affect all users
- Difficult to rollback quickly
- No learning opportunity
- High risk

**Remediation**: Gradual rollout with canary deployments and automatic rollback.

**Confidence: HIGH** - Standard DevOps anti-pattern applied to AI systems.

---

## Agent Design Anti-Patterns

*Source: Kimi-Research analysis*

### Anti-Pattern: Prompt Injection Vulnerability

**Description**: Agents execute user input without sanitization.

**Failure Mode**:
- Arbitrary code execution
- Data exfiltration
- System compromise

**Remediation**: Input validation and sandboxing of all user-provided content.

**Confidence: HIGH** - Critical security vulnerability.

---

### Anti-Pattern: Hallucination Acceptance

**Description**: Blindly accepting AI-generated output without verification.

**Failure Mode**:
- Production bugs
- Security vulnerabilities
- Incorrect functionality

**Remediation**: Multi-layer verification including syntax check, test execution, and static analysis.

**Confidence: HIGH** - Common failure mode in production AI systems.

---

### Anti-Pattern: Temperature Ignorance

**Description**: Using wrong temperature for task type.

**Failure Mode**:
- Inconsistent code generation
- Hallucinated facts
- Poor task performance

**Remediation**: Task-appropriate temperature settings (0.1 for code, 0.0 for factual Q&A, 0.7 for creative tasks).

**Confidence: HIGH** - Well-documented model behavior.

---

## Summary

The patterns identified reveal a maturing field with clear best practices emerging:

1. **Decomposition is essential** - Monolithic agents fail; system-theoretic decomposition succeeds
2. **Hierarchy provides structure** - Hierarchical orchestration balances complexity with coordination
3. **Human-in-the-loop remains critical** - Checkpoints and clarification prevent runaway execution
4. **Monitoring must include progress** - Activity monitoring alone misses livelock
5. **Standardization accelerates** - MCP and similar protocols reduce integration overhead
6. **Adversarial approaches improve quality** - Critic agents catch what single agents miss

**Confidence levels vary by pattern maturity** - Architectural patterns generally HIGH confidence, operational patterns MEDIUM to HIGH, and emerging patterns (stigmergic coordination) MEDIUM to LOW.

# Agent System Design Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in agent system design for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Architectural Patterns

### System-Theoretic Decomposition

**Name**: System-Theoretic Agent Decomposition

**Description**: Decompose agent systems into five distinct subsystems: Reasoning, Perception, Action, Learning, and Communication. Each subsystem has explicit interfaces and can be developed, tested, and scaled independently.

**When to Use**:
- Large-scale agent deployments requiring modularity
- Systems with diverse capability requirements
- Environments where subsystems may be distributed across machines

**Tradeoffs**:
- ✅ Improved testability and maintainability
- ✅ Enables independent scaling of subsystems
- ✅ Clear boundaries for debugging and monitoring
- ❌ Integration complexity between subsystems
- ❌ Potential latency from inter-subsystem communication
- ❌ Overhead for simple agent systems

**Confidence: HIGH** - Based on established multi-agent systems theory [paper:3].

---

### Hierarchical Orchestration

**Name**: Hierarchical Multi-Agent Orchestration

**Description**: Organize agents in a tree structure with a planner/manager agent at the root decomposing tasks for specialist sub-agents at lower levels. Results aggregate upward with validation at each level.

**When to Use**:
- Complex tasks requiring multiple expertise areas
- Workflows with natural decomposition (e.g., SDLC phases)
- Systems needing progress tracking and checkpointing

**Tradeoffs**:
- ✅ Clear responsibility boundaries
- ✅ Natural progress tracking through hierarchy levels
- ✅ Enables parallel execution of independent subtasks
- ❌ Single point of failure at planner level
- ❌ Communication overhead increases with depth
- ❌ May over-decompose simple tasks

**Confidence: HIGH** - Validated in MetaGPT, ChatDev, AgentOrchestra [paper:1][paper:2][web:6].

---

### TEA Protocol Pattern

**Name**: Task-Environment-Agent Protocol

**Description**: Explicitly model three components: Task (what to accomplish), Environment (context and constraints), Agent (capabilities and state). Define clear interfaces between these components for interoperability.

**When to Use**:
- Multi-framework agent deployments
- Systems requiring agent portability across environments
- Standardized tool integration via MCP

**Tradeoffs**:
- ✅ Framework interoperability
- ✅ Clear separation of concerns
- ✅ Enables agent reuse across tasks
- ❌ Abstraction overhead
- ❌ May limit optimization opportunities
- ❌ Requires protocol compliance testing

**Confidence: MEDIUM** - Emerging pattern from AgentOrchestra [web:6].

---

### Mixture-of-Agents (MoA)

**Name**: Layered Voting Architecture

**Description**: Arrange multiple agents in layers where each layer receives outputs from the previous layer and produces refined outputs. Final layer aggregates through voting or weighted combination.

**When to Use**:
- Quality-critical tasks requiring high confidence
- Scenarios with diverse valid approaches
- Systems tolerant of compute overhead

**Tradeoffs**:
- ✅ 8-12% improvement over single-agent baselines
- ✅ Reduces impact of individual agent failures
- ✅ Captures diverse perspectives
- ❌ 3-5x compute overhead
- ❌ Increased latency
- ❌ May average out creative solutions

**Confidence: HIGH** - Empirically validated in benchmarks [web:7].

---

### Role-Based Specialization

**Name**: Software Company Simulation

**Description**: Define explicit roles (e.g., CEO, Architect, Engineer, QA) with specific responsibilities, expertise, and communication patterns. Agents role-play within defined boundaries.

**When to Use**:
- End-to-end software development tasks
- Scenarios mirroring human team structures
- Systems requiring clear handoff protocols

**Tradeoffs**:
- ✅ Clear responsibility assignment
- ✅ Mirrors proven human workflows
- ✅ Natural quality gates between roles
- ❌ Communication overhead between roles
- ❌ May miss cross-role optimizations
- ❌ Role boundary rigidity

**Confidence: HIGH** - Validated in ChatDev, MetaGPT [paper:1][paper:2].

---

## Operational Patterns

### Mode-Based Operation

**Name**: Explicit Mode Switching

**Description**: Define discrete operational modes (e.g., Code, Debug, Architect, Review) with distinct tool access, reasoning patterns, and output constraints. Switch modes explicitly based on task requirements.

**When to Use**:
- Multi-phase workflows with different requirements
- Systems serving diverse user intents
- Environments requiring clear state boundaries

**Tradeoffs**:
- ✅ 34% reduction in task drift
- ✅ Clear user expectations per mode
- ✅ Enables mode-specific optimization
- ❌ Context reloading latency on switch
- ❌ May require manual mode selection
- ❌ Mode boundary ambiguity for edge cases

**Confidence: HIGH** - Implemented in Kilo, Cline [seed:Kilo][web:2].

---

### Checkpoint-Based Execution

**Name**: Human-in-the-Loop Checkpoints

**Description**: Insert explicit checkpoints in agent workflows where execution pauses for human review, approval, or clarification. Checkpoints can be automatic (at phase boundaries) or triggered by confidence thresholds.

**When to Use**:
- High-stakes or irreversible operations
- Tasks with ambiguous requirements
- Systems building user trust

**Tradeoffs**:
- ✅ Prevents runaway execution
- ✅ Enables course correction
- ✅ Builds user trust through transparency
- ❌ Interrupts workflow flow
- ❌ Requires user availability
- ❌ May over-checkpoint simple tasks

**Confidence: HIGH** - Implemented in Cline, Kilo ask_followup_question [seed:Kilo-ask][web:2].

---

### Conditional Multi-Stage Recovery

**Name**: Zero-Shot Recovery Chaining

**Description**: On failure, chain through diagnosis → planning → recovery stages using zero-shot prompting. Each stage produces outputs consumed by the next, enabling adaptive recovery without pre-programmed strategies.

**When to Use**:
- Systems with diverse failure modes
- Environments where failures are costly
- Agents operating autonomously for extended periods

**Tradeoffs**:
- ✅ 19% higher success rate on TfD benchmarks
- ✅ Adaptive to novel failure modes
- ✅ No pre-programmed recovery logic needed
- ❌ Prompt brittleness
- ❌ Token overhead for multi-stage prompting
- ❌ May cascade failures if diagnosis is wrong

**Confidence: HIGH** - Empirically validated [paper:5].

---

### Stigmergic Coordination

**Name**: Environment-Mediated Communication

**Description**: Agents communicate indirectly through modifications to a shared environment (e.g., codebase, task queue, blackboard) rather than direct messages. Coordination emerges from environmental signals.

**When to Use**:
- Large agent swarms where direct communication doesn't scale
- Systems with shared work artifacts
- Environments requiring loose coupling

**Tradeoffs**:
- ✅ Scales to large agent counts
- ✅ No central coordinator bottleneck
- ✅ Robust to individual agent failures
- ❌ Emergent behavior unpredictability
- ❌ Difficult to debug coordination
- ❌ Potential for conflicting modifications

**Confidence: MEDIUM** - Biological inspiration, limited production validation.

---

## Integration Patterns

### MCP Tool Integration

**Name**: Model Context Protocol Standardization

**Description**: Use MCP for tool definitions, enabling standardized discovery, invocation, and validation. Tools are defined with JSON Schema for type safety.

**When to Use**:
- Multi-model agent systems
- Environments requiring tool portability
- Systems with evolving tool ecosystems

**Tradeoffs**:
- ✅ Standardization reduces integration effort
- ✅ Type safety through JSON Schema
- ✅ Growing ecosystem of MCP servers
- ❌ Limits tool expressiveness to protocol capabilities
- ❌ Protocol versioning challenges
- ❌ Overhead for simple tool integrations

**Confidence: HIGH** - Industry adoption accelerating [seed:Augment-MCP].

---

### Repo Grokking Integration

**Name**: Semantic Codebase Understanding

**Description**: Maintain a semantic model of the codebase through continuous analysis, enabling agents to query code relationships, dependencies, and patterns without full context loading.

**When to Use**:
- Large codebases exceeding context windows
- Tasks requiring cross-file understanding
- Systems needing consistent codebase awareness

**Tradeoffs**:
- ✅ Enables large codebase navigation
- ✅ Reduces context window pressure
- ✅ Provides consistent codebase model
- ❌ Compute overhead for semantic analysis
- ❌ Model stalency between updates
- ❌ May miss recent changes

**Confidence: MEDIUM** - Zencoder implementation, limited independent validation [seed:Zencoder].

---

## Monitoring Patterns

### Watchdog Monitoring

**Name**: Agent Health Surveillance

**Description**: Implement heartbeat monitoring, progress tracking, and anomaly detection for agent systems. Automatic intervention triggers when health metrics degrade.

**When to Use**:
- Production agent deployments
- Long-running autonomous tasks
- Systems requiring reliability guarantees

**Tradeoffs**:
- ✅ Early failure detection
- ✅ Enables automatic intervention
- ✅ Provides observability for debugging
- ❌ Monitoring infrastructure overhead
- ❌ False positive interventions
- ❌ May not detect subtle failures (livelock)

**Confidence: HIGH** - Established distributed systems pattern [web:8].

---

### Adversarial Review

**Name**: Critic-Based Quality Assurance

**Description**: Deploy dedicated critic agents to challenge, review, and validate outputs from worker agents. Critics have different objectives and success criteria.

**When to Use**:
- Quality-critical outputs (security, correctness)
- Systems with high cost of failure
- Scenarios benefiting from diverse perspectives

**Tradeoffs**:
- ✅ 40% higher bug detection rate
- ✅ Catches edge cases and assumptions
- ✅ Provides quality signal for trust scoring
- ❌ Additional agent overhead
- ❌ May slow iteration cycles
- ❌ Critic calibration challenges

**Confidence: HIGH** - Validated in code review research [paper:6].

---

## Anti-Patterns

### Monolithic FM-Centric Design

**Name**: Foundation Model Without Structure

**Description**: Relying solely on a foundation model's capabilities without explicit subsystems, state management, or tool integration. The model handles all reasoning, planning, and execution implicitly.

**Failure Mode**:
- World modeling failures when context exceeds training
- No introspection or explainability
- Difficult to debug or improve specific capabilities
- Unpredictable behavior on edge cases

**Remediation**: Implement system-theoretic decomposition with explicit subsystems.

**Confidence: HIGH** - Well-documented failure mode [paper:3].

---

### Tight Vendor Coupling

**Name**: SDK Lock-In

**Description**: Building agent systems tightly coupled to a specific vendor's SDK, model, or API without abstraction layers.

**Failure Mode**:
- Migration costs when changing providers
- Vulnerability to vendor pricing/availability changes
- Limited to vendor's capability roadmap
- Difficulty incorporating multi-model approaches

**Remediation**: Use protocol abstractions (MCP) and vendor-agnostic interfaces.

**Confidence: HIGH** - Common practitioner complaint [community:1].

---

### Silent State Drift

**Name**: Unmonitored Context Corruption

**Description**: Allowing agent state to drift without validation, leading to corrupted beliefs, stale context, or poisoned reasoning chains.

**Failure Mode**:
- Cascading errors from invalid assumptions
- Context poisoning from malicious/low-quality inputs
- Difficulty attributing failures to specific state changes
- Unpredictable behavior after extended operation

**Remediation**: Implement state validation, context sanitization, and lineage tracking.

**Confidence: HIGH** - Documented in Roocode context poisoning [seed:Roocode].

---

### Over-Delegation

**Name**: Excessive Task Decomposition

**Description**: Decomposing tasks too finely, creating excessive coordination overhead and losing task coherence.

**Failure Mode**:
- Communication overhead dominates execution time
- Lost context between subtask handoffs
- Difficulty maintaining coherent overall strategy
- Increased failure points

**Remediation**: Balance decomposition granularity with coordination cost.

**Confidence: MEDIUM** - Observed in hierarchical systems, limited formal study.

---

### Under-Specified Intent

**Name**: Ambiguous Task Definition

**Description**: Providing agents with vague or incomplete task specifications, expecting them to infer missing details.

**Failure Mode**:
- Agents pursue incorrect interpretations
- Scope creep as agents add assumptions
- Inconsistent results across runs
- User frustration from unexpected outputs

**Remediation**: Use structured task specifications with explicit constraints; implement clarification prompts.

**Confidence: HIGH** - Common failure mode, addressed by Kilo ask_followup_question [seed:Kilo-ask].

---

### Retry Without Adaptation

**Name**: Identical Retry Loop

**Description**: Retrying failed operations with identical parameters, expecting different results without adaptation.

**Failure Mode**:
- Infinite retry loops
- Resource waste on unrecoverable failures
- Masking underlying issues
- Eventual timeout without resolution

**Remediation**: Implement adaptive retry with parameter variation or alternative approaches.

**Confidence: HIGH** - Basic engineering anti-pattern, common in simple agent implementations.

---

### Centralized Bottleneck

**Name**: Single Coordinator Overload

**Description**: Routing all agent coordination through a single central agent or service, creating a bottleneck.

**Failure Mode**:
- Scalability limits as agent count grows
- Single point of failure
- Increased latency for coordination
- Coordinator overload leading to failures

**Remediation**: Implement distributed coordination or hierarchical delegation.

**Confidence: HIGH** - Established distributed systems anti-pattern.

---

### Ignoring Livelock

**Name**: Activity Without Progress

**Description**: Monitoring agent activity (heartbeats, tool calls) without verifying actual progress toward task completion.

**Failure Mode**:
- Agents appear healthy but make no progress
- Resource consumption without value
- Difficult to detect without progress metrics
- May continue indefinitely

**Remediation**: Implement progress metrics and thresholds, not just activity monitoring.

**Confidence: MEDIUM** - Under-discussed in agent literature, observed in practitioner reports.

---

## Use-Case Patterns

### CI/CD Pipeline Integration

**Pattern**: CLI Agent Swarm for Continuous Integration

**Description**: Deploy multiple CLI agents (Kilo, Cline) in CI/CD pipelines for parallel code review, testing, and deployment tasks.

**Implementation Notes**:
- Use mode-based operation for task-specific behavior
- Implement checkpoint-based execution for human gates
- Monitor with watchdog pattern for pipeline reliability

**Confidence: HIGH** - Production deployments exist.

---

### Multi-File Refactoring

**Pattern**: IDE Agent with MCP Tools

**Description**: Use IDE-integrated agents (VS Code Agent Mode, Augment) with MCP tools for semantic codebase understanding during large-scale refactoring.

**Implementation Notes**:
- Leverage repo grokking for cross-file awareness
- Use hierarchical orchestration for complex refactorings
- Implement adversarial review for quality assurance

**Confidence: HIGH** - Common use case for IDE agents.

---

### Autonomous Bug Fixing

**Pattern**: Hierarchical Diagnosis and Repair

**Description**: Deploy planner agent for bug diagnosis, specialist agents for fix proposals, and critic agents for validation.

**Implementation Notes**:
- Use conditional multi-stage recovery for novel bugs
- Implement voting for fix selection
- Use checkpoint-based execution for human approval

**Confidence: MEDIUM** - Research prototypes exist, production validation limited.

---

### Code Review Automation

**Pattern**: Adversarial Review Swarm

**Description**: Deploy multiple reviewer agents with different focus areas (security, performance, style) and aggregate findings.

**Implementation Notes**:
- Use MoA pattern for comprehensive coverage
- Implement trust scoring for reviewer weighting
- Use clarification prompts for ambiguous issues

**Confidence: HIGH** - Validated in research, production implementations exist.

---

## Additional Patterns: Modes, Skills, and Workflows

*Source: Kimi-Research analysis (Modes, Skills, Workflows)*

### Progressive Disclosure Skill Architecture

**Description**: Three-level skill architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

| Level | Content | Token Estimate | Purpose |
|-------|---------|----------------|---------|
| **Level 1: Identity** | Name, description, triggers | ~100 tokens | Skill selection |
| **Level 2: Instructions** | Procedural knowledge, examples | ~1,000 tokens | Task execution |
| **Level 3: Resources** | Scripts, templates, references | Unbounded | Deep expertise |

**When to Use**:
- Large skill libraries with diverse capabilities
- Context-constrained environments
- Systems requiring dynamic skill loading

**Tradeoffs**:
- ✅ Minimizes context window usage
- ✅ Enables deep expertise access
- ❌ Multi-stage loading adds latency

---

### Mode-Specific Tool Access

**Description**: Different agent modes activate different tool sets, reducing context window usage and improving tool selection accuracy.

| Mode | Primary Use | Autonomy Level | Human Oversight |
|------|-------------|----------------|-----------------|
| **Code** | Implementation | Medium | Review required |
| **Ask** | Explanation | Low | Minimal |
| **Architect** | Design | High | Approval gates |
| **Debug** | Troubleshooting | Medium | Confirmation |
| **Orchestrator** | Coordination | Very High | Exception handling |

**When to Use**:
- Multi-purpose agent systems
- Tasks with varying risk profiles
- Systems requiring different expertise levels

---

### Skill Composition Pattern

**Description**: Complex tasks invoke multiple skills sequentially, with skills able to reference other skills for reusable capability building blocks.

**Skill Execution Lifecycle**:
1. **Trigger Detection**: User request matches skill description
2. **Context Injection**: Skill instructions loaded as hidden message
3. **Permission Activation**: Pre-approved tools enabled
4. **Execution**: Agent completes task with enriched context
5. **Cleanup**: Skill context removed

**When to Use**:
- Complex multi-step tasks
- Workflows requiring multiple expertise areas
- Systems with reusable capability components

---

### Workflow Templating Pattern

**Description**: Common workflows defined as reusable templates with explicit step sequencing and variables.

**When to Use**:
- Repeated task patterns
- Team standardization requirements
- Audit trail requirements

**Tradeoffs**:
- ✅ Reproducible execution
- ✅ Clear audit trail
- ❌ Reduced flexibility
- ❌ Template maintenance overhead

---

## Architecture Anti-Patterns

*Source: Kimi-Research analysis*

### Anti-Pattern: God Agent

**Description**: A single agent tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Remediation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Confidence: HIGH** - Common anti-pattern in early agent implementations.

---

### Anti-Pattern: Chatty Agent Communication

**Description**: Agents communicate excessively, causing latency and cost explosion.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Remediation**: Batch communications and use shared state instead of per-step confirmations.

**Confidence: HIGH** - Observed in production multi-agent systems.

---

### Anti-Pattern: Big Bang Deployment

**Description**: Deploying AI systems all at once without gradual rollout.

**Failure Mode**:
- Production failures affect all users
- Difficult to rollback quickly
- No learning opportunity
- High risk

**Remediation**: Gradual rollout with canary deployments and automatic rollback.

**Confidence: HIGH** - Standard DevOps anti-pattern applied to AI systems.

---

## Agent Design Anti-Patterns

*Source: Kimi-Research analysis*

### Anti-Pattern: Prompt Injection Vulnerability

**Description**: Agents execute user input without sanitization.

**Failure Mode**:
- Arbitrary code execution
- Data exfiltration
- System compromise

**Remediation**: Input validation and sandboxing of all user-provided content.

**Confidence: HIGH** - Critical security vulnerability.

---

### Anti-Pattern: Hallucination Acceptance

**Description**: Blindly accepting AI-generated output without verification.

**Failure Mode**:
- Production bugs
- Security vulnerabilities
- Incorrect functionality

**Remediation**: Multi-layer verification including syntax check, test execution, and static analysis.

**Confidence: HIGH** - Common failure mode in production AI systems.

---

### Anti-Pattern: Temperature Ignorance

**Description**: Using wrong temperature for task type.

**Failure Mode**:
- Inconsistent code generation
- Hallucinated facts
- Poor task performance

**Remediation**: Task-appropriate temperature settings (0.1 for code, 0.0 for factual Q&A, 0.7 for creative tasks).

**Confidence: HIGH** - Well-documented model behavior.

---

## Summary

The patterns identified reveal a maturing field with clear best practices emerging:

1. **Decomposition is essential** - Monolithic agents fail; system-theoretic decomposition succeeds
2. **Hierarchy provides structure** - Hierarchical orchestration balances complexity with coordination
3. **Human-in-the-loop remains critical** - Checkpoints and clarification prevent runaway execution
4. **Monitoring must include progress** - Activity monitoring alone misses livelock
5. **Standardization accelerates** - MCP and similar protocols reduce integration overhead
6. **Adversarial approaches improve quality** - Critic agents catch what single agents miss

**Confidence levels vary by pattern maturity** - Architectural patterns generally HIGH confidence, operational patterns MEDIUM to HIGH, and emerging patterns (stigmergic coordination) MEDIUM to LOW.
