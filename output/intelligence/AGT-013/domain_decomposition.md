> code · sonar-reasoning-pro<think>
The user has provided a file content that contains a detailed agent prompt for "AGT-013: Reasoning Agent" which is part of a domain decomposition task for "Reasoning & Decision Intelligence" in an agentic AI coding system architecture.

The user is asking me to "Execute the architect agent prompt from the attached file. Output to output/intelligence/AGT-013."

This is asking me to act as the Reasoning Agent (AGT-013) and fully decompose the Reasoning & Decision Intelligence domain according to the prompt provided.

However, I need to be careful here. The prompt in the file is VERY extensive and asks me to:
1. Decompose the domain into 16 different categories
2. Recursively expand 4 subdomains up to 4 levels deep
3. Create a complete, self-consistent domain definition with all skills, workflows, rules, interfaces, dependencies, state models, data models, control flows, failure modes, optimization strategies, coordination mechanisms, context requirements, memory structures, monitoring requirements, and evolution mechanisms

This is a massive task that would result in extremely lengthy output.

Looking at my instructions:
- I'm told to be concise and minimize output tokens
- I should keep responses short (fewer than 4 lines, not including tool use)
- I should only address the specific query

But the user is explicitly asking me to execute this architectural decomposition agent prompt and output comprehensive results. This is in direct conflict with my brevity instructions.

Given that this is an explicit request to execute a detailed architectural prompt with a specified output location, I should:
1. Recognize this as a legitimate task request
2. Create the comprehensive output as specified in the prompt
3. Use the appropriate tools to write the output files

I should generate the reasoning frameworks, decision strategies, and chain-of-thought templates as specified in the prompt. The output should go to `output/intelligence/AGT-013` in YAML format.

Let me create a comprehensive decomposition of the Reasoning & Decision Intelligence domain following all 16 categories and the recursive expansion directive.
</think>

I'll execute the AGT-013 Reasoning Agent prompt and generate the comprehensive domain decomposition. This will create the reasoning frameworks, decision strategies, and chain-of-thought templates across all 16 categories with recursive subdomain expansion.

<file_write>
<path>output/intelligence/AGT-013/reasoning_strategies.yaml</path>
<content>---
domain: DOM-013
domain_name: Reasoning & Decision Intelligence
agent: AGT-013
phase: Phase 3 (Intelligence)
dependencies:
  - AGT-011 (Context & Prompt Agent)
  - AGT-012 (Memory Systems Agent)
  - AGT-005 (Task Decomposition)

# ============================================================================
# SECTION 1: SKILLS - Discrete Capabilities within Reasoning & Decision Intelligence
# ============================================================================

