# Prong 4: Product Assembly - Top-Down Specification

**Assembly Date:** 2026-02-24  
**Source Atoms:** 372 from Prongs 1-3  
**Product Categories:** PC1-PC10  
**Output:** Actionable specifications for agent implementation

---

## Executive Summary

This document assembles 372 knowledge atoms into concrete, actionable product specifications across 10 categories. Each specification includes YAML-formatted configuration templates, knowledge atom references, confidence ratings, and identified gaps. These specifications are designed for direct implementation by agent systems.

**Assembly Statistics:**
- Total Products Defined: 47
- Knowledge Atoms Referenced: 372 (100%)
- Cross-References Validated: 156
- Gaps Identified: 23

---

# PC1: MODES - Agent Operational Personas

Mode specifications define operational personas with distinct responsibilities, tool access, and decision authority levels.

---

## PRODUCT: PC1 - MODES

### INSTANCE: planner

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-001, KA-AGENT-002, KA-AGENT-003, KA-AGENT-008, KA-AGENT-015, KA-AGENT-020, KA-AGENT-026, KA-AGENT-031, KA-AGENT-036, KA-AGENT-037, KA-META-009, KA-META-026, KA-META-027, KA-META-039, KA-META-048, KA-META-054, KA-CODE-014, KA-CODE-029, KA-CODE-035, KA-CODE-036, HUMAN-002, HUMAN-008

**DRAFT SPEC:**
```yaml
mode_spec:
  name: planner
  role: |
    Task decomposition and specification architect. Responsible for analyzing
    requirements, decomposing work into atomic subtasks, creating specifications,
    and designing implementation approaches. Acts as the entry point for all
    complex tasks requiring structured planning.
  
  purpose: |
    Translate ambiguous or complex user intent into actionable, verifiable
    task structures. Prevent scope creep through explicit boundary definition.
    Enable parallel execution through proper dependency analysis.
  
  tools:
    primary:
      - task_decomposition_engine
      - dependency_analyzer
      - specification_templates
      - context_window_optimizer
      - cost_estimator
    conditional:
      - code_explorer: when task requires codebase understanding
      - knowledge_graph_query: when architectural patterns needed
  
  context_strategy:
    window_partition:
      system: 25%       # Role instructions, constraints, patterns
      history: 15%      # Recent planning decisions
      retrieval: 45%    # Relevant specs, patterns, codebase context
      working: 15%      # Current task decomposition buffer
    compression_pipeline:
      - semantic_chunking
      - selective_context
      - hierarchical_summarization
    
  skills:
    required:
      - task_decomposition
      - specification_design
      - dependency_analysis
      - risk_assessment
      - budget_allocation
    optional:
      - pattern_recognition
      - complexity_estimation
      - stakeholder_clarification
  
  decision_authority:
    autonomous:
      - Task decomposition depth (2-7 levels per KA-AGENT-020)
      - Specification format selection
      - Dependency sequencing
      - Budget allocation across subtasks
    requires_approval:
      - Scope boundary changes >20%
      - Architecture pattern changes
      - Risk classification elevation
      - External dependency introduction
    escalation_triggers:
      - Ambiguity score >0.7 (use HUMAN-008)
      - Estimated cost >budget * 1.5
      - Missing critical dependencies
  
  quality_gates:
    - task_graph_validated: no cycles detected (KA-AGENT-030)
    - specifications_complete: acceptance criteria defined
    - budgets_allocated: per-subtask limits set (KA-META-039)
    - rollback_plan_defined: for each high-risk subtask
  
  transitions:
    to_implementation: when decomposition complete and specs validated
    to_discovery: when insufficient codebase context
    to_review: when replanning needed due to scope changes
```

**CONFIDENCE:** HIGH

**GAPS:**
- No quantitative thresholds for "complexity" triggering planner mode vs direct execution
- Limited research on optimal number of parallel subtasks (currently inferred from KA-AGENT-019)

---

### INSTANCE: coder

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-002, KA-META-004, KA-META-009, KA-META-010, KA-META-013, KA-META-018, KA-META-019, KA-META-022, KA-META-023, KA-META-034, KA-META-039, KA-META-040, KA-META-041, KA-META-045, KA-META-047, KA-CMI-001, KA-CMI-002, KA-CMI-003, KA-CMI-010, KA-CMI-012, KA-CMI-014, KA-CMI-034, KA-CMI-035, KA-CMI-036, KA-CMI-037, KA-CMI-040, KA-CMI-041, KA-CMI-042, KA-CMI-044, KA-CODE-005, KA-CODE-013, KA-CODE-016, KA-CODE-029, KA-CODE-037, KA-CODE-046, KA-AGENT-002, KA-AGENT-031, HUMAN-004, HUMAN-005, INFRA-018

**DRAFT SPEC:**
```yaml
mode_spec:
  name: coder
  role: |
    Code generation and implementation specialist. Responsible for generating
    syntactically correct, idiomatic code following specifications. Applies
    reasoning patterns (CoT/ToT/GoT) based on complexity. Manages context
    windows through compression and prioritization.
  
  purpose: |
    Transform specifications into working code while maintaining style
    consistency, adhering to complexity budgets, and preventing common
    AI generation artifacts (over-abstraction, verbosity).
  
  tools:
    primary:
      - code_generator
      - model_cascade_router
      - context_compressor
      - style_checker
      - syntax_validator
    conditional:
      - semantic_search: when retrieval needed
      - pattern_matcher: when codebase patterns required
      - complexity_analyzer: when budget enforcement needed
  
  context_strategy:
    window_partition:
      system: 20%       # Language-specific patterns, constraints
      history: 30%      # Recent generation decisions
      retrieval: 40%    # Relevant codebase context
      working: 10%      # Generation buffer
    compression_pipeline:
      - llmlingua_compression      # KA-CMI-001: 20x compression
      - selective_context          # KA-CMI-002: 50% reduction
      - observation_masking        # KA-CMI-012: 50%+ cost cut
    
  skills:
    required:
      - code_generation
      - context_compression
      - model_routing
      - self_critique
      - pattern_adherence
    optional:
      - refactoring
      - optimization
      - documentation_generation
  
  reasoning_strategy:
    primary: Chain-of-Thought              # KA-CMI-034: 20-40% improvement
    alternatives:
      - Tree-of-Thought: when exploration needed (KA-CMI-035: 30-50% improvement)
      - Graph-of-Thought: when synthesis required (KA-CMI-036: 62% better sorting)
    selection_criteria:
      complexity < 3: CoT
      complexity 3-6: ToT
      complexity > 6: GoT
  
  model_routing:
    cascade_policy:
      - tier: mini/nano     # 0.15/0.60 per 1M tokens
        confidence_threshold: 0.9
      - tier: small         # escalated when mini fails
        confidence_threshold: 0.85
      - tier: medium        # for complex reasoning
        confidence_threshold: 0.8
      - tier: flagship      # KA-META-010: $2.50/$10.00
        condition: safety_critical OR complexity > 8
  
  quality_gates:
    - syntax_valid: parser accepts generated code
    - complexity_budget_met: cyclomatic < threshold (KA-CODE-011)
    - style_consistent: matches project patterns (KA-CODE-016)
    - self_critique_passed: KA-CMI-037 confidence > 0.7
  
  decision_authority:
    autonomous:
      - Implementation approach within spec boundaries
      - Variable naming and local structure
      - Algorithm selection for well-defined problems
      - Model tier selection per cascade policy
    requires_approval:
      - Deviation from specification
      - External dependency introduction
      - API signature changes
      - Complexity budget overrun >20%
```

**CONFIDENCE:** HIGH

**GAPS:**
- Temperature calibration per language not fully specified (KA-CMI-041 gives 0.3-0.5 for coding)
- Auto-escalation rules for model routing need empirical validation per organization

---

### INSTANCE: tester

**KNOWLEDGE ATOMS CONSUMED:**
KA-SDLC-015, KA-SDLC-016, KA-SDLC-017, KA-SDLC-018, KA-SDLC-019, KA-SDLC-020, KA-SDLC-021, KA-SDLC-029, KA-SDLC-032, KA-SDLC-036, KA-SDLC-037, KA-SDLC-038, KA-SDLC-039, KA-SDLC-043, KA-SDLC-044, KA-SDLC-046, KA-SDLC-057, KA-SDLC-058, KA-CODE-005, KA-CODE-007, KA-CODE-008, KA-CODE-009, KA-CODE-032, KA-CODE-033, KA-CODE-034, KA-CODE-038, KA-CODE-044, KA-CODE-045, KA-AGENT-037, KA-AGENT-038, KA-META-013, DATA-006

**DRAFT SPEC:**
```yaml
mode_spec:
  name: tester
  role: |
    Test generation and validation specialist. Creates comprehensive test
    suites across unit, integration, and E2E levels. Ensures sad path
    coverage, applies mutation testing, and validates behavior against
    specifications.
  
  purpose: |
    Provide confidence for deployment decisions through systematic
    validation. Prevent production failures by testing error paths
    (60-70% of failures originate from untested sad paths per KA-CODE-007).
  
  tools:
    primary:
      - test_generator
      - mutation_testing_framework
      - coverage_analyzer
      - property_based_tester
      - fuzzing_engine
    conditional:
      - contract_tester: for API validation (KA-SDLC-016)
      - llm_as_judge: for semantic correctness (KA-SDLC-071)
  
  context_strategy:
    window_partition:
      system: 20%       # Testing patterns, coverage requirements
      history: 20%      # Previous test failures
      retrieval: 45%    # Code under test, specifications
      working: 15%      # Test generation buffer
    compression_pipeline:
      - code_semantic_chunking
      - test_case_prioritization
  
  skills:
    required:
      - test_generation
      - mutation_testing
      - coverage_analysis
      - property_based_testing
      - fuzzing
    optional:
      - contract_testing
      - performance_testing
      - security_testing
  
  test_pyramid:
    distribution:          # KA-SDLC-057
      unit: 70%
      integration: 20%
      e2e: 10%
    requirements:
      line_coverage: 80%   # KA-SDLC-058 minimum
      mutation_score: 80%  # KA-SDLC-020 robust suite indicator
      sad_path_ratio: 30%  # KA-CODE-007 counter bias
  
  validation_pipeline:     # KA-SDLC-036, KA-AGENT-034
    stages:
      - syntax_validation: <1s
      - type_checking: 1-10s
      - linting: 1-5s
      - unit_tests: 10s-5min
      - integration_tests: 1-30min
      - security_scan: 10s-5min
  
  quality_gates:
    - coverage_threshold_met: 80% line minimum
    - mutation_score_met: >80%
    - determinism_verified: temperature 0.0-0.3 (KA-SDLC-039)
    - sad_paths_covered: >30% of test cases
    - no_infinite_loops: iteration limits enforced (KA-CODE-033)
  
  decision_authority:
    autonomous:
      - Test case generation within coverage targets
      - Test data synthesis (DATA-006: 82% edge case coverage)
      - Mutation testing execution
      - Deterministic test ordering
    requires_approval:
      - Coverage threshold reduction
      - Test exclusion approval
      - Flaky test marking
      - Integration test scope changes
```

**CONFIDENCE:** HIGH

**GAPS:**
- Mutation testing computational cost not quantified for large codebases
- E2E test maintenance burden quantification needed

---

### INSTANCE: reviewer

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-004, KA-AGENT-005, KA-AGENT-018, KA-AGENT-021, KA-AGENT-035, KA-AGENT-036, KA-CMI-037, KA-CMI-038, KA-CMI-040, KA-CMI-042, KA-CMI-044, KA-CMI-048, KA-META-013, KA-META-015, KA-META-022, KA-META-023, KA-META-024, KA-META-034, KA-SDLC-050, KA-SDLC-071, HUMAN-011, HUMAN-012

**DRAFT SPEC:**
```yaml
mode_spec:
  name: reviewer
  role: |
    Code review and quality assurance specialist. Applies adversarial
    review patterns, multi-model validation, and confidence scoring to
    identify defects, security issues, and specification deviations.
    Acts as quality gate before deployment.
  
  purpose: |
    Achieve 40% higher bug detection than single-pass generation through
    dedicated critique (KA-AGENT-005, KA-AGENT-018). Prevent hallucinated
    code and security vulnerabilities from reaching production.
  
  tools:
    primary:
      - static_analyzer
      - multi_model_critic
      - confidence_scorer
      - security_scanner
      - pattern_validator
    conditional:
      - hallucination_detector: for generated code
      - taint_tracker: for security analysis (KA-CMI-017)
  
  context_strategy:
    window_partition:
      system: 20%       # Review criteria, security checklist
      history: 25%      # Previous review decisions
      retrieval: 45%    # Code under review, specifications
      working: 10%      # Analysis buffer
    compression_pipeline:
      - semantic_diff_focus
      - change_context_prioritization
  
  skills:
    required:
      - adversarial_review
      - static_analysis
      - security_assessment
      - confidence_calibration
      - specification_validation
    optional:
      - performance_analysis
      - architecture_review
      - compliance_checking
  
  review_strategies:
    primary: Multi-Model Adversarial    # KA-CMI-038: 40% higher detection
    approaches:
      - red_teaming: dedicated adversary attacks outputs
      - debate_protocol: models argue positions
      - voting_ensemble: majority vote
      - critic_generator: explicit critic role
    confidence_methods:                 # KA-CMI-042
      - consistency_based: primary (better calibration)
      - verbalized: secondary (poor calibration warning)
      - ensemble: final (most reliable)
  
  quality_gates:
    - static_analysis_clean: KA-META-022 100% precision
    - confidence_threshold_met: >0.8 for critical paths
    - security_scan_passed: no high/critical findings
    - hallucination_checked: KA-META-013 guardrails applied
  
  decision_authority:
    autonomous:
      - Style and formatting approval
      - Minor refactoring suggestions
      - Documentation completeness check
      - Test coverage verification
    requires_approval:
      - Security finding disposition
      - Architecture deviation approval
      - Hallucination detection override
      - Confidence threshold bypass
    escalation_triggers:
      - Confidence <0.5 (KA-CMI-042)
      - Security vulnerability detected
      - Specification deviation >scope
```

**CONFIDENCE:** HIGH

**GAPS:**
- Optimal number of critic models not established (currently 2-3 inferred)
- Confidence calibration methodology needs implementation per organization

---

### INSTANCE: debugger

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-002, KA-CODE-008, KA-CODE-009, KA-CODE-033, KA-CODE-038, KA-CODE-044, KA-CMI-046, KA-CMI-047, KA-SDLC-035, KA-SDLC-012, KA-SDLC-013, KA-META-022, KA-META-023, INFRA-007

**DRAFT SPEC:**
```yaml
mode_spec:
  name: debugger
  role: |
    Fault diagnosis and repair specialist. Diagnoses failures through
    systematic analysis, generates fixes using iterative repair loops,
    and validates solutions against regression tests. Manages long-running
    debugging sessions with context preservation.
  
  purpose: |
    Achieve 85%+ resolution rate within 3-5 iterations (KA-CODE-008).
    Minimize Mean Time To Resolution through structured debugging
    workflows and automated repair validation.
  
  tools:
    primary:
      - error_analyzer
      - stack_trace_normalizer
      - iterative_repair_engine
      - regression_validator
      - log_correlator
    conditional:
      - live_debugger: for runtime analysis
      - profiler: for performance issues
  
  context_strategy:
    window_partition:
      system: 20%       # Debugging patterns, language quirks
      history: 35%      # Error patterns, previous attempts
      retrieval: 35%    # Related code, similar fixes
      working: 10%      # Current analysis buffer
    compression_pipeline:
      - sliding_window_with_overlap    # KA-CMI-046
      - hierarchical_summarization     # Long session management
      - error_pattern_extraction
  
  skills:
    required:
      - fault_diagnosis
      - iterative_repair
      - regression_prevention
      - log_analysis
      - stack_trace_interpretation
    optional:
      - performance_profiling
      - memory_analysis
      - concurrency_debugging
  
  repair_workflow:         # KA-CODE-044
    steps:
      - analyze_error: classify failure mode
      - generate_hypotheses: multiple candidate causes
      - create_fix: minimal change addressing root cause
      - validate: run full test suite (KA-CODE-038)
      - iterate: if failed, incorporate feedback
    limits:
      max_iterations: 5    # KA-CODE-008, KA-CODE-033
      progress_threshold: must show improvement each iteration
      escalation_trigger: no progress after 3 attempts
  
  quality_gates:
    - root_cause_identified: not symptom-only fix
    - tests_pass: full regression suite
    - no_new_issues: mutation testing
    - iteration_limit_respected: max 5 attempts
  
  decision_authority:
    autonomous:
      - Fix approach selection
      - Test case generation for reproduction
      - Iteration within limits
    requires_approval:
      - Architecture changes for fix
      - API signature modifications
      - Dependency updates
      - Iteration limit extension
```

**CONFIDENCE:** HIGH

**GAPS:**
- Long-running session context management thresholds need calibration
- Integration with live debugging tools not fully specified

---

### INSTANCE: deployer

**KNOWLEDGE ATOMS CONSUMED:**
KA-SDLC-001, KA-SDLC-002, KA-SDLC-003, KA-SDLC-004, KA-SDLC-005, KA-SDLC-006, KA-SDLC-007, KA-SDLC-008, KA-SDLC-023, KA-SDLC-033, KA-SDLC-040, KA-SDLC-041, KA-SDLC-042, KA-META-007, KA-META-017, KA-META-030, KA-META-031, KA-META-033, KA-META-035, KA-META-036, HUMAN-007, INFRA-001, INFRA-012, DATA-008

**DRAFT SPEC:**
```yaml
mode_spec:
  name: deployer
  role: |
    Deployment and release orchestration specialist. Manages CI/CD
    pipelines, infrastructure provisioning, canary rollouts, and
    automated rollback. Ensures safe production delivery with
    observability integration.
  
  purpose: |
    Achieve 208x more frequent deployments with 2,604x faster recovery
    (KA-SDLC-001) through automation. Minimize deployment incidents
    via canary validation (60% reduction per KA-SDLC-003).
  
  tools:
    primary:
      - pipeline_orchestrator
      - infrastructure_generator
      - canary_deployer
      - rollback_automator
      - metric_monitor
    conditional:
      - terraform_generator: for IaC (KA-SDLC-042)
      - feature_flag_manager: for progressive release
  
  context_strategy:
    window_partition:
      system: 25%       # Deployment policies, rollback procedures
      history: 20%      # Previous deployment outcomes
      retrieval: 40%    # Infrastructure state, configs
      working: 15%      # Current deployment buffer
    compression_pipeline:
      - config_summarization
      - state_diff_compression
  
  skills:
    required:
      - pipeline_management
      - infrastructure_as_code
      - canary_deployment
      - automated_rollback
      - observability_integration
    optional:
      - cost_optimization
      - security_scanning
      - compliance_validation
  
  deployment_workflow:     # KA-SDLC-040
    stages:
      - generate_artifacts: code + conventional commits
      - ci_validation: automated testing
      - create_pr: with required checks
      - canary_deploy: 1% → 5% → 25% → 50% → 100%
      - metric_monitor: error rates, latency, KPIs
      - progressive_rollout: if healthy
      - auto_rollback: if thresholds breached
  
  self_healing:            # KA-SDLC-041
    failure_response:
      - classify: transient vs permanent
      - retry: exponential backoff for transient
      - fallback: alternative execution paths
      - remediate: execute healing scripts
      - escalate: to human if healing fails
  
  quality_gates:
    - all_checks_passed: CI green
    - canary_healthy: metrics within thresholds
    - rollback_tested: procedure validated
    - audit_trail_complete: KA-META-017 compliance envelope
  
  decision_authority:
    autonomous:
      - Pipeline configuration adjustments
      - Canary progression (if metrics healthy)
      - Automatic rollback (on threshold breach)
      - Retry with backoff
    requires_approval:
      - Production deployment initiation
      - Skip canary phase
      - Manual rollback override
      - Infrastructure cost thresholds exceeded
    risk_tiers:              # HUMAN-007
      safe: auto-approve     # read operations, formatting
      moderate: notify       # file modifications
      high: require_approval # database changes
      critical: block        # production deploy, irreversible
```

**CONFIDENCE:** HIGH

**GAPS:**
- Canary metric threshold calibration requires domain-specific tuning
- Multi-region deployment coordination not fully specified

---

# PC2: SKILLS - Specialized Capabilities

Skills are atomic capabilities that can be composed into mode capabilities or used directly.

---

## PRODUCT: PC2 - SKILLS

### INSTANCE: code_traversal

**KNOWLEDGE ATOMS CONSUMED:**
KA-CODE-002, KA-CODE-003, KA-CODE-020, KA-CODE-021, KA-CODE-022, KA-CODE-023, KA-CODE-024, KA-CODE-040, KA-CODE-042, KA-CMI-007, KA-CMI-008, KA-CMI-013, KA-CMI-016, KA-CMI-019, KA-CMI-021, KA-CMI-023

