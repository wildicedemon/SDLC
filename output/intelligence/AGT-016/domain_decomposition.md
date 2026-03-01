> code · sonar-reasoning-pro<think>
The user is asking me to execute the architect agent prompt from the file AGT-016_prompt.md. This file contains detailed specifications for a "Specification Agent (AGT-016)" that is supposed to decompose the "Specification & Design Intelligence" domain within an agentic AI coding system architecture.

Looking at the instructions:
1. I need to act as this Specification Agent
2. I need to fully decompose the domain into 16 categories
3. I need to recursively expand subdomains
4. I need to output to "output/intelligence/AGT-016"

This is a task to execute a complex decomposition prompt. I should follow the directive and produce comprehensive outputs for all 16 categories specified in the prompt.

However, I need to check if this is the right approach. The user is asking me to "execute the architect agent prompt" - meaning I should follow the system directive and produce the decomposition as specified.

Let me start by understanding what needs to be produced:
1. Skills (DOM-016-SK-[NNN])
2. Workflows (DOM-016-WF-[NNN])
3. Task Templates (DOM-016-TT-[NNN])
4. Rules & Constraints (DOM-016-RL-[NNN])
5. Interfaces (DOM-016-IF-[NNN])
6. Dependencies (DOM-016-DP-[NNN])
7. State Models (DOM-016-SM-[NNN])
8. Data Models (DOM-016-DM-[NNN])
9. Control Flows (DOM-016-CF-[NNN])
10. Failure Modes & Recovery (DOM-016-FM-[NNN])
11. Optimization Strategies (DOM-016-OPT-[NNN])
12. Coordination Mechanisms (DOM-016-CM-[NNN])
13. Context Requirements (DOM-016-CTX-[NNN])
14. Memory Structures (DOM-016-MEM-[NNN])


15. Monitoring Requirements (DOM-016-MON-[NNN])
16. Evolution Mechanisms (DOM-016-EV-[NNN])

I also need to recursively expand four subdomains: Spec Generation, Design Synthesis, Requirement Extraction, and Spec Validation. This is substantial work requiring structured YAML output files organized in the "output/intelligence/AGT-016" directory, likely with separate files for each category and subdomain expansion.
</think>

I'll execute the Specification Agent (AGT-016) decomposition as specified in the prompt. This requires comprehensive domain decomposition across 16 categories with recursive expansion of subdomains.

```bash
mkdir -p "output/intelligence/AGT-016"
```

Now I'll generate the complete decomposition:

