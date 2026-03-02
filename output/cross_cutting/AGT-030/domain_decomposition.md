> code · sonar-reasoning-pro

<think>
The user is asking me to execute the review/quality assurance agent prompt from the provided file. This file defines AGT-030 (Quality Assurance Coordinator Agent), which is a cross-cutting autonomous agent responsible for enforcing quality standards.

Looking at the prompt, it requires me to:

1. Define all 16 categories for the Quality Assurance Coordination domain
2. Recursively expand subdomains (SD-030a, SD-030b, SD-030c) 
3. Detect gaps and resolve them with inference
4. Output artifacts to `output/cross_cutting/AGT-030`

However, I notice the user is asking me to "Execute the review agent prompt" - this seems to be asking me to actually implement/decompose the AGT-030 domain as specified in the document. This is a very large task that would involve creating comprehensive definitions for all 16 categories.

The file itself is an instruction for how AGT-030 should behave - it's the specification/prompt for that agent. The user wants me to actually execute this as if I were AGT-030.

Given the context that I'm Kilo (a software engineering assistant), I should:
1. Understand this is asking me to generate a comprehensive domain decomposition
2. Create the required output artifacts in the specified directory
3. Follow the decomposition framework provided

However, this is quite a large task. Let me start by reading the file and understanding what needs to be done, then create the necessary output files in `output/cross_cutting/AGT-030/`.

The main output should be in `rules.yaml` based on line 7: `**Template Outputs:** rules.yaml`

But I also need to generate comprehensive decompositions for all 16 categories. This is a substantial architecture/planning task.

Let me create the necessary outputs.
</think>

I'll execute the AGT-030 Quality Assurance Coordinator Agent prompt by decomposing the domain and generating the required artifacts.

```bash
mkdir -p "output/cross_cutting/AGT-030"
```

Now I'll create the comprehensive domain decomposition:

