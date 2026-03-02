# Prong 1: Meta-Architecture Knowledge Atom Extraction

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

# Prong 1: Meta-Architecture Knowledge Atom Extraction

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

# Prong 1: Meta-Architecture Knowledge Atom Extraction

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

# Prong 1: Meta-Architecture Knowledge Atom Extraction

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

# Prong 1: Meta-Architecture Knowledge Atom Extraction

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

# Prong 1: Meta-Architecture Knowledge Atom Extraction

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

# Prong 1: Meta-Architecture Knowledge Atom Extraction

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

# Prong 1: Meta-Architecture Knowledge Atom Extraction

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

# Prong 1: Meta-Architecture Knowledge Atom Extraction

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

# Prong 1: Meta-Architecture Knowledge Atom Extraction

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

# Prong 1: Meta-Architecture Knowledge Atom Extraction

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

**Research Domain:** 01_meta_architecture  
**Areas Covered:** economic_optimization_modeling, governance_compliance, security_architecture, system_design_philosophy  
**Extraction Date:** 2026-02-24  
**Atom Types:** TECHNIQUE, METRIC, CONSTRAINT, TOOL, COMBINATION, FAILURE_MODE, ANTI_PATTERN, TRADEOFF, RECIPE

---

## Executive Summary

This document contains 60 deduplicated knowledge atoms extracted from the meta-architecture research corpus across four domains: economic optimization, governance/compliance, security architecture, and system design philosophy. Atoms are ranked by evidence strength (STRONG > MODERATE > WEAK) and tagged with applicable SDLC domains, phases, and products.

**Key Statistics:**
- Total Atoms: 60
- STRONG Evidence: 24 atoms (40%)
- MODERATE Evidence: 28 atoms (47%)
- WEAK Evidence: 8 atoms (13%)

---

## STRONG Evidence Atoms

