> code · sonar-reasoning-pro


<think>
The user is asking me to execute a review/analysis agent prompt that is defined in the file `AGT-029_prompt.md`. This is an agent specification for a "Cost Optimization Coordinator Agent" that needs to perform a comprehensive domain decomposition for cost and token optimization across an agentic AI system.

Looking at the file, this is a detailed specification document that outlines:
1. The agent's domain (DOM-029 Cost & Token Optimization)
2. Its system directive and core mission
3. A comprehensive list of 16 categories that need to be fully decomposed:
   - Skills
   - Workflows
   - Task Templates
   - Rules & Constraints
   - Interfaces
   - Dependencies
   - State Models
   - Data Models
   - Control Flows
   - Failure Modes & Recovery
   - Optimization Strategies
   - Coordination Mechanisms
   - Context Requirements
   - Memory Structures
   - Monitoring Requirements
   - Evolution Mechanisms

The agent is supposed to recursively expand three subdomains (SD-029a, SD-029b, SD-029c) and output to `output/cross_cutting/AGT-029`.

This is asking me to execute/perform this role - meaning I need to:
1. Act as the AGT-029 agent
2. Perform the domain decomposition as specified
3. Output the structured results to the specified directory

This appears to be a legitimate software engineering task - building out a domain specification for a cost optimization system in an agentic AI architecture. The search results provided are about AI agents for cost optimization, which are contextually relevant background information.

Let me proceed with executing this task systematically.
</think>

I'll execute the AGT-029 Cost Optimization Coordinator Agent prompt, performing the complete domain decomposition and generating the structured output.
<function_calls>
<invoke name="bash">
<parameter name="command">mkdir -p "c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\cross_cutting\AGT-029"</parameter>
</invoke>
</function_calls>
<function_calls>
<invoke name="writeFile">
<parameter name="filePath">c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\cross_cutting\AGT-029\cost_optimization_rules.yaml</parameter>
<parameter name="content">---
domain_id: DOM-029
domain_name: Cost & Token Optimization
agent_id: AGT-029
agent_name: Cost Optimization Coordinator Agent
version: 1.0
generated: 2026-03-01T05:00:00Z
status: ACTIVE

# ============================================================================
# SECTION 1: SKILLS (DOM-029-SK-*)
# ============================================================================

skills:
  DOM-029-SK-001:
    name: Token Budget Allocation
    description: Distribute system-wide token budget across domain agents based on workload, priority, and historical consumption patterns.
    inputs:
      - total_system_budget_tokens
      - agent_demand_forecast
      - priority_weights
      - historical_consumption_per_agent
    outputs:
      - budget_allocation_per_agent
      - allocation_rationale_report
      - inheritance_hierarchy
    complexity: High
    dependencies: [AGT-019, AGT-007]

  DOM-029-SK-002:
    name: Cheap-First Cascade Enforcement
    description: Enforce sequential model routing from cheapest to most expensive, blocking escalation without ROI justification.
    inputs:
      - operation_request
      - model_cost_matrix
      - quality_requirements
      - budget_available
    outputs:
      - approved_model
      - cascade_rationale
      - escalation_decision
    complexity: High
    dependencies: [AGT-007, AGT-019]

  DOM-029-SK-003:
    name: Per-Agent Cost Attribution
    description: Calculate precise cost per agent per task, including token consumption, model pricing, and caching efficiency gains.
    inputs:
      - task_id
      - agent_id
      - token_consumption
      - model_used
      - cache_hit_indicator
      - external_api_calls
    outputs:
      - cost_attribution_record
      - cost_breakdown_by_component
    complexity: Medium
    dependencies: []

  DOM-029-SK-004:
    name: Semantic Cache Hit-Rate Optimization
    description: Analyze cache patterns, identify high-value repetitive contexts, and recommend cache strategies for maximum token savings.
    inputs:
      - historical_cache_logs
      - query_patterns
      - semantic_similarity_matrix
      - ttl_policies
    outputs:
      - cache_efficiency_report
      - recommended_cache_policies
      - projected_token_savings
    complexity: High
    dependencies: [AGT-012, AGT-002]

  DOM-029-SK-005:
    name: Budget Burn-Rate Forecasting
    description: Project token consumption forward based on current velocity, trending behavior, and anticipated workload changes.
    inputs:
      - current_budget_remaining
      - consumption_velocity_per_agent
      - historical_trend_data
      - upcoming_workload_predictions
      - seasonal_factors
    outputs:
      - burn_rate_forecast
      - exhaustion_eta_per_agent
      - confidence_interval
    complexity: High
    dependencies: [AGT-019]

  DOM-029-SK-006:
    name: Cost Anomaly Detection
    description: Identify unusual cost spikes, inefficient workflows, or potential budget gaming through statistical analysis and behavioral patterns.
    inputs:
      - cost_time_series
      - per_agent_cost_logs
      - baseline_patterns
      - model_routing_decisions
    outputs:
      - anomaly_alerts
      - affected_agents
      - probable_causes
      - recommended_interventions
    complexity: Medium
    dependencies: []

  DOM-029-SK-007:
    name: Model Downgrade Recommendation Generation
    description: Propose cheaper model substitutions for agents exceeding cost targets without quality degradation.
    inputs:
      - agent_current_model
      - agent_quality_requirements
      - available_cheaper_models
      - performance_benchmarks
      - cost_reduction_target
    outputs:
      - model_downgrade_recommendation
      - quality_impact_assessment
      - projected_cost_savings
    complexity: Medium
    dependencies: [AGT-007]

  DOM-029-SK-008:
    name: Cost-Benefit ROI Analysis
    description: Calculate expected value vs. cost for proposed expensive operations to determine if budget exception is justified.
    inputs:
      - operation_description
      - operation_cost
      - expected_outcome_value
      - success_probability
      - strategic_alignment
    outputs:
      - roi_calculation
      - roi_category (High|Medium|Low)
      - recommendation (Allow|Negotiate|Block)
    complexity: High
    dependencies: [AGT-019]

  DOM-029-SK-009:
    name: Dynamic Budget Adjustment
    description: Rebalance budget allocations during runtime based on changing demand, performance metrics, and strategic priorities.
    inputs:
      - current_allocations
      - actual_consumption_per_agent
      - performance_metrics
      - new_constraints
      - priority_changes
    outputs:
      - adjusted_budget_allocations
      - rebalance_rationale
      - affected_agents
    complexity: Medium
    dependencies: [AGT-019]

  DOM-029-SK-010:
    name: Overflow Policy Enforcement
    description: Apply configured overflow handling (wait, queue, escalate, fail gracefully) when agents exceed allocated budget.
    inputs:
      - agent_id
      - current_consumption
      - budget_limit
      - configured_overflow_policy
      - task_priority
    outputs:
      - enforcement_action
      - escalation_notification
      - queue_position
    complexity: Low
    dependencies: []