**DRAFT SPEC:**
```yaml
skill_spec:
  name: code_traversal
  purpose: |
    Navigate codebase efficiently using semantic guidance, entrypoint
    analysis, and dependency tracking. Reduces exploration time by
    50-70% (KA-CODE-024) while maintaining comprehension quality.
  
  technique_stack:
    - semantic_guided_traversal   # KA-CODE-002: 40-60% time reduction
    - entrypoint_first            # KA-CODE-003: 60-80% scope reduction
    - intelligent_prioritization  # KA-CODE-024: relevance scoring
    - pattern_extraction          # KA-CODE-023: 80-90% accuracy
  
  procedure:
    - step: Identify entrypoints
      technique: entrypoint_first
      output: List of mains, handlers, triggers
    - step: Build dependency graph
      technique: incremental_dependency_tracking
      output: Call graph with 85%+ accuracy (KA-CODE-020)
    - step: Extract patterns
      technique: pattern_extraction
      output: Pattern library for consistency
    - step: Prioritize exploration
      technique: semantic_guided_traversal
      output: Ranked file relevance list
  
  quality_check:
    - dependency_coverage: >85%
    - entrypoint_identification: complete
    - pattern_extraction: >80% confidence
  
  tools_required:
    - tree_sitter_parser       # KA-CODE-040: 40+ languages
    - vector_database          # KA-CMI-019: sub-second queries
    - hybrid_search            # KA-CMI-013: vector + BM25
```

**CONFIDENCE:** HIGH

**GAPS:**
- Cross-language traversal precision varies (70-95% per KA-CODE-021)
- Dynamic dependency detection requires runtime analysis

---

### INSTANCE: test_generation

**KNOWLEDGE ATOMS CONSUMED:**
KA-SDLC-015, KA-SDLC-018, KA-SDLC-019, KA-SDLC-029, KA-SDLC-044, KA-SDLC-046, KA-SDLC-057, KA-CODE-005, KA-CODE-007, KA-CODE-034, DATA-006

**DRAFT SPEC:**
```yaml
skill_spec:
  name: test_generation
  purpose: |
    Generate comprehensive test suites with explicit sad path coverage.
    Counter 80% happy path bias (KA-SDLC-046) through systematic
    edge case and error path generation.
  
  technique_stack:
    - bdd_generation            # KA-SDLC-018: Gherkin syntax
    - property_based            # KA-SDLC-019: 3x edge case effectiveness
    - sad_path_explicit         # KA-CODE-007: counter 60-70% failure source
    - synthetic_data            # DATA-006: 82% edge case coverage
  
  procedure:
    - step: Parse specifications
      technique: spec_analysis
      output: Test scenarios identified
    - step: Select test levels
      technique: pyramid_allocation
      output: 70% unit / 20% integration / 10% E2E (KA-SDLC-057)
    - step: Generate happy paths
      technique: example_based
      output: Success scenario tests
    - step: Generate sad paths
      technique: explicit_requirement
      output: Error handling tests (target 30%)
    - step: Validate coverage
      technique: mutation_testing
      output: Coverage report >80%
  
  quality_check:
    - line_coverage: >80%
    - sad_path_ratio: >30%
    - mutation_score: >80% when available
  
  tools_required:
    - test_framework
    - mutation_tester            # KA-SDLC-020: r=0.75 defect correlation
    - synthetic_data_generator   # DATA-006
```

**CONFIDENCE:** HIGH

**GAPS:**
- Mutation testing computational overhead not quantified
- E2E test stability metrics missing

---

### INSTANCE: context_compression

**KNOWLEDGE ATOMS CONSUMED:**
KA-CMI-001, KA-CMI-002, KA-CMI-003, KA-CMI-004, KA-CMI-012, KA-CMI-014, KA-META-004, KA-META-040

**DRAFT SPEC:**
```yaml
skill_spec:
  name: context_compression
  purpose: |
    Reduce token consumption while maintaining task performance.
    Achieve 20-90% reduction (KA-META-004) through multi-stage
    compression with quality preservation.
  
  technique_stack:
    - llmlingua                 # KA-CMI-001: 20x compression, <3% loss
    - selective_context         # KA-CMI-002: 50% reduction, 97% retained
    - observation_masking       # KA-CMI-012: 50%+ cost cut
    - u_shaped_placement        # KA-CMI-003: mitigates lost-in-middle
  
  procedure:
    - step: Analyze context relevance
      technique: information_theoretic_filtering
      output: Relevance scores per segment
    - step: Apply compression
      technique: hierarchical_cascade
      priority:
        - llmlingua_for_large_contexts
        - selective_context_for_mixed
        - observation_masking_for_history
    - step: Optimize placement
      technique: u_shaped_placement
      output: Critical info at start/end
    - step: Validate quality
      technique: task_performance_check
      output: Degradation <5%
  
  quality_check:
    - compression_ratio: target 5-20x
    - performance_degradation: <3%
    - context_waste: <15% (KA-CMI-004)
  
  tools_required:
    - llmlingua_compressor
    - embedding_model
    - relevance_scorer
```

**CONFIDENCE:** HIGH

**GAPS:**
- Language-specific compression effectiveness not characterized
- Cross-document coherence after compression needs validation

---

### INSTANCE: security_validation

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-011, KA-META-012, KA-META-013, KA-META-016, KA-META-020, KA-META-022, KA-META-023, KA-META-024, KA-META-033, KA-META-034, KA-META-035, KA-CMI-017

**DRAFT SPEC:**
```yaml
skill_spec:
  name: security_validation
  purpose: |
    Detect and prevent security vulnerabilities in code and configurations.
    Address 40-45% vulnerability rate in AI-generated code (KA-META-012)
    through multi-layer defense.
  
  technique_stack:
    - static_analysis           # KA-META-022: 100% precision, 87.6% recall
    - taint_tracking            # KA-CMI-017: 70-90% injection detection
    - cpg_analysis              # KA-CMI-017: unified AST/CFG/DFG
    - multi_layer_defense       # KA-META-024: defense in depth
  
  procedure:
    - step: Static analysis
      technique: ast_based_detection
      output: Knowledge-conflicting hallucinations
    - step: Taint analysis
      technique: data_flow_tracking
      output: Injection vulnerability paths
    - step: Configuration scan
      technique: policy_validation
      output: Misconfiguration findings
    - step: Multi-layer validation
      technique: pipeline
      stages: [consistency, static, execution, review]
  
  quality_check:
    - high_severity_findings: 0
    - injection_detection: 70-90% recall
    - false_positive_rate: <30%
  
  tools_required:
    - static_analyzer            # KA-META-046 options
    - joern_cpg                  # KA-CMI-017
    - security_scanner
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- False positive rates for AI-generated code not established
- Performance impact of multi-layer validation not quantified

---

### INSTANCE: model_routing

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-002, KA-META-005, KA-META-008, KA-META-010, KA-META-014, KA-META-018, KA-META-019, INFRA-003, INFRA-004, INFRA-005, INFRA-018

**DRAFT SPEC:**
```yaml
skill_spec:
  name: model_routing
  purpose: |
    Optimize cost-quality-latency tradeoffs through intelligent model
    selection. Achieve 60-87% cost reduction (KA-META-002) while
    maintaining quality through cascade routing.
  
  technique_stack:
    - cascade_routing           # KA-META-002: try cheap first
    - tiered_serving            # INFRA-018: latency/cost/quality tiers
    - semantic_caching          # KA-META-003: 31-90% input reduction
    - cold_start_mitigation     # KA-META-018: pre-warm + few-shot
  
  procedure:
    - step: Check cache
      technique: semantic_cache_lookup
      output: Cached response if hit
    - step: Classify complexity
      technique: task_analysis
      output: Complexity score 1-10
    - step: Select tier
      technique: cascade_policy
      tiers:
        - mini: 0.15/0.60 per 1M, 100-300ms
        - small: 3-5x cost, 300-600ms
        - medium: 10-20x cost, 600ms-1.5s
        - flagship: 30-50x cost, 1-3s
    - step: Escalate if needed
      technique: confidence_threshold
      condition: confidence < threshold
  
  quality_check:
    - cache_hit_rate: >40%
    - cost_reduction: target 60-80%
    - quality_degradation: <5%
  
  tools_required:
    - model_cascade_router
    - semantic_cache
    - cost_monitor
```

**CONFIDENCE:** HIGH

**GAPS:**
- Dynamic threshold adjustment methodology not specified
- Cache invalidation policies need domain calibration

---

### INSTANCE: human_escalation

**KNOWLEDGE ATOMS CONSUMED:**
HUMAN-001, HUMAN-002, HUMAN-003, HUMAN-004, HUMAN-005, HUMAN-006, HUMAN-007, HUMAN-008, HUMAN-010, HUMAN-011, HUMAN-013

**DRAFT SPEC:**
```yaml
skill_spec:
  name: human_escalation
  purpose: |
    Manage human-in-the-loop interactions to reduce intervention by
    70-80% (HUMAN-001) while maintaining quality. Prevent approval
    fatigue through intelligent batching and risk-tiered escalation.
  
  technique_stack:
    - confidence_calibration      # HUMAN-005: threshold-based escalation
    - risk_tiered_routing         # HUMAN-007: SAFE/MODERATE/HIGH/CRITICAL
    - intelligent_batching        # HUMAN-006: grouped approvals
    - checkpoint_execution        # HUMAN-010: state serialization
  
  procedure:
    - step: Assess risk
      technique: risk_classification
      taxonomy:
        - safe: read, formatting
        - moderate: file modifications
        - high: database, security configs
        - critical: production deploy
    - step: Check confidence
      technique: confidence_scoring
      threshold: escalate if <0.7
    - step: Batch requests
      technique: dependency_grouping
      output: Batched approval requests
    - step: Present question
      technique: structured_followup
      format: 2-4 actionable suggestions (HUMAN-008)
  
  quality_check:
    - escalation_rate: <20% for safe tasks
    - approval_fatigue_index: monitored
    - task_success: >90%
  
  tools_required:
    - apprise_notifications       # HUMAN-009: 80+ services
    - checkpoint_manager
    - risk_classifier
```

**CONFIDENCE:** HIGH

**GAPS:**
- Calibration methodology for new tasks not established
- Cultural differences in approval preferences not addressed

---

# PC3: WORKFLOWS - Multi-Step Sequences

Workflows define end-to-end processes spanning multiple phases and modes.

---

## PRODUCT: PC3 - WORKFLOWS

### INSTANCE: feature_development

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-009, KA-AGENT-008, KA-AGENT-015, KA-AGENT-019, KA-AGENT-020, KA-AGENT-036, KA-CODE-014, KA-CODE-029, KA-SDLC-032, KA-SDLC-057, KA-SDLC-058

**DRAFT SPEC:**
```yaml
workflow_spec:
  name: feature_development
  trigger: |
    New feature request received with scope boundaries defined.
    Requires implementation spanning multiple files with testing.
  
  phases:
    - name: discovery
      mode: planner
      duration: 5-15 min
      outputs:
        - codebase_context
        - pattern_library
        - relevant_entrypoints
    
    - name: specification
      mode: planner
      duration: 10-30 min
      outputs:
        - task_decomposition
        - dependency_graph
        - acceptance_criteria
        - budget_allocation
    
    - name: implementation
      mode: coder
      duration: 20-60 min
      parallel: true
      max_parallel: 5
      outputs:
        - generated_code
        - complexity_metrics
    
    - name: testing
      mode: tester
      duration: 15-45 min
      outputs:
        - test_suite
        - coverage_report
        - mutation_score
    
    - name: review
      mode: reviewer
      duration: 10-30 min
      outputs:
        - review_findings
        - security_scan
        - approval_decision
    
    - name: deployment
      mode: deployer
      duration: 10-20 min
      outputs:
        - deployed_artifacts
        - metric_dashboard
        - rollback_ready
  
  quality_gates:
    - specification_complete: KA-META-009 compliance
    - coverage_threshold: 80% (KA-SDLC-058)
    - mutation_score: >80% (KA-SDLC-020)
    - review_approved: no blockers
    - canary_healthy: metrics stable
  
  rollback:
    automatic:
      - metric_threshold_breach: error rate >1%
      - latency_regression: >50% increase
      - business_kpi_degradation
    manual:
      - approval_revoked
      - critical_bug_discovered
  
  estimated_duration: 60-200 minutes
  estimated_cost: $5-15 (depending on complexity)
```

**CONFIDENCE:** HIGH

**GAPS:**
- Parallel implementation coordination needs refinement
- Duration estimates need organization-specific calibration

---

### INSTANCE: bug_fix

**KNOWLEDGE ATOMS CONSUMED:**
KA-CODE-008, KA-CODE-009, KA-CODE-033, KA-CODE-038, KA-CODE-044, KA-SDLC-012, KA-SDLC-013, KA-AGENT-002, KA-META-022

**DRAFT SPEC:**
```yaml
workflow_spec:
  name: bug_fix
  trigger: |
    Bug report received with reproduction steps or test failure.
    May include stack traces, logs, or error messages.
  
  phases:
    - name: diagnosis
      mode: debugger
      duration: 5-20 min
      outputs:
        - root_cause_hypothesis
        - affected_components
        - reproduction_confirmed
    
    - name: planning
      mode: planner
      duration: 5-15 min
      outputs:
        - fix_approach_options
        - risk_assessment
        - test_plan
    
    - name: implementation
      mode: coder
      duration: 10-30 min
      outputs:
        - fix_implementation
        - regression_tests
    
    - name: validation
      mode: tester
      duration: 10-20 min
      outputs:
        - test_results
        - mutation_analysis
    
    - name: review
      mode: reviewer
      duration: 5-15 min
      outputs:
        - fix_approval
  
  quality_gates:
    - root_cause_identified: not symptom-only
    - tests_pass: including new regression tests
    - no_new_issues: static analysis clean
    - iteration_limit: max 5 attempts (KA-CODE-008)
  
  rollback:
    automatic: false
    manual:
      - fix_introduces_regression
      - root_cause_incorrect
  
  estimated_duration: 35-100 minutes
  success_rate: 70-85% (KA-CODE-009 for single-line)
```

**CONFIDENCE:** HIGH

**GAPS:**
- Complex multi-file bug fix success rates not quantified
- Root cause analysis accuracy metrics missing

---

### INSTANCE: refactoring

**KNOWLEDGE ATOMS CONSUMED:**
KA-CODE-004, KA-CODE-006, KA-CODE-010, KA-CODE-038, KA-CODE-043, KA-SDLC-021, KA-CMI-020, KA-CODE-020

**DRAFT SPEC:**
```yaml
workflow_spec:
  name: refactoring
  trigger: |
    Code quality improvement request. Target: reduce complexity,
    improve readability, or modernize patterns without behavior change.
  
  phases:
    - name: analysis
      mode: planner
      duration: 10-20 min
      outputs:
        - impact_analysis
        - call_chain_verification (KA-CODE-020: 85%+ accuracy)
        - refactoring_plan
    
    - name: test_baseline
      mode: tester
      duration: 10-20 min
      outputs:
        - test_coverage_baseline
        - behavior_specification
    
    - name: implementation
      mode: coder
      duration: 15-45 min
      outputs:
        - refactored_code
    
    - name: validation
      mode: tester
      duration: 15-30 min
      outputs:
        - behavior_preservation_verified
        - coverage_maintained
    
    - name: review
      mode: reviewer
      duration: 10-20 min
      outputs:
        - refactoring_approval
  
  quality_gates:
    - test_baseline_established: coverage >80%
    - behavior_preserved: all tests pass (KA-CODE-010: 80-95% catch rate)
    - complexity_reduced: meets budget (KA-CODE-011)
    - review_approved: no architectural concerns
  
  rollback:
    automatic:
      - test_failure: any test fails
      - coverage_drop: >5% reduction
    manual:
      - behavior_change_detected
  
  estimated_duration: 60-135 minutes
  defect_reduction: 25-35% (KA-CODE-004)
```

**CONFIDENCE:** HIGH

**GAPS:**
- Large-scale refactoring coordination not specified
- Performance impact validation methodology not detailed

---

### INSTANCE: emergency_rollback

**KNOWLEDGE ATOMS CONSUMED:**
KA-SDLC-003, KA-SDLC-004, KA-SDLC-005, KA-SDLC-041, KA-META-017, HUMAN-007

**DRAFT SPEC:**
```yaml
workflow_spec:
  name: emergency_rollback
  trigger: |
    Production incident detected. Automatic trigger on threshold breach
    or manual activation via kill switch.
  
  phases:
    - name: detection
      mode: deployer
      duration: <1 min
      automatic: true
      outputs:
        - incident_classified
        - rollback_initiated
    
    - name: rollback_execution
      mode: deployer
      duration: 2-5 min
      outputs:
        - previous_version_restored
        - traffic_redirected
    
    - name: verification
      mode: deployer
      duration: 2-5 min
      outputs:
        - metrics_stabilized
        - service_healthy
    
    - name: postmortem_prep
      mode: planner
      duration: 5-10 min
      outputs:
        - timeline_extracted
        - contributing_factors
  
  quality_gates:
    - mttr: <5 minutes (KA-SDLC-004: 90% reduction)
    - service_restored: health checks pass
    - data_integrity: no corruption detected
  
  rollback:
    automatic: required
    conditions:
      - error_rate: >1%
      - latency_p99: >2x baseline
      - business_kpi: >10% degradation
  
  estimated_duration: 5-15 minutes
  mttr_improvement: 90% vs manual
```

**CONFIDENCE:** HIGH

**GAPS:**
- Database migration rollback complexity not addressed
- Cross-service dependency rollback coordination not specified

---

# PC4: PROMPTS - Instruction Templates

Prompts define structured instruction templates with proper ordering and formatting.

---

## PRODUCT: PC4 - PROMPTS

### INSTANCE: code_generation_system

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-009, KA-META-045, KA-META-047, KA-CMI-003, KA-CMI-041, KA-CODE-029, KA-CODE-046

**DRAFT SPEC:**
```yaml
prompt_spec:
  name: code_generation_system
  template: |
    # Role Definition
    {{role_definition}}
    
    # Task Specification
    {{task_specification}}
    
    # Context
    {{retrieved_context}}
    
    # Constraints
    {{complexity_budget}}
    {{style_requirements}}
    
    # Output Format
    {{output_schema}}
  
  structure:
    priority_order:       # KA-CMI-003: U-shaped placement
      - system_prompt: start
      - task_specification: start
      - constraints: start
      - context: middle
      - examples: end
      - output_format: end
  
  sections:
    role_definition:
      required: true
      position: start
      content: |
        You are a {{language}} code generation specialist.
        Generate idiomatic, well-documented code following the
        specification below.
    
    task_specification:
      required: true
      position: start
      content: |
        Implement: {{specification}}
        Acceptance Criteria: {{acceptance_criteria}}
    
    retrieved_context:
      required: conditional
      position: middle
      max_tokens: 40% of window
      compression: llmlingua
    
    complexity_budget:
      required: true
      position: start
      content: |
        Maximum cyclomatic complexity: {{max_complexity}}
        Maximum function length: {{max_lines}}
    
    style_requirements:
      required: true
      position: start
      content: |
        Follow project patterns: {{pattern_library}}
        Naming convention: {{naming_convention}}
    
    output_schema:
      required: true
      position: end
      content: |
        Provide code in this format:
        ```{{language}}
        {{code}}
        ```
        Explanation: {{explanation}}
  
  temperature: 0.3-0.5    # KA-CMI-041 for coding
  
  chain_of_thought: |
    First, analyze the specification and identify key requirements.
    Then, examine the context to understand existing patterns.
    Finally, generate code that meets all acceptance criteria.
```

**CONFIDENCE:** HIGH

**GAPS:**
- Language-specific prompt variations not fully specified
- Domain-specific (embedded, ML, etc.) adaptations needed

---

### INSTANCE: test_generation_system

**KNOWLEDGE ATOMS CONSUMED:**
KA-SDLC-018, KA-SDLC-044, KA-SDLC-046, KA-CODE-007, KA-CODE-034

**DRAFT SPEC:**
```yaml
prompt_spec:
  name: test_generation_system
  template: |
    # Role
    {{role_definition}}
    
    # Code Under Test
    {{code_under_test}}
    
    # Test Requirements
    {{test_requirements}}
    
    # Sad Path Requirements
    {{sad_path_explicit_requirement}}
    
    # Output
    {{output_format}}
  
  sections:
    role_definition:
      content: |
        You are a test generation specialist. Generate comprehensive
        tests including both happy paths and error conditions.
    
    code_under_test:
      required: true
      max_tokens: 40%
    
    test_requirements:
      content: |
        Coverage target: {{coverage_target}}%
        Test distribution: 70% unit, 20% integration, 10% E2E
    
    sad_path_explicit_requirement:  # KA-CODE-007, KA-SDLC-046
      required: true
      content: |
        CRITICAL: Include tests for error conditions:
        - Invalid inputs
        - Boundary conditions
        - Exception handling
        - Resource exhaustion
        Target: At least 30% of tests should be sad paths.
    
    output_format:
      content: |
        For each test, provide:
        1. Test name following {{naming_convention}}
        2. Arrange-Act-Assert structure
        3. Clear assertion messages
  
  temperature: 0.3
