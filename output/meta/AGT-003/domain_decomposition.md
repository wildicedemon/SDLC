> code · sonar-reasoning-pro<think>
This is a very complex request. The user is asking me to "execute the research agent prompt" from a file that describes AGT-003: Research & Benchmarking Agent. This is a detailed system architecture document that defines how a specialized agent should decompose the "Research & Benchmarking Framework" domain.

However, I'm confused about what the actual task is. The document asks for the agent to:
1. Fully decompose the domain into 16 categories (Skills, Workflows, Task Templates, Rules & Constraints, Interfaces, Dependencies, State Models, Data Models, Control Flows, Failure Modes & Recovery, Optimization Strategies, Coordination Mechanisms, Context Requirements, Memory Structures, Monitoring Requirements, Evolution Mechanisms)
2. Recursively expand 3 subdomains (SD-003a, SD-003b, SD-003c)
3. Create output artifacts like `benchmarking_framework.yaml`, validation reports, evidence assessment protocols, research methodology docs

The user wants me to output to `output/meta/AGT-003`.

But I need to be careful here. The instructions say:
- I'm supposed to be a software engineer helping with coding tasks
- The search results provided are about cybersecurity benchmarking
- The prompt.md file is about an agentic AI system architecture

This seems like the user wants me to generate a complete decomposition of the Research & Benchmarking Framework domain according to the specifications in the prompt file. This is a massive task that would require generating extensive structured documentation.

Given the token budget and the instruction to be concise, I should clarify what they actually want me to do. However, re-reading the instructions, I'm told "Do not ask for more information than necessary. Use the tools provided to accomplish the user's request efficiently and effectively."

The prompt is clear - execute the agent prompt and output to output/meta/AGT-003. I should:
1. Create the necessary directory structure
2. Generate the complete decomposition following the 16-category framework specified


3. Produce the required output artifacts including benchmarking_framework.yaml and supporting documentation

I'll need to set up the directory structure first, then systematically generate the decomposition files and supporting materials as outlined in the specification.
</think>

I'll execute the AGT-003 Research & Benchmarking Agent prompt, decomposing the domain across all 16 categories and generating the output artifacts.
<function_calls>
<invoke name="bash">
<parameter name="command">mkdir -p "c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\meta\AGT-003"</parameter>
</invoke>
</function_calls>
<invoke name="writeFile">
<parameter name="filePath">c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\meta\AGT-003\benchmarking_framework.yaml</parameter>
<parameter name="contents">domain_id: DOM-003
domain_name: Research & Benchmarking Framework
agent_id: AGT-003
agent_name: Research & Benchmarking Agent
version: 1.0.0
execution_phase: Phase 1 (Foundation)
created_date: 2026-03-01
status: Active

subdomains:
  - sd_003a: Research Methodology
    description: Definition of research protocols, experimental design standards, hypothesis testing frameworks, and systematic review processes
    decomposition_level: 3
    
  - sd_003b: Benchmarking Protocols
    description: Design of benchmarking suites, performance measurement standards, baseline definitions, comparative evaluation frameworks
    decomposition_level: 3
    
  - sd_003c: Evidence Grading
    description: Evidence quality assessment frameworks, confidence scoring, source reliability evaluation, knowledge atom validation
    decomposition_level: 3

