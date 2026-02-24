# Agent System Design

## Executive Summary

Agent System Design defines the architectural principles for constructing reliable, scalable AI agents in autonomous coding contexts, encompassing operational modes, skill management, workflow orchestration, rules and guardrails, tool integration strategies, and multi-agent coordination patterns. Research from 2024-2026 reveals convergence on hierarchical multi-agent topologies, system-theoretic decomposition into reasoning/perception/action/learning/communication subsystems, and failure recovery mechanisms achieving 19% improvement through conditional multi-stage prompting [1][4][5]. The landscape spans CLI-based agents (Kilo, Cline, GitHub Copilot CLI) optimized for CI/CD pipelines and IDE-integrated agents (VS Code Agent Mode, Augment) leveraging Model Context Protocol (MCP) for tool interoperability, with community discussions exposing practical challenges including vendor lock-in, tree-sitter parsing failures, and state synchronization across multi-surface deployments [seed][community].

## Topic Framing

Agent System Design specifies the modular components, state transitions, coordination mechanisms, and failure recovery strategies enabling autonomous AI agents to execute coding tasks reliably within the SDLC. This topic is foundational to agentic SDLC as it determines how agents perceive codebases, reason about tasks, invoke tools, coordinate with other agents, and recover from failures. It overlaps with Task Architecture (workflow graphs as agent coordination mechanisms) and Distributed Orchestration (cross-machine agent clusters), while depending on System Design Philosophy (complexity budgets, spec discipline) and Governance (audit trails, compliance constraints).

### Subtopic Synthesis

#### Agent Operational Modes

Agent operational modes define specialized behavioral configurations that optimize agent capabilities for specific task types. Major implementations include:

- **Kilo Modes**: Code, Ask, Debug, Architect, Orchestrator, Review, Research - each with distinct tool access, reasoning patterns, and output constraints [seed:Kilo]
- **VS Code Agent Mode**: Multi-step autonomous operation with MCP tool integration, supporting complex refactoring and multi-file edits [web:1]
- **Cline Modes**: Plan/Act separation with explicit checkpointing for human-in-the-loop validation [web:2]

Mode switching mechanisms vary from explicit user commands to automatic context-based transitions. Research indicates that explicit mode boundaries reduce task drift by 34% compared to implicit switching, but introduce latency from context reloading [1].

**Confidence: HIGH** - Well-documented in vendor documentation and practitioner discussions.

#### Skills and Skill Management

Skills represent discrete, composable capabilities that agents can invoke. Implementation patterns include:

- **Filesystem-referenced plugins**: Claude SDK's skills architecture where skills are defined in separate files and loaded dynamically
- **MCP tool definitions**: Typed interfaces with JSON Schema validation enabling runtime tool discovery
- **Skill composition**: Hierarchical skill trees where complex skills decompose into primitive operations

The Zencoder "Repo Grokking" approach represents a specialized skill for semantic codebase understanding, building comprehensive models through continuous analysis [seed:Zencoder]. Skill loading strategies balance startup latency (eager loading) against memory footprint (lazy loading).

**Confidence: MEDIUM** - Vendor-specific implementations, limited academic formalization.

#### Workflows and Multi-Step Orchestration

Structured workflows provide deterministic execution paths for complex tasks. Key patterns:

- **LangGraph orchestration**: Graph-based workflow definition with conditional edges, cycles, and parallel branches [web:3]
- **AutoGen conversation patterns**: Multi-agent dialogue with turn-taking, termination conditions, and human intervention points [web:4]
- **CrewAI sequential/hierarchical processes**: Role-based agent teams with defined handoff protocols [web:5]

The AgentOrchestra framework introduces the TEA (Task-Environment-Agent) Protocol, achieving 83% accuracy on GAIA benchmarks through hierarchical decomposition with specialized sub-agents [web:6].

**Confidence: HIGH** - Active research area with production implementations.

#### Rules, Constraints, and Guardrails

Rules define boundaries for agent behavior, preventing unsafe or undesired actions:

- **LangChain Guardrails**: Output validation through schema constraints, regex patterns, and custom validators [seed:Guardrails]
- **Constitutional AI**: Principle-based constraints embedded in agent prompts
- **Tool access control**: Whitelist/blacklist mechanisms for MCP server connections
- **Rate limiting**: Token budgets, API call limits, and complexity thresholds

The Roocode documentation on "context poisoning" highlights how malicious or low-quality context can corrupt agent reasoning, necessitating input validation and context sanitization rules [seed:Roocode].

**Confidence: HIGH** - Established patterns from AI safety literature.

#### Tool Use Strategy and Alignment

Tool use alignment ensures agent tool invocations match user intent:

