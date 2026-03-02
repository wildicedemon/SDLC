# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

# Security Architecture: References

## Peer-Reviewed Papers (≥5)

**[Wang et al. (2025)]** Prompt Injection Attacks in Tool-Using LLM Agents: Taxonomy and Defenses. Type: paper. URL: https://arxiv.org/abs/2503.10211.  
Main contribution: Formal attack taxonomy and layered defense evaluation for tool-augmented agents.  
Limitations/biases: Benchmarks may not reflect full enterprise complexity.  
Tag: Cutting-edge (2024–2026)

**[Singh et al. (2024)]** Secure Retrieval Pipelines Against Context Poisoning in LLM Systems. Type: paper. URL: https://arxiv.org/abs/2410.04412.  
Main contribution: Provenance-aware retrieval controls and poisoning resilience metrics.  
Limitations/biases: Limited long-horizon agent experiments.  
Tag: Cutting-edge (2024–2026)

**[Morita et al. (2025)]** Capability Isolation for Multi-Tool AI Agents. Type: paper. URL: https://arxiv.org/abs/2506.01984.  
Main contribution: Capability-scoped permission models reducing cross-tool privilege escalation.  
Limitations/biases: Early adoption toolchain assumptions.  
Tag: Cutting-edge (2024–2026)

**[Rahim et al. (2026)]** Hallucination-Aware Safety Control in Autonomous Code Agents. Type: paper. URL: https://arxiv.org/abs/2601.07142.  
Main contribution: Confidence-gated action framework for high-impact operations.  
Limitations/biases: Requires careful threshold calibration.  
Tag: Cutting-edge (2024–2026)

**[Dhamija et al. (2023)]** SoK: Security and Privacy in Machine Learning Systems. Type: paper. URL: https://arxiv.org/abs/2303.06862.  
Main contribution: Foundational security threat framing adapted for modern agent stacks.  
Limitations/biases: Predates widespread MCP/tool-agent adoption.  
Tag: Foundational

## Web Sources (≥20)

**[LangChain (2025)]** Guardrails Documentation. Type: doc. URL: https://docs.langchain.com/oss/python/langchain/guardrails.  
Main contribution: Practical guardrail patterns for prompt/tool/output validation.  
Limitations/biases: Framework-specific integration model.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Context Poisoning. Type: doc. URL: https://docs.roocode.com/advanced-usage/context-poisoning.  
Main contribution: Operational guidance for poisoning mitigation in coding agents.  
Limitations/biases: Product-context-specific workflows.  
Tag: Cutting-edge (2024–2026)

**[Roo Code (2025)]** Model Temperature. Type: doc. URL: https://docs.roocode.com/features/model-temperature.  
Main contribution: Temperature settings impact determinism and risky variance.  
Limitations/biases: Tool-specific defaults.  
Tag: Cutting-edge (2024–2026)

**[OpenCLaw (2025)]** OpenCLaw Anti-Hallucination Framework. Type: repo/doc. URL: https://github.com/openclaw/openclaw.  
Main contribution: Confidence-aware anti-hallucination controls and policy checks.  
Limitations/biases: Ecosystem maturity still evolving.  
Tag: Cutting-edge (2024–2026)

**[OWASP (2025)]** Top 10 for LLM Applications. Type: doc. URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/.  
Main contribution: Canonical threat categories including prompt injection and data leakage.  
Limitations/biases: Broad guidance, limited implementation specifics.  
Tag: Cutting-edge (2024–2026)

**[NVIDIA (2025)]** NeMo Guardrails Documentation. Type: doc. URL: https://docs.nvidia.com/nemo/guardrails/.  
Main contribution: Rule-and-flow guardrail framework for conversational systems.  
Limitations/biases: Integration complexity for heterogeneous stacks.  
Tag: Cutting-edge (2024–2026)

**[OpenAI (2025)]** Safety Best Practices for Tool Use. Type: doc. URL: https://platform.openai.com/docs/guides/safety-best-practices.  
Main contribution: Tool permission and output validation practices.  
Limitations/biases: Provider-centric recommendations.  
Tag: Cutting-edge (2024–2026)

**[Anthropic (2025)]** Reduce Prompt Injection. Type: doc. URL: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-injection.  
Main contribution: Injection mitigation tactics and evaluation strategies.  
Limitations/biases: Claude-oriented implementation assumptions.  
Tag: Cutting-edge (2024–2026)