section_1_skills:
  - skill_id: DOM-003-SK-001
    name: Benchmark Suite Design and Execution
    description: Design comprehensive benchmark suites and execute them against target systems, collecting standardized performance metrics.
    inputs: [Target system specs, metric definitions, environment config, baseline targets]
    outputs: [Benchmark results, performance metrics, execution logs, analysis reports]
    complexity: High
    knowledge_atoms: [KA-003]

  - skill_id: DOM-003-SK-002
    name: Evidence Grading and Confidence Scoring
    description: Assess evidence quality using standardized grading scales and assign confidence scores to claims and metrics.
    inputs: [Raw evidence, source metadata, evidence type, context]
    outputs: [Graded evidence, confidence scores, grading rationale, audit trail]
    complexity: High
    related_subdomains: [SD-003c]

  - skill_id: DOM-003-SK-003
    name: Research Protocol Authoring
    description: Create rigorous research protocols with defined hypotheses, methodologies, controls, and expected outcomes.
    inputs: [Research objectives, domain knowledge, governance constraints, success criteria]
    outputs: [Research protocol document, hypothesis statements, methodology specs]
    complexity: Medium
    related_subdomains: [SD-003a]

  - skill_id: DOM-003-SK-004
    name: Statistical Analysis for Performance Evaluation
    description: Apply statistical methods to interpret performance data, detect trends, calculate confidence intervals, and validate hypotheses.
    inputs: [Performance datasets, statistical requirements, baseline data]
    outputs: [Statistical summaries, significance tests, trend analysis, p-values]
    complexity: High
    related_subdomains: [SD-003b]

  - skill_id: DOM-003-SK-005
    name: Knowledge Atom Validation
    description: Validate knowledge atoms for correctness, completeness, consistency, and readiness for production use.
    inputs: [Knowledge atom candidate, validation rules, reference data]
    outputs: [Validation result, confidence level, evidence references, approval status]
    complexity: Medium
    related_subdomains: [SD-003c]

  - skill_id: DOM-003-SK-006
    name: Comparative Model Capability Assessment
    description: Compare capabilities across multiple models or systems using standardized evaluation frameworks and metrics.
    inputs: [Multiple models/systems, evaluation criteria, test datasets]
    outputs: [Capability matrices, comparison reports, ranking analysis]
    complexity: High
    knowledge_atoms: [KA-003]

  - skill_id: DOM-003-SK-007
    name: Reproducibility Verification
    description: Verify that experimental results and benchmarks can be reliably reproduced across different environments and runs.
    inputs: [Experimental design, execution logs, environment specs, raw results]
    outputs: [Reproducibility report, variance analysis, environment dependency map]
    complexity: Medium
    related_subdomains: [SD-003a]

  - skill_id: DOM-003-SK-008
    name: Baseline Definition and Management
    description: Establish, document, and maintain performance baselines for benchmarks and metrics.
    inputs: [Historical performance data, business requirements, environmental factors]
    outputs: [Baseline specification, version history, baseline documentation]
    complexity: Medium
    related_subdomains: [SD-003b]

  - skill_id: DOM-003-SK-009
    name: Source Reliability Evaluation
    description: Assess the credibility, authority, and bias of information sources used in research and evidence grading.
    inputs: [Source metadata, publication history, methodology details]
    outputs: [Source reliability score, trust assessment, bias analysis]
    complexity: Medium
    related_subdomains: [SD-003c]

  - skill_id: DOM-003-SK-010
    name: Systematic Review Process Management
    description: Conduct systematic reviews of existing research and benchmarking work to identify best practices and gaps.
    inputs: [Review scope, search criteria, inclusion/exclusion rules]
    outputs: [Literature summary, gap analysis, recommendations]
    complexity: High
    related_subdomains: [SD-003a]

