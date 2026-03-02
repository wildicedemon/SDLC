# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?

# System Design & Philosophy: Patterns and Anti-Patterns

## Design Patterns

### Auto-Launch Workspaces

**Description**: Deterministic workspace initialization triggered by opening a project, using configuration files (e.g., `.kilocode/launchConfig.json`) to specify profile, mode, and initial prompts.

**When to Use**:
- Reproducible development environments
- A/B testing across models or modes
- Onboarding new team members
- CI/CD pipeline initialization

**Tradeoffs**:
- **Benefits**: Guaranteed consistency, reduced cold-start time, explicit configuration
- **Costs**: Reduced flexibility, configuration maintenance, workspace-specific setup

**Implementation Notes**: Kilo's Auto-Launch enables workspace-triggered deterministic task execution with profile/mode/prompt triples [5].

---

### Bidirectional Specifications

**Description**: Specifications that evolve alongside code implementations, with agents updating specs as they discover codebase realities.

**When to Use**:
- Production codebases with active development
- Long-lived projects where specs would otherwise become stale
- Teams using both human and agent contributors

**Tradeoffs**:
- **Benefits**: Prevents specification debt, maintains alignment between intent and implementation
- **Costs**: Requires agent coordination, potential for spec churn

**Implementation Notes**: AugmentCode advocates for bidirectional maintenance where agents update plans when discovering codebase realities [2].

---

### BDI Hybrid Architecture

**Description**: Combining Belief-Desire-Intent (BDI) symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability.

**When to Use**:
- Safety-critical systems requiring accountability
- Systems needing explainable decisions
- Multi-agent coordination scenarios

**Tradeoffs**:
- **Benefits**: Accountable autonomy, verifiable intentions, audit-friendly
- **Costs**: Coordination overhead, requires dual expertise (symbolic + neural)

**Implementation Notes**: BDI architectures provide explicit mental states that can be logged and audited, contrasting with implicit LLM intentionality [1].

---

### 4-Phase Spec-Driven Workflow

**Description**: Structured development workflow with explicit phases: Specify (requirements), Plan (decomposition), Tasks (generation), Implement (execution with verification).

**When to Use**:
- Regulated industries requiring audit trails
- Complex multi-file changes
- Teams needing reproducible workflows

**Tradeoffs**:
- **Benefits**: 56% faster development, clear audit trail, reproducible
- **Costs**: Upfront investment, maintenance burden, reduced flexibility

**Implementation Notes**: AugmentCode's GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are properly maintained [2].

---

### Modular Agent Decomposition

**Description**: Decomposing agent systems into distinct subsystems (Retriever, Writer, Manager, Observer, core orchestration) with clear interfaces.

**When to Use**:
- Complex agent systems with multiple responsibilities
- Systems requiring independent scaling
- Teams with specialized expertise

**Tradeoffs**:
- **Benefits**: Testable components, clear separation of concerns, independent evolution
- **Costs**: Implementation complexity, coordination overhead

**Implementation Notes**: The 12 Agentic Design Patterns framework provides modular building blocks for reliable agent architectures [4].

---

### Critic-Actor Pattern

**Description**: Separate agents for generation (actor) and review (critic), with the critic validating outputs before commit.

**When to Use**:
- High-stakes code generation
- Security-sensitive changes
- Quality-critical deployments

**Tradeoffs**:
- **Benefits**: Higher quality outputs, catches errors before commit
- **Costs**: Increased latency, requires critic agent configuration

**Implementation Notes**: Well-established pattern from multi-agent systems literature.

---

### Structured Human-in-Loop

**Description**: Explicit checkpoints for human review using structured clarification tools (e.g., `ask_followup_question`).

**When to Use**:
- Uncertain task boundaries
- High-impact decisions
- Regulatory requirements for human oversight

**Tradeoffs**:
- **Benefits**: Prevents runaway execution, captures human intent
- **Costs**: Latency, requires human availability

**Implementation Notes**: Kilo's `ask_followup_question` tool enables structured human-in-loop clarification [5].

---

### Semantic Codebase Understanding

**Description**: Building comprehensive codebase understanding through semantic analysis rather than file-by-file processing.

**When to Use**:
- Large codebases (>10K LOC)
- Complex dependency graphs
- Architecture drift detection

**Tradeoffs**:
- **Benefits**: Prevents context poisoning, enables drift detection
- **Costs**: Initial indexing cost, requires maintenance

**Implementation Notes**: Zencoder's "Repo Grokking" uses semantic analysis for comprehensive codebase understanding [4].

---

## Anti-Patterns

### Vibe Coding

**Description**: Ad-hoc code generation without explicit specifications or structured workflows, relying on agent intuition.

**Failure Mode**:
- Inconsistent outputs
- Difficult to reproduce
- No audit trail
- Scope creep

**Mitigation**: Implement spec-driven workflows with explicit phases and verification gates.

---

### Shallow Repo Understanding

**Description**: File-by-file analysis without architectural context, leading to incomplete mental models.

**Failure Mode**:
- Context poisoning (incorrect assumptions about dependencies)
- Inconsistent changes across related files
- Missed architectural constraints

**Mitigation**: Use semantic codebase understanding tools (Repo Grokking) to build comprehensive models [4].

---

### Stale Documentation Specs

**Description**: Human-only specification maintenance that diverges from implementation reality.

**Failure Mode**:
- Agents execute against outdated assumptions
- Specification debt accumulates
- Trust in specifications erodes

**Mitigation**: Implement bidirectional specification maintenance where agents update specs alongside code changes [2].

---

### Unbounded Context Accumulation

**Description**: Allowing agents to accumulate context without explicit limits, leading to token budget exhaustion.

**Failure Mode**:
- Runaway token costs
- Context window overflow
- Degraded output quality

