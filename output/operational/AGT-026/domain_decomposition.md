> code · sonar-reasoning-pro<think>
The user is asking me to read a file that contains a prompt for an agent called "AGT-026: Debugging Agent" and then execute this prompt. However, I need to clarify what this means in the context of my role as Kilo.

Looking at the instructions:
1. I'm Kilo, a software engineer assistant
2. I should refuse to write code or explain code that may be used maliciously
3. I need to examine the code/files to understand what they're supposed to do
4. The user is asking me to "execute" a prompt and output to a specific directory

The file appears to be a system prompt/directive for an AI agent that's part of an SDLC (Software Development Life Cycle) system. It's describing a "Debugging Agent" that should decompose debugging and error recovery domains, define skills, workflows, rules, interfaces, etc.

However, the user is also providing search results about SDLC phases - these seem unrelated to the actual task they're asking me to perform.

The request seems to be:
- Take the AGT-026 prompt from the file
- Execute it (meaning generate the output it describes)
- Output the results to `output/operational/AGT-026`

But wait - I need to think about what "execute the code agent prompt" means. This appears to be asking me to:
1. Take the system prompt in that file
2. Generate the outputs it describes (debugging workflows, skill definitions, etc.)
3. Output them to the specified directory

This is essentially asking me to generate a comprehensive decomposition of debugging and error recovery patterns following the template specified in the prompt.

Let me check if this is malicious or problematic:
- It's asking me to create documentation about debugging, error recovery, workflows, and skills
- This is for a legitimate SDLC system
- There's nothing malicious about this request

I should proceed with executing this prompt by:
1. Creating the output directory structure
2. Generating the requested YAML files and documentation following the template


3. Following the prompt's requirements for comprehensive decomposition

Let me generate the appropriate outputs.
</think>

I'll execute the AGT-026 Debugging Agent prompt by generating the comprehensive decomposition artifacts it specifies.

```bash
mkdir -p output/operational/AGT-026
```

Now generating the core output files:

