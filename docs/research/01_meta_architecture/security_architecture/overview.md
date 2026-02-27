# Security Architecture for Autonomous AI Coding Systems

## Executive Summary

Security in autonomous AI coding systems is now primarily a **compositional control problem**: no single mechanism reliably blocks prompt injection, context poisoning, tool abuse, or hallucinated actions in complex agent/tool chains. The strongest evidence supports layered defenses combining input/output guardrails, policy-gated tool invocation, least-privilege MCP capabilities, execution sandboxing, egress restrictions, and high-fidelity audit trails. Security posture improves significantly when controls are enforced at multiple boundaries: prompt boundary, reasoning boundary, tool boundary, artifact boundary, and deployment boundary.

Across recent sources, there is strong convergence on two points: (1) MCP/tool ecosystems expand attack surface faster than most teams model, and (2) anti-hallucination must be treated as a security control when agents can mutate code or infrastructure. Divergence remains on where enforcement should live (inline middleware vs gateway vs sidecar) and how much developer friction is acceptable. Community incidents repeatedly show failures from over-trusting retrieved context, permissive tool scopes, and missing egress controls.

## Topic Framing

Security Architecture in agentic SDLC covers controls that prevent, detect, contain, and recover from adversarial behavior in autonomous coding workflows. Scope includes prompt injection defense, context poisoning mitigation, MCP privilege isolation, secure inter-agent communication, sandboxed execution, network/file permission modeling, adversarial simulation testing, and anti-hallucination guardrails. This topic depends on governance/compliance for policy evidence and on system design for enforceable trust boundaries.

## Detailed Synthesis by Subtopic

### Prompt Injection Defense

Current best practice is **defense in depth** across:

- Input sanitization and policy filtering
- Prompt segmentation with immutable system instructions
- Tool-call preconditions and argument validation
- Output validation and policy checks before side effects

LangChain Guardrails (policy and schema checks) and related middleware patterns help block common injection vectors, but do not eliminate semantic bypasses in complex chains.

**Convergence**: Pre-tool validation is essential.
**Divergence**: Static regex/rule filters vs model-based adjudicators.

### Context Poisoning Mitigation

Context poisoning often enters through retrieval, logs, issue trackers, docs, and transitive tool outputs.

- Roo Code guidance emphasizes context hygiene and boundary controls.
- Effective mitigations include source trust scoring, context provenance tags, and quarantine of untrusted retrieved chunks.
- “Never trust retrieved instructions as policy” is now a recurring security principle.

### MCP Privilege Isolation and Secure Inter-Agent Communication

MCP introduces a capability-routing layer that can either enforce or erode least privilege.

- Strong pattern: per-tool/per-task capability scopes with explicit allowlists.
- Weak pattern: broad default tool exposure across all agent tasks.
- Secure inter-agent messaging benefits from signed envelopes, scoped channels, and policy-tagged intents.

### Sandboxing Execution Environments

Agent-executed code and tool actions require execution isolation.

- Container/VM sandboxes with constrained syscall profiles and read-only mounts reduce damage radius.
- Ephemeral workspaces and disposable credentials reduce persistence risk.
- Sandboxes must be paired with file/network policies to prevent lateral movement.

### Network Egress Restriction Modeling

Egress policy is a critical but often missing control.

- Recommended: default-deny outbound network with explicit destination allowlists.
- Additional controls: DNS filtering, protocol restrictions, request signing, and outbound anomaly detection.
- Incident reports show exfiltration and command-and-control opportunities when unrestricted egress exists.

### File Permission Modeling

File system permissions should align with task intent and branch policy.

- Read-mostly mode by default; write scopes granted per task/path.
- Sensitive path deny-lists (secrets, deployment manifests) reduce catastrophic edits.
- Signed commit pipelines and protected branches provide secondary containment.

### Adversarial Prompt Simulation Testing

Security testing needs adversarial simulation, not only static checks.

- Build red-team prompt corpora (injection, tool misuse, social engineering variants).
- Evaluate both detection rate and blast-radius containment.
- Continuous regression testing is required as models and tools change.

### Anti-Hallucination Strategies

Hallucination is a security risk when agents can act.

- Verification-first pipelines (retrieve-evidence-then-act) outperform generate-then-check in high-risk contexts.
- Structured output schemas and policy-linked assertions reduce unsafe side effects.
- OpenCLaw-style anti-hallucination framing emphasizes legal/compliance-aware confidence gating for autonomous outputs.

