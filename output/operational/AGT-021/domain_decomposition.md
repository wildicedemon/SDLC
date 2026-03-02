> code · sonar-reasoning-pro


<think>
The user is asking me to execute a code agent prompt from a file. The file contains a detailed specification for "AGT-021: CI/CD Pipeline Agent" which is a gap-filler agent for defining CI/CD pipeline orchestration patterns for an agentic AI coding system.

This is a complex system architecture document that asks me to:
1. Define 16 categories of CI/CD patterns (Skills, Workflows, Task Templates, Rules, Interfaces, Dependencies, State Models, Data Models, Control Flows, Failure Modes, Optimization Strategies, Coordination Mechanisms, Context Requirements, Memory Structures, Monitoring Requirements, Evolution Mechanisms)
2. Recursively expand 4 subdomains (Pipeline Design, Canary Deployment, Rollback Strategies, Artifact Management)
3. Synthesize CI/CD patterns from first principles and industry best practices (which I have search results for)
4. Generate outputs to `output/operational/AGT-021`

The search results provide excellent context about CI/CD best practices from multiple authoritative sources.

Given the instructions, I should:
1. Be concise and direct
2. Not be conversational or ask questions
3. Execute the task iteratively
4. Use tools to accomplish the goal
5. Minimize token usage

I need to create comprehensive CI/CD domain specifications based on the prompt requirements and search results, then output them to the specified directory.

Let me generate the comprehensive CI/CD domain definition with all 16 categories fully populated based on industry best practices from the search results.
</think>

I'll execute the AGT-021 CI/CD Pipeline Agent prompt by synthesizing industry best practices from the search results into a comprehensive domain decomposition. This generates all 16 required categories across 4 subdomains.

```bash
mkdir -p "output/operational/AGT-021"
```

Now I'll create the complete CI/CD domain specification:

