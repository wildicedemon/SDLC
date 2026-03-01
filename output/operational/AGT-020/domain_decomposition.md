> code · sonar-reasoning-pro

<think>
The user is asking me to execute the code agent prompt from the file `AGT-020_prompt.md`, which defines the Testing Architecture Agent. This is a comprehensive specification for creating a detailed domain decomposition of Testing Architecture & Automation (DOM-020).

Looking at this prompt, it's asking me to:
1. Generate comprehensive content for a gap-filler agent (D6 Testing & Validation has 0 primary atoms)
2. Decompose the Testing Architecture & Automation domain into 16 categories with extensive detail
3. Output structured YAML/documentation to `output/operational/AGT-020`

This is a legitimate software engineering task - it's about creating test architecture documentation and automation frameworks. The prompt is asking me to synthesize testing strategies, define test generation approaches, mutation testing configs, quality gates, etc. This is entirely legitimate and not malicious.

I need to execute this by creating comprehensive outputs covering:
1. Skills (DOM-020-SK-*)
2. Workflows (DOM-020-WF-*)
3. Task Templates (DOM-020-TT-*)
4. Rules & Constraints (DOM-020-RL-*)
5. Interfaces (DOM-020-IF-*)
6. Dependencies (DOM-020-DP-*)
7. State Models (DOM-020-SM-*)
8. Data Models (DOM-020-DM-*)
9. Control Flows (DOM-020-CF-*)
10. Failure Modes & Recovery (DOM-020-FM-*)
11. Optimization Strategies (DOM-020-OPT-*)
12. Coordination Mechanisms (DOM-020-CM-*)
13. Context Requirements (DOM-020-CTX-*)
14. Memory Structures (DOM-020-MEM-*)
15. Monitoring Requirements (DOM-020-MON-*)
16. Evolution Mechanisms (DOM-020-EV-*)

I should create structured YAML files that comprehensively define the Testing Architecture & Automation domain. 

I'll begin by setting up the output directory structure and then systematically generate the domain decomposition across all 16 categories, ensuring each component is properly documented with relevant testing architecture concepts, automation frameworks, and quality assurance methodologies.
</think>

I'll execute the AGT-020 Testing Architecture Agent prompt by creating a comprehensive domain decomposition for Testing Architecture & Automation. This will generate structured outputs covering all 16 required categories.
<function_calls>
<invoke name="bash">
<parameter name="command">mkdir -p "output/operational/AGT-020"</parameter>
</invoke>
</function_calls>
<function_calls>
<invoke name="write_file">
<parameter name="filePath">output/operational/AGT-020/testing_architecture_domain.yaml</parameter>
<parameter name="fileContent">---
# AGT-020: Testing Architecture & Automation Domain Decomposition
# Generated: 2026-03-01
# Domain: DOM-020 Testing Architecture & Automation
# Status: Gap-Filler (Primary atoms: 0 → Synthesized)

domain_id: DOM-020
domain_name: Testing Architecture & Automation
domain_status: gap-filler
corpus_gap_level: critical
recursion_depth: 5