```yaml
# output/operational/AGT-026/skills.yaml
domain: DOM-026
domain_name: Debugging & Error Recovery
category: Skills
total_skills: 24
skills:
  - skill_id: DOM-026-SK-001
    name: Fault Localization via Stack Trace Analysis
    description: Systematically parse error stack traces to identify the exact code location and function call chain leading to failure.
    inputs: [error_stack_trace, source_code_mapping, thread_context]
    outputs: [fault_location, call_chain, entry_point]
    complexity: Medium
    knowledge_atoms: [KA-031]

  - skill_id: DOM-026-SK-002
    name: Root Cause Hypothesis Generation
    description: Apply chain-of-thought reasoning to generate plausible root cause hypotheses from error symptoms and context.
    inputs: [error_message, fault_location, symptom_description, recent_changes]
    outputs: [hypothesis_list, confidence_scores, reasoning_chain]
    complexity: High
    knowledge_atoms: [KA-031]

  - skill_id: DOM-026-SK-003
    name: Error Classification & Severity Assessment
    description: Classify errors into taxonomic categories and assign severity levels based on impact scope and business criticality.
    inputs: [error_type, affected_components, user_impact, data_affected]
    outputs: [classification, severity_level, impact_scope, escalation_path]
    complexity: Medium
    knowledge_atoms: []

  - skill_id: DOM-026-SK-004
    name: Automated Patch Generation
    description: Synthesize code patches from root cause analysis and repair strategies using templates and pattern matching.
    inputs: [root_cause, error_taxonomy_entry, affected_files, constraint_rules]
    outputs: [patch_code, diff, test_cases, rollback_plan]
    complexity: High
    knowledge_atoms: [KA-038]

  - skill_id: DOM-026-SK-005
    name: Zero-Shot Recovery Chaining
    description: Attempt autonomous recovery strategies in sequence for unknown or unhandled errors without human intervention.
    inputs: [error_state, available_strategies, retry_budget, escalation_threshold]
    outputs: [recovery_attempt_log, success_status, escalation_trigger]
    complexity: High
    knowledge_atoms: []

  - skill_id: DOM-026-SK-006
    name: Bisect-Based Regression Identification
    description: Perform binary search through commit history to identify the specific change introducing a regression bug.
    inputs: [failing_test, last_known_good_state, commit_range, test_execution_environment]
    outputs: [culprit_commit, change_diff, regression_root_cause]
    complexity: Medium
    knowledge_atoms: [KA-031]

  - skill_id: DOM-026-SK-007
    name: Multi-File Fix Coordination
    description: Coordinate repairs across multiple interdependent files while maintaining consistency and preventing cascading failures.
    inputs: [affected_files_list, dependency_graph, patch_sequence, consistency_rules]
    outputs: [coordinated_patches, application_order, verification_checkpoints]
    complexity: High
    knowledge_atoms: [KA-038]

  - skill_id: DOM-026-SK-008
    name: Fix Verification via Test Execution
    description: Execute comprehensive test suites to validate that repairs resolve the bug without introducing regressions.
    inputs: [patched_code, test_suite, regression_tests, baseline_metrics]
    outputs: [test_results, coverage_report, regression_report, verification_status]
    complexity: Medium
    knowledge_atoms: []

  - skill_id: DOM-026-SK-009
    name: Error Pattern Fingerprinting & Deduplication
    description: Generate cryptographic fingerprints of error patterns to identify duplicates and cluster related bugs.
    inputs: [error_signature, stack_trace_abstraction, error_message_template]
    outputs: [fingerprint_hash, duplicate_matches, cluster_id]
    complexity: Low
    knowledge_atoms: []

  - skill_id: DOM-026-SK-010
    name: Safe Sandboxed Debugging Execution
    description: Execute debugging operations in isolated sandbox environments to prevent accidental production system corruption.
    inputs: [debug_operation, sandbox_config, credential_guardrails, production_data_exemption]
    outputs: [sandbox_result, state_isolation_verified, data_exposure_audit]
    complexity: High
    knowledge_atoms: [KA-010]

  - skill_id: DOM-026-SK-011
    name: Log-Based Fault Trace Reconstruction
    description: Reconstruct detailed execution traces from log files, telemetry, and event streams to understand error context.
    inputs: [log_files, time_window, component_filter, event_schema]
    outputs: [execution_trace, causality_graph, temporal_sequence]
    complexity: Medium
    knowledge_atoms: []

  - skill_id: DOM-026-SK-012
    name: Runtime State Inspection & Snapshot Analysis
    description: Capture and analyze runtime application state at failure points to extract debugging context.
    inputs: [crash_dump, memory_snapshot, register_state, heap_analysis]
    outputs: [state_summary, anomaly_detection, object_graph_analysis]
    complexity: High
    knowledge_atoms: []

  - skill_id: DOM-026-SK-013
    name: Debugging Context Assembly
    description: Aggregate debugging information from multiple sources into a coherent context for analysis.
    inputs: [stack_trace, logs, metrics, code_context, user_actions, system_state]
    outputs: [unified_context, relationship_graph, priority_ranked_evidence]
    complexity: Medium
    knowledge_atoms: []

  - skill_id: DOM-026-SK-014
    name: Hypothesis Testing & Evidence Collection
    description: Systematically test hypotheses through experiments while collecting and evaluating evidence.
    inputs: [hypothesis, test_plan, evidence_collection_strategy, success_criteria]
    outputs: [test_results, evidence_set, hypothesis_validity_score]
    complexity: Medium
    knowledge_atoms: [KA-031]

  - skill_id: DOM-026-SK-015
    name: Causal Chain Analysis
    description: Decompose error causality into a chain of contributing factors from root cause to symptom manifestation.
    inputs: [root_cause, error_manifestation, system_dependencies, timing_information]
    outputs: [causal_chain, contributing_factors, failure_propagation_path]
    complexity: Medium
    knowledge_atoms: [KA-031]

  - skill_id: DOM-026-SK-016
    name: Automated Regression Testing Integration
    description: Automatically generate and integrate regression tests to prevent reoccurrence of fixed bugs.
    inputs: [bug_report, reproduction_steps, fix_verification_data, test_template]
    outputs: [regression_test_code, test_integration_config, coverage_metrics]
    complexity: Medium
    knowledge_atoms: []

  - skill_id: DOM-026-SK-017
    name: Error Context Window Management
    description: Manage limited context windows during debugging to preserve critical evidence within token budgets.
    inputs: [full_debugging_context, context_size_limit, importance_ranking]
    outputs: [pruned_context, compressed_summary, archive_references]
    complexity: Medium
    knowledge_atoms: []

  - skill_id: DOM-026-SK-018
    name: Dependency Graph Traversal for Impact Analysis
    description: Traverse code dependency graphs to identify all potentially affected components from a bug or fix.
    inputs: [bug_location, dependency_graph, change_diff]
    outputs: [impacted_components, risk_zones, safe_modification_boundaries]
    complexity: Medium
    knowledge_atoms: []

  - skill_id: DOM-026-SK-019
    name: Error Message Parsing & Semantic Extraction
    description: Parse and extract semantic meaning from error messages, codes, and diagnostics across multiple languages.
    inputs: [error_message, error_code, error_context, language_parsers]
    outputs: [parsed_components, semantic_meaning, error_category, action_suggestions]
    complexity: Low
    knowledge_atoms: []

  - skill_id: DOM-026-SK-020
    name: Repair Template Matching & Instantiation
    description: Match error patterns to known repair templates and instantiate them with bug-specific parameters.
    inputs: [error_pattern, repair_template_library, bug_parameters]
    outputs: [instantiated_repair, confidence_score, alternative_templates]
    complexity: Medium
    knowledge_atoms: [KA-038]

  - skill_id: DOM-026-SK-021
    name: Hotfix Expedited Approval Workflow Orchestration
    description: Route hotfix patches through expedited but tracked approval workflows to balance speed and safety.
    inputs: [hotfix_patch, severity_level, change_scope, approver_list]
    outputs: [approval_status, tracking_record, deployment_authorization]
    complexity: Medium
    knowledge_atoms: []

  - skill_id: DOM-026-SK-022
    name: Debug Session Time Budgeting & Resource Management
    description: Allocate and monitor time and resource budgets for debug sessions to prevent runaway debugging.
    inputs: [session_complexity, baseline_budget, resource_constraints]
    outputs: [time_allocation, milestone_checkpoints, escalation_triggers]
    complexity: Low
    knowledge_atoms: []

  - skill_id: DOM-026-SK-023
    name: Debugging Telemetry Aggregation & Analysis
    description: Aggregate telemetry from debugging sessions to extract patterns and improve future debugging efficiency.
    inputs: [debug_session_logs, telemetry_events, performance_metrics]
    outputs: [aggregate_patterns, efficiency_metrics, improvement_recommendations]
    complexity: Medium
    knowledge_atoms: []

  - skill_id: DOM-026-SK-024
    name: Graceful Degradation During Debugging
    description: Maintain system functionality at reduced capacity while debugging critical production issues.
    inputs: [affected_service, degradation_strategy, fallback_options, user_notification_config]
    outputs: [degraded_service_state, fallback_activation_status, user_communication]
    complexity: High
    knowledge_atoms: [KA-010]
```