**Mitigation**: Implement explicit token budgets and retrieval strategies with clear boundaries.

---

### Credential Sprawl in IDE

**Description**: Storing credentials in IDE configuration or agent memory without proper vaulting.

**Failure Mode**:
- Security breaches
- Credential leakage in logs
- Compliance violations

**Mitigation**: Use credential vaulting with short-lived tokens and event-based rotation.

---

### Single-Pass Generation

**Description**: Generating code in a single pass without verification or refinement loops.

**Failure Mode**:
- Lower quality outputs
- Missed edge cases
- Inconsistent style

**Mitigation**: Implement multi-pass generation with critic review or self-reflection.

---

### Implicit Intent Tracking

**Description**: Relying on agent memory or conversation history for intent tracking without explicit logging.

**Failure Mode**:
- Lost context across sessions
- No audit trail
- Difficult debugging

**Mitigation**: Log design decisions explicitly with timestamps and rationale.

---

### Monolithic Agent Design

**Description**: Building single agents that handle all responsibilities without modular decomposition.

**Failure Mode**:
- Hard to test individual components
- Single point of failure
- Difficult to scale

**Mitigation**: Decompose into specialized agents with clear interfaces.

---

## Pattern Selection Guide

| Scenario | Recommended Pattern | Rationale |
|----------|---------------------|-----------|
| New project exploration | Intent-Driven + Critic-Actor | Flexibility with quality gates |
| Production feature development | 4-Phase Spec-Driven + Bidirectional | Reproducibility with maintenance |
| Large codebase refactoring | Semantic Understanding + Modular | Context awareness with isolation |
| Safety-critical systems | BDI Hybrid + Structured HITL | Accountability with oversight |
| Rapid prototyping | Auto-Launch + Intent-Driven | Speed with consistency |
| Multi-team collaboration | Modular Decomposition + Spec-Driven | Clear interfaces with audit |

### Intent-Driven Development

**Description**: Starting with intent rather than specifications, allowing agents to draft plans based on codebase analysis and update them as they discover implementation realities.

**When to Use**:
- Exploratory development where requirements evolve
- Projects with legacy code where specs would be inaccurate
- Teams wanting to reduce documentation maintenance burden

**Tradeoffs**:
- **Benefits**: Self-maintaining specs, adapts to codebase reality, reduced human maintenance
- **Costs**: Less reproducibility than spec-driven, requires trust in agent judgment

**Implementation Notes**: AugmentCode's Intent product demonstrates this approach—agents draft specs from codebase analysis, update them during execution, and surface decisions that change direction [7].

---

### Progressive Disclosure Architecture

**Description**: Three-level skill/knowledge architecture that minimizes context window consumption while maintaining access to deep procedural knowledge.

**When to Use**:
- Large skill libraries (>50 skills)
- Context-sensitive capability loading
- Multi-agent systems with shared knowledge

**Tradeoffs**:
- **Benefits**: Efficient context usage, on-demand expertise, scalable knowledge
- **Costs**: Implementation complexity, requires skill management system

**Implementation Notes**: Level 1 (Identity: ~100 tokens) for selection, Level 2 (Instructions: ~1,000 tokens) for execution, Level 3 (Resources: unbounded) for deep expertise [8].

---

## Anti-Patterns

### God Agent

**Description**: A single agent that tries to handle all tasks, becoming a bottleneck and single point of failure.

**Failure Mode**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Mitigation**: Use specialized agents with clear responsibilities coordinated by an orchestrator.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Chatty Agent Communication

**Description**: Agents communicating excessively, causing latency and cost explosion through repeated API calls.

**Failure Mode**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Mitigation**: Batch communications and use shared state instead of per-step confirmations.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Blind Trust in AI Output

**Description**: Accepting AI-generated code without verification, assuming correctness.

**Failure Mode**:
- Production bugs from hallucinations
- Security vulnerabilities (40-45% of AI code contains weaknesses)
- Incorrect functionality

**Mitigation**: Implement multi-layer verification: syntax checks, test execution, static analysis, and human review for high-stakes code.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### Temperature Ignorance

**Description**: Using the same temperature setting for all task types regardless of requirements.

**Failure Mode**:
- Inconsistent code generation (temperature too high)
- Hallucinated facts (temperature too high for factual tasks)
- Lack of creativity when needed (temperature too low)

**Mitigation**: Use task-appropriate temperatures:
- Code generation: 0.1 (consistency)
- Code review: 0.1 (consistency)
- Documentation: 0.3 (some creativity)
- Brainstorming: 0.7 (high creativity)
- Factual Q&A: 0.0 (deterministic)

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

### False Confidence

**Description**: Presenting uncertain AI results as certain without confidence indicators.

**Failure Mode**:
- Wrong decisions based on overconfident outputs
- Over-reliance on AI without verification
- Missed edge cases

**Mitigation**: Always include confidence scores and uncertainty areas with AI outputs.

**Source**: Kimi-Research ANTI_PATTERNS.md [9]

---

## Anti-Pattern Detection Checklist

- [ ] Are specifications updated when code changes?
- [ ] Is there a token budget enforcement mechanism?
- [ ] Are credentials stored in a vault?
- [ ] Is there a verification loop before commit?
- [ ] Are design decisions logged explicitly?
- [ ] Is the agent system decomposed into modules?
- [ ] Is there a human-in-loop checkpoint for high-impact decisions?
- [ ] Is codebase understanding semantic (not just file-by-file)?
- [ ] Are agents specialized rather than monolithic?
- [ ] Is agent communication batched efficiently?
- [ ] Are AI outputs verified before use?
- [ ] Is temperature appropriate for each task type?
- [ ] Are confidence scores provided with uncertain outputs?
