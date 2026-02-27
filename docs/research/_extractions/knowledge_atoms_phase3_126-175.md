# Knowledge Atoms - Phase 3 Extraction (KA-126 to KA-175)

**Extraction Date**: 2026-02-24
**Source Files**: 
- `docs/research/01_meta_architecture/security_architecture/overview.md`
- `docs/research/01_meta_architecture/security_architecture/patterns.md`
- `docs/research/05_sdlc_automation/testing_architecture/overview.md`
- `docs/research/05_sdlc_automation/testing_architecture/patterns.md`
- `docs/research/07_human_interaction/human_in_the_loop_systems/overview.md`

---

## KA-126
**TYPE**: METRIC
**CONTENT**: 19.7% of recommended packages in LLM-generated code are fabricated ("slopsquatting"), creating supply chain attack vectors when developers attempt to install non-existent packages.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC10

---

## KA-127
**TYPE**: METRIC
**CONTENT**: 40-45% of AI-generated code contains exploitable security vulnerabilities, making security scanning mandatory for all AI-generated code before deployment.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P4, P5
**PRODUCTS**: PC10

---

## KA-128
**TYPE**: METRIC
**CONTENT**: 43% of Java errors in AI-generated code are API misuse hallucinations, where the code references non-existent methods or incorrect parameters.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P6
**PRODUCTS**: PC10

---

## KA-129
**TYPE**: METRIC
**CONTENT**: $1.3M annual cost per enterprise for hallucination-induced false positive management, quantifying the economic impact of AI code quality issues.
**EVIDENCE_STRENGTH**: MODERATE
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P8
**PRODUCTS**: PC10

---

## KA-130
**TYPE**: TECHNIQUE
**CONTENT**: Hybrid retrieval (BM25 + dense retrieval) achieves 67% reduction in hallucinations for code generation. Must be combined with verification for production use as context noise and conflict remain challenges.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D3, D7
**SDLC_PHASES**: P3
**PRODUCTS**: PC7

---

## KA-131
**TYPE**: TECHNIQUE
**CONTENT**: Self-consistency verification samples multiple reasoning paths and selects via majority vote, reducing stochastic errors by 7-19%. Chain-of-Verification (CoVe) follows: Draft → Plan verification → Answer independently → Generate verified response.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D3, D7
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC10

---

## KA-132
**TYPE**: METRIC
**CONTENT**: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations (KCHs) in code. Dr.Fix framework provides: Detection → Classification → Reasoning → Repair pipeline.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D5, D7
**SDLC_PHASES**: P4, P6
**PRODUCTS**: PC7

---

## KA-133
**TYPE**: TECHNIQUE
**CONTENT**: Neuro-symbolic approaches combining neural generation with symbolic verification achieve 20-30% improvement in vulnerability detection compared to neural-only methods.
**EVIDENCE_STRENGTH**: MODERATE
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D5, D7
**SDLC_PHASES**: P4, P5
**PRODUCTS**: PC10

---

## KA-134
**TYPE**: TECHNIQUE
**CONTENT**: Test-time compute scaling uses additional inference-time computation for verification, achieving 50% reduction in verification cost compared to separate verification passes.
**EVIDENCE_STRENGTH**: MODERATE
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-135
**TYPE**: TOOL
**CONTENT**: Sandbox technology comparison: gVisor (user-space kernel, container-like performance, general purpose), Kata Containers (VM-like isolation, container-like UX, high-security requirements), HopX (purpose-built for AI agents, AI-specific workloads).
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7, D10
**SDLC_PHASES**: P3, P7
**PRODUCTS**: PC9

---

## KA-136
**TYPE**: CONSTRAINT
**CONTENT**: Short-lived credentials must have maximum 1 hour TTL for agent access. Quarterly access reviews with automated expiration are required for compliance.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P7, P8
**PRODUCTS**: PC6

---

## KA-137
**TYPE**: TECHNIQUE
**CONTENT**: Prompt injection detection patterns with risk levels: Critical (instruction override like "Ignore all previous instructions"), High (role manipulation, system prompt leakage, disregard commands), Medium (persona injection). Pattern matching and ML classifiers required.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC6

---

## KA-138
**TYPE**: TECHNIQUE
**CONTENT**: Layered guardrail envelope combines input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks with higher latency tradeoff.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC6

---

## KA-139
**TYPE**: TECHNIQUE
**CONTENT**: Provenance-tagged context ingestion attaches trust/provenance metadata to each retrieved context element and enforces policy by trust tier. Better poisoning containment and auditability with metadata pipeline overhead.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D4, D7
**SDLC_PHASES**: P1, P3
**PRODUCTS**: PC7

---

## KA-140
**TYPE**: TECHNIQUE
**CONTENT**: Task-scoped MCP capability minting issues narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius with capability broker complexity.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3
**PRODUCTS**: PC5

---

## KA-141
**TYPE**: CONSTRAINT
**CONTENT**: Default-deny egress with explicit allowlists blocks all outbound network access except approved domains/protocols tied to task policy. Critical for enterprise environments with strict data controls.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P7
**PRODUCTS**: PC6

---

## KA-142
**TYPE**: TECHNIQUE
**CONTENT**: Evidence-first action gating requires retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects with extra retrieval/validation latency.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P5, P7
**PRODUCTS**: PC6

---

## KA-143
**TYPE**: TECHNIQUE
**CONTENT**: Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Each layer adds 100ms-5s latency but provides defense in depth against multiple hallucination types.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P4, P5
**PRODUCTS**: PC10

---

## KA-144
**TYPE**: TECHNIQUE
**CONTENT**: Early exit with confidence gating: Generate → Confidence Check → [High: Output] / [Low: Retrieval + Regenerate]. Reduces latency for confident outputs but may miss subtle hallucinations in seemingly confident outputs.
**EVIDENCE_STRENGTH**: MODERATE
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC10

---

## KA-145
**TYPE**: TECHNIQUE
**CONTENT**: Multi-agent verification consensus uses specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation but increased cost and complexity (3x inference).
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D1, D7
**SDLC_PHASES**: P4, P5
**PRODUCTS**: PC3

---

## KA-146
**TYPE**: ANTI_PATTERN
**CONTENT**: Prompt-only security relies on instruction text alone without runtime enforcement boundaries. Failure mode: easy bypass by injection or tool misuse. Mitigation: add hard policy gates at tool, artifact, and deployment boundaries.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC6

