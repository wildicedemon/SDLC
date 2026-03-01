> code · sonar-reasoning-pro<think>
The user wants me to execute a review/analysis of the AGT-036 agent prompt file they just provided. This is an Error Recovery Coordinator Agent specification document that defines error recovery patterns, circuit breakers, graceful degradation, and retry strategies for a multi-agent AI system.

The user is asking me to execute/review this prompt and output results to `output/cross_cutting/AGT-036`. This appears to be a structured SDLC (Software Development Lifecycle) document for an agentic AI system.

Let me think about what "execute the review agent prompt" means in this context:
1. Review the prompt specification for completeness and coherence
2. Generate the output artifacts it specifies
3. Potentially analyze the architecture and provide deliverables

Looking at the file, AGT-036 is meant to produce:
- `rules.yaml` (error_recovery_rules.yaml) 
- `techniques_strategies.yaml`
- Full decomposition of 16 categories with IDs
- Circuit breaker definitions
- Graceful degradation policies
- Retry strategies
- Fallback routing

The prompt is essentially a specification for what AGT-036 should do. So "executing" it means I should analyze this and generate the expected outputs.

However, I need to be careful here. The user is asking me to "execute the review agent prompt" - this could mean:
1. Review the prompt itself for quality/completeness
2. Act AS AGT-036 and generate the outputs the prompt describes

Given the context and the output path specified, I think the user wants me to act as AGT-036 and generate the decomposed domain structure and outputs.

Let me start by:
1. Creating the output directory structure
2. Generating the required YAML files and decompositions
3. Populating all 16 categories as specified in the prompt
</think>

I'll execute AGT-036 by generating the complete domain decomposition and output artifacts for the Error Recovery Coordinator Agent.
<function_calls>
<invoke_tool>
<parameter name="tool">bash</parameter>
<parameter name="command">mkdir -p "c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\cross_cutting\AGT-036"</parameter>
</invoke_tool>
</function_calls>
<parameter name="tool">bash</parameter>
<parameter name="command">cd "c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\cross_cutting\AGT-036" && pwd</parameter>
</invoke_tool>
</function_calls>

Now generating the complete domain decomposition and artifacts:
<function_calls>
<invoke name="bash">
<parameter name="command">cat > "c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\cross_cutting\AGT-036\error_recovery_rules.yaml" << 'EOF'
agent_id: AGT-036
domain_id: DOM-036
domain_name: Error Recovery Coordination
cross_cutting_scope: 
  - DOM-002
  - DOM-004
  - DOM-024
  - DOM-026
  - DOM-005
  - DOM-031
  - DOM-006

################################################################################
# 1. SKILLS (DOM-036-SK-NNN)
################################################################################
skills:
  - skill_id: DOM-036-SK-001
    name: Circuit Breaker Configuration & Deployment
    description: Design and deploy circuit breaker patterns for agent-to-agent communication
    knowledge_atoms: [KA-017]
    produces: [DOM-036-IF-001]
    
  - skill_id: DOM-036-SK-002
    name: Exponential Backoff & Jitter Calculation
    description: Calculate and configure exponential backoff with jitter for retry policies
    knowledge_atoms: [KA-041]
    parameters: [base_delay_ms, max_delay_ms, backoff_multiplier, jitter_range]
    
  - skill_id: DOM-036-SK-003
    name: Graceful Degradation Mode Design
    description: Design degraded operation modes and partial result handling
    knowledge_atoms: []
    
  - skill_id: DOM-036-SK-004
    name: Failure Cascade Analysis
    description: Analyze failure propagation paths and containment boundaries
    knowledge_atoms: [KA-041]
    
  - skill_id: DOM-036-SK-005
    name: Zero-Shot Recovery Chain Construction
    description: Build recovery chains without requiring training data
    knowledge_atoms: []
    
  - skill_id: DOM-036-SK-006
    name: Idempotency Requirement Identification
    description: Identify which operations must be idempotent for safe recovery
    knowledge_atoms: []
    
  - skill_id: DOM-036-SK-007
    name: Dead-Letter Queue Management
    description: Design and manage dead-letter queues for failed tasks
    knowledge_atoms: [KA-041]
    
  - skill_id: DOM-036-SK-008
    name: Cross-Agent Failure Containment
    description: Prevent failure propagation across agent boundaries
    knowledge_atoms: [KA-041]
    
  - skill_id: DOM-036-SK-009
    name: Recovery Plan Validation
    description: Validate recovery plans for completeness and consistency
    knowledge_atoms: []

