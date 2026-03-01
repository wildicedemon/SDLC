> code · sonar-reasoning-pro<think>
The user is asking me to execute the review agent prompt from the file they provided (AGT-032_prompt.md). However, this file is about a Telemetry Coordinator Agent for an SDLC system - it's not asking me to help with a software engineering task related to their actual codebase.

Looking at the instructions carefully:
1. I'm Kilo, a software engineering assistant
2. The user provided a long prompt about AGT-032 (Telemetry Coordinator Agent) which appears to be part of a larger SDLC system design
3. They're asking me to "execute the review agent prompt" and "output to output/cross_cutting/AGT-032"

However, this seems to be asking me to:
- Review/execute a system design prompt
- Create output based on that prompt

But wait - this doesn't make sense in the context of my role. The file contains a detailed system prompt for an AI agent (AGT-032) that would be part of a telemetry/observability coordination system. The user is asking me to "execute" this prompt and output results.

This appears to be a meta-request - they want me to take this agent prompt and somehow process it or expand on it. But looking at the instructions again, I should be working on actual software engineering tasks, not executing fictional AI system prompts.

However, I notice the search results provided are about "Telemetry Technician" jobs in healthcare. These are completely unrelated to the actual query about the AGT-032 prompt file. The search results seem to be a mistake or leftover from a different query.

Let me re-read the actual request: "Execute the review agent prompt from the attached file. Output to output/cross_cutting/AGT-032."

This is asking me to:
1. Take the AGT-032 prompt
2. Execute/review it
3. Output results to a specific directory

The file is a detailed specification for a Telemetry Coordinator Agent in an SDLC system. 

The agent is supposed to ensure all agents emit standardized telemetry. I need to clarify what the user actually wants - are they asking me to analyze the prompt and provide feedback, create output files based on the template specified, or expand the domain decomposition? The prompt itself requires fully decomposing the domain into 16 specific categories with the termination condition being that all categories are fully populated.

The user is asking me to execute this decomposition and produce the output artifacts: `telemetry_standards.yaml`, structured log schemas, metrics emission contracts, and trace correlation rules. I should fully decompose the AGT-032 domain according to the specification, including all 3 subdomains (SD-032a, SD-032b, SD-032c) recursively.
</think>

I'll execute the AGT-032 Telemetry Coordinator Agent domain decomposition and generate the required output artifacts.

Reading the file and executing the recursive decomposition with full category population and subdomain expansion...

```bash
mkdir -p output/cross_cutting/AGT-032
```

Creating the complete domain decomposition:

