> code · sonar-reasoning-pro


<think>
The user has provided a file path to read and wants me to execute the architect agent prompt. This is the AGT-034 MCP Integration Coordinator Agent prompt. They want output to be generated to `output/cross_cutting/AGT-034`.

Looking at the file, this is a comprehensive agent specification that requires:
1. Full decomposition into 16 categories
2. Recursive expansion of 3 subdomains
3. Gap detection and resolution
4. Output artifacts: `mcp_configurations.yaml`, `rules.yaml`, etc.

The prompt is asking for a complete definition of the MCP Integration Coordinator Agent's domain with all skills, workflows, task templates, rules, interfaces, dependencies, state models, data models, control flows, failure modes, optimization strategies, coordination mechanisms, context requirements, memory structures, monitoring requirements, and evolution mechanisms.

This is a complex task that requires:
1. Understanding MCP (Model Context Protocol) from the search results
2. Decomposing the domain comprehensively
3. Creating YAML configurations
4. Following the recursive expansion directive
5. Detecting and resolving gaps

I should create output files with:
- Complete domain decomposition
- MCP configurations
- Rules and compliance standards
- Server templates
- All 16 categories populated

Let me work through this systematically and create the required artifacts.
</think>

I'll execute the AGT-034 MCP Integration Coordinator Agent specification, decomposing the domain and generating the required artifacts.
<function_calls>
<invoke name="bash">
<parameter name="command">mkdir -p "c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\cross_cutting\AGT-034"</parameter>
</invoke>
</function_calls>
<function_calls>
<invoke name="file_edit">
<parameter name="filePath">c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\cross_cutting\AGT-034\mcp_configurations.yaml</parameter>
<parameter name="mode">create</parameter>
<parameter name="content">version: "1.0"
agent_id: "AGT-034"
agent_name: "MCP Integration Coordinator Agent"
domain_id: "DOM-034"
domain_name: "MCP Integration Coordination"
category: "Cross-Cutting"
execution_phase: "Continuous (post-Phase-1)"

mcp_framework:
  protocol_version: "1.0"
  standardization_scope:
    - tool_registration
    - server_discovery
    - protocol_compliance
    - invocation_patterns
    - lifecycle_management

mcp_servers:
  registration_schema:
    server_id:
      type: "string"
      pattern: "^MCP-SRV-[0-9]{4}$"
      description: "Unique MCP server identifier"
    name:
      type: "string"
      description: "Human-readable server name"
    capabilities:
      type: "array"
      items:
        type: "object"
        properties:
          tool_id:
            type: "string"
          tool_name:
            type: "string"
          category:
            type: "string"
            enum:
              - "data_retrieval"
              - "data_mutation"
              - "analysis"
              - "automation"
              - "coordination"
          capability_level:
            type: "string"
            enum:
              - "basic"
              - "advanced"
              - "expert"
    version:
      type: "string"
      pattern: "^[0-9]+\\.[0-9]+\\.[0-9]+$"
    endpoint:
      type: "string"
      format: "uri"
    auth_method:
      type: "string"
      enum:
        - "api_key"
        - "oauth2"
        - "mutual_tls"
        - "service_account"
    health_check_url:
      type: "string"
      format: "uri"
    health_check_interval_ms:
      type: "integer"
      minimum: 5000
      maximum: 300000
    timeout_ms:
      type: "integer"
      minimum: 1000
      maximum: 60000
    owner_agent:
      type: "string"
      pattern: "^AGT-[0-9]{3}$"
    tags:
      type: "array"
      items:
        type: "string"
    cost_per_invocation:
      type: "number"
      minimum: 0
    created_date:
      type: "string"
      format: "date-time"
    deprecated:
      type: "boolean"
      default: false

tool_capability_schema:
  tool_id:
    type: "string"
    pattern: "^TOOL-[0-9A-Z]{8}$"
  server_id:
    type: "string"
  name:
    type: "string"
  description:
    type: "string"
  input_schema:
    type: "object"
    properties:
      type:
        type: "string"
        enum:
          - "object"
          - "array"
          - "string"
          - "number"
          - "boolean"
      properties:
        type: "object"
        additionalProperties: true
      required:
        type: "array"
        items:
          type: "string"
  output_schema:
    type: "object"
    properties:
      type:
        type: "string"
      properties:
        type: "object"
      additionalProperties: true
  timeout_ms:
    type: "integer"
    minimum: 1000
  error_handling:
    type: "object"
    properties:
      retry_strategy:
        type: "string"
        enum:
          - "exponential_backoff"
          - "linear_backoff"
          - "no_retry"
      max_retries:
        type: "integer"
        minimum: 0
        maximum: 10
      timeout_behavior:
        type: "string"
        enum:
          - "fail"
          - "timeout_response"
          - "circuit_break"

