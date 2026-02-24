# Consolidated Decision Log

This document consolidates all architectural decisions from the SDLC Framework Master Report and six domain reports. Each decision is cross-referenced to its originating report.

---

## Resolved Decisions

| ID | Decision | Rationale | Alternatives Considered | Domain | Source Report |
|----|----------|-----------|------------------------|--------|--------------|
| D-1 | LangGraph for SDLC state machine | Directed graph semantics with built-in state management; existing CLI wrappable | Custom state machine (more effort, less ecosystem); Temporal (heavier infra) | Orchestration | [Master §7](./sdlc_framework_master_report.md#7-critical-decisions), [Orchestration §F](./reports/orchestration_workflow.md#f-decision-log) |
| D-2 | Wrap LangGraph CLI, don't rewrite | Avoids duplicating existing functionality; reduces maintenance burden | Full TypeScript reimplementation (higher control, much more code) | Orchestration | [Master §7](./sdlc_framework_master_report.md#7-critical-decisions), [Orchestration §F](./reports/orchestration_workflow.md#f-decision-log) |
| D-3 | Three custom Kilo modes + built-in Orchestrator | Minimizes mode proliferation; Orchestrator configured via project rules | Custom Orchestrator mode (duplication); more granular modes (fragmentation) | Orchestration | [Master §7](./sdlc_framework_master_report.md#7-critical-decisions), [Orchestration §F](./reports/orchestration_workflow.md#f-decision-log) |
| D-4 | Hierarchical config: default → project → user | Standard layered config pattern; supports environment-specific overrides | Flat config (simpler but inflexible); database-backed config (overkill) | Environment | [Master §7](./sdlc_framework_master_report.md#7-critical-decisions), [Environment §F E-2](./reports/environment_infrastructure.md#f-decision-log) |
| D-5 | Markdown for scanner state and research artifacts | Human-readable, git-friendly, no database dependency | SQLite (structured but opaque); JSON (less readable) | Documentation | [Master §7](./sdlc_framework_master_report.md#7-critical-decisions), [Documentation §F K-4](./reports/documentation_knowledge.md#f-decision-log) |
| D-6 | Single-command bootstrap (`framework bootstrap`) | Reduces onboarding friction; validates environment in one pass | Manual setup docs (error-prone); Docker-only (limits flexibility) | Environment | [Master §7](./sdlc_framework_master_report.md#7-critical-decisions), [Environment §F E-1](./reports/environment_infrastructure.md#f-decision-log) |
| D-7 | Feature branches for all framework work | Isolates experimental changes; prevents main branch destabilization | Trunk-based development (risky for large framework changes) | Orchestration | [Master §7](./sdlc_framework_master_report.md#7-critical-decisions), [Orchestration §F](./reports/orchestration_workflow.md#f-decision-log) |
| D-8 | Six focused domain reports + master report | Balances depth with manageable scope | 12 reports (too granular); single monolithic report (too dense) | Documentation | [Master §7](./sdlc_framework_master_report.md#7-critical-decisions) |
| D-9 | Evidence-first completion protocol | Tests/artifacts must exist before marking done; prevents false progress | Self-reported status (unreliable); manual review only (doesn't scale) | Testing | [Master §7](./sdlc_framework_master_report.md#7-critical-decisions), [Orchestration §F](./reports/orchestration_workflow.md#f-decision-log), [Testing §F](./reports/testing_validation.md#f-decision-log) |
| T-1 | pytest for Python testing | Already in technology stack; well-supported for unit and integration testing | unittest (less expressive); nose2 (less community support) | Testing | [Testing §F](./reports/testing_validation.md#f-decision-log) |
| T-2 | Playwright for E2E testing | Already in dependency list; supports browser and CLI testing | Cypress (browser-only); Selenium (heavier) | Testing | [Testing §F](./reports/testing_validation.md#f-decision-log) |
| T-3 | 80% coverage floor on critical paths | Balances coverage with development velocity; blocks promotion below threshold | 100% (impractical); 60% (insufficient confidence) | Testing | [Testing §F](./reports/testing_validation.md#f-decision-log) |
| T-4 | Quality gates at defined checkpoints | Prevents accumulated debt; enforced every 5 tasks, phase boundaries, and completion | Continuous (too noisy); end-only (too late) | Testing | [Testing §F](./reports/testing_validation.md#f-decision-log) |
| E-1 | Single-command bootstrap | Reduces onboarding to one step; all checks and installs automated | — (see D-6) | Environment | [Environment §F](./reports/environment_infrastructure.md#f-decision-log) |
| E-2 | Hierarchical config (default > project > user) | Standard pattern; allows customization without modifying defaults | — (see D-4) | Environment | [Environment §F](./reports/environment_infrastructure.md#f-decision-log) |
| E-3 | YAML config with JSON Schema validation | YAML is human-readable; JSON Schema provides machine validation | TOML (less tooling); JSON-only (less readable) | Environment | [Environment §F](./reports/environment_infrastructure.md#f-decision-log) |
| E-4 | Git worktrees for parallel agent execution | Isolates concurrent branches without full clone overhead | Separate clones (disk waste); single branch (no parallelism) | Environment | [Environment §F](./reports/environment_infrastructure.md#f-decision-log) |
| E-5 | Local installs for initial bootstrap (not Docker) | Simplifies first-run; Docker containers deferred to CI/CD | Docker-only (steeper first-run); mixed (complexity) | Environment | [Environment §F](./reports/environment_infrastructure.md#f-decision-log) |
| E-6 | Environment variable substitution for secrets | Avoids storing secrets in config files; twelve-factor pattern | Config file secrets (insecure); vault-only (complex setup) | Security | [Environment §F](./reports/environment_infrastructure.md#f-decision-log), [Security §B](./reports/security_compliance.md#b-core-concepts) |
| S-1 | HMAC-SHA256 for webhook authentication | GitHub's standard mechanism; prevents payload forgery | Token-based (less secure); IP allowlist (fragile) | Security | [Security §F](./reports/security_compliance.md#f-decision-log) |
| S-2 | Environment variables for secret storage | Twelve-factor pattern; avoids secrets in config files | Vault (complex); encrypted config (key management overhead) | Security | [Security §F](./reports/security_compliance.md#f-decision-log) |
| S-3 | Try-catch on all async operations | Prevents unhandled rejections from crashing the framework | Global error handler only (misses context); no catching (crashes) | Security | [Security §F](./reports/security_compliance.md#f-decision-log) |
| S-4 | No production deployment without approval | Safety boundary for autonomous agents | Full autonomy (risky); approval on everything (slow) | Security | [Security §F](./reports/security_compliance.md#f-decision-log) |
| S-5 | No destructive operations on main branch | Protects codebase integrity; all work via feature branches | — (see D-7) | Security | [Security §F](./reports/security_compliance.md#f-decision-log) |
| S-6 | Structured JSON audit logging | Machine-parseable; supports post-incident analysis and compliance | Plaintext logs (harder to query); database (heavier) | Security | [Security §F](./reports/security_compliance.md#f-decision-log) |
| P-1 | Langfuse for observability/cost tracking | Already in technology stack; provides dashboard, tracing, cost attribution | Prometheus (no LLM-specific features); custom (high effort) | Performance | [Performance §F](./reports/performance_optimization.md#f-decision-log) |
| P-2 | 15K/30K token thresholds for waste detection | Concrete, enforceable limits; warn first, then pause | Fixed budgets (inflexible); no limits (runaway costs) | Performance | [Performance §F](./reports/performance_optimization.md#f-decision-log) |
| P-3 | Budget enforcement at orchestration checkpoints | Aligns cost control with checkpoint protocol; no separate loop | Continuous monitoring (overhead); end-of-phase only (too late) | Performance | [Performance §F](./reports/performance_optimization.md#f-decision-log) |
| P-4 | Per-task and per-phase cost ledger | Granular attribution; supports real-time alerts and post-hoc analysis | Aggregate-only (no attribution); per-call (too noisy) | Performance | [Performance §F](./reports/performance_optimization.md#f-decision-log) |
| P-5 | Loop detection via repeated error pattern matching | Simple heuristic; catches common stall patterns | ML-based detection (complex); manual monitoring (doesn't scale) | Performance | [Performance §F](./reports/performance_optimization.md#f-decision-log) |
| K-1 | Deferred documentation strategy | Avoids premature specs that drift; docs follow code | Spec-first (drift risk); no docs standard (chaos) | Documentation | [Documentation §F](./reports/documentation_knowledge.md#f-decision-log) |
| K-2 | ADRs for architectural decisions | Lightweight, widely adopted; captures rationale and alternatives | Wiki pages (hard to version); no records (lost context) | Documentation | [Documentation §F](./reports/documentation_knowledge.md#f-decision-log) |
| K-3 | CodeGraphContext MCP for code intelligence | Already a required dependency; provides AST, symbol index, call graphs | Tree-sitter directly (lower level); custom indexer (high effort) | Documentation | [Documentation §F](./reports/documentation_knowledge.md#f-decision-log) |
| K-4 | Markdown for scanner state and repertoire | Human-readable, git-friendly, no database dependency | — (see D-5) | Documentation | [Documentation §F](./reports/documentation_knowledge.md#f-decision-log) |
| K-5 | Documentation as quality gate | Enforces docs before phase promotion; prevents undocumented code | Separate doc review (disconnected); optional docs (inconsistent) | Documentation | [Documentation §F](./reports/documentation_knowledge.md#f-decision-log) |
| K-6 | rag-memory-mcp for agent knowledge retrieval | Persistent memory and semantic search without custom vector DB | Custom vector DB (high effort); file-based search (poor recall) | Documentation | [Documentation §F](./reports/documentation_knowledge.md#f-decision-log) |

---

## Open Decisions

| ID | Question | Options | Trade-offs | Recommendation | Domain | Source Report |
|----|----------|---------|------------|----------------|--------|--------------|
| O-1 | Which vector DB for agent memory? | Chroma, Pinecone, Weaviate, pgvector | Chroma: simple/local; Pinecone: managed/scalable; pgvector: reuses Postgres | Default to Chroma for local dev | Orchestration | [Master §7](./sdlc_framework_master_report.md#open-decisions) |
| O-2 | Model routing strategy | Static config, dynamic cost-based, capability-based | Static: predictable; Dynamic: optimizes per-task; Capability: best quality | Start static; add dynamic later | Performance | [Master §7](./sdlc_framework_master_report.md#open-decisions), [Performance §F P-O1](./reports/performance_optimization.md#f-decision-log) |
| O-3 | Auto-approval gateway design | Rule-based, ML confidence threshold, hybrid | Rules: deterministic; ML: adaptive but opaque; Hybrid: best of both | Begin rule-based; add scoring later | Orchestration | [Master §7](./sdlc_framework_master_report.md#open-decisions) |
| O-4 | Multi-agent conflict resolution | Lock-based, merge-based, queue-based | Locking: simple but blocking; Merge: complex but concurrent; Queue: serialized | Queue-based initially; merge later | Orchestration | [Master §7](./sdlc_framework_master_report.md#open-decisions), [Orchestration §F](./reports/orchestration_workflow.md#f-decision-log) |
| O-5 | Rollback on quality gate failure | Auto git revert, manual, remediation subtask | Auto-revert: clean but may lose progress; Subtask: preserves work | Remediation subtask; auto-revert for critical | Orchestration | [Master §7](./sdlc_framework_master_report.md#open-decisions), [Orchestration §F](./reports/orchestration_workflow.md#f-decision-log) |
| O-6 | Scanner termination strategy | Time-bounded, resource-bounded, convergence-based | Time: predictable; Resource: cost-efficient; Convergence: thorough | Configurable; default time-bounded | Orchestration | [Master §7](./sdlc_framework_master_report.md#open-decisions), [Orchestration §F](./reports/orchestration_workflow.md#f-decision-log) |
| O-7 | Notification framework selection | Apprise, custom webhooks, Slack SDK | Apprise: multi-channel; Custom: minimal deps; Slack: team-focused | Apprise (broad channel support) | Performance | [Master §7](./sdlc_framework_master_report.md#open-decisions), [Performance §F P-O4](./reports/performance_optimization.md#f-decision-log) |
| T-O1 | Mutation testing tool | mutmut (Python), Stryker (TypeScript), none initially | mutmut: Python-native; Stryker: TS-native; none: less cost | Defer; add after core test suites stable | Testing | [Testing §F](./reports/testing_validation.md#f-decision-log) |
| T-O2 | Contract testing approach | Pact, custom schema validation, none initially | Pact: mature but heavy; Schema: lightweight; None: tech debt | Evaluate when inter-service boundaries defined | Testing | [Testing §F](./reports/testing_validation.md#f-decision-log) |
| T-O3 | Automatic test generation strategy | LLM-based, property-based (Hypothesis), manual only | LLM: broad but unreliable; Property: thorough for data; Manual: reliable | Start manual; add property-based for data modules | Testing | [Testing §F](./reports/testing_validation.md#f-decision-log) |
| T-O4 | Performance benchmark tooling | pytest-benchmark, custom scripts, k6 | pytest-benchmark: unit-level; k6: HTTP-focused; custom: flexible | pytest-benchmark for unit; custom for CLI | Testing | [Testing §F](./reports/testing_validation.md#f-decision-log), [Performance §F P-O3](./reports/performance_optimization.md#f-decision-log) |
| E-O1 | Docker Compose for local development | Full containerization, partial (MCP servers only), none | Full: reproducible but heavy; Partial: pragmatic; None: simple | Partial: containerize MCP servers first | Environment | [Environment §F](./reports/environment_infrastructure.md#f-decision-log) |
| E-O2 | IaC tool selection | Terraform, Pulumi, Docker Compose, none initially | Terraform: mature; Pulumi: code-native; None: less complexity | Defer; bootstrap scripts sufficient initially | Environment | [Environment §F](./reports/environment_infrastructure.md#f-decision-log) |
| E-O3 | Cross-platform bootstrap support | Windows-first, cross-platform from start, CI-only | Windows-first: fastest delivery; Cross-platform: wider reach | Windows-first; CI matrix for macOS/Linux | Environment | [Environment §F](./reports/environment_infrastructure.md#f-decision-log) |
| E-O4 | Bootstrap rollback strategy | Cleanup script, transactional install, manual | Cleanup: reliable; Transactional: complex; Manual: error-prone | Cleanup script to reverse partial installs | Environment | [Environment §F](./reports/environment_infrastructure.md#f-decision-log) |
| E-O5 | MCP server version management | Pin exact, pin major, latest always | Exact: reproducible; Major: flexibility; Latest: risky | Pin exact; update via explicit command | Environment | [Environment §F](./reports/environment_infrastructure.md#f-decision-log) |
| S-O1 | Sandboxing approach | Docker, gVisor, Firecracker, OS-level, none | Docker: balanced; gVisor: secure; None: fastest delivery | Docker containers for agent execution; defer advanced | Security | [Security §F](./reports/security_compliance.md#f-decision-log) |
| S-O2 | MCP privilege model | Per-server ACL, role-based, capability-based, none | ACL: granular; Role-based: simpler; None: risky | Per-server ACL tied to mode | Security | [Security §F](./reports/security_compliance.md#f-decision-log) |
| S-O3 | SBOM/license scanning tool | Syft, Trivy, FOSSA, custom | Syft: SBOM-focused; Trivy: vulnerability-focused; FOSSA: commercial | Syft for SBOM; Trivy for vulnerabilities | Security | [Security §F](./reports/security_compliance.md#f-decision-log) |
| S-O4 | Prompt injection test framework | Custom fuzzing, Garak, manual | Custom: tailored; Garak: pre-built; Manual: low effort | Manual first; evaluate Garak for automation | Security | [Security §F](./reports/security_compliance.md#f-decision-log) |
| S-O5 | Context poisoning detection method | Embedding similarity, token anomaly, LLM classifier | Embedding: fast; Anomaly: broad; LLM: accurate but costly | Embedding similarity first; LLM for flagged items | Security | [Security §F](./reports/security_compliance.md#f-decision-log) |
| S-O6 | Audit log storage | Local files, centralized (ELK/Loki), cloud | Local: simple; Centralized: scalable; Cloud: managed | Local initially; centralized at multi-agent scale | Security | [Security §F](./reports/security_compliance.md#f-decision-log) |
| S-O7 | Network egress policy | Allowlist, denylist, no restrictions | Allowlist: secure; Denylist: permissive; None: fastest | Allowlist for known endpoints; block rest in sandbox | Security | [Security §F](./reports/security_compliance.md#f-decision-log) |
| P-O1 | Model routing strategy | Static, dynamic cost-based, capability-based | — (see O-2) | Start static; add dynamic as optimization | Performance | [Performance §F](./reports/performance_optimization.md#f-decision-log) |
| P-O2 | Cache strategy for scanner results | File-hash based, timestamp-based, none | Hash: accurate; Timestamp: simpler; None: wasteful | File-hash; invalidate on content change | Performance | [Performance §F](./reports/performance_optimization.md#f-decision-log) |
| P-O3 | Performance benchmark tooling | pytest-benchmark, custom, k6 | — (see T-O4) | pytest-benchmark for unit; custom for CLI | Performance | [Performance §F](./reports/performance_optimization.md#f-decision-log) |
| P-O4 | Notification delivery for cost alerts | Apprise, Slack webhook, email, log-only | — (see O-7) | Apprise multi-channel; log-only fallback | Performance | [Performance §F](./reports/performance_optimization.md#f-decision-log) |
| P-O5 | Model pricing table maintenance | Manual config, API-fetched, vendor webhook | Manual: simple; API: automatic; Webhook: real-time | Manual initially; automate if model changes frequent | Performance | [Performance §F](./reports/performance_optimization.md#f-decision-log) |
| P-O6 | Cold start optimization targets | Bootstrap <60s, scan <120s, CLI <2s | — | Define after baselines measured; optimize worst first | Performance | [Performance §F](./reports/performance_optimization.md#f-decision-log) |
| K-O1 | API documentation generator | TypeDoc, Sphinx, custom Markdown, none | TypeDoc: TS-native; Sphinx: Python-native; None: deferred | TypeDoc for TS; Sphinx for Python; defer until APIs stable | Documentation | [Documentation §F](./reports/documentation_knowledge.md#f-decision-log) |
| K-O2 | Changelog tooling | conventional-changelog, standard-version, release-please | conventional-changelog: mature; release-please: GitHub-native | conventional-changelog with conventional commits | Documentation | [Documentation §F](./reports/documentation_knowledge.md#f-decision-log) |
| K-O3 | Docstring style for Python | Google, NumPy, Sphinx style | Google: concise; NumPy: detailed; Sphinx: tool-native | Google style (concise, widely adopted) | Documentation | [Documentation §F](./reports/documentation_knowledge.md#f-decision-log) |
| K-O4 | Knowledge graph implementation | Neo4j, NetworkX, custom, defer | Neo4j: powerful; NetworkX: lightweight; Defer: no cost now | Defer; CodeGraphContext MCP sufficient initially | Documentation | [Documentation §F](./reports/documentation_knowledge.md#f-decision-log) |
| K-O5 | Spec-driven vs. deferred docs default | Spec-first, deferred-docs, configurable | Spec-first: thorough upfront; Deferred: avoids drift | Deferred-docs default; configurable override | Documentation | [Documentation §F](./reports/documentation_knowledge.md#f-decision-log) |

---

## Decision Summary by Domain

| Domain | Resolved | Open | Key Resolved IDs | Key Open IDs |
|--------|----------|------|-------------------|--------------|
| Orchestration | 5 | 5 | D-1, D-2, D-3, D-7, D-9 | O-1, O-3, O-4, O-5, O-6 |
| Testing | 4 | 4 | T-1, T-2, T-3, T-4 | T-O1, T-O2, T-O3, T-O4 |
| Environment | 6 | 5 | E-1–E-6 | E-O1–E-O5 |
| Security | 6 | 7 | S-1–S-6 | S-O1–S-O7 |
| Performance | 5 | 6 | P-1–P-5 | P-O1–P-O6 |
| Documentation | 6 | 5 | K-1–K-6 | K-O1–K-O5 |
| **Total** | **32** | **32** | — | — |

*Note: Some open decisions overlap across domains (O-2/P-O1, O-7/P-O4, T-O4/P-O3). Cross-references are noted in the table above. Canonical IDs from the Master Report (O-*) take precedence when duplicated in domain reports.*

---

## Priority Ranking for Open Decisions

Decisions ordered by blocking impact on implementation roadmap.

### High Priority (blocks "Now" roadmap items)

| ID | Question | Blocking |
|----|----------|----------|
| E-O5 | MCP server version management | Bootstrap reproducibility |
| S-O2 | MCP privilege model | MCP server configuration |
| E-O4 | Bootstrap rollback strategy | Bootstrap reliability |

### Medium Priority (blocks "Next" roadmap items)

| ID | Question | Blocking |
|----|----------|----------|
| O-4 | Multi-agent conflict resolution | Scanner + parallel execution |
| O-5 | Rollback on quality gate failure | Quality gate enforcement |
| P-O2 | Cache strategy for scanner results | Scanner performance |
| S-O1 | Sandboxing approach | Agent execution security |
| O-1 | Vector DB for agent memory | rag-memory-mcp configuration |
| O-2 | Model routing strategy | Waste detection optimization |

### Low Priority (blocks "Later" roadmap items or non-blocking)

| ID | Question | Blocking |
|----|----------|----------|
| O-3 | Auto-approval gateway | Later: Auto-Approval Gateway |
| T-O1 | Mutation testing tool | Non-blocking; enhancement |
| K-O4 | Knowledge graph implementation | Later: advanced code intelligence |
| S-O5 | Context poisoning detection | Later: advanced security |
| K-O5 | Spec-driven vs. deferred docs | Non-blocking; default chosen |