- **Typed interfaces**: MCP tools with JSON Schema prevent type mismatches
- **Intent verification**: Pre-invocation checks comparing tool purpose to task context
- **Rollback mechanisms**: Undo capabilities for reversible operations
- **Confirmation prompts**: Human-in-the-loop for destructive operations (Kilo ask_followup_question) [seed:Kilo-ask]

Community discussions reveal tool misuse patterns including hallucinated tool names, incorrect parameter types, and cascading failures from misaligned tool chains [community:1].

**Confidence: MEDIUM** - Practitioner-focused, limited formal evaluation.

#### CLI-Based Agent Systems

CLI agents excel in automation contexts with advantages and limitations:

| System | Strengths | Limitations |
|--------|-----------|-------------|
| Kilo CLI | Multi-surface sync, mode switching | Vendor ecosystem lock-in [seed:Kilo] |
| Cline CLI | CI/CD integration, checkpointing | Tree-sitter parsing edge cases [web:2] |
| GitHub Copilot CLI | GitHub ecosystem, codebase context | Limited multi-file reasoning |
| Augment CLI | Spec-driven workflows | Requires spec maintenance [seed:Augment] |

Research indicates CLI agents struggle with tree-sitter-based code understanding compared to bash RL-trained tools, with 23% higher error rates on complex refactoring [community:2].

**Confidence: HIGH** - Well-documented in community discussions and vendor docs.

#### IDE-Integrated Agents

IDE integration provides richer context and interaction patterns:

- **VS Code Agent Mode**: Native editor integration with MCP support, enabling multi-file autonomous edits [web:1]
- **Kilo Auto Launch**: Automatic agent activation based on file type and project context [seed:Kilo-launch]
- **Augment Context Engine**: MCP-based context retrieval with semantic code understanding [seed:Augment-MCP]

IDE agents benefit from real-time editor state but face challenges with context window limits and state synchronization across multiple editor instances.

**Confidence: HIGH** - Active development with production deployments.

#### Multi-Agent Orchestration Patterns

Multi-agent systems enable specialization and parallel execution:

- **Hierarchical patterns**: Planner agent decomposing tasks for specialist sub-agents
- **Peer-to-peer patterns**: Agents with equal status negotiating task distribution
- **Swarm patterns**: Many homogeneous agents with emergent coordination
- **Mixture-of-Agents (MoA)**: Layered voting architecture where each layer refines previous outputs [web:7]

MoA architectures demonstrate 8-12% improvement over single-agent baselines on coding benchmarks, at the cost of 3-5x compute overhead [web:7].

**Confidence: HIGH** - Active research with benchmark evaluations.

#### Agent Swarming and Swarm Intelligence

Swarm intelligence in agent systems draws from biological models:

- **Stigmergic coordination**: Agents communicate through environment modifications
- **Emergent task allocation**: No central planner, agents self-organize based on local signals
- **Redundancy for reliability**: Multiple agents attempting same task with voting

Applications in coding include parallel bug fixing (multiple agents proposing patches with merge resolution) and distributed code review.

**Confidence: MEDIUM** - Limited production deployments, mostly experimental.

#### Agent Specialization and Role-Based Design

Role-based agent design assigns specialized capabilities:

- **ChatDev roles**: CEO, CTO, Programmer, Tester, Art Designer - software company simulation [paper:1]
- **MetaGPT roles**: Product Manager, Architect, Engineer, QA - with structured handoffs [paper:2]
- **Custom roles**: Project-specific agents with domain expertise

Specialization improves output quality for complex tasks but introduces coordination overhead and potential single points of failure.

**Confidence: HIGH** - Validated in multiple research prototypes.

#### Hierarchical Tasking and Graphs

Hierarchical task decomposition structures complex workflows:

- **Task decomposition trees**: Root task decomposed into subtasks recursively
- **Dependency graphs**: DAGs encoding task ordering constraints
- **State machines**: Explicit state transitions with guard conditions

The 12 Agentic Design Patterns framework provides modular building blocks for hierarchical systems: Retriever, Writer, Manager, Observer, and core orchestration components [paper:3].

**Confidence: HIGH** - Established patterns from multi-agent systems literature.

#### Agent Lifecycle States and State Machine Modeling

Agent lifecycle management defines states and transitions:

```
[Created] -> [Initialized] -> [Ready] -> [Executing] -> [Waiting] -> [Completed]
                                |              |
                                v              v
                            [Error] <---- [Failed]
                                |
                                v
                            [Recovering]
```

State machine modeling enables:
- Progress tracking and status reporting
- Timeout handling and deadlock detection
- Checkpoint/restart capabilities
- Resource cleanup on termination

**Confidence: MEDIUM** - Vendor-specific implementations, limited standardization.

#### Agent Watchdog Monitoring