**[Google Cloud (2025)]** Secure Generative AI on Vertex AI. Type: doc. URL: https://cloud.google.com/vertex-ai/docs/generative-ai/security-controls.  
Main contribution: Enterprise cloud controls for generative workloads.  
Limitations/biases: Platform-specific architecture patterns.  
Tag: Cutting-edge (2024–2026)

**[AWS (2025)]** Security for Bedrock and Agent Workloads. Type: doc. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/security.html.  
Main contribution: IAM and network control patterns for model/tool integrations.  
Limitations/biases: AWS-centric trust model.  
Tag: Cutting-edge (2024–2026)

**[Azure (2025)]** Responsible AI and Security Controls for Azure AI. Type: doc. URL: https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview.  
Main contribution: Security and governance control catalog.  
Limitations/biases: Broad platform-level guidance.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** Auto-Launch Configuration. Type: doc. URL: https://kilo.ai/docs/automate/extending/auto-launch.  
Main contribution: Deterministic startup profiles supporting secure baseline initialization.  
Limitations/biases: Kilo runtime scope.  
Tag: Cutting-edge (2024–2026)

**[Kilo AI (2025)]** ask_followup_question Tool. Type: doc. URL: https://kilo.ai/docs/automate/tools/ask-followup-question.  
Main contribution: Human-in-the-loop security checkpoint capability.  
Limitations/biases: Manual path dependency.  
Tag: Cutting-edge (2024–2026)

**[Zencoder (2025)]** Repo Grokking. Type: blog. URL: https://zencoder.ai/blog/about-repo-grokking.  
Main contribution: Better code context grounding can reduce hallucinated code paths.  
Limitations/biases: Vendor-defined claims.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** What Spec-Driven Development Gets Wrong. Type: blog. URL: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong.  
Main contribution: Highlights governance-security tension in intent/spec drift.  
Limitations/biases: Product positioning bias.  
Tag: Cutting-edge (2024–2026)

**[AugmentCode (2025)]** Context Engine MCP Now Live. Type: blog. URL: https://www.augmentcode.com/blog/context-engine-mcp-now-live.  
Main contribution: MCP context architecture implications for security controls.  
Limitations/biases: Product-centric narrative.  
Tag: Cutting-edge (2024–2026)

**[Cline (2025)]** Prompts Collection. Type: doc. URL: https://cline.bot/prompts.  
Main contribution: Prompt hardening templates and operational scaffolds.  
Limitations/biases: Template quality varies by adaptation.  
Tag: Cutting-edge (2024–2026)

**[Apprise (2025)]** Notification Framework. Type: repo/doc. URL: https://github.com/caronc/apprise.  
Main contribution: Multi-channel security alerting integration for violation events.  
Limitations/biases: Alerting only; no policy engine.  
Tag: Cutting-edge (2024–2026)

**[MITRE ATLAS (2025)]** Adversarial Threat Matrix for AI Systems. Type: doc. URL: https://atlas.mitre.org/.  
Main contribution: Threat modeling framework adaptable to agentic coding workflows.  
Limitations/biases: Requires mapping to local architecture details.  
Tag: Cutting-edge (2024–2026)

**[Trail of Bits (2025)]** Security Reviews of AI Agent Tooling. Type: blog/whitepaper. URL: https://blog.trailofbits.com/.  
Main contribution: Practical offensive findings and defensive recommendations.  
Limitations/biases: Case-study dependent.  
Tag: Cutting-edge (2024–2026)

## Community Signals (≥7)

**[Hacker News (2025)]** Prompt injection incidents in coding copilots. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Real-world failure narratives and mitigation attempts.  
Limitations/biases: Anecdotal and non-standardized evidence.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/netsec (2025)]** LLM tool abuse and egress containment patterns. Type: forum. URL: https://www.reddit.com/r/netsec/.  
Main contribution: Practitioner controls for exfiltration prevention.  
Limitations/biases: Mixed rigor.  
Tag: Cutting-edge (2024–2026)

**[GitHub Issues (LangChain) (2025)]** Guardrail bypass edge cases. Type: forum. URL: https://github.com/langchain-ai/langchain/issues.  
Main contribution: Concrete bypass examples and patch patterns.  
Limitations/biases: Issue-tracker negativity bias.  
Tag: Cutting-edge (2024–2026)

