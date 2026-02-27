# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

# Governance & Compliance: Patterns and Anti-Patterns

## Governance Patterns

### Compliance Envelope per Agent Run

**Description**: Every run emits a standardized evidence envelope (policy version, model/tool versions, inputs hash, outputs hash, approvals, and trace IDs).

**When to Use**:
- Regulated environments
- Multi-team incident response
- External audit readiness

**Tradeoffs**:
- **Benefits**: Strong auditability and replay readiness
- **Costs**: Data volume and schema governance overhead

---

### Policy-as-Code with Runtime Adjudication

**Description**: Combine preflight static checks with runtime policy decisions at each sensitive tool boundary.

**When to Use**:
- Tool-using agent workflows
- High-risk code modification pipelines

**Tradeoffs**:
- **Benefits**: Better real-world enforceability than static-only checks
- **Costs**: Runtime latency and policy maintenance burden

---

### Deterministic Control Plane, Stochastic Data Plane

**Description**: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation.

**When to Use**:
- Workflows requiring replay and compliance evidence
- Systems with evolving model providers

**Tradeoffs**:
- **Benefits**: Practical balance between reproducibility and capability
- **Costs**: Partial replay mismatch in generated content

---

### AI-Native SBOM Extension

**Description**: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage.

**When to Use**:
- Enterprise SDLC with legal/security requirements
- Incident investigation and provenance tracing

**Tradeoffs**:
- **Benefits**: Better root-cause analysis and legal posture
- **Costs**: Metadata management complexity

---

### Ephemeral Scoped Credential Broker

**Description**: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker.

**When to Use**:
- MCP-rich environments
- Sensitive repository or infrastructure access

**Tradeoffs**:
- **Benefits**: Reduces standing privilege and leakage impact
- **Costs**: Broker availability and issuance latency dependency

---

### Explainability Record with Policy Context

**Description**: For each consequential action, persist a concise structured rationale tied to policy outcomes and alternatives considered.

**When to Use**:
- Human approval checkpoints
- Compliance-driven deployment gates

**Tradeoffs**:
- **Benefits**: Better accountability and reviewer efficiency
- **Costs**: Authoring/normalization overhead

---

## Anti-Patterns

### Action Logs Without Decision Context

**Description**: Recording what happened but not why.

**Failure Mode**:
- Weak audit defensibility
- Slow incident triage

**Mitigation**: Add structured decision/rationale records tied to each action.

---

### Policy-in-Prompt Only

**Description**: Relying on prompt instructions as the sole enforcement mechanism.

**Failure Mode**:
- Easy bypass under adversarial inputs or tool misuse

**Mitigation**: Enforce policies at runtime boundaries and CI gates.

---

### Long-Lived Shared Credentials

**Description**: Reusing static tokens across agents and workflows.

**Failure Mode**:
- Large blast radius on compromise
- Poor attribution

**Mitigation**: Ephemeral, identity-bound, scoped credentials with auto-revocation.

---

### SBOM Without AI Context

**Description**: Tracking package dependencies only, excluding models/prompts/tools.

**Failure Mode**:
- Incomplete provenance during incidents and legal review

**Mitigation**: Adopt AI-native SBOM fields and provenance attestations.

---

### Replay Claims Without Environment Snapshots

**Description**: Declaring reproducibility without preserving tool responses, retrieval index versions, and runtime image hashes.

**Failure Mode**:
- Non-reproducible postmortems
- Compliance gaps

**Mitigation**: Bundle deterministic replay metadata and artifact snapshots.

---

## Research-Grounded Use Cases

1. **Regulated Code Assistant Rollout**
   - Use compliance envelopes + runtime policy adjudication + human escalation.

2. **License-Sensitive Enterprise Monorepo**
   - Use similarity-based license screening + AI-native SBOM + quarantine stage.

3. **Incident Forensics for Agent-Caused Regression**
   - Use deterministic control-plane replay + signed logs + trace-linked explanations.

4. **Secure MCP Tool Ecosystem**
   - Use signed tool manifests + scoped credential broker + per-tool policy gates.