# ============================================================================
# CATEGORY 1: SKILLS (DOM-020-SK-*)
# ============================================================================
skills:
  DOM-020-SK-001:
    name: Test Case Generation from Specifications
    description: >
      Automatically generate executable test cases from formal specifications using
      constraint satisfaction and semantic analysis.
    inputs:
      - specification_document
      - requirement_formalization
      - acceptance_criteria
    outputs:
      - test_case_set[]
      - test_mapping_matrix
      - coverage_estimate
    complexity: High
    dependencies:
      - AGT-016 (Specification Agent)
    cross_domain_links:
      - DOM-016-SK-* (Specification formalization)
      - DOM-017-SK-* (Code structure understanding)

  DOM-020-SK-002:
    name: Property-Based Test Generation
    description: >
      Generate property-based tests from declarative properties and invariants,
      enabling systematic exploration of input spaces.
    inputs:
      - property_declarations[]
      - type_schemas
      - invariant_constraints
    outputs:
      - property_test_suite
      - discovered_counterexamples
      - property_coverage_report
    complexity: High
    dependencies:
      - Formal property specification capability
    techniques:
      - QuickCheck-style generators
      - Shrinking strategies
      - Invariant assertion frameworks

  DOM-020-SK-003:
    name: Mutation Operator Application & Scoring
    description: >
      Apply mutation operators to source code, execute test suite against mutants,
      and calculate mutation score metrics.
    inputs:
      - source_code
      - mutation_operators[]
      - test_suite
    outputs:
      - mutant_set[]
      - mutation_score
      - equivalent_mutant_set
      - killed_mutant_analysis
    complexity: High
    dependencies:
      - AGT-017 (Code Generation Agent)
    mutation_operators_supported:
      - statement_deletion
      - boundary_value_mutation
      - operator_replacement
      - constant_replacement
      - loop_modification
      - conditional_boundary_shift

  DOM-020-SK-004:
    name: Code Coverage Measurement & Gap Analysis
    description: >
      Measure multiple coverage dimensions (line, branch, path, condition) and
      identify gaps in test suite coverage.
    inputs:
      - instrumented_code
      - test_execution_traces
      - coverage_threshold_policy
    outputs:
      - line_coverage_report
      - branch_coverage_report
      - path_coverage_report
      - condition_coverage_report
      - uncovered_code_segments[]
      - gap_priority_ranking
    complexity: Medium
    coverage_metrics:
      - line_coverage: percentage of executable lines exercised
      - branch_coverage: percentage of conditional branches taken
      - path_coverage: percentage of execution paths exercised
      - condition_coverage: percentage of boolean sub-expressions evaluated
      - mcdc_coverage: modified condition/decision coverage

  DOM-020-SK-005:
    name: Quality Gate Definition & Enforcement
    description: >
      Define measurable quality gates with thresholds and enforce them as
      non-bypassable gates in CI/CD pipelines.
    inputs:
      - quality_metrics[]
      - threshold_definitions
      - business_priority_matrix
    outputs:
      - quality_gate_definition
      - enforcement_policy
      - override_audit_trail
    complexity: Medium
    gate_types:
      - coverage_gate: minimum coverage percentage
      - mutation_gate: minimum mutation score
      - performance_gate: test execution time budget
      - flakiness_gate: maximum allowed flaky test percentage
      - regression_gate: no increase in defect escape rate

  DOM-020-SK-006:
    name: Test Oracle Design & Implementation
    description: >
      Design and implement test oracles that can reliably determine expected
      outputs for generated tests without human specification.
    inputs:
      - specification
      - reference_implementation
      - property_definitions
    outputs:
      - test_oracle_specification
      - oracle_implementation
      - oracle_confidence_metric
    complexity: High
    oracle_techniques:
      - specification_oracle: executable specification as oracle
      - metamorphic_oracle: metamorphic relations as test oracle
      - differential_oracle: comparison against reference implementation
      - property_oracle: property-based assertion validation
      - statistical_oracle: statistical properties of output distribution

  DOM-020-SK-007:
    name: Fuzz Testing Configuration & Execution
    description: >
      Configure and execute fuzz testing campaigns to discover edge cases,
      protocol violations, and robustness issues.
    inputs:
      - target_function_signature
      - input_grammar_or_format
      - coverage_feedback_mechanism
    outputs:
      - discovered_crash_set
      - reproducible_input_set
      - coverage_progression_data
    complexity: High
    fuzzing_strategies:
      - coverage_guided_fuzzing
      - grammar_based_fuzzing
      - evolutionary_fuzzing
      - symbolic_execution_fuzzing

  DOM-020-SK-008:
    name: Adversarial Test Pattern Generation
    description: >
      Generate adversarial test patterns targeting security-sensitive code paths,
      authentication, authorization, and data validation.
    inputs:
      - security_threat_model
      - vulnerable_code_patterns
      - attack_vector_database
    outputs:
      - adversarial_test_suite
      - threat_coverage_matrix
      - vulnerability_report
    complexity: High
    attack_vector_categories:
      - injection_attacks: SQL, command, XPath injection
      - authentication_bypass: default credentials, race conditions
      - authorization_flaws: privilege escalation, IDOR
      - data_validation: boundary violations, type confusion
      - denial_of_service: resource exhaustion, algorithmic complexity

  DOM-020-SK-009:
    name: Test Prioritization & Selection
    description: >
      Prioritize tests for execution based on code changes, risk factors, and
      execution cost to optimize feedback loop.
    inputs:
      - code_change_set
      - test_coverage_map
      - test_execution_costs
      - test_failure_history
    outputs:
      - prioritized_test_schedule
      - estimated_execution_time
      - confidence_in_coverage
    complexity: Medium
    prioritization_factors:
      - code_change_impact: how much code changed
      - test_failure_history: historical flakiness and failures
      - coverage_criticality: coverage of critical paths
      - execution_cost: test runtime vs. value
      - time_since_last_run: recency of test execution

  DOM-020-SK-010:
    name: Regression Test Suite Optimization
    description: >
      Optimize regression test suites by identifying redundant tests, eliminating
      dead tests, and maximizing coverage efficiency.
    inputs:
      - test_suite
      - test_execution_history
      - code_coverage_data
      - test_dependency_graph
    outputs:
      - optimized_test_suite
      - redundancy_report
      - efficiency_improvement_metrics
    complexity: Medium
    optimization_techniques:
      - test_redundancy_detection: identify duplicate coverage
      - dead_test_elimination: remove never-failing tests
      - test_merging: combine similar tests
      - dependency_ordering: optimal execution order

  DOM-020-SK-011:
    name: Flaky Test Detection & Quarantine
    description: >
      Detect non-deterministic (flaky) tests through statistical analysis and
      quarantine them with investigation priorities.
    inputs:
      - test_execution_history
      - test_failure_patterns
      - environmental_factors[]
    outputs:
      - flaky_test_report
      - quarantine_decision
      - investigation_priority
    complexity: Medium
    flakiness_detection_methods:
      - failure_pattern_analysis: inconsistent pass/fail rates
      - environmental_correlation: correlation with timing or environment
      - retry_analysis: test behavior under retry
      - statistical_significance: failure rate vs. random chance

  DOM-020-SK-012:
    name: Test Data Generation & Management
    description: >
      Generate and manage test data that is representative, isolated, and
      refreshed consistently across test runs.
    inputs:
      - data_schema
      - constraint_specifications
      - dependency_graph
    outputs:
      - test_data_set
      - data_freshness_policy
      - isolation_guarantees
    complexity: Medium
    data_generation_techniques:
      - combinatorial_generation: property-based combinations
      - constraint_solving: CSP-based generation
      - schema_based_generation: from data model schemas
      - synthetic_data_generation: realistic but non-sensitive data

  DOM-020-SK-013:
    name: Integration Test Scaffolding
    description: >
      Create scaffolding, mocks, stubs, and test doubles for integration testing
      across component boundaries.
    inputs:
      - component_interfaces
      - integration_requirements
      - external_dependency_specs
    outputs:
      - integration_test_harness
      - mock_implementation_set
      - stub_service_definitions
    complexity: Medium
    scaffold_types:
      - mock_objects: fake implementations for testing
      - stubs: minimal implementations for dependencies
      - test_doubles: fake external services
      - contract_test_definitions: API contract specifications

  DOM-020-SK-014:
    name: End-to-End Test Orchestration
    description: >
      Orchestrate end-to-end tests spanning full system workflows with
      environment setup, data preparation, and cleanup.
    inputs:
      - user_journey_specification
      - system_environment_config
      - test_data_requirements
    outputs:
      - e2e_test_script
      - orchestration_plan
      - cleanup_guarantees
    complexity: High
    orchestration_concerns:
      - environment_setup: provision test infrastructure
      - data_preparation: seed data, database state
      - workflow_execution: orchestrated user journey
      - state_validation: assertions at each step
      - cleanup: resource deallocation, state reset

  DOM-020-SK-015:
    name: Performance Test Design & Baseline Establishment
    description: >
      Design performance tests with defined baselines, thresholds, and
      regression detection for latency and throughput.
    inputs:
      - performance_requirements
      - load_profiles
      - system_capacity_model
    outputs:
      - performance_test_plan
      - baseline_metrics
      - regression_detection_rules
    complexity: High
    performance_dimensions:
      - latency: response time measurements
      - throughput: requests/operations per unit time
      - scalability: performance under load variation
      - resource_utilization: CPU, memory, I/O efficiency
      - degradation_patterns: performance under stress