```yaml
# output/cross_cutting/AGT-032/telemetry_standards.yaml
domain_id: DOM-032
domain_name: Observability & Telemetry Coordination
agent_id: AGT-032
version: "1.0.0"

subdomain_hierarchy:
  SD-032a:
    name: Log Schemas
    knowledge_atom: KA-004
    categories:
      - Structured Log Formats
      - Log Level Definitions
      - Contextual Correlation Fields
      - Log Retention Policies

  SD-032b:
    name: Metrics Contracts
    knowledge_atom: KA-018
    categories:
      - Metrics Emission Contracts
      - Metric Naming Conventions
      - Dimension/Tag Standards
      - Aggregation Rules

  SD-032c:
    name: Trace Correlation
    categories:
      - Distributed Trace Context Propagation
      - Trace ID Standards
      - Span Definitions
      - Cross-Agent Trace Correlation

categories:
  1_skills:
    DOM-032-SK-001:
      name: Structured Log Schema Definition
      description: Design and maintain standardized JSON-LD log schemas with version control
      capability_areas: [schema_design, schema_versioning, backward_compatibility]
      
    DOM-032-SK-002:
      name: Metrics Contract Authoring
      description: Define mandatory metrics emission contracts with SLO binding
      capability_areas: [contract_design, metric_taxonomy, slo_mapping]
      
    DOM-032-SK-003:
      name: Trace Correlation Protocol Definition
      description: Design W3C Trace Context propagation standards for agent communication
      capability_areas: [w3c_standards, context_propagation, span_correlation]
      
    DOM-032-SK-004:
      name: Telemetry Compliance Auditing
      description: Scan agent outputs against telemetry contracts; identify missing metrics/logs
      capability_areas: [compliance_scanning, gap_detection, audit_reporting]
      
    DOM-032-SK-005:
      name: Schema Migration Management
      description: Plan and execute schema migrations with zero data loss
      capability_areas: [schema_migration, data_transformation, rollback_planning]
      
    DOM-032-SK-006:
      name: Cross-Agent Trace Visualization
      description: Generate trace dependency graphs and critical path analysis
      capability_areas: [graph_generation, critical_path_analysis, bottleneck_detection]
      
    DOM-032-SK-007:
      name: Telemetry Gap Detection
      description: Proactively identify missing telemetry in agent interactions
      capability_areas: [gap_analysis, inference_logic, recommendation_generation]

  2_workflows:
    DOM-032-WF-001:
      name: Telemetry Standards Onboarding
      description: Assign contracts to new agents; validate initial compliance
      steps:
        - Identify new agent in system
        - Select appropriate telemetry contract template
        - Provision structured log schema
        - Assign metrics emission contract
        - Validate baseline compliance
      triggers: [new_agent_initialization]
      
    DOM-032-WF-002:
      name: Telemetry Compliance Audit
      description: Periodic compliance verification across all active agents
      steps:
        - Collect telemetry from all agents (sampling if needed)
        - Validate schema conformance
        - Check required metric emissions
        - Verify trace correlation completeness
        - Generate compliance report
        - Flag non-compliant agents
      frequency: continuous_with_hourly_reports
      triggers: [scheduled, manual_trigger, threshold_breach]
      
    DOM-032-WF-003:
      name: Schema Evolution
      description: Evolve telemetry schemas with version management
      steps:
        - Design new schema version
        - Create migration plan
        - Deploy schema alongside old version
        - Coordinate agent migration
        - Validate data consistency
        - Deprecate old schema
      triggers: [new_schema_required, compatibility_issue]
      
    DOM-032-WF-004:
      name: Cross-Agent Trace Debugging
      description: Reconstruct and analyze complete request traces
      steps:
        - Retrieve trace ID from any span
        - Collect all related spans across agents
        - Build trace DAG
        - Identify latency contributors
        - Detect anomalies or failures
        - Generate debug report
      triggers: [manual_investigation, performance_anomaly, error_spike]
      
    DOM-032-WF-005:
      name: Telemetry Infrastructure Health Check
      description: Monitor observability pipeline health
      steps:
        - Test metrics ingestion endpoint
        - Verify log collection pipeline
        - Check trace aggregation service
        - Monitor collection latency
        - Alert on pipeline failures
      frequency: every_5_minutes
      triggers: [scheduled, heartbeat_failure]

  3_task_templates:
    DOM-032-TT-001:
      name: Contract Assignment Task
      template: |-
        AgentID: {{agent_id}}
        ContractTemplate: {{contract_template}}
        RequiredMetrics: {{required_metrics_list}}
        RequiredLogs: {{required_logs_list}}
        TraceRequirements: {{trace_requirements}}
        ComplianceDeadline: {{deadline_timestamp}}
        
    DOM-032-TT-002:
      name: Compliance Report Generation Task
      template: |-
        ReportID: {{report_id}}
        Period: {{start_time}} - {{end_time}}
        AgentsCovered: {{agent_count}}
        ComplianceSummary:
          - OverallScore: {{overall_pct}}
          - SchemaCompliance: {{schema_pct}}
          - MetricCompliance: {{metric_pct}}
          - TraceCompliance: {{trace_pct}}
        NonCompliantAgents: {{non_compliant_list}}
        Recommendations: {{remediation_actions}}

  4_rules_and_constraints:
    DOM-032-RL-001:
      name: Mandatory Structured Logging
      rule: All agents must emit structured logs with correlation IDs
      enforcement: STRICT
      impact: Enables distributed tracing and debugging
      
    DOM-032-RL-002:
      name: Standard Metrics Emission
      rule: All agents must emit start/end/duration/result metrics for every operation
      enforcement: STRICT
      impact: Enables performance monitoring and SLO tracking
      
    DOM-032-RL-003:
      name: Schema Versioning
      rule: Telemetry schemas must be versioned and backward-compatible
      enforcement: STRICT
      impact: Enables schema evolution without breaking consumers
      
    DOM-032-RL-004:
      name: Log Level Standards
      rule: Log levels must follow TRACE|DEBUG|INFO|WARN|ERROR|FATAL
      enforcement: STRICT
      impact: Standardizes log analysis and filtering
      
    DOM-032-RL-005:
      name: Trace Context Propagation
      rule: Trace context must be propagated across all agent-to-agent communications
      enforcement: STRICT
      impact: Enables end-to-end request tracing
      
    DOM-032-RL-006:
      name: Sampling Strategy
      rule: High-volume operations must use configurable sampling (never eliminate)
      enforcement: MODERATE
      impact: Balances observability with cost
      
    DOM-032-RL-007:
      name: Metric Naming Convention
      rule: Metrics must follow domain_agent_operation_unit format
      enforcement: STRICT
      impact: Enables consistent metric aggregation
      
    DOM-032-RL-008:
      name: Telemetry Retention
      rule: Raw telemetry retained 7 days; aggregates retained 90 days
      enforcement: MODERATE
      impact: Balances storage cost with historical analysis capability

  5_interfaces:
    DOM-032-IF-001:
      name: Architecture Input Interface
      source: DOM-002
      direction: input
      contract: Architecture contracts include telemetry design patterns
      data_model: ArchitectureContract
      
    DOM-032-IF-002:
      name: Infrastructure Input Interface
      source: DOM-022
      direction: input
      contract: Observability infrastructure details (collectors, backends, APIs)
      data_model: ObservabilityInfrastructure
      
    DOM-032-IF-003:
      name: Telemetry Contract Output Interface
      target: All_Agents
      direction: output
      contract: Mandatory emission standards and validation rules
      data_model: TelemetryContract[]
      
    DOM-032-IF-004:
      name: Compliance Feed Interface
      target: DOM-035
      direction: output
      contract: Audit-trail compatible telemetry and compliance reports
      data_model: ComplianceReport
      
    DOM-032-IF-005:
      name: Cost Telemetry Interface
      target: DOM-029
      direction: output
      contract: Token counts, API call counts, resource utilization
      data_model: CostTelemetry
      
    DOM-032-IF-006:
      name: Performance Telemetry Interface
      target: DOM-037
      direction: output
      contract: Operation latency, throughput, error rates for regression detection
      data_model: PerformanceTelemetry
      
    DOM-032-IF-007:
      name: Pipeline Integration Interface
      target: DOM-021
      direction: output
      contract: Build and deployment metrics, pipeline health
      data_model: PipelineTelemetry

  6_dependencies:
    DOM-032-DP-001:
      agent: AGT-002
      type: hard_dependency
      reason: Requires architecture contracts to design telemetry patterns
      
    DOM-032-DP-002:
      agent: AGT-022
      type: hard_dependency
      reason: Depends on observability infrastructure for collection
      
    DOM-032-DP-003:
      agent: AGT-021
      type: coordinated_dependency
      reason: Enforces telemetry standards in CI/CD pipelines
      
    DOM-032-DP-004:
      agent: AGT-029
      type: data_dependency
      reason: Consumes cost metrics; provides cost telemetry
      
    DOM-032-DP-005:
      agent: AGT-035
      type: data_dependency
      reason: Provides compliance-audit telemetry
      
    DOM-032-DP-006:
      agent: AGT-037
      type: data_dependency
      reason: Provides performance metrics for regression detection

  7_state_models:
    DOM-032-SM-001:
      name: Telemetry Contract Lifecycle
      states:
        - Drafted: Initial specification, not yet enforced
        - Reviewed: Contract reviewed and approved
        - Published: Available for agent assignment
        - Active: Currently enforced on active agents
        - Evolving: Schema update in progress
        - Deprecated: Phased out; migration to new version in progress
        - Retired: No longer enforced
      transitions:
        - Drafted → Reviewed: manual_approval
        - Reviewed → Published: auto_on_approval
        - Published → Active: agent_assignment
        - Active → Evolving: schema_version_bump
        - Evolving → Active: migration_complete
        - Active → Deprecated: new_major_version
        - Deprecated → Retired: retention_period_expired
        
    DOM-032-SM-002:
      name: Agent Compliance State
      states:
        - Unknown: No compliance data available
        - Auditing: Compliance scan in progress
        - Compliant: All required telemetry being emitted
        - NonCompliant: Missing required metrics or logs
        - Remediating: Agent implementing compliance fixes
        - Suspended: Telemetry collection temporarily stopped
      transitions:
        - Unknown → Auditing: audit_trigger
        - Auditing → Compliant: all_checks_pass
        - Auditing → NonCompliant: failures_detected
        - NonCompliant → Remediating: remediation_started
        - Remediating → Compliant: re_audit_pass
        - NonCompliant → Suspended: critical_failures
        - Suspended → Remediating: manual_resume
        
    DOM-032-SM-003:
      name: Trace Correlation State
      states:
        - Initiated: Trace ID created for request
        - Propagating: Context propagated across agents
        - Complete: All spans collected
        - Analyzed: Trace analysis performed
        - Expired: Retention period exceeded
        - Archived: Long-term storage
      transitions:
        - Initiated → Propagating: auto_on_creation
        - Propagating → Complete: all_spans_collected
        - Complete → Analyzed: analysis_triggered
        - Analyzed → Expired: retention_days_elapsed
        - Expired → Archived: auto_archival

  8_data_models:
    DOM-032-DM-001:
      name: Telemetry Contract
      schema:
        contract_id: string
        agent_type: string
        version: string
        contract_status: enum[Drafted|Reviewed|Published|Active|Evolving|Deprecated|Retired]
        required_metrics:
          - metric_name: string
            dimensions: string[]
            sampling_rate: float [0.0-1.0]
            aggregation_type: enum[sum|avg|p99|histogram]
        required_logs:
          - log_type: string
            min_log_level: enum