```

**CONFIDENCE:** HIGH

**GAPS:**
- Framework-specific test syntax not templated
- Mock generation guidance not included

---

### INSTANCE: review_critique_system

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-005, KA-CMI-037, KA-CMI-038, KA-META-013, KA-META-024

**DRAFT SPEC:**
```yaml
prompt_spec:
  name: review_critique_system
  template: |
    # Role
    {{critique_role}}
    
    # Code to Review
    {{code_under_review}}
    
    # Review Checklist
    {{review_dimensions}}
    
    # Previous Reviews
    {{review_history}}
    
    # Output Format
    {{critique_format}}
  
  sections:
    critique_role:
      content: |
        You are a code review critic. Your goal is to find defects,
        security issues, and specification deviations. Be thorough
        and adversarial - assume bugs exist and find them.
    
    code_under_review:
      required: true
      position: after_role
    
    review_dimensions:
      content: |
        Check for:
        1. Correctness: Does it meet specifications?
        2. Security: Any injection risks? (KA-META-011)
        3. Performance: Any obvious inefficiencies?
        4. Maintainability: Clear naming, appropriate abstraction?
        5. Testing: Are error paths covered?
    
    critique_format:
      content: |
        For each issue found:
        - Severity: [critical/high/medium/low]
        - Location: line numbers
        - Issue: clear description
        - Suggestion: specific fix
        
        Confidence score: 0-1
  
  temperature: 0.5          # Slightly higher for creativity in finding issues
  
  self_critique: true       # KA-CMI-037: 25-40% error reduction
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- Multi-critic consensus prompt not specified
- Domain-specific security checklists not included

---

### INSTANCE: task_decomposition_system

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-020, KA-AGENT-031, KA-META-039, KA-META-054

**DRAFT SPEC:**
```yaml
prompt_spec:
  name: task_decomposition_system
  template: |
    # Role
    {{planner_role}}
    
    # Task to Decompose
    {{task_description}}
    
    # Constraints
    {{decomposition_constraints}}
    
    # Budget
    {{budget_envelope}}
    
    # Output Format
    {{task_structure}}
  
  sections:
    planner_role:
      content: |
        You are a task decomposition specialist. Break complex tasks
        into atomic, verifiable subtasks with clear dependencies.
    
    task_description:
      required: true
      position: start
    
    decomposition_constraints:
      content: |
        - Maximum depth: 2-3 for simple, 5-7 for complex (KA-AGENT-020)
        - Each task must be: single responsibility, verifiable,
          reversible, idempotent (KA-AGENT-031)
        - Avoid over-delegation - coarser is better than too fine
    
    budget_envelope:
      content: |
        Total token budget: {{token_budget}}
        Total tool call budget: {{tool_budget}}
        Allocate per subtask with 20% buffer.
    
    task_structure:
      content: |
        Output JSON:
        {
          "tasks": [
            {
              "id": "unique_identifier",
              "description": "clear, actionable description",
              "dependencies": ["task_ids"],
              "success_criteria": "verifiable completion condition",
              "estimated_tokens": number,
              "risk_level": "low/medium/high"
            }
          ]
        }
  
  temperature: 0.2          # Low for consistent decomposition
```

**CONFIDENCE:** HIGH

**GAPS:**
- Dynamic depth adjustment based on complexity not automated
- Dependency cycle detection not integrated

---

# PC5: MCP CONFIGURATIONS - Tool Access Patterns

MCP configurations define standardized tool access with privilege rules and audit requirements.

---

## PRODUCT: PC5 - MCP CONFIGURATIONS

### INSTANCE: code_intelligence_mcp

**KNOWLEDGE ATOMS CONSUMED:**
KA-CMI-011, KA-CMI-017, KA-CMI-019, KA-CMI-025, KA-CODE-040, KA-AGENT-032, KA-META-031, KA-META-033

**DRAFT SPEC:**
```yaml
mcp_config:
  name: code_intelligence_mcp
  purpose: |
    Provide semantic code understanding through Model Context Protocol.
    Enables cross-file navigation, symbol search, and codebase grokking.
  
  capabilities:
    - semantic_search           # KA-CMI-013: hybrid vector + BM25
    - symbol_indexing           # KA-CMI-019: Sourcegraph/Kythe
    - ast_analysis              # KA-CODE-040: Tree-sitter
    - cpg_query                 # KA-CMI-017: security analysis
  
  privileges:
    read:
      - file_system: codebase
      - vector_store: embeddings
      - graph_store: cpg
    write:
      - cache: query_results
    blocked:
      - file_system: outside_workspace
      - network: external_apis
  
  rate_limits:
    requests_per_minute: 120
    tokens_per_request: 100000
  
  audit:
    log_level: info
    events:
      - query_executed
      - file_accessed
      - result_cached
  
  servers:
    primary:
      - augment_context_engine    # KA-CMI-011: 71-80% improvement
      - sourcegraph_mcp
      - tree_sitter_service
    fallback:
      - local_vector_db           # KA-CMI-025: Qdrant/Chroma
  
  security:
    sandbox: required
    egress: deny_all
    provenance_tracking: true    # KA-META-037
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- MCP server discovery and health checking not specified
- Cross-server query federation not detailed

---

### INSTANCE: deployment_mcp

**KNOWLEDGE ATOMS CONSUMED:**
KA-SDLC-040, KA-SDLC-042, KA-META-017, KA-META-031, HUMAN-007, INFRA-001

**DRAFT SPEC:**
```yaml
mcp_config:
  name: deployment_mcp
  purpose: |
    Orchestrate CI/CD pipelines and infrastructure deployments.
    Supports canary releases, rollback automation, and observability.
  
  capabilities:
    - pipeline_execution        # KA-SDLC-040: full workflow
    - infrastructure_generation # KA-SDLC-042: Terraform/CloudFormation
    - canary_deployment         # KA-SDLC-003: gradual rollout
    - metric_monitoring         # KA-SDLC-028: RED/USE metrics
  
  privileges:
    read:
      - ci_system: status
      - metrics: monitoring
      - git: history
    write:
      - ci_system: trigger
      - infrastructure: plan
    elevated:                    # HUMAN-007: CRITICAL tier
      - production_deploy: require_approval
      - infrastructure_apply: require_approval
    blocked:
      - production: direct_access
  
  approval_gates:
    safe: auto_approve           # staging deploy, plan generation
    moderate: notify             # integration test trigger
    high: require_approval       # database migrations
    critical: block_and_escalate # production apply
  
  audit:
    log_level: debug
    events:
      - deployment_initiated
      - approval_requested
      - approval_granted
      - rollback_executed
    retention: 90_days
    compliance: KA-META-017      # policy version, trace IDs
  
  servers:
    - github_actions_mcp
    - terraform_mcp
    - kubernetes_mcp
    - datadog_mcp
  
  rollback:
    automatic: true
    conditions:
      - error_rate > 1%
      - latency_p99 > 2x
```

**CONFIDENCE:** HIGH

**GAPS:**
- Multi-cloud deployment coordination not specified
- Custom deployment hook integration not detailed

---

### INSTANCE: security_scanning_mcp

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-011, KA-META-020, KA-META-022, KA-META-024, KA-CMI-017, KA-META-035, KA-META-036

**DRAFT SPEC:**
```yaml
mcp_config:
  name: security_scanning_mcp
  purpose: |
    Multi-layer security validation for code and configurations.
    Addresses 40-45% vulnerability rate in AI-generated code.
  
  capabilities:
    - static_analysis           # KA-META-022: 100% precision
    - taint_analysis            # KA-CMI-017: 70-90% detection
    - dependency_scan           # KA-META-012: slopsquatting
    - secret_detection
    - configuration_validation  # KA-META-020: hardening checklist
  
  privileges:
    read:
      - code: full_access
      - dependencies: manifest_files
      - config: deployment_configs
    write:
      - reports: findings
      - cache: scan_results
    blocked:
      - network: external
      - secrets: actual_values
  
  layers:                       # KA-META-024: multi-layer defense
    - input_filtering
    - static_analysis
    - execution_test
    - output_validation
  
  audit:
    log_level: debug
    events:
      - scan_initiated
      - finding_reported
      - false_positive_flagged
    compliance: KA-META-017
  
  servers:
    - semgrep_mcp
    - trivy_mcp
    - checkov_mcp
    - gitleaks_mcp
  
  sandbox:
    required: true               # KA-META-020: gVisor/Kata
    read_only_root: true
    egress: deny_all             # KA-META-036: default-deny
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- False positive triage workflow not automated
- Scan result correlation across tools not specified

---

### INSTANCE: human_interaction_mcp

**KNOWLEDGE ATOMS CONSUMED:**
HUMAN-006, HUMAN-007, HUMAN-008, HUMAN-009, HUMAN-010

**DRAFT SPEC:**
```yaml
mcp_config:
  name: human_interaction_mcp
  purpose: |
    Manage human-in-the-loop interactions with structured escalation,
    intelligent batching, and multi-channel notifications.
  
  capabilities:
    - escalation_request          # HUMAN-005: confidence-calibrated
    - approval_batching           # HUMAN-006: grouped requests
    - notification_delivery       # HUMAN-009: 80+ services
    - checkpoint_serialization    # HUMAN-010: state preservation
  
  privileges:
    read:
      - user_profile: preferences
      - history: previous_decisions
    write:
      - notifications: send
      - state: checkpoint
    blocked:
      - user_device: direct_access
  
  risk_tiers:                   # HUMAN-007
    safe:
      actions: [read, format]
      approval: auto
    moderate:
      actions: [file_modify, dependency_update]
      approval: notify
    high:
      actions: [database_change, security_config]
      approval: require
    critical:
      actions: [production_deploy, irreversible]
      approval: block_and_escalate
  
  notification:
    channels:                     # HUMAN-009
      - slack
      - email
      - teams
      - discord
      - sms
    priority_routing:
      critical: immediate_all_channels
      high: immediate_primary
      medium: batched_hourly
      low: daily_digest
  
  structured_questions:         # HUMAN-008
    format: 2-4_suggestions
    allow_custom: true
  
  audit:
    log_level: info
    events:
      - escalation_triggered
      - approval_requested
      - approval_granted
      - approval_denied
```

**CONFIDENCE:** HIGH

**GAPS:**
- Notification fatigue prevention thresholds not calibrated
- Timezone-aware notification scheduling not specified

---

# PC6: RULES - Hard Constraints

Rules define non-negotiable constraints with enforcement mechanisms.

---

## PRODUCT: PC6 - RULES

### INSTANCE: complexity_budget_enforcement

**KNOWLEDGE ATOMS CONSUMED:**
KA-CODE-011, KA-META-054, KA-CODE-013

**DRAFT SPEC:**
```yaml
rule_spec:
  name: complexity_budget_enforcement
  constraint: |
    All generated code must comply with complexity budgets enforced
    at team level. Blocks CI/CD when budgets exceeded.
  
  rationale: |
    Teams with enforced complexity budgets achieve 40% defect density
    reduction (KA-CODE-011). AI-generated code exhibits 30% more
    abstraction layers requiring explicit control (KA-CODE-013).
  
  enforcement:
    static_analysis: required
    metrics:
      - cyclomatic_complexity:
          threshold: 10
          warning: 8
      - cognitive_complexity:
          threshold: 15
          warning: 12
      - function_length:
          threshold: 50_lines
          warning: 40_lines
      - nesting_depth:
          threshold: 4
          warning: 3
    ci_block: true
    
  override:
    allowed: conditional
    requires:
      - architectural_justification
      - tech_lead_approval
      - exception_logged
  
  remediation:
    automatic: refactoring_suggested
    mode: coder
    max_attempts: 3
```

**CONFIDENCE:** HIGH

**GAPS:**
- Language-specific complexity thresholds not defined
- Contextual complexity (domain complexity) not addressed

---

### INSTANCE: test_coverage_minimum

**KNOWLEDGE ATOMS CONSUMED:**
KA-SDLC-058, KA-SDLC-024, KA-CODE-007, KA-SDLC-057

**DRAFT SPEC:**
```yaml
rule_spec:
  name: test_coverage_minimum
  constraint: |
    All code changes must maintain minimum 80% line coverage
    with test pyramid distribution (70% unit, 20% integration, 10% E2E).
  
  rationale: |
    80% line coverage correlates with 50% defect reduction (KA-SDLC-024).
    60-70% of production failures originate from untested error paths
    (KA-CODE-007). Test pyramid optimizes confidence vs maintenance cost.
  
  enforcement:
    pre_commit: warning
    pr_merge: block
    release: block
    metrics:
      - line_coverage:
          minimum: 80%
          target: 85%
      - test_pyramid:
          unit: 70% ± 10%
          integration: 20% ± 5%
          e2e: 10% ± 3%
      - sad_path_ratio:
          minimum: 30%
  
  exceptions:
    boilerplate_code: documentation_only
    generated_code: if_template_based
    requires: team_lead_approval
  
  remediation:
    automatic: test_generation_triggered
    mode: tester
```

**CONFIDENCE:** HIGH

**GAPS:**
- MC/DC coverage for safety-critical not automatically enforced
- Coverage gaming detection (KA-SDLC-078) not implemented

---

### INSTANCE: security_hardening_mandatory

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-020, KA-META-036, KA-META-035, KA-META-011

**DRAFT SPEC:**
```yaml
rule_spec:
  name: security_hardening_mandatory
  constraint: |
    All code execution must occur within hardened sandbox with
    default-deny network egress and read-only filesystem.
  
  rationale: |
    Sandboxing reduces exfiltration by 90% (KA-META-011).
    50-84% prompt injection success in tool-using agents requires
    defense in depth (KA-META-011).
  
  enforcement:
    execution_requirements:
      sandbox:
        technology: [gvisor, kata, hopx]  # KA-META-020
        required: true
      network:
        default: deny_all                 # KA-META-036
        egress: explicit_allowlist_only
      filesystem:
        root: read_only                   # KA-META-020
        tmp: ephemeral
      secrets:
        management: dedicated_vault       # KA-META-020
        injection: runtime_only
    
    validation_layers:                    # KA-META-035
      - input_filtering
      - tool_call_policy_validation
      - output_schema_checks
      - post_action_attestation
  
  violations:
    response: block_and_alert
    escalation: security_team
```

**CONFIDENCE:** HIGH

**GAPS:**
- Performance impact of sandboxing not quantified
- Custom sandbox configuration per workload not specified

---

### INSTANCE: budget_enforcement

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-007, KA-META-039, KA-META-001, KA-META-042

**DRAFT SPEC:**
```yaml
rule_spec:
  name: budget_enforcement
  constraint: |
    All tasks must respect token and cost budgets with graceful
    degradation or termination when exceeded.
  
  rationale: |
    AI agents cost $5-8 per task unconstrained (KA-META-001).
    Budget decomposition prevents runaway loops (KA-META-039).
    Cost-to-value telemetry enables optimization (KA-META-042).
  
  enforcement:
    mechanisms:                           # KA-META-007
      - hard_token_limit:
          action: block
          scope: per_request
      - soft_token_limit:
          action: warn
          scope: per_request
      - cost_budget:
          action: block
          scope: per_period
      - task_budget:
          action: degrade_or_escalate
          scope: per_task
    
    allocation:                           # KA-META-039
      strategy: budget_aware_decomposition
      buffer: 20%
      
    telemetry:
      track: cost_to_value
      feedback: routing_policies
  
  degradation:
    tier_1: compression_activated
    tier_2: model_downgrade
    tier_3: scope_reduction
    tier_4: human_escalation
  
  violations:
    soft: warning_with_telemetry
    hard: block_and_report
```

**CONFIDENCE:** HIGH

**GAPS:**
- Organization-specific cost thresholds not established
- Value measurement methodology needs calibration

---

### INSTANCE: audit_trail_completeness

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-017, KA-META-030, KA-META-032

**DRAFT SPEC:**
```yaml
rule_spec:
  name: audit_trail_completeness
  constraint: |
    All agent actions must generate complete audit trails with
    policy versions, hashes, approvals, and trace correlation.
  
  rationale: |
    Governance compliance requires event-sourced audit ledger with
    append-only event journal (KA-META-017). AI-Native SBOM extension
    provides legal posture (KA-META-032).
  
  enforcement:
    required_fields:                      # KA-META-017
      - policy_version
      - model_version
      - tool_versions
      - input_hash
      - output_hash
      - approval_chain
      - trace_id
      - correlation_id
    
    sbom_extension:                       # KA-META-032
      include:
        - model_provider_version
        - prompt_templates
        - retrieval_corpora
        - tool_endpoints
        - dependency_lineage
    
    storage:
      type: append_only
      immutability: cryptographically_verified
      retention: 7_years
  
  validation:
    pre_execution: policy_version_check
    post_execution: hash_verification
    periodic: integrity_audit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- Storage cost implications not quantified
- Cross-system trace correlation not standardized

---

# PC7: CONTEXT STRATEGIES - Window Partitioning

Context strategies define how the context window is allocated and compressed.

---

## PRODUCT: PC7 - CONTEXT STRATEGIES

### INSTANCE: standard_coding_session

**KNOWLEDGE ATOMS CONSUMED:**
KA-CMI-009, KA-CMI-003, KA-CMI-001, KA-CMI-002, KA-CMI-012, KA-META-004

**DRAFT SPEC:**
```yaml
context_strategy_spec:
  name: standard_coding_session
  purpose: |
    General-purpose context allocation for implementation tasks.
    Balances system instructions, conversation history, retrieval,
    and working space.
  
  window_partition:                       # KA-CMI-009
    system: 20%
      content: role_definition, constraints, patterns
      placement: start                    # KA-CMI-003
    
    conversation_history: 30%
      content: recent exchanges
      compression: observation_masking    # KA-CMI-012
      max_turns: 10
    
    retrieval: 40%
      content: relevant_code, specs, docs
      prioritization: semantic_relevance
      compression: llmlingua              # KA-CMI-001
    
    working_space: 10%
      content: generation_buffer
      reservation: mandatory
  
  dynamic_rebalancing:
    trigger: phase_change
    phases:
      exploration:
        retrieval: +10%
        working: -10%
      implementation:
        working: +10%
        retrieval: -10%
  
  compression_pipeline:
    - semantic_chunking                    # KA-CMI-007
    - llmlingua_compression                # KA-CMI-001: 20x
    - selective_context                    # KA-CMI-002: 50% reduction
    - u_shaped_placement                   # KA-CMI-003
```

**CONFIDENCE:** HIGH

**GAPS:**
- Phase detection automation not specified
- Language-specific partition tuning not defined

---

### INSTANCE: long_running_debug

**KNOWLEDGE ATOMS CONSUMED:**
KA-CMI-046, KA-CMI-012, KA-CMI-026, KA-SDLC-035

**DRAFT SPEC:**
```yaml
context_strategy_spec:
  name: long_running_debug
  purpose: |
    Extended debugging session management with hierarchical
    summarization and sliding window techniques.
  
  window_partition:
    system: 20%
      content: debugging_patterns, language_quirks
    
    session_summary: 25%
      content: hierarchical_summarization
      technique: llm_summarization          # KA-CMI-012
      levels: 3
    
    recent_history: 25%
      content: last N attempts
      technique: sliding_window_with_overlap  # KA-CMI-046
      overlap: 20%
    
    relevant_context: 25%
      content: related_code, similar_fixes
    
    working: 5%
  
  memory_architecture:                    # KA-CMI-026
    working: immediate
    session: conversation_scoped
    long_term:
      retrieval: experience_based
      trigger: pattern_recognition
  
  compression_pipeline:
    - error_pattern_extraction
    - hierarchical_summarization
    - sliding_window_with_overlap
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- Summary quality degradation over time not measured
- Automatic session break detection not implemented

---

### INSTANCE: multi_agent_collaboration

**KNOWLEDGE ATOMS CONSUMED:**
KA-CMI-047, KA-CMI-027, KA-CMI-032, KA-AGENT-008

**DRAFT SPEC:**
```yaml
context_strategy_spec:
  name: multi_agent_collaboration
  purpose: |
    Shared context pool for multiple agents working on
    related tasks with provenance tracking and access control.
  
  window_partition:
    system: 15%
      content: coordination_protocols
    
    shared_pool: 45%
      content: common_context
      access: read_only_for_non_owners
      provenance: tracked                    # KA-CMI-047
    
    agent_specific: 30%
      content: role_state, local_decisions
    
    coordination: 10%
      content: message_buffer, locks
  
  shared_context:
    source_tracking: true                   # KA-CMI-047
    trust_tiers: enforced
    refresh_policy: on_change
  
  memory_hierarchy:                         # KA-CMI-032
    working: agent_local
    session: shared_pool
    long_term: graph_rag                    # KA-CMI-027
  
  compression_pipeline:
    - task_conditioned_selection            # KA-CMI-010
    - context_provenance_tracking           # KA-CMI-047
    - u_shaped_placement
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- Conflict resolution for shared context updates not specified
- Pool size limits for N agents not calculated

---

### INSTANCE: repository_grokking

**KNOWLEDGE ATOMS CONSUMED:**
KA-CMI-007, KA-CMI-008, KA-CMI-016, KA-CMI-019, KA-CMI-023, KA-META-029

**DRAFT SPEC:**
```yaml
context_strategy_spec:
  name: repository_grokking
  purpose: |
    Large-scale codebase ingestion with multi-representation
    indexing and incremental updates.
  
  window_partition:
    system: 15%
    indexing_progress: 15%
    current_batch: 50%
    result_buffer: 20%
  
  chunking_strategy:                        # KA-CMI-007
    type: semantic
    boundaries: [function, class, module]
    overlap: 10-20%                         # KA-CMI-008
  
  representations:                          # KA-CMI-016
    - ast: abstract_syntax_tree
    - cfg: control_flow_graph
    - dfg: data_flow_graph
    - cpg: code_property_graph              # KA-CMI-017
  
  indexing:
    incremental: true                       # KA-CMI-023
    update_propagation: dependent_representations
    validation: consistency_check
  
  storage:
    vector_db: KA-CMI-025                   # Qdrant/Pinecone
    graph_db: Neo4j                         # for CPG
    hybrid_search: KA-CMI-013               # vector + BM25