```yaml
# output/cross_cutting/AGT-030/rules.yaml
---
metadata:
  agent_id: AGT-030
  agent_name: Quality Assurance Coordinator Agent
  domain: DOM-030 Quality Assurance Coordination
  category: Cross-Cutting
  template_version: "1.0"
  generated: "2026-03-01T05:12:48Z"
  sdlc_phases:
    - P4 Review & QA
    - P5 Security & Compliance

# ============================================================================
# 1. SKILLS
# ============================================================================
skills:
  DOM-030-SK-001:
    name: Quality Gate Definition & Configuration
    description: Define pass/fail criteria for artifact types, establish enforcement levels, configure gate thresholds
    inputs:
      - artifact_type_definition
      - quality_metrics
      - stakeholder_requirements
    outputs:
      - quality_gate_specification
      - enforcement_configuration
    complexity: High

  DOM-030-SK-002:
    name: Automated Quality Score Calculation
    description: Calculate composite quality scores (0-100) by evaluating multiple quality dimensions
    inputs:
      - quality_assessment_data
      - scoring_rubrics
      - artifact_analysis_results
    outputs:
      - quality_score_record
      - score_breakdown_analysis
    complexity: High

  DOM-030-SK-003:
    name: Cross-Agent Quality Audit Execution
    description: Systematically audit outputs from multiple agents for consistency, completeness, and adherence to standards
    inputs:
      - artifact_batch
      - audit_criteria
      - baseline_standards
    outputs:
      - audit_report
      - findings_summary
      - remediation_recommendations
    complexity: High

  DOM-030-SK-004:
    name: Review Standard Enforcement Validation
    description: Verify that review processes comply with defined review standards and escalation policies
    inputs:
      - review_process_log
      - review_standard_definition
      - reviewer_assignment_policy
    outputs:
      - compliance_assessment
      - violation_report
    complexity: Medium

  DOM-030-SK-005:
    name: Quality Regression Detection
    description: Monitor quality metrics over time, identify downward trends, distinguish signal from noise
    inputs:
      - historical_quality_scores
      - time_series_analysis_config
      - threshold_definitions
    outputs:
      - regression_alert
      - trend_analysis_report
    complexity: High

  DOM-030-SK-006:
    name: Code Quality Assessment
    description: Evaluate generated code against KA-030 standards (style, complexity, maintainability, security)
    inputs:
      - source_code
      - code_quality_rules
      - complexity_thresholds
    outputs:
      - code_quality_score
      - violations_list
      - refactoring_recommendations
    complexity: High

  DOM-030-SK-007:
    name: Specification Completeness Validation
    description: Verify specifications are unambiguous, complete, and contain no contradictions
    inputs:
      - specification_document
      - completeness_checklist
      - ambiguity_detection_rules
    outputs:
      - completeness_assessment
      - gap_identification
      - ambiguity_report
    complexity: Medium

  DOM-030-SK-008:
    name: Configuration Correctness Verification
    description: Validate configurations against schema definitions, detect invalid or inconsistent settings
    inputs:
      - configuration_artifact
      - schema_definition
      - consistency_rules
    outputs:
      - verification_result
      - error_report
      - correction_suggestions
    complexity: Medium

  DOM-030-SK-009:
    name: Artifact Type Classifier
    description: Identify artifact type (code, spec, config, documentation) and route to appropriate quality gates
    inputs:
      - artifact_metadata
      - artifact_content_sample
    outputs:
      - artifact_type_classification
      - routing_decision
    complexity: Low

  DOM-030-SK-010:
    name: Quality Threshold Calibration
    description: Calibrate quality gate thresholds based on historical data and organizational objectives
    inputs:
      - historical_quality_data
      - stakeholder_objectives
      - calibration_parameters
    outputs:
      - calibrated_thresholds
      - calibration_report
    complexity: High

  DOM-030-SK-011:
    name: Review Bottleneck Detection
    description: Monitor review queue metrics, identify when reviews are delaying system progress
    inputs:
      - review_queue_metrics
      - throughput_targets
      - sla_definitions
    outputs:
      - bottleneck_alert
      - capacity_analysis
    complexity: Medium

  DOM-030-SK-012:
    name: Quality Bypass Detection
    description: Identify agents or workflows attempting to circumvent quality gates
    inputs:
      - artifact_publication_log
      - quality_gate_audit_log
      - bypass_pattern_definitions
    outputs:
      - bypass_alert
      - pattern_analysis
    complexity: Medium

# ============================================================================
# 2. WORKFLOWS
# ============================================================================
workflows:
  DOM-030-WF-001:
    name: Artifact Quality Review Workflow
    trigger: |
      Artifact submitted for publication OR scheduled review cycle initiated
    steps:
      - step: 1
        name: Artifact Reception & Classification
        action: Receive artifact, classify type, extract metadata
        entry_criteria: Artifact received with metadata
        exit_criteria: Artifact type determined, routing path clear
        
      - step: 2
        name: Quality Gate Selection
        action: Match artifact type to applicable quality gates
        entry_criteria: Artifact classification complete
        exit_criteria: Quality gate set selected
        
      - step: 3
        name: Automated Quality Assessment
        action: Execute automated quality checks (code analysis, spec validation, config verification)
        entry_criteria: Quality gate set selected
        exit_criteria: Automated assessment complete, initial score generated
        
      - step: 4
        name: Human Review Determination
        action: Decide if artifact requires human review based on score tier
        entry_criteria: Automated assessment complete
        exit_criteria: Review requirement determined
        
      - step: 5
        name: Human Review Execution (if needed)
        action: Assign qualified reviewer, conduct structured review, document findings
        entry_criteria: Review required, reviewer available
        exit_criteria: Review complete, reviewer recommendations documented
        
      - step: 6
        name: Quality Score Finalization
        action: Calculate final quality score incorporating automation + human review
        entry_criteria: All assessment inputs complete
        exit_criteria: Final score calculated, score record created
        
      - step: 7
        name: Gate Decision Determination
        action: Apply gate thresholds: <70=Reject, 70-85=Flag, 85+=Approve
        entry_criteria: Final score available
        exit_criteria: Gate decision determined
        
      - step: 8
        name: Decision Communication & Recording
        action: Notify requester of gate decision, record quality score for trend analysis
        entry_criteria: Gate decision determined
        exit_criteria: Decision communicated, recorded in quality database
        
      - step: 9
        name: Remediation Tracking (if rejected)
        action: Create remediation task, track revisions, re-assess when revised
        entry_criteria: Artifact rejected
        exit_criteria: Remediation plan agreed upon
    
    completion_criteria: |
      Artifact either approved for publication OR remediation plan created for rejected artifact,
      AND quality score recorded for trend analysis
    
    rollback_plan: |
      If assessment fails: Re-run automated checks, escalate to quality lead.
      If reviewer unavailable: Escalate to manager for alternate reviewer assignment.
      If gate decision disputed: Log appeal, evaluate with governance committee.

  DOM-030-WF-002:
    name: Quality Gate Enforcement Workflow
    trigger: |
      Artifact submitted for publication encounters quality gate
    steps:
      - step: 1
        name: Gate Configuration Verification
        action: Load quality gate config, verify gate is active and properly configured
        entry_criteria: Gate triggered
        exit_criteria: Gate configuration validated
        
      - step: 2
        name: Assessment Criteria Application
        action: Apply all gate criteria (code style, coverage, complexity, security, etc.)
        entry_criteria: Gate configuration validated
        exit_criteria: All criteria evaluated against artifact
        
      - step: 3
        name: Threshold Evaluation
        action: Compare assessment results against gate thresholds
        entry_criteria: All criteria evaluated
        exit_criteria: Threshold pass/fail determined
        
      - step: 4
        name: Bypass Authority Check
        action: If failing, check if artifact qualifies for documented bypass exception
        entry_criteria: Threshold evaluation complete
        exit_criteria: Bypass eligibility determined
        
      - step: 5
        name: Gate Decision
        action: Pass, Conditional Pass (with flag), or Block
        entry_criteria: Threshold evaluation + bypass check complete
        exit_criteria: Gate decision finalized
        
      - step: 6
        name: Enforcement Action
        action: Allow publication OR block with remediation guidance
        entry_criteria: Gate decision finalized
        exit_criteria: Enforcement action executed
    
    completion_criteria: |
      Gate enforcement decision applied (artifact passed/blocked),
      AND enforcement action recorded in audit log
    
    rollback_plan: |
      If gate malfunction detected: Temporarily disable gate, escalate to gate owner,
      notify impacted artifacts, re-run assessments with corrected gate.

  DOM-030-WF-003:
    name: Quality Regression Investigation Workflow
    trigger: |
      Regression detected (quality score trend declining OR defect escape rate exceeding threshold)
    steps:
      - step: 1
        name: Regression Alert Reception
        action: Receive regression alert, extract affected agent/domain/metric
        entry_criteria: Regression detected and alert generated
        exit_criteria: Alert details parsed
        
      - step: 2
        name: Root Cause Analysis Initiation
        action: Analyze quality trends, identify potential root causes
        entry_criteria: Alert details parsed
        exit_criteria: Root cause hypotheses identified
        
      - step: 3
        name: Data Collection
        action: Gather historical quality data, recent artifacts, recent changes to gates/standards
        entry_criteria: Root cause hypotheses identified
        exit_criteria: Relevant data collected
        
      - step: 4
        name: Root Cause Determination
        action: Investigate hypotheses, determine actual cause (gate miscalibration, agent change, standard drift, metric noise)
        entry_criteria: Relevant data collected
        exit_criteria: Root cause identified
        
      - step: 5
        name: Remediation Planning
        action: Develop corrective action plan (recalibrate gate, train agent, update standard, adjust threshold)
        entry_criteria: Root cause identified
        exit_criteria: Remediation plan documented
        
      - step: 6
        name: Remediation Implementation
        action: Execute corrective actions, monitor for effectiveness
        entry_criteria: Remediation plan approved
        exit_criteria: Corrective actions applied
        
      - step: 7
        name: Verification
        action: Re-assess quality metrics, confirm regression arrested
        entry_criteria: Corrective actions applied
        exit_criteria: Metrics re-evaluated
    
    completion_criteria: |
      Root cause identified AND documented, remediation plan created,
      AND verification shows regression arrested OR escalated to governance
    
    rollback_plan: |
      If remediation causes new problems: Revert changes, reassess root cause, escalate to domain owner.

  DOM-030-WF-004:
    name: Cross-Domain Quality Audit Workflow
    trigger: |
      Scheduled audit interval OR explicit audit request from governance
    steps:
      - step: 1
        name: Audit Scope Definition
        action: Determine which domains/agents to audit, select artifacts to review
        entry_criteria: Audit triggered
        exit_criteria: Audit scope defined, artifact sample selected
        
      - step: 2
        name: Audit Standard Preparation
        action: Consolidate review standards, quality gate definitions applicable to audit scope
        entry_criteria: Audit scope defined
        exit_criteria: Audit standard pack prepared
        
      - step: 3
        name: Artifact Assessment
        action: Evaluate sampled artifacts against audit standards
        entry_criteria: Audit standards prepared
        exit_criteria: All artifacts assessed
        
      - step: 4
        name: Cross-Domain Consistency Check
        action: Verify consistency of quality decisions across agents, identify outliers
        entry_criteria: All artifacts assessed
        exit_criteria: Consistency analysis complete
        
      - step: 5
        name: Finding Compilation
        action: Aggregate findings, identify patterns, categorize by severity
        entry_criteria: Consistency analysis complete
        exit_criteria: Findings documented
        
      - step: 6
        name: Remediation Recommendation
        action: Recommend corrective actions for identified issues
        entry_criteria: Findings documented
        exit_criteria: Recommendations documented
        
      - step: 7
        name: Audit Report Publication
        action: Generate audit report, distribute to domain owners, governance
        entry_criteria: Recommendations documented
        exit_criteria: Audit report published
    
    completion_criteria: |
      Audit report generated AND distributed, remediation recommendations documented,
      domain owners assigned accountability for corrective actions
    
    rollback_plan: |
      If audit reveals systemic issues: Escalate immediately to governance,
      place partial gate restrictions pending root cause analysis.

  DOM-030-WF-005:
    name: Quality Standard Update Workflow
    trigger: |
      New regulation/standard identified OR quality gate needs adjustment OR
      standard lifecycle review triggered
    steps:
      - step: 1
        name: Standard Change Request Reception
        action: Receive change request, document rationale and scope
        entry_criteria: Change request submitted
        exit_criteria: Change request details extracted
        
      - step: 2
        name: Impact Assessment
        action: Analyze impact on gates, workflows, agent outputs
        entry_criteria: Change request details extracted
        exit_criteria: Impact assessment complete
        
      - step: 3
        name: Draft Standard Revision
        action: Develop revised standard incorporating requested changes
        entry_criteria: Impact assessment complete
        exit_criteria: Draft standard created
        
      - step: 4
        name: Stakeholder Review
        action: Obtain review and approval from impacted domain owners and governance
        entry_criteria: Draft standard created
        exit_criteria: Stakeholder feedback incorporated
        
      - step: 5
        name: Standard Finalization
        action: Finalize standard, set effective date, document all changes
        entry_criteria: Stakeholder feedback incorporated
        exit_criteria: Standard finalized
        
      - step: 6
        name: Communication & Training
        action: Notify all affected agents