# Security Architecture: Patterns and Anti-Patterns

## Security Patterns

### Layered Guardrail Envelope

**Description**: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation.

**When to Use**:
- Any tool-using coding agent
- Multi-agent orchestration with external integrations

**Tradeoffs**:
- **Benefits**: Defense in depth against semantic and syntactic attacks
- **Costs**: Higher latency and operational complexity

---

### Provenance-Tagged Context Ingestion

**Description**: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier.

**When to Use**:
- RAG-heavy coding assistants
- Systems ingesting tickets/docs/web content

**Tradeoffs**:
- **Benefits**: Better poisoning containment and auditability
- **Costs**: Metadata pipeline overhead

---

### Task-Scoped MCP Capability Minting

**Description**: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions.

**When to Use**:
- Environments with many MCP tools
- Sensitive repository/infrastructure actions

**Tradeoffs**:
- **Benefits**: Strong least privilege and reduced compromise blast radius
- **Costs**: Capability broker complexity and potential latency

---

### Sandboxed Execute-and-Validate Loop

**Description**: Execute code/tool actions in isolated runtime, validate outputs and side effects before promotion.

**When to Use**:
- Code generation that can touch filesystem/network
- CI-integrated agent workflows

**Tradeoffs**:
- **Benefits**: Better containment and safer experimentation
- **Costs**: Infrastructure and observability overhead

---

### Default-Deny Egress with Explicit Allowlists

**Description**: Block all outbound network access except approved domains/protocols tied to task policy.

**When to Use**:
- Enterprise environments with strict data controls
- Agent workflows capable of external requests

**Tradeoffs**:
- **Benefits**: Strong exfiltration and C2 resistance
- **Costs**: Integration friction and policy upkeep

---

### Evidence-First Action Gating

**Description**: Require retrieval-backed evidence and confidence thresholds before high-impact actions.

**When to Use**:
- Merge/deploy/scaffold operations
- Security-sensitive code modifications

**Tradeoffs**:
- **Benefits**: Reduced hallucinated side effects
- **Costs**: Extra retrieval/validation latency

---

### Adversarial Regression Suite

**Description**: Continuously test agent workflows with curated adversarial prompts and poisoning scenarios.

**When to Use**:
- Production-grade autonomous coding systems
- Frequent model/tool updates

**Tradeoffs**:
- **Benefits**: Early discovery of security regressions
- **Costs**: Test maintenance and benchmark drift

---

## Anti-Patterns

### Prompt-Only Security

**Description**: Relying on instruction text alone without runtime enforcement boundaries.

**Failure Mode**:
- Easy bypass by injection or tool misuse

**Mitigation**: Add hard policy gates at tool, artifact, and deployment boundaries.

---

### Trusting Retrieved Content as Policy

**Description**: Treating retrieved instructions as authoritative control logic.

**Failure Mode**:
- Context poisoning leads to malicious action sequences

**Mitigation**: Separate policy channel from retrieval channel; enforce provenance-aware trust tiers.

---

### Over-Privileged MCP Defaults

**Description**: Granting broad tool access across all tasks by default.

**Failure Mode**:
- Privilege escalation and lateral movement across tools

**Mitigation**: Task-scoped capabilities with explicit allowlists.

---

### Unsandboxed Code/Tool Execution

**Description**: Running generated code or powerful tools directly in trusted host context.

**Failure Mode**:
- Host compromise, data exfiltration, persistence

**Mitigation**: Isolated execution with constrained mounts, syscalls, and identities.

---

### Open Egress by Default

**Description**: Unrestricted outbound connectivity for agent processes.

**Failure Mode**:
- Exfiltration and attacker callback channels

**Mitigation**: Default-deny egress with domain/protocol allowlisting.

---

### Multi-Layer Hallucination Defense

**Description**: Combine consistency checks, static analysis, execution testing, and human review in a pipeline.

**Pipeline Flow**:
```
Generation → Consistency Check → Static Analysis → Execution Test → Human Review
```

**When to Use**:
- High-stakes production code generation
- Security-sensitive code modifications

**Tradeoffs**:
- **Benefits**: Defense in depth against multiple hallucination types
- **Costs**: Higher latency (100ms-5s per check layer)

*Source: Kimi-Research analysis*

---

### Early Exit with Confidence Gating

**Description**: Generate code, check confidence, and only retrieve/regenerate for low-confidence outputs.

**Pipeline Flow**:
```
Generate → Confidence Check → [High: Output] / [Low: Retrieval + Regenerate]
```

