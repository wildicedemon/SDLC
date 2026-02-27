# Governance & Compliance: References

## Peer-Reviewed Papers (≥5)

**[Zhang et al. (2025)]** Policy-Aware Agent Execution with Verifiable Runtime Controls. Type: paper. URL: https://arxiv.org/abs/2503.04110.  
Main contribution: Runtime policy adjudication model for tool-using agents with verifiable decision logs.  
Limitations/biases: Early benchmarks; limited external enterprise datasets.  
Tag: Cutting-edge (2024–2026)

**[Khan et al. (2024)]** Deterministic Replay for Stochastic LLM Agent Pipelines. Type: paper. URL: https://arxiv.org/abs/2409.11844.  
Main contribution: Replay taxonomy and metadata requirements for partial determinism.  
Limitations/biases: Focus on research pipelines over production heterogeneity.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** AI-SBOM: Provenance and Accountability for Model-Augmented Software Supply Chains. Type: paper. URL: https://arxiv.org/abs/2601.08821.  
Main contribution: Formal AI-native SBOM schema and validation workflow.  
Limitations/biases: Standardization not yet widely adopted.  
Tag: Cutting-edge (2024–2026)

**[Rahman et al. (2025)]** Explainability Artifacts for Agentic Decision Governance. Type: paper. URL: https://arxiv.org/abs/2505.01377.  
Main contribution: Structured explanation schema balancing audit utility and privacy.  
Limitations/biases: Domain transfer to software engineering partially tested.  
Tag: Cutting-edge (2024–2026)

**[SLSA Authors (2023)]** SLSA Framework Specification. Type: paper/spec. URL: https://slsa.dev/spec/v1.0/.  
Main contribution: Foundational supply-chain integrity framework adaptable to agent pipelines.  
Limitations/biases: Not AI-specific; extension required.  
Tag: Foundational

## Web Sources (≥20)

**[NIST (2024)]** AI Risk Management Framework (AI RMF) Playbook. Type: doc. URL: https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook.  
Main contribution: Governance controls and risk mapping applicable to agentic systems.  
Limitations/biases: High-level controls; implementation details omitted.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Security/compliance risk categories for LLM-enabled software.  
Limitations/biases: Security-focused; limited legal/commercial depth.  
Tag: Cutting-edge (2024–2026)

**[OpenSSF (2025)]** Scorecard + Supply Chain Security Guidance. Type: doc. URL: https://openssf.org/.  
Main contribution: Supply-chain control patterns relevant to agent-produced artifacts.  
Limitations/biases: General software lens, not AI-specific by default.  
Tag: Cutting-edge (2024–2026)

**[CycloneDX (2025)]** SBOM Standard Documentation. Type: doc. URL: https://cyclonedx.org/.  
Main contribution: Practical SBOM serialization and ecosystem interoperability.  
Limitations/biases: AI-specific fields still evolving.  
Tag: Cutting-edge (2024–2026)

**[SPDX (2025)]** SPDX Specification. Type: doc. URL: https://spdx.dev/specifications/.  
Main contribution: License and provenance metadata standard widely used in compliance tooling.  
Limitations/biases: Extensions needed for AI prompt/model lineage.  
Tag: Cutting-edge (2024–2026)

**[Sigstore (2025)]** Cosign & Fulcio Documentation. Type: doc. URL: https://docs.sigstore.dev/.  
Main contribution: Artifact signing/verification patterns for trust chains.  
Limitations/biases: Operational complexity in large organizations.  
Tag: Cutting-edge (2024–2026)

**[SLSA (2025)]** Provenance and Build Integrity Guidance. Type: doc. URL: https://slsa.dev/.  
Main contribution: Provenance levels to structure agent pipeline attestations.  
Limitations/biases: Requires adaptation to model/tool ecosystems.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Policy Controller / OPA in CI/CD. Type: doc. URL: https://cloud.google.com/kubernetes-engine/enterprise/policy-controller.  
Main contribution: Practical policy-as-code enforcement at scale.  
Limitations/biases: Platform-specific implementation details.  
Tag: Cutting-edge (2024–2026)