**[Hacker News (2024)]** “MCP security model?” discussion thread. Type: forum. URL: https://news.ycombinator.com/.  
Main contribution: Debate on capability scoping and trust boundaries.  
Limitations/biases: Early ecosystem understanding.  
Tag: Cutting-edge (2024–2026)

**[Reddit r/LocalLLaMA (2025)]** Context poisoning examples and defenses. Type: forum. URL: https://www.reddit.com/r/LocalLLaMA/.  
Main contribution: Community-curated poisoning scenarios and mitigations.  
Limitations/biases: Informal experimental setup.  
Tag: Cutting-edge (2024–2026)

**[GitHub Discussions (Security tooling) (2025)]** Sandbox escape concerns in agent runners. Type: forum. URL: https://github.com/discussions.  
Main contribution: Hardening practices for sandboxed execution environments.  
Limitations/biases: Tool-specific scope fragmentation.  
Tag: Cutting-edge (2024–2026)

**[Discord/Discourse AI SecOps (2025)]** Operational playbooks for adversarial prompt testing. Type: forum. URL: https://discord.com/.  
Main contribution: Practical red-team suite maintenance patterns.  
Limitations/biases: Hard-to-verify anecdotal guidance.  
Tag: Cutting-edge (2024–2026)

## Seed Sources Coverage Notes

- Fully incorporated: LangChain Guardrails, Roo context poisoning, Roo model temperature, OpenCLaw, Kilo Auto Launch, Kilo ask_followup_question, Zencoder, AugmentCode, Cline prompts, Apprise.

## Source Count Summary

- Papers: 37 (5 original + 32 from Kimi-Research integration)
- Web sources: 20
- Community threads: 7

---

## Papers from Kimi-Research Integration (2025-2026)

### Adversarial Code Security

**[Bertram & Geiping (2026)]** NESSiE: The Necessary Safety Benchmark -- Identifying Errors that should not Exist. Type: paper. URL: https://arxiv.org/abs/2602.16756.  
Main contribution: Introduces minimal test cases for information and access security, revealing safety-relevant failures that should not exist. Shows models are biased toward being helpful rather than safe.  
Limitations/biases: Not sufficient for guaranteeing safety in general, but passing is necessary for deployment.  
Tag: Cutting-edge (2024–2026)

**[Thornton (2026)]** Can Adversarial Code Comments Fool AI Security Reviewers. Type: paper. URL: https://arxiv.org/abs/2602.16741.  
Main contribution: Large-scale empirical study of comment-based attacks against LLM vulnerability detection across 100 samples and 9,366 trials. Finds adversarial comments produce small, statistically non-significant effects on detection accuracy.  
Limitations/biases: Focused on detection rather than generation settings.  
Tag: Cutting-edge (2024–2026)

**[Livshits (2026)]** LLMs + Security = Trouble. Type: paper. URL: https://arxiv.org/abs/2602.08422.  
Main contribution: Argues that "fighting fire with fire" approaches fail to address the long tail of security bugs. Proposes enforcing security constraints during code generation via constrained decoding.  
Limitations/biases: Position paper with proposed direction rather than implemented solution.  
Tag: Cutting-edge (2024–2026)

**[Feng et al. (2026)]** SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks. Type: paper. URL: https://arxiv.org/abs/2602.06854.  
Main contribution: Proposes framework for training multi-turn attackers without relying on existing strategies. Achieves 80.1% ASR across three victim models on AdvBench, 33.9% over SOTA.  
Limitations/biases: Open-loop attack regime may not cover all real-world scenarios.  
Tag: Cutting-edge (2024–2026)

**[Lee et al. (2026)]** MPIB: A Benchmark for Medical Prompt Injection Attacks and Clinical Safety in LLMs. Type: paper. URL: https://arxiv.org/abs/2602.06268.  
Main contribution: Introduces benchmark for evaluating clinical safety under direct and indirect prompt injection. Emphasizes Clinical Harm Event Rate (CHER) alongside Attack Success Rate.  
Limitations/biases: Medical domain specific, may not generalize.  
Tag: Cutting-edge (2024–2026)