### KA-META-001
**TYPE:** METRIC  
**CONTENT:** AI agents cost $5-8 per task unconstrained, with multi-turn reasoning consuming 40-60% of costs, tool calls 20-30%, context accumulation 15-25%, and verification loops 10-20%. Output:input token ratio is 4-8:1, driving need for compression.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-002
**TYPE:** TECHNIQUE  
**CONTENT:** Model cascade routing achieves 60-87% cost reduction by trying cheap models first and escalating only when confidence thresholds are not met. EvoRoute RL-tuned routing demonstrates 76% cost reduction with 14% latency improvement.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-003
**TYPE:** METRIC  
**CONTENT:** Semantic caching achieves 31-90% input token reduction through embedding-based similarity matching. Cache hit rates by type: Exact Match 10-20%, Semantic 31-90%, Tool Result 40-60%, Embedding 50-80%, Multi-Level 60-90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-004
**TYPE:** TECHNIQUE  
**CONTENT:** Token efficiency techniques achieve: Prompt Compression 20-40% reduction, Structured Outputs (JSON) 30-50% reduction, Context Pruning 20-60% reduction, Retrieval Optimization 40-70% reduction, Semantic Caching 31-90% input reduction, Output Compression 10-30% reduction.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-005
**TYPE:** METRIC  
**CONTENT:** Model tier latency benchmarks (p50/p99): Mini/Nano 100-300ms/500-1000ms, Small 300-600ms/1-2s, Medium 600ms-1.5s/2-4s, Flagship 1-3s/5-15s. Relative cost multipliers: 1x, 3-5x, 10-20x, 30-50x respectively.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-006
**TYPE:** TOOL  
**CONTENT:** Cost modeling frameworks comparison: LangSmith (per trace granularity), Arize (per model with excellent visualization), Weights & Biases (per project with experiment tracking), Custom Prometheus (configurable), OpenAI Evals (per evaluation, basic visualization).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-007
**TYPE:** CONSTRAINT  
**CONTENT:** Budget enforcement mechanisms: Hard Token Limit (blocks per request), Soft Token Limit (warns per request), Cost Budget (blocks per period), Rate Limiting (throttles per time window), BATS Framework (block/warn per task with configurable override).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md, docs/research/01_meta_architecture/economic_optimization_modeling/overview.md  
**DOMAINS:** D1, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-008
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Matrix by constraint profile: Cost-first uses Cascade routing + semantic cache + budget decomposition; Latency-first uses Prewarm profiles + compact retrieval + small-model default; Quality-first uses Confidence escalation + critic verification + selective premium usage; Security-first uses Skill gating + MCP entitlement + audit telemetry.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-009
**TYPE:** TECHNIQUE  
**CONTENT:** Spec-driven 4-phase workflow (Specify → Plan → Tasks → Implement) achieves 56% faster development than ad-hoc approaches. AugmentCode GitHub Spec Kit demonstrates 87% accuracy for multi-file changes when specifications are maintained.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-010
**TYPE:** TECHNIQUE  
**CONTENT:** Provider cost comparison (2025 pricing per 1M tokens): OpenAI GPT-4o $2.50/$10.00 (input/output), GPT-4o-mini $0.15/$0.60, Anthropic Claude 3.5 Sonnet $3.00/$15.00, Claude 3.5 Haiku $0.25/$1.25, Google Gemini 1.5 Pro $1.25/$5.00, Gemini 1.5 Flash $0.075/$0.30. Cache hit discounts: OpenAI 50%, Anthropic 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-011
**TYPE:** FAILURE_MODE  
**CONTENT:** Prompt injection attack success rates: 50-84% in tool-using agents (USENIX Security 2025), 70% context poisoning in RAG systems (NeurIPS 2024), 65% indirect injection without delimiters (CCS 2024). Sandboxing reduces exfiltration by 90%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_08.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-012
**TYPE:** METRIC  
**CONTENT:** Hallucination impact statistics: 19.7% of recommended packages in LLM-generated code are fabricated (slopsquatting), 40-45% of AI-generated code contains exploitable security vulnerabilities, 43% of Java errors are API misuse hallucinations, $1.3M annual cost per enterprise for hallucination-induced false positive management.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-013
**TYPE:** TECHNIQUE  
**CONTENT:** Anti-hallucination guardrail effectiveness: RAG reduces factual hallucinations 60-80%, rule-based/classifier guardrails achieve 70-90% mitigation, multi-model validation catches 75% of reasoning errors, self-verification reduces SDLC hallucinations 65%, OpenCLaw achieves 92% precision in grounded tasks.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-014
**TYPE:** TRADEOFF  
**CONTENT:** Latency vs Intelligence tradeoff: o1-preview (high quality, 30s+) vs GPT-4o-mini (fast, 80% capability). Multi-model cascade achieves 87% cost reduction with minimal quality loss. Batching + prompt caching = 5x savings.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/perplexityai_research_overview.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-015
**TYPE:** COMBINATION  
**CONTENT:** Hallucination defense tradeoff matrix: RAG (Medium precision, High recall, Medium latency, Medium cost, Low creativity impact), Self-Consistency (High precision, Medium recall, High latency, High cost, None), Static Analysis (Very High precision, Medium recall, Low latency, Low cost, None), UQ-Based Filtering (Medium precision, Medium recall, Low latency, Low cost, Medium), Multi-Agent (High precision, High recall, Very High latency, Very High cost, Low).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-016
**TYPE:** ANTI_PATTERN  
**CONTENT:** Security anti-patterns with failure modes: Prompt-Only Security (easy bypass), Trusting Retrieved Content as Policy (context poisoning), Over-Privileged MCP Defaults (privilege escalation), Unsandboxed Code Execution (host compromise), Open Egress by Default (exfiltration).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-017
**TYPE:** RECIPE  
**CONTENT:** Governance compliance envelope per agent run must include: policy version, model/tool versions, inputs hash, outputs hash, approvals, trace IDs. Event-sourced audit ledger with append-only event journal and correlation IDs provides strong forensics.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-018
**TYPE:** TECHNIQUE  
**CONTENT:** Cold start mitigation strategies: Cache Pre-warming (minutes, low cost, high effectiveness), Repo Grokking (minutes-hours, medium cost, high effectiveness), Few-Shot Prompting (instant, low cost, medium effectiveness), Transfer Learning (hours-days, high cost, high effectiveness), Hybrid Pre-warm + Few-shot (minutes, medium cost, very high effectiveness).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-019
**TYPE:** TECHNIQUE  
**CONTENT:** Skill/Agent enablement strategies achieve token savings: Static Enablement 10-30%, Task-Based Gating 20-50%, Predictive Loading 30-60%, On-Demand Loading 40-70%, Hybrid Predictive + On-demand 40-60%.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/comparisons.md  
**DOMAINS:** D1, D2, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-020
**TYPE:** CONSTRAINT  
**CONTENT:** Security hardening checklist: Sandboxing (gVisor/Kata/HopX critical), Network Security (deny all egress by default critical), File System (read-only root filesystem critical), Secret Management (dedicated vault critical), Input/Output Validation (prompt injection detection critical), Access Control (tool-level RBAC critical).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-021
**TYPE:** ANTI_PATTERN  
**CONTENT:** Economic optimization anti-patterns: One-Model-for-Everything (unnecessary cost inflation), Unlimited Recursive Planning (token runaway), Full-Context Stuffing (context dilution), Cache Without Freshness Policy (stale advice), Optimization by Averages Only (p95/p99 regressions), Missing Skill Entitlement Boundaries (token/tool overhead).  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-022
**TYPE:** TECHNIQUE  
**CONTENT:** Static analysis integration for hallucination detection: AST-based detection achieves 100% precision, 87.6% recall for Knowledge-Conflicting Hallucinations. Dr.Fix framework: Detection → Classification → Reasoning → Repair pipeline.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-023
**TYPE:** TECHNIQUE  
**CONTENT:** RAG for Code with Hybrid Retrieval: BM25 + dense retrieval achieves 67% reduction in hallucinations. Must be combined with verification for production use. Context noise and conflict remain major challenges.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D3, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-024
**TYPE:** COMBINATION  
**CONTENT:** Multi-layer hallucination defense pipeline: Generation → Consistency Check → Static Analysis → Execution Test → Human Review. Latency cost: 100ms-5s per check layer.  
**EVIDENCE_STRENGTH:** STRONG  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## MODERATE Evidence Atoms