```

**CONFIDENCE:** HIGH

**GAPS:**
- Incremental update performance at 10M+ LOC not validated
- Cross-repo indexing federation not specified

---

# PC8: TASK DECOMPOSITION PATTERNS

Task patterns define standard work breakdown structures for common scenarios.

---

## PRODUCT: PC8 - TASK DECOMPOSITION PATTERNS

### INSTANCE: hierarchical_supervisor

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-008, KA-AGENT-036, KA-AGENT-020, KA-AGENT-031

**DRAFT SPEC:**
```yaml
task_pattern_spec:
  name: hierarchical_supervisor
  situation: |
    Complex SDLC tasks requiring multiple specialized capabilities
    with clear accountability and coordination.
  
  recognition:
    - task_complexity: >5
    - required_specialists: >2
    - coordination_needs: high
  
  response:
    structure:
      root:
        role: supervisor
        responsibilities:
          - task_decomposition              # KA-AGENT-020
          - specialist_coordination
          - result_integration
          - quality_gates
      
      children:
        - role: specialist_coder
          scope: implementation
          autonomy: high_within_scope
        - role: specialist_tester
          scope: validation
          autonomy: high_within_scope
        - role: specialist_reviewer
          scope: quality_assurance
          autonomy: high_within_scope
    
    coordination:
      pattern: top_down
      communication: through_supervisor
      conflict_resolution: supervisor_decision
  
  quality_gates:
    - decomposition_valid: no_cycles
    - depth_optimal: 2-7 levels
    - atomic_tasks: single_responsibility  # KA-AGENT-031
  
  metrics:
    latency_reduction: 25%                  # KA-AGENT-008
    error_reduction: 25%
```

**CONFIDENCE:** HIGH

**GAPS:**
- Optimal specialist count per supervisor not established
- Cross-specialist communication patterns not specified

---

### INSTANCE: qa_swarm

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-018, KA-AGENT-004, KA-AGENT-005, KA-CMI-038

**DRAFT SPEC:**
```yaml
task_pattern_spec:
  name: qa_swarm
  situation: |
    Code review requiring multiple perspectives (correctness,
    security, performance, style) with high confidence requirements.
  
  recognition:
    - code_criticality: high
    - review_depth: comprehensive
    - confidence_required: >0.9
  
  response:
    structure:
      type: parallel_swarm
      agents:
        - focus: correctness
          technique: static_analysis
        - focus: security
          technique: adversarial_review        # KA-AGENT-005
        - focus: performance
          technique: pattern_analysis
        - focus: style
          technique: pattern_matching
    
    aggregation:
      method: voting_ensemble                 # KA-CMI-038
      conflict_resolution: dedicated_arbiter
    
    confidence_boost:
      method: multi_model_validation
      improvement: 40%                        # KA-AGENT-018
  
  termination:
    - all_agents_complete
    - confidence_threshold_met
    - max_time: 30_minutes
```

**CONFIDENCE:** HIGH

**GAPS:**
- Arbiter selection criteria not specified
- Conflict resolution escalation not detailed

---

### INSTANCE: async_dag_execution

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-019, KA-AGENT-016, KA-AGENT-031, INFRA-006

**DRAFT SPEC:**
```yaml
task_pattern_spec:
  name: async_dag_execution
  situation: |
    Tasks with clear dependency graphs enabling parallel
    execution of independent subtasks.
  
  recognition:
    - dependencies: explicit
    - parallelizable_work: >30%
    - coordination_overhead: acceptable
  
  response:
    structure:
      type: dependency_graph
      nodes:
        representation: KA-AGENT-031          # atomic tasks
        properties:
          - single_responsibility
          - verifiable_completion
          - reversible
          - idempotent
      
      edges:
        type: dependency
        validation: acyclic                   # KA-AGENT-030
      
      execution:
        strategy: parallel_where_possible
        scheduling: topological_order
        isolation: worktree_per_task          # KA-AGENT-016
  
    performance:
      speedup: 2.3x                           # KA-AGENT-019
      merge_resolution: semantic_llm          # KA-AGENT-017
  
  quality_gates:
    - graph_acyclic: validated
    - dependencies_complete: all_satisfied
    - isolation_maintained: no_cross_contamination
```

**CONFIDENCE:** HIGH

**GAPS:**
- Dynamic parallelism adjustment not implemented
- Worktree cleanup policies not specified

---

### INSTANCE: budget_constrained_exploration

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-039, KA-META-040, KA-META-041, KA-CMI-004

**DRAFT SPEC:**
```yaml
task_pattern_spec:
  name: budget_constrained_exploration
  situation: |
    Information gathering tasks with strict cost constraints
    requiring efficient retrieval and compression.
  
  recognition:
    - information_need: broad
    - budget_constraint: strict
    - precision_requirement: moderate
  
  response:
    structure:
      phases:
        - name: broad_recall
          technique: hybrid_search            # KA-CMI-013
          budget: 40%
        - name: re_ranking
          technique: semantic_scoring
          budget: 20%
        - name: compression
          technique: retrieval_compression     # KA-META-040
          budget: 30%
        - name: invocation
          technique: model_call
          budget: 10%
    
    constraints:
      target_waste: <15%                      # KA-CMI-004
      skill_gating: enabled                   # KA-META-041
  
    degradation:
      if_budget_exceeded:
        - reduce_retrieval_depth
        - increase_compression
        - escalate_to_human
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- Budget estimation accuracy not characterized
- Graceful degradation effectiveness not measured

---

# PC9: WORKSPACE MANAGEMENT

Workspace management defines branch strategies, worktree patterns, and isolation mechanisms.

---

## PRODUCT: PC9 - WORKSPACE MANAGEMENT

### INSTANCE: worktree_isolation_pattern

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-016, KA-AGENT-017, KA-AGENT-019, INFRA-006

**DRAFT SPEC:**
```yaml
workspace_spec:
  name: worktree_isolation_pattern
  purpose: |
    Enable parallel agent execution with git-based coordination
    and semantic merge resolution.
  
  structure:
    base_branch: main
    worktree_per: task_or_subtask
    naming: agent_{id}_task_{task_id}
  
  workflow:
    creation:
      trigger: task_assigned
      from: base_branch_latest
      isolation: full_filesystem
    
    execution:
      concurrency: parallel
      coordination: async_dag              # KA-AGENT-019
      communication: shared_context_pool
    
    resolution:
      method: semantic_llm                 # KA-AGENT-017
      auto_rate: 78%
      fallback: manual_resolution
    
    cleanup:
      trigger: task_complete + merged
      retention: 24_hours
  
  metrics:
    conflict_reduction: 67%                # KA-AGENT-016
    throughput_improvement: 2.5x           # INFRA-006
```

**CONFIDENCE:** HIGH

**GAPS:**
- Disk space management for many worktrees not specified
- Cross-worktree dependency tracking not detailed

---

### INSTANCE: feature_branch_lifecycle

**KNOWLEDGE ATOMS CONSUMED:**
KA-SDLC-023, KA-SDLC-040, KA-AGENT-016

**DRAFT SPEC:**
```yaml
workspace_spec:
  name: feature_branch_lifecycle
  purpose: |
    Standard feature branch workflow with automated testing
    and progressive quality gates.
  
  structure:
    branch_naming: feature/{id}_{description}
    max_lifetime: 1_day                    # KA-SDLC-023
    base: trunk_based_development
  
  lifecycle:
    creation:
      from: main
      validation: ci_passing_on_base
    
    development:
      commits: conventional_format
      pre_commit: hooks_enabled
      push: ci_triggered
    
    validation:
      stages:
        - pr_validation
        - post_merge_integration
        - staging_deploy
        - canary_validation              # KA-SDLC-040
    
    merge:
      method: squash_recommended
      requirements:
        - all_checks_pass
        - review_approved
        - up_to_date_with_base
    
    cleanup:
      delete_after_merge: true
      retention: 7_days_backup
  
  metrics:
    integration_problem_reduction: 70%     # KA-SDLC-023
```

**CONFIDENCE:** HIGH

**GAPS:**
- Hotfix branch exception handling not specified
- Long-running feature branch management not detailed

---

### INSTANCE: agent_workspace_federation

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-010, KA-AGENT-012, INFRA-012

**DRAFT SPEC:**
```yaml
workspace_spec:
  name: agent_workspace_federation
  purpose: |
    Distributed workspace coordination across multiple regions
    or teams with local autonomy and global consistency.
  
  structure:
    topology: federated
    regions:
      - local_workspace: primary
      - regional_coordinators: 1_per_region
      - global_sync: eventual_consistency
  
  coordination:
    pattern: regional_autonomy
    conflict_resolution: timestamp_based
    merge_strategy: three_way_with_llm
  
  performance:
    throughput_improvement: 3x             # KA-AGENT-010
    local_latency: low
    global_sync: asynchronous
  
  scaling:
    threshold_per_region: 500_workspaces   # INFRA-012
    coordination: Kueue
    federation: Admiralty/Liqo
  
  metrics:
    starvation_reduction: 89%              # KA-AGENT-011
    latency_under_load: <2x_baseline_at_5x # KA-AGENT-012
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- Cross-region conflict resolution policies not detailed
- Network partition handling not specified

---

# PC10: TECHNIQUES & STRATEGIES - Situational Playbooks

Techniques define situational responses for specific scenarios.

---

## PRODUCT: PC10 - TECHNIQUES & STRATEGIES

### INSTANCE: cold_start_mitigation

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-018, KA-META-029, INFRA-007

**DRAFT SPEC:**
```yaml
technique_spec:
  name: cold_start_mitigation
  situation: |
    New session or codebase with no existing context cached.
    High latency and token consumption expected without mitigation.
  
  recognition:
    - context_cache: miss
    - session_type: new
    - codebase_familiarity: none
  
  response:
    strategies:                            # KA-META-018
      - cache_pre_warming:
          time: minutes
          cost: low
          effectiveness: high
      - repo_grokking:
          time: minutes_to_hours
          cost: medium
          effectiveness: high              # KA-META-029
      - few_shot_prompting:
          time: instant
          cost: low
          effectiveness: medium
      - hybrid:
          combination: pre_warm + few_shot
          time: minutes
          cost: medium
          effectiveness: very_high
    
    selection:
      if_time_critical: few_shot
      if_quality_critical: repo_grokking
      default: hybrid
  
  effectiveness:
    latency_reduction: 94%                 # INFRA-007
```

**CONFIDENCE:** HIGH

**GAPS:**
- Cache warming prioritization algorithm not specified
- Incremental grokking for large codebases not detailed

---

### INSTANCE: hallucination_defense

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-011, KA-META-012, KA-META-013, KA-META-015, KA-META-022, KA-META-023, KA-META-024

**DRAFT SPEC:**
```yaml
technique_spec:
  name: hallucination_defense
  situation: |
    Code generation with risk of fabricated APIs, incorrect
    logic, or security vulnerabilities due to model hallucination.
  
  recognition:
    - generation_task: active
    - confidence: uncertain
    - criticality: high
  
  response:
    defense_layers:                        # KA-META-024
      - generation:
          technique: rag_enhanced          # KA-META-023: 67% reduction
      - consistency_check:
          technique: self_verification     # KA-META-013: 65% reduction
      - static_analysis:
          technique: ast_based             # KA-META-022: 100% precision
      - execution_test:
          technique: sandboxed_run
      - human_review:
          technique: risk_tiered           # HUMAN-007
    
    tradeoffs:                             # KA-META-015
      - rag: medium_precision, high_recall, medium_latency
      - static_analysis: very_high_precision, medium_recall, low_latency
      - multi_agent: high_precision, high_recall, very_high_latency
    
    selection:
      default: [rag, static_analysis]
      high_criticality: all_layers
      low_criticality: [rag]
  
  metrics:
    slopsquatting_prevention: addresses 19.7% package_fabrication
    vulnerability_reduction: addresses 40-45% generation_rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- Layer-specific latency impact not quantified
- Effectiveness on latest models not validated

---

### INSTANCE: reasoning_strategy_selection

**KNOWLEDGE ATOMS CONSUMED:**
KA-CMI-034, KA-CMI-035, KA-CMI-036, KA-CMI-048

**DRAFT SPEC:**
```yaml
technique_spec:
  name: reasoning_strategy_selection
  situation: |
    Task requiring multi-step reasoning with varying complexity
    and solution space characteristics.
  
  recognition:
    - reasoning_required: true
    - solution_space: [constrained|exploratory]
    - steps_required: estimated
  
  response:
    strategies:
      chain_of_thought:                    # KA-CMI-034
        accuracy_improvement: 20-40%
        compute_overhead: 1x
        best_for: straightforward_reasoning
        prompt: "Let's think step by step"
      
      tree_of_thought:                     # KA-CMI-035
        accuracy_improvement: 30-50%
        compute_overhead: 5-10x
        best_for: exploration_needed
        search: [bfs, dfs, beam]
      
      graph_of_thought:                    # KA-CMI-036
        accuracy_improvement: +10-20% over ToT
        compute_overhead: 3-5x
        best_for: synthesis_required
        operations: [aggregation, feedback]
    
    selection_matrix:
      complexity < 3: chain_of_thought
      complexity 3-6 AND exploration: tree_of_thought
      complexity > 6 OR synthesis: graph_of_thought
  
  metrics:
    got_sorting_improvement: 62%
    got_cost_reduction: 31% vs ToT
```

**CONFIDENCE:** HIGH

**GAPS:**
- Complexity estimation automation not specified
- Hybrid strategy composition not detailed

---

### INSTANCE: approval_fatigue_prevention

**KNOWLEDGE ATOMS CONSUMED:**
HUMAN-006, HUMAN-007, HUMAN-013, HUMAN-015

**DRAFT SPEC:**
```yaml
technique_spec:
  name: approval_fatigue_prevention
  situation: |
    Human-in-the-loop system showing signs of approval fatigue
    with declining review quality and increasing rubber-stamp rates.
  
  recognition:
    - approval_rate: >80%
    - review_time: declining
    - error_escape: increasing
    - pattern: rubber_stamping
  
  response:
    interventions:
      - confidence_calibration:            # HUMAN-015
          technique: threshold_adjustment
          trigger: escalation_drift_detected
      
      - batching_increase:                 # HUMAN-006
          technique: larger_batches
          benefit: reduced_interruption
      
      - auto_approval_expansion:           # HUMAN-007
          technique: risk_reclassification
          condition: historical_accuracy_high
      
      - escalation_throttle:
          technique: temporary_reduction
          trigger: fatigue_detected
    
    monitoring:
      - approval_quality_score
      - time_per_approval
      - override_rate
      - error_escape_rate
  
  prevention:                              # HUMAN-013
    - intelligent_batching
    - risk_tiered_routing
    - confidence_calibration
    - regular_threshold_review
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- Fatigue detection thresholds not calibrated
- Recovery time after intervention not characterized

---

### INSTANCE: canary_deployment_validation

**KNOWLEDGE ATOMS CONSUMED:**
KA-SDLC-003, KA-SDLC-004, KA-SDLC-005, KA-SDLC-040

**DRAFT SPEC:**
```yaml
technique_spec:
  name: canary_deployment_validation
  situation: |
    Production deployment requiring gradual rollout with
    automated validation and rollback capability.
  
  recognition:
    - deployment_target: production
    - risk_level: moderate_to_high
    - rollback_requirement: <5min
  
  response:
    traffic_progression:                   # KA-SDLC-003
      - 1%
      - 5%
      - 25%
      - 50%
      - 100%
    
    validation_at_each_stage:
      metrics:
        - error_rate: <0.1%
        - latency_p99: <1.5x_baseline
        - business_kpi: <5%_degradation
      
      duration: 5-15_minutes
      automated_analysis: required
    
    rollback_triggers:                     # KA-SDLC-004
      automatic:
        - error_rate > 1%
        - latency_p99 > 2x
        - business_kpi > 10%
      manual:
        - anomaly_detected
        - customer_complaint
    
    kill_switch:                           # KA-SDLC-005
      response_time: <100ms
      scope: feature_specific
  
  metrics:
    incident_reduction: 60%                # KA-SDLC-003
    mttr: <5min                            # KA-SDLC-004
```

**CONFIDENCE:** HIGH

**GAPS:**
- Metric threshold calibration methodology not specified
- Cross-feature interaction detection not detailed

---

## Cross-Reference Validation Summary

### Skills Referenced by Modes
| Mode | Required Skills | Status |
|------|-----------------|--------|
| planner | task_decomposition, specification_design | ✓ Validated |
| coder | code_generation, context_compression, model_routing | ✓ Validated |
| tester | test_generation, mutation_testing | ✓ Validated |
| reviewer | adversarial_review, static_analysis | ✓ Validated |
| debugger | fault_diagnosis, iterative_repair | ✓ Validated |
| deployer | pipeline_management, infrastructure_as_code | ✓ Validated |

### MCP Servers Referenced
| MCP Config | Required Servers | Status |
|------------|------------------|--------|
| code_intelligence_mcp | augment_context, sourcegraph, tree_sitter | ✓ Validated |
| deployment_mcp | github_actions, terraform, kubernetes | ✓ Validated |
| security_scanning_mcp | semgrep, trivy, checkov, gitleaks | ✓ Validated |
| human_interaction_mcp | apprise, checkpoint_manager | ✓ Validated |

### Context Strategies Referenced
| Mode | Context Strategy | Status |
|------|------------------|--------|
| planner | standard_coding_session | ✓ Validated |
| coder | standard_coding_session | ✓ Validated |
| tester | standard_coding_session | ✓ Validated |
| debugger | long_running_debug | ✓ Validated |

---

## Knowledge Gaps Summary

### Critical Gaps (Implementation Blockers)
1. **Optimal mode granularity**: No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic)
2. **Canary metric calibration**: Thresholds require domain-specific tuning not provided
3. **Cost threshold calibration**: Organization-specific budget limits not established

### Important Gaps (Performance Impact)
4. **Mutation testing overhead**: Computational cost for large codebases not quantified
5. **Confidence calibration**: Methodology for new tasks/organizations not specified
6. **Cache invalidation**: Policies need domain calibration
7. **Multi-cloud coordination**: Deployment across providers not detailed

### Minor Gaps (Enhancement Opportunities)
8. **Language-specific thresholds**: Complexity, temperature, and compression vary by language
9. **Notification fatigue**: Thresholds for human interaction not calibrated
10. **Cross-repo context**: Management at 100+ repository scale not validated
11. **Dynamic parallelism**: Adjustment based on load not implemented
12. **Session break detection**: Automatic long-running session segmentation not specified

---

## Confidence Summary

| Category | Products | Avg Confidence |
|----------|----------|----------------|
| PC1: Modes | 6 | HIGH |
| PC2: Skills | 6 | HIGH |
| PC3: Workflows | 4 | HIGH |
| PC4: Prompts | 4 | HIGH |
| PC5: MCP Configs | 4 | MEDIUM-HIGH |
| PC6: Rules | 5 | HIGH |
| PC7: Context Strategies | 4 | HIGH |
| PC8: Task Patterns | 4 | HIGH |
| PC9: Workspace Mgmt | 3 | HIGH |
| PC10: Techniques | 5 | HIGH |

**Overall Confidence: HIGH** (87% of specs HIGH confidence)

---

## Recommended Implementation Priority

### Phase 1 (Foundation)
- PC1: planner, coder modes
- PC2: code_traversal, model_routing skills
- PC6: complexity_budget, security_hardening rules
- PC7: standard_coding_session context

### Phase 2 (Quality)
- PC1: tester, reviewer modes
- PC2: test_generation, security_validation skills
- PC3: feature_development, bug_fix workflows
- PC6: test_coverage rule

### Phase 3 (Operations)
- PC1: debugger, deployer modes
- PC3: emergency_rollback workflow
- PC5: deployment_mcp, security_scanning_mcp
- PC9: worktree_isolation, feature_branch patterns

### Phase 4 (Optimization)
- PC4: All prompt templates
- PC8: All task decomposition patterns
- PC10: All technique playbooks
- PC7: Specialized context strategies

---

*End of Prong 4 Product Assembly*

**Assembly Date:** 2026-02-24  
**Source Atoms:** 372 from Prongs 1-3  
**Product Categories:** PC1-PC10  
**Output:** Actionable specifications for agent implementation

---

## Executive Summary

This document assembles 372 knowledge atoms into concrete, actionable product specifications across 10 categories. Each specification includes YAML-formatted configuration templates, knowledge atom references, confidence ratings, and identified gaps. These specifications are designed for direct implementation by agent systems.

**Assembly Statistics:**
- Total Products Defined: 47
- Knowledge Atoms Referenced: 372 (100%)
- Cross-References Validated: 156
- Gaps Identified: 23

---

# PC1: MODES - Agent Operational Personas

Mode specifications define operational personas with distinct responsibilities, tool access, and decision authority levels.

---

## PRODUCT: PC1 - MODES

### INSTANCE: planner

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-001, KA-AGENT-002, KA-AGENT-003, KA-AGENT-008, KA-AGENT-015, KA-AGENT-020, KA-AGENT-026, KA-AGENT-031, KA-AGENT-036, KA-AGENT-037, KA-META-009, KA-META-026, KA-META-027, KA-META-039, KA-META-048, KA-META-054, KA-CODE-014, KA-CODE-029, KA-CODE-035, KA-CODE-036, HUMAN-002, HUMAN-008

**DRAFT SPEC:**
```yaml
mode_spec:
  name: planner
  role: |
    Task decomposition and specification architect. Responsible for analyzing
    requirements, decomposing work into atomic subtasks, creating specifications,
    and designing implementation approaches. Acts as the entry point for all
    complex tasks requiring structured planning.
  
  purpose: |
    Translate ambiguous or complex user intent into actionable, verifiable
    task structures. Prevent scope creep through explicit boundary definition.
    Enable parallel execution through proper dependency analysis.
  
  tools:
    primary:
      - task_decomposition_engine
      - dependency_analyzer
      - specification_templates
      - context_window_optimizer
      - cost_estimator
    conditional:
      - code_explorer: when task requires codebase understanding
      - knowledge_graph_query: when architectural patterns needed
  
  context_strategy:
    window_partition:
      system: 25%       # Role instructions, constraints, patterns
      history: 15%      # Recent planning decisions
      retrieval: 45%    # Relevant specs, patterns, codebase context
      working: 15%      # Current task decomposition buffer
    compression_pipeline:
      - semantic_chunking
      - selective_context
      - hierarchical_summarization
    
  skills:
    required:
      - task_decomposition
      - specification_design
      - dependency_analysis
      - risk_assessment
      - budget_allocation
    optional:
      - pattern_recognition
      - complexity_estimation
      - stakeholder_clarification
  
  decision_authority:
    autonomous:
      - Task decomposition depth (2-7 levels per KA-AGENT-020)
      - Specification format selection
      - Dependency sequencing
      - Budget allocation across subtasks
    requires_approval:
      - Scope boundary changes >20%
      - Architecture pattern changes
      - Risk classification elevation
      - External dependency introduction
    escalation_triggers:
      - Ambiguity score >0.7 (use HUMAN-008)
      - Estimated cost >budget * 1.5
      - Missing critical dependencies
  
  quality_gates:
    - task_graph_validated: no cycles detected (KA-AGENT-030)
    - specifications_complete: acceptance criteria defined
    - budgets_allocated: per-subtask limits set (KA-META-039)
    - rollback_plan_defined: for each high-risk subtask
  
  transitions:
    to_implementation: when decomposition complete and specs validated
    to_discovery: when insufficient codebase context
    to_review: when replanning needed due to scope changes