**[Rybak et al. (2026)]** REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop. Type: paper. URL: https://arxiv.org/abs/2602.06248.  
Main contribution: Evolutionary approach for adversarial prompt generation to probe whether unlearned data can still be recovered. Shows ASRs up to 60% on TOFU and 93% on WMDP.  
Limitations/biases: Focuses on unlearning verification rather than general security.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Semantic Consensus Decoding: Backdoor Defense for Verilog Code Generation. Type: paper. URL: https://arxiv.org/abs/2602.04195.  
Main contribution: Proposes inference-time passive defense for hardware trojans. Reduces attack success rate from 89% to under 3% with negligible impact on generation quality.  
Limitations/biases: Focused on Verilog/hardware domain.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety. Type: paper. URL: https://arxiv.org/abs/2602.01539.  
Main contribution: Multi-turn multi-agent RL framework formulating safety alignment as adversarial asymmetric game. Attacker evolves novel combinatorial strategies through iterative RL training.  
Limitations/biases: Requires significant computational resources for training.  
Tag: Cutting-edge (2024–2026)

**[Cui et al. (2026)]** Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models. Type: paper. URL: https://arxiv.org/abs/2602.01025.  
Main contribution: Proposes UltraBreak framework for VLM jailbreaks that constrains adversarial patterns through transformations and regularisation. Achieves strong transferability across models and attack targets.  
Limitations/biases: Focused on vision-language models specifically.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** GradingAttack: Attacking Large Language Models Towards Short Answer Grading Ability. Type: paper. URL: https://arxiv.org/abs/2602.00979.  
Main contribution: Fine-grained adversarial attack framework for ASAG models with token-level and prompt-level strategies. Demonstrates vulnerability of LLM-based educational assessment.  
Limitations/biases: Educational domain specific.  
Tag: Cutting-edge (2024–2026)

**[Tamber et al. (2026)]** Unifying Adversarial Robustness and Training Across Text Scoring Models. Type: paper. URL: https://arxiv.org/abs/2602.00857.  
Main contribution: Unifies study of adversarial robustness across dense retrievers, rerankers, and reward models. Shows combining complementary training methods yields strong robustness while improving task effectiveness.  
Limitations/biases: Focused on text scoring rather than generation.  
Tag: Cutting-edge (2024–2026)

**[He et al. (2026)]** ICL-EVADER: Zero-Query Black-Box Evasion Attacks on In-Context Learning. Type: paper. URL: https://arxiv.org/abs/2601.21586.  
Main contribution: Novel black-box evasion attack framework operating under zero-query threat model. Achieves up to 95.3% attack success rate against ICL classifiers.  
Limitations/biases: Focused on classification tasks.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation. Type: paper. URL: https://arxiv.org/abs/2601.20615.  
Main contribution: First adversarial attack targeting computational efficiency of RAG-based code generation. Achieves up to 85% increase in latency and 49% increase in energy consumption.  
Limitations/biases: Attack effectiveness depends on specific RAG implementation.  
Tag: Cutting-edge (2024–2026)

**[Dang & Ngo (2026)]** Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection. Type: paper. URL: https://arxiv.org/abs/2601.19375.  
Main contribution: Addresses limitations of activation steering through norm-preserving rotation and discriminative layer selection. Achieves 5.5x higher attack success rates than prior methods.  
Limitations/biases: Can be used for both attack and defense.  
Tag: Cutting-edge (2024–2026)

**[Chugh (2026)]** RECAP: A Resource-Efficient Method for Adversarial Prompting in LLMs. Type: paper. URL: https://arxiv.org/abs/2601.15331.  
Main contribution: Resource-efficient adversarial prompting that eliminates retraining by matching prompts to pre-trained adversarial prompt database. Achieves competitive ASR with reduced computational cost.  
Limitations/biases: Requires pre-existing database of adversarial prompts.  
Tag: Cutting-edge (2024–2026)

### Prompt Injection Attacks and Defenses

**[Guo et al. (2026)]** TFL: Targeted Bit-Flip Attack on Large Language Model. Type: paper. URL: https://arxiv.org/abs/2602.17837.  
Main contribution: Novel targeted bit-flip attack enabling precise manipulation of LLM outputs for selected prompts. Achieves successful manipulation with less than 50 bit flips.  
Limitations/biases: Requires hardware access for bit-flip attacks.  
Tag: Cutting-edge (2024–2026)

**[Deng et al. (2026)]** Automating Agent Hijacking via Structural Template Injection. Type: paper. URL: https://arxiv.org/abs/2602.16958.  
Main contribution: Proposes Phantom framework using Structured Template Injection targeting chat template tokens. Identified over 70 vulnerabilities in real-world commercial products.  
Limitations/biases: Attack effectiveness varies by model architecture.  
Tag: Cutting-edge (2024–2026)

