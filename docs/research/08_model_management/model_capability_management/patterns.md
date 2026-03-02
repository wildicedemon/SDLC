# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]

# Model Capability Management: Patterns

This document catalogs identified patterns and anti-patterns in model capability management for autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Cascaded Model Selection

**Name**: Cascaded Model Selection (also known as "Model Cascade" or "Tiered Routing")

**Description**: Route requests through a sequence of models, starting with smaller/cheaper models and escalating to larger/more capable models only when necessary. The cascade terminates when a model produces a satisfactory result or all models have been tried.

**When to Use**:
- High-volume, cost-sensitive workloads
- Tasks with variable complexity
- When latency budget allows for potential escalation
- Production systems with clear quality thresholds

**Implementation**:
1. Define model tiers (e.g., small → medium → large)
2. Set quality/confidence thresholds for escalation
3. Implement fallback logic with timeout handling
4. Track escalation rates for optimization

**Trade-offs**:
- ✅ 60-80% cost reduction compared to always using largest model
- ✅ Graceful degradation under load
- ✅ Automatic quality-cost balancing
- ❌ Added latency on escalations (typically 2-3x base latency)
- ❌ Requires threshold tuning and monitoring
- ❌ May over-provision for simple tasks if thresholds too low

**Confidence**: HIGH - Well-documented in academic literature and production deployments [paper:1][paper:2]

---

### Pattern 2: Task-Type Routing

**Name**: Task-Type Routing (also known as "Semantic Routing" or "Intent-Based Routing")

**Description**: Classify incoming tasks by type and route to models optimized for that task type. Classification can be rule-based (keyword matching, regex) or ML-based (embeddings, classifiers).

**When to Use**:
- Diverse task types with different model requirements
- When task types have clear differentiation
- When specialized models provide significant advantages
- Systems with task classification infrastructure

**Implementation**:
1. Define task type taxonomy (planning, generation, debugging, review, etc.)
2. Map task types to optimal models
3. Implement classification logic
4. Monitor and refine mappings based on outcomes

**Trade-offs**:
- ✅ Leverages model specializations
- ✅ Predictable routing behavior
- ✅ Easy to reason about and debug
- ❌ Requires accurate task classification
- ❌ May miss nuanced task requirements
- ❌ Taxonomy maintenance overhead

**Confidence**: HIGH - Common pattern in production systems [web:4][web:26]

---

### Pattern 3: Confidence-Based Escalation

**Name**: Confidence-Based Escalation

**Description**: Use model confidence scores (or estimated confidence) to determine when to escalate to a more capable model. Low confidence triggers automatic escalation without explicit failure.

**When to Use**:
- Tasks with uncertainty quantification
- When confidence correlates with quality
- Cost-sensitive applications with quality requirements
- Systems with calibrated confidence estimates

**Implementation**:
1. Obtain or estimate confidence scores from model outputs
2. Define confidence thresholds per task type or model
3. Implement escalation logic with confidence checks
4. Monitor calibration and adjust thresholds

**Trade-offs**:
- ✅ Adaptive to task difficulty
- ✅ Efficient resource utilization
- ✅ Handles uncertainty gracefully
- ❌ Requires calibrated confidence estimates
- ❌ Threshold tuning complexity
- ❌ May escalate unnecessarily if poorly calibrated

**Confidence**: HIGH - Strong empirical support [paper:1][paper:13]

---

### Pattern 4: Generator-Critic Pattern

**Name**: Generator-Critic Pattern (also known as "Generate-Review" or "Producer-Verifier")

**Description**: One model generates output, another model reviews/critiques it. The critic can approve, reject, or suggest improvements. Multiple iterations may occur.

**When to Use**:
- High-stakes code generation
- Security-sensitive applications
- When quality is more important than cost
- Complex tasks prone to subtle errors

**Implementation**:
1. Select generator model (often larger, creative)
2. Select critic model (often specialized for review)
3. Define review criteria and feedback format
4. Implement iteration logic with termination conditions

**Trade-offs**:
- ✅ 15-25% error reduction
- ✅ Catches hallucinations and subtle bugs
- ✅ Provides quality assurance
- ❌ 1.5-2x cost increase
- ❌ Added latency
- ❌ Requires well-defined review criteria

**Confidence**: HIGH - Well-established pattern [paper:16][web:30]

---

### Pattern 5: Temperature Per Task

**Name**: Temperature Per Task (also known as "Task-Specific Temperature")

**Description**: Configure different temperature values for different task types based on their requirements for creativity vs. consistency.