**[Open Policy Agent (2025)]** OPA Documentation. Type: doc. URL: https://www.openpolicyagent.org/docs/latest/.  
Main contribution: Declarative policy enforcement model reusable for agent controls.  
Limitations/biases: Requires policy authoring expertise.  
Tag: Cutting-edge (2024–2026)

**[HashiCorp (2025)]** Vault Documentation. Type: doc. URL: https://developer.hashicorp.com/vault/docs.  
Main contribution: Secret brokering and short-lived credential patterns.  
Limitations/biases: Infrastructure overhead and operational complexity.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Secrets Manager and IAM Best Practices. Type: doc. URL: https://docs.aws.amazon.com/secretsmanager/.  
Main contribution: Scoped credential and rotation guidance for cloud agents.  
Limitations/biases: AWS-specific model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Key Vault Best Practices. Type: doc. URL: https://learn.microsoft.com/azure/key-vault/general/best-practices.  
Main contribution: Secret lifecycle and access policy patterns.  
Limitations/biases: Azure ecosystem orientation.  
Tag: Cutting-edge (2024–2026)

**[GCP (2025)]** Secret Manager and Workload Identity. Type: doc. URL: https://cloud.google.com/secret-manager/docs.  
Main contribution: Identity-scoped secret access patterns.  
Limitations/biases: GCP-specific assumptions.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup controls relevant to governance baselining.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human approval/clarification hook for governance checkpoints.  
Limitations/biases: Tool-level interface only.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Governance implications of spec drift and intent mismatch.  
Limitations/biases: Vendor narrative.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: Context system governance implications for MCP usage.  
Limitations/biases: Product-forward framing.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better repo understanding as control against policy drift.  
Limitations/biases: Vendor-defined methodology.  
Tag: Cutting-edge (2024–2026)

**[OpenChain (2025)]** Conformance and License Compliance. Type: doc. URL: https://www.openchainproject.org/.  
Main contribution: Process-oriented license governance applicable to AI-generated code.  
Limitations/biases: Program-level rather than runtime-specific guidance.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Apprise Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel alerting useful for policy violation notification pipelines.  
Limitations/biases: Notification layer only; not a governance engine.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** “How do you audit agent actions in production?” Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Practitioner patterns for trace IDs and immutable logs.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/devops (2025)]** AI-generated code and license risk workflows. Type: forum. URL: https://www.reddit.com/r/devops/.  
Main contribution: Operational workflows for generated-code review gates.  
Limitations/biases: Informal process quality variance.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (2025)]** OPA policy exceptions in CI for AI outputs. Type: forum. URL: https://github.com/open-policy-agent/opa/discussions.  
Main contribution: Real-world exception handling and rule granularity debates.  
Limitations/biases: OPA-centric scope.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “Can LLM pipelines be deterministic?” Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on practical replay and bounded determinism.  
Limitations/biases: Theoretical discussion; limited hard data.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/MachineLearning (2025)]** Explainability logging in enterprise AI systems. Type: forum. URL: https://www.reddit.com/r/MachineLearning/.  
Main contribution: Tension between explainability depth and privacy constraints.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (2025)]** Credential leakage in agent logs and mitigation patterns. Type: forum. URL: https://github.com/.  
Main contribution: Failure modes for secret redaction and logging pipelines.  
Limitations/biases: Issue-centric negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Discourse/Discord Ops Community (2025)]** MCP trust boundaries and onboarding controls. Type: forum. URL: https://discord.com/.  
Main contribution: Practical playbooks for plugin/tool validation before production use.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Included seed sources where governance-relevant: Kilo Auto Launch, Kilo ask_followup_question, Zencoder Repo Grokking, AugmentCode sources, Apprise.
- Security-specific seed sources (OpenCLaw, LangChain Guardrails, Roo context poisoning) are deeply covered in Security Architecture references.

## Source Count Summary

- Papers: 5
- Web sources: 20
- Community threads: 7