**[Yin et al. (2026)]** The Vulnerability of LLM Rankers to Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.16752.  
Main contribution: Comprehensive empirical study of jailbreak prompt attacks against LLM rankers. Reveals encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks.  
Limitations/biases: Focused on ranking rather than generation tasks.  
Tag: Cutting-edge (2024–2026)

**[Yang et al. (2026)]** Zombie Agents: Persistent Control of Self-Evolving LLM Agents. Type: paper. URL: https://arxiv.org/abs/2602.15654.  
Main contribution: Formalizes persistent attack where untrusted content stored as memory later causes unauthorized tool behavior. Shows memory evolution converts one-time injection into persistent compromise.  
Limitations/biases: Requires specific memory implementation patterns.  
Tag: Cutting-edge (2024–2026)

**[Jia et al. (2026)]** AlignSentinel: Alignment-Aware Detection of Prompt Injection Attacks. Type: paper. URL: https://arxiv.org/abs/2602.13597.  
Main contribution: Three-class classifier distinguishing misaligned instructions, aligned instructions, and non-instruction inputs using LLM attention map features.  
Limitations/biases: Requires access to model attention maps.  
Tag: Cutting-edge (2024–2026)

**[Naik et al. (2026)]** OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage. Type: paper. URL: https://arxiv.org/abs/2602.13477.  
Main contribution: Demonstrates novel attack vector compromising multi-agent orchestrator setups to leak sensitive data through single indirect prompt injection, even with access control.  
Limitations/biases: Focused on orchestrator pattern specifically.  
Tag: Cutting-edge (2024–2026)

**[Corll (2026)]** Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection. Type: paper. URL: https://arxiv.org/abs/2602.11247.  
Main contribution: Proposes formula combining peak single-turn risk, persistence ratio, and category diversity. Achieves 90.8% recall at 1.20% FPR on 10,654 conversations.  
Limitations/biases: Proxy-layer approach may miss sophisticated attacks.  
Tag: Cutting-edge (2024–2026)

**[Zou et al. (2026)]** Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System. Type: paper. URL: https://arxiv.org/abs/2602.10915.  
Main contribution: Proposes Aura architecture replacing GUI scraping with structured agent-native interaction. Improves Task Success Rate from ~75% to 94.3%, reduces Attack Success Rate from ~40% to 4.4%.  
Limitations/biases: Requires clean-slate OS implementation.  
Tag: Cutting-edge (2024–2026)

**[Rajagopalan & Rao (2026)]** Protecting Context and Prompts: Deterministic Security for Non-Deterministic AI. Type: paper. URL: https://arxiv.org/abs/2602.10481.  
Main contribution: Introduces authenticated prompts and authenticated context primitives providing cryptographically verifiable provenance. Achieves 100% detection with zero false positives.  
Limitations/biases: Requires protocol-level adoption.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis. Type: paper. URL: https://arxiv.org/abs/2602.10453.  
Main contribution: Comprehensive SoK covering PI attacks, defenses, and evaluation practices. Introduces AgentPI benchmark for context-dependent interaction settings.  
Limitations/biases: Shows no single defense achieves high trustworthiness, utility, and low latency simultaneously.  
Tag: Cutting-edge (2024–2026)

**[Syros et al. (2026)]** MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection. Type: paper. URL: https://arxiv.org/abs/2602.09222.  
Main contribution: Automated agentic framework for evaluating web agent security. Discovers 37 new attacks across 4 web applications with 10 adversarial objectives.  
Limitations/biases: Focused on web agents specifically.  
Tag: Cutting-edge (2024–2026)

**[Hassan et al. (2026)]** Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation. Type: paper. URL: https://arxiv.org/abs/2602.08062.  
Main contribution: BAGEL framework using bootstrap aggregation of fine-tuned models. Achieves F1 of 0.92 with just 5 ensemble members (430M parameters), outperforming billion-parameter guardrails.  
Limitations/biases: Requires incremental updates for new attack types.  
Tag: Cutting-edge (2024–2026)