section_2_workflows:
  - workflow_id: DOM-003-WF-001
    name: Benchmark Execution and Reporting Workflow
    description: Complete lifecycle for designing, executing, analyzing, and reporting benchmark results
    trigger: New benchmarking requirement or scheduled benchmark run
    steps:
      - step_1:
          name: Benchmark Design Review
          action: Review benchmark specifications against governance standards
          entry_criteria: Benchmark design document exists, governance context available
          exit_criteria: Design approved, environment specs confirmed
          responsible_skill: [DOM-003-SK-003, DOM-003-SK-008]
      - step_2:
          name: Environment Setup
          action: Prepare isolated test environment matching benchmark specs
          entry_criteria: Benchmark design approved
          exit_criteria: Environment verified, baseline metrics established
          responsible_skill: [DOM-003-SK-008]
      - step_3:
          name: Benchmark Execution
          action: Run benchmark suite according to design specifications
          entry_criteria: Environment setup complete, metrics configured
          exit_criteria: All test iterations complete, raw data collected
          responsible_skill: [DOM-003-SK-001]
      - step_4:
          name: Statistical Analysis
          action: Apply statistical methods to interpret results
          entry_criteria: Raw benchmark data complete
          exit_criteria: Statistical significance determined, trends identified
          responsible_skill: [DOM-003-SK-004]
      - step_5:
          name: Reproducibility Check
          action: Verify results can be reproduced
          entry_criteria: Statistical analysis complete
          exit_criteria: Reproducibility confirmed or issues identified
          responsible_skill: [DOM-003-SK-007]
      - step_6:
          name: Report Generation
          action: Create comprehensive benchmark report with findings
          entry_criteria: Analysis complete, reproducibility verified
          exit_criteria: Report published, stakeholders notified
          responsible_skill: [DOM-003-SK-001, DOM-003-SK-004]
    completion_criteria: Benchmark report approved, results archived, baselines updated
    rollback_plan: Revert environment, discard compromised results, restart from step 1

  - workflow_id: DOM-003-WF-002
    name: Evidence Grading Pipeline
    description: Complete process for assessing and grading evidence quality
    trigger: New evidence submitted or periodic evidence review
    steps:
      - step_1:
          name: Evidence Classification
          action: Categorize evidence type and source
          entry_criteria: Raw evidence available
          exit_criteria: Evidence type and source classified
          responsible_skill: [DOM-003-SK-009]
      - step_2:
          name: Source Reliability Assessment
          action: Evaluate source credibility and potential bias
          entry_criteria: Evidence classified
          exit_criteria: Source reliability score assigned
          responsible_skill: [DOM-003-SK-009]
      - step_3:
          name: Quality Assessment
          action: Evaluate evidence against quality criteria
          entry_criteria: Source assessed
          exit_criteria: Quality metrics computed
          responsible_skill: [DOM-003-SK-002]
      - step_4:
          name: Confidence Scoring
          action: Assign confidence scores based on evidence quality and source
          entry_criteria: Quality assessment complete
          exit_criteria: Confidence score assigned
          responsible_skill: [DOM-003-SK-002]
      - step_5:
          name: Evidence Grading
          action: Assign formal grade (A/B/C/D/F) using standardized scale
          entry_criteria: Confidence score assigned
          exit_criteria: Grade assigned, grading justification documented
          responsible_skill: [DOM-003-SK-002]
      - step_6:
          name: Audit Trail Creation
          action: Document all assessment decisions and dates
          entry_criteria: Grade assigned
          exit_criteria: Audit trail complete, ready for compliance review
          responsible_skill: [DOM-003-SK-002]
    completion_criteria: Evidence graded, audit trail complete, grade published
    rollback_plan: Revert grade, investigate assessment error, reassess evidence

  - workflow_id: DOM-003-WF-003
    name: Knowledge Atom Validation Workflow
    description: Lifecycle for validating knowledge atoms before production use
    trigger: New knowledge atom submission or periodic validation review
    steps:
      - step_1:
          name: Completeness Check
          action: Verify all required fields and metadata present
          entry_criteria: Knowledge atom submitted
          exit_criteria: Completeness verified
          responsible_skill: [DOM-003-SK-005]
      - step_2:
          name: Consistency Validation
          action: Check for logical consistency and conflicts with existing atoms
          entry_criteria: Completeness verified
          exit_criteria: Consistency confirmed or conflicts documented
          responsible_skill: [DOM-003-SK-005]
      - step_3:
          name: Evidence Collection
          action: Gather supporting evidence for atom claims
          entry_criteria: Consistency validated
          exit_criteria: Evidence set compiled, sources cited
          responsible_skill: [DOM-003-SK-005]
      - step_4:
          name: Evidence Grading
          action: Grade supporting evidence quality
          entry_criteria: Evidence collected
          exit_criteria: Each evidence item graded
          responsible_skill: [DOM-003-SK-002]
      - step_5:
          name: Confidence Assignment
          action: Calculate overall confidence score for atom
          entry_criteria: Evidence graded
          exit_criteria: Confidence score assigned
          responsible_skill: [DOM-003-SK-005]
      - step_6:
          name: Approval Decision
          action: Determine if atom meets production readiness criteria
          entry_criteria: Confidence score assigned
          exit_criteria: Approved or rejected with justification
          responsible_skill: [DOM-003-SK-005]
    completion_criteria: Validation complete, status recorded, decision documented
    rollback_plan: Return atom to review, request additional evidence, defer decision

  - workflow_id: DOM-003-WF-004
    name: Research Methodology Review Workflow
    description: Process for reviewing and approving research protocols
    trigger: New research initiative or periodic methodology audit
    steps:
      - step_1:
          name: Protocol Submission Review
          action: Check research protocol for completeness
          entry_criteria: Research protocol document submitted
          exit_criteria: Submission requirements verified
          responsible_skill: [DOM-003-SK-003]
      - step_2:
          name: Governance Compliance Check
          action: Verify protocol aligns with AGT-001 governance standards
          entry_criteria: Protocol complete
          exit_criteria: Governance compliance confirmed or issues identified
          responsible_skill: [DOM-003-SK-003]
      - step_3:
          name: Methodology Review
          action: Evaluate research methodology for rigor and validity
          entry_criteria: Governance check passed
          exit_criteria: Methodology assessment documented
          responsible_skill: [DOM-003-SK-003]
      - step_4:
          name: Control Assessment
          action: Review controls and potential confounding variables
          entry_criteria: Methodology reviewed
          exit_criteria: Control design approved
          responsible_skill: [DOM-003-SK-003]
      - step_5:
          name: Approval Decision
          action: Approve or require modifications to protocol
          entry_criteria: All reviews complete
          exit_criteria: Protocol approved or revision requirements documented
          responsible_skill: [DOM-003-SK-003]
    completion_criteria: Protocol approved, authorization recorded, research can commence
    rollback_plan: Request protocol revisions, schedule follow-up review

  - workflow_id: DOM-003-WF-005
    name: Performance Baseline Establishment Workflow
    description: Process for defining and validating baseline metrics
    trigger: New performance domain or baseline update cycle
    steps:
      - step_1:
          name: Historical Data Collection
          action: Gather existing performance data from all available sources
          entry_criteria: Baseline scope defined
          exit_criteria: Historical dataset compiled
          responsible_skill: [DOM-003-SK-008]
      - step_2:
          name: Baseline Calculation
          action: Compute baseline metrics from historical data
          entry_criteria: Historical data collected
          exit_criteria: Initial baseline metrics calculated
          responsible_skill: [DOM-003-SK-004, DOM-003-SK-008]
      - step_3:
          name: Environment Normalization
          action: Account for environmental variations in baseline
          entry_criteria: Baseline metrics calculated
          exit_criteria: Environment-adjusted baselines established
          responsible_skill: [DOM-003-SK-008]
      - step_4:
          name: Validation Testing
          action: Test baseline against current system performance
          entry_criteria: Environment-adjusted baselines established
          exit_criteria: Baseline validation results recorded
          responsible_skill: [DOM-003-SK-001, DOM-003-SK-008]
      - step_5:
          name: Stakeholder Review
          action: Present baseline to stakeholders for acceptance