```bash
cat > "output/intelligence/AGT-016/domain_decomposition.yaml" << 'EOF'
domain_id: DOM-016
domain_name: Specification & Design Intelligence
version: 1.0
generated_date: 2026-03-01
agent_id: AGT-016
phase: P2 (Planning)
execution_phase: Phase 3 (Intelligence)

subdomains:
  - id: SD-016a
    name: Spec Generation
    description: Automated specification generation from user requirements, intent decomposition into formal specifications
  - id: SD-016b
    name: Design Synthesis
    description: Design document creation from specifications, architectural design generation
  - id: SD-016c
    name: Requirement Extraction
    description: Natural language requirement parsing, ambiguity detection, requirement classification
  - id: SD-016d
    name: Spec Validation
    description: Specification completeness checking, consistency validation, feasibility analysis

---
## 1. SKILLS (DOM-016-SK-[NNN])

skills:
  - id: DOM-016-SK-001
    name: Automated Specification Generation
    description: Transforms user intent and requirements into formal, structured specifications consumable by code generation agents
    inputs: [user_intent, requirements_list, context_constraints, existing_specs]
    outputs: [specification_document, spec_metadata, generation_reasoning]
    complexity: High
    subdomain: SD-016a

  - id: DOM-016-SK-002
    name: Requirement Extraction from Natural Language
    description: Parses natural language inputs (user stories, transcripts, documentation) and extracts structured requirements
    inputs: [text_input, requirement_template, domain_context]
    outputs: [structured_requirements, entity_map, ambiguity_flags]
    complexity: High
    subdomain: SD-016c

  - id: DOM-016-SK-003
    name: Ambiguity Detection and Classification
    description: Identifies ambiguous, vague, or conflicting statements in requirements and classifies ambiguity type
    inputs: [requirement_text, domain_ontology, historical_ambiguities]
    outputs: [ambiguity_score, ambiguity_type, clarification_suggestions]
    complexity: Medium
    subdomain: SD-016c

  - id: DOM-016-SK-004
    name: Structured Clarification Prompt Generation
    description: Generates targeted clarification questions to resolve identified ambiguities in requirements
    inputs: [ambiguous_requirement, ambiguity_context, stakeholder_profile]
    outputs: [clarification_questions, question_priority, expected_response_format]
    complexity: Medium
    subdomain: SD-016c

  - id: DOM-016-SK-005
    name: Multi-Level Specification Decomposition
    description: Decomposes system-level specifications into component and function-level specifications maintaining traceability
    inputs: [system_specification, decomposition_rules, target_granularity]
    outputs: [component_specs, function_specs, decomposition_tree, traceability_map]
    complexity: High
    subdomain: SD-016a

  - id: DOM-016-SK-006
    name: Design Document Synthesis
    description: Generates comprehensive design documents from formal specifications including architecture, components, interactions
    inputs: [specification, design_patterns, architectural_constraints, existing_designs]
    outputs: [design_document, architecture_diagram, component_interactions, design_rationale]
    complexity: High
    subdomain: SD-016b

  - id: DOM-016-SK-007
    name: Specification Completeness Validation
    description: Verifies that specifications contain all required elements and satisfy completeness criteria
    inputs: [specification, completeness_checklist, requirement_types]
    outputs: [completeness_score, missing_elements, remediation_suggestions]
    complexity: Medium
    subdomain: SD-016d

  - id: DOM-016-SK-008
    name: Specification Consistency Validation
    description: Detects contradictions, conflicts, and inconsistencies within and across specifications
    inputs: [specification_set, constraint_rules, consistency_rules]
    outputs: [consistency_report, conflict_list, resolution_recommendations]
    complexity: Medium
    subdomain: SD-016d

  - id: DOM-016-SK-009
    name: Feasibility Analysis
    description: Evaluates whether specifications are technically feasible given constraints and dependencies
    inputs: [specification, technical_constraints, resource_availability, timeline]
    outputs: [feasibility_score, risk_assessment, feasibility_concerns, mitigation_strategies]
    complexity: Medium
    subdomain: SD-016d

  - id: DOM-016-SK-010
    name: Specification-to-Implementation Traceability Mapping
    description: Creates and maintains bidirectional traceability between specifications and implementation artifacts
    inputs: [specification, implementation_code, test_cases, deployment_config]
    outputs: [traceability_matrix, coverage_report, orphaned_specs, unused_code]
    complexity: Medium
    subdomain: SD-016d

  - id: DOM-016-SK-011
    name: Requirement Classification
    description: Categorizes requirements as functional, non-functional, constraints, assumptions, or dependencies
    inputs: [requirement_text, classification_ontology, domain_context]
    outputs: [classified_requirement, confidence_score, classification_reasoning]
    complexity: Low
    subdomain: SD-016c

  - id: DOM-016-SK-012
    name: Design Alternative Analysis
    description: Evaluates multiple design approaches against specifications and trade-offs
    inputs: [specification, design_alternatives, evaluation_criteria, constraints]
    outputs: [evaluation_matrix, recommendation, trade-off_analysis, decision_rationale]
    complexity: High
    subdomain: SD-016b

  - id: DOM-016-SK-013
    name: Specification Template Management
    description: Maintains, retrieves, and applies specification templates for different specification types
    inputs: [spec_type, context, customization_parameters]
    outputs: [template_instance, template_guidance, required_sections]
    complexity: Low
    subdomain: SD-016a

  - id: DOM-016-SK-014
    name: Specification Versioning and Change Tracking
    description: Manages specification versions, tracks changes, and maintains change history with impact analysis
    inputs: [specification, change_description, impact_scope]
    outputs: [new_version, change_log, impact_assessment, downstream_dependencies]
    complexity: Medium
    subdomain: SD-016a

  - id: DOM-016-SK-015
    name: Acceptance Criteria Derivation
    description: Generates measurable acceptance criteria from requirements and specifications
    inputs: [requirement, specification_context, acceptance_template]
    outputs: [acceptance_criteria, measurement_approach, validation_method]
    complexity: Medium
    subdomain: SD-016d

---
## 2. WORKFLOWS (DOM-016-WF-[NNN])

workflows:
  - id: DOM-016-WF-001
    name: User Intent to Specification
    subdomain: SD-016a
    trigger: New user requirement received or feature request initiated
    steps:
      - step: 1
        action: Parse user intent
        entry_criteria: Raw user input available
        exit_criteria: Intent understood, scope boundaries identified
        agent: DOM-016-SK-002
      
      - step: 2
        action: Extract structured requirements
        entry_criteria: Intent parsed
        exit_criteria: Requirements list with classification
        agent: DOM-016-SK-002, DOM-016-SK-011
      
      - step: 3
        action: Detect ambiguities
        entry_criteria: Requirements extracted
        exit_criteria: Ambiguity map with severity scores
        agent: DOM-016-SK-003
      
      - step: 4
        action: Generate clarification questions
        entry_criteria: Ambiguities detected
        exit_criteria: Prioritized clarification questions
        agent: DOM-016-SK-004
        conditional: ambiguity_detected = true
      
      - step: 5
        action: Collect stakeholder feedback
        entry_criteria: Clarification questions generated
        exit_criteria: Feedback incorporated, ambiguities resolved
        agent: DOM-023 (HITL)
        conditional: clarification_needed = true
      
      - step: 6
        action: Formalize specification
        entry_criteria: Requirements clarified
        exit_criteria: Formal specification document
        agent: DOM-016-SK-001, DOM-016-SK-005
      
      - step: 7
        action: Validate specification
        entry_criteria: Specification formalized
        exit_criteria: Validation report with completeness/consistency score
        agent: DOM-016-SK-007, DOM-016-SK-008
      
      - step: 8
        action: Iterate on gaps
        entry_criteria: Validation complete
        exit_criteria: All gaps resolved or documented as known limitations
        agent: DOM-016-SK-001
        loop_condition: validation_score < 0.95 or gaps_remain = true
    
    completion_criteria: 
      - Specification has completeness score >= 0.95
      - No critical ambiguities remain
      - Specification is approved by stakeholder
      - Traceability established to original intent
    
    rollback_plan: |
      If critical ambiguity unresolved after 3 clarification rounds:
      - Flag specification for expert review
      - Mark scope as reduced (descope ambiguous features)
      - Document assumptions and proceed with approved subset
      - Schedule follow-up session with domain expert

  - id: DOM-016-WF-002
    name: Design Document Generation
    subdomain: SD-016b
    trigger: Specification approved and ready for detailed design
    steps:
      - step: 1
        action: Generate design outline
        entry_criteria: Specification available and validated
        exit_criteria: Design outline with sections and components identified
        agent: DOM-016-SK-006
      
      - step: 2
        action: Synthesize architecture design
        entry_criteria: Design outline complete
        exit_criteria: Architecture diagram and design rationale
        agent: DOM-016-SK-006
      
      - step: 3
        action: Define component interactions
        entry_criteria: Architecture defined
        exit_criteria: Component interaction matrix and sequence diagrams
        agent: DOM-016-SK-006
      
      - step: 4
        action: Analyze design alternatives
        entry_criteria: Initial design complete
        exit_criteria: Alternative designs evaluated with trade-offs
        agent: DOM-016-SK-012
      
      - step: 5
        action: Review and approve design
        entry_criteria: Design complete with alternatives analyzed
        exit_criteria: Design approved, decisions documented
        agent: DOM-023 (HITL)
      
      - step: 6
        action: Generate design templates for implementation
        entry_criteria: Design approved
        exit_criteria: Implementation guides and code generation seeds
        agent: DOM-016-SK-006
    
    completion_criteria:
      - Design document complete and approved
      - All components mapped to specification requirements
      - Trade-off decisions documented
      - Ready for code generation phase

  - id: DOM-016-WF-003
    name: Requirement Ambiguity Resolution
    subdomain: SD-016c
    trigger: Ambiguity detected in requirements with score > threshold
    steps:
      - step: 1
        action: Classify ambiguity type
        entry_criteria: Ambiguous requirement identified
        exit_criteria: Ambiguity type classified and contextualized
        agent: DOM-016-SK-003
      
      - step: 2
        action: Generate targeted clarification questions
        entry_criteria: Ambiguity classified
        exit_criteria: Prioritized clarification questions with response templates
        agent: DOM-016-SK-004
      
      - step: 3
        action: Submit for stakeholder clarification
        entry_criteria: Questions generated
        exit_criteria: Stakeholder response received
        agent: DOM-023 (HITL)
      
      - step: 4
        action: Incorporate feedback
        entry_criteria: Stakeholder response received
        exit_criteria: Requirement re-specified with ambiguity resolved
        agent: DOM-016-SK-001
      
      - step: 5
        action: Validate resolution
        entry_criteria: Requirement updated
        exit_criteria: New ambiguity score calculated
        agent: DOM-016-SK-003
        loop_condition: ambiguity_score > threshold and attempts < max_attempts
      
      - step: 6
        action: Document assumptions
        entry_criteria: Ambiguity partially resolved or max attempts reached
        exit_criteria: Assumptions documented and flagged
        conditional: ambiguity_unresolved = true
    
    completion_criteria:
      - Ambiguity score falls below acceptable threshold OR
      - Maximum clarification attempts reached and assumptions documented
      - Decision recorded in traceability matrix

  - id: DOM-016-WF-004
    name: Specification Validation and Approval
    subdomain: SD-016d
    trigger: Specification ready for validation before approval
    steps:
      - step: 1
        action: Check completeness
        entry_criteria: Specification available
        exit_criteria: Completeness report with missing elements
        agent: DOM-016-SK-007
      
      - step: 2
        action: Check consistency
        entry_criteria: Completeness check complete
        exit_criteria: Consistency report with conflicts identified
        agent: DOM-016-SK-008
      
      - step: 3
        action: Perform feasibility analysis
        entry_criteria: Consistency check complete
        exit_criteria: Feasibility assessment with risks identified
        agent: DOM-016-SK-009
      
      - step: 4
        action: Reme