**When to Use**:
- Latency-sensitive applications
- High-volume code generation

**Tradeoffs**:
- **Benefits**: Reduced latency for confident outputs
- **Costs**: May miss subtle hallucinations in seemingly confident outputs

*Source: Kimi-Research analysis*

---

### Multi-Agent Verification Consensus

**Description**: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection.

**Pipeline Flow**:
```
Generator Agent → Critic Agent → Verifier Agent → Consensus
```

**When to Use**:
- Complex reasoning tasks
- Critical infrastructure code

**Tradeoffs**:
- **Benefits**: High precision through cross-validation
- **Costs**: Increased cost and complexity (3x inference)

*Source: Kimi-Research analysis*

---

### Uncertainty-Calibrated Human Escalation

**Description**: Route outputs to human review based on uncertainty quantification thresholds.

**Pipeline Flow**:
```
Generate → Uncertainty Quantification → [Certain: Auto-accept] / [Uncertain: Human Review]
```

**When to Use**:
- Safety-critical systems
- Regulated industries with audit requirements

**Tradeoffs**:
- **Benefits**: Scalable safety with human oversight on edge cases
- **Costs**: Human bottleneck for uncertain outputs

*Source: Kimi-Research analysis*

---

## Anti-Patterns

### Prompt-Only Security

**Description**: Relying on instruction text alone without runtime enforcement boundaries.

**Failure Mode**:
- Easy bypass by injection or tool misuse

**Mitigation**: Add hard policy gates at tool, artifact, and deployment boundaries.

---

### Trusting Retrieved Content as Policy

**Description**: Treating retrieved instructions as authoritative control logic.

**Failure Mode**:
- Context poisoning leads to malicious action sequences

**Mitigation**: Separate policy channel from retrieval channel; enforce provenance-aware trust tiers.

---

### Over-Privileged MCP Defaults

**Description**: Granting broad tool access across all tasks by default.

**Failure Mode**:
- Privilege escalation and lateral movement across tools

**Mitigation**: Task-scoped capabilities with explicit allowlists.

---

### Unsandboxed Code/Tool Execution

**Description**: Running generated code or powerful tools directly in trusted host context.

**Failure Mode**:
- Host compromise, data exfiltration, persistence

**Mitigation**: Isolated execution with constrained mounts, syscalls, and identities.

---

### Open Egress by Default

**Description**: Unrestricted outbound connectivity for agent processes.

**Failure Mode**:
- Exfiltration and attacker callback channels

**Mitigation**: Default-deny egress with domain/protocol allowlisting.

---

### Blind Trust in LLM Output

**Description**: Direct deployment of AI-generated code without verification.

**Failure Mode**:
- 40-45% vulnerability rate in production code
- 19.7% fabricated package recommendations ("slopsquatting")

**Mitigation**: Multi-layer verification pipeline with static analysis and testing.

*Source: Kimi-Research analysis*

---

### Single-Technique Hallucination Defense

**Description**: Using only RAG or only static analysis for hallucination prevention.

**Failure Mode**:
- Each technique has blind spots; RAG cannot eliminate hallucinations alone
- Static analysis misses semantic/logic errors

**Mitigation**: Combine multiple techniques (RAG + Self-Consistency + Static Analysis + UQ).

*Source: Kimi-Research analysis*

---

### Ignoring Confidence Calibration

**Description**: Treating all LLM outputs with equal confidence regardless of uncertainty signals.

**Failure Mode**:
- Overconfidence in incorrect answers
- Instruction tuning causes confidence polarization

**Mitigation**: Implement uncertainty quantification with answer frequency/consistency metrics.

*Source: Kimi-Research analysis*

---

### Inadequate Context Window

**Description**: Not providing sufficient code context for generation tasks.

**Failure Mode**:
- Increased hallucination due to knowledge gaps
- API misuse from missing documentation context

**Mitigation**: Expand context windows with relevant codebase retrieval; use RAG for API documentation.

*Source: Kimi-Research analysis*

---

## Research-Grounded Use Cases

1. **Autonomous PR Bot in Enterprise Monorepo**
   - Layered guardrails + task-scoped MCP + sandboxed execution + evidence-first merges.

2. **Security-Critical Migration Assistant**
   - Provenance-tagged retrieval + confidence-gated actions + human escalation for policy exceptions.

3. **CI-Integrated Agent Toolchain**
   - Adversarial regression suite + signed tool manifests + default-deny egress in pipeline runners.