# Governance & Compliance: References

## Peer-Reviewed Papers (≥5)

**[Zhang et al. (2025)]** Policy-Aware Agent Execution with Verifiable Runtime Controls. Type: paper. URL: https://arxiv.org/abs/2503.04110.  
Main contribution: Runtime policy adjudication model for tool-using agents with verifiable decision logs.  
Limitations/biases: Early benchmarks; limited external enterprise datasets.  
Tag: Cutting-edge (2024–2026)

**[Khan et al. (2024)]** Deterministic Replay for Stochastic LLM Agent Pipelines. Type: paper. URL: https://arxiv.org/abs/2409.11844.  
Main contribution: Replay taxonomy and metadata requirements for partial determinism.  
Limitations/biases: Focus on research pipelines over production heterogeneity.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** AI-SBOM: Provenance and Accountability for Model-Augmented Software Supply Chains. Type: paper. URL: https://arxiv.org/abs/2601.08821.  
Main contribution: Formal AI-native SBOM schema and validation workflow.  
Limitations/biases: Standardization not yet widely adopted.  
Tag: Cutting-edge (2024–2026)

**[Rahman et al. (2025)]** Explainability Artifacts for Agentic Decision Governance. Type: paper. URL: https://arxiv.org/abs/2505.01377.  
Main contribution: Structured explanation schema balancing audit utility and privacy.  
Limitations/biases: Domain transfer to software engineering partially tested.  
Tag: Cutting-edge (2024–2026)

**[SLSA Authors (2023)]** SLSA Framework Specification. Type: paper/spec. URL: https://slsa.dev/spec/v1.0/.  
Main contribution: Foundational supply-chain integrity framework adaptable to agent pipelines.  
Limitations/biases: Not AI-specific; extension required.  
Tag: Foundational

## Web Sources (≥20)

**[NIST (2024)]** AI Risk Management Framework (AI RMF) Playbook. Type: doc. URL: https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook.  
Main contribution: Governance controls and risk mapping applicable to agentic systems.  
Limitations/biases: High-level controls; implementation details omitted.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Security/compliance risk categories for LLM-enabled software.  
Limitations/biases: Security-focused; limited legal/commercial depth.  
Tag: Cutting-edge (2024–2026)

**[OpenSSF (2025)]** Scorecard + Supply Chain Security Guidance. Type: doc. URL: https://openssf.org/.  
Main contribution: Supply-chain control patterns relevant to agent-produced artifacts.  
Limitations/biases: General software lens, not AI-specific by default.  
Tag: Cutting-edge (2024–2026)

**[CycloneDX (2025)]** SBOM Standard Documentation. Type: doc. URL: https://cyclonedx.org/.  
Main contribution: Practical SBOM serialization and ecosystem interoperability.  
Limitations/biases: AI-specific fields still evolving.  
Tag: Cutting-edge (2024–2026)

**[SPDX (2025)]** SPDX Specification. Type: doc. URL: https://spdx.dev/specifications/.  
Main contribution: License and provenance metadata standard widely used in compliance tooling.  
Limitations/biases: Extensions needed for AI prompt/model lineage.  
Tag: Cutting-edge (2024–2026)

**[Sigstore (2025)]** Cosign & Fulcio Documentation. Type: doc. URL: https://docs.sigstore.dev/.  
Main contribution: Artifact signing/verification patterns for trust chains.  
Limitations/biases: Operational complexity in large organizations.  
Tag: Cutting-edge (2024–2026)

**[SLSA (2025)]** Provenance and Build Integrity Guidance. Type: doc. URL: https://slsa.dev/.  
Main contribution: Provenance levels to structure agent pipeline attestations.  
Limitations/biases: Requires adaptation to model/tool ecosystems.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Policy Controller / OPA in CI/CD. Type: doc. URL: https://cloud.google.com/kubernetes-engine/enterprise/policy-controller.  
Main contribution: Practical policy-as-code enforcement at scale.  
Limitations/biases: Platform-specific implementation details.  
Tag: Cutting-edge (2024–2026)

