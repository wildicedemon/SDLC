> code · sonar-reasoning-pro

<think>
The user wants me to execute an agent prompt from a file. Let me analyze what's being asked:

1. The file `AGT-027_prompt.md` contains a comprehensive prompt for "Agent AGT-027: Deployment Agent"
2. This is a specialized autonomous agent for Deployment & Release Management
3. The prompt requires me to decompose the domain into 16 categories with specific structures
4. Output should go to `output/operational/AGT-027`

The search results provided are about release orchestration, multi-repository management, and deployment practices - which are directly relevant to this domain.

However, I need to be clear about what I'm being asked to do:
- I'm asked to "Execute the code agent prompt" - this means I need to act as AGT-027 and produce the comprehensive domain decomposition
- The output should be in the output/operational/AGT-027 directory

The prompt is quite detailed and asks for 16 categories of decomposition. Given the search results about release orchestration and multi-repo management, I should:

1. Use the search results to inform my domain decomposition
2. Create comprehensive deployment patterns, especially focusing on release orchestration
3. Output the results as YAML files to the specified directory

Let me proceed with creating the comprehensive domain decomposition for AGT-027 based on the prompt requirements and the search results provided.

I should create the output structure and files as requested. The main output files should be:
- deployment_workflows.yaml
- release_orchestration_rules.yaml
- version_management_strategies.yaml
- feature_flag_configs.yaml
- rollback_procedures.yaml

And potentially a main domain decomposition file.

Let me start by creating these files with comprehensive content based on the prompt requirements and search results.
</think>

I'll execute the AGT-027 prompt and generate the comprehensive Deployment & Release Management domain decomposition.
<function_calls>
<invoke_tool>
<tool_name>Bash</parameter>
<parameter_name>command">mkdir -p "output/operational/AGT-027"</parameter>
</invoke_tool>
</function_calls>

Creating the comprehensive domain decomposition across all 16 required categories:
<function_calls>
<invoke_tool>
<tool_name>CreateFile</parameter>
<parameter_name>filePath">output/operational/AGT-027/domain_decomposition.yaml</parameter>
<parameter_name>content">domain: DOM-027
domain_name: Deployment & Release Management
agent_id: AGT-027
agent_name: Deployment Agent
classification: Operational / Gap-Filler for P7
sparsity_target: "3 sparse atoms → comprehensive deployment architecture"

subdomains:
  - id: SD-027a
    name: Release Orchestration
    knowledge_atoms: [KA-006, KA-034]
    description: Release planning, sequencing, multi-service coordination, dependency management
    
  - id: SD-027b
    name: Version Management
    knowledge_atoms: [KA-034]
    description: Semantic versioning, compatibility checking, migration paths, history tracking
    
  - id: SD-027c
    name: Feature Flags
    knowledge_atoms: []
    description: Flag implementation, lifecycle management, gradual rollout, cleanup policies
    
  - id: SD-027d
    name: Blue-Green Deployments
    knowledge_atoms: [KA-006]
    description: Architecture, traffic switching, environment parity, seamless cutover

