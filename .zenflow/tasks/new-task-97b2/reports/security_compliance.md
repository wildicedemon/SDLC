# Domain Report: Security & Compliance

## A. Executive Summary

This report covers security architecture, governance, compliance, and safety requirements for the SDLC Framework. The framework faces a unique threat surface: autonomous agents executing code, managing secrets, invoking MCP servers, and processing external webhooks. Research identifies six critical security domains: prompt injection defense, context poisoning mitigation, MCP privilege isolation, sandboxed execution, secret management, and webhook authentication. Governance requirements include audit trails, deterministic replay, SBOM generation, and supply chain validation. Key gaps include absence of a formal threat model, no runtime sandboxing implementation, and undefined MCP permission boundaries.

*Sources: Research.md §I.3 (Governance & Compliance), §I.4 (Security Architecture); start_prompt.md §4.5 (Safety & Error Handling), §4.4.6 (Webhooks)*

## B. Core Concepts

- **Prompt injection defense**: Adversarial simulation testing to validate agent resilience against malicious prompts *(Research.md §I.4)*
- **Context poisoning mitigation**: Detection and filtering pipelines to prevent corrupted context from propagating *(Research.md §I.4; seed source: Roocode context poisoning docs)*
- **MCP privilege isolation**: Per-server permission boundaries restricting which tools and data each MCP server can access *(Research.md §I.4)*
- **Sandboxed execution**: Network egress restrictions and file permission modeling for agent-executed code *(Research.md §I.4)*
- **Secret handling via environment variables**: Credential vaulting with `${ENV_VAR}` substitution; secrets never stored in config files *(see [Environment Report §F E-6](./environment_infrastructure.md#f-decision-log))*
- **Webhook signature validation**: GitHub webhook requests verified via HMAC-SHA256 signature before processing *(start_prompt.md §4.4.6)*
- **Input validation on all external inputs**: Sanitize webhook payloads, CLI arguments, and API responses before processing *(start_prompt.md §4.5)*
- **Graceful degradation**: Services degrade safely when dependencies are unavailable; no cascading failures *(start_prompt.md §4.5)*
- **Rollback mechanisms**: Data backup before destructive operations; reversible changes where possible *(start_prompt.md §4.5)*
- **Audit trail architecture**: Explainability logging for all agent decisions and actions *(Research.md §I.3)*
- **Deterministic replay**: Reproducibility frameworks enabling re-execution of any workflow from recorded state *(Research.md §I.3)*
- **SBOM generation**: Software Bill of Materials for all framework dependencies *(Research.md §I.3)*
- **Supply chain security**: Dependency validation and license compliance scanning *(Research.md §I.3)*
- **Policy enforcement layer**: Configurable rules defining permitted agent actions and boundaries *(Research.md §I.3)*

## C. Implementation Guidance

### What to Build

| Component | Location | Purpose |
|-----------|----------|---------|
| Input sanitizer | `src/framework/security/input-validator.ts` | Validates and sanitizes all external inputs |
| Webhook authenticator | `src/webhooks/auth.ts` | HMAC-SHA256 signature verification for GitHub webhooks |
| Secret validator | `src/bootstrap/checks/secrets.ts` | Validates API keys exist and are non-empty at bootstrap |
| Error handler | `src/framework/security/error-handler.ts` | Try-catch wrappers, graceful degradation, rollback triggers |
| Audit logger | `src/framework/security/audit-log.ts` | Structured logging of all agent decisions and state changes |
| Policy engine | `src/framework/security/policy.ts` | Configurable rules for permitted agent operations |

### How to Build It

- **Input sanitizer**: Validate webhook payloads against expected JSON schemas; sanitize CLI arguments via allowlist; reject unexpected fields; log rejected inputs for audit *(start_prompt.md §4.5)*
- **Webhook authenticator**: Compute HMAC-SHA256 of request body using webhook secret; compare against `X-Hub-Signature-256` header; reject on mismatch with 401 response *(start_prompt.md §4.4.6)*
- **Secret validator**: At bootstrap, check environment variables `KILO_API_KEY`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`; fail with specific missing-key error message; never log secret values *(start_prompt.md §4.4.7)*
- **Error handler**: Wrap all async operations in try-catch; log full stack traces; report actionable error messages; suggest remediation steps; escalate on repeated failures *(start_prompt.md §4.5)*
- **Audit logger**: Emit structured JSON logs for: task state transitions, mode switches, file modifications, MCP server invocations, cost threshold events; store in `.framework/logs/audit/` with rotation
- **Policy engine**: Load rules from `.framework/config.yaml` security section; enforce: no production deployment without approval, no destructive operations on main branch, no infinite loops without progress checkpoints *(start_prompt.md §2.4)*

### Why This Approach

- Input validation at boundaries prevents malicious data from reaching core logic
- HMAC signature verification is GitHub's standard webhook authentication mechanism
- Environment variable secrets follow twelve-factor app principles and avoid config file exposure
- Structured audit logging enables post-incident analysis and compliance verification
- Policy engine provides configurable guardrails without hard-coding constraints

### Dependencies

- Webhook server must be running to receive GitHub events *(see [Master Report §2.6](../sdlc_framework_master_report.md#26-webhooks--github-integration))*
- Bootstrap must validate secrets before any agent execution *(see [Environment Report §C](./environment_infrastructure.md#c-implementation-guidance))*
- Langfuse integration required for cost-related audit events *(see [Master Report §5.6](../sdlc_framework_master_report.md#56-langfuse-observability))*
- Config subsystem must be loaded before policy engine initializes *(see [Environment Report §C](./environment_infrastructure.md#c-implementation-guidance))*

## D. Validation Criteria

| Criterion | Metric | Method |
|-----------|--------|--------|
| Webhook authentication | Invalid signatures rejected with 401 | Unit test: tampered payload, missing header, valid signature |
| Input sanitization | Malformed payloads rejected before processing | Unit test: invalid JSON, extra fields, XSS patterns |
| Secret validation | Missing keys produce specific error messages | Unit test: mock env with missing/empty keys |
| Error handling | Async failures caught and logged with stack trace | Unit test: mock failing operations, verify log output |
| Graceful degradation | Service unavailability does not crash framework | Integration test: disable MCP server, verify fallback |
| Audit logging | All state transitions produce structured log entries | Integration test: execute workflow, verify log completeness |
| Policy enforcement | Violations blocked with explanatory message | Unit test: attempt prohibited operations, verify rejection |
| Secrets never logged | No secret values appear in any log output | Grep test: scan all log outputs for known key patterns |
| Rollback on failure | Destructive operations reversible | Integration test: simulate failed operation, verify state restored |
| SBOM generation | Dependency list produced with licenses | Script test: run SBOM tool, verify output completeness |

## E. Known Gaps & Risks

| Gap/Risk | Severity | Mitigation |
|----------|----------|------------|
| No formal threat model | High | Security requirements derived from source docs; formal STRIDE/DREAD analysis not performed |
| Runtime sandboxing not implemented | High | Agents execute with full host permissions; container-based isolation deferred *(Research.md §I.4)* |
| MCP permission boundaries undefined | High | No per-server access control list; all MCP servers have full tool access *(Research.md §I.4)* |
| No adversarial prompt testing suite | Medium | Prompt injection defense specified but no test cases or fuzzing harness built |
| Context poisoning detection not built | Medium | Detection pipeline specified in Research.md but not yet designed *(Research.md §I.4)* |
| License compliance scanning absent | Medium | SBOM generation specified but no scanning tool selected *(Research.md §I.3)* |
| Audit log rotation/retention undefined | Low | Logs accumulate without rotation policy; disk exhaustion risk for long-running agents |
| No network egress filtering | Medium | Agents can make arbitrary network requests; no allowlist enforcement *(Research.md §I.4)* |
| Deterministic replay not implemented | Low | Stated as requirement; no recording/replay mechanism built *(Research.md §I.3)* |
| Policy engine rules not defined | Medium | Engine structure planned; specific rule definitions not authored yet |

## F. Decision Log

### Resolved Decisions

| ID | Decision | Rationale |
|----|----------|-----------|
| S-1 | HMAC-SHA256 for webhook authentication | GitHub's standard mechanism; well-documented; prevents payload forgery *(start_prompt.md §4.4.6)* |
| S-2 | Environment variables for secret storage | Twelve-factor pattern; avoids secrets in config files; supported by all CI/CD platforms *(start_prompt.md §4.4.7)* |
| S-3 | Try-catch on all async operations | Prevents unhandled rejections from crashing the framework *(start_prompt.md §4.5)* |
| S-4 | No production deployment without approval | Safety boundary; prevents autonomous agents from pushing to production *(start_prompt.md §2.4)* |
| S-5 | No destructive operations on main branch | Protects codebase integrity; all work via feature branches *(start_prompt.md §2.1)* |
| S-6 | Structured JSON audit logging | Machine-parseable; supports post-incident analysis and compliance queries *(Research.md §I.3)* |

### Open Decisions

| ID | Question | Options | Recommendation |
|----|----------|---------|----------------|
| S-O1 | Sandboxing approach | Docker containers, gVisor, Firecracker, OS-level (AppArmor/SELinux), none initially | Docker containers for agent execution; defer advanced sandboxing |
| S-O2 | MCP privilege model | Per-server ACL, role-based, capability-based, none initially | Per-server ACL tied to mode; e.g., Scanner mode gets CodeGraphContext only |
| S-O3 | SBOM/license scanning tool | Syft, Trivy, FOSSA, custom script | Syft for SBOM generation; Trivy for vulnerability scanning |
| S-O4 | Prompt injection test framework | Custom fuzzing harness, third-party tool (Garak), manual testing | Start with manual adversarial prompts; evaluate Garak for automation |
| S-O5 | Context poisoning detection method | Embedding similarity, token anomaly detection, LLM-based classifier | Embedding similarity as first filter; LLM classifier for flagged items |
| S-O6 | Audit log storage | Local files, centralized logging (ELK/Loki), cloud service | Local files initially; centralized logging when multi-agent scaling begins |
| S-O7 | Network egress policy | Allowlist, denylist, no restrictions initially | Allowlist for known API endpoints; block all other egress in sandboxed mode |

*Cross-references: See [Master Report §6](../sdlc_framework_master_report.md#6-performance--compliance) for security and governance requirements overview; [Environment Report §C](./environment_infrastructure.md#c-implementation-guidance) for secret validation in bootstrap; [Orchestration Report §B](./orchestration_workflow.md#b-core-concepts) for branch isolation policy.*