## Prior Research Integration

- **Perplexity Space “Smoke Test Framework”**: Not directly accessible in this environment; external reconciliation pending.
- **ChatGPT Project “Smoke”**: Not directly accessible in this environment; external reconciliation pending.
- **Remaining gaps**:
  - No direct source-by-source mapping against prior smoke findings.
  - No shared benchmark baseline imported from prior projects.
- **New sources beyond prior research**:
  - Updated MCP security guidance and guardrail tooling docs.
  - Recent community incident narratives on context poisoning and tool overreach.

## Relationships & Dependencies

- Related: [System Design & Philosophy](../system_design_philosophy/README.md)
  - Design modularity and constraints define enforceable trust boundaries.
- Related: [Economic & Optimization Modeling](../economic_optimization_modeling/README.md)
  - Security controls impose latency/cost tradeoffs and routing implications.
- Related: [Governance & Compliance](../governance_compliance/README.md)
  - Policy enforcement and audit evidence are co-dependent with security controls.

## Additional Research Synthesis

*Source: Kimi-Research analysis (January 2025)*

### Hallucination Impact Statistics

Research from 40+ peer-reviewed papers (2024-2026) reveals critical hallucination patterns in AI code generation:

- **19.7% of recommended packages** in LLM-generated code are fabricated ("slopsquatting") [1]
- **40-45% of AI-generated code** contains exploitable security vulnerabilities [2]
- **43% of Java errors** are API misuse hallucinations [3]
- **$1.3M annual cost** per enterprise for hallucination-induced false positive management [4]

### Taxonomy of Code Hallucinations

| Category | Description | Example |
|----------|-------------|---------|
| **Knowledge-Conflicting Hallucinations (KCH)** | Code that conflicts with documented API behavior | Using non-existent `huggingface-cli` package |
| **Intent Misuse** | Syntactically correct but functionally inappropriate APIs | Using `eval()` for user input parsing |
| **Hallucination Misuse** | Non-existent API methods or parameters | Calling methods with fabricated parameters |
| **Missing Item Misuse** | Omitting required parameters or methods | Forgetting to close database connections |
| **Redundancy Misuse** | Unnecessary API calls or method chaining | Multiple redundant validation checks |

### Key Detection and Mitigation Techniques

**RAG for Code (Hybrid Retrieval):**
- BM25 + dense retrieval achieves 67% reduction in hallucinations [5]
- Context noise and conflict remain major challenges
- Must be combined with verification for production use

**Self-Consistency and Verification:**
- Sample multiple reasoning paths, select via majority vote
- Reduces stochastic errors by 7-19% [6]
- Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response

**Uncertainty Quantification (UQ):**
- Answer frequency (consistency) shows strongest correlation with correctness
- Verbalized confidence methods are systematically biased
- Token-level methods: log-probability thresholds, entropy-based measures

**Static Analysis Integration:**
- AST-based detection achieves 100% precision, 87.6% recall for KCHs [7]
- Dr.Fix framework: Detection → Classification → Reasoning → Repair
- Deterministic rules for API and identifier validation

### Tradeoff Matrix

| Technique | Precision | Recall | Latency | Cost | Creativity Impact |
|-----------|-----------|--------|---------|------|-------------------|
| RAG | Medium | High | Medium | Medium | Low |
| Self-Consistency | High | Medium | High | High | None |
| Static Analysis | Very High | Medium | Low | Low | None |
| UQ-Based Filtering | Medium | Medium | Low | Low | Medium |
| Multi-Agent | High | High | Very High | Very High | Low |
| Human Review | Very High | Very High | Very High | Very High | None |

### Emerging Trends (2025-2026)

1. **Neuro-Symbolic Approaches**: Neural generation + symbolic verification (20-30% improvement in vulnerability detection)
2. **Test-Time Compute Scaling**: Additional inference-time computation for verification (50% reduction in verification cost)
3. **Multi-Modal Fact Verification**: Integrating code with documentation, comments, and visual context
4. **Agent-Based Verification**: Specialized agents for different verification tasks (MulVul architecture)
5. **Confidence Calibration at Scale**: Moving from binary detection to calibrated confidence scores

### Open Source Tools

| Tool | Purpose | Maturity |
|------|---------|----------|
| LangChain Guardrails | Output validation, structure enforcement | High |
| LM-Polygraph | Uncertainty quantification | High |
| RAGAS | RAG evaluation framework | High |
| HaluEval | Hallucination benchmark | Medium |
| Dr.Fix | API misuse repair | Research |