################################################################################
# 2. WORKFLOWS (DOM-036-WF-NNN)
################################################################################
workflows:
  - workflow_id: DOM-036-WF-001
    name: Agent Failure Detection & Recovery
    description: Detect agent failure and execute recovery strategy
    stages:
      - stage: DETECT
        action: Monitor agent health metrics, detect failure signal
        timeout_ms: 5000
      - stage: CLASSIFY
        action: Classify failure type (transient, permanent, cascading)
        timeout_ms: 2000
      - stage: ISOLATE
        action: Activate circuit breaker, prevent further calls
        timeout_ms: 1000
      - stage: RECOVER
        action: Execute recovery strategy based on failure type
        timeout_ms: 30000
      - stage: VALIDATE
        action: Validate agent is healthy before resuming normal load
        timeout_ms: 5000
    escalation_path: DOM-031

  - workflow_id: DOM-036-WF-002
    name: Circuit Breaker Trip & Recovery
    description: Manage circuit breaker state transitions
    states: [CLOSED, OPEN, HALF_OPEN, FAILED]
    transitions:
      CLOSED_to_OPEN: "failure_threshold_exceeded"
      OPEN_to_HALF_OPEN: "recovery_timeout_elapsed"
      HALF_OPEN_to_CLOSED: "test_call_succeeded"
      HALF_OPEN_to_OPEN: "test_call_failed"
      
  - workflow_id: DOM-036-WF-003
    name: Cascade Failure Containment
    description: Detect and contain cascading failures across agent networks
    stages:
      - stage: DETECT_CASCADE
        action: Monitor for dependent failures
        metric: failure_correlation > 0.8
      - stage: TRACE_PATH
        action: Trace failure propagation path
      - stage: ACTIVATE_BOUNDARIES
        action: Activate failure isolation boundaries
      - stage: REPORT_CASCADE
        action: Generate cascade report for DOM-026 (Debugging)

  - workflow_id: DOM-036-WF-004
    name: System-Wide Recovery Mode Activation
    description: Activate reduced-load recovery mode across system
    authorization: AGT-036 override authority
    steps:
      - Pause non-essential agents
      - Enable graceful degradation on critical agents
      - Increase monitoring frequency
      - Activate recovery coordination across all domains
      - Report status to DOM-031

  - workflow_id: DOM-036-WF-005
    name: Recovery Plan Audit
    description: Audit all agents for adequate recovery coverage
    frequency: "per_phase_completion"
    checks:
      - All agents have defined recovery plans
      - All failure modes have strategies
      - All agent connections have circuit breakers
      - Retry policies have finite limits
      - Degradation modes are defined
      
  - workflow_id: DOM-036-WF-006
    name: Post-Failure Root Cause → Recovery Improvement
    description: Feed debugging results into recovery strategy enhancement
    inputs: [DOM-026-debug-reports]
    outputs: [DOM-036-updated-recovery-plans]
    coordination: DOM-026 (Debugging)

################################################################################
# 3. RULES & CONSTRAINTS (DOM-036-RL-NNN)
################################################################################
rules:
  - rule_id: DOM-036-RL-001
    name: Circuit Breaker Mandate
    statement: All agent-to-agent calls MUST implement circuit breaker patterns
    severity: CRITICAL
    enforced_by: [AGT-036]
    knowledge_atom: KA-017
    
  - rule_id: DOM-036-RL-002
    name: Exponential Backoff Requirement
    statement: Retry policies MUST include exponential backoff with jitter
    severity: CRITICAL
    formula: "delay = min(base_delay * (multiplier ^ attempt) + random(0, jitter), max_delay)"
    
  - rule_id: DOM-036-RL-003
    name: Finite Retry Limit
    statement: Maximum retry count MUST be finite (no unlimited retries)
    severity: CRITICAL
    knowledge_atom: KA-017
    constraint: "max_retries >= 1 AND max_retries <= 10"
    
  - rule_id: DOM-036-RL-004
    name: Degraded Operation Mode
    statement: All agents MUST define at least one degraded operation mode
    severity: HIGH
    
  - rule_id: DOM-036-RL-005
    name: Task Dependency Isolation
    statement: Task dependency failures MUST NOT cascade to independent tasks
    severity: CRITICAL
    knowledge_atom: KA-041
    
  - rule_id: DOM-036-RL-006
    name: Recovery Operation Idempotence
    statement: All recovery operations MUST be idempotent
    severity: CRITICAL
    
  - rule_id: DOM-036-RL-007
    name: Failure Boundary Isolation
    statement: Failure isolation boundaries MUST be defined for all agent clusters
    severity: HIGH
    
  - rule_id: DOM-036-RL-008
    name: Recovery Validation
    statement: Recovered agents MUST pass health validation before resuming full load
    severity: CRITICAL
    
  - rule_id: DOM-036-RL-009
    name: Escalation Threshold Definition
    statement: All agents MUST define escalation thresholds for human intervention
    severity: HIGH
    coordination: DOM-031
    
  - rule_id: DOM-036-RL-010
    name: Cascading Failure Prevention
    statement: All multi-agent interactions MUST have failure cascade prevention mechanisms
    severity: CRITICAL