```yaml
# output/operational/AGT-026/workflows.yaml
domain: DOM-026
domain_name: Debugging & Error Recovery
category: Workflows
total_workflows: 10

workflows:
  - workflow_id: DOM-026-WF-001
    name: Root Cause Analysis Workflow
    trigger: Test failure detected or production error alert
    steps:
      - step: 1
        name: Fault Localization
        action: Apply DOM-026-SK-001 to identify exact failure location
        entry_criteria: Error stack trace and error message available
        exit_criteria: Fault location and call chain identified
      
      - step: 2
        name: Context Assembly
        action: Execute DOM-026-SK-013 to aggregate all debugging context
        entry_criteria: Fault location known
        exit_criteria: Unified debugging context created
      
      - step: 3
        name: Hypothesis Generation
        action: Execute DOM-026-SK-002 to generate root cause hypotheses
        entry_criteria: Context assembled
        exit_criteria: Ranked list of hypotheses with confidence scores
      
      - step: 4
        name: Hypothesis Testing
        action: Execute DOM-026-SK-014 to systematically test hypotheses
        entry_criteria: Hypotheses generated
        exit_criteria: Evidence collected, strongest hypothesis identified
      
      - step: 5
        name: Causal Chain Documentation
        action: Execute DOM-026-SK-015 to create causal chain
        entry_criteria: Root cause confirmed
        exit_criteria: Complete causal analysis documented
      
      - step: 6
        name: Analysis Report Generation
        action: Synthesize findings into Root Cause Analysis report (DM-026-RCA)
        entry_criteria: All analysis steps complete
        exit_criteria: Report ready for repair team
    
    completion_criteria:
      - Root cause confidence score ≥ 85%
      - Causal chain fully documented
      - Evidence collected and logged
      - Report generated and reviewed
    
    rollback_plan: Archive analysis session, flag for human review if confidence < 70%

  - workflow_id: DOM-026-WF-002
    name: Automated Repair & Verification Workflow
    trigger: Root cause analysis completed with high confidence (≥ 85%)
    steps:
      - step: 1
        name: Repair Strategy Selection
        action: Apply DOM-026-SK-020 to match error pattern to repair templates
        entry_criteria: Root cause confirmed
        exit_criteria: Repair template and strategy selected
      
      - step: 2
        name: Patch Generation
        action: Execute DOM-026-SK-004 to synthesize code patches
        entry_criteria: Repair template selected
        exit_criteria: Patches generated for all affected files
      
      - step: 3
        name: Multi-File Coordination
        action: Execute DOM-026-SK-007 to coordinate patches across files
        entry_criteria: All patches generated
        exit_criteria: Coordinated patch sequence with consistency checks
      
      - step: 4
        name: Sandbox Deployment
        action: Execute DOM-026-SK-010 to safely deploy patch in sandbox
        entry_criteria: Patches coordinated and validated
        exit_criteria: Patch applied in isolated environment
      
      - step: 5
        name: Test Execution
        action: Execute DOM-026-SK-008 to run verification tests
        entry_criteria: Patch deployed in sandbox
        exit_criteria: All tests passed, regression report clear
      
      - step: 6
        name: Regression Test Generation
        action: Execute DOM-026-SK-016 to create regression tests
        entry_criteria: Fix verified
        exit_criteria: Regression test integrated into test suite
      
      - step: 7
        name: Approval & Deployment
        action: Execute DOM-026-SK-021 for hotfix approval if applicable
        entry_criteria: All verifications passed
        exit_criteria: Patch approved and deployed to production
    
    completion_criteria:
      - All verification tests passed
      - No regressions detected
      - Regression test integrated
      - Patch deployed and monitored
    
    rollback_plan: Revert patch, notify stakeholders, escalate to manual debugging

  - workflow_id: DOM-026-WF-003
    name: Error Triage & Classification Workflow
    trigger: New