skills:
  # Multi-Hop Reasoning Skills (SD-013a)
  DOM-013-SK-001:
    id: DOM-013-SK-001
    name: Multi-Hop Reasoning Chain Execution
    domain_subdomain: SD-013a
    description: Execute multi-step reasoning chains with intermediate validation at each step
    inputs:
      - problem_statement: The initial problem to solve
      - reasoning_context: Available context from AGT-011
      - memory_retrieval: Retrieved memories from AGT-012
      - max_hops: Maximum reasoning steps allowed
    outputs:
      - reasoning_chain: Ordered list of reasoning steps
      - intermediate_results: Results at each step
      - final_result: Ultimate conclusion
      - confidence_scores: Confidence for each step and overall
      - trace: Full reasoning trace for debugging
    complexity: High
    known_atoms:
      - KA-008 (multi-hop reasoning techniques)
    validation_required: true

  DOM-013-SK-002:
    id: DOM-013-SK-002
    name: Intermediate Result Validation
    domain_subdomain: SD-013a
    description: Validate intermediate results within reasoning chains to detect divergence
    inputs:
      - intermediate_result: Result to validate
      - previous_steps: Earlier steps in the chain
      - validation_rules: Domain-specific validation rules
    outputs:
      - validation_passed: Boolean pass/fail
      - confidence: Validation confidence score (0.0-1.0)
      - divergence_detected: Whether reasoning is diverging
      - correction_suggestion: Optional guidance for correction
    complexity: Medium
    validation_required: true

  DOM-013-SK-003:
    id: DOM-013-SK-003
    name: Reasoning Path Exploration
    domain_subdomain: SD-013a
    description: Explore multiple potential reasoning paths and compare outcomes
    inputs:
      - problem_state: Current problem state
      - available_approaches: Alternative reasoning strategies
      - resource_budget: Available computation tokens
    outputs:
      - explored_paths: List of explored reasoning paths
      - path_outcomes: Results from each path
      - optimal_path: Best path identified
      - path_comparison: Comparative analysis of paths
    complexity: High
    validation_required: true

  DOM-013-SK-004:
    id: DOM-013-SK-004
    name: Reasoning Depth Management
    domain_subdomain: SD-013a
    description: Manage and optimize the depth of reasoning chains to prevent explosion
    inputs:
      - current_depth: Current reasoning step count
      - max_depth_allowed: Maximum permitted depth
      - problem_complexity: Estimated problem complexity
      - diminishing_returns_threshold: When confidence gains plateau
    outputs:
      - should_continue: Whether to continue reasoning
      - depth_recommendation: Recommended depth level
      - optimization_feedback: Feedback on current depth
    complexity: Medium
    validation_required: false

  # Self-Consistency Skills (SD-013b)
  DOM-013-SK-005:
    id: DOM-013-SK-005
    name: Self-Consistency Sampling
    domain_subdomain: SD-013b
    description: Generate multiple independent reasoning samples and collect results
    inputs:
      - problem_statement: Problem to solve
      - sample_count: Number of samples to generate
      - sampling_strategy: Deterministic | Stochastic | Adaptive
      - memory_context: Long-term memory for consistency
    outputs:
      - samples: Array of reasoning outputs
      - sample_metadata: Generation details for each sample
      - sampling_statistics: Summary statistics
    complexity: Medium
    known_atoms:
      - KA-031 (self-consistency sampling techniques)
    validation_required: true

  DOM-013-SK-006:
    id: DOM-013-SK-006
    name: Majority Voting and Consensus Detection
    domain_subdomain: SD-013b
    description: Aggregate multiple reasoning samples and detect consensus
    inputs:
      - samples: Array of reasoning outputs
      - aggregation_method: Majority | Weighted | Ranked Choice
      - minimum_consensus_threshold: Minimum agreement ratio
    outputs:
      - consensus_answer: Majority-selected answer
      - agreement_ratio: Percentage of samples agreeing
      - consensus_confidence: Confidence in consensus
      - dissenting_views: Minority reasoning samples
    complexity: Medium
    known_atoms:
      - KA-031 (self-consistency techniques)
    validation_required: true

  DOM-013-SK-007:
    id: DOM-013-SK-007
    name: Consistency Validation
    domain_subdomain: SD-013b
    description: Validate consistency across reasoning samples and identify conflicts
    inputs:
      - samples: Multiple reasoning outputs
      - conflict_threshold: Tolerance for disagreement
    outputs:
      - consistency_score: Overall consistency measure (0.0-1.0)
      - conflict_regions: Areas of disagreement
      - conflict_resolution_strategy: How to handle conflicts
    complexity: Medium
    validation_required: true

  DOM-013-SK-008:
    id: DOM-013-SK-008
    name: Confidence Calibration
    domain_subdomain: SD-013b
    description: Calibrate confidence scores based on sample agreement and consistency
    inputs:
      - agreement_ratio: Percentage of samples in agreement
      - consistency_score: Overall consistency measure
      - historical_accuracy: Past performance on similar problems
      - problem_difficulty: Assessed problem difficulty
    outputs:
      - calibrated_confidence: Adjusted confidence score (0.0-1.0)
      - confidence_components: Breakdown of confidence factors
      - uncertainty_estimate: Quantified uncertainty
    complexity: Medium
    validation_required: true

  # Chain-of-Thought Skills (SD-013c)
  DOM-013-SK-009:
    id: DOM-013-SK-009
    name: Chain-of-Thought Prompt Construction
    domain_subdomain: SD-013c
    description: Construct effective chain-of-thought prompts that guide reasoning
    inputs:
      - problem_statement: Problem to solve
      - reasoning_style: Analytical | Creative | Systematic | Comparative
      - context_information: Available contextual information
      - examples: Few-shot examples if available
    outputs:
      - cot_prompt: Constructed chain-of-thought prompt
      - prompt_structure: Template/pattern used
      - expected_reasoning_steps: Steps the model should follow
    complexity: Medium
    known_atoms:
      - KA-031 (chain-of-thought prompting patterns)
    validation_required: false

  DOM-013-SK-010:
    id: DOM-013-SK-010
    name: Step-by-Step Decomposition
    domain_subdomain: SD-013c
    description: Break complex problems into step-by-step reasoning sequences
    inputs:
      - problem: Complex problem to decompose
      - decomposition_strategy: Linear | Tree | Graph | Recursive
      - step_granularity: Level of detail for each step
    outputs:
      - steps: Ordered list of reasoning steps
      - step_dependencies: How steps relate to each other
      - expected_outputs: Expected output at each step
      - step_templates: Templates for executing each step
    complexity: Medium
    validation_required: true

  DOM-013-SK-011:
    id: DOM-013-SK-011
    name: Reasoning Trace Documentation
    domain_subdomain: SD-013c
    description: Document complete reasoning traces for transparency and debugging
    inputs:
      - reasoning_chain: Complete reasoning execution
      - reasoning_context: Context in which reasoning occurred
      - model_parameters: Model configuration used
    outputs:
      - trace_document: Structured reasoning trace
      - trace_format: JSON | YAML | Markdown
      - trace_with_annotations: Annotated with explanations
      - trace_visualization: Graphical representation data
    complexity: Low
    validation_required: false

  DOM-013-SK-012:
    id: DOM-013-SK-012
    name: Structured Reasoning Templates
    domain_subdomain: SD-013c
    description: Create and apply structured templates for common reasoning patterns
    inputs:
      - reasoning_pattern: Pattern type (analysis | comparison | synthesis | etc.)
      - domain_context: Domain-specific constraints
      - complexity_level: Simple | Moderate | Complex
    outputs:
      - template: Structured reasoning template
      - template_instructions: How to use the template
      - template_examples: Example outputs using this template
    complexity: Low
    validation_required: false

  # Decision Framework Skills (SD-013d)
  DOM-013-SK-013:
    id: DOM-013-SK-013
    name: Decision-Making Under Uncertainty
    domain_subdomain: SD-013d
    description: Make informed decisions when outcomes are uncertain
    inputs:
      - options: Available decision options
      - uncertainty_factors: Sources of uncertainty
      - risk_tolerance: Organization's risk tolerance
      - probability_estimates: Estimated probabilities if available
    outputs:
      - decision: Selected option
      - decision_confidence: Confidence in decision (0.0-1.0)
      - decision_rationale: Justification for decision
      - alternative_analysis: Analysis of alternatives
    complexity: High
    validation_required: true

  DOM-013-SK-014:
    id: DOM-013-SK-014
    name: Multi-Criteria Decision Analysis
    domain_subdomain: SD-013d
    description: Evaluate options against multiple criteria with weighted importance
    inputs:
      - options: Decision alternatives
      - criteria: Evaluation criteria with weights
      - scoring_function: How to score each option
      - normalization_method: How to normalize across criteria
    outputs:
      - scores: Numerical scores for each option
      - ranked_options: Options ranked by score
      - tradeoff_analysis: Visualization of tradeoffs
      - sensitivity_analysis: How rankings change with criteria weights
    complexity: Medium
    validation_required: true

  DOM-013-SK-015:
    id: DOM-013-SK-015
    name: Risk Assessment Frameworks
    domain_subdomain: SD-013d
    description: Assess and quantify risks associated with decisions
    inputs:
      - decision_option: Option to assess
      - risk_categories: Types of risks to consider
      - probability_estimates: Risk occurrence probabilities
      - impact_estimates: Potential impact if risk occurs
    outputs:
      - risk_assessment: Structured risk assessment
      - risk_score: Overall risk level (0.0-1.0)
      - risk_mitigation: Suggested mitigation strategies
      - acceptable_risk_threshold: Determination if risk is acceptable
    complexity: Medium
    validation_required: true

  DOM-013-SK-016:
    id: DOM-013-SK-016
    name: Delegation Decision Model
    domain_subdomain: SD-013d
    description: Decide whether to self-execute or delegate to another agent/human
    inputs:
      - task_complexity: Assessed complexity level
      - self_capability: Own capability assessment
      - external_resources: Available delegation targets
      - time_constraints: Time availability
      - criticality: Task importance/risk level
    outputs:
      - should_delegate: Boolean decision
      - delegation_target: Who to delegate to if applicable
      - retention_rationale: Why self-execute or why delegate
      - confidence: Confidence in delegation decision
    complexity: High
    validation_required: true

  # Additional Meta-Skills
  DOM-013-SK-017:
    id: DOM-013-SK-017
    name: Confidence Scoring for Reasoning Outputs
    domain_subdomain: SD-013a
    description: Generate and calibrate confidence scores for reasoning conclusions
    inputs:
      - reasoning_output: Conclusion from reasoning
      - reasoning_quality: Quality metrics from reasoning process
      - sample_agreement: Agreement across self-consistency samples
      - domain_knowledge: Known accuracy on similar problems
    outputs:
      - confidence_score: Final confidence (0.0-1.0)
      - confidence_components: Breakdown of contributing factors
      - confidence_calibration: Whether score is well-calibrated
    complexity: Medium
    validation_required: true

  DOM-013-SK-018:
    id: DOM-013-SK-018
    name: Reasoning Path Pruning and Optimization
    domain_subdomain: SD-013a
    description: Prune unpromising reasoning paths and optimize for efficiency
    inputs:
      - explored_paths: Multiple reasoning paths
      - path_metrics: Quality/efficiency metrics for each path
      - optimization_target: What to optimize for (speed | accuracy | efficiency)
    outputs:
      - pruned_paths: Remaining viable paths
      - optimal_execution_path: Best path to follow
      - pruning_rationale: Why paths were pruned
    complexity: Medium
    validation_required: false

  DOM-013-SK-019:
    id: DOM-013-SK-019
    name: Uncertainty Quantification
    domain_subdomain: SD-013d
    description: Quantify different types of uncertainty in reasoning and decisions
    inputs:
      - reasoning_output: Result with uncertainty
      - uncertainty_sources: Types of uncertainty (aleatoric | epistemic | model)
    outputs:
      - uncertainty_components: Breakdown of uncertainty types
      - total_uncertainty: Overall uncertainty estimate
      - uncertainty_reduction_strategy: How to reduce uncertainty
    complexity: High
    validation_required: true

  DOM-013-SK-020:
    id: DOM-013-SK-020
    name: Reasoning Trace Documentation and Retrieval
    domain_subdomain: SD-013c
    description: Store and retrieve reasoning traces for learning and debugging
    inputs:
      - trace_document: Reasoning trace to store
      - indexing_strategy: How to index for retrieval
      - retention_policy: How long to keep traces
    outputs:
      - trace_id: Unique identifier for trace
      - retrievable_trace: Formatted for later retrieval
      - indexing_metadata: Metadata for future lookup
    complexity: Low
    validation_required: false
</content>
</file_write>

<file_write>
<path>output/intelligence/AGT-013/workflows.yaml</path>
<content