**When to Use**:
- Systems handling diverse task types
- When output characteristics vary by task
- Quality optimization for specific workflows
- Multi-mode agent systems

**Implementation**:
1. Define task type taxonomy
2. Determine optimal temperature per task type
3. Configure temperature in model calls
4. Monitor and adjust based on outcomes

**Trade-offs**:
- ✅ Optimizes output characteristics per task
- ✅ Simple to implement
- ✅ Significant quality improvements
- ❌ Requires task classification
- ❌ Temperature may interact with other parameters
- ❌ Model-specific optimal values vary

**Confidence**: HIGH - Well-documented guidance [web:1][paper:11]

---

### Pattern 6: Capability Matrix Registry

**Name**: Capability Matrix Registry

**Description**: Maintain a centralized registry of model capabilities, updated through benchmarking, production metrics, and research signals. Use this registry for routing decisions.

**When to Use**:
- Multi-model systems with frequent model changes
- When routing decisions need current capability data
- Systems with automated model evaluation
- Enterprise environments with governance requirements

**Implementation**:
1. Define capability dimensions
2. Implement benchmarking pipeline
3. Create registry with update mechanisms
4. Integrate with routing logic

**Trade-offs**:
- ✅ Data-driven routing decisions
- ✅ Handles model updates gracefully
- ✅ Supports governance and auditing
- ❌ Maintenance overhead
- ❌ Benchmark latency
- ❌ May not capture all relevant capabilities

**Confidence**: MEDIUM-HIGH - Common practice but limited formal documentation [web:2][web:3]

---

### Pattern 7: Parallel Model Execution

**Name**: Parallel Model Execution (also known as "Race" or "Best-of-N")

**Description**: Execute multiple models in parallel and select the best result based on quality metrics, voting, or other selection criteria.

**When to Use**:
- High-stakes decisions requiring high confidence
- When latency budget allows parallel execution
- Tasks with objective quality metrics
- Time-sensitive applications (parallel faster than cascade)

**Implementation**:
1. Select models for parallel execution
2. Execute requests simultaneously
3. Implement selection logic (quality score, voting, etc.)
4. Handle timeouts and partial results

**Trade-offs**:
- ✅ Higher quality through diversity
- ✅ Fast (parallel latency)
- ✅ Reduces single-model bias
- ❌ 2-4x cost increase
- ❌ Requires quality evaluation
- ❌ Coordination complexity

**Confidence**: MEDIUM-HIGH - Used in production but cost-prohibitive for many use cases [paper:16]

---

### Pattern 8: Trust Score Accumulation

**Name**: Trust Score Accumulation (also known as "Reputation Scoring")

**Description**: Maintain running trust scores for each model based on historical performance. Use these scores to inform routing decisions and detect degradation.

**When to Use**:
- Long-running systems with repeated tasks
- Multi-agent systems with delegation
- When model performance varies over time
- Systems requiring explainable routing

**Implementation**:
1. Define trust score calculation method
2. Track task outcomes per model
3. Update scores with decay for recency
4. Integrate scores into routing decisions

**Trade-offs**:
- ✅ Adapts to model changes
- ✅ Supports explainable decisions
- ✅ Detects degradation early
- ❌ Cold start for new models
- ❌ Requires outcome tracking
- ❌ May be slow to adapt

**Confidence**: MEDIUM - Established concept but limited production documentation [paper:20][paper:21]

---

### Pattern 9: Context-Aware Model Selection

**Name**: Context-Aware Model Selection

**Description**: Select models based on context characteristics (size, complexity, language, domain) in addition to task type.

**When to Use**:
- Systems with variable context sizes
- Multi-language codebases
- Domain-specific applications
- When context significantly impacts model performance

**Implementation**:
1. Analyze context characteristics
2. Define selection rules based on context
3. Consider context window limits
4. Monitor context-model interactions

**Trade-offs**:
- ✅ Handles context diversity
- ✅ Avoids context overflow
- ✅ Leverages model strengths
- ❌ Requires context analysis
- ❌ More complex routing logic
- ❌ Context extraction overhead

**Confidence**: MEDIUM-HIGH - Important for production systems [paper:14]

---

### Pattern 10: Validation-Gated Fallback

**Name**: Validation-Gated Fallback

**Description**: Validate model outputs against defined criteria. If validation fails, automatically retry with a different model or escalate.

**When to Use**:
- Quality-critical applications
- When outputs must meet specific criteria
- Systems with validation infrastructure
- Tasks with objective correctness measures

**Implementation**:
1. Define validation criteria per task type
2. Implement validation logic (tests, linters, schemas)
3. Configure fallback chain
4. Track validation rates per model