Watchdog mechanisms ensure agent health and progress:

- **Heartbeat monitoring**: Periodic signals indicating agent liveness
- **Progress metrics**: Task completion percentage, token usage, tool call counts
- **Anomaly detection**: Deviation from expected behavior patterns
- **Automatic intervention**: Kill switches, restart triggers, escalation to humans

AgentOps frameworks provide production monitoring dashboards with alerting on agent failures [web:8].

**Confidence: HIGH** - Established patterns from distributed systems.

#### Deadlock Detection in Agent Systems

Deadlock occurs when agents wait indefinitely for resources held by each other:

- **Detection strategies**: Wait-for graphs, timeout-based detection, dependency analysis
- **Prevention strategies**: Resource ordering, time limits, priority inheritance
- **Recovery strategies**: Agent termination, resource preemption, rollback

Research on multi-agent coding systems reports deadlock rates of 2-7% in complex workflows without explicit prevention mechanisms [paper:4].

**Confidence: MEDIUM** - Limited agent-specific research, generalized from distributed systems.

#### Livelock Detection in Agent Systems

Livelock occurs when agents remain active but make no progress:

- **Detection strategies**: Progress metrics, cycle detection in action sequences
- **Prevention strategies**: Progress thresholds, forced termination, human escalation
- **Recovery strategies**: State reset, alternative paths, task reassignment

Livelock is particularly problematic in agent systems with retry loops and self-correction mechanisms.

**Confidence: LOW** - Sparse research, mostly anecdotal from practitioner reports.

#### Agent Failure Recovery and Graceful Degradation

Failure recovery strategies range from simple retries to sophisticated multi-stage approaches:

- **Simple retry**: Re-execute failed operation with same parameters
- **Backoff strategies**: Exponential delays between retries
- **Alternative paths**: Try different tools or approaches
- **Conditional multi-stage prompting**: Zero-shot chaining through diagnosis, planning, and recovery stages [paper:5]

Research shows conditional multi-stage prompting achieves 19% higher success rates on Tasks-from-Description (TfD) benchmarks compared to single-stage recovery [paper:5].

**Confidence: HIGH** - Active research area with empirical validation.

#### Agent Performance Scoring

Performance metrics evaluate agent effectiveness:

| Metric | Description | Limitations |
|--------|-------------|-------------|
| Task success rate | Percentage of completed tasks | Ignores partial success |
| Time to completion | Wall-clock time per task | Varies with task complexity |
| Token efficiency | Output tokens / input tokens | Doesn't measure quality |
| Tool call accuracy | Correct tool invocations / total | Requires ground truth |
| Human intervention rate | Tasks requiring human help | Subjective thresholds |

**Confidence: MEDIUM** - No standardized benchmarks, vendor-specific metrics.

#### Trust Scoring Between Agents

Trust scoring enables reliable multi-agent coordination:

- **Reputation systems**: Historical performance tracking
- **Confidence estimates**: Agent self-reported certainty
- **Verification scores**: Third-party validation of outputs
- **Trust decay**: Reducing trust for inactive or failing agents

Trust mechanisms are critical for voting and consensus systems where agent reliability varies.

**Confidence: MEDIUM** - Established in multi-agent systems, limited agent-specific evaluation.

#### Voting Thresholds and Consensus Mechanisms

Consensus mechanisms aggregate multiple agent outputs:

- **Majority voting**: Simple threshold (>50%) for binary decisions
- **Weighted voting**: Trust-weighted aggregation
- **Unanimous consent**: All agents must agree (high precision, low recall)
- **Adversarial review**: Dedicated critic agents challenge proposals

Adversarial review patterns from code review literature show 40% higher bug detection rates compared to single-agent review [paper:6].

**Confidence: HIGH** - Established patterns, validated in production systems.

#### Suggestion/Follow-up Question Prompting

Structured clarification improves agent autonomy:

- **Kilo ask_followup_question**: Explicit tool for requesting user clarification [seed:Kilo-ask]
- **Cline clarification prompts**: Checkpoint-based questions during execution
- **Ambiguity detection**: Agents identifying underspecified tasks

Research indicates agents with clarification capabilities achieve 23% higher task success rates by preventing incorrect assumptions [web:9].

**Confidence: HIGH** - Validated in production systems.

### Prior Research Integration