---

## KA-147
**TYPE**: ANTI_PATTERN
**CONTENT**: Trusting retrieved content as policy treats retrieved instructions as authoritative control logic. Failure mode: context poisoning leads to malicious action sequences. Mitigation: separate policy channel from retrieval channel; enforce provenance-aware trust tiers.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3
**PRODUCTS**: PC6

---

## KA-148
**TYPE**: ANTI_PATTERN
**CONTENT**: Over-privileged MCP defaults grant broad tool access across all tasks by default. Failure mode: privilege escalation and lateral movement across tools. Mitigation: task-scoped capabilities with explicit allowlists.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3
**PRODUCTS**: PC5

---

## KA-149
**TYPE**: ANTI_PATTERN
**CONTENT**: Unsandboxed code/tool execution runs generated code or powerful tools directly in trusted host context. Failure mode: host compromise, data exfiltration, persistence. Mitigation: isolated execution with constrained mounts, syscalls, and identities.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P7
**PRODUCTS**: PC9

---

## KA-150
**TYPE**: ANTI_PATTERN
**CONTENT**: Blind trust in LLM output deploys AI-generated code without verification. Failure mode: 40-45% vulnerability rate in production code, 19.7% fabricated package recommendations. Mitigation: multi-layer verification pipeline with static analysis and testing.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P4, P5
**PRODUCTS**: PC10

---

## KA-151
**TYPE**: ANTI_PATTERN
**CONTENT**: Single-technique hallucination defense uses only RAG or only static analysis. Failure mode: each technique has blind spots; RAG cannot eliminate hallucinations alone, static analysis misses semantic/logic errors. Mitigation: combine RAG + Self-Consistency + Static Analysis + UQ.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-152
**TYPE**: TECHNIQUE
**CONTENT**: MCP security threat mitigation addresses eight categories: Authentication/Authorization (OAuth 2.1, per-user tokens), Credential Exposure (secret managers, rotation), Malicious Servers (code signing, sandboxing), Command Injection (input validation), Prompt Injection (user confirmation), Tool Poisoning (version pinning), Session Hijacking (TLS, rate limiting), DoS (quotas, timeouts).
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P7
**PRODUCTS**: PC5

---

## KA-153
**TYPE**: METRIC
**CONTENT**: Tool description smells prevalence: 56% of MCP tools have unclear purpose, 43% have missing parameters, 38% have vague return values, 62% have insufficient examples. Augmenting descriptions accepts 67% increase in execution steps for 5.85% task success improvement.
**EVIDENCE_STRENGTH**: MODERATE
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3
**PRODUCTS**: PC5

---

## KA-154
**TYPE**: METRIC
**CONTENT**: AI-generated test suites achieve 60-80% coverage but often miss edge cases and boundary conditions that human testers identify. Coverage metrics alone are insufficient for test quality assessment.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-155
**TYPE**: METRIC
**CONTENT**: Well-structured unit tests reduce debugging time by 40-60% and improve code maintainability by 25%. Unit tests provide executable specifications that can be generated alongside code.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4, P6
**PRODUCTS**: PC10

---

## KA-156
**TYPE**: METRIC
**CONTENT**: Contract testing with tools like Pact reduces integration failures by 70% in distributed systems. Contract tests provide clear specifications for API generation in microservices architectures.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-157
**TYPE**: METRIC
**CONTENT**: E2E tests catch 15-25% of defects missed by unit and integration tests, but are 10x more expensive to maintain. AI agents should select critical paths carefully for E2E coverage.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-158
**TYPE**: METRIC
**CONTENT**: BDD with Given-When-Then structure improves stakeholder communication by 50% and provides natural language specifications that AI agents can parse and implement.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P2, P4
**PRODUCTS**: PC4

---

## KA-159
**TYPE**: METRIC
**CONTENT**: Property-based testing finds edge cases 3x more effectively than example-based testing by generating hundreds of test cases automatically. Provides concise way to specify expected behavior through invariants.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-160
**TYPE**: METRIC
**CONTENT**: Fuzzing finds security vulnerabilities 5x more effectively than manual testing. Essential for security-critical code, parsers, and input handling in AI-generated code.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6, D7
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-161
**TYPE**: METRIC
**CONTENT**: Mutation testing correlates with real defect detection at r=0.75, making it a strong predictor of test quality. Mutation scores provide feedback on test suite effectiveness for AI agents.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4, P5
**PRODUCTS**: PC10

---

## KA-162
**TYPE**: METRIC
**CONTENT**: Runtime validation catches 20-30% of defects that escape testing, particularly in production environments. Provides safety nets for AI-generated code through assertions and invariant monitoring.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4, P8
**PRODUCTS**: PC10

---

## KA-163
**TYPE**: METRIC
**CONTENT**: AI-generated tests focus 80% on happy paths, missing critical error handling. Explicit sad path testing requirements are essential for robust AI code generation.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-164
**TYPE**: METRIC
**CONTENT**: Multi-stage testing reduces production incidents by 60% compared to single-stage testing. Staged workflows enable autonomous operation with safety checkpoints.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4, P7
**PRODUCTS**: PC3

---

## KA-165
**TYPE**: METRIC
**CONTENT**: 80% line coverage correlates with 50% defect reduction, but coverage alone is insufficient. MC/DC coverage is required for safety-critical systems (DO-178C).
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-166
**TYPE**: TECHNIQUE
**CONTENT**: Test pyramid proportions for AI agents: ~70% unit tests, ~20% integration tests, ~10% E2E tests. Optimizes for fast feedback while maintaining comprehensive coverage.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/patterns.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-167
**TYPE**: METRIC
**CONTENT**: TDD initial development time increase is 15-35%, but ensures testability of design and provides executable specifications. AI agents can generate tests first as specifications, then implement code to pass them.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/patterns.md
**DOMAINS**: D6
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC10

---