# ============================================================================
# CATEGORY 2: WORKFLOWS (DOM-020-WF-*)
# ============================================================================
workflows:
  DOM-020-WF-001:
    name: Automated Test Generation Pipeline
    workflow_id: DOM-020-WF-001
    trigger:
      - event: code_generation_complete
        source: AGT-017
      - event: specification_updated
        source: AGT-016
      - event: manual_trigger
    steps:
      - step_id: 1
        name: Parse Specification
        entry_criteria: Valid specification document available
        action: Extract requirements, acceptance criteria, business rules
        exit_criteria: Normalized specification model created
        tools:
          - specification_parser
          - constraint_extractor
        timeout: 30s
        
      - step_id: 2
        name: Analyze Generated Code
        entry_criteria: Code parsing complete
        action: Build code structure graph, identify functions, parameters, return types
        exit_criteria: Code dependency graph complete
        tools:
          - AST_analyzer
          - dependency_graph_builder
        timeout: 60s
        
      - step_id: 3
        name: Generate Test Cases
        entry_criteria: Specification and code analysis complete
        action: Apply property-based generation, boundary value analysis, equivalence partitioning
        exit_criteria: Comprehensive test case set with traceability to spec
        tools:
          - property_test_generator
          - boundary_analyzer
          - equivalence_partitioner
        parallelizable: true
        timeout: 300s
        
      - step_id: 4
        name: Validate Generated Tests
        entry_criteria: Test cases generated
        action: Type-check tests, validate assertions, check oracle soundness
        exit_criteria: All generated tests validated and ready for execution
        tools:
          - test_validator
          - oracle_verifier
        timeout: 120s
        
      - step_id: 5
        name: Integrate into Test Suite
        entry_criteria: Tests validated
        action: Merge into master test suite, update coverage mapping, register with CI
        exit_criteria: Tests registered in test management system
        tools:
          - test_suite_merger
          - ci_integration_service
        timeout: 60s
        
    completion_criteria:
      - all_test_cases_generated: "test_case_count >= 5"
      - coverage_increase: "new_coverage > baseline_coverage"
      - zero_syntax_errors: "validation_errors == 0"
      - oracle_validation: "oracle_confidence >= 0.95"
      
    rollback_plan:
      - trigger: generation_failure_rate > 0.3
        action: revert_to_previous_test_suite
        rationale: Too many generation failures indicates specification or code analysis issue
      - trigger: validation_failure_rate > 0.5
        action: investigate_oracle_issue
        rationale: High validation failure indicates oracle problem
        
    dependencies:
      - AGT