invocation_record_schema:
  invocation_id:
    type: "string"
    pattern: "^INV-[0-9]{16}$"
  tool_id:
    type: "string"
  agent_id:
    type: "string"
  request:
    type: "object"
  response:
    type: "object"
  status:
    type: "string"
    enum:
      - "success"
      - "failed"
      - "timeout"
      - "rate_limited"
      - "circuit_breaker_open"
  duration_ms:
    type: "integer"
  trace_id:
    type: "string"
    pattern: "^TRACE-[0-9A-Z]{16}$"
  correlation_id:
    type: "string"
  error:
    type: "object"
    properties:
      code:
        type: "string"
      message:
        type: "string"
  timestamp:
    type: "string"
    format: "date-time"

compliance_report_schema:
  server_id:
    type: "string"
  audit_date:
    type: "string"
    format: "date"
  protocol_version:
    type: "string"
  compliance_status:
    type: "string"
    enum:
      - "compliant"
      - "non_compliant"
      - "compliant_with_exceptions"
  violations:
    type: "array"
    items:
      type: "object"
      properties:
        violation_id:
          type: "string"
        rule_id:
          type: "string"
        severity:
          type: "string"
          enum:
            - "critical"
            - "high"
            - "medium"
            - "low"
        description:
          type: "string"
  remediation_actions:
    type: "array"
    items:
      type: "object"
      properties:
        action_id:
          type: "string"
        rule_id:
          type: "string"
        status:
          type: "string"
          enum:
            - "pending"
            - "in_progress"
            - "completed"
            - "failed"
        due_date:
          type: "string"
          format: "date"

server_lifecycle_states:
  - state: "Proposed"
    description: "Server proposed but not yet registered"
    allowed_transitions:
      - "Registered"
      - "Rejected"
  - state: "Registered"
    description: "Server registered and awaiting validation"
    allowed_transitions:
      - "Validating"
      - "Cancelled"
  - state: "Validating"
    description: "Server undergoing compliance and capability validation"
    allowed_transitions:
      - "Active"
      - "ValidationFailed"
  - state: "Active"
    description: "Server fully operational and compliant"
    allowed_transitions:
      - "Degraded"
      - "Maintenance"
      - "Deprecation"
  - state: "Degraded"
    description: "Server operational but with reduced capability or performance"
    allowed_transitions:
      - "Active"
      - "Maintenance"
      - "Removed"
  - state: "Maintenance"
    description: "Server undergoing updates or repairs"
    allowed_transitions:
      - "Active"
      - "Degraded"
  - state: "Deprecation"
    description: "Server marked for eventual removal"
    allowed_transitions:
      - "Active"
      - "Removed"
  - state: "ValidationFailed"
    description: "Server failed validation and cannot be activated"
    allowed_transitions:
      - "Cancelled"
  - state: "Removed"
    description: "Server decommissioned and archived"
    allowed_transitions: []
  - state: "Cancelled"
    description: "Server registration cancelled"
    allowed_transitions: []

tool_invocation_states:
  - state: "Requested"
    description: "Tool invocation requested by agent"
  - state: "Queued"
    description: "Invocation queued for execution"
  - state: "Routed"
    description: "Invocation routed to appropriate server"
  - state: "Executing"
    description: "Tool executing on server"
  - state: "Completed"
    description: "Tool execution completed successfully"
  - state: "Failed"
    description: "Tool execution failed with error"
  - state: "TimedOut"
    description: "Tool execution exceeded timeout threshold"
  - state: "Retrying"
    description: "Failed invocation being retried"