## KA-168
**TYPE**: ANTI_PATTERN
**CONTENT**: Test inversion (more E2E tests than unit tests) creates slow, brittle test suites with long feedback cycles, high maintenance cost, flaky tests, and difficulty isolating failures. AI agents should be constrained to generate tests in pyramid proportions.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/patterns.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-169
**TYPE**: ANTI_PATTERN
**CONTENT**: Happy path bias in AI-generated tests only covers success scenarios, missing error handling and edge cases. Failure mode: production failures on edge cases, poor error handling. AI agents must be explicitly prompted to generate sad path tests.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/patterns.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-170
**TYPE**: ANTI_PATTERN
**CONTENT**: Coverage gaming writes tests to maximize coverage metrics without meaningful verification. Failure mode: high coverage but low quality, false confidence, missed bugs. AI agents should optimize for test quality, not just coverage metrics.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/patterns.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-171
**TYPE**: TECHNIQUE
**CONTENT**: Five autonomy levels for HITL systems: Operator (human directly controls), Collaborator (human and agent work together), Consultant (agent seeks human input), Approver (agent operates autonomously but requires approval for consequential actions), Observer (agent fully autonomous with monitoring only).
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/07_human_interaction/human_in_the_loop_systems/overview.md
**DOMAINS**: D11
**SDLC_PHASES**: P1, P2, P3
**PRODUCTS**: PC3

---

## KA-172
**TYPE**: METRIC
**CONTENT**: Well-designed HITL systems reduce human intervention by 70-80% while improving task success rates. Poorly designed systems create "approval fatigue" that degrades both human experience and system reliability.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/07_human_interaction/human_in_the_loop_systems/overview.md
**DOMAINS**: D11
**SDLC_PHASES**: P3, P5
**PRODUCTS**: PC3

---

## KA-173
**TYPE**: TOOL
**CONTENT**: Apprise notification framework supports 80+ services with unified API across email, chat, SMS, push notifications, and desktop. Enables intelligent routing based on urgency, time, and recipient preferences. Tagging system for service organization (family, devops, critical).
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/07_human_interaction/human_in_the_loop_systems/overview.md
**DOMAINS**: D11
**SDLC_PHASES**: P5, P7
**PRODUCTS**: PC9

---

## KA-174
**TYPE**: TECHNIQUE
**CONTENT**: Cascaded LLM decision frameworks use deferral policies (base model → large model → human) based on confidence scores, achieving 70% cost reduction while maintaining high accuracy.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/07_human_interaction/human_in_the_loop_systems/overview.md
**DOMAINS**: D8, D11
**SDLC_PHASES**: P3
**PRODUCTS**: PC3

---

## KA-175
**TYPE**: METRIC
**CONTENT**: Humans overestimate AI correctness by up to 80 percentage points (belief-performance gap). Calibration monitoring and adjustment over time is required to address proof-belief gaps where confidence exceeds verification capability.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/07_human_interaction/human_in_the_loop_systems/overview.md
**DOMAINS**: D11
**SDLC_PHASES**: P5, P8
**PRODUCTS**: PC10

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total Atoms Extracted | 50 |
| Starting ID | KA-126 |
| Ending ID | KA-175 |

### By Type
| Type | Count |
|------|-------|
| METRIC | 20 |
| TECHNIQUE | 15 |
| ANTI_PATTERN | 9 |
| TOOL | 3 |
| CONSTRAINT | 3 |

### By Evidence Strength
| Strength | Count |
|----------|-------|
| STRONG | 45 |
| MODERATE | 5 |
| WEAK | 0 |

### By Domain
| Domain | Count |
|--------|-------|
| D7: Security & Guardrails | 28 |
| D6: Testing & Validation | 16 |
| D11: Human Interaction | 5 |
| D3: Context & Prompt Engineering | 2 |
| D4: Memory & Knowledge Systems | 1 |
| D5: Code Intelligence | 1 |
| D8: Model Management & Routing | 1 |
| D10: Workspace & Infrastructure | 1 |

### By SDLC Phase
| Phase | Count |
|-------|-------|
| P4: Testing & Verification | 32 |
| P3: Implementation | 26 |
| P5: Code Review | 11 |
| P7: Deployment & Release | 8 |
| P6: Debugging & Error Recovery | 5 |
| P8: Maintenance & Monitoring | 4 |
| P1: Discovery & Onboarding | 3 |
| P2: Planning & Design | 3 |

### By Product
| Product | Count |
|---------|-------|
| PC10: Techniques & Strategies | 28 |
| PC6: Rules | 8 |
| PC3: Workflows | 5 |
| PC5: MCP Configurations | 4 |
| PC7: Context Management Strategies | 4 |
| PC9: Workspace Management | 3 |
| PC4: Prompts | 1 |

**Extraction Date**: 2026-02-24
**Source Files**: 
- `docs/research/01_meta_architecture/security_architecture/overview.md`
- `docs/research/01_meta_architecture/security_architecture/patterns.md`
- `docs/research/05_sdlc_automation/testing_architecture/overview.md`
- `docs/research/05_sdlc_automation/testing_architecture/patterns.md`
- `docs/research/07_human_interaction/human_in_the_loop_systems/overview.md`

---

## KA-126
**TYPE**: METRIC
**CONTENT**: 19.7% of recommended packages in LLM-generated code are fabricated ("slopsquatting"), creating supply chain attack vectors when developers attempt to install non-existent packages.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC10

---

## KA-127
**TYPE**: METRIC
**CONTENT**: 40-45% of AI-generated code contains exploitable security vulnerabilities, making security scanning mandatory for all AI-generated code before deployment.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P4, P5
**PRODUCTS**: PC10

---

## KA-128
**TYPE**: METRIC
**CONTENT**: 43% of Java errors in AI-generated code are API misuse hallucinations, where the code references non-existent methods or incorrect parameters.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P6
**PRODUCTS**: PC10

---

## KA-129
**TYPE**: METRIC
**CONTENT**: $1.3M annual cost per enterprise for hallucination-induced false positive management, quantifying the economic impact of AI code quality issues.
**EVIDENCE_STRENGTH**: MODERATE
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P8
**PRODUCTS**: PC10

---

## KA-130
**TYPE**: TECHNIQUE
**CONTENT**: Hybrid retrieval (BM25 + dense retrieval) achieves 67% reduction in hallucinations for code generation. Must be combined with verification for production use as context noise and conflict remain challenges.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D3, D7
**SDLC_PHASES**: P3
**PRODUCTS**: PC7

---

## KA-131
**TYPE**: TECHNIQUE
**CONTENT**: Self-consistency verification samples multiple reasoning paths and selects via majority vote, reducing stochastic errors by 7-19%. Chain-of-Verification (CoVe) follows: Draft → Plan verification → Answer independently → Generate verified response.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D3, D7
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC10

---