# ============================================================================
# SECTION 2: WORKFLOWS (DOM-029-WF-*)
# ============================================================================

workflows:
  DOM-029-WF-001:
    name: Budget Allocation & Distribution
    trigger: |
      System startup OR
      Monthly budget cycle OR
      Strategic priority change OR
      New agent onboarding
    steps:
      - step: 1
        name: Collect Agent Demand Signals
        entry_criteria: Trigger activated
        exit_criteria: Demand forecast complete
        action: Gather projected token needs from all agents
      
      - step: 2
        name: Apply Priority Weighting
        entry_criteria: Demand signals collected
        exit_criteria: Priority-weighted scores computed
        action: Weight demands by strategic priority and SLA requirements
      
      - step: 3
        name: Calculate Allocations
        entry_criteria: Priority weights applied
        exit_criteria: Per-agent budget computed
        action: Use DOM-029-SK-001 to distribute total budget
      
      - step: 4
        name: Define Overflow Policies
        entry_criteria: Allocations calculated
        exit_criteria: Overflow policies assigned per agent
        action: Set overflow behavior (queue, escalate, fail)
      
      - step: 5
        name: Publish Budget Directives
        entry_criteria: Allocations & policies finalized
        exit_criteria: All agents notified
        action: Send budget allocation to all agents via DOM-029-IF-001
      
      - step: 6
        name: Initialize Monitoring
        entry_criteria: Budget published
        exit_criteria: Monitoring dashboards active
        action: Activate cost tracking and alert systems
    
    completion_criteria: |
      All agents have assigned budgets AND
      Monitoring is active AND
      All agents have acknowledged budget directive
    
    rollback_plan: |
      If allocation fails:
      - Restore previous budget allocation from backup
      - Notify affected agents of allocation delay
      - Trigger escalation to AGT-019 for manual intervention

  DOM-029-WF-002:
    name: Cost Overrun Detection & Intervention
    trigger: |
      70% budget threshold reached OR
      Cost spike detected OR
      Anomalous consumption pattern observed
    steps:
      - step: 1
        name: Detect Budget Threshold
        entry_criteria: Real-time cost data available
        exit_criteria: Threshold breach identified
        action: Monitor per-agent budget consumption against thresholds (70%, 85%, 95%)
      
      - step: 2
        name: Issue Alert
        entry_criteria: Threshold breach confirmed
        exit_criteria: Alert issued to agent & operations
        action: Send budget warning (DOM-029-DM-003) with recommended actions
      
      - step: 3
        name: Analyze Root Cause
        entry_criteria: Alert issued
        exit_criteria: Probable cause identified
        action: Use DOM-029-SK-006 to detect anomalies (cost spike, inefficiency, gaming)
      
      - step: 4
        name: Calculate ROI Impact
        entry_criteria: Root cause confirmed
        exit_criteria: ROI category determined
        action: Assess remaining operations' ROI using DOM-029-SK-008
      
      - step: 5
        name: Issue Intervention Directive
        entry_criteria: ROI calculated
        exit_criteria: Intervention action assigned
        action: |
          - High ROI (>3x): Allow, log exception, debit reserve
          - Medium ROI (1-3x): Negotiate cheaper alternative
          - Low ROI (<1x): Block operation, force optimization
      
      - step: 6
        name: Monitor Intervention Results
        entry_criteria: Directive issued
        exit_criteria: Agent compliance confirmed
        action: Track whether agent reduces consumption or escalates
    
    completion_criteria: |
      Budget brought below threshold OR
      Exception approved by AGT-019 OR
      Operation blocked
    
    rollback_plan: |
      If intervention causes operational failure:
      - Restore operation to previous model/approach
      - Grant temporary budget exception
      - Schedule post-incident review

  DOM-029-WF-003:
    name: Cheap-First Routing Verification
    trigger: |
      Model routing decision requested OR
      Hourly compliance audit
    steps:
      - step: 1
        name: Receive Routing Request
        entry_criteria: AGT-007 requests model selection guidance
        exit_criteria: Request queued for evaluation
        action: Accept operation context, task requirements, quality thresholds
      
      - step: 2
        name: Validate Cheap-First Precedence
        entry_criteria: Request received
        exit_criteria: Cheapest model identified
        action: Use DOM-029-SK-002 to verify cheapest model is attempted first
      
      - step: 3
        name: Assess Quality Compatibility
        entry_criteria: Cheap model identified
        exit_criteria: Quality fit determined
        action: Compare cheap model capabilities against task quality requirements
      
      - step: 4
        name: Escalation Decision
        entry_criteria: Quality assessment complete
        exit_criteria: Escalation approved or denied
        action: |
          - Cheap model sufficient: Approve, return to AGT-007
          - Cheap model insufficient: Check budget for escalation
            - Budget available: Approve escalation, recommend medium-cost model
            - Budget scarce: Reject escalation, suggest task redesign
      
      - step: 5
        name: Log Routing Audit Trail
        entry_criteria: Routing decision made
        exit_criteria: Decision recorded
        action: Store routing decision with model selected, quality assessed, cost approved
    
    completion_criteria: Routing decision returned to AGT-007
    rollback_plan: Use previous routing decision if validation fails

  DOM-029-WF-004:
    name: Cache Efficiency Optimization
    trigger: |
      Weekly cache analysis scheduled OR
      Cache hit rate drops below 30% OR
      New semantic pattern detected
    steps:
      - step: 1
        name: Collect Cache Metrics
        entry_criteria: Trigger activated
        exit_criteria: Cache logs aggregated
        action: Gather cache access patterns from DOM-012 and prompt storage
      
      - step: 2
        name: Analyze Hit Patterns
        entry_criteria: Cache logs available
        exit_criteria: High-value repetitive patterns identified
        action: Use DOM-029-SK-004 to find semantically similar queries
      
      - step: 3
        name: Recommend Cache Policies
        entry_criteria: Patterns analyzed
        exit_criteria: Policy recommendations generated
        action: |
          - Increase TTL for high-hit patterns
          - Enable semantic compression for verbose contexts
          - Add new cache keys for missed patterns
      
      - step: 4
        name: Calculate Token Savings
        entry_criteria: Policies recommended
        exit_criteria: Savings projection complete
        action: Estimate tokens saved by implementing recommendations
      
      - step: 5
        name: Deploy Policy Changes
        entry_criteria: Savings validated
        exit_criteria: New policies active
        action: Push cache policies to DOM-011 and DOM-012
      
      - step: 6
        name: Validate Results
        entry_criteria: Policies deployed
        exit_criteria: Hit rate improvement confirmed
        action: Monitor cache metrics over next 7 days
    
    completion_criteria: New cache policies active and improvement validated
    rollback_plan: Revert to previous cache policies if hit rate declines

  DOM-029-WF-005:
    name: Cost Reporting & Analysis
    trigger: |
      Daily cost summary requested OR
      Weekly cost review scheduled OR
      Monthly financial close
    steps:
      - step: 1
        name: Aggregate Cost Data
        entry_criteria: Reporting period defined
        exit_criteria: All cost records collected
        action: Retrieve cost attribution records from all agents and tasks
      
      - step: 2
        name: Calculate Summary Metrics
        entry_criteria: Cost data aggregated
        exit_criteria: KPIs computed
        action: |
          - Total cost vs. budget
          - Per-agent cost attribution
          - Per-task cost
          - Cache hit rate impact
          - Model routing efficiency
      
      - step: 3
        name: Identify Trends
        entry_criteria: Metrics calculated
        exit_criteria: Trends documented
        action: Compare to historical periods, identify cost drivers and savings
      
      - step: 4
        name: Generate Report
        entry_criteria: Trends identified
        exit_criteria: Report formatted
        action: Create cost report with visualizations and recommendations
      
      - step: 5
        name: Distribute Report
        entry_criteria: Report generated
        exit_criteria: Recipients notified
        action: Publish to finance team, engineering leadership, and agents
    
    completion_criteria: Report distributed and acknowledged
    rollback_plan: Resend report if distribution fails

# ============================================================================
# SECTION 3