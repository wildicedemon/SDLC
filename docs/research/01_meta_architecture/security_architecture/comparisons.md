# Security Architecture: Comparative Analysis

## Prompt Injection and Guardrail Approaches

| Approach/Tool | Architecture Pattern | Complexity | Observed Benefits | Risks | Maturity Level |
|---|---|---:|---|---|---|
| Rule-based input filters | Static signatures/deny patterns | Low | Fast, simple, low overhead | High bypass risk via obfuscation | Production |
| Schema-constrained outputs | Structured generation with validators | Medium | Reduces unsafe action formatting | Does not stop intent-level manipulation | Production |
| Model-based guard adjudication | Secondary model evaluates risk | High | Better semantic detection | Added cost/latency; model disagreement | Early/Production |
| LangChain Guardrails | Middleware policy + validation chain | Medium | Practical integration and policy hooks | Coverage depends on policy quality | Production |
| Hybrid layered guardrails | Rules + schemas + model adjudicator | High | Best empirical resilience | Operational complexity | Early/Production |

## Context Poisoning Defenses

| Approach/Tool | Architecture Pattern | Complexity | Observed Benefits | Risks | Maturity Level |
|---|---|---:|---|---|---|
| Source allowlist retrieval | Trust-scoped retrieval sources | Low | Reduces untrusted context ingress | Misses useful external evidence | Production |
| Provenance-tagged context | Metadata labels per retrieved chunk | Medium | Better downstream policy decisions | Label quality variance | Early/Production |
| Context quarantine stage | Isolate suspicious retrieved content | Medium | Limits poisoning blast radius | False positives may reduce utility | Early |
| Roo Code context poisoning guidance | Operational hygiene + boundary controls | Low/Medium | Actionable mitigation practices | Requires disciplined adoption | Production |

## MCP Privilege Isolation Models

| Approach/Tool | Architecture Pattern | Complexity | Observed Benefits | Risks | Maturity Level |
|---|---|---:|---|---|---|
| Broad default capabilities | Open tool access by default | Low | Developer convenience | Severe over-privilege risk | Legacy |
| Per-tool allowlist | Explicit capability assignment | Medium | Strong least-privilege baseline | Policy maintenance overhead | Production |
| Task-scoped ephemeral capabilities | Capabilities minted per run/task | High | Reduced standing privilege | Broker dependency/latency | Early/Production |
| Signed inter-agent intents | Verified message envelopes | High | Better spoofing/tampering resistance | Key management complexity | Early |

## Sandboxing and Egress Controls

| Approach/Tool | Architecture Pattern | Complexity | Observed Benefits | Risks | Maturity Level |
|---|---|---:|---|---|---|
| Container sandbox + seccomp | Isolated runtime with syscall constraints | Medium | Good containment for code execution | Misconfiguration can leak privileges | Production |
| MicroVM sandbox | Stronger isolation boundary | High | Higher containment confidence | Infrastructure overhead | Production |
| Default-deny egress allowlist | Network control-plane restriction | Medium | Blocks exfil/C2 by default | Operational friction for new integrations | Production |
| DNS/protocol policy layer | Domain/protocol-aware egress controls | High | Finer-grained network governance | Maintenance complexity | Early/Production |

## Anti-Hallucination Security Controls

| Approach/Tool | Architecture Pattern | Complexity | Observed Benefits | Risks | Maturity Level |
|---|---|---:|---|---|---|
| Retrieve-verify-act pipeline | Evidence before side effects | Medium | Lower unsafe-action hallucinations | Retrieval dependency quality | Production |
| Confidence-gated execution | Threshold-based action permissions | Medium | Risk-scaled control of side effects | Calibration drift over time | Early/Production |
| Dual-run consistency check | Compare independent generations | High | Better detection of unstable outputs | Double cost/latency | Early |
| OpenCLaw anti-hallucination framing | Legal/compliance-aware confidence controls | Medium | Strong governance-security alignment | Tooling ecosystem still developing | Early |