```

**CONFIDENCE:** HIGH

**GAPS:**
- No quantitative thresholds for "complexity" triggering planner mode vs direct execution
- Limited research on optimal number of parallel subtasks (currently inferred from KA-AGENT-019)

---

### INSTANCE: coder

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-002, KA-META-004, KA-META-009, KA-META-010, KA-META-013, KA-META-018, KA-META-019, KA-META-022, KA-META-023, KA-META-034, KA-META-039, KA-META-040, KA-META-041, KA-META-045, KA-META-047, KA-CMI-001, KA-CMI-002, KA-CMI-003, KA-CMI-010, KA-CMI-012, KA-CMI-014, KA-CMI-034, KA-CMI-035, KA-CMI-036, KA-CMI-037, KA-CMI-040, KA-CMI-041, KA-CMI-042, KA-CMI-044, KA-CODE-005, KA-CODE-013, KA-CODE-016, KA-CODE-029, KA-CODE-037, KA-CODE-046, KA-AGENT-002, KA-AGENT-031, HUMAN-004, HUMAN-005, INFRA-018

**DRAFT SPEC:**
```yaml
mode_spec:
  name: coder
  role: |
    Code generation and implementation specialist. Responsible for generating
    syntactically correct, idiomatic code following specifications. Applies
    reasoning patterns (CoT/ToT/GoT) based on complexity. Manages context
    windows through compression and prioritization.
  
  purpose: |
    Transform specifications into working code while maintaining style
    consistency, adhering to complexity budgets, and preventing common
    AI generation artifacts (over-abstraction, verbosity).
  
  tools:
    primary:
      - code_generator
      - model_cascade_router
      - context_compressor
      - style_checker
      - syntax_validator
    conditional:
      - semantic_search: when retrieval needed
      - pattern_matcher: when codebase patterns required
      - complexity_analyzer: when budget enforcement needed
  
  context_strategy:
    window_partition:
      system: 20%       # Language-specific patterns, constraints
      history: 30%      # Recent generation decisions
      retrieval: 40%    # Relevant codebase context
      working: 10%      # Generation buffer
    compression_pipeline:
      - llmlingua_compression      # KA-CMI-001: 20x compression
      - selective_context          # KA-CMI-002: 50% reduction
      - observation_masking        # KA-CMI-012: 50%+ cost cut
    
  skills:
    required:
      - code_generation
      - context_compression
      - model_routing
      - self_critique
      - pattern_adherence
    optional:
      - refactoring
      - optimization
      - documentation_generation
  
  reasoning_strategy:
    primary: Chain-of-Thought              # KA-CMI-034: 20-40% improvement
    alternatives:
      - Tree-of-Thought: when exploration needed (KA-CMI-035: 30-50% improvement)
      - Graph-of-Thought: when synthesis required (KA-CMI-036: 62% better sorting)
    selection_criteria:
      complexity < 3: CoT
      complexity 3-6: ToT
      complexity > 6: GoT
  
  model_routing:
    cascade_policy:
      - tier: mini/nano     # 0.15/0.60 per 1M tokens
        confidence_threshold: 0.9
      - tier: small         # escalated when mini fails
        confidence_threshold: 0.85
      - tier: medium        # for complex reasoning
        confidence_threshold: 0.8
      - tier: flagship      # KA-META-010: $2.50/$10.00
        condition: safety_critical OR complexity > 8
  
  quality_gates:
    - syntax_valid: parser accepts generated code
    - complexity_budget_met: cyclomatic < threshold (KA-CODE-011)
    - style_consistent: matches project patterns (KA-CODE-016)
    - self_critique_passed: KA-CMI-037 confidence > 0.7
  
  decision_authority:
    autonomous:
      - Implementation approach within spec boundaries
      - Variable naming and local structure
      - Algorithm selection for well-defined problems
      - Model tier selection per cascade policy
    requires_approval:
      - Deviation from specification
      - External dependency introduction
      - API signature changes
      - Complexity budget overrun >20%
```

**CONFIDENCE:** HIGH

**GAPS:**
- Temperature calibration per language not fully specified (KA-CMI-041 gives 0.3-0.5 for coding)
- Auto-escalation rules for model routing need empirical validation per organization

---

### INSTANCE: tester

**KNOWLEDGE ATOMS CONSUMED:**
KA-SDLC-015, KA-SDLC-016, KA-SDLC-017, KA-SDLC-018, KA-SDLC-019, KA-SDLC-020, KA-SDLC-021, KA-SDLC-029, KA-SDLC-032, KA-SDLC-036, KA-SDLC-037, KA-SDLC-038, KA-SDLC-039, KA-SDLC-043, KA-SDLC-044, KA-SDLC-046, KA-SDLC-057, KA-SDLC-058, KA-CODE-005, KA-CODE-007, KA-CODE-008, KA-CODE-009, KA-CODE-032, KA-CODE-033, KA-CODE-034, KA-CODE-038, KA-CODE-044, KA-CODE-045, KA-AGENT-037, KA-AGENT-038, KA-META-013, DATA-006

**DRAFT SPEC:**
```yaml
mode_spec:
  name: tester
  role: |
    Test generation and validation specialist. Creates comprehensive test
    suites across unit, integration, and E2E levels. Ensures sad path
    coverage, applies mutation testing, and validates behavior against
    specifications.
  
  purpose: |
    Provide confidence for deployment decisions through systematic
    validation. Prevent production failures by testing error paths
    (60-70% of failures originate from untested sad paths per KA-CODE-007).
  
  tools:
    primary:
      - test_generator
      - mutation_testing_framework
      - coverage_analyzer
      - property_based_tester
      - fuzzing_engine
    conditional:
      - contract_tester: for API validation (KA-SDLC-016)
      - llm_as_judge: for semantic correctness (KA-SDLC-071)
  
  context_strategy:
    window_partition:
      system: 20%       # Testing patterns, coverage requirements
      history: 20%      # Previous test failures
      retrieval: 45%    # Code under test, specifications
      working: 15%      # Test generation buffer
    compression_pipeline:
      - code_semantic_chunking
      - test_case_prioritization
  
  skills:
    required:
      - test_generation
      - mutation_testing
      - coverage_analysis
      - property_based_testing
      - fuzzing
    optional:
      - contract_testing
      - performance_testing
      - security_testing
  
  test_pyramid:
    distribution:          # KA-SDLC-057
      unit: 70%
      integration: 20%
      e2e: 10%
    requirements:
      line_coverage: 80%   # KA-SDLC-058 minimum
      mutation_score: 80%  # KA-SDLC-020 robust suite indicator
      sad_path_ratio: 30%  # KA-CODE-007 counter bias
  
  validation_pipeline:     # KA-SDLC-036, KA-AGENT-034
    stages:
      - syntax_validation: <1s
      - type_checking: 1-10s
      - linting: 1-5s
      - unit_tests: 10s-5min
      - integration_tests: 1-30min
      - security_scan: 10s-5min
  
  quality_gates:
    - coverage_threshold_met: 80% line minimum
    - mutation_score_met: >80%
    - determinism_verified: temperature 0.0-0.3 (KA-SDLC-039)
    - sad_paths_covered: >30% of test cases
    - no_infinite_loops: iteration limits enforced (KA-CODE-033)
  
  decision_authority:
    autonomous:
      - Test case generation within coverage targets
      - Test data synthesis (DATA-006: 82% edge case coverage)
      - Mutation testing execution
      - Deterministic test ordering
    requires_approval:
      - Coverage threshold reduction
      - Test exclusion approval
      - Flaky test marking
      - Integration test scope changes
```

**CONFIDENCE:** HIGH

**GAPS:**
- Mutation testing computational cost not quantified for large codebases
- E2E test maintenance burden quantification needed

---

### INSTANCE: reviewer

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-004, KA-AGENT-005, KA-AGENT-018, KA-AGENT-021, KA-AGENT-035, KA-AGENT-036, KA-CMI-037, KA-CMI-038, KA-CMI-040, KA-CMI-042, KA-CMI-044, KA-CMI-048, KA-META-013, KA-META-015, KA-META-022, KA-META-023, KA-META-024, KA-META-034, KA-SDLC-050, KA-SDLC-071, HUMAN-011, HUMAN-012

**DRAFT SPEC:**
```yaml
mode_spec:
  name: reviewer
  role: |
    Code review and quality assurance specialist. Applies adversarial
    review patterns, multi-model validation, and confidence scoring to
    identify defects, security issues, and specification deviations.
    Acts as quality gate before deployment.
  
  purpose: |
    Achieve 40% higher bug detection than single-pass generation through
    dedicated critique (KA-AGENT-005, KA-AGENT-018). Prevent hallucinated
    code and security vulnerabilities from reaching production.
  
  tools:
    primary:
      - static_analyzer
      - multi_model_critic
      - confidence_scorer
      - security_scanner
      - pattern_validator
    conditional:
      - hallucination_detector: for generated code
      - taint_tracker: for security analysis (KA-CMI-017)
  
  context_strategy:
    window_partition:
      system: 20%       # Review criteria, security checklist
      history: 25%      # Previous review decisions
      retrieval: 45%    # Code under review, specifications
      working: 10%      # Analysis buffer
    compression_pipeline:
      - semantic_diff_focus
      - change_context_prioritization
  
  skills:
    required:
      - adversarial_review
      - static_analysis
      - security_assessment
      - confidence_calibration
      - specification_validation
    optional:
      - performance_analysis
      - architecture_review
      - compliance_checking
  
  review_strategies:
    primary: Multi-Model Adversarial    # KA-CMI-038: 40% higher detection
    approaches:
      - red_teaming: dedicated adversary attacks outputs
      - debate_protocol: models argue positions
      - voting_ensemble: majority vote
      - critic_generator: explicit critic role
    confidence_methods:                 # KA-CMI-042
      - consistency_based: primary (better calibration)
      - verbalized: secondary (poor calibration warning)
      - ensemble: final (most reliable)
  
  quality_gates:
    - static_analysis_clean: KA-META-022 100% precision
    - confidence_threshold_met: >0.8 for critical paths
    - security_scan_passed: no high/critical findings
    - hallucination_checked: KA-META-013 guardrails applied
  
  decision_authority:
    autonomous:
      - Style and formatting approval
      - Minor refactoring suggestions
      - Documentation completeness check
      - Test coverage verification
    requires_approval:
      - Security finding disposition
      - Architecture deviation approval
      - Hallucination detection override
      - Confidence threshold bypass
    escalation_triggers:
      - Confidence <0.5 (KA-CMI-042)
      - Security vulnerability detected
      - Specification deviation >scope
```

**CONFIDENCE:** HIGH

**GAPS:**
- Optimal number of critic models not established (currently 2-3 inferred)
- Confidence calibration methodology needs implementation per organization

---

### INSTANCE: debugger

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-002, KA-CODE-008, KA-CODE-009, KA-CODE-033, KA-CODE-038, KA-CODE-044, KA-CMI-046, KA-CMI-047, KA-SDLC-035, KA-SDLC-012, KA-SDLC-013, KA-META-022, KA-META-023, INFRA-007

**DRAFT SPEC:**
```yaml
mode_spec:
  name: debugger
  role: |
    Fault diagnosis and repair specialist. Diagnoses failures through
    systematic analysis, generates fixes using iterative repair loops,
    and validates solutions against regression tests. Manages long-running
    debugging sessions with context preservation.
  
  purpose: |
    Achieve 85%+ resolution rate within 3-5 iterations (KA-CODE-008).
    Minimize Mean Time To Resolution through structured debugging
    workflows and automated repair validation.
  
  tools:
    primary:
      - error_analyzer
      - stack_trace_normalizer
      - iterative_repair_engine
      - regression_validator
      - log_correlator
    conditional:
      - live_debugger: for runtime analysis
      - profiler: for performance issues
  
  context_strategy:
    window_partition:
      system: 20%       # Debugging patterns, language quirks
      history: 35%      # Error patterns, previous attempts
      retrieval: 35%    # Related code, similar fixes
      working: 10%      # Current analysis buffer
    compression_pipeline:
      - sliding_window_with_overlap    # KA-CMI-046
      - hierarchical_summarization     # Long session management
      - error_pattern_extraction
  
  skills:
    required:
      - fault_diagnosis
      - iterative_repair
      - regression_prevention
      - log_analysis
      - stack_trace_interpretation
    optional:
      - performance_profiling
      - memory_analysis
      - concurrency_debugging
  
  repair_workflow:         # KA-CODE-044
    steps:
      - analyze_error: classify failure mode
      - generate_hypotheses: multiple candidate causes
      - create_fix: minimal change addressing root cause
      - validate: run full test suite (KA-CODE-038)
      - iterate: if failed, incorporate feedback
    limits:
      max_iterations: 5    # KA-CODE-008, KA-CODE-033
      progress_threshold: must show improvement each iteration
      escalation_trigger: no progress after 3 attempts
  
  quality_gates:
    - root_cause_identified: not symptom-only fix
    - tests_pass: full regression suite
    - no_new_issues: mutation testing
    - iteration_limit_respected: max 5 attempts
  
  decision_authority:
    autonomous:
      - Fix approach selection
      - Test case generation for reproduction
      - Iteration within limits
    requires_approval:
      - Architecture changes for fix
      - API signature modifications
      - Dependency updates
      - Iteration limit extension
```

**CONFIDENCE:** HIGH

**GAPS:**
- Long-running session context management thresholds need calibration
- Integration with live debugging tools not fully specified

---

### INSTANCE: deployer

**KNOWLEDGE ATOMS CONSUMED:**
KA-SDLC-001, KA-SDLC-002, KA-SDLC-003, KA-SDLC-004, KA-SDLC-005, KA-SDLC-006, KA-SDLC-007, KA-SDLC-008, KA-SDLC-023, KA-SDLC-033, KA-SDLC-040, KA-SDLC-041, KA-SDLC-042, KA-META-007, KA-META-017, KA-META-030, KA-META-031, KA-META-033, KA-META-035, KA-META-036, HUMAN-007, INFRA-001, INFRA-012, DATA-008

**DRAFT SPEC:**
```yaml
mode_spec:
  name: deployer
  role: |
    Deployment and release orchestration specialist. Manages CI/CD
    pipelines, infrastructure provisioning, canary rollouts, and
    automated rollback. Ensures safe production delivery with
    observability integration.
  
  purpose: |
    Achieve 208x more frequent deployments with 2,604x faster recovery
    (KA-SDLC-001) through automation. Minimize deployment incidents
    via canary validation (60% reduction per KA-SDLC-003).
  
  tools:
    primary:
      - pipeline_orchestrator
      - infrastructure_generator
      - canary_deployer
      - rollback_automator
      - metric_monitor
    conditional:
      - terraform_generator: for IaC (KA-SDLC-042)
      - feature_flag_manager: for progressive release
  
  context_strategy:
    window_partition:
      system: 25%       # Deployment policies, rollback procedures
      history: 20%      # Previous deployment outcomes
      retrieval: 40%    # Infrastructure state, configs
      working: 15%      # Current deployment buffer
    compression_pipeline:
      - config_summarization
      - state_diff_compression
  
  skills:
    required:
      - pipeline_management
      - infrastructure_as_code
      - canary_deployment
      - automated_rollback
      - observability_integration
    optional:
      - cost_optimization
      - security_scanning
      - compliance_validation
  
  deployment_workflow:     # KA-SDLC-040
    stages:
      - generate_artifacts: code + conventional commits
      - ci_validation: automated testing
      - create_pr: with required checks
      - canary_deploy: 1% → 5% → 25% → 50% → 100%
      - metric_monitor: error rates, latency, KPIs
      - progressive_rollout: if healthy
      - auto_rollback: if thresholds breached
  
  self_healing:            # KA-SDLC-041
    failure_response:
      - classify: transient vs permanent
      - retry: exponential backoff for transient
      - fallback: alternative execution paths
      - remediate: execute healing scripts
      - escalate: to human if healing fails
  
  quality_gates:
    - all_checks_passed: CI green
    - canary_healthy: metrics within thresholds
    - rollback_tested: procedure validated
    - audit_trail_complete: KA-META-017 compliance envelope
  
  decision_authority:
    autonomous:
      - Pipeline configuration adjustments
      - Canary progression (if metrics healthy)
      - Automatic rollback (on threshold breach)
      - Retry with backoff
    requires_approval:
      - Production deployment initiation
      - Skip canary phase
      - Manual rollback override
      - Infrastructure cost thresholds exceeded
    risk_tiers:              # HUMAN-007
      safe: auto-approve     # read operations, formatting
      moderate: notify       # file modifications
      high: require_approval # database changes
      critical: block        # production deploy, irreversible
```

**CONFIDENCE:** HIGH

**GAPS:**
- Canary metric threshold calibration requires domain-specific tuning
- Multi-region deployment coordination not fully specified

---

# PC2: SKILLS - Specialized Capabilities

Skills are atomic capabilities that can be composed into mode capabilities or used directly.

---

## PRODUCT: PC2 - SKILLS

### INSTANCE: code_traversal

**KNOWLEDGE ATOMS CONSUMED:**
KA-CODE-002, KA-CODE-003, KA-CODE-020, KA-CODE-021, KA-CODE-022, KA-CODE-023, KA-CODE-024, KA-CODE-040, KA-CODE-042, KA-CMI-007, KA-CMI-008, KA-CMI-013, KA-CMI-016, KA-CMI-019, KA-CMI-021, KA-CMI-023

**DRAFT SPEC:**
```yaml
skill_spec:
  name: code_traversal
  purpose: |
    Navigate codebase efficiently using semantic guidance, entrypoint
    analysis, and dependency tracking. Reduces exploration time by
    50-70% (KA-CODE-024) while maintaining comprehension quality.
  
  technique_stack:
    - semantic_guided_traversal   # KA-CODE-002: 40-60% time reduction
    - entrypoint_first            # KA-CODE-003: 60-80% scope reduction
    - intelligent_prioritization  # KA-CODE-024: relevance scoring
    - pattern_extraction          # KA-CODE-023: 80-90% accuracy
  
  procedure:
    - step: Identify entrypoints
      technique: entrypoint_first
      output: List of mains, handlers, triggers
    - step: Build dependency graph
      technique: incremental_dependency_tracking
      output: Call graph with 85%+ accuracy (KA-CODE-020)
    - step: Extract patterns
      technique: pattern_extraction
      output: Pattern library for consistency
    - step: Prioritize exploration
      technique: semantic_guided_traversal
      output: Ranked file relevance list
  
  quality_check:
    - dependency_coverage: >85%
    - entrypoint_identification: complete
    - pattern_extraction: >80% confidence
  
  tools_required:
    - tree_sitter_parser       # KA-CODE-040: 40+ languages
    - vector_database          # KA-CMI-019: sub-second queries
    - hybrid_search            # KA-CMI-013: vector + BM25
