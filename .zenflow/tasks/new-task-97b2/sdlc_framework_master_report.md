# SDLC Framework Master Report

## 1. Framework Architecture

### Orchestration Model

The framework uses a hierarchical orchestration model combining Zenflow for task management with Kilo Code for agent execution.

- **Zenflow** manages task lifecycle: creation, assignment, tracking, completion
- **Kilo Code** provides agent execution modes: Orchestrator, Architect, Code, Debug, Review
- **LangGraph** implements SDLC phase transitions as a directed state machine
- Control flows unidirectionally: Research → Planning → Implementation → Verification
- Mode transitions are deterministic: planning outputs trigger architect mode, designs trigger code mode

*Sources: start_prompt.md §2.6, §4.4.2; Research.md §II.5-7*

### Workflow Hierarchy

Five-level decomposition structures all work:

1. **Initiative** — top-level business objective or feature request
2. **Phase** — SDLC stage (Research, Planning, Implementation, Verification)
3. **Stage** — logical grouping within a phase (e.g., "Anti-pattern scan" within Verification)
4. **Task** — assignable unit of work with clear acceptance criteria
5. **Atomic Action** — single tool invocation or file edit

Each level inherits context from its parent and reports status upward.

*Sources: Research.md §II.6, §2.3; start_prompt.md §4.2*

### Quality Gates

Every phase boundary enforces a quality gate before promotion:

- **Code Gate**: TypeScript compiles without errors; lint passes
- **Test Gate**: unit tests pass; ≥80% coverage on critical paths
- **Documentation Gate**: inline docs present; ADRs recorded for decisions
- **Workspace Hygiene Gate**: no uncommitted changes; branches clean; scanner state persisted

Gate failure triggers a Debug mode loop with remediation subtask creation.

*Sources: start_prompt.md §6.2, §4.6; Research.md §2.3 (quality gates, workspace hygiene)*

### Verification Protocol

All completions require empirical evidence, not self-reported status:

- Tests must produce passing output logs
- Scanner passes must produce artifact files
- CLI commands must execute without error codes
- Cost tracking must show non-zero progress metrics

*Sources: Research.md §2.3 (evidence-first completion); start_prompt.md §6.2*

---

## 2. Core Components

### 2.1 Framework Config Subsystem

- Hierarchical config: default → project → user override
- Schema-validated YAML at `.framework/config.yaml`
- JSON Schema at `.framework/schema.json`
- Environment variable substitution for secrets
- Hot reload support during development

*Source: start_prompt.md §4.4.1*

### 2.2 LangGraph Integration + CLI Wrapper

- SDLC pipeline modeled as LangGraph state graph
- Graph nodes: Research, Planning, Implementation, Verification
- State management persisted between phase transitions
- CLI entry point: `framework start|status|scan|bootstrap`
- Wraps existing LangGraph CLI; extends rather than duplicates

*Source: start_prompt.md §4.4.2*

### 2.3 Kilo Custom Modes

Three custom YAML mode definitions plus built-in Orchestrator:

| Mode | File | Purpose |
|------|------|---------|
| Requirements | `.kilo/modes/requirements.yaml` | Requirements extraction and analysis |
| Scanner | `.kilo/modes/scanner.yaml` | Deep Scanner execution mode |
| Review | `.kilo/modes/review.yaml` | Code review and verification |
| Orchestrator | (built-in) | High-level coordination via project rules |

Each mode defines: `roleDefinition`, `groups`, `tools`, `customInstructions`, `description`.

*Source: start_prompt.md §4.4.3*

### 2.4 Deep Scanner

Multi-pass continuous analysis engine:

- **Anti-pattern detection pass** — identifies code smells and anti-patterns
- **Architecture analysis pass** — validates separation of concerns
- **Performance profiling pass** — flags resource-intensive paths
- **Security auditing pass** — checks for vulnerabilities
- State persisted to `.framework/scanner-state.md`
- Learned patterns stored in `.framework/scanner-repertoire.md`
- Runs continuously until explicitly stopped or resource-bounded

*Sources: start_prompt.md §4.4.4, §4.7*