### KA-META-025
**TYPE:** TECHNIQUE  
**CONTENT:** BDI Hybrid Architecture combines Belief-Desire-Intent symbolic reasoning with LLM-based agents, providing explicit mental states for introspection and verifiability. Enables accountable autonomy in production environments.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-026
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven comparison: Spec-Driven (Low flexibility, High reproducibility, High maintenance cost) best for regulated/safety-critical. Intent-Driven (High flexibility, Variable reproducibility, Low maintenance cost) best for exploratory/prototype. Hybrid approach recommended for most scenarios.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-027
**TYPE:** TECHNIQUE  
**CONTENT:** Bidirectional Specifications pattern: Specifications evolve alongside code implementations, with agents updating specs as they discover codebase realities. Prevents specification debt where specs diverge from implementation.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-028
**TYPE:** TECHNIQUE  
**CONTENT:** 12 Agentic Design Patterns framework decomposes agent systems into 5 subsystems: Retriever, Writer, Manager, Observer, and core orchestration. Provides modular building blocks for reliable agent architectures.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/comparisons.md, docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-029
**TYPE:** TECHNIQUE  
**CONTENT:** Semantic Codebase Understanding (Repo Grokking): Build comprehensive codebase understanding through semantic analysis rather than file-by-file processing. Enables architecture drift detection and prevents context poisoning.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-030
**TYPE:** TECHNIQUE  
**CONTENT:** Deterministic Control Plane, Stochastic Data Plane pattern: Enforce strict determinism for orchestration/policy decisions while allowing bounded stochasticity for content generation. Provides practical balance between reproducibility and capability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-031
**TYPE:** TECHNIQUE  
**CONTENT:** Ephemeral Scoped Credential Broker pattern: Issue short-lived least-privilege credentials per task/tool invocation from a vault broker. Reduces standing privilege and leakage impact.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md, docs/research/01_meta_architecture/governance_compliance/comparisons.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-032
**TYPE:** TECHNIQUE  
**CONTENT:** AI-Native SBOM Extension: Extend SBOM to include model/provider/version, prompt templates, retrieval corpora, tool endpoints, and dependency lineage. Better root-cause analysis and legal posture than traditional package-only SBOMs.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-033
**TYPE:** TECHNIQUE  
**CONTENT:** Task-Scoped MCP Capability Minting: Issue narrow, temporary capabilities per task/tool invocation rather than static broad permissions. Strong least privilege and reduced compromise blast radius.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-034
**TYPE:** TECHNIQUE  
**CONTENT:** Evidence-First Action Gating: Require retrieval-backed evidence and confidence thresholds before high-impact actions (merge/deploy/scaffold). Reduces hallucinated side effects at cost of extra retrieval/validation latency.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-035
**TYPE:** TECHNIQUE  
**CONTENT:** Layered Guardrail Envelope: Combine input filtering, tool-call policy validation, output schema checks, and post-action attestation. Defense in depth against semantic and syntactic attacks.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-036
**TYPE:** TECHNIQUE  
**CONTENT:** Default-Deny Egress with Explicit Allowlists: Block all outbound network access except approved domains/protocols tied to task policy. Strong exfiltration and C2 resistance at cost of integration friction.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md, docs/research/01_meta_architecture/security_architecture/comparisons.md  
**DOMAINS:** D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-037
**TYPE:** TECHNIQUE  
**CONTENT:** Provenance-Tagged Context Ingestion: Attach trust/provenance metadata to each retrieved context element and enforce policy by trust tier. Better poisoning containment and auditability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D3, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-038
**TYPE:** ANTI_PATTERN  
**CONTENT:** System design anti-patterns: Vibe Coding (ad-hoc without specs), Shallow Repo Understanding (file-by-file without context), Stale Documentation Specs (human-only maintenance), Unbounded Context Accumulation (no token limits), Credential Sprawl in IDE (improper vaulting), Single-Pass Generation (no verification), Implicit Intent Tracking (no logging), Monolithic Agent Design (no decomposition).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-039
**TYPE:** TECHNIQUE  
**CONTENT:** Budget-Aware Task Decomposition: Split tasks into sub-steps with explicit token and tool-call budgets per step; terminate or degrade gracefully when budget envelopes are exceeded. Prevents runaway loops.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-040
**TYPE:** TECHNIQUE  
**CONTENT:** Retrieval Compression Pipeline: Multi-stage retrieval where broad recall is followed by re-ranking and context compression before final model invocation. Better signal-to-noise ratio, lower token cost, improved reasoning quality.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D3  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-041
**TYPE:** TECHNIQUE  
**CONTENT:** Skill Gating and Tool Entitlement: Dynamically enable only the minimum required skills/workflows/tools/MCP servers for each task class. Lower token/tool overhead, reduced attack surface, cleaner traceability.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D2, D5  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-042
**TYPE:** TECHNIQUE  
**CONTENT:** Cost-to-Value Telemetry Loop: Track task outcomes (quality, completion, human rework) against spend, then feed metrics back into routing and budget policies. Evidence-based model selection, defensible budget decisions.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/economic_optimization_modeling/patterns.md  
**DOMAINS:** D1, D11  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-043
**TYPE:** RECIPE  
**CONTENT:** Governance research-grounded use cases: (1) Regulated Code Assistant: compliance envelopes + runtime policy adjudication + human escalation; (2) License-Sensitive Monorepo: similarity-based screening + AI-native SBOM + quarantine; (3) Agent-Caused Regression Forensics: deterministic control-plane replay + signed logs + trace-linked explanations; (4) Secure MCP Ecosystem: signed tool manifests + scoped credential broker + per-tool policy gates.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D5, D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-044
**TYPE:** TRADEOFF  
**CONTENT:** Complexity Budget Framework dimensions: Code size (LOC per function/module), Abstraction depth (layers of indirection), Cyclomatic complexity (independent paths), Coupling (inter-module dependencies), Cognitive complexity (subjective understandability). Threshold triggers required for enforcement.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-045
**TYPE:** TECHNIQUE  
**CONTENT:** Chain-of-Verification (CoVe): Draft → Plan verification → Answer independently → Generate verified response. Reduces stochastic errors by 7-19%. Self-consistency via multiple reasoning paths with majority vote.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-046
**TYPE:** TOOL  
**CONTENT:** Anti-hallucination tools: LangChain Guardrails (output validation, structure enforcement), LM-Polygraph (uncertainty quantification), RAGAS (RAG evaluation), HaluEval (hallucination benchmark), Dr.Fix (API misuse repair), NeMo Guardrails, LLM Guard.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-047
**TYPE:** TECHNIQUE  
**CONTENT:** Neuro-Symbolic Approaches: Neural generation + symbolic verification achieves 20-30% improvement in vulnerability detection. Test-Time Compute Scaling provides additional inference-time computation for verification with 50% reduction in verification cost.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/overview.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-048
**TYPE:** COMBINATION  
**CONTENT:** Pattern Selection Guide by scenario: New project exploration → Intent-Driven + Critic-Actor; Production feature development → 4-Phase Spec-Driven + Bidirectional; Large codebase refactoring → Semantic Understanding + Modular; Safety-critical systems → BDI Hybrid + Structured HITL.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D2, D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-049
**TYPE:** TECHNIQUE  
**CONTENT:** Progressive Disclosure Architecture: Three-level skill/knowledge architecture (Level 1 Identity ~100 tokens for selection, Level 2 Instructions ~1,000 tokens for execution, Level 3 Resources unbounded for deep expertise) minimizes context window consumption while maintaining access to deep procedural knowledge.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/patterns.md  
**DOMAINS:** D3, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-050
**TYPE:** TRADEOFF  
**CONTENT:** Key architectural tradeoffs for autonomous systems: Autonomy vs Control (risk-based with approval gates), Simplicity vs Capability (start simple, add as needed), Cost vs Quality (task-dependent model selection), Latency vs Intelligence (user-facing vs batch processing).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D1, D2, D4  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-051
**TYPE:** TECHNIQUE  
**CONTENT:** Topology-driven performance: Orchestration topology dominates over individual model capability (12-23% improvement). Four canonical patterns: Parallel, Sequential, Hierarchical, Hybrid. Protocol maturation: MCP, A2A, ACP, ANP emerging as standards.  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-052
**TYPE:** COMBINATION  
**CONTENT:** Technology Selection Guidance by layer: Orchestration (LangGraph for complex, CrewAI for simple), Context (RAG + long-context hybrid), Memory (vector + graph hybrid), Security (gVisor/Kata minimum), Model Routing (cascading with circuit breakers), Testing (self-healing with mutation testing), CI/CD (GitOps with progressive delivery).  
**EVIDENCE_STRENGTH:** MODERATE  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D2, D3, D5, D8, D9, D10  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## WEAK Evidence Atoms