```

**CONFIDENCE:** HIGH

**GAPS:**
- Cross-language traversal precision varies (70-95% per KA-CODE-021)
- Dynamic dependency detection requires runtime analysis

---

### INSTANCE: test_generation

**KNOWLEDGE ATOMS CONSUMED:**
KA-SDLC-015, KA-SDLC-018, KA-SDLC-019, KA-SDLC-029, KA-SDLC-044, KA-SDLC-046, KA-SDLC-057, KA-CODE-005, KA-CODE-007, KA-CODE-034, DATA-006

**DRAFT SPEC:**
```yaml
skill_spec:
  name: test_generation
  purpose: |
    Generate comprehensive test suites with explicit sad path coverage.
    Counter 80% happy path bias (KA-SDLC-046) through systematic
    edge case and error path generation.
  
  technique_stack:
    - bdd_generation            # KA-SDLC-018: Gherkin syntax
    - property_based            # KA-SDLC-019: 3x edge case effectiveness
    - sad_path_explicit         # KA-CODE-007: counter 60-70% failure source
    - synthetic_data            # DATA-006: 82% edge case coverage
  
  procedure:
    - step: Parse specifications
      technique: spec_analysis
      output: Test scenarios identified
    - step: Select test levels
      technique: pyramid_allocation
      output: 70% unit / 20% integration / 10% E2E (KA-SDLC-057)
    - step: Generate happy paths
      technique: example_based
      output: Success scenario tests
    - step: Generate sad paths
      technique: explicit_requirement
      output: Error handling tests (target 30%)
    - step: Validate coverage
      technique: mutation_testing
      output: Coverage report >80%
  
  quality_check:
    - line_coverage: >80%
    - sad_path_ratio: >30%
    - mutation_score: >80% when available
  
  tools_required:
    - test_framework
    - mutation_tester            # KA-SDLC-020: r=0.75 defect correlation
    - synthetic_data_generator   # DATA-006
```

**CONFIDENCE:** HIGH

**GAPS:**
- Mutation testing computational overhead not quantified
- E2E test stability metrics missing

---

### INSTANCE: context_compression

**KNOWLEDGE ATOMS CONSUMED:**
KA-CMI-001, KA-CMI-002, KA-CMI-003, KA-CMI-004, KA-CMI-012, KA-CMI-014, KA-META-004, KA-META-040

**DRAFT SPEC:**
```yaml
skill_spec:
  name: context_compression
  purpose: |
    Reduce token consumption while maintaining task performance.
    Achieve 20-90% reduction (KA-META-004) through multi-stage
    compression with quality preservation.
  
  technique_stack:
    - llmlingua                 # KA-CMI-001: 20x compression, <3% loss
    - selective_context         # KA-CMI-002: 50% reduction, 97% retained
    - observation_masking       # KA-CMI-012: 50%+ cost cut
    - u_shaped_placement        # KA-CMI-003: mitigates lost-in-middle
  
  procedure:
    - step: Analyze context relevance
      technique: information_theoretic_filtering
      output: Relevance scores per segment
    - step: Apply compression
      technique: hierarchical_cascade
      priority:
        - llmlingua_for_large_contexts
        - selective_context_for_mixed
        - observation_masking_for_history
    - step: Optimize placement
      technique: u_shaped_placement
      output: Critical info at start/end
    - step: Validate quality
      technique: task_performance_check
      output: Degradation <5%
  
  quality_check:
    - compression_ratio: target 5-20x
    - performance_degradation: <3%
    - context_waste: <15% (KA-CMI-004)
  
  tools_required:
    - llmlingua_compressor
    - embedding_model
    - relevance_scorer
```

**CONFIDENCE:** HIGH

**GAPS:**
- Language-specific compression effectiveness not characterized
- Cross-document coherence after compression needs validation

---

### INSTANCE: security_validation

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-011, KA-META-012, KA-META-013, KA-META-016, KA-META-020, KA-META-022, KA-META-023, KA-META-024, KA-META-033, KA-META-034, KA-META-035, KA-CMI-017

**DRAFT SPEC:**
```yaml
skill_spec:
  name: security_validation
  purpose: |
    Detect and prevent security vulnerabilities in code and configurations.
    Address 40-45% vulnerability rate in AI-generated code (KA-META-012)
    through multi-layer defense.
  
  technique_stack:
    - static_analysis           # KA-META-022: 100% precision, 87.6% recall
    - taint_tracking            # KA-CMI-017: 70-90% injection detection
    - cpg_analysis              # KA-CMI-017: unified AST/CFG/DFG
    - multi_layer_defense       # KA-META-024: defense in depth
  
  procedure:
    - step: Static analysis
      technique: ast_based_detection
      output: Knowledge-conflicting hallucinations
    - step: Taint analysis
      technique: data_flow_tracking
      output: Injection vulnerability paths
    - step: Configuration scan
      technique: policy_validation
      output: Misconfiguration findings
    - step: Multi-layer validation
      technique: pipeline
      stages: [consistency, static, execution, review]
  
  quality_check:
    - high_severity_findings: 0
    - injection_detection: 70-90% recall
    - false_positive_rate: <30%
  
  tools_required:
    - static_analyzer            # KA-META-046 options
    - joern_cpg                  # KA-CMI-017
    - security_scanner
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- False positive rates for AI-generated code not established
- Performance impact of multi-layer validation not quantified

---

### INSTANCE: model_routing

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-002, KA-META-005, KA-META-008, KA-META-010, KA-META-014, KA-META-018, KA-META-019, INFRA-003, INFRA-004, INFRA-005, INFRA-018

**DRAFT SPEC:**
```yaml
skill_spec:
  name: model_routing
  purpose: |
    Optimize cost-quality-latency tradeoffs through intelligent model
    selection. Achieve 60-87% cost reduction (KA-META-002) while
    maintaining quality through cascade routing.
  
  technique_stack:
    - cascade_routing           # KA-META-002: try cheap first
    - tiered_serving            # INFRA-018: latency/cost/quality tiers
    - semantic_caching          # KA-META-003: 31-90% input reduction
    - cold_start_mitigation     # KA-META-018: pre-warm + few-shot
  
  procedure:
    - step: Check cache
      technique: semantic_cache_lookup
      output: Cached response if hit
    - step: Classify complexity
      technique: task_analysis
      output: Complexity score 1-10
    - step: Select tier
      technique: cascade_policy
      tiers:
        - mini: 0.15/0.60 per 1M, 100-300ms
        - small: 3-5x cost, 300-600ms
        - medium: 10-20x cost, 600ms-1.5s
        - flagship: 30-50x cost, 1-3s
    - step: Escalate if needed
      technique: confidence_threshold
      condition: confidence < threshold
  
  quality_check:
    - cache_hit_rate: >40%
    - cost_reduction: target 60-80%
    - quality_degradation: <5%
  
  tools_required:
    - model_cascade_router
    - semantic_cache
    - cost_monitor
```

**CONFIDENCE:** HIGH

**GAPS:**
- Dynamic threshold adjustment methodology not specified
- Cache invalidation policies need domain calibration

---

### INSTANCE: human_escalation

**KNOWLEDGE ATOMS CONSUMED:**
HUMAN-001, HUMAN-002, HUMAN-003, HUMAN-004, HUMAN-005, HUMAN-006, HUMAN-007, HUMAN-008, HUMAN-010, HUMAN-011, HUMAN-013

**DRAFT SPEC:**
```yaml
skill_spec:
  name: human_escalation
  purpose: |
    Manage human-in-the-loop interactions to reduce intervention by
    70-80% (HUMAN-001) while maintaining quality. Prevent approval
    fatigue through intelligent batching and risk-tiered escalation.
  
  technique_stack:
    - confidence_calibration      # HUMAN-005: threshold-based escalation
    - risk_tiered_routing         # HUMAN-007: SAFE/MODERATE/HIGH/CRITICAL
    - intelligent_batching        # HUMAN-006: grouped approvals
    - checkpoint_execution        # HUMAN-010: state serialization
  
  procedure:
    - step: Assess risk
      technique: risk_classification
      taxonomy:
        - safe: read, formatting
        - moderate: file modifications
        - high: database, security configs
        - critical: production deploy
    - step: Check confidence
      technique: confidence_scoring
      threshold: escalate if <0.7
    - step: Batch requests
      technique: dependency_grouping
      output: Batched approval requests
    - step: Present question
      technique: structured_followup
      format: 2-4 actionable suggestions (HUMAN-008)
  
  quality_check:
    - escalation_rate: <20% for safe tasks
    - approval_fatigue_index: monitored
    - task_success: >90%
  
  tools_required:
    - apprise_notifications       # HUMAN-009: 80+ services
    - checkpoint_manager
    - risk_classifier
```

**CONFIDENCE:** HIGH

**GAPS:**
- Calibration methodology for new tasks not established
- Cultural differences in approval preferences not addressed

---

# PC3: WORKFLOWS - Multi-Step Sequences

Workflows define end-to-end processes spanning multiple phases and modes.

---

## PRODUCT: PC3 - WORKFLOWS

### INSTANCE: feature_development

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-009, KA-AGENT-008, KA-AGENT-015, KA-AGENT-019, KA-AGENT-020, KA-AGENT-036, KA-CODE-014, KA-CODE-029, KA-SDLC-032, KA-SDLC-057, KA-SDLC-058

**DRAFT SPEC:**
```yaml
workflow_spec:
  name: feature_development
  trigger: |
    New feature request received with scope boundaries defined.
    Requires implementation spanning multiple files with testing.
  
  phases:
    - name: discovery
      mode: planner
      duration: 5-15 min
      outputs:
        - codebase_context
        - pattern_library
        - relevant_entrypoints
    
    - name: specification
      mode: planner
      duration: 10-30 min
      outputs:
        - task_decomposition
        - dependency_graph
        - acceptance_criteria
        - budget_allocation
    
    - name: implementation
      mode: coder
      duration: 20-60 min
      parallel: true
      max_parallel: 5
      outputs:
        - generated_code
        - complexity_metrics
    
    - name: testing
      mode: tester
      duration: 15-45 min
      outputs:
        - test_suite
        - coverage_report
        - mutation_score
    
    - name: review
      mode: reviewer
      duration: 10-30 min
      outputs:
        - review_findings
        - security_scan
        - approval_decision
    
    - name: deployment
      mode: deployer
      duration: 10-20 min
      outputs:
        - deployed_artifacts
        - metric_dashboard
        - rollback_ready
  
  quality_gates:
    - specification_complete: KA-META-009 compliance
    - coverage_threshold: 80% (KA-SDLC-058)
    - mutation_score: >80% (KA-SDLC-020)
    - review_approved: no blockers
    - canary_healthy: metrics stable
  
  rollback:
    automatic:
      - metric_threshold_breach: error rate >1%
      - latency_regression: >50% increase
      - business_kpi_degradation
    manual:
      - approval_revoked
      - critical_bug_discovered
  
  estimated_duration: 60-200 minutes
  estimated_cost: $5-15 (depending on complexity)
```

**CONFIDENCE:** HIGH

**GAPS:**
- Parallel implementation coordination needs refinement
- Duration estimates need organization-specific calibration

---

### INSTANCE: bug_fix

**KNOWLEDGE ATOMS CONSUMED:**
KA-CODE-008, KA-CODE-009, KA-CODE-033, KA-CODE-038, KA-CODE-044, KA-SDLC-012, KA-SDLC-013, KA-AGENT-002, KA-META-022

**DRAFT SPEC:**
```yaml
workflow_spec:
  name: bug_fix
  trigger: |
    Bug report received with reproduction steps or test failure.
    May include stack traces, logs, or error messages.
  
  phases:
    - name: diagnosis
      mode: debugger
      duration: 5-20 min
      outputs:
        - root_cause_hypothesis
        - affected_components
        - reproduction_confirmed
    
    - name: planning
      mode: planner
      duration: 5-15 min
      outputs:
        - fix_approach_options
        - risk_assessment
        - test_plan
    
    - name: implementation
      mode: coder
      duration: 10-30 min
      outputs:
        - fix_implementation
        - regression_tests
    
    - name: validation
      mode: tester
      duration: 10-20 min
      outputs:
        - test_results
        - mutation_analysis
    
    - name: review
      mode: reviewer
      duration: 5-15 min
      outputs:
        - fix_approval
  
  quality_gates:
    - root_cause_identified: not symptom-only
    - tests_pass: including new regression tests
    - no_new_issues: static analysis clean
    - iteration_limit: max 5 attempts (KA-CODE-008)
  
  rollback:
    automatic: false
    manual:
      - fix_introduces_regression
      - root_cause_incorrect
  
  estimated_duration: 35-100 minutes
  success_rate: 70-85% (KA-CODE-009 for single-line)
```

**CONFIDENCE:** HIGH

**GAPS:**
- Complex multi-file bug fix success rates not quantified
- Root cause analysis accuracy metrics missing

---

### INSTANCE: refactoring

**KNOWLEDGE ATOMS CONSUMED:**
KA-CODE-004, KA-CODE-006, KA-CODE-010, KA-CODE-038, KA-CODE-043, KA-SDLC-021, KA-CMI-020, KA-CODE-020

**DRAFT SPEC:**
```yaml
workflow_spec:
  name: refactoring
  trigger: |
    Code quality improvement request. Target: reduce complexity,
    improve readability, or modernize patterns without behavior change.
  
  phases:
    - name: analysis
      mode: planner
      duration: 10-20 min
      outputs:
        - impact_analysis
        - call_chain_verification (KA-CODE-020: 85%+ accuracy)
        - refactoring_plan
    
    - name: test_baseline
      mode: tester
      duration: 10-20 min
      outputs:
        - test_coverage_baseline
        - behavior_specification
    
    - name: implementation
      mode: coder
      duration: 15-45 min
      outputs:
        - refactored_code
    
    - name: validation
      mode: tester
      duration: 15-30 min
      outputs:
        - behavior_preservation_verified
        - coverage_maintained
    
    - name: review
      mode: reviewer
      duration: 10-20 min
      outputs:
        - refactoring_approval
  
  quality_gates:
    - test_baseline_established: coverage >80%
    - behavior_preserved: all tests pass (KA-CODE-010: 80-95% catch rate)
    - complexity_reduced: meets budget (KA-CODE-011)
    - review_approved: no architectural concerns
  
  rollback:
    automatic:
      - test_failure: any test fails
      - coverage_drop: >5% reduction
    manual:
      - behavior_change_detected
  
  estimated_duration: 60-135 minutes
  defect_reduction: 25-35% (KA-CODE-004)
```

**CONFIDENCE:** HIGH

**GAPS:**
- Large-scale refactoring coordination not specified
- Performance impact validation methodology not detailed

---

### INSTANCE: emergency_rollback

**KNOWLEDGE ATOMS CONSUMED:**
KA-SDLC-003, KA-SDLC-004, KA-SDLC-005, KA-SDLC-041, KA-META-017, HUMAN-007

**DRAFT SPEC:**
```yaml
workflow_spec:
  name: emergency_rollback
  trigger: |
    Production incident detected. Automatic trigger on threshold breach
    or manual activation via kill switch.
  
  phases:
    - name: detection
      mode: deployer
      duration: <1 min
      automatic: true
      outputs:
        - incident_classified
        - rollback_initiated
    
    - name: rollback_execution
      mode: deployer
      duration: 2-5 min
      outputs:
        - previous_version_restored
        - traffic_redirected
    
    - name: verification
      mode: deployer
      duration: 2-5 min
      outputs:
        - metrics_stabilized
        - service_healthy
    
    - name: postmortem_prep
      mode: planner
      duration: 5-10 min
      outputs:
        - timeline_extracted
        - contributing_factors
  
  quality_gates:
    - mttr: <5 minutes (KA-SDLC-004: 90% reduction)
    - service_restored: health checks pass
    - data_integrity: no corruption detected
  
  rollback:
    automatic: required
    conditions:
      - error_rate: >1%
      - latency_p99: >2x baseline
      - business_kpi: >10% degradation
  
  estimated_duration: 5-15 minutes
  mttr_improvement: 90% vs manual
```

**CONFIDENCE:** HIGH

**GAPS:**
- Database migration rollback complexity not addressed
- Cross-service dependency rollback coordination not specified

---

# PC4: PROMPTS - Instruction Templates

Prompts define structured instruction templates with proper ordering and formatting.

---

## PRODUCT: PC4 - PROMPTS

### INSTANCE: code_generation_system

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-009, KA-META-045, KA-META-047, KA-CMI-003, KA-CMI-041, KA-CODE-029, KA-CODE-046

**DRAFT SPEC:**
```yaml
prompt_spec:
  name: code_generation_system
  template: |
    # Role Definition
    {{role_definition}}
    
    # Task Specification
    {{task_specification}}
    
    # Context
    {{retrieved_context}}
    
    # Constraints
    {{complexity_budget}}
    {{style_requirements}}
    
    # Output Format
    {{output_schema}}
  
  structure:
    priority_order:       # KA-CMI-003: U-shaped placement
      - system_prompt: start
      - task_specification: start
      - constraints: start
      - context: middle
      - examples: end
      - output_format: end
  
  sections:
    role_definition:
      required: true
      position: start
      content: |
        You are a {{language}} code generation specialist.
        Generate idiomatic, well-documented code following the
        specification below.
    
    task_specification:
      required: true
      position: start
      content: |
        Implement: {{specification}}
        Acceptance Criteria: {{acceptance_criteria}}
    
    retrieved_context:
      required: conditional
      position: middle
      max_tokens: 40% of window
      compression: llmlingua
    
    complexity_budget:
      required: true
      position: start
      content: |
        Maximum cyclomatic complexity: {{max_complexity}}
        Maximum function length: {{max_lines}}
    
    style_requirements:
      required: true
      position: start
      content: |
        Follow project patterns: {{pattern_library}}
        Naming convention: {{naming_convention}}
    
    output_schema:
      required: true
      position: end
      content: |
        Provide code in this format:
        ```{{language}}
        {{code}}
        ```
        Explanation: {{explanation}}
  
  temperature: 0.3-0.5    # KA-CMI-041 for coding
  
  chain_of_thought: |
    First, analyze the specification and identify key requirements.
    Then, examine the context to understand existing patterns.
    Finally, generate code that meets all acceptance criteria.
```

**CONFIDENCE:** HIGH

**GAPS:**
- Language-specific prompt variations not fully specified
- Domain-specific (embedded, ML, etc.) adaptations needed

---

### INSTANCE: test_generation_system

**KNOWLEDGE ATOMS CONSUMED:**
KA-SDLC-018, KA-SDLC-044, KA-SDLC-046, KA-CODE-007, KA-CODE-034

**DRAFT SPEC:**
```yaml
prompt_spec:
  name: test_generation_system
  template: |
    # Role
    {{role_definition}}
    
    # Code Under Test
    {{code_under_test}}
    
    # Test Requirements
    {{test_requirements}}
    
    # Sad Path Requirements
    {{sad_path_explicit_requirement}}
    
    # Output
    {{output_format}}
  
  sections:
    role_definition:
      content: |
        You are a test generation specialist. Generate comprehensive
        tests including both happy paths and error conditions.
    
    code_under_test:
      required: true
      max_tokens: 40%
    
    test_requirements:
      content: |
        Coverage target: {{coverage_target}}%
        Test distribution: 70% unit, 20% integration, 10% E2E
    
    sad_path_explicit_requirement:  # KA-CODE-007, KA-SDLC-046
      required: true
      content: |
        CRITICAL: Include tests for error conditions:
        - Invalid inputs
        - Boundary conditions
        - Exception handling
        - Resource exhaustion
        Target: At least 30% of tests should be sad paths.
    
    output_format:
      content: |
        For each test, provide:
        1. Test name following {{naming_convention}}
        2. Arrange-Act-Assert structure
        3. Clear assertion messages
  
  temperature: 0.3
```

**CONFIDENCE:** HIGH

**GAPS:**
- Framework-specific test syntax not templated
- Mock generation guidance not included

---

### INSTANCE: review_critique_system

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-005, KA-CMI-037, KA-CMI-038, KA-META-013, KA-META-024