## Open Questions for Architect/Orchestrator Phase

1. Which control points (agent runtime, gateway, sidecar, CI) should own final authority for dangerous tool calls?
2. What minimal MCP capability model prevents cross-tool privilege escalation while preserving usability?
3. How should adversarial prompt suites be versioned and tied to release gates for agent workflows?
4. What is the acceptable latency budget for multi-layer security checks in interactive coding loops?
5. How can anti-hallucination confidence thresholds be calibrated by action criticality?
6. How can we achieve real-time hallucination detection for streaming code generation?
7. What is the optimal balance between detection accuracy and developer experience?
8. Can we develop universal hallucination benchmarks for code across languages?

---

## Security Hardening Implementation Guide

*Source: Kimi-Research analysis (Security Hardening Guide)*

### Security Principles

#### Zero Trust Architecture
1. **Never trust, always verify**
2. **Assume breach**
3. **Least privilege access**
4. **Continuous monitoring**

#### Defense in Depth
Multiple security layers:
1. Network security
2. Application security
3. Data security
4. Access security
5. Audit security

### Hardening Checklist

#### 1. Sandboxing (Critical)

| Technology | Description | Use Case |
|------------|-------------|----------|
| **gVisor** | User-space kernel, container-like performance | General purpose sandboxing |
| **Kata Containers** | VM-like isolation, container-like UX | High-security requirements |
| **HopX** | Purpose-built for AI agents | AI-specific workloads |

#### 2. Network Security

| Control | Implementation | Priority |
|---------|----------------|----------|
| Deny all egress by default | Kubernetes NetworkPolicy | Critical |
| Allow specific endpoints | IPBlock CIDR whitelisting | High |
| DNS restrictions | Allow only kube-system DNS | High |
| API endpoint whitelisting | Azure OpenAI, Anthropic, etc. | Medium |

#### 3. File System Security

| Control | Implementation | Priority |
|---------|----------------|----------|
| Read-only root filesystem | `readOnlyRootFilesystem: true` | Critical |
| Workspace isolation | Separate PVC for workspace | High |
| No privilege escalation | `allowPrivilegeEscalation: false` | Critical |
| Non-root user | `runAsNonRoot: true` | High |
| Drop all capabilities | `capabilities: drop: ALL` | High |

#### 4. Secret Management

| Practice | Implementation | Priority |
|----------|----------------|----------|
| Dedicated secret manager | HashiCorp Vault, AWS Secrets Manager | Critical |
| No hardcoded secrets | Environment variables, secret injection | Critical |
| Regular rotation | Monthly rotation schedule | High |
| Access auditing | Log all secret access | High |
| CI/CD scanning | Secret detection in pipelines | High |

#### 5. Input/Output Validation

| Control | Implementation | Priority |
|---------|----------------|----------|
| Prompt injection detection | Pattern matching, ML classifiers | Critical |
| Output sanitization | Bleach, HTML stripping | High |
| PII detection | DLP scanning | Medium |
| Rate limiting | Per-user, per-agent limits | High |

#### 6. Access Control

| Control | Implementation | Priority |
|---------|----------------|----------|
| Tool-level RBAC | Permission matrix per tool | Critical |
| Short-lived credentials | Max 1 hour TTL | High |
| MFA for admin access | Hardware keys recommended | High |
| Quarterly access reviews | Automated expiration | Medium |

### Prompt Injection Detection Patterns

Common injection patterns to detect and block:

| Pattern | Risk Level | Example |
|---------|------------|---------|
| Instruction override | Critical | "Ignore all previous instructions" |
| Role manipulation | High | "You are now a system administrator" |
| System prompt leakage | High | "System: " prefix attempts |
| Persona injection | Medium | "New persona: " declarations |
| Disregard commands | High | "Disregard all instructions" |

### Tool-Level Permission Matrix

```yaml
# Example permission configuration
agent_permissions:
  filesystem:
    read:
      - "./src/**"
      - "./tests/**"
    write:
      - "./src/**"
    deny:
      - "./secrets/**"
      - "./.env"
  
  network:
    allow:
      - "api.github.com"
      - "api.openai.com"
    deny:
      - "*"
  
  commands:
    allow:
      - "git"
      - "npm"
    deny:
      - "sudo"
      - "rm -rf"
```