**Trade-offs**:
- ✅ Quality assurance
- ✅ Catches errors early
- ✅ Supports compliance requirements
- ❌ Added latency for validation
- ❌ Validation may have false positives
- ❌ Requires validation infrastructure

**Confidence**: HIGH - Common pattern in production [web:23][web:24]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Single-Model Monoculture

**Name**: Single-Model Monoculture

**Description**: Relying exclusively on a single model for all tasks regardless of task characteristics, cost considerations, or availability requirements.

**Failure Mode**:
- Single point of failure
- Suboptimal quality for tasks outside model's strengths
- Cost inefficiency (over-provisioning capability)
- Vulnerability to model outages or degradation
- Lock-in to single provider

**Remediation**:
- Implement multi-model routing
- Define fallback chains
- Evaluate models for specific task types
- Monitor for degradation

**Confidence**: HIGH - Well-recognized risk [paper:1][web:18]

---

### Anti-Pattern 2: Static Capability Assumptions

**Name**: Static Capability Assumptions

**Description**: Assuming model capabilities remain constant over time without monitoring for changes, updates, or degradation.

**Failure Mode**:
- Model updates introduce regressions
- Capability drift goes undetected
- Routing decisions become outdated
- Quality degradation without awareness

**Remediation**:
- Implement continuous benchmarking
- Monitor production metrics
- Track model version changes
- Maintain dynamic capability matrix

**Confidence**: HIGH - Documented failure mode [paper:10][web:14]

---

### Anti-Pattern 3: Temperature Neglect

**Name**: Temperature Neglect

**Description**: Using default temperature values for all tasks without considering task-specific requirements.

**Failure Mode**:
- Inconsistent outputs for reasoning tasks (temperature too high)
- Lack of creativity for exploratory tasks (temperature too low)
- Suboptimal quality across task types
- Unpredictable behavior

**Remediation**:
- Define temperature per task type
- Document temperature guidelines
- Monitor output characteristics
- Adjust based on outcomes

**Confidence**: HIGH - Well-documented impact [web:1][paper:11]

---

### Anti-Pattern 4: Confidence Blindness

**Name**: Confidence Blindness

**Description**: Ignoring model confidence scores or failing to estimate confidence when making routing or escalation decisions.

**Failure Mode**:
- Low-quality outputs accepted without scrutiny
- Missed opportunities for escalation
- Overconfidence in uncertain outputs
- Quality issues in production

**Remediation**:
- Extract or estimate confidence scores
- Define escalation thresholds
- Monitor confidence-quality correlation
- Calibrate confidence estimates

**Confidence**: MEDIUM-HIGH - Recognized issue [paper:1][paper:13]

---

### Anti-Pattern 5: Hallucination Blindness

**Name**: Hallucination Blindness

**Description**: Failing to detect or mitigate hallucinations in model outputs, assuming all outputs are correct.

**Failure Mode**:
- Incorrect code deployed to production
- Security vulnerabilities introduced
- API calls to non-existent methods
- Logic errors in critical paths

**Remediation**:
- Implement hallucination detection
- Use multi-model verification
- Integrate static analysis
- Apply test-based validation

**Confidence**: HIGH - Critical failure mode [paper:3][paper:7]

---

### Anti-Pattern 6: Cost-Unaware Routing

**Name**: Cost-Unaware Routing

**Description**: Making routing decisions without considering cost implications, leading to unnecessary expense.

**Failure Mode**:
- Using expensive models for simple tasks
- Budget overruns
- Inefficient resource utilization
- Unsustainable operational costs

**Remediation**:
- Track costs per model and task type
- Implement cost-aware routing logic
- Define cost-quality trade-offs
- Monitor and optimize spending

**Confidence**: HIGH - Common operational issue [paper:6][web:5]

---

### Anti-Pattern 7: Fallback Infinite Loop

**Name**: Fallback Infinite Loop (also known as "Circular Fallback")

**Description**: Poorly designed fallback chains that can loop indefinitely or exhaust all options without resolution.

**Failure Mode**:
- Infinite retry loops
- Resource exhaustion
- Timeout failures
- Poor user experience

**Remediation**:
- Define maximum retry counts
- Implement circuit breakers
- Design acyclic fallback graphs
- Add terminal fallback (human escalation)

**Confidence**: HIGH - Common implementation error [web:24][web:25]

---

### Anti-Pattern 8: Context Poisoning Propagation

**Name**: Context Poisoning Propagation

**Description**: Allowing erroneous or misleading context from one model to propagate to subsequent models in a cascade or fallback chain.