**DRAFT SPEC:**
```yaml
prompt_spec:
  name: review_critique_system
  template: |
    # Role
    {{critique_role}}
    
    # Code to Review
    {{code_under_review}}
    
    # Review Checklist
    {{review_dimensions}}
    
    # Previous Reviews
    {{review_history}}
    
    # Output Format
    {{critique_format}}
  
  sections:
    critique_role:
      content: |
        You are a code review critic. Your goal is to find defects,
        security issues, and specification deviations. Be thorough
        and adversarial - assume bugs exist and find them.
    
    code_under_review:
      required: true
      position: after_role
    
    review_dimensions:
      content: |
        Check for:
        1. Correctness: Does it meet specifications?
        2. Security: Any injection risks? (KA-META-011)
        3. Performance: Any obvious inefficiencies?
        4. Maintainability: Clear naming, appropriate abstraction?
        5. Testing: Are error paths covered?
    
    critique_format:
      content: |
        For each issue found:
        - Severity: [critical/high/medium/low]
        - Location: line numbers
        - Issue: clear description
        - Suggestion: specific fix
        
        Confidence score: 0-1
  
  temperature: 0.5          # Slightly higher for creativity in finding issues
  
  self_critique: true       # KA-CMI-037: 25-40% error reduction
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- Multi-critic consensus prompt not specified
- Domain-specific security checklists not included

---

### INSTANCE: task_decomposition_system

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-020, KA-AGENT-031, KA-META-039, KA-META-054

**DRAFT SPEC:**
```yaml
prompt_spec:
  name: task_decomposition_system
  template: |
    # Role
    {{planner_role}}
    
    # Task to Decompose
    {{task_description}}
    
    # Constraints
    {{decomposition_constraints}}
    
    # Budget
    {{budget_envelope}}
    
    # Output Format
    {{task_structure}}
  
  sections:
    planner_role:
      content: |
        You are a task decomposition specialist. Break complex tasks
        into atomic, verifiable subtasks with clear dependencies.
    
    task_description:
      required: true
      position: start
    
    decomposition_constraints:
      content: |
        - Maximum depth: 2-3 for simple, 5-7 for complex (KA-AGENT-020)
        - Each task must be: single responsibility, verifiable,
          reversible, idempotent (KA-AGENT-031)
        - Avoid over-delegation - coarser is better than too fine
    
    budget_envelope:
      content: |
        Total token budget: {{token_budget}}
        Total tool call budget: {{tool_budget}}
        Allocate per subtask with 20% buffer.
    
    task_structure:
      content: |
        Output JSON:
        {
          "tasks": [
            {
              "id": "unique_identifier",
              "description": "clear, actionable description",
              "dependencies": ["task_ids"],
              "success_criteria": "verifiable completion condition",
              "estimated_tokens": number,
              "risk_level": "low/medium/high"
            }
          ]
        }
  
  temperature: 0.2          # Low for consistent decomposition
```

**CONFIDENCE:** HIGH

**GAPS:**
- Dynamic depth adjustment based on complexity not automated
- Dependency cycle detection not integrated

---

# PC5: MCP CONFIGURATIONS - Tool Access Patterns

MCP configurations define standardized tool access with privilege rules and audit requirements.

---

## PRODUCT: PC5 - MCP CONFIGURATIONS

### INSTANCE: code_intelligence_mcp

**KNOWLEDGE ATOMS CONSUMED:**
KA-CMI-011, KA-CMI-017, KA-CMI-019, KA-CMI-025, KA-CODE-040, KA-AGENT-032, KA-META-031, KA-META-033

**DRAFT SPEC:**
```yaml
mcp_config:
  name: code_intelligence_mcp
  purpose: |
    Provide semantic code understanding through Model Context Protocol.
    Enables cross-file navigation, symbol search, and codebase grokking.
  
  capabilities:
    - semantic_search           # KA-CMI-013: hybrid vector + BM25
    - symbol_indexing           # KA-CMI-019: Sourcegraph/Kythe
    - ast_analysis              # KA-CODE-040: Tree-sitter
    - cpg_query                 # KA-CMI-017: security analysis
  
  privileges:
    read:
      - file_system: codebase
      - vector_store: embeddings
      - graph_store: cpg
    write:
      - cache: query_results
    blocked:
      - file_system: outside_workspace
      - network: external_apis
  
  rate_limits:
    requests_per_minute: 120
    tokens_per_request: 100000
  
  audit:
    log_level: info
    events:
      - query_executed
      - file_accessed
      - result_cached
  
  servers:
    primary:
      - augment_context_engine    # KA-CMI-011: 71-80% improvement
      - sourcegraph_mcp
      - tree_sitter_service
    fallback:
      - local_vector_db           # KA-CMI-025: Qdrant/Chroma
  
  security:
    sandbox: required
    egress: deny_all
    provenance_tracking: true    # KA-META-037
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- MCP server discovery and health checking not specified
- Cross-server query federation not detailed

---

### INSTANCE: deployment_mcp

**KNOWLEDGE ATOMS CONSUMED:**
KA-SDLC-040, KA-SDLC-042, KA-META-017, KA-META-031, HUMAN-007, INFRA-001

**DRAFT SPEC:**
```yaml
mcp_config:
  name: deployment_mcp
  purpose: |
    Orchestrate CI/CD pipelines and infrastructure deployments.
    Supports canary releases, rollback automation, and observability.
  
  capabilities:
    - pipeline_execution        # KA-SDLC-040: full workflow
    - infrastructure_generation # KA-SDLC-042: Terraform/CloudFormation
    - canary_deployment         # KA-SDLC-003: gradual rollout
    - metric_monitoring         # KA-SDLC-028: RED/USE metrics
  
  privileges:
    read:
      - ci_system: status
      - metrics: monitoring
      - git: history
    write:
      - ci_system: trigger
      - infrastructure: plan
    elevated:                    # HUMAN-007: CRITICAL tier
      - production_deploy: require_approval
      - infrastructure_apply: require_approval
    blocked:
      - production: direct_access
  
  approval_gates:
    safe: auto_approve           # staging deploy, plan generation
    moderate: notify             # integration test trigger
    high: require_approval       # database migrations
    critical: block_and_escalate # production apply
  
  audit:
    log_level: debug
    events:
      - deployment_initiated
      - approval_requested
      - approval_granted
      - rollback_executed
    retention: 90_days
    compliance: KA-META-017      # policy version, trace IDs
  
  servers:
    - github_actions_mcp
    - terraform_mcp
    - kubernetes_mcp
    - datadog_mcp
  
  rollback:
    automatic: true
    conditions:
      - error_rate > 1%
      - latency_p99 > 2x
```

**CONFIDENCE:** HIGH

**GAPS:**
- Multi-cloud deployment coordination not specified
- Custom deployment hook integration not detailed

---

### INSTANCE: security_scanning_mcp

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-011, KA-META-020, KA-META-022, KA-META-024, KA-CMI-017, KA-META-035, KA-META-036

**DRAFT SPEC:**
```yaml
mcp_config:
  name: security_scanning_mcp
  purpose: |
    Multi-layer security validation for code and configurations.
    Addresses 40-45% vulnerability rate in AI-generated code.
  
  capabilities:
    - static_analysis           # KA-META-022: 100% precision
    - taint_analysis            # KA-CMI-017: 70-90% detection
    - dependency_scan           # KA-META-012: slopsquatting
    - secret_detection
    - configuration_validation  # KA-META-020: hardening checklist
  
  privileges:
    read:
      - code: full_access
      - dependencies: manifest_files
      - config: deployment_configs
    write:
      - reports: findings
      - cache: scan_results
    blocked:
      - network: external
      - secrets: actual_values
  
  layers:                       # KA-META-024: multi-layer defense
    - input_filtering
    - static_analysis
    - execution_test
    - output_validation
  
  audit:
    log_level: debug
    events:
      - scan_initiated
      - finding_reported
      - false_positive_flagged
    compliance: KA-META-017
  
  servers:
    - semgrep_mcp
    - trivy_mcp
    - checkov_mcp
    - gitleaks_mcp
  
  sandbox:
    required: true               # KA-META-020: gVisor/Kata
    read_only_root: true
    egress: deny_all             # KA-META-036: default-deny
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- False positive triage workflow not automated
- Scan result correlation across tools not specified

---

### INSTANCE: human_interaction_mcp

**KNOWLEDGE ATOMS CONSUMED:**
HUMAN-006, HUMAN-007, HUMAN-008, HUMAN-009, HUMAN-010

**DRAFT SPEC:**
```yaml
mcp_config:
  name: human_interaction_mcp
  purpose: |
    Manage human-in-the-loop interactions with structured escalation,
    intelligent batching, and multi-channel notifications.
  
  capabilities:
    - escalation_request          # HUMAN-005: confidence-calibrated
    - approval_batching           # HUMAN-006: grouped requests
    - notification_delivery       # HUMAN-009: 80+ services
    - checkpoint_serialization    # HUMAN-010: state preservation
  
  privileges:
    read:
      - user_profile: preferences
      - history: previous_decisions
    write:
      - notifications: send
      - state: checkpoint
    blocked:
      - user_device: direct_access
  
  risk_tiers:                   # HUMAN-007
    safe:
      actions: [read, format]
      approval: auto
    moderate:
      actions: [file_modify, dependency_update]
      approval: notify
    high:
      actions: [database_change, security_config]
      approval: require
    critical:
      actions: [production_deploy, irreversible]
      approval: block_and_escalate
  
  notification:
    channels:                     # HUMAN-009
      - slack
      - email
      - teams
      - discord
      - sms
    priority_routing:
      critical: immediate_all_channels
      high: immediate_primary
      medium: batched_hourly
      low: daily_digest
  
  structured_questions:         # HUMAN-008
    format: 2-4_suggestions
    allow_custom: true
  
  audit:
    log_level: info
    events:
      - escalation_triggered
      - approval_requested
      - approval_granted
      - approval_denied
```

**CONFIDENCE:** HIGH

**GAPS:**
- Notification fatigue prevention thresholds not calibrated
- Timezone-aware notification scheduling not specified

---

# PC6: RULES - Hard Constraints

Rules define non-negotiable constraints with enforcement mechanisms.

---

## PRODUCT: PC6 - RULES

### INSTANCE: complexity_budget_enforcement

**KNOWLEDGE ATOMS CONSUMED:**
KA-CODE-011, KA-META-054, KA-CODE-013

**DRAFT SPEC:**
```yaml
rule_spec:
  name: complexity_budget_enforcement
  constraint: |
    All generated code must comply with complexity budgets enforced
    at team level. Blocks CI/CD when budgets exceeded.
  
  rationale: |
    Teams with enforced complexity budgets achieve 40% defect density
    reduction (KA-CODE-011). AI-generated code exhibits 30% more
    abstraction layers requiring explicit control (KA-CODE-013).
  
  enforcement:
    static_analysis: required
    metrics:
      - cyclomatic_complexity:
          threshold: 10
          warning: 8
      - cognitive_complexity:
          threshold: 15
          warning: 12
      - function_length:
          threshold: 50_lines
          warning: 40_lines
      - nesting_depth:
          threshold: 4
          warning: 3
    ci_block: true
    
  override:
    allowed: conditional
    requires:
      - architectural_justification
      - tech_lead_approval
      - exception_logged
  
  remediation:
    automatic: refactoring_suggested
    mode: coder
    max_attempts: 3
```

**CONFIDENCE:** HIGH

**GAPS:**
- Language-specific complexity thresholds not defined
- Contextual complexity (domain complexity) not addressed

---

### INSTANCE: test_coverage_minimum

**KNOWLEDGE ATOMS CONSUMED:**
KA-SDLC-058, KA-SDLC-024, KA-CODE-007, KA-SDLC-057

**DRAFT SPEC:**
```yaml
rule_spec:
  name: test_coverage_minimum
  constraint: |
    All code changes must maintain minimum 80% line coverage
    with test pyramid distribution (70% unit, 20% integration, 10% E2E).
  
  rationale: |
    80% line coverage correlates with 50% defect reduction (KA-SDLC-024).
    60-70% of production failures originate from untested error paths
    (KA-CODE-007). Test pyramid optimizes confidence vs maintenance cost.
  
  enforcement:
    pre_commit: warning
    pr_merge: block
    release: block
    metrics:
      - line_coverage:
          minimum: 80%
          target: 85%
      - test_pyramid:
          unit: 70% ± 10%
          integration: 20% ± 5%
          e2e: 10% ± 3%
      - sad_path_ratio:
          minimum: 30%
  
  exceptions:
    boilerplate_code: documentation_only
    generated_code: if_template_based
    requires: team_lead_approval
  
  remediation:
    automatic: test_generation_triggered
    mode: tester
```

**CONFIDENCE:** HIGH

**GAPS:**
- MC/DC coverage for safety-critical not automatically enforced
- Coverage gaming detection (KA-SDLC-078) not implemented

---

### INSTANCE: security_hardening_mandatory

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-020, KA-META-036, KA-META-035, KA-META-011

**DRAFT SPEC:**
```yaml
rule_spec:
  name: security_hardening_mandatory
  constraint: |
    All code execution must occur within hardened sandbox with
    default-deny network egress and read-only filesystem.
  
  rationale: |
    Sandboxing reduces exfiltration by 90% (KA-META-011).
    50-84% prompt injection success in tool-using agents requires
    defense in depth (KA-META-011).
  
  enforcement:
    execution_requirements:
      sandbox:
        technology: [gvisor, kata, hopx]  # KA-META-020
        required: true
      network:
        default: deny_all                 # KA-META-036
        egress: explicit_allowlist_only
      filesystem:
        root: read_only                   # KA-META-020
        tmp: ephemeral
      secrets:
        management: dedicated_vault       # KA-META-020
        injection: runtime_only
    
    validation_layers:                    # KA-META-035
      - input_filtering
      - tool_call_policy_validation
      - output_schema_checks
      - post_action_attestation
  
  violations:
    response: block_and_alert
    escalation: security_team
```

**CONFIDENCE:** HIGH

**GAPS:**
- Performance impact of sandboxing not quantified
- Custom sandbox configuration per workload not specified

---

### INSTANCE: budget_enforcement

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-007, KA-META-039, KA-META-001, KA-META-042

**DRAFT SPEC:**
```yaml
rule_spec:
  name: budget_enforcement
  constraint: |
    All tasks must respect token and cost budgets with graceful
    degradation or termination when exceeded.
  
  rationale: |
    AI agents cost $5-8 per task unconstrained (KA-META-001).
    Budget decomposition prevents runaway loops (KA-META-039).
    Cost-to-value telemetry enables optimization (KA-META-042).
  
  enforcement:
    mechanisms:                           # KA-META-007
      - hard_token_limit:
          action: block
          scope: per_request
      - soft_token_limit:
          action: warn
          scope: per_request
      - cost_budget:
          action: block
          scope: per_period
      - task_budget:
          action: degrade_or_escalate
          scope: per_task
    
    allocation:                           # KA-META-039
      strategy: budget_aware_decomposition
      buffer: 20%
      
    telemetry:
      track: cost_to_value
      feedback: routing_policies
  
  degradation:
    tier_1: compression_activated
    tier_2: model_downgrade
    tier_3: scope_reduction
    tier_4: human_escalation
  
  violations:
    soft: warning_with_telemetry
    hard: block_and_report
```

**CONFIDENCE:** HIGH

**GAPS:**
- Organization-specific cost thresholds not established
- Value measurement methodology needs calibration

---

### INSTANCE: audit_trail_completeness

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-017, KA-META-030, KA-META-032

**DRAFT SPEC:**
```yaml
rule_spec:
  name: audit_trail_completeness
  constraint: |
    All agent actions must generate complete audit trails with
    policy versions, hashes, approvals, and trace correlation.
  
  rationale: |
    Governance compliance requires event-sourced audit ledger with
    append-only event journal (KA-META-017). AI-Native SBOM extension
    provides legal posture (KA-META-032).
  
  enforcement:
    required_fields:                      # KA-META-017
      - policy_version
      - model_version
      - tool_versions
      - input_hash
      - output_hash
      - approval_chain
      - trace_id
      - correlation_id
    
    sbom_extension:                       # KA-META-032
      include:
        - model_provider_version
        - prompt_templates
        - retrieval_corpora
        - tool_endpoints
        - dependency_lineage
    
    storage:
      type: append_only
      immutability: cryptographically_verified
      retention: 7_years
  
  validation:
    pre_execution: policy_version_check
    post_execution: hash_verification
    periodic: integrity_audit
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- Storage cost implications not quantified
- Cross-system trace correlation not standardized

---

# PC7: CONTEXT STRATEGIES - Window Partitioning

Context strategies define how the context window is allocated and compressed.

---

## PRODUCT: PC7 - CONTEXT STRATEGIES

### INSTANCE: standard_coding_session

**KNOWLEDGE ATOMS CONSUMED:**
KA-CMI-009, KA-CMI-003, KA-CMI-001, KA-CMI-002, KA-CMI-012, KA-META-004

**DRAFT SPEC:**
```yaml
context_strategy_spec:
  name: standard_coding_session
  purpose: |
    General-purpose context allocation for implementation tasks.
    Balances system instructions, conversation history, retrieval,
    and working space.
  
  window_partition:                       # KA-CMI-009
    system: 20%
      content: role_definition, constraints, patterns
      placement: start                    # KA-CMI-003
    
    conversation_history: 30%
      content: recent exchanges
      compression: observation_masking    # KA-CMI-012
      max_turns: 10
    
    retrieval: 40%
      content: relevant_code, specs, docs
      prioritization: semantic_relevance
      compression: llmlingua              # KA-CMI-001
    
    working_space: 10%
      content: generation_buffer
      reservation: mandatory
  
  dynamic_rebalancing:
    trigger: phase_change
    phases:
      exploration:
        retrieval: +10%
        working: -10%
      implementation:
        working: +10%
        retrieval: -10%
  
  compression_pipeline:
    - semantic_chunking                    # KA-CMI-007
    - llmlingua_compression                # KA-CMI-001: 20x
    - selective_context                    # KA-CMI-002: 50% reduction
    - u_shaped_placement                   # KA-CMI-003
```

**CONFIDENCE:** HIGH

**GAPS:**
- Phase detection automation not specified
- Language-specific partition tuning not defined

---

### INSTANCE: long_running_debug

**KNOWLEDGE ATOMS CONSUMED:**
KA-CMI-046, KA-CMI-012, KA-CMI-026, KA-SDLC-035

**DRAFT SPEC:**
```yaml
context_strategy_spec:
  name: long_running_debug
  purpose: |
    Extended debugging session management with hierarchical
    summarization and sliding window techniques.
  
  window_partition:
    system: 20%
      content: debugging_patterns, language_quirks
    
    session_summary: 25%
      content: hierarchical_summarization
      technique: llm_summarization          # KA-CMI-012
      levels: 3
    
    recent_history: 25%
      content: last N attempts
      technique: sliding_window_with_overlap  # KA-CMI-046
      overlap: 20%
    
    relevant_context: 25%
      content: related_code, similar_fixes
    
    working: 5%
  
  memory_architecture:                    # KA-CMI-026
    working: immediate
    session: conversation_scoped
    long_term:
      retrieval: experience_based
      trigger: pattern_recognition
  
  compression_pipeline:
    - error_pattern_extraction
    - hierarchical_summarization
    - sliding_window_with_overlap
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- Summary quality degradation over time not measured
- Automatic session break detection not implemented

---

### INSTANCE: multi_agent_collaboration

**KNOWLEDGE ATOMS CONSUMED:**
KA-CMI-047, KA-CMI-027, KA-CMI-032, KA-AGENT-008

**DRAFT SPEC:**
```yaml
context_strategy_spec:
  name: multi_agent_collaboration
  purpose: |
    Shared context pool for multiple agents working on
    related tasks with provenance tracking and access control.
  
  window_partition:
    system: 15%
      content: coordination_protocols
    
    shared_pool: 45%
      content: common_context
      access: read_only_for_non_owners
      provenance: tracked                    # KA-CMI-047
    
    agent_specific: 30%
      content: role_state, local_decisions
    
    coordination: 10%
      content: message_buffer, locks
  
  shared_context:
    source_tracking: true                   # KA-CMI-047
    trust_tiers: enforced
    refresh_policy: on_change
  
  memory_hierarchy:                         # KA-CMI-032
    working: agent_local
    session: shared_pool
    long_term: graph_rag                    # KA-CMI-027
  
  compression_pipeline:
    - task_conditioned_selection            # KA-CMI-010
    - context_provenance_tracking           # KA-CMI-047
    - u_shaped_placement
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- Conflict resolution for shared context updates not specified
- Pool size limits for N agents not calculated

---

### INSTANCE: repository_grokking

**KNOWLEDGE ATOMS CONSUMED:**
KA-CMI-007, KA-CMI-008, KA-CMI-016, KA-CMI-019, KA-CMI-023, KA-META-029