## KA-132
**TYPE**: METRIC
**CONTENT**: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations (KCHs) in code. Dr.Fix framework provides: Detection → Classification → Reasoning → Repair pipeline.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D5, D7
**SDLC_PHASES**: P4, P6
**PRODUCTS**: PC7

---

## KA-133
**TYPE**: TECHNIQUE
**CONTENT**: Neuro-symbolic approaches combining neural generation with symbolic verification achieve 20-30% improvement in vulnerability detection compared to neural-only methods.
**EVIDENCE_STRENGTH**: MODERATE
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D5, D7
**SDLC_PHASES**: P4, P5
**PRODUCTS**: PC10

---

## KA-134
**TYPE**: TECHNIQUE
**CONTENT**: Test-time compute scaling uses additional inference-time computation for verification, achieving 50% reduction in verification cost compared to separate verification passes.
**EVIDENCE_STRENGTH**: MODERATE
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-135
**TYPE**: TOOL
**CONTENT**: Sandbox technology comparison: gVisor (user-space kernel, container-like performance, general purpose), Kata Containers (VM-like isolation, container-like UX, high-security requirements), HopX (purpose-built for AI agents, AI-specific workloads).
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7, D10
**SDLC_PHASES**: P3, P7
**PRODUCTS**: PC9

---

## KA-136
**TYPE**: CONSTRAINT
**CONTENT**: Short-lived credentials must have maximum 1 hour TTL for agent access. Quarterly access reviews with automated expiration are required for compliance.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P7, P8
**PRODUCTS**: PC6

---

## KA-137
**TYPE**: TECHNIQUE
**CONTENT**: Prompt injection detection patterns with risk levels: Critical (instruction override like "Ignore all previous instructions"), High (role manipulation, system prompt leakage, disregard commands), Medium (persona injection). Pattern matching and ML classifiers required.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC6

---

## KA-138
**TYPE**: TECHNIQUE
**CONTENT**: Layered guardrail envelope combines input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks with higher latency tradeoff.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC6

---

## KA-139
**TYPE**: TECHNIQUE
**CONTENT**: Provenance-tagged context ingestion attaches trust/provenance metadata to each retrieved context element and enforces policy by trust tier. Better poisoning containment and auditability with metadata pipeline overhead.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D4, D7
**SDLC_PHASES**: P1, P3
**PRODUCTS**: PC7

---

## KA-140
**TYPE**: TECHNIQUE
**CONTENT**: Task-scoped MCP capability minting issues narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius with capability broker complexity.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3
**PRODUCTS**: PC5

---

## KA-141
**TYPE**: CONSTRAINT
**CONTENT**: Default-deny egress with explicit allowlists blocks all outbound network access except approved domains/protocols tied to task policy. Critical for enterprise environments with strict data controls.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P7
**PRODUCTS**: PC6

---

## KA-142
**TYPE**: TECHNIQUE
**CONTENT**: Evidence-first action gating requires retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects with extra retrieval/validation latency.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P5, P7
**PRODUCTS**: PC6

---

## KA-143
**TYPE**: TECHNIQUE
**CONTENT**: Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Each layer adds 100ms-5s latency but provides defense in depth against multiple hallucination types.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P4, P5
**PRODUCTS**: PC10

---

## KA-144
**TYPE**: TECHNIQUE
**CONTENT**: Early exit with confidence gating: Generate → Confidence Check → [High: Output] / [Low: Retrieval + Regenerate]. Reduces latency for confident outputs but may miss subtle hallucinations in seemingly confident outputs.
**EVIDENCE_STRENGTH**: MODERATE
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC10

---

## KA-145
**TYPE**: TECHNIQUE
**CONTENT**: Multi-agent verification consensus uses specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation but increased cost and complexity (3x inference).
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D1, D7
**SDLC_PHASES**: P4, P5
**PRODUCTS**: PC3

---

## KA-146
**TYPE**: ANTI_PATTERN
**CONTENT**: Prompt-only security relies on instruction text alone without runtime enforcement boundaries. Failure mode: easy bypass by injection or tool misuse. Mitigation: add hard policy gates at tool, artifact, and deployment boundaries.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC6

---

## KA-147
**TYPE**: ANTI_PATTERN
**CONTENT**: Trusting retrieved content as policy treats retrieved instructions as authoritative control logic. Failure mode: context poisoning leads to malicious action sequences. Mitigation: separate policy channel from retrieval channel; enforce provenance-aware trust tiers.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3
**PRODUCTS**: PC6

---

## KA-148
**TYPE**: ANTI_PATTERN
**CONTENT**: Over-privileged MCP defaults grant broad tool access across all tasks by default. Failure mode: privilege escalation and lateral movement across tools. Mitigation: task-scoped capabilities with explicit allowlists.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3
**PRODUCTS**: PC5

---

## KA-149
**TYPE**: ANTI_PATTERN
**CONTENT**: Unsandboxed code/tool execution runs generated code or powerful tools directly in trusted host context. Failure mode: host compromise, data exfiltration, persistence. Mitigation: isolated execution with constrained mounts, syscalls, and identities.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P7
**PRODUCTS**: PC9

---

## KA-150
**TYPE**: ANTI_PATTERN
**CONTENT**: Blind trust in LLM output deploys AI-generated code without verification. Failure mode: 40-45% vulnerability rate in production code, 19.7% fabricated package recommendations. Mitigation: multi-layer verification pipeline with static analysis and testing.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P4, P5
**PRODUCTS**: PC10

---

## KA-151
**TYPE**: ANTI_PATTERN
**CONTENT**: Single-technique hallucination defense uses only RAG or only static analysis. Failure mode: each technique has blind spots; RAG cannot eliminate hallucinations alone, static analysis misses semantic/logic errors. Mitigation: combine RAG + Self-Consistency + Static Analysis + UQ.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-152
**TYPE**: TECHNIQUE
**CONTENT**: MCP security threat mitigation addresses eight categories: Authentication/Authorization (OAuth 2.1, per-user tokens), Credential Exposure (secret managers, rotation), Malicious Servers (code signing, sandboxing), Command Injection (input validation), Prompt Injection (user confirmation), Tool Poisoning (version pinning), Session Hijacking (TLS, rate limiting), DoS (quotas, timeouts).
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P7
**PRODUCTS**: PC5

---