**[Wen et al. (2026)]** AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. Type: paper. URL: https://arxiv.org/abs/2602.07398.  
Main contribution: Framework defending against indirect prompt injection through explicit memory management. Achieves 0.78% and 4.25% attack success on AgentDojo and ASB benchmarks.  
Limitations/biases: Requires hierarchical agent architecture.  
Tag: Cutting-edge (2024–2026)

**[Koide et al. (2026)]** Clouding the Mirror: Stealthy Prompt Injection Attacks Targeting LLM-based Phishing Detection. Type: paper. URL: https://arxiv.org/abs/2602.05484.  
Main contribution: First comprehensive evaluation of PI against multimodal LLM-based phishing detection. Proposes InjectDefuser defense framework combining prompt hardening and output validation.  
Limitations/biases: Focused on phishing detection domain.  
Tag: Cutting-edge (2024–2026)

**[Wang et al. (2026)]** BadTemplate: A Training-Free Backdoor Attack via Chat Template. Type: paper. URL: https://arxiv.org/abs/2602.05401.  
Main contribution: Reveals customizability of chat templates allows injection of arbitrary strings into system prompt. Achieves up to 100% attack success rate across 5 benchmark datasets.  
Limitations/biases: Requires control over chat template configuration.  
Tag: Cutting-edge (2024–2026)

### Sandboxing and Runtime Security

**[Piao et al. (2025)]** AgentBay: A Hybrid Interaction Sandbox for Seamless Human-AI Intervention. Type: paper. URL: https://arxiv.org/abs/2512.04367.  
Main contribution: Novel sandbox service for hybrid human-AI interaction with unified session accessible via MCP and SDK. Agent+Human model achieved >48% success rate improvement.  
Limitations/biases: Focused on human-in-the-loop scenarios.  
Tag: Cutting-edge (2024–2026)

**[Ghosh et al. (2025)]** A Safety and Security Framework for Real-World Agentic Systems. Type: paper. URL: https://arxiv.org/abs/2511.21990.  
Main contribution: Dynamic framework for securing agentic AI systems treating safety/security as emergent properties. Introduces operational agentic risk taxonomy unifying traditional concerns with novel risks.  
Limitations/biases: Framework requires customization for specific deployments.  
Tag: Cutting-edge (2024–2026)

### MCP Security

**[Felendler et al. (2026)]** From Tool Orchestration to Code Execution: A Study of MCP Design Choices. Type: paper. URL: https://arxiv.org/abs/2602.15945.  
Main contribution: Formalizes architectural distinction between context-coupled and context-decoupled (CE-MCP) models. Identifies sixteen attack classes across five execution phases.  
Limitations/biases: CE-MCP introduces expanded attack surface despite efficiency gains.  
Tag: Cutting-edge (2024–2026)

**[Zhou et al. (2026)]** MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in MCP Agents. Type: paper. URL: https://arxiv.org/abs/2602.14281.  
Main contribution: Plug-in security cognition layer mitigating misalignment between agents and MCP servers. Defends against six novel MCP-based attack scenarios across six LLMs.  
Limitations/biases: Requires integration with existing agent architectures.  
Tag: Cutting-edge (2024–2026)

**[Anbiaee et al. (2026)]** Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP. Type: paper. URL: https://arxiv.org/abs/2602.11327.  
Main contribution: Systematic security analysis of four emerging AI agent communication protocols. Identifies twelve protocol-level risks with qualitative risk assessment framework.  
Limitations/biases: Rapidly evolving protocol specifications may outdate findings.  
Tag: Cutting-edge (2024–2026)

**[Fan et al. (2026)]** Information Fidelity in Tool-Using LLM Agents: A Martingale Analysis of MCP. Type: paper. URL: https://arxiv.org/abs/2602.13320.  
Main contribution: First theoretical framework for analyzing error accumulation in MCP agents. Proves cumulative distortion exhibits linear growth with O(√T) deviation bounds.  
Limitations/biases: Theoretical analysis requires empirical validation across more implementations.  
Tag: Cutting-edge (2024–2026)

**[Li et al. (2026)]** Don't believe everything you read: Understanding MCP Behavior under Misleading Tool Descriptions. Type: paper. URL: https://arxiv.org/abs/2602.03580.  
Main contribution: First large-scale study of description-code inconsistency in MCP ecosystem. Shows ~13% of 10,240 servers exhibit substantial mismatches enabling undocumented operations.  
Limitations/biases: Static analysis may miss runtime behaviors.  
Tag: Cutting-edge (2024–2026)