### KA-META-053
**TYPE:** METRIC  
**CONTENT:** Complexity scoring metrics for agent systems: Token count (ignores semantic complexity), Tool call depth (misses parallel complexity), Cyclomatic complexity (doesn't capture agent reasoning), State space size (hard to compute), Hybrid scoring (requires calibration). No standardized metrics exist; active research area.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-054
**TYPE:** CONSTRAINT  
**CONTENT:** Anti-slop constraints for agent-generated code: Complexity budgets (hard limits on code size/abstraction depth), Specification discipline (explicit minimal specs), Entropy tracking (architectural drift measurement), Autonomy constraints (pre-defined modes/tools), Feedback loops (continuous human/auto feedback).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/perplexityai_research_overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-055
**TYPE:** FAILURE_MODE  
**CONTENT:** Governance anti-patterns: Action Logs Without Decision Context (weak audit defensibility), Policy-in-Prompt Only (easy bypass), Long-Lived Shared Credentials (large blast radius), SBOM Without AI Context (incomplete provenance), Replay Claims Without Environment Snapshots (non-reproducible postmortems).  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/patterns.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-056
**TYPE:** TECHNIQUE  
**CONTENT:** Entropy tracking in evolving codebases: Monitor inconsistent naming conventions, duplicate/near-duplicate code blocks, circular dependencies, dead code accumulation. Requires baseline measurements and trend analysis; agent systems may accelerate entropy through uncoordinated modifications.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/system_design_philosophy/overview.md  
**DOMAINS:** D4  
**SDLC_PHASES:** P2, P3, P4  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-057
**TYPE:** TRADEOFF  
**CONTENT:** Spec-Driven vs Intent-Driven tradeoffs: Granular audits increase storage/latency (10-50% overhead). Strict policies vs developer velocity. Reproducibility seeding reduces true autonomy. Audit depth provides forensic proof but performance hit. Policy strictness ensures compliance but velocity loss. SBOM scope provides transparency but maintenance burden.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/governance_compliance/perplexityai_research_overview.md  
**DOMAINS:** D6  
**SDLC_PHASES:** P1, P2, P3, P4, P5, P6, P7, P8  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-058
**TYPE:** TECHNIQUE  
**CONTENT:** Self-Verification: Agents critique own outputs via verifiers (e.g., web search, code exec). Reduces SDLC hallucinations 65%. Failure on edge cases like private repos. Agents self-query verifiers reducing hallucinations through iterative verification.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/perplexityai_research_overview_09.md  
**DOMAINS:** D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-059
**TYPE:** TECHNIQUE  
**CONTENT:** Uncertainty-Calibrated Human Escalation: Route outputs to human review based on uncertainty quantification thresholds. Scalable safety with human oversight on edge cases. Human bottleneck for uncertain outputs. Threshold calibration critical for effectiveness.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

### KA-META-060
**TYPE:** TECHNIQUE  
**CONTENT:** Multi-Agent Verification Consensus: Use specialized agents (Generator, Critic, Verifier) with consensus-based output selection. High precision through cross-validation at cost of increased complexity (3x inference). Best for complex reasoning tasks and critical infrastructure code.  
**EVIDENCE_STRENGTH:** WEAK  
**SOURCE:** docs/research/01_meta_architecture/security_architecture/patterns.md  
**DOMAINS:** D2, D5, D7  
**SDLC_PHASES:** P3, P4, P5, P6  
**PRODUCTS:** PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9, PC10

---

## Knowledge Gaps

The following areas could not be confirmed or require further investigation:

1. **Formal complexity metrics for agent systems**: No standardized framework exists; all proposed metrics have significant limitations.

2. **Empirical data on spec vs. intent approaches**: Limited peer-reviewed studies comparing outcomes in LLM/agentic contexts.

3. **Scope creep quantification**: Few frameworks for detecting or measuring scope creep in real-time during agent execution.

4. **Anti-slop validation**: Lack of automated methods to detect and prevent AI-generated complexity without human review.

5. **Enterprise ROI baselines**: Limited standardized frameworks for measuring true ROI of agent deployments (code quality → business value).

6. **Optimal cache invalidation**: Strategy for dynamic codebases not well-established.

7. **Budget enforcement mechanisms**: How to prevent runaway costs without blocking critical tasks requires more research.

8. **Multi-objective routing**: Optimal algorithms for cost + latency + quality tradeoffs are emerging but not mature.

9. **Agent economy design**: Internal token markets and cost attribution models still theoretical.

10. **Zero-trust for inter-agent communication**: Formal models and empirical evaluations lacking.

---

## Recommended Next Subtask

**Prong 2: Cross-Domain Relationship Mapping**

The next phase should map relationships between extracted knowledge atoms across all 4 prongs, identifying:
- Dependencies between economic constraints and security controls
- Governance requirements that impact system design choices
- Security patterns that enable or constrain optimization strategies
- Design patterns that facilitate compliance and auditability

This cross-domain analysis will inform the domain groupings and phase mappings in subsequent prongs.

---

## Sources

### Economic Optimization Modeling
- comparisons.md (7,732 chars)
- overview.md (8,584 chars)
- patterns.md (6,981 chars)
- perplexityai_research_overview.md (10,733 chars)
- references.md (9,853 chars)

### Governance & Compliance
- comparisons.md (4,681 chars)
- overview.md (8,468 chars)
- patterns.md (4,674 chars)
- perplexityai_research_overview.md (11,173 chars)
- references.md (10,238 chars)

### Security Architecture
- comparisons.md (4,178 chars)
- overview.md (14,762 chars)
- patterns.md (14,647 chars)
- perplexityai_research_overview_08.md (10,610 chars)
- perplexityai_research_overview_09.md (11,065 chars)
- references.md (27,387 chars)

### System Design Philosophy
- comparisons.md (6,758 chars)
- overview.md (15,721 chars)
- patterns.md (13,402 chars)
- perplexityai_research_overview.md (47,004 chars)
- references.md (13,682 chars)

**Total Research Corpus:** ~220,000 characters across 20+ files

---

*Generated: 2026-02-24*  
*Prong: 1 of 4*  
*Research Mode: knowledge extraction only - no architecture design or implementation*