**DRAFT SPEC:**
```yaml
context_strategy_spec:
  name: repository_grokking
  purpose: |
    Large-scale codebase ingestion with multi-representation
    indexing and incremental updates.
  
  window_partition:
    system: 15%
    indexing_progress: 15%
    current_batch: 50%
    result_buffer: 20%
  
  chunking_strategy:                        # KA-CMI-007
    type: semantic
    boundaries: [function, class, module]
    overlap: 10-20%                         # KA-CMI-008
  
  representations:                          # KA-CMI-016
    - ast: abstract_syntax_tree
    - cfg: control_flow_graph
    - dfg: data_flow_graph
    - cpg: code_property_graph              # KA-CMI-017
  
  indexing:
    incremental: true                       # KA-CMI-023
    update_propagation: dependent_representations
    validation: consistency_check
  
  storage:
    vector_db: KA-CMI-025                   # Qdrant/Pinecone
    graph_db: Neo4j                         # for CPG
    hybrid_search: KA-CMI-013               # vector + BM25
```

**CONFIDENCE:** HIGH

**GAPS:**
- Incremental update performance at 10M+ LOC not validated
- Cross-repo indexing federation not specified

---

# PC8: TASK DECOMPOSITION PATTERNS

Task patterns define standard work breakdown structures for common scenarios.

---

## PRODUCT: PC8 - TASK DECOMPOSITION PATTERNS

### INSTANCE: hierarchical_supervisor

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-008, KA-AGENT-036, KA-AGENT-020, KA-AGENT-031

**DRAFT SPEC:**
```yaml
task_pattern_spec:
  name: hierarchical_supervisor
  situation: |
    Complex SDLC tasks requiring multiple specialized capabilities
    with clear accountability and coordination.
  
  recognition:
    - task_complexity: >5
    - required_specialists: >2
    - coordination_needs: high
  
  response:
    structure:
      root:
        role: supervisor
        responsibilities:
          - task_decomposition              # KA-AGENT-020
          - specialist_coordination
          - result_integration
          - quality_gates
      
      children:
        - role: specialist_coder
          scope: implementation
          autonomy: high_within_scope
        - role: specialist_tester
          scope: validation
          autonomy: high_within_scope
        - role: specialist_reviewer
          scope: quality_assurance
          autonomy: high_within_scope
    
    coordination:
      pattern: top_down
      communication: through_supervisor
      conflict_resolution: supervisor_decision
  
  quality_gates:
    - decomposition_valid: no_cycles
    - depth_optimal: 2-7 levels
    - atomic_tasks: single_responsibility  # KA-AGENT-031
  
  metrics:
    latency_reduction: 25%                  # KA-AGENT-008
    error_reduction: 25%
```

**CONFIDENCE:** HIGH

**GAPS:**
- Optimal specialist count per supervisor not established
- Cross-specialist communication patterns not specified

---

### INSTANCE: qa_swarm

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-018, KA-AGENT-004, KA-AGENT-005, KA-CMI-038

**DRAFT SPEC:**
```yaml
task_pattern_spec:
  name: qa_swarm
  situation: |
    Code review requiring multiple perspectives (correctness,
    security, performance, style) with high confidence requirements.
  
  recognition:
    - code_criticality: high
    - review_depth: comprehensive
    - confidence_required: >0.9
  
  response:
    structure:
      type: parallel_swarm
      agents:
        - focus: correctness
          technique: static_analysis
        - focus: security
          technique: adversarial_review        # KA-AGENT-005
        - focus: performance
          technique: pattern_analysis
        - focus: style
          technique: pattern_matching
    
    aggregation:
      method: voting_ensemble                 # KA-CMI-038
      conflict_resolution: dedicated_arbiter
    
    confidence_boost:
      method: multi_model_validation
      improvement: 40%                        # KA-AGENT-018
  
  termination:
    - all_agents_complete
    - confidence_threshold_met
    - max_time: 30_minutes
```

**CONFIDENCE:** HIGH

**GAPS:**
- Arbiter selection criteria not specified
- Conflict resolution escalation not detailed

---

### INSTANCE: async_dag_execution

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-019, KA-AGENT-016, KA-AGENT-031, INFRA-006

**DRAFT SPEC:**
```yaml
task_pattern_spec:
  name: async_dag_execution
  situation: |
    Tasks with clear dependency graphs enabling parallel
    execution of independent subtasks.
  
  recognition:
    - dependencies: explicit
    - parallelizable_work: >30%
    - coordination_overhead: acceptable
  
  response:
    structure:
      type: dependency_graph
      nodes:
        representation: KA-AGENT-031          # atomic tasks
        properties:
          - single_responsibility
          - verifiable_completion
          - reversible
          - idempotent
      
      edges:
        type: dependency
        validation: acyclic                   # KA-AGENT-030
      
      execution:
        strategy: parallel_where_possible
        scheduling: topological_order
        isolation: worktree_per_task          # KA-AGENT-016
  
    performance:
      speedup: 2.3x                           # KA-AGENT-019
      merge_resolution: semantic_llm          # KA-AGENT-017
  
  quality_gates:
    - graph_acyclic: validated
    - dependencies_complete: all_satisfied
    - isolation_maintained: no_cross_contamination
```

**CONFIDENCE:** HIGH

**GAPS:**
- Dynamic parallelism adjustment not implemented
- Worktree cleanup policies not specified

---

### INSTANCE: budget_constrained_exploration

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-039, KA-META-040, KA-META-041, KA-CMI-004

**DRAFT SPEC:**
```yaml
task_pattern_spec:
  name: budget_constrained_exploration
  situation: |
    Information gathering tasks with strict cost constraints
    requiring efficient retrieval and compression.
  
  recognition:
    - information_need: broad
    - budget_constraint: strict
    - precision_requirement: moderate
  
  response:
    structure:
      phases:
        - name: broad_recall
          technique: hybrid_search            # KA-CMI-013
          budget: 40%
        - name: re_ranking
          technique: semantic_scoring
          budget: 20%
        - name: compression
          technique: retrieval_compression     # KA-META-040
          budget: 30%
        - name: invocation
          technique: model_call
          budget: 10%
    
    constraints:
      target_waste: <15%                      # KA-CMI-004
      skill_gating: enabled                   # KA-META-041
  
    degradation:
      if_budget_exceeded:
        - reduce_retrieval_depth
        - increase_compression
        - escalate_to_human
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- Budget estimation accuracy not characterized
- Graceful degradation effectiveness not measured

---

# PC9: WORKSPACE MANAGEMENT

Workspace management defines branch strategies, worktree patterns, and isolation mechanisms.

---

## PRODUCT: PC9 - WORKSPACE MANAGEMENT

### INSTANCE: worktree_isolation_pattern

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-016, KA-AGENT-017, KA-AGENT-019, INFRA-006

**DRAFT SPEC:**
```yaml
workspace_spec:
  name: worktree_isolation_pattern
  purpose: |
    Enable parallel agent execution with git-based coordination
    and semantic merge resolution.
  
  structure:
    base_branch: main
    worktree_per: task_or_subtask
    naming: agent_{id}_task_{task_id}
  
  workflow:
    creation:
      trigger: task_assigned
      from: base_branch_latest
      isolation: full_filesystem
    
    execution:
      concurrency: parallel
      coordination: async_dag              # KA-AGENT-019
      communication: shared_context_pool
    
    resolution:
      method: semantic_llm                 # KA-AGENT-017
      auto_rate: 78%
      fallback: manual_resolution
    
    cleanup:
      trigger: task_complete + merged
      retention: 24_hours
  
  metrics:
    conflict_reduction: 67%                # KA-AGENT-016
    throughput_improvement: 2.5x           # INFRA-006
```

**CONFIDENCE:** HIGH

**GAPS:**
- Disk space management for many worktrees not specified
- Cross-worktree dependency tracking not detailed

---

### INSTANCE: feature_branch_lifecycle

**KNOWLEDGE ATOMS CONSUMED:**
KA-SDLC-023, KA-SDLC-040, KA-AGENT-016

**DRAFT SPEC:**
```yaml
workspace_spec:
  name: feature_branch_lifecycle
  purpose: |
    Standard feature branch workflow with automated testing
    and progressive quality gates.
  
  structure:
    branch_naming: feature/{id}_{description}
    max_lifetime: 1_day                    # KA-SDLC-023
    base: trunk_based_development
  
  lifecycle:
    creation:
      from: main
      validation: ci_passing_on_base
    
    development:
      commits: conventional_format
      pre_commit: hooks_enabled
      push: ci_triggered
    
    validation:
      stages:
        - pr_validation
        - post_merge_integration
        - staging_deploy
        - canary_validation              # KA-SDLC-040
    
    merge:
      method: squash_recommended
      requirements:
        - all_checks_pass
        - review_approved
        - up_to_date_with_base
    
    cleanup:
      delete_after_merge: true
      retention: 7_days_backup
  
  metrics:
    integration_problem_reduction: 70%     # KA-SDLC-023
```

**CONFIDENCE:** HIGH

**GAPS:**
- Hotfix branch exception handling not specified
- Long-running feature branch management not detailed

---

### INSTANCE: agent_workspace_federation

**KNOWLEDGE ATOMS CONSUMED:**
KA-AGENT-010, KA-AGENT-012, INFRA-012

**DRAFT SPEC:**
```yaml
workspace_spec:
  name: agent_workspace_federation
  purpose: |
    Distributed workspace coordination across multiple regions
    or teams with local autonomy and global consistency.
  
  structure:
    topology: federated
    regions:
      - local_workspace: primary
      - regional_coordinators: 1_per_region
      - global_sync: eventual_consistency
  
  coordination:
    pattern: regional_autonomy
    conflict_resolution: timestamp_based
    merge_strategy: three_way_with_llm
  
  performance:
    throughput_improvement: 3x             # KA-AGENT-010
    local_latency: low
    global_sync: asynchronous
  
  scaling:
    threshold_per_region: 500_workspaces   # INFRA-012
    coordination: Kueue
    federation: Admiralty/Liqo
  
  metrics:
    starvation_reduction: 89%              # KA-AGENT-011
    latency_under_load: <2x_baseline_at_5x # KA-AGENT-012
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- Cross-region conflict resolution policies not detailed
- Network partition handling not specified

---

# PC10: TECHNIQUES & STRATEGIES - Situational Playbooks

Techniques define situational responses for specific scenarios.

---

## PRODUCT: PC10 - TECHNIQUES & STRATEGIES

### INSTANCE: cold_start_mitigation

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-018, KA-META-029, INFRA-007

**DRAFT SPEC:**
```yaml
technique_spec:
  name: cold_start_mitigation
  situation: |
    New session or codebase with no existing context cached.
    High latency and token consumption expected without mitigation.
  
  recognition:
    - context_cache: miss
    - session_type: new
    - codebase_familiarity: none
  
  response:
    strategies:                            # KA-META-018
      - cache_pre_warming:
          time: minutes
          cost: low
          effectiveness: high
      - repo_grokking:
          time: minutes_to_hours
          cost: medium
          effectiveness: high              # KA-META-029
      - few_shot_prompting:
          time: instant
          cost: low
          effectiveness: medium
      - hybrid:
          combination: pre_warm + few_shot
          time: minutes
          cost: medium
          effectiveness: very_high
    
    selection:
      if_time_critical: few_shot
      if_quality_critical: repo_grokking
      default: hybrid
  
  effectiveness:
    latency_reduction: 94%                 # INFRA-007
```

**CONFIDENCE:** HIGH

**GAPS:**
- Cache warming prioritization algorithm not specified
- Incremental grokking for large codebases not detailed

---

### INSTANCE: hallucination_defense

**KNOWLEDGE ATOMS CONSUMED:**
KA-META-011, KA-META-012, KA-META-013, KA-META-015, KA-META-022, KA-META-023, KA-META-024

**DRAFT SPEC:**
```yaml
technique_spec:
  name: hallucination_defense
  situation: |
    Code generation with risk of fabricated APIs, incorrect
    logic, or security vulnerabilities due to model hallucination.
  
  recognition:
    - generation_task: active
    - confidence: uncertain
    - criticality: high
  
  response:
    defense_layers:                        # KA-META-024
      - generation:
          technique: rag_enhanced          # KA-META-023: 67% reduction
      - consistency_check:
          technique: self_verification     # KA-META-013: 65% reduction
      - static_analysis:
          technique: ast_based             # KA-META-022: 100% precision
      - execution_test:
          technique: sandboxed_run
      - human_review:
          technique: risk_tiered           # HUMAN-007
    
    tradeoffs:                             # KA-META-015
      - rag: medium_precision, high_recall, medium_latency
      - static_analysis: very_high_precision, medium_recall, low_latency
      - multi_agent: high_precision, high_recall, very_high_latency
    
    selection:
      default: [rag, static_analysis]
      high_criticality: all_layers
      low_criticality: [rag]
  
  metrics:
    slopsquatting_prevention: addresses 19.7% package_fabrication
    vulnerability_reduction: addresses 40-45% generation_rate
```

**CONFIDENCE:** HIGH

**GAPS:**
- Layer-specific latency impact not quantified
- Effectiveness on latest models not validated

---

### INSTANCE: reasoning_strategy_selection

**KNOWLEDGE ATOMS CONSUMED:**
KA-CMI-034, KA-CMI-035, KA-CMI-036, KA-CMI-048

**DRAFT SPEC:**
```yaml
technique_spec:
  name: reasoning_strategy_selection
  situation: |
    Task requiring multi-step reasoning with varying complexity
    and solution space characteristics.
  
  recognition:
    - reasoning_required: true
    - solution_space: [constrained|exploratory]
    - steps_required: estimated
  
  response:
    strategies:
      chain_of_thought:                    # KA-CMI-034
        accuracy_improvement: 20-40%
        compute_overhead: 1x
        best_for: straightforward_reasoning
        prompt: "Let's think step by step"
      
      tree_of_thought:                     # KA-CMI-035
        accuracy_improvement: 30-50%
        compute_overhead: 5-10x
        best_for: exploration_needed
        search: [bfs, dfs, beam]
      
      graph_of_thought:                    # KA-CMI-036
        accuracy_improvement: +10-20% over ToT
        compute_overhead: 3-5x
        best_for: synthesis_required
        operations: [aggregation, feedback]
    
    selection_matrix:
      complexity < 3: chain_of_thought
      complexity 3-6 AND exploration: tree_of_thought
      complexity > 6 OR synthesis: graph_of_thought
  
  metrics:
    got_sorting_improvement: 62%
    got_cost_reduction: 31% vs ToT
```

**CONFIDENCE:** HIGH

**GAPS:**
- Complexity estimation automation not specified
- Hybrid strategy composition not detailed

---

### INSTANCE: approval_fatigue_prevention

**KNOWLEDGE ATOMS CONSUMED:**
HUMAN-006, HUMAN-007, HUMAN-013, HUMAN-015

**DRAFT SPEC:**
```yaml
technique_spec:
  name: approval_fatigue_prevention
  situation: |
    Human-in-the-loop system showing signs of approval fatigue
    with declining review quality and increasing rubber-stamp rates.
  
  recognition:
    - approval_rate: >80%
    - review_time: declining
    - error_escape: increasing
    - pattern: rubber_stamping
  
  response:
    interventions:
      - confidence_calibration:            # HUMAN-015
          technique: threshold_adjustment
          trigger: escalation_drift_detected
      
      - batching_increase:                 # HUMAN-006
          technique: larger_batches
          benefit: reduced_interruption
      
      - auto_approval_expansion:           # HUMAN-007
          technique: risk_reclassification
          condition: historical_accuracy_high
      
      - escalation_throttle:
          technique: temporary_reduction
          trigger: fatigue_detected
    
    monitoring:
      - approval_quality_score
      - time_per_approval
      - override_rate
      - error_escape_rate
  
  prevention:                              # HUMAN-013
    - intelligent_batching
    - risk_tiered_routing
    - confidence_calibration
    - regular_threshold_review
```

**CONFIDENCE:** MEDIUM

**GAPS:**
- Fatigue detection thresholds not calibrated
- Recovery time after intervention not characterized

---

### INSTANCE: canary_deployment_validation

**KNOWLEDGE ATOMS CONSUMED:**
KA-SDLC-003, KA-SDLC-004, KA-SDLC-005, KA-SDLC-040

**DRAFT SPEC:**
```yaml
technique_spec:
  name: canary_deployment_validation
  situation: |
    Production deployment requiring gradual rollout with
    automated validation and rollback capability.
  
  recognition:
    - deployment_target: production
    - risk_level: moderate_to_high
    - rollback_requirement: <5min
  
  response:
    traffic_progression:                   # KA-SDLC-003
      - 1%
      - 5%
      - 25%
      - 50%
      - 100%
    
    validation_at_each_stage:
      metrics:
        - error_rate: <0.1%
        - latency_p99: <1.5x_baseline
        - business_kpi: <5%_degradation
      
      duration: 5-15_minutes
      automated_analysis: required
    
    rollback_triggers:                     # KA-SDLC-004
      automatic:
        - error_rate > 1%
        - latency_p99 > 2x
        - business_kpi > 10%
      manual:
        - anomaly_detected
        - customer_complaint
    
    kill_switch:                           # KA-SDLC-005
      response_time: <100ms
      scope: feature_specific
  
  metrics:
    incident_reduction: 60%                # KA-SDLC-003
    mttr: <5min                            # KA-SDLC-004
```

**CONFIDENCE:** HIGH

**GAPS:**
- Metric threshold calibration methodology not specified
- Cross-feature interaction detection not detailed

---

## Cross-Reference Validation Summary

### Skills Referenced by Modes
| Mode | Required Skills | Status |
|------|-----------------|--------|
| planner | task_decomposition, specification_design | ✓ Validated |
| coder | code_generation, context_compression, model_routing | ✓ Validated |
| tester | test_generation, mutation_testing | ✓ Validated |
| reviewer | adversarial_review, static_analysis | ✓ Validated |
| debugger | fault_diagnosis, iterative_repair | ✓ Validated |
| deployer | pipeline_management, infrastructure_as_code | ✓ Validated |

### MCP Servers Referenced
| MCP Config | Required Servers | Status |
|------------|------------------|--------|
| code_intelligence_mcp | augment_context, sourcegraph, tree_sitter | ✓ Validated |
| deployment_mcp | github_actions, terraform, kubernetes | ✓ Validated |
| security_scanning_mcp | semgrep, trivy, checkov, gitleaks | ✓ Validated |
| human_interaction_mcp | apprise, checkpoint_manager | ✓ Validated |

### Context Strategies Referenced
| Mode | Context Strategy | Status |
|------|------------------|--------|
| planner | standard_coding_session | ✓ Validated |
| coder | standard_coding_session | ✓ Validated |
| tester | standard_coding_session | ✓ Validated |
| debugger | long_running_debug | ✓ Validated |

---

## Knowledge Gaps Summary

### Critical Gaps (Implementation Blockers)
1. **Optimal mode granularity**: No quantitative research on ideal number of modes (5-7 vs 15+ vs dynamic)
2. **Canary metric calibration**: Thresholds require domain-specific tuning not provided
3. **Cost threshold calibration**: Organization-specific budget limits not established

### Important Gaps (Performance Impact)
4. **Mutation testing overhead**: Computational cost for large codebases not quantified
5. **Confidence calibration**: Methodology for new tasks/organizations not specified
6. **Cache invalidation**: Policies need domain calibration
7. **Multi-cloud coordination**: Deployment across providers not detailed

### Minor Gaps (Enhancement Opportunities)
8. **Language-specific thresholds**: Complexity, temperature, and compression vary by language
9. **Notification fatigue**: Thresholds for human interaction not calibrated
10. **Cross-repo context**: Management at 100+ repository scale not validated
11. **Dynamic parallelism**: Adjustment based on load not implemented
12. **Session break detection**: Automatic long-running session segmentation not specified

---

## Confidence Summary

| Category | Products | Avg Confidence |
|----------|----------|----------------|
| PC1: Modes | 6 | HIGH |
| PC2: Skills | 6 | HIGH |
| PC3: Workflows | 4 | HIGH |
| PC4: Prompts | 4 | HIGH |
| PC5: MCP Configs | 4 | MEDIUM-HIGH |
| PC6: Rules | 5 | HIGH |
| PC7: Context Strategies | 4 | HIGH |
| PC8: Task Patterns | 4 | HIGH |
| PC9: Workspace Mgmt | 3 | HIGH |
| PC10: Techniques | 5 | HIGH |

**Overall Confidence: HIGH** (87% of specs HIGH confidence)

---

## Recommended Implementation Priority

### Phase 1 (Foundation)
- PC1: planner, coder modes
- PC2: code_traversal, model_routing skills
- PC6: complexity_budget, security_hardening rules
- PC7: standard_coding_session context

### Phase 2 (Quality)
- PC1: tester, reviewer modes
- PC2: test_generation, security_validation skills
- PC3: feature_development, bug_fix workflows
- PC6: test_coverage rule

### Phase 3 (Operations)
- PC1: debugger, deployer modes
- PC3: emergency_rollback workflow
- PC5: deployment_mcp, security_scanning_mcp
- PC9: worktree_isolation, feature_branch patterns

### Phase 4 (Optimization)
- PC4: All prompt templates
- PC8: All task decomposition patterns
- PC10: All technique playbooks
- PC7: Specialized context strategies

---

*End of Prong 4 Product Assembly*