# Security Architecture for Autonomous AI Coding Systems

## Executive Summary

Security in autonomous AI coding systems is now primarily a **compositional control problem**: no single mechanism reliably blocks prompt injection, context poisoning, tool abuse, or hallucinated actions in complex agent/tool chains. The strongest evidence supports layered defenses combining input/output guardrails, policy-gated tool invocation, least-privilege MCP capabilities, execution sandboxing, egress restrictions, and high-fidelity audit trails. Security posture improves significantly when controls are enforced at multiple boundaries: prompt boundary, reasoning boundary, tool boundary, artifact boundary, and deployment boundary.

Across recent sources, there is strong convergence on two points: (1) MCP/tool ecosystems expand attack surface faster than most teams model, and (2) anti-hallucination must be treated as a security control when agents can mutate code or infrastructure. Divergence remains on where enforcement should live (inline middleware vs gateway vs sidecar) and how much developer friction is acceptable. Community incidents repeatedly show failures from over-trusting retrieved context, permissive tool scopes, and missing egress controls.

## Topic Framing

Security Architecture in agentic SDLC covers controls that prevent, detect, contain, and recover from adversarial behavior in autonomous coding workflows. Scope includes prompt injection defense, context poisoning mitigation, MCP privilege isolation, secure inter-agent communication, sandboxed execution, network/file permission modeling, adversarial simulation testing, and anti-hallucination guardrails. This topic depends on governance/compliance for policy evidence and on system design for enforceable trust boundaries.

## Detailed Synthesis by Subtopic

### Prompt Injection Defense

Current best practice is **defense in depth** across:

- Input sanitization and policy filtering
- Prompt segmentation with immutable system instructions
- Tool-call preconditions and argument validation
- Output validation and policy checks before side effects

LangChain Guardrails (policy and schema checks) and related middleware patterns help block common injection vectors, but do not eliminate semantic bypasses in complex chains.

**Convergence**: Pre-tool validation is essential.
**Divergence**: Static regex/rule filters vs model-based adjudicators.

### Context Poisoning Mitigation

Context poisoning often enters through retrieval, logs, issue trackers, docs, and transitive tool outputs.

- Roo Code guidance emphasizes context hygiene and boundary controls.
- Effective mitigations include source trust scoring, context provenance tags, and quarantine of untrusted retrieved chunks.
- “Never trust retrieved instructions as policy” is now a recurring security principle.

### MCP Privilege Isolation and Secure Inter-Agent Communication

MCP introduces a capability-routing layer that can either enforce or erode least privilege.

- Strong pattern: per-tool/per-task capability scopes with explicit allowlists.
- Weak pattern: broad default tool exposure across all agent tasks.
- Secure inter-agent messaging benefits from signed envelopes, scoped channels, and policy-tagged intents.

### Sandboxing Execution Environments

Agent-executed code and tool actions require execution isolation.

- Container/VM sandboxes with constrained syscall profiles and read-only mounts reduce damage radius.
- Ephemeral workspaces and disposable credentials reduce persistence risk.
- Sandboxes must be paired with file/network policies to prevent lateral movement.

### Network Egress Restriction Modeling

Egress policy is a critical but often missing control.

- Recommended: default-deny outbound network with explicit destination allowlists.
- Additional controls: DNS filtering, protocol restrictions, request signing, and outbound anomaly detection.
- Incident reports show exfiltration and command-and-control opportunities when unrestricted egress exists.

### File Permission Modeling

File system permissions should align with task intent and branch policy.

- Read-mostly mode by default; write scopes granted per task/path.
- Sensitive path deny-lists (secrets, deployment manifests) reduce catastrophic edits.
- Signed commit pipelines and protected branches provide secondary containment.

### Adversarial Prompt Simulation Testing

Security testing needs adversarial simulation, not only static checks.

- Build red-team prompt corpora (injection, tool misuse, social engineering variants).
- Evaluate both detection rate and blast-radius containment.
- Continuous regression testing is required as models and tools change.

### Anti-Hallucination Strategies

Hallucination is a security risk when agents can act.

- Verification-first pipelines (retrieve-evidence-then-act) outperform generate-then-check in high-risk contexts.
- Structured output schemas and policy-linked assertions reduce unsafe side effects.
- OpenCLaw-style anti-hallucination framing emphasizes legal/compliance-aware confidence gating for autonomous outputs.