# ============================================================================
# 1. SKILLS
# ============================================================================
skills:
  - id: DOM-027-SK-001
    name: Release Plan Generation
    description: Generate structured release plans with service sequencing, dependency graphs, and scheduling
    inputs: [service_manifests, change_logs, deployment_calendar, business_priorities]
    outputs: [release_plan, dependency_graph, sequence_diagram]
    complexity: High
    domain_binding: SD-027a

  - id: DOM-027-SK-002
    name: Multi-Service Release Coordination
    description: Coordinate atomic release of multiple interdependent services respecting dependency ordering
    inputs: [release_plan, service_versions, dependency_matrix]
    outputs: [orchestration_script, coordination_manifest]
    complexity: High
    domain_binding: SD-027a

  - id: DOM-027-SK-003
    name: Semantic Version Calculation
    description: Calculate and assign semantic versions based on API compatibility and feature sets
    inputs: [previous_version, change_type, api_changes, feature_list]
    outputs: [new_version, version_bump_justification]
    complexity: Medium
    domain_binding: SD-027b

  - id: DOM-027-SK-004
    name: Version Compatibility Validation
    description: Verify version compatibility across service dependencies and identify breaking changes
    inputs: [service_versions, dependency_constraints, schema_changes]
    outputs: [compatibility_report, breaking_change_list, migration_guide]
    complexity: High
    domain_binding: SD-027b

  - id: DOM-027-SK-005
    name: Feature Flag Configuration
    description: Configure feature flags with rollout percentages, user segments, and safe defaults
    inputs: [feature_definition, rollout_strategy, user_segments, experiment_config]
    outputs: [flag_config, rollout_schedule]
    complexity: Medium
    domain_binding: SD-027c

  - id: DOM-027-SK-006
    name: Gradual Rollout Management
    description: Manage percentage-based rollout of features with automatic rollback triggers
    inputs: [flag_id, current_percentage, health_metrics, error_rate_threshold]
    outputs: [updated_percentage, rollout_status, rollback_decision]
    complexity: Medium
    domain_binding: SD-027c

  - id: DOM-027-SK-007
    name: Blue-Green Environment Provisioning
    description: Provision parallel green environment with identical configuration to blue
    inputs: [blue_environment_config, infrastructure_spec, resource_limits]
    outputs: [green_environment, parity_validation_report]
    complexity: Medium
    domain_binding: SD-027d

  - id: DOM-027-SK-008
    name: Environment Parity Validation
    description: Validate blue-green environment configuration, dependencies, and data consistency
    inputs: [blue_env_state, green_env_state, validation_rules]
    outputs: [parity_report, discrepancies, switch_approval]
    complexity: High
    domain_binding: SD-027d

  - id: DOM-027-SK-009
    name: Traffic Switching Orchestration
    description: Execute atomic traffic switch from blue to green with no service interruption
    inputs: [load_balancer_config, switch_strategy, rollback_threshold, monitoring_rules]
    outputs: [switch_execution_log, traffic_distribution_log]
    complexity: High
    domain_binding: SD-027d

  - id: DOM-027-SK-010
    name: Post-Deployment Health Verification
    description: Execute comprehensive health checks against deployed service within time window
    inputs: [deployment_config, health_check_suite, timeout_window, success_criteria]
    outputs: [health_check_report, deployment_status, health_score]
    complexity: High
    domain_binding: SD-027a

  - id: DOM-027-SK-011
    name: Release Note Generation
    description: Generate comprehensive release notes from changelog entries and commit metadata
    inputs: [changelog_entries, commit_history, version, api_changes, feature_list]
    outputs: [release_notes, upgrade_guide, deprecation_notices]
    complexity: Medium
    domain_binding: SD-027a

  - id: DOM-027-SK-012
    name: Rollback Execution
    description: Execute rollback to previous version with data consistency validation
    inputs: [target_version, rollback_strategy, data_migration_plan, pre_rollback_snapshot]
    outputs: [rollback_execution_log, post_rollback_state, success_status]
    complexity: High
    domain_binding: SD-027a

  - id: DOM-027-SK-013
    name: Release Approval Gate Management
    description: Orchestrate multi-stakeholder approval process with escalation and timeout handling
    inputs: [release_plan, approval_rules, stakeholder_list, approval_window]
    outputs: [approval_status, approver_log, escalation_status]
    complexity: Medium
    domain_binding: SD-027a

  - id: DOM-027-SK-014
    name: Deployment Dependency Resolution
    description: Resolve and order complex service dependencies with topological sort and conflict detection
    inputs: [service_dependency_graph, version_constraints]
    outputs: [deployment_sequence, conflict_list, unresolvable_dependencies]
    complexity: High
    domain_binding: SD-027a

  - id: DOM-027-SK-015
    name: Feature Flag Lifecycle Management
    description: Manage complete feature flag lifecycle from creation through cleanup with ownership tracking
    inputs: [flag_definition, creation_context, owner, expiry_date]
    outputs: [flag_lifecycle_record, cleanup_checklist]
    complexity: Medium
    domain_binding: SD-027c

  - id: DOM-027-SK-016
    name: Canary Deployment Execution
    description: Execute canary deployment directing small traffic percentage to new version
    inputs: [canary_percentage, duration, error_threshold, rollback_trigger]
    outputs: [canary_metrics, success_decision, rollback_trigger_status]
    complexity: High
    domain_binding: SD-027a