## KA-153
**TYPE**: METRIC
**CONTENT**: Tool description smells prevalence: 56% of MCP tools have unclear purpose, 43% have missing parameters, 38% have vague return values, 62% have insufficient examples. Augmenting descriptions accepts 67% increase in execution steps for 5.85% task success improvement.
**EVIDENCE_STRENGTH**: MODERATE
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3
**PRODUCTS**: PC5

---

## KA-154
**TYPE**: METRIC
**CONTENT**: AI-generated test suites achieve 60-80% coverage but often miss edge cases and boundary conditions that human testers identify. Coverage metrics alone are insufficient for test quality assessment.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-155
**TYPE**: METRIC
**CONTENT**: Well-structured unit tests reduce debugging time by 40-60% and improve code maintainability by 25%. Unit tests provide executable specifications that can be generated alongside code.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4, P6
**PRODUCTS**: PC10

---

## KA-156
**TYPE**: METRIC
**CONTENT**: Contract testing with tools like Pact reduces integration failures by 70% in distributed systems. Contract tests provide clear specifications for API generation in microservices architectures.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-157
**TYPE**: METRIC
**CONTENT**: E2E tests catch 15-25% of defects missed by unit and integration tests, but are 10x more expensive to maintain. AI agents should select critical paths carefully for E2E coverage.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-158
**TYPE**: METRIC
**CONTENT**: BDD with Given-When-Then structure improves stakeholder communication by 50% and provides natural language specifications that AI agents can parse and implement.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P2, P4
**PRODUCTS**: PC4

---

## KA-159
**TYPE**: METRIC
**CONTENT**: Property-based testing finds edge cases 3x more effectively than example-based testing by generating hundreds of test cases automatically. Provides concise way to specify expected behavior through invariants.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-160
**TYPE**: METRIC
**CONTENT**: Fuzzing finds security vulnerabilities 5x more effectively than manual testing. Essential for security-critical code, parsers, and input handling in AI-generated code.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6, D7
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-161
**TYPE**: METRIC
**CONTENT**: Mutation testing correlates with real defect detection at r=0.75, making it a strong predictor of test quality. Mutation scores provide feedback on test suite effectiveness for AI agents.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4, P5
**PRODUCTS**: PC10

---

## KA-162
**TYPE**: METRIC
**CONTENT**: Runtime validation catches 20-30% of defects that escape testing, particularly in production environments. Provides safety nets for AI-generated code through assertions and invariant monitoring.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4, P8
**PRODUCTS**: PC10

---

## KA-163
**TYPE**: METRIC
**CONTENT**: AI-generated tests focus 80% on happy paths, missing critical error handling. Explicit sad path testing requirements are essential for robust AI code generation.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-164
**TYPE**: METRIC
**CONTENT**: Multi-stage testing reduces production incidents by 60% compared to single-stage testing. Staged workflows enable autonomous operation with safety checkpoints.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4, P7
**PRODUCTS**: PC3

---

## KA-165
**TYPE**: METRIC
**CONTENT**: 80% line coverage correlates with 50% defect reduction, but coverage alone is insufficient. MC/DC coverage is required for safety-critical systems (DO-178C).
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-166
**TYPE**: TECHNIQUE
**CONTENT**: Test pyramid proportions for AI agents: ~70% unit tests, ~20% integration tests, ~10% E2E tests. Optimizes for fast feedback while maintaining comprehensive coverage.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/patterns.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-167
**TYPE**: METRIC
**CONTENT**: TDD initial development time increase is 15-35%, but ensures testability of design and provides executable specifications. AI agents can generate tests first as specifications, then implement code to pass them.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/patterns.md
**DOMAINS**: D6
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC10

---

## KA-168
**TYPE**: ANTI_PATTERN
**CONTENT**: Test inversion (more E2E tests than unit tests) creates slow, brittle test suites with long feedback cycles, high maintenance cost, flaky tests, and difficulty isolating failures. AI agents should be constrained to generate tests in pyramid proportions.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/patterns.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-169
**TYPE**: ANTI_PATTERN
**CONTENT**: Happy path bias in AI-generated tests only covers success scenarios, missing error handling and edge cases. Failure mode: production failures on edge cases, poor error handling. AI agents must be explicitly prompted to generate sad path tests.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/patterns.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-170
**TYPE**: ANTI_PATTERN
**CONTENT**: Coverage gaming writes tests to maximize coverage metrics without meaningful verification. Failure mode: high coverage but low quality, false confidence, missed bugs. AI agents should optimize for test quality, not just coverage metrics.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/patterns.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-171
**TYPE**: TECHNIQUE
**CONTENT**: Five autonomy levels for HITL systems: Operator (human directly controls), Collaborator (human and agent work together), Consultant (agent seeks human input), Approver (agent operates autonomously but requires approval for consequential actions), Observer (agent fully autonomous with monitoring only).
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/07_human_interaction/human_in_the_loop_systems/overview.md
**DOMAINS**: D11
**SDLC_PHASES**: P1, P2, P3
**PRODUCTS**: PC3

---

## KA-172
**TYPE**: METRIC
**CONTENT**: Well-designed HITL systems reduce human intervention by 70-80% while improving task success rates. Poorly designed systems create "approval fatigue" that degrades both human experience and system reliability.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/07_human_interaction/human_in_the_loop_systems/overview.md
**DOMAINS**: D11
**SDLC_PHASES**: P3, P5
**PRODUCTS**: PC3

---

## KA-173
**TYPE**: TOOL
**CONTENT**: Apprise notification framework supports 80+ services with unified API across email, chat, SMS, push notifications, and desktop. Enables intelligent routing based on urgency, time, and recipient preferences. Tagging system for service organization (family, devops, critical).
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/07_human_interaction/human_in_the_loop_systems/overview.md
**DOMAINS**: D11
**SDLC_PHASES**: P5, P7
**PRODUCTS**: PC9

---

## KA-174
**TYPE**: TECHNIQUE
**CONTENT**: Cascaded LLM decision frameworks use deferral policies (base model → large model → human) based on confidence scores, achieving 70% cost reduction while maintaining high accuracy.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/07_human_interaction/human_in_the_loop_systems/overview.md
**DOMAINS**: D8, D11
**SDLC_PHASES**: P3
**PRODUCTS**: PC3

---