## Prior Research Integration

- **Perplexity Space “Smoke Test Framework”**: Not directly accessible in this environment; external reconciliation pending.
- **ChatGPT Project “Smoke”**: Not directly accessible in this environment; external reconciliation pending.
- **Remaining gaps**:
  - No direct source-by-source mapping against prior smoke findings.
  - No shared benchmark baseline imported from prior projects.
- **New sources beyond prior research**:
  - Updated MCP security guidance and guardrail tooling docs.
  - Recent community incident narratives on context poisoning and tool overreach.

## Relationships & Dependencies

- Related: [System Design & Philosophy](../system_design_philosophy/README.md)
  - Design modularity and constraints define enforceable trust boundaries.
- Related: [Economic & Optimization Modeling](../economic_optimization_modeling/README.md)
  - Security controls impose latency/cost tradeoffs and routing implications.
- Related: [Governance & Compliance](../governance_compliance/README.md)
  - Policy enforcement and audit evidence are co-dependent with security controls.

## Additional Research Synthesis

*Source: Kimi-Research analysis (January 2025)*

### Hallucination Impact Statistics

Research from 40+ peer-reviewed papers (2024-2026) reveals critical hallucination patterns in AI code generation:

- **19.7% of recommended packages** in LLM-generated code are fabricated ("slopsquatting") [1]
- **40-45% of AI-generated code** contains exploitable security vulnerabilities [2]
- **43% of Java errors** are API misuse hallucinations [3]
- **$1.3M annual cost** per enterprise for hallucination-induced false positive management [4]

### Taxonomy of Code Hallucinations

| Category | Description | Example |
|----------|-------------|---------|
| **Knowledge-Conflicting Hallucinations (KCH)** | Code that conflicts with documented API behavior | Using non-existent `huggingface-cli` package |
| **Intent Misuse** | Syntactically correct but functionally inappropriate APIs | Using `eval()` for user input parsing |
| **Hallucination Misuse** | Non-existent API methods or parameters | Calling methods with fabricated parameters |
| **Missing Item Misuse** | Omitting required parameters or methods | Forgetting to close database connections |
| **Redundancy Misuse** | Unnecessary API calls or method chaining | Multiple redundant validation checks |

### Key Detection and Mitigation Techniques

**RAG for Code (Hybrid Retrieval):**
- BM25 + dense retrieval achieves 67% reduction in hallucinations [5]
- Context noise and conflict remain major challenges
- Must be combined with verification for production use

**Self-Consistency and Verification:**
- Sample multiple reasoning paths, select via majority vote
- Reduces stochastic errors by 7-19% [6]
- Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response

**Uncertainty Quantification (UQ):**
- Answer frequency (consistency) shows strongest correlation with correctness
- Verbalized confidence methods are systematically biased
- Token-level methods: log-probability thresholds, entropy-based measures

**Static Analysis Integration:**
- AST-based detection achieves 100% precision, 87.6% recall for KCHs [7]
- Dr.Fix framework: Detection → Classification → Reasoning → Repair
- Deterministic rules for API and identifier validation

### Tradeoff Matrix

| Technique | Precision | Recall | Latency | Cost | Creativity Impact |
|-----------|-----------|--------|---------|------|-------------------|
| RAG | Medium | High | Medium | Medium | Low |
| Self-Consistency | High | Medium | High | High | None |
| Static Analysis | Very High | Medium | Low | Low | None |
| UQ-Based Filtering | Medium | Medium | Low | Low | Medium |
| Multi-Agent | High | High | Very High | Very High | Low |
| Human Review | Very High | Very High | Very High | Very High | None |

### Emerging Trends (2025-2026)

1. **Neuro-Symbolic Approaches**: Neural generation + symbolic verification (20-30% improvement in vulnerability detection)
2. **Test-Time Compute Scaling**: Additional inference-time computation for verification (50% reduction in verification cost)
3. **Multi-Modal Fact Verification**: Integrating code with documentation, comments, and visual context
4. **Agent-Based Verification**: Specialized agents for different verification tasks (MulVul architecture)
5. **Confidence Calibration at Scale**: Moving from binary detection to calibrated confidence scores

### Open Source Tools

| Tool | Purpose | Maturity |
|------|---------|----------|
| LangChain Guardrails | Output validation, structure enforcement | High |
| LM-Polygraph | Uncertainty quantification | High |
| RAGAS | RAG evaluation framework | High |
| HaluEval | Hallucination benchmark | Medium |
| Dr.Fix | API misuse repair | Research |