# ============================================================================
# 2. WORKFLOWS
# ============================================================================
workflows:
  - id: DOM-027-WF-001
    name: Full Release Orchestration Workflow
    description: End-to-end orchestration from planning through verification
    trigger: "Release scheduled OR manual release request"
    steps:
      - step: 1
        name: Release Plan Validation
        entry_criteria: "Release plan exists and is signed off"
        action: "Validate release plan, dependency graph, approval chain"
        exit_criteria: "Plan approved or escalated"
        timeout: 4h
        
      - step: 2
        name: Build Validation
        entry_criteria: "Release plan validated"
        action: "Verify all service builds are ready, artifacts signed, tests passing"
        exit_criteria: "All builds verified and staged"
        timeout: 2h
        
      - step: 3
        name: Staging Deployment
        entry_criteria: "Builds validated"
        action: "Deploy to staging environment for final integration testing"
        exit_criteria: "Staging deployment successful, integration tests pass"
        timeout: 1h
        
      - step: 4
        name: Release Approval
        entry_criteria: "Staging tests passing"
        action: "Obtain required approvals from stakeholders (list from release plan)"
        exit_criteria: "All required approvers have signed off"
        timeout: 8h
        escalation: "Auto-escalate to release manager after 4h"
        
      - step: 5
        name: Production Deployment
        entry_criteria: "All approvals obtained"
        action: "Deploy using configured strategy (blue-green/canary/rolling)"
        exit_criteria: "Deployment completed without errors"
        timeout: 2h
        rollback_trigger: "Any health check failure during deployment"
        
      - step: 6
        name: Health Verification
        entry_criteria: "Deployment completed"
        action: "Execute post-deployment health checks, monitor key metrics"
        exit_criteria: "All health checks passing, error rates normal"
        timeout: 30m
        
      - step: 7
        name: Release Finalization
        entry_criteria: "Health checks passing"
        action: "Generate release notes, publish release, update documentation"
        exit_criteria: "Release published and communicated"
        timeout: 1h
    
    completion_criteria: "All steps completed successfully, release marked as RELEASED"
    rollback_plan: "If any step fails, trigger DOM-027-WF-004 (Rollback Workflow)"

  - id: DOM-027-WF-002
    name: Blue-Green Deployment Execution Workflow
    description: Execute blue-green deployment with traffic switching and environment parity validation
    trigger: "Release approved OR manual blue-green deployment request"
    deployment_method: "Blue-Green"
    steps:
      - step: 1
        name: Green Environment Provisioning
        entry_criteria: "Blue environment stable, deployment approved"
        action: "Provision green environment with identical specs to blue"
        exit_criteria: "Green environment up, configured, and ready"
        timeout: 20m
        
      - step: 2
        name: Service Deployment to Green
        entry_criteria: "Green environment ready"
        action: "Deploy new service version to green environment"
        exit_criteria: "All services running in green"
        timeout: 15m
        
      - step: 3
        name: Environment Parity Validation
        entry_criteria: "Services running in green"
        action: "Compare configurations, run parity tests, validate data consistency"
        exit_criteria: "Parity validated, no discrepancies found"
        timeout: 10m
        
      - step: 4
        name: Smoke Testing on Green
        entry_criteria: "Parity validated"
        action: "Run smoke test suite against green environment"
        exit_criteria: "All smoke tests passing"
        timeout: 5m
        
      - step: 5
        name: Traffic Switch
        entry_criteria: "Smoke tests passing, switch approved"
        action: "Atomically switch load balancer traffic from blue to green"
        exit_criteria: "Traffic fully routed to green (100%)"
        timeout: 2m
        
      - step: 6
        name: Post-Switch Monitoring
        entry_criteria: "Traffic switched"
        action: "Monitor green for errors, latency, resource utilization"
        exit_criteria: "Metrics stable, no errors detected (5m window)"
        timeout: 10m
        
      - step: 7
        name: Blue Environment Decommission
        entry_criteria: "Green stable post-switch"
        action: "Gracefully shut down blue environment, preserve snapshot for quick rollback"
        exit_criteria: "Blue resources released, snapshot archived"
        timeout: 5m
    
    completion_criteria: "Traffic fully on green, blue decommissioned, deployment marked SUCCESS"
    rollback_plan: "If switch fails or green unstable, reverse traffic immediately and preserve blue"

  - id: DOM-027-WF-003
    name: Feature Flag Gradual Rollout Workflow
    description: Execute feature flag rollout with percentage-based traffic management
    trigger: "Feature flag created and configured"
    steps:
      - step: 1
        name: Flag Initialization
        entry_criteria: "Flag configured with rollout strategy"
        action: "Create flag in flag management system, set to initial percentage (1-5%)"
        exit_criteria: "Flag exists and is active at initial percentage"
        timeout: 5m
        
      - step: 2
        name: Canary Monitoring
        entry_criteria: "Flag active at initial percentage"
        action: "Monitor error rates, latency, feature-specific metrics for 30 minutes"
        exit_criteria: "Error rate below threshold, no critical issues"
        timeout: 35m
        
      - step: 3
        name: Percentage Increase Decision
        entry_criteria: "Canary period complete"
        action: "Evaluate metrics; if healthy increase to next tier (5% → 25% → 50% → 100%)"
        exit_criteria: "Percentage increased or rollback triggered"
        timeout: 5m
        
      - step: 4
        name: Tier Monitoring
        entry_criteria: "Percentage increased"
        action: "Monitor for 1 hour at new percentage tier"
        exit_criteria: "Healthy metrics OR rollback triggered"
        timeout: 65m
        loop_condition: "Repeat until 100% OR error threshold exceeded"
        
      - step: 5
        name: Full Rollout Completion
        entry_criteria: "Flag at 100% for 1 hour"
        action: "Mark flag as fully rolled out, remove gradual rollout configuration"
        exit_criteria: "Flag in FULLY_ROLLED state"
        timeout: 5m
        
      - step: 6
        name: Cleanup Scheduling
        entry_criteria: "Flag fully rolled out"
        action: "Schedule flag cleanup/removal after grace period (typically 2 weeks)"
        exit_criteria: "Cleanup scheduled, owner notified"
        timeout: 5m