compliance_states:
  - state: "Unchecked"
    description: "Server compliance not yet evaluated"
  - state: "Auditing"
    description: "Compliance audit in progress"
  - state: "Compliant"
    description: "Server fully compliant with standards"
  - state: "NonCompliant"
    description: "Server violates compliance standards"
  - state: "Remediating"
    description: "Non-compliance being addressed"
  - state: "Archived"
    description: "Server removed, compliance archived"

cross_cutting_patterns:
  agent_to_agent_handoff:
    enabled: true
    context_preservation: true
    correlation_tracking: true
  tool_discovery_pattern: "dynamic_with_caching"
  security_validation: "pre_invocation"
  observability_integration: "full_logging"
  cost_tracking: "per_invocation"
</parameter>
</invoke>
</function_calls>
<function_calls>
<invoke name="file_edit">
<parameter name="filePath">c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\cross_cutting\AGT-034\rules.yaml</parameter>
<parameter name="mode">create</parameter>
<parameter name="content">version: "1.0"
agent_id: "AGT-034"
rule_engine: "StandardsEnforcement"

rules:
  DOM-034-RL-001:
    name: "Mandatory Capability Declaration"
    category: "Registration"
    priority: "CRITICAL"
    description: "All MCP tools must declare capabilities using standardized capability schema"
    rule_type: "registration_validation"
    enforcement:
      point: "pre_activation"
      action: "block_registration"
    validation:
      - capability_schema_present: true
      - tool_name_present: true
      - input_schema_valid: true
      - output_schema_valid: true
      - error_handling_defined: true

  DOM-034-RL-002:
    name: "Correlation ID Propagation"
    category: "Protocol"
    priority: "CRITICAL"
    description: "All MCP invocations must include correlation IDs for trace propagation"
    rule_type: "invocation_validation"
    enforcement:
      point: "pre_invocation"
      action: "reject_request"
    validation:
      - correlation_id_format: "^TRACE-[0-9A-Z]{16}$"
      - trace_id_included: true
      - parent_span_id_included: true

  DOM-034-RL-003:
    name: "Timeout Threshold Compliance"
    category: "Performance"
    priority: "HIGH"
    description: "MCP servers must respond within configured timeout thresholds"
    rule_type: "invocation_monitoring"
    enforcement:
      point: "execution"
      action: "enforce_timeout"
    parameters:
      default_timeout_ms: 30000
      max_timeout_ms: 60000
      min_timeout_ms: 1000
      slow_query_threshold_ms: 5000

  DOM-034-RL-004:
    name: "Duplicate Tool Detection"
    category: "Deduplication"
    priority: "HIGH"
    description: "Duplicate tool registrations across agents must be detected and consolidated"
    rule_type: "registration_audit"
    enforcement:
      point: "continuous"
      action: "flag_for_consolidation"
    validation:
      - tool_name_uniqueness: true
      - capability_set_comparison: true
      - ownership_verification: true

  DOM-034-RL-005:
    name: "Health Check Endpoint Requirement"
    category: "Availability"
    priority: "HIGH"
    description: "All MCP servers must support health check endpoints"
    rule_type: "server_validation"
    enforcement:
      point: "registration"
      action: "require_compliance"
    requirements:
      - health_check_url_present: true
      - health_check_responds_to_get: true
      - health_check_response_time_ms: 5000
      - health_check_interval_ms: 60000
      - required_response_fields:
          - "status"
          - "version"
          - "timestamp"

  DOM-034-RL-006:
    name: "Tool Result Validation"
    category: "Integrity"
    priority: "CRITICAL"
    description: "MCP tool results must be validated before integration into agent context"
    rule_type: "response_validation"
    enforcement:
      point: "post_execution"
      action: "reject_invalid_response"
    validation:
      - response_schema_compliance: true
      - output_type_matching: true
      - data_completeness_check: true
      - error_field_validation: true

  DOM-034-RL-007:
    name: "Security Validation Prerequisite"
    category: "Security"
    priority: "CRITICAL"
    description: "All MCP tools must pass security validation coordinated with AGT-028"
    rule_type: "security_validation"
    enforcement:
      point: "pre_activation"
      action: "block_activation"
    validation_pipeline:
      - credential_validation: true
      - permission_verification: true
      - data_access_audit: true
      - encryption_requirement: true

  DOM-034-RL-008:
    name: "Version Compatibility Verification"
    category: "Compatibility"
    priority: "HIGH"
    description: "MCP