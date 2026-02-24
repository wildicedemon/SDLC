# Domain Report: Environment & Infrastructure

## A. Executive Summary

This report covers Docker orchestration, dynamic stack allocation, bootstrap/self-provisioning, port management, health checks, and infrastructure engineering for the SDLC Framework. The framework requires single-command environment setup (`framework bootstrap`) with automated dependency installation, MCP server configuration, and health validation. Key findings show that containerized reproducibility, Git worktree-based parallelism, and resource scaling are essential for reliable multi-agent operation. Critical gaps include GPU orchestration for model serving, cache invalidation strategy, and infrastructure-as-code definitions for the framework itself.

*Sources: Research.md §VI.18-19 (Data & Infrastructure), §V.16 (CI/CD & DevOps); start_prompt.md §4.4.7 (Bootstrap), §4.8 (Self-Provisioning)*

## B. Core Concepts

- **Single-command bootstrap**: `framework bootstrap` performs environment checks, dependency installation, config generation, secret validation, and health checks in one invocation *(start_prompt.md §4.8)*
- **Environment prerequisite validation**: Checks Node.js, Python, Git, VS Code, and Kilo Code extension versions before proceeding *(start_prompt.md §4.4.7)*
- **MCP server provisioning**: Installs and configures CodeGraphContext, rag-memory-mcp, and TaskMaster MCP servers *(start_prompt.md §4.4.7)*
- **Dependency installation chain**: Playwright, LangGraph, Langfuse installed with version locking for reproducibility *(start_prompt.md §4.4.7)*
- **Hierarchical configuration**: Default > project > user override; schema-validated YAML with environment variable substitution *(see [Master Report §2.1](../sdlc_framework_master_report.md#21-framework-config-subsystem))*
- **Git worktree parallelism**: Concurrent agent branches via `git worktree` for isolated parallel execution *(Research.md §II.6)*
- **Docker containerization**: Reproducible build and test environments; Kubernetes standards for agentic systems *(Research.md §V.16)*
- **Infrastructure-as-Code**: Declarative environment definitions for consistent provisioning *(Research.md §V.16)*
- **Resource scaling strategy**: Dynamic allocation of CPU, RAM, and disk based on workload demands *(Research.md §VI.19)*
- **Cold start optimization**: Minimize latency for first-run bootstrap and scanner initialization *(Research.md §VI.19)*
- **Health check protocol**: Post-bootstrap validation confirms all services reachable and functional *(start_prompt.md §4.8)*
- **Directory structure convention**: `.framework/` root for config, scanner state, notes, reuse proposals *(start_prompt.md §4.4.1)*

## C. Implementation Guidance

### What to Build

| Component | Location | Purpose |
|-----------|----------|---------|
| Bootstrap engine | `src/bootstrap/bootstrap.ts` | Orchestrates full environment setup |
| Environment checker | `src/bootstrap/checks/environment.ts` | Validates Node.js, Python, Git, VS Code, Kilo |
| Dependency installer | `src/bootstrap/checks/dependencies.ts` | Installs MCP servers, Playwright, LangGraph, Langfuse |
| Secret validator | `src/bootstrap/checks/secrets.ts` | Validates KILO_API_KEY, provider API keys |
| Config writer | `src/bootstrap/config-writer.ts` | Generates `.framework/` directory and default configs |
| Config subsystem | `src/framework/config.ts` + `src/framework/types.ts` | Hierarchical config load, validate, hot-reload |
| Config schema | `.framework/schema.json` | JSON Schema for `.framework/config.yaml` validation |

### How to Build It

- **Bootstrap engine**: Sequential pipeline: prerequisites > dependencies > MCP config > directory structure > defaults > secrets > health checks > status report *(start_prompt.md §4.8)*
- **Environment checker**: Shell-out to `node --version`, `python --version`, `git --version`; parse semver; fail with actionable error messages on version mismatch
- **Dependency installer**: Use `npm install` / `pip install` with version pinning; verify post-install via import or CLI check
- **MCP server config**: Generate MCP configuration JSON pointing to installed server binaries; validate server connectivity
- **Config subsystem**: Load YAML via `js-yaml`; validate against JSON Schema; merge default < project < user layers; substitute `${ENV_VAR}` patterns; watch for file changes in dev mode *(start_prompt.md §4.4.1)*
- **Health checks**: Ping each MCP server; verify LangGraph CLI responds; confirm Langfuse API reachable; output pass/fail per service

### Why This Approach

- Single-command bootstrap reduces onboarding friction and eliminates manual configuration errors
- Version-locked dependencies ensure reproducibility across environments *(see [Master Report §6 Reproducibility](../sdlc_framework_master_report.md#reproducibility))*
- Hierarchical config allows per-project and per-user customization without modifying defaults
- Health checks catch configuration issues immediately rather than at runtime

### Dependencies

- Node.js >= 18 and Python >= 3.10 must be pre-installed on host
- Git must be available for worktree management
- Network access required for initial dependency download
- Provider API keys (OpenAI, Anthropic) must be set as environment variables
- KILO_API_KEY must be provisioned before bootstrap

## D. Validation Criteria

| Criterion | Metric | Method |
|-----------|--------|--------|
| Bootstrap completes | Exit code 0 with status report | Integration test: `framework bootstrap` |
| Environment checks | All prerequisites detected correctly | Unit test: mock version outputs, verify pass/fail |
| Dependencies installed | All 6 packages available post-install | Integration test: import/CLI check per package |
| MCP servers configured | Config JSON generated and valid | Unit test: schema validation of generated config |
| Secrets validated | Missing keys produce actionable errors | Unit test: mock env with missing keys |
| Health checks | All services respond to ping | Integration test: mock servers, verify connectivity check |
| Config hierarchy | User overrides project overrides default | Unit test: merge logic with layered YAML files |
| Hot reload | Config changes detected without restart | Integration test: file watch triggers reload callback |
| Directory structure | `.framework/` with expected subdirectories | Integration test: verify directory tree post-bootstrap |
| Worktree support | Multiple worktrees can run concurrently | Integration test: create/remove worktree operations |

## E. Known Gaps & Risks

| Gap/Risk | Severity | Mitigation |
|----------|----------|------------|
| No Docker Compose definitions for framework services | Medium | Bootstrap uses local installs; containerization deferred to CI/CD phase |
| GPU orchestration for model serving absent | Low | Not needed for initial delivery; documented for future scaling *(Research.md §VI.19)* |
| Cache invalidation strategy undefined | Medium | No strategy for config cache, dependency cache, or scanner state cache *(Research.md §VI.19)* |
| Infrastructure-as-Code not implemented | Medium | Bootstrap uses imperative scripts; declarative IaC (Terraform/Pulumi) deferred |
| No cross-platform bootstrap testing | Medium | Bootstrap tested on Windows only; macOS/Linux compatibility not verified |
| Sharded vector DB strategy missing | Low | Single-node vector DB sufficient initially; sharding for large codebases deferred *(Research.md §VI.19)* |
| No rollback on failed bootstrap | Medium | Partial install state can leave environment broken; cleanup script not yet designed |
| MCP server version pinning absent | Medium | Server versions not locked; upgrades could break compatibility |
| Cold start optimization not measured | Low | No benchmarks for bootstrap or first-scan latency *(Research.md §VI.19)* |

## F. Decision Log

### Resolved Decisions

| ID | Decision | Rationale |
|----|----------|-----------|
| E-1 | Single-command bootstrap (`framework bootstrap`) | Reduces onboarding to one step; all checks and installs automated *(start_prompt.md §4.8)* |
| E-2 | Hierarchical config (default > project > user) | Standard pattern; allows customization without modifying defaults *(start_prompt.md §4.4.1)* |
| E-3 | YAML config with JSON Schema validation | YAML is human-readable; JSON Schema provides machine validation *(start_prompt.md §4.4.1)* |
| E-4 | Git worktrees for parallel agent execution | Isolates concurrent branches without full clone overhead *(Research.md §II.6)* |
| E-5 | Local installs for initial bootstrap (not Docker) | Simplifies first-run; Docker containers deferred to CI/CD *(start_prompt.md §4.4.7)* |
| E-6 | Environment variable substitution for secrets | Avoids storing secrets in config files; standard twelve-factor pattern *(start_prompt.md §4.4.1)* |

### Open Decisions

| ID | Question | Options | Recommendation |
|----|----------|---------|----------------|
| E-O1 | Docker Compose for local development | Full containerization, partial (MCP servers only), none initially | Partial: containerize MCP servers first; full Docker later |
| E-O2 | IaC tool selection | Terraform, Pulumi, Docker Compose, none initially | Defer; bootstrap scripts sufficient for initial delivery |
| E-O3 | Cross-platform bootstrap support | Windows-first, cross-platform from start, CI-only cross-platform | Windows-first; add CI matrix testing for macOS/Linux |
| E-O4 | Bootstrap rollback strategy | Cleanup script, transactional install, manual cleanup | Implement cleanup script that reverses partial installs |
| E-O5 | MCP server version management | Pin exact versions, pin major versions, latest always | Pin exact versions in bootstrap config; update via explicit command |

*Cross-references: See [Master Report §2.7](../sdlc_framework_master_report.md#27-bootstrap--self-provisioning) for bootstrap component overview; [Master Report §3](../sdlc_framework_master_report.md#3-technology-stack) for full technology stack; [Orchestration Report §C](./orchestration_workflow.md#c-implementation-guidance) for worktree lifecycle in task execution.*