## KA-175
**TYPE**: METRIC
**CONTENT**: Humans overestimate AI correctness by up to 80 percentage points (belief-performance gap). Calibration monitoring and adjustment over time is required to address proof-belief gaps where confidence exceeds verification capability.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/07_human_interaction/human_in_the_loop_systems/overview.md
**DOMAINS**: D11
**SDLC_PHASES**: P5, P8
**PRODUCTS**: PC10

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total Atoms Extracted | 50 |
| Starting ID | KA-126 |
| Ending ID | KA-175 |

### By Type
| Type | Count |
|------|-------|
| METRIC | 20 |
| TECHNIQUE | 15 |
| ANTI_PATTERN | 9 |
| TOOL | 3 |
| CONSTRAINT | 3 |

### By Evidence Strength
| Strength | Count |
|----------|-------|
| STRONG | 45 |
| MODERATE | 5 |
| WEAK | 0 |

### By Domain
| Domain | Count |
|--------|-------|
| D7: Security & Guardrails | 28 |
| D6: Testing & Validation | 16 |
| D11: Human Interaction | 5 |
| D3: Context & Prompt Engineering | 2 |
| D4: Memory & Knowledge Systems | 1 |
| D5: Code Intelligence | 1 |
| D8: Model Management & Routing | 1 |
| D10: Workspace & Infrastructure | 1 |

### By SDLC Phase
| Phase | Count |
|-------|-------|
| P4: Testing & Verification | 32 |
| P3: Implementation | 26 |
| P5: Code Review | 11 |
| P7: Deployment & Release | 8 |
| P6: Debugging & Error Recovery | 5 |
| P8: Maintenance & Monitoring | 4 |
| P1: Discovery & Onboarding | 3 |
| P2: Planning & Design | 3 |

### By Product
| Product | Count |
|---------|-------|
| PC10: Techniques & Strategies | 28 |
| PC6: Rules | 8 |
| PC3: Workflows | 5 |
| PC5: MCP Configurations | 4 |
| PC7: Context Management Strategies | 4 |
| PC9: Workspace Management | 3 |
| PC4: Prompts | 1 |

**Extraction Date**: 2026-02-24
**Source Files**: 
- `docs/research/01_meta_architecture/security_architecture/overview.md`
- `docs/research/01_meta_architecture/security_architecture/patterns.md`
- `docs/research/05_sdlc_automation/testing_architecture/overview.md`
- `docs/research/05_sdlc_automation/testing_architecture/patterns.md`
- `docs/research/07_human_interaction/human_in_the_loop_systems/overview.md`

---

## KA-126
**TYPE**: METRIC
**CONTENT**: 19.7% of recommended packages in LLM-generated code are fabricated ("slopsquatting"), creating supply chain attack vectors when developers attempt to install non-existent packages.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC10

---

## KA-127
**TYPE**: METRIC
**CONTENT**: 40-45% of AI-generated code contains exploitable security vulnerabilities, making security scanning mandatory for all AI-generated code before deployment.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P4, P5
**PRODUCTS**: PC10

---

## KA-128
**TYPE**: METRIC
**CONTENT**: 43% of Java errors in AI-generated code are API misuse hallucinations, where the code references non-existent methods or incorrect parameters.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P6
**PRODUCTS**: PC10

---

## KA-129
**TYPE**: METRIC
**CONTENT**: $1.3M annual cost per enterprise for hallucination-induced false positive management, quantifying the economic impact of AI code quality issues.
**EVIDENCE_STRENGTH**: MODERATE
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P8
**PRODUCTS**: PC10

---

## KA-130
**TYPE**: TECHNIQUE
**CONTENT**: Hybrid retrieval (BM25 + dense retrieval) achieves 67% reduction in hallucinations for code generation. Must be combined with verification for production use as context noise and conflict remain challenges.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D3, D7
**SDLC_PHASES**: P3
**PRODUCTS**: PC7

---

## KA-131
**TYPE**: TECHNIQUE
**CONTENT**: Self-consistency verification samples multiple reasoning paths and selects via majority vote, reducing stochastic errors by 7-19%. Chain-of-Verification (CoVe) follows: Draft → Plan verification → Answer independently → Generate verified response.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D3, D7
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC10

---

## KA-132
**TYPE**: METRIC
**CONTENT**: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations (KCHs) in code. Dr.Fix framework provides: Detection → Classification → Reasoning → Repair pipeline.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D5, D7
**SDLC_PHASES**: P4, P6
**PRODUCTS**: PC7

---

## KA-133
**TYPE**: TECHNIQUE
**CONTENT**: Neuro-symbolic approaches combining neural generation with symbolic verification achieve 20-30% improvement in vulnerability detection compared to neural-only methods.
**EVIDENCE_STRENGTH**: MODERATE
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D5, D7
**SDLC_PHASES**: P4, P5
**PRODUCTS**: PC10

---

## KA-134
**TYPE**: TECHNIQUE
**CONTENT**: Test-time compute scaling uses additional inference-time computation for verification, achieving 50% reduction in verification cost compared to separate verification passes.
**EVIDENCE_STRENGTH**: MODERATE
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-135
**TYPE**: TOOL
**CONTENT**: Sandbox technology comparison: gVisor (user-space kernel, container-like performance, general purpose), Kata Containers (VM-like isolation, container-like UX, high-security requirements), HopX (purpose-built for AI agents, AI-specific workloads).
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7, D10
**SDLC_PHASES**: P3, P7
**PRODUCTS**: PC9

---

## KA-136
**TYPE**: CONSTRAINT
**CONTENT**: Short-lived credentials must have maximum 1 hour TTL for agent access. Quarterly access reviews with automated expiration are required for compliance.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P7, P8
**PRODUCTS**: PC6

---

## KA-137
**TYPE**: TECHNIQUE
**CONTENT**: Prompt injection detection patterns with risk levels: Critical (instruction override like "Ignore all previous instructions"), High (role manipulation, system prompt leakage, disregard commands), Medium (persona injection). Pattern matching and ML classifiers required.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/overview.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC6

---

## KA-138
**TYPE**: TECHNIQUE
**CONTENT**: Layered guardrail envelope combines input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks with higher latency tradeoff.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC6

---

## KA-139
**TYPE**: TECHNIQUE
**CONTENT**: Provenance-tagged context ingestion attaches trust/provenance metadata to each retrieved context element and enforces policy by trust tier. Better poisoning containment and auditability with metadata pipeline overhead.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D4, D7
**SDLC_PHASES**: P1, P3
**PRODUCTS**: PC7

---