### 2.5 Waste Detection & Cost Oversight

- Token usage tracking per operation and per task
- Cost calculation per phase with budget thresholds
- Waste rules: >15K tokens with no progress → warn; >30K → pause
- Loop detection triggers break-and-report
- Langfuse integration for observability dashboard

*Source: start_prompt.md §4.4.5, §6.4*

### 2.6 Webhooks & GitHub Integration

- GitHub webhook receivers for issues, PRs, and CI failures
- Issue parsing auto-creates framework tasks
- PR review handler processes review requests
- CI failure handler creates remediation tasks
- Signature validation for webhook security

*Source: start_prompt.md §4.4.6*

### 2.7 Bootstrap / Self-Provisioning

Single-command setup: `framework bootstrap`

- Environment checks: Node.js, Python, Git, VS Code, Kilo Code extension
- Dependency installation: CodeGraphContext MCP, rag-memory-mcp, TaskMaster MCP, Playwright, LangGraph, Langfuse
- Secret validation: KILO_API_KEY, provider API keys
- Config generation: MCP server config, `.framework/` directory, defaults

*Sources: start_prompt.md §4.4.7, §4.8*

### 2.8 Voice / PersonaPlex Hooks

- Configuration placeholders in `.framework/config.yaml`
- Persona definition schema
- Voice command routing scaffolding
- Integration points for Kilo speech hooks

*Source: start_prompt.md §4.4.8*

---

## 3. Technology Stack

### Languages & Runtimes

| Technology | Role |
|-----------|------|
| TypeScript/JavaScript | Primary implementation (Kilo Code extension, framework modules) |
| Python | CLI scripts, LangGraph integration, scanner passes |
| YAML | Mode definitions, configuration files |
| JSON | Schema validation, API contracts |
| Markdown | Documentation, research artifacts, scanner state |

### Frameworks & Libraries

| Framework | Purpose |
|-----------|---------|
| LangGraph | SDLC pipeline state machine; phase transitions |
| Kilo Code SDK | Agent execution, mode management, CLI integration |
| Langfuse | Observability, cost tracking, telemetry |
| Playwright | End-to-end testing |
| pytest | Python unit/integration testing |

### Infrastructure & Tooling

| Tool | Purpose |
|------|---------|
| Docker | Containerization; reproducible environments |
| GitHub Actions / Jenkins | CI/CD pipelines |
| MCP Servers | CodeGraphContext, rag-memory-mcp, TaskMaster |
| VS Code | IDE integration via Kilo Code extension |
| Git worktrees | Parallel branch management for concurrent agent work |

### Data Stores

| Store | Purpose |
|-------|---------|
| File system (Markdown/YAML) | Scanner state, config, research artifacts |
| Vector DB | Agent memory, semantic search (via rag-memory-mcp) |
| PostgreSQL / Oracle | Application data (project-dependent) |

*Sources: start_prompt.md §0, §4.4.2, §4.4.7; Research.md §VI.18-19*

---

## 4. Workflow Lifecycle

### Phase 0: Discovery & Gap Analysis

1. Parse specification documents automatically
2. Extract requirements from user inputs
3. Gather context from existing codebase
4. Run gap analysis: current state vs. desired state
5. Assess feasibility of proposed features
6. Output: research summary, risks, technology recommendations

*Source: start_prompt.md §4.1*

### Phase 1: Planning

1. Decompose requirements into tasks with dependencies
2. Build task dependency graph
3. Sequence tasks for optimal execution
4. Allocate resources: time, token budget, API budget
5. Define checkpoints (every 5 tasks, at 50% budget, before major decisions)
6. Output: `.framework/plan.md`, dependency graph, effort estimates

*Source: start_prompt.md §4.2*

### Phase 2: Autonomous Execution

1. Select next task by priority and dependency resolution
2. Execute without per-step approval
3. Monitor progress against plan
4. Adaptively replan when blocked
5. Track resource consumption per operation
6. Escalate only on blocking failures or budget overruns

**Checkpoints**: after every 5 tasks; at 50% phase budget; before architectural decisions; on significant risk detection.