```yaml
# output/operational/AGT-021/cicd_domain_specification.yaml
agent_id: AGT-021
agent_name: CI/CD Pipeline Orchestration Agent
domain: DOM-021
classification: Operational Gap-Filler (D9 CI/CD - 0 primary atoms)
execution_phase: Phase 4 - Post AGT-020, AGT-009, AGT-010
output_artifacts:
  - cicd_workflows.yaml
  - canary_deployment_configs.yaml
  - rollback_strategies.yaml
  - artifact_management_rules.yaml
  - pipeline_definitions.yaml

---

# CATEGORY 1: SKILLS
# ==================

skills:
  - skill_id: DOM-021-SK-001
    name: Pipeline-as-Code Definition
    description: Generate declarative pipeline definitions in YAML/JSON that define stages, triggers, and execution logic. Enables version control and reproducibility.
    inputs: [change_scope, infrastructure_spec, test_config, deployment_targets]
    outputs: [pipeline_definition, pipeline_yaml, validation_report]
    complexity: High
    source_confidence: HIGH

  - skill_id: DOM-021-SK-002
    name: Agent-Triggered Pipeline Execution
    description: Execute pipelines autonomously based on agent detection of code changes, passing execution context and environmental parameters.
    inputs: [trigger_event, change_metadata, agent_context]
    outputs: [execution_session, job_queue, status_stream]
    complexity: High
    source_confidence: HIGH

  - skill_id: DOM-021-SK-003
    name: Dynamic Stage Configuration
    description: Determine which pipeline stages to execute based on scope of changes (e.g., skip UI tests if only backend changed).
    inputs: [commit_diff, affected_components, test_matrix]
    outputs: [stage_execution_plan, conditional_logic]
    complexity: Medium
    source_confidence: HIGH

  - skill_id: DOM-021-SK-004
    name: Canary Deployment Configuration
    description: Define traffic splitting ratios, metric baselines, promotion/rollback thresholds for safe graduated deployments.
    inputs: [deployment_target, baseline_metrics, risk_profile]
    outputs: [traffic_split_config, metric_thresholds, promotion_criteria]
    complexity: High
    source_confidence: HIGH
    best_practice_ref: "[1][7]"

  - skill_id: DOM-021-SK-005
    name: Automated Rollback Execution
    description: Execute rollback procedures including state restoration, data migration reversal, and verification of rollback success.
    inputs: [rollback_trigger, current_state, previous_version]
    outputs: [rollback_execution_log, state_verification, success_confirmation]
    complexity: High
    source_confidence: HIGH

  - skill_id: DOM-021-SK-006
    name: Build Artifact Versioning
    description: Generate semantic version identifiers for build artifacts, manage artifact storage with content hashing for integrity.
    inputs: [build_metadata, version_strategy, artifact_content]
    outputs: [versioned_artifact_id, checksum, storage_location]
    complexity: Medium
    source_confidence: HIGH

  - skill_id: DOM-021-SK-007
    name: Artifact Provenance Tracking
    description: Maintain cryptographically verifiable chain of custody for artifacts from build through deployment.
    inputs: [artifact_id, build_context, deployment_history]
    outputs: [provenance_chain, digital_signature, audit_trail]
    complexity: High
    source_confidence: HIGH

  - skill_id: DOM-021-SK-008
    name: Pipeline Metric Collection
    description: Aggregate build time, test coverage, deployment frequency, MTTR and other KPIs across pipeline execution.
    inputs: [pipeline_execution, stage_logs, deployment_status]
    outputs: [metric_dataset, performance_report, trend_analysis]
    complexity: Medium
    source_confidence: HIGH
    best_practice_ref: "[3]"

  - skill_id: DOM-021-SK-009
    name: Parallel Stage Orchestration
    description: Execute independent pipeline stages concurrently while respecting dependency constraints and resource limits.
    inputs: [stage_dependency_graph, available_resources]
    outputs: [execution_schedule, resource_allocation, concurrency_plan]
    complexity: High
    source_confidence: HIGH

  - skill_id: DOM-021-SK-010
    name: Pipeline Cache Management
    description: Implement build caching strategies to reuse unchanged components, reducing pipeline execution time.
    inputs: [build_artifacts, dependency_tree, change_detection]
    outputs: [cache_strategy, cache_keys, cache_invalidation_rules]
    complexity: Medium
    source_confidence: HIGH
    best_practice_ref: "[1]"

  - skill_id: DOM-021-SK-011
    name: Infrastructure-as-Code Integration
    description: Provision and configure dynamic build environments using IaC patterns, auto-scaling based on pipeline load.
    inputs: [infrastructure_template, resource_requirements, scaling_policy]
    outputs: [provisioned_environment, connection_config, cleanup_schedule]
    complexity: High
    source_confidence: HIGH

  - skill_id: DOM-021-SK-012
    name: Secret & Credential Management
    description: Securely inject credentials into pipelines without exposing in logs/artifacts; rotate credentials on schedule.
    inputs: [credential_store, pipeline_context, environment_type]
    outputs: [injected_secrets, access_token, expiry_metadata]
    complexity: High
    source_confidence: HIGH
    best_practice_ref: "[6]"

  - skill_id: DOM-021-SK-013
    name: Pipeline Failure Analysis
    description: Automatically diagnose root causes of pipeline failures and suggest remediation actions.
    inputs: [failure_logs, stage_metrics, system_state]
    outputs: [failure_diagnosis, remediation_suggestions, alert_notification]
    complexity: High
    source_confidence: HIGH
    best_practice_ref: "[1]"

  - skill_id: DOM-021-SK-014
    name: Test Streamlining & Optimization
    description: Identify and eliminate redundant tests, implement test parallelization, and optimize test execution order.
    inputs: [test_suite, code_changes, execution_history]
    outputs: [optimized_test_plan, expected_runtime, coverage_report]
    complexity: Medium
    source_confidence: HIGH
    best_practice_ref: "[2]"

  - skill_id: DOM-021-SK-015
    name: Pipeline Governance & Approval
    description: Enforce approval workflows for production deployments with audit trails and policy compliance checks.
    inputs: [deployment_request, approval_policy, change_log]
    outputs: [approval_status, audit_record, deployment_authorization]
    complexity: Medium
    source_confidence: HIGH
    best_practice_ref: "[3]"

---

# CATEGORY 2: WORKFLOWS
# =====================

workflows:
  - workflow_id: DOM-021-WF-001
    name: Full CI/CD Pipeline Execution
    trigger: Code push to repository | Agent-initiated change detection
    description: Complete pipeline from code commit through production deployment with all validation gates.
    steps:
      - step_1:
          name: Trigger Detection & Context Gathering
          entry_criteria: Git webhook received OR agent change detection event
          action: Collect commit metadata, identify affected services, determine scope
          exit_criteria: Change scope determined, build context established
      - step_2:
          name: Build Artifact Creation
          entry_criteria: Code available in workspace
          action: Compile/package code, run build optimization cache checks, generate versioned artifact
          exit_criteria: Artifact created, checksum verified, stored in artifact repository
      - step_3:
          name: Unit Testing
          entry_criteria: Build artifact available
          action: Execute unit tests in parallel across affected components, collect coverage metrics
          exit_criteria: Test results reported; if <95% coverage OR failures present, FAIL; else PASS
      - step_4:
          name: Integration Testing
          entry_criteria: Unit tests passed
          action: Deploy artifact to integration test environment, execute integration test suite
          exit_criteria: Integration tests passed OR documented acceptable failures; coverage >90%
      - step_5:
          name: Security Scanning
          entry_criteria: Artifact available
          action: SAST/dependency scanning, secrets detection, vulnerability assessment
          exit_criteria: No critical vulnerabilities found; all policy checks passed
      - step_6:
          name: Artifact Publication
          entry_criteria: All tests and security scans passed
          action: Publish artifact with provenance metadata, publish build logs, trigger downstream jobs
          exit_criteria: Artifact available in production artifact repository with audit trail
      - step_7:
          name: Staging Deployment
          entry_criteria: Artifact published
          action: Deploy to staging environment, run smoke tests, verify infrastructure
          exit_criteria: Application healthy in staging, endpoints responding, metrics baseline established
      - step_8:
          name: Production Approval Gate
          entry_criteria: Staging deployment successful
          action: Notify approvers, collect manual approval, verify deployment window
          exit_criteria: Approval received from authorized personnel within time limit
      - step_9:
          name: Canary Deployment
          entry_criteria: Production approval received
          action: Deploy to canary (5% traffic), monitor metrics vs baseline, compare error rates
          exit_criteria: Canary metrics healthy OR degradation detected triggering rollback
      - step_10:
          name: Production Promotion
          entry_criteria: Canary metrics passed
          action: Gradually increase traffic (10% → 25% → 50% → 100%) with metric monitoring at each stage
          exit_criteria: 100% traffic reached OR rollback triggered
      - step_11:
          name: Deployment Verification
          entry_criteria: Canary promoted to production
          action: Run production smoke tests, verify business metrics, check alert thresholds
          exit_criteria: All verifications passed; deployment complete notification sent
    completion_criteria: Artifact deployed to production OR rollback completed with previous version restored
    rollback_plan: |
      If any step fails:
        - Steps 1-6: Halt pipeline, notify engineering team, no customer impact
        - Steps 7-8: Revert staging deployment, retain artifact for analysis
        - Steps 9-11: Execute canary/production rollback workflow (DOM-021-WF-003)
    estimated_duration: 45-90 minutes
    parallel_stages: [2,3,5], [4,7]
    dependencies: AGT-020 (testing config), AGT-009 (infrastructure), AGT-027 (deployment execution)

  - workflow_id: DOM-021-WF-002
    name: Canary Deployment & Gradual Promotion
    trigger: Artifact available AND production approval granted
    description: Execute controlled canary release with metric-based promotion to full production rollout.
    steps:
      - step_1:
          name: Canary Initialization
          entry_criteria: Production approval received, baseline metrics collected
          action: Deploy version to 5% of production traffic, configure traffic splitter, establish metric collection
          exit_criteria: Canary endpoints receiving 5% traffic, metrics flowing to monitoring
      - step_2:
          name: Baseline Comparison
          entry_criteria: Canary running for 5 minutes
          action: Collect canary metrics, compare error rate/latency/throughput against baseline, compute deltas
          exit_criteria: Metric comparison completed; decision ready
      - step_3:
          name: Metric Evaluation & Decision
          entry_criteria: Baseline comparison complete
          action: |
            If error_rate_delta > threshold OR latency_increase > threshold: ROLLBACK
            If metrics acceptable: PROMOTE to next stage
          exit_criteria: Promotion or rollback decision made
      - step_4:
          name: Gradual Traffic Shifting
          entry_criteria: Metric evaluation passed
          action: |
            Traffic shift schedule:
            - Stage 1: 10% (5 min monitoring)
            - Stage 2: 25% (5 min monitoring)
            - Stage 3: 50% (10 min monitoring)
            - Stage 4: 100% (5 min final verification)
            At each stage: re-evaluate metrics, continue or rollback
          exit_criteria: 100% traffic reached OR rollback triggered
      - step_5:
          name: Final Verification
          entry_criteria: 100% traffic reached
          action: Run production smoke tests, verify business metrics, check SLA compliance
          exit_criteria: All metrics healthy; deployment marked complete
    completion_criteria: 100% traffic reached AND all metrics within acceptable range
    rollback_plan: Execute DOM-021-WF-003 at any stage if metrics exceed thresholds
    rollback_decision_criteria:
      - Error rate increase > 5%
      - Latency increase > 10%
      - Memory/CPU anomalies detected
      - Business metric decline > 2%
    monitoring_duration: 25 minutes minimum
    dependencies: AGT-022 (observability), DOM-021-SM-002 (canary state machine)

  - workflow_id: DOM-021-WF-003
    name: Rollback Execution & Verification
    trigger: Metric threshold exceeded during canary OR operator-initiated rollback request
    description: Execute controlled rollback to previous stable version with state restoration and verification.
    steps:
      - step_1:
          name: Rollback Initiation
          entry_criteria: Rollback trigger detected (automatic OR manual)
          action: Immediately halt traffic shift, redirect to previous version, log rollback reason
          exit_criteria: New traffic stopped within 10 seconds, previous version receiving traffic
      - step_2:
          name: State Restoration
          entry_criteria: Traffic redirected to previous version
          action: |
            For stateless services: Complete (traffic redirect sufficient)
            For stateful services: Restore database state from pre-deployment snapshot
            For caches: Invalidate canary cache entries
          exit_criteria: System state consistent with previous deployment
      - step_3:
          name: Data Consistency Verification
          entry_criteria: State restoration complete
          action: Run consistency checks on database, verify data integrity, reconcile in-flight transactions
          exit_criteria: No data corruption detected; consistency verified
      - step_4:
          name: Service Health Verification
          entry_criteria: State restored
          action: Run health checks, smoke tests, verify endpoints responding, check error rates returning to baseline
          exit_criteria: All health checks pass; service stable
      - step_5:
          name: Rollback Completion & Notification
          entry_criteria: Health verification passed
          action: Mark deployment as rolled back, notify stakeholders, create incident record
          exit_criteria: Rollback audit trail complete, incident documentation created
    completion_criteria: Previous version fully operational AND system health verified
    expected_duration: 5-10 minutes total
    maximum_allowed_duration: 15 minutes
    failure_handling: |
      If rollback itself fails:
        - Stop all deployment operations
        - Engage on-call engineering team immediately
        - Escalate to incident