## KA-140
**TYPE**: TECHNIQUE
**CONTENT**: Task-scoped MCP capability minting issues narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius with capability broker complexity.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3
**PRODUCTS**: PC5

---

## KA-141
**TYPE**: CONSTRAINT
**CONTENT**: Default-deny egress with explicit allowlists blocks all outbound network access except approved domains/protocols tied to task policy. Critical for enterprise environments with strict data controls.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P7
**PRODUCTS**: PC6

---

## KA-142
**TYPE**: TECHNIQUE
**CONTENT**: Evidence-first action gating requires retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects with extra retrieval/validation latency.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P5, P7
**PRODUCTS**: PC6

---

## KA-143
**TYPE**: TECHNIQUE
**CONTENT**: Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Each layer adds 100ms-5s latency but provides defense in depth against multiple hallucination types.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P4, P5
**PRODUCTS**: PC10

---

## KA-144
**TYPE**: TECHNIQUE
**CONTENT**: Early exit with confidence gating: Generate → Confidence Check → [High: Output] / [Low: Retrieval + Regenerate]. Reduces latency for confident outputs but may miss subtle hallucinations in seemingly confident outputs.
**EVIDENCE_STRENGTH**: MODERATE
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC10

---

## KA-145
**TYPE**: TECHNIQUE
**CONTENT**: Multi-agent verification consensus uses specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation but increased cost and complexity (3x inference).
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D1, D7
**SDLC_PHASES**: P4, P5
**PRODUCTS**: PC3

---

## KA-146
**TYPE**: ANTI_PATTERN
**CONTENT**: Prompt-only security relies on instruction text alone without runtime enforcement boundaries. Failure mode: easy bypass by injection or tool misuse. Mitigation: add hard policy gates at tool, artifact, and deployment boundaries.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC6

---

## KA-147
**TYPE**: ANTI_PATTERN
**CONTENT**: Trusting retrieved content as policy treats retrieved instructions as authoritative control logic. Failure mode: context poisoning leads to malicious action sequences. Mitigation: separate policy channel from retrieval channel; enforce provenance-aware trust tiers.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3
**PRODUCTS**: PC6

---

## KA-148
**TYPE**: ANTI_PATTERN
**CONTENT**: Over-privileged MCP defaults grant broad tool access across all tasks by default. Failure mode: privilege escalation and lateral movement across tools. Mitigation: task-scoped capabilities with explicit allowlists.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3
**PRODUCTS**: PC5

---

## KA-149
**TYPE**: ANTI_PATTERN
**CONTENT**: Unsandboxed code/tool execution runs generated code or powerful tools directly in trusted host context. Failure mode: host compromise, data exfiltration, persistence. Mitigation: isolated execution with constrained mounts, syscalls, and identities.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P7
**PRODUCTS**: PC9

---

## KA-150
**TYPE**: ANTI_PATTERN
**CONTENT**: Blind trust in LLM output deploys AI-generated code without verification. Failure mode: 40-45% vulnerability rate in production code, 19.7% fabricated package recommendations. Mitigation: multi-layer verification pipeline with static analysis and testing.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P4, P5
**PRODUCTS**: PC10

---

## KA-151
**TYPE**: ANTI_PATTERN
**CONTENT**: Single-technique hallucination defense uses only RAG or only static analysis. Failure mode: each technique has blind spots; RAG cannot eliminate hallucinations alone, static analysis misses semantic/logic errors. Mitigation: combine RAG + Self-Consistency + Static Analysis + UQ.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-152
**TYPE**: TECHNIQUE
**CONTENT**: MCP security threat mitigation addresses eight categories: Authentication/Authorization (OAuth 2.1, per-user tokens), Credential Exposure (secret managers, rotation), Malicious Servers (code signing, sandboxing), Command Injection (input validation), Prompt Injection (user confirmation), Tool Poisoning (version pinning), Session Hijacking (TLS, rate limiting), DoS (quotas, timeouts).
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3, P7
**PRODUCTS**: PC5

---

## KA-153
**TYPE**: METRIC
**CONTENT**: Tool description smells prevalence: 56% of MCP tools have unclear purpose, 43% have missing parameters, 38% have vague return values, 62% have insufficient examples. Augmenting descriptions accepts 67% increase in execution steps for 5.85% task success improvement.
**EVIDENCE_STRENGTH**: MODERATE
**SOURCE**: docs/research/01_meta_architecture/security_architecture/patterns.md
**DOMAINS**: D7
**SDLC_PHASES**: P3
**PRODUCTS**: PC5

---

## KA-154
**TYPE**: METRIC
**CONTENT**: AI-generated test suites achieve 60-80% coverage but often miss edge cases and boundary conditions that human testers identify. Coverage metrics alone are insufficient for test quality assessment.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-155
**TYPE**: METRIC
**CONTENT**: Well-structured unit tests reduce debugging time by 40-60% and improve code maintainability by 25%. Unit tests provide executable specifications that can be generated alongside code.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4, P6
**PRODUCTS**: PC10

---

## KA-156
**TYPE**: METRIC
**CONTENT**: Contract testing with tools like Pact reduces integration failures by 70% in distributed systems. Contract tests provide clear specifications for API generation in microservices architectures.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-157
**TYPE**: METRIC
**CONTENT**: E2E tests catch 15-25% of defects missed by unit and integration tests, but are 10x more expensive to maintain. AI agents should select critical paths carefully for E2E coverage.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-158
**TYPE**: METRIC
**CONTENT**: BDD with Given-When-Then structure improves stakeholder communication by 50% and provides natural language specifications that AI agents can parse and implement.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P2, P4
**PRODUCTS**: PC4

---

## KA-159
**TYPE**: METRIC
**CONTENT**: Property-based testing finds edge cases 3x more effectively than example-based testing by generating hundreds of test cases automatically. Provides concise way to specify expected behavior through invariants.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-160
**TYPE**: METRIC
**CONTENT**: Fuzzing finds security vulnerabilities 5x more effectively than manual testing. Essential for security-critical code, parsers, and input handling in AI-generated code.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6, D7
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-161
**TYPE**: METRIC
**CONTENT**: Mutation testing correlates with real defect detection at r=0.75, making it a strong predictor of test quality. Mutation scores provide feedback on test suite effectiveness for AI agents.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4, P5
**PRODUCTS**: PC10

---