## Open Questions for Architect/Orchestrator Phase

1. Which control points (agent runtime, gateway, sidecar, CI) should own final authority for dangerous tool calls?
2. What minimal MCP capability model prevents cross-tool privilege escalation while preserving usability?
3. How should adversarial prompt suites be versioned and tied to release gates for agent workflows?
4. What is the acceptable latency budget for multi-layer security checks in interactive coding loops?
5. How can anti-hallucination confidence thresholds be calibrated by action criticality?
6. How can we achieve real-time hallucination detection for streaming code generation?
7. What is the optimal balance between detection accuracy and developer experience?
8. Can we develop universal hallucination benchmarks for code across languages?

---

## Security Hardening Implementation Guide

*Source: Kimi-Research analysis (Security Hardening Guide)*

### Security Principles

#### Zero Trust Architecture
1. **Never trust, always verify**
2. **Assume breach**
3. **Least privilege access**
4. **Continuous monitoring**

#### Defense in Depth
Multiple security layers:
1. Network security
2. Application security
3. Data security
4. Access security
5. Audit security

### Hardening Checklist

#### 1. Sandboxing (Critical)

| Technology | Description | Use Case |
|------------|-------------|----------|
| **gVisor** | User-space kernel, container-like performance | General purpose sandboxing |
| **Kata Containers** | VM-like isolation, container-like UX | High-security requirements |
| **HopX** | Purpose-built for AI agents | AI-specific workloads |

#### 2. Network Security

| Control | Implementation | Priority |
|---------|----------------|----------|
| Deny all egress by default | Kubernetes NetworkPolicy | Critical |
| Allow specific endpoints | IPBlock CIDR whitelisting | High |
| DNS restrictions | Allow only kube-system DNS | High |
| API endpoint whitelisting | Azure OpenAI, Anthropic, etc. | Medium |

#### 3. File System Security

| Control | Implementation | Priority |
|---------|----------------|----------|
| Read-only root filesystem | `readOnlyRootFilesystem: true` | Critical |
| Workspace isolation | Separate PVC for workspace | High |
| No privilege escalation | `allowPrivilegeEscalation: false` | Critical |
| Non-root user | `runAsNonRoot: true` | High |
| Drop all capabilities | `capabilities: drop: ALL` | High |

#### 4. Secret Management

| Practice | Implementation | Priority |
|----------|----------------|----------|
| Dedicated secret manager | HashiCorp Vault, AWS Secrets Manager | Critical |
| No hardcoded secrets | Environment variables, secret injection | Critical |
| Regular rotation | Monthly rotation schedule | High |
| Access auditing | Log all secret access | High |
| CI/CD scanning | Secret detection in pipelines | High |

#### 5. Input/Output Validation

| Control | Implementation | Priority |
|---------|----------------|----------|
| Prompt injection detection | Pattern matching, ML classifiers | Critical |
| Output sanitization | Bleach, HTML stripping | High |
| PII detection | DLP scanning | Medium |
| Rate limiting | Per-user, per-agent limits | High |

#### 6. Access Control

| Control | Implementation | Priority |
|---------|----------------|----------|
| Tool-level RBAC | Permission matrix per tool | Critical |
| Short-lived credentials | Max 1 hour TTL | High |
| MFA for admin access | Hardware keys recommended | High |
| Quarterly access reviews | Automated expiration | Medium |

### Prompt Injection Detection Patterns

Common injection patterns to detect and block:

| Pattern | Risk Level | Example |
|---------|------------|---------|
| Instruction override | Critical | "Ignore all previous instructions" |
| Role manipulation | High | "You are now a system administrator" |
| System prompt leakage | High | "System: " prefix attempts |
| Persona injection | Medium | "New persona: " declarations |
| Disregard commands | High | "Disregard all instructions" |

### Tool-Level Permission Matrix

```yaml
# Example permission configuration
agent_permissions:
  filesystem:
    read:
      - "./src/**"
      - "./tests/**"
    write:
      - "./src/**"
    deny:
      - "./secrets/**"
      - "./.env"
  
  network:
    allow:
      - "api.github.com"
      - "api.openai.com"
    deny:
      - "*"
  
  commands:
    allow:
      - "git"
      - "npm"
    deny:
      - "sudo"
      - "rm -rf"
```