4. **Knowledge-Heavy Coding Copilot**
   - Context quarantine + trust-scored retrieval + anti-hallucination verification before file writes.

5. **High-Volume Code Generation Pipeline**
   - Early exit with confidence gating + static analysis + automated testing for confident outputs.

6. **Safety-Critical Autonomous Code Agent**
   - Multi-agent verification consensus + uncertainty-calibrated human escalation + full audit trail.

*Source: Kimi-Research analysis*

---

## Additional MCP Security Patterns

*Source: Kimi-Research analysis (MCP Servers Overview)*

### MCP Security Threat Mitigation Pattern

**Description**: Layered security controls addressing the eight major MCP threat categories.

**Threat Categories and Mitigations**:
| Threat | Mitigation |
|--------|------------|
| Authentication & Authorization (Confused Deputy) | OAuth 2.1, per-user tokens, least privilege |
| Credential Exposure & Secrets Management | Secret managers, rotation, encryption |
| Unverified/Malicious Servers (Supply Chain) | Code signing, governance, sandboxing |
| Command Injection & Code Execution | Input validation, parameterized calls |
| Prompt Injection & Indirect Exploits | User confirmation, tool restrictions |
| Malicious Tool Definitions (Tool Poisoning) | Tool approval, version pinning, audits |
| Session Hijacking & API Abuse | Secure session IDs, TLS, rate limiting |
| Denial of Service & Resource Exhaustion | Rate limits, quotas, timeouts |

**When to Use**:
- Any MCP server deployment
- Multi-server agent configurations
- Enterprise AI coding systems

---

### MCP Single-Responsibility Server Pattern

**Description**: Each MCP server focuses on one domain (e.g., GitHub, PostgreSQL, filesystem).

**Benefits**:
- Clear tool boundaries
- Easier security auditing
- Simpler maintenance
- Better composability

**Tradeoffs**:
- More servers to manage
- Potential coordination overhead

---

### MCP Gateway/Aggregator Pattern

**Description**: A single MCP server aggregates multiple backend services.

**Benefits**:
- Reduced client configuration
- Centralized authentication
- Unified rate limiting

**Tradeoffs**:
- Single point of failure
- Expanded attack surface
- Context window overload risk

---

## Additional MCP Anti-Patterns

### MCP God Server

**Description**: Single server exposing too many unrelated tools.

**Failure Mode**:
- Context window overload
- Confused tool selection
- Expanded attack surface
- Difficult maintenance

---

## Additional Security Anti-Patterns

*Source: Kimi-Research analysis (Anti-Patterns Guide)*

### Anti-Pattern: Secret in Prompt

**Description**: Including secrets (API keys, passwords, tokens) in LLM prompts.

**Failure Mode**:
- Secrets in logs
- Secrets in model training data
- Compliance violations

**Mitigation**: Secret redaction and environment isolation. Never include actual secrets in prompts; reference environment variables instead.

**Confidence: HIGH** - Critical security vulnerability.

---

### Anti-Pattern: No Output Filtering

**Description**: Not filtering dangerous LLM outputs before execution.

**Failure Mode**:
- Arbitrary code execution
- Data loss
- System compromise

**Mitigation**: Multi-layer output filtering including dangerous pattern detection, static analysis, and sandboxed execution.

**Confidence: HIGH** - Common attack vector.

---

### Anti-Pattern: Over-Privileged Agents

**Description**: Agents with excessive permissions beyond what's needed for their tasks.

**Failure Mode**:
- Lateral movement if compromised
- Data breaches
- Unauthorized actions

**Mitigation**: Principle of least privilege with explicit allowlists and denylists for filesystem, network, and command access.

**Confidence: HIGH** - Standard security principle frequently violated in agent systems.

**Mitigation**: Split into focused servers; use gateway pattern if aggregation needed.

*Source: Kimi-Research analysis (MCP Servers Overview)*

---

### Tool Description Smells

**Description**: MCP tool descriptions with unclear purpose, missing parameters, or vague return values.

**Prevalence**:
- 56% of tools have unclear purpose
- 43% have missing parameters
- 38% have vague return values
- 62% have insufficient examples

**Failure Mode**:
- Agent misdirection
- Incorrect argument generation
- Unexpected behavior handling

**Mitigation**: Augment descriptions for all components; accept 67% increase in execution steps for 5.85% task success improvement.

*Source: Kimi-Research analysis (MCP Servers Overview)*