**Failure Mode**:
- Errors compound across models
- Subsequent models misled by bad context
- Quality degradation in cascade
- Difficult to diagnose root cause

**Remediation**:
- Validate context before passing
- Reset context on fallback
- Track context provenance
- Implement context sanitization

**Confidence**: MEDIUM-HIGH - Documented in Roocode documentation [seed:7]

---

### Anti-Pattern 9: Benchmark Over-Reliance

**Name**: Benchmark Over-Reliance

**Description**: Making routing decisions based solely on benchmark performance without considering production workload characteristics.

**Failure Mode**:
- Benchmarks don't reflect real tasks
- Contamination leads to inflated scores
- Model selection mismatched to actual needs
- Poor production performance despite good benchmarks

**Remediation**:
- Use production-specific evaluation
- Maintain custom benchmark suites
- Consider multiple evaluation dimensions
- Validate benchmark claims with real tasks

**Confidence**: MEDIUM-HIGH - Recognized limitation [paper:5]

---

### Anti-Pattern 10: Trust Score Stagnation

**Name**: Trust Score Stagnation

**Description**: Failing to update trust scores over time, causing them to become stale and unrepresentative of current model performance.

**Failure Mode**:
- Outdated routing decisions
- Failure to detect degradation
- New model capabilities ignored
- Misaligned trust and actual performance

**Remediation**:
- Implement score decay
- Continuous score updates
- Periodic score recalculation
- Monitor score-performance alignment

**Confidence**: MEDIUM - Less documented but logical concern [paper:20]

---

## Use Cases Grounded in Research

### Use Case 1: Enterprise Code Assistant

**Scenario**: Large enterprise deploying AI coding assistant for 1000+ developers.

**Applicable Patterns**:
- Cascaded Model Selection (cost optimization at scale)
- Task-Type Routing (diverse developer tasks)
- Capability Matrix Registry (governance requirements)
- Trust Score Accumulation (long-term performance tracking)

**Avoided Anti-Patterns**:
- Single-Model Monoculture (availability requirements)
- Cost-Unaware Routing (budget constraints)
- Static Capability Assumptions (enterprise governance)

**Sources**: [paper:1][paper:6][web:18][web:22]

---

### Use Case 2: Security-Focused Code Generation

**Scenario**: Financial services company requiring secure code generation.

**Applicable Patterns**:
- Generator-Critic Pattern (security review)
- Validation-Gated Fallback (security validation)
- Temperature Per Task (consistent security analysis)
- Parallel Model Execution (high confidence requirements)

**Avoided Anti-Patterns**:
- Hallucination Blindness (security risk)
- Confidence Blindness (cannot accept uncertain security code)
- Context Poisoning Propagation (security context integrity)

**Sources**: [paper:3][paper:16][web:7][web:30]

---

### Use Case 3: Multi-Language Codebase Migration

**Scenario**: Tech company migrating monolith to microservices across multiple languages.

**Applicable Patterns**:
- Context-Aware Model Selection (language-specific routing)
- Task-Type Routing (different migration phases)
- Temperature Per Task (planning vs. generation)
- Capability Matrix Registry (language capability tracking)

**Avoided Anti-Patterns**:
- Benchmark Over-Reliance (custom language requirements)
- Temperature Neglect (consistent migration patterns)
- Static Capability Assumptions (evolving language support)

**Sources**: [paper:14][web:4][web:26]

---

### Use Case 4: Real-Time Code Review Bot

**Scenario**: CI/CD pipeline integration for automated code review.

**Applicable Patterns**:
- Confidence-Based Escalation (uncertain reviews to humans)
- Trust Score Accumulation (review quality tracking)
- Validation-Gated Fallback (review criteria enforcement)
- Task-Type Routing (different review types)

**Avoided Anti-Patterns**:
- Fallback Infinite Loop (CI timeout constraints)
- Cost-Unaware Routing (high volume of reviews)
- Confidence Blindness (review reliability)

**Sources**: [paper:1][paper:13][web:23][web:24]

---

### Use Case 5: Debugging and Incident Response

**Scenario**: On-call debugging assistance for production incidents.

**Applicable Patterns**:
- Temperature Per Task (low temperature for debugging)
- Cascaded Model Selection (fast initial response)
- Generator-Critic Pattern (solution verification)
- Confidence-Based Escalation (uncertain diagnoses to humans)

**Avoided Anti-Patterns**:
- Temperature Neglect (inconsistent debugging)
- Hallucination Blindness (incorrect diagnoses)
- Fallback Infinite Loop (incident timeout)

**Sources**: [web:1][paper:11][paper:16]