## KA-162
**TYPE**: METRIC
**CONTENT**: Runtime validation catches 20-30% of defects that escape testing, particularly in production environments. Provides safety nets for AI-generated code through assertions and invariant monitoring.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4, P8
**PRODUCTS**: PC10

---

## KA-163
**TYPE**: METRIC
**CONTENT**: AI-generated tests focus 80% on happy paths, missing critical error handling. Explicit sad path testing requirements are essential for robust AI code generation.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-164
**TYPE**: METRIC
**CONTENT**: Multi-stage testing reduces production incidents by 60% compared to single-stage testing. Staged workflows enable autonomous operation with safety checkpoints.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4, P7
**PRODUCTS**: PC3

---

## KA-165
**TYPE**: METRIC
**CONTENT**: 80% line coverage correlates with 50% defect reduction, but coverage alone is insufficient. MC/DC coverage is required for safety-critical systems (DO-178C).
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/overview.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-166
**TYPE**: TECHNIQUE
**CONTENT**: Test pyramid proportions for AI agents: ~70% unit tests, ~20% integration tests, ~10% E2E tests. Optimizes for fast feedback while maintaining comprehensive coverage.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/patterns.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-167
**TYPE**: METRIC
**CONTENT**: TDD initial development time increase is 15-35%, but ensures testability of design and provides executable specifications. AI agents can generate tests first as specifications, then implement code to pass them.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/patterns.md
**DOMAINS**: D6
**SDLC_PHASES**: P3, P4
**PRODUCTS**: PC10

---

## KA-168
**TYPE**: ANTI_PATTERN
**CONTENT**: Test inversion (more E2E tests than unit tests) creates slow, brittle test suites with long feedback cycles, high maintenance cost, flaky tests, and difficulty isolating failures. AI agents should be constrained to generate tests in pyramid proportions.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/patterns.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-169
**TYPE**: ANTI_PATTERN
**CONTENT**: Happy path bias in AI-generated tests only covers success scenarios, missing error handling and edge cases. Failure mode: production failures on edge cases, poor error handling. AI agents must be explicitly prompted to generate sad path tests.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/patterns.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-170
**TYPE**: ANTI_PATTERN
**CONTENT**: Coverage gaming writes tests to maximize coverage metrics without meaningful verification. Failure mode: high coverage but low quality, false confidence, missed bugs. AI agents should optimize for test quality, not just coverage metrics.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/05_sdlc_automation/testing_architecture/patterns.md
**DOMAINS**: D6
**SDLC_PHASES**: P4
**PRODUCTS**: PC10

---

## KA-171
**TYPE**: TECHNIQUE
**CONTENT**: Five autonomy levels for HITL systems: Operator (human directly controls), Collaborator (human and agent work together), Consultant (agent seeks human input), Approver (agent operates autonomously but requires approval for consequential actions), Observer (agent fully autonomous with monitoring only).
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/07_human_interaction/human_in_the_loop_systems/overview.md
**DOMAINS**: D11
**SDLC_PHASES**: P1, P2, P3
**PRODUCTS**: PC3

---

## KA-172
**TYPE**: METRIC
**CONTENT**: Well-designed HITL systems reduce human intervention by 70-80% while improving task success rates. Poorly designed systems create "approval fatigue" that degrades both human experience and system reliability.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/07_human_interaction/human_in_the_loop_systems/overview.md
**DOMAINS**: D11
**SDLC_PHASES**: P3, P5
**PRODUCTS**: PC3

---

## KA-173
**TYPE**: TOOL
**CONTENT**: Apprise notification framework supports 80+ services with unified API across email, chat, SMS, push notifications, and desktop. Enables intelligent routing based on urgency, time, and recipient preferences. Tagging system for service organization (family, devops, critical).
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/07_human_interaction/human_in_the_loop_systems/overview.md
**DOMAINS**: D11
**SDLC_PHASES**: P5, P7
**PRODUCTS**: PC9

---

## KA-174
**TYPE**: TECHNIQUE
**CONTENT**: Cascaded LLM decision frameworks use deferral policies (base model → large model → human) based on confidence scores, achieving 70% cost reduction while maintaining high accuracy.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/07_human_interaction/human_in_the_loop_systems/overview.md
**DOMAINS**: D8, D11
**SDLC_PHASES**: P3
**PRODUCTS**: PC3

---

## KA-175
**TYPE**: METRIC
**CONTENT**: Humans overestimate AI correctness by up to 80 percentage points (belief-performance gap). Calibration monitoring and adjustment over time is required to address proof-belief gaps where confidence exceeds verification capability.
**EVIDENCE_STRENGTH**: STRONG
**SOURCE**: docs/research/07_human_interaction/human_in_the_loop_systems/overview.md
**DOMAINS**: D11
**SDLC_PHASES**: P5, P8
**PRODUCTS**: PC10

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total Atoms Extracted | 50 |
| Starting ID | KA-126 |
| Ending ID | KA-175 |

### By Type
| Type | Count |
|------|-------|
| METRIC | 20 |
| TECHNIQUE | 15 |
| ANTI_PATTERN | 9 |
| TOOL | 3 |
| CONSTRAINT | 3 |

### By Evidence Strength
| Strength | Count |
|----------|-------|
| STRONG | 45 |
| MODERATE | 5 |
| WEAK | 0 |

### By Domain
| Domain | Count |
|--------|-------|
| D7: Security & Guardrails | 28 |
| D6: Testing & Validation | 16 |
| D11: Human Interaction | 5 |
| D3: Context & Prompt Engineering | 2 |
| D4: Memory & Knowledge Systems | 1 |
| D5: Code Intelligence | 1 |
| D8: Model Management & Routing | 1 |
| D10: Workspace & Infrastructure | 1 |

### By SDLC Phase
| Phase | Count |
|-------|-------|
| P4: Testing & Verification | 32 |
| P3: Implementation | 26 |
| P5: Code Review | 11 |
| P7: Deployment & Release | 8 |
| P6: Debugging & Error Recovery | 5 |
| P8: Maintenance & Monitoring | 4 |
| P1: Discovery & Onboarding | 3 |
| P2: Planning & Design | 3 |

### By Product
| Product | Count |
|---------|-------|
| PC10: Techniques & Strategies | 28 |
| PC6: Rules | 8 |
| PC3: Workflows | 5 |
| PC5: MCP Configurations | 4 |
| PC7: Context Management Strategies | 4 |
| PC9: Workspace Management | 3 |
| PC4: Prompts | 1 |