*Source: start_prompt.md §4.3*

### Phase 3: Implementation

Produces working code for all framework components:

- Match existing Kilo Code patterns
- Include comprehensive error handling
- Add logging at appropriate levels
- Write unit tests alongside code
- Compile-and-test before marking tasks complete

*Source: start_prompt.md §4.4*

### Phase 4: Verification

- Unit tests: ≥80% coverage
- Integration tests: all CLI commands execute
- E2E tests: full SDLC flow completes
- Performance benchmarks: no regressions
- Scanner: all passes execute and persist findings
- Workspace hygiene: clean branches, committed state

*Source: start_prompt.md §4.6, §7.8*

### Quality Gate Enforcement

| Gate | Trigger | Action on Failure |
|------|---------|-------------------|
| Compile | Phase 2→3 boundary | Return to Code mode |
| Test | Every 5 tasks | Debug mode + remediation subtask |
| Integration | Phase boundary | Block promotion; escalate |
| Full suite | Before completion | Mandatory fix cycle |

*Sources: start_prompt.md §6.2; Research.md §2.3*

---

## 5. Integration Points

### 5.1 Zenflow Task Orchestration

- Task creation, tracking, and status management
- Workflow execution triggers
- Progress reporting and status queries
- Artifact path management per task

### 5.2 MCP (Model Context Protocol) Servers

| MCP Server | Function |
|------------|----------|
| CodeGraphContext | Code graph navigation, symbol indexing, AST access |
| rag-memory-mcp | Persistent agent memory, semantic search |
| TaskMaster | Task state persistence, dependency resolution |

MCP servers require privilege isolation and secure inter-agent communication.

*Sources: Research.md §I.4 (MCP privilege isolation); start_prompt.md §4.4.7*

### 5.3 Kilo Code Extension

- Mode registration and switching
- VS Code command palette integration
- Extension settings and configuration injection
- Tool group management per mode

*Source: start_prompt.md §2.5*

### 5.4 CI/CD Pipelines

- GitHub Actions / GitLab CI / Jenkins integration
- Webhook-triggered pipeline runs
- CI failure analysis feeds back as remediation tasks
- Self-healing CI/CD: auto-retry with diagnostic context

*Sources: Research.md §V.16; start_prompt.md §4.4.6*

### 5.5 GitHub Webhooks

- Issue → task creation pipeline
- PR review → review mode trigger
- CI failure → debug mode trigger with context
- Signature validation for all incoming webhooks

*Source: start_prompt.md §4.4.6*

### 5.6 Langfuse Observability

- Token usage telemetry per operation
- Cost tracking per task and phase
- Waste detection rule evaluation
- Dashboard for real-time monitoring

*Source: start_prompt.md §4.4.5*

### 5.7 Reference Project Mining

Read-only access to local reference projects for pattern extraction:

- `agentic-dev-orchestrator`
- `ai_agent_enhancement`
- `Ice-Dev_InterAgent`

Non-trivial concept reuse requires approval via `.framework/reuse/proposals.md`.

*Source: start_prompt.md §5.1-5.3*

---

## 6. Performance & Compliance

### Performance Targets

| Metric | Target | Enforcement |
|--------|--------|-------------|
| Token efficiency | <15K tokens per task without waste flag | Waste detector warns at 15K, pauses at 30K |
| Test coverage | ≥80% on critical paths | Test gate blocks promotion below threshold |
| CLI response | Commands execute without timeout | Integration test validation |
| Scanner throughput | All 4 passes complete per scan cycle | Progress reporting per pass |
| Build | TypeScript compiles without errors | Compile gate at every checkpoint |

*Sources: start_prompt.md §4.4.5, §4.6, §6.4*

### Resource Management

- Track token usage, API calls, time, and cost per component
- Warn at 50% of phase budget
- Pause at 80% without justification
- Escalate at 100% or on overrun
- Loop detection: repeated same errors trigger escalation

*Source: start_prompt.md §6.4*

### Security Requirements