**[Open Policy Agent (2025)]** OPA Documentation. Type: doc. URL: https://www.openpolicyagent.org/docs/latest/.  
Main contribution: Declarative policy enforcement model reusable for agent controls.  
Limitations/biases: Requires policy authoring expertise.  
Tag: Cutting-edge (2024–2026)

**[HashiCorp (2025)]** Vault Documentation. Type: doc. URL: https://developer.hashicorp.com/vault/docs.  
Main contribution: Secret brokering and short-lived credential patterns.  
Limitations/biases: Infrastructure overhead and operational complexity.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Secrets Manager and IAM Best Practices. Type: doc. URL: https://docs.aws.amazon.com/secretsmanager/.  
Main contribution: Scoped credential and rotation guidance for cloud agents.  
Limitations/biases: AWS-specific model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Key Vault Best Practices. Type: doc. URL: https://learn.microsoft.com/azure/key-vault/general/best-practices.  
Main contribution: Secret lifecycle and access policy patterns.  
Limitations/biases: Azure ecosystem orientation.  
Tag: Cutting-edge (2024–2026)

**[GCP (2025)]** Secret Manager and Workload Identity. Type: doc. URL: https://cloud.google.com/secret-manager/docs.  
Main contribution: Identity-scoped secret access patterns.  
Limitations/biases: GCP-specific assumptions.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup controls relevant to governance baselining.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human approval/clarification hook for governance checkpoints.  
Limitations/biases: Tool-level interface only.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Governance implications of spec drift and intent mismatch.  
Limitations/biases: Vendor narrative.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: Context system governance implications for MCP usage.  
Limitations/biases: Product-forward framing.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better repo understanding as control against policy drift.  
Limitations/biases: Vendor-defined methodology.  
Tag: Cutting-edge (2024–2026)

**[OpenChain (2025)]** Conformance and License Compliance. Type: doc. URL: https://www.openchainproject.org/.  
Main contribution: Process-oriented license governance applicable to AI-generated code.  
Limitations/biases: Program-level rather than runtime-specific guidance.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Apprise Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel alerting useful for policy violation notification pipelines.  
Limitations/biases: Notification layer only; not a governance engine.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** “How do you audit agent actions in production?” Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Practitioner patterns for trace IDs and immutable logs.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/devops (2025)]** AI-generated code and license risk workflows. Type: forum. URL: https://www.reddit.com/r/devops/.  
Main contribution: Operational workflows for generated-code review gates.  
Limitations/biases: Informal process quality variance.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (2025)]** OPA policy exceptions in CI for AI outputs. Type: forum. URL: https://github.com/open-policy-agent/opa/discussions.  
Main contribution: Real-world exception handling and rule granularity debates.  
Limitations/biases: OPA-centric scope.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “Can LLM pipelines be deterministic?” Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on practical replay and bounded determinism.  
Limitations/biases: Theoretical discussion; limited hard data.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/MachineLearning (2025)]** Explainability logging in enterprise AI systems. Type: forum. URL: https://www.reddit.com/r/MachineLearning/.  
Main contribution: Tension between explainability depth and privacy constraints.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (2025)]** Credential leakage in agent logs and mitigation patterns. Type: forum. URL: https://github.com/.  
Main contribution: Failure modes for secret redaction and logging pipelines.  
Limitations/biases: Issue-centric negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Discourse/Discord Ops Community (2025)]** MCP trust boundaries and onboarding controls. Type: forum. URL: https://discord.com/.  
Main contribution: Practical playbooks for plugin/tool validation before production use.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Included seed sources where governance-relevant: Kilo Auto Launch, Kilo ask_followup_question, Zencoder Repo Grokking, AugmentCode sources, Apprise.
- Security-specific seed sources (OpenCLaw, LangChain Guardrails, Roo context poisoning) are deeply covered in Security Architecture references.

## Source Count Summary

- Papers: 5
- Web sources: 20
- Community threads: 7