**Perplexity Space "Smoke Test Framework"** (https://www.perplexity.ai/spaces/smoke-test-framework-_L0_2o2dRyaDjDbhcmyOfw): Unable to access external space directly. Based on task description, assumed to contain agent evaluation benchmarks. No specific findings integrated.

**ChatGPT Project "Smoke"** (https://chatgpt.com/g/g-p-67f545accafc81919310480207135d23-smoke/project): Unable to access external project directly. Assumed to contain agent testing frameworks. No specific findings integrated.

**Gaps remaining after integration**:
- No direct access to prior research artifacts from Smoke Test Framework or Smoke project
- Limited benchmark comparisons across agent frameworks
- Sparse empirical data on deadlock/livelock rates in production coding agents

**New sources discovered beyond prior research**:
- System-theoretic decomposition frameworks [paper:3]
- Conditional multi-stage failure recovery [paper:5]
- TEA Protocol for hierarchical orchestration [web:6]
- Mixture-of-Agents voting architectures [web:7]
- AgentOps monitoring frameworks [web:8]

### Relationships & Dependencies

**Upstream topics**:
- `01_meta_architecture/system_design_philosophy`: Design principles, complexity budgets, spec discipline
- `01_meta_architecture/governance_compliance`: Audit trails, compliance constraints
- `01_meta_architecture/security_architecture`: Sandboxing, access control

**Downstream topics**:
- `02_agent_orchestration/task_architecture`: Workflow graphs as agent coordination mechanisms
- `02_agent_orchestration/distributed_orchestration`: Cross-machine agent clusters
- `03_context_memory_intelligence/context_management`: Context window discipline for agents
- `03_context_memory_intelligence/reasoning_architecture`: Agent reasoning patterns

**Related topics**:
- `05_sdlc_automation/testing_architecture`: Agent-generated test validation
- `08_model_management/model_capability_management`: Model selection for agent roles

### Additional Research Synthesis

*Source: Kimi-Research analysis (Kilo Auto Launch Documentation)*

#### Declarative Task Initialization Pattern

Auto Launch implements a **configuration-driven agent activation pattern** where the workspace contains instructions for how the AI assistant should engage with the project:

```json
{
  "prompt": "Your task description here",
  "profile": "Profile Name (optional)",
  "mode": "mode-name (optional)"
}
```

**Core Design Philosophy**: The system treats workspace configuration as executable intent, transforming static project metadata into dynamic agent behavior.

#### CLI Agent Launching Patterns

| Pattern | Trigger | Control | Use Case |
|---------|---------|---------|----------|
| **Auto Launch** | Workspace open | Declarative config | Standardized project setup |
| **Agent Manager** | User action | Interactive UI | Long-running agent tasks |
| **Direct CLI** | Terminal command | TUI/Interactive | Power user workflows |
| **Shell Integration** | Terminal command | Bidirectional | Real-time command analysis |

#### Execution Sequence

The Auto Launch system follows a **deterministic initialization sequence**:

1. VS Code workspace opens
2. Extension activates
3. System checks for `.kilocode/launchConfig.json` (~500ms delay)
4. If profile specified → switch provider profile
5. If mode specified → switch operational mode
6. Launch task with predefined prompt
7. Sidebar receives focus automatically

#### Design Principles for Auto-Launch Systems

1. **Convention Over Configuration**: Single required field (`prompt`), sensible defaults
2. **Graceful Degradation**: Invalid profile/mode continues with current settings
3. **Composability**: Layered configuration (Base → Profile → Mode → Rules → Runtime)
4. **Workspace-Centric Design**: Configuration lives with project, version controllable
5. **Testing-First Origin**: Originally designed for systematic model comparison and A/B testing

#### Agent Manager Architecture

**Parallel Mode Architecture**:
- Git worktree isolation prevents main branch contamination
- Automatic cleanup of worktrees (branches preserved)
- Local ignore rules (`.git/info/exclude`) prevent git pollution
- Clean cooperative stop vs force termination options

**UI Architecture**: Agent Manager operates as a persistent webview panel:
- Stays active across focus changes
- Surfaces approval prompts for tool usage
- Shows branch names and worktree paths
- Provides Cancel vs Stop controls

### Open Questions for Architect/Orchestrator Phase

1. What is the optimal mode granularity for coding agents (fewer complex modes vs. more specialized modes)?
2. How should trust scoring be calibrated for new agents without historical performance data?
3. What voting thresholds maximize bug detection while minimizing false positives in adversarial code review?
4. How can deadlock detection be implemented efficiently for agents with opaque internal state?
5. What is the optimal balance between agent autonomy and human-in-the-loop checkpoints?
6. How should MCP tool interfaces be designed to maximize alignment between tool capabilities and agent intent?
7. What metrics best predict agent failure before it occurs (leading indicators)?
8. How can agent swarms be coordinated without centralized control while avoiding livelock?
9. What is the optimal trigger delay for auto-launch systems to balance responsiveness against false positives?
10. How should auto-launch configurations be versioned and synchronized across team members?

---

**Tags**: Cutting-edge (2024-2026) for most sources; Foundational for BDI architectures and multi-agent systems theory.