- **Prompt injection defense**: adversarial simulation testing
- **Context poisoning mitigation**: detection and filtering pipelines
- **MCP privilege isolation**: per-server permission boundaries
- **Sandboxed execution**: network egress restrictions, file permission modeling
- **Secret handling**: credential vaulting, environment variable substitution
- **Webhook security**: GitHub signature validation on all incoming requests
- **Input validation**: all external inputs sanitized before processing

*Sources: Research.md §I.4; start_prompt.md §4.5, §4.4.6*

### Governance & Compliance

- **Audit trail**: explainability logging for all decisions
- **Deterministic replay**: reproducibility frameworks for builds
- **License compliance**: SBOM generation and scanning
- **Supply chain security**: dependency validation
- **Policy enforcement**: configurable rules layer

*Source: Research.md §I.3*

### Reproducibility

- Deterministic builds via version-locked dependencies
- Scanner state persisted for audit replay
- Research artifacts committed as markdown for traceability
- Configuration schema-validated on every load

---

## 7. Critical Decisions

### Resolved Decisions

| ID | Decision | Rationale | Alternatives Considered |
|----|----------|-----------|------------------------|
| D-1 | Use LangGraph for SDLC state machine | Provides directed graph semantics with built-in state management; existing CLI can be wrapped | Custom state machine (more effort, less ecosystem); Temporal (heavier infra) |
| D-2 | Wrap LangGraph CLI, don't rewrite | Avoids duplicating existing functionality; reduces maintenance burden | Full TypeScript reimplementation (higher control, much more code) |
| D-3 | Three custom Kilo modes + built-in Orchestrator | Minimizes custom mode proliferation; Orchestrator configured via project rules | Custom Orchestrator mode (unnecessary duplication); more granular modes (fragmentation) |
| D-4 | Hierarchical config: default → project → user | Standard layered config pattern; supports environment-specific overrides | Flat config (simpler but inflexible); database-backed config (overkill) |
| D-5 | Markdown for scanner state and research artifacts | Human-readable, git-friendly, no database dependency | SQLite (structured but opaque); JSON (less readable for humans) |
| D-6 | Single-command bootstrap (`framework bootstrap`) | Reduces onboarding friction; validates entire environment in one pass | Manual setup docs (error-prone); Docker-only (limits flexibility) |
| D-7 | Feature branches for all framework work | Isolates experimental changes; prevents main branch destabilization | Trunk-based development (risky for large framework changes) |
| D-8 | Six focused domain reports + master report | Balances depth with manageable scope; remaining domains covered in master | 12 domain reports (too granular); single monolithic report (too dense) |
| D-9 | Evidence-first completion protocol | Prevents false progress claims; tests/artifacts must exist before done | Self-reported status (unreliable); manual review only (doesn't scale) |

### Open Decisions

| ID | Question | Options | Trade-offs | Recommendation |
|----|----------|---------|------------|----------------|
| O-1 | Which vector DB for agent memory? | Chroma, Pinecone, Weaviate, pgvector | Chroma: simple/local; Pinecone: managed/scalable; pgvector: reuses Postgres | Evaluate based on project's existing infra; default to Chroma for local dev |
| O-2 | Model routing strategy | Static config, dynamic cost-based, capability-based | Static: predictable cost; Dynamic: optimizes per-task; Capability: best quality | Start with static config; add dynamic routing as optimization |
| O-3 | Auto-approval gateway design | Rule-based, ML confidence threshold, hybrid | Rules: deterministic; ML: adaptive but opaque; Hybrid: best of both | Begin rule-based; add confidence scoring incrementally |
| O-4 | Multi-agent conflict resolution | Lock-based, merge-based, queue-based | Locking: simple but blocking; Merge: complex but concurrent; Queue: serialized | Queue-based for initial implementation; add merge support later |
| O-5 | Rollback mechanism on quality gate failure | Automatic git revert, manual intervention, remediation subtask | Auto-revert: clean but may lose partial progress; Subtask: preserves work | Remediation subtask (current approach); add auto-revert for critical failures |
| O-6 | Scanner termination strategy | Time-bounded, resource-bounded, convergence-based | Time: predictable; Resource: cost-efficient; Convergence: thorough | Configurable via `.framework/config.yaml`; default to time-bounded |
| O-7 | Notification framework selection | Apprise, custom webhooks, Slack SDK | Apprise: multi-channel; Custom: minimal deps; Slack: team-focused | Apprise (broad channel support, community-maintained) |

*Sources: Research.md §I.2, §II.5, §VII.20, §VIII.21; start_prompt.md §4.4.5, §4.4.7*

---

## 8. Implementation Roadmap

### Now (Immediate Priorities)

These items unblock all downstream work:

1. **Framework Config Subsystem** — `.framework/config.yaml` + schema + validation
2. **LangGraph CLI Wrapper** — `framework start|status` commands operational
3. **Bootstrap System** — `framework bootstrap` validates environment and installs dependencies
4. **Kilo Custom Modes** — Requirements, Scanner, Review YAML registered
5. **Core Test Harness** — pytest + Playwright configured; CI pipeline runs tests

### Next (Short-Term Goals)

Build on the foundation once Config + CLI + Bootstrap are stable:

6. **Deep Scanner v1** — all 4 passes execute; state persistence works
7. **Waste Detection** — token tracking + cost calculation + threshold alerts
8. **Webhook Integration** — GitHub issue/PR/CI-failure handlers operational
9. **Task Decomposition Engine** — automated breakdown with dependency graphing
10. **Mode Transition Logic** — deterministic Orchestrator → Specialist handoffs
11. **Observability Dashboard** — Langfuse integration for real-time metrics

### Later (Future Enhancements)

Extend and optimize once core framework is production-stable:

12. **Voice/PersonaPlex Integration** — voice command routing, persona switching
13. **Dynamic Model Routing** — cost-aware, capability-based model selection
14. **Multi-Agent Swarming** — parallel agent execution with conflict resolution
15. **Auto-Approval Gateway** — confidence-based autonomous approval
16. **Cross-Repo Agent Orchestration** — multi-repo context, distributed locking
17. **Self-Healing CI/CD** — auto-retry with diagnostic context injection
18. **Reinforcement Learning from Review** — prompt evolution based on code review feedback
19. **Entropy Tracking** — architecture drift detection in evolving codebases
20. **Upstream Contribution Preparation** — code + docs + tests ready for Kilo Code PR

*Sources: start_prompt.md §7.1-7.10; Research.md §9 (prioritization tiers)*

---

## Appendix: Domain Coverage Matrix

All 12 taxonomy domains from Research.md are represented in this report.

| # | Domain | Primary Coverage | Detailed Report |
|---|--------|-----------------|-----------------|
| I | Meta Architecture | §1 (Architecture), §6 (Compliance), §7 (Decisions) | Security: `reports/security_compliance.md`; Performance: `reports/performance_optimization.md` |
| II | Agent & Orchestration | §1 (Orchestration Model), §4 (Workflow Lifecycle) | `reports/orchestration_workflow.md` |
| III | Context, Memory & Intelligence | §5.2 (MCP Servers), §3 (Vector DB) | Master report only |
| IV | Code Intelligence & Exploration | §2.4 (Deep Scanner), §5.2 (CodeGraphContext MCP) | `reports/documentation_knowledge.md` |
| V | SDLC Automation | §4 (Workflow Lifecycle), §6 (Test Coverage) | `reports/testing_validation.md` |
| VI | Data & Infrastructure | §3 (Technology Stack), §2.7 (Bootstrap) | `reports/environment_infrastructure.md` |
| VII | Human Interaction | §7 O-3 (Auto-Approval), §4 (Escalation Checkpoints) | Master report only |
| VIII | Model Management | §7 O-2 (Model Routing) | Master report only |
| IX | Research Discipline | §7 D-8 (Report Structure) | Master report only |
| X | Scaling & Enterprise | §8 Later (#16 Cross-Repo) | Master report only |
| XI | Advanced & Bleeding Edge | §8 Later (#18 RL from Review) | Master report only |
| XII | Meta-Control | §8 Later (#19 Entropy Tracking) | Master report only |