################################################################################
# 4. STATE MODELS (DOM-036-SM-NNN)
################################################################################
state_models:
  - state_model_id: DOM-036-SM-001
    name: Circuit Breaker State Model
    states:
      CLOSED:
        description: Normal operation, forwarding calls
        transitions: {failure_threshold_exceeded: OPEN}
      OPEN:
        description: Failing fast, blocking calls
        transitions: {recovery_timeout_elapsed: HALF_OPEN}
      HALF_OPEN:
        description: Testing recovery with limited traffic
        transitions: {test_succeeded: CLOSED, test_failed: OPEN}
    initial_state: CLOSED
    
  - state_model_id: DOM-036-SM-002
    name: Agent Recovery State Model
    states:
      HEALTHY:
        description: Normal operation
        transitions: {failure_detected: FAILURE_DETECTED}
      FAILURE_DETECTED:
        description: Failure signal received
        transitions: {recovery_initiated: RECOVERY_INITIATED}
      RECOVERY_INITIATED:
        description: Recovery process started
        transitions: {recovery_executing: RECOVERING}
      RECOVERING:
        description: Recovery in progress
        transitions: 
          health_restored: RECOVERED
          degradation_activated: DEGRADED
          escalation_triggered: ESCALATED
      RECOVERED:
        description: Agent recovered to full capacity
        transitions: {failure_detected: FAILURE_DETECTED}
      DEGRADED:
        description: Agent operating in reduced-capacity mode
        transitions: {recovery_completed: RECOVERED}
      ESCALATED:
        description: Issue escalated to human intervention
        transitions: {human_resolved: RECOVERED}
        
  - state_model_id: DOM-036-SM-003
    name: System Recovery Mode State Model
    states:
      NORMAL:
        description: System operating normally
        transitions: {cascade_detected: DEGRADED}
      DEGRADED:
        description: Some agents failing but system functional
        transitions: 
          recovery_mode_activated: RECOVERY_MODE
          cascade_contained: NORMAL
      RECOVERY_MODE:
        description: System in reduced-load recovery mode
        transitions: {recovery_complete: NORMAL}

################################################################################
# 5. DATA MODELS (DOM-036-DM-NNN)
################################################################################
data_models:
  - data_model_id: DOM-036-DM-001
    name: Circuit Breaker Configuration Schema
    fields:
      - breaker_id: string (identifier)
      - source_agent: string (agent_id)
      - target_agent: string (agent_id)
      - failure_threshold: integer (0-100, percentage)
      - failure_window_ms: integer (milliseconds to evaluate threshold)
      - recovery_timeout_ms: integer (time before OPEN→HALF_OPEN transition)
      - half_open_max_attempts: integer (test calls in HALF_OPEN state)
      - last_failure_time: timestamp
      - state: enum [CLOSED, OPEN, HALF_OPEN]
    
  - data_model_id: DOM-036-DM-002
    name: Retry Policy Schema
    fields:
      - policy_id: string
      - max_retries: integer (1-10)
      - base_delay_ms: integer (minimum delay)
      - max_delay_ms: integer (maximum delay)
      - backoff_multiplier: float (1.0-10.0)
      - jitter_range: float (0.0-1.0, percentage of delay)
      - idempotency_required: boolean
      - dead_letter_queue: string (optional queue identifier)
    
  - data_model_id: DOM-036-DM-003
    name: Recovery Plan Schema
    fields:
      - agent_id: string
      - failure_modes: array[string] (identifiers)
      - recovery_strategies: array[object]
        - failure_mode: string
        - strategy_type: enum [RETRY, DEGRADE, CIRCUIT_BREAK, ESCALATE]
        - configuration: object
      - degraded_modes: array[object]
        - mode_id: string
        - description: string
        - capabilities_available: array[string]
        - resource_reduction: float (0.0-1.0)
      - escalation_threshold: integer (retry attempt count before escalation)
      - last_validated: timestamp
      - validation_status: enum [VALID, NEEDS_UPDATE, INVALID]
    
  - data_model_id: DOM-036-DM-004
    name: Failure Cascade Record Schema
    fields:
      - cascade_id: string (unique identifier)
      - root_failure_agent: string (agent_id)
      - root_failure_time: timestamp
      - propagation_path: array[object]
        - agent_id: string
        - failure_time: timestamp
        - failure_reason: string
      - containment_boundary: string (agent_id where cascade stopped)
      - contained_by_rule: string (rule_id that prevented further propagation)
      - recovery_duration_ms: integer
      - resolution: enum [RECOVERED, DEGRADED, ESCALATED]
      - root_cause: string (output from DOM-026)
    
  - data_model_id: DOM-036-DM-005
    name: Recovery Coordination Event Schema
    fields:
      - event_id: string
      - event_type: enum [FAILURE_DETECTED, RECOVERY_INITIATED, RECOVERY_COMPLETED, ESCALATED, DEGRADATION_ACTIVATED]
      - timestamp: timestamp
      -