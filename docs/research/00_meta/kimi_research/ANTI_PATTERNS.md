# Anti-Patterns Guide

Common mistakes in autonomous AI coding systems and how to avoid them.

---

## Table of Contents

1. [Architecture Anti-Patterns](#architecture-anti-patterns)
2. [Agent Design Anti-Patterns](#agent-design-anti-patterns)
3. [Context Management Anti-Patterns](#context-management-anti-patterns)
4. [Security Anti-Patterns](#security-anti-patterns)
5. [Operational Anti-Patterns](#operational-anti-patterns)
6. [Human Interaction Anti-Patterns](#human-interaction-anti-patterns)

---

## Architecture Anti-Patterns

### 1. The "God Agent"

**Problem**: A single agent tries to handle all tasks, becoming a bottleneck and single point of failure.

```python
# ANTI-PATTERN: God Agent
class GodAgent:
    """One agent to rule them all"""
    
    def handle_request(self, request):
        if request.type == "code":
            return self.generate_code(request)
        elif request.type == "review":
            return self.review_code(request)
        elif request.type == "test":
            return self.generate_tests(request)
        elif request.type == "deploy":
            return self.deploy(request)
        # ... 50 more elif statements
```

**Impact**:
- Context window overflow
- Poor performance on specialized tasks
- Difficult to maintain and debug
- No fault isolation

**Solution**: Use specialized agents with clear responsibilities.

```python
# PATTERN: Specialized Agents
class CodeGenerationAgent:
    def generate(self, request): ...

class CodeReviewAgent:
    def review(self, request): ...

class TestGenerationAgent:
    def generate_tests(self, request): ...

class DeploymentAgent:
    def deploy(self, request): ...

# Orchestrator coordinates
class AgentOrchestrator:
    def route(self, request):
        agent = self.select_agent(request.type)
        return agent.handle(request)
```

---

### 2. "Chatty" Agent Communication

**Problem**: Agents communicate excessively, causing latency and cost explosion.

```python
# ANTI-PATTERN: Excessive communication
class ChattyAgent:
    def process(self, task):
        # Every micro-decision requires confirmation
        for step in task.steps:
            result = self.execute(step)
            self.ask_other_agent("Is this correct?", result)
            self.ask_coordinator("Should I continue?")
            self.log_to_all_agents(result)
            # 3+ API calls per step!
```

**Impact**:
- 10x cost increase
- 5x latency increase
- Rate limiting issues
- Poor user experience

**Solution**: Batch communications and use shared state.

```python
# PATTERN: Efficient communication
class EfficientAgent:
    def process(self, task):
        results = []
        for step in task.steps:
            result = self.execute(step)
            results.append(result)
        
        # Single batch communication
        self.share_results_batch(results)
        return self.aggregate_results(results)
```

---

### 3. "Big Bang" Deployment

**Problem**: Deploying AI systems all at once without gradual rollout.

```yaml
# ANTI-PATTERN: Big bang deployment
deployment:
  strategy: all_at_once
  traffic: 100%  # All traffic immediately!
  rollback: manual
  testing: none
```

**Impact**:
- Production failures affect all users
- Difficult to rollback quickly
- No learning opportunity
- High risk

**Solution**: Gradual rollout with canary deployments.

```yaml
# PATTERN: Gradual rollout
deployment:
  strategy: canary
  phases:
    - name: canary
      traffic: 5%
      duration: 24h
      metrics: [error_rate, latency]
    - name: expanded
      traffic: 25%
      duration: 48h
    - name: full
      traffic: 100%
  auto_rollback:
    enabled: true
    error_threshold: 1%
```

---

## Agent Design Anti-Patterns

### 4. "Prompt Injection Vulnerability"

**Problem**: Agents execute user input without sanitization.

```python
# ANTI-PATTERN: Unsanitized input
class VulnerableAgent:
    def process_user_input(self, user_input):
        # DANGER: Direct execution!
        prompt = f"""
        Execute the following command:
        {user_input}
        """
        return self.llm.generate(prompt)
```

**Impact**:
- Arbitrary code execution
- Data exfiltration
- System compromise

**Solution**: Input validation and sandboxing.

```python
# PATTERN: Sanitized input with sandboxing
class SecureAgent:
    def process_user_input(self, user_input):
        # Validate input
        if not self.validator.is_safe(user_input):
            raise SecurityException("Unsafe input detected")
        
        # Execute in sandbox
        with Sandbox() as sandbox:
            return sandbox.execute(user_input)
```

---

### 5. "Hallucination Acceptance"

**Problem**: Blindly accepting AI-generated output without verification.

```python
# ANTI-PATTERN: No verification
class TrustingAgent:
    def generate_code(self, requirements):
        code = self.llm.generate(f"Write code for: {requirements}")
        # No verification!
        return code  # Might be completely wrong
```

**Impact**:
- Production bugs
- Security vulnerabilities
- Incorrect functionality

**Solution**: Multi-layer verification.

```python
# PATTERN: Verified output
class VerifiedAgent:
    def generate_code(self, requirements):
        code = self.llm.generate(f"Write code for: {requirements}")
        
        # Layer 1: Syntax check
        if not self.is_valid_syntax(code):
            return self.retry_with_feedback(code, "Syntax error")
        
        # Layer 2: Test execution
        test_results = self.run_tests(code)
        if not test_results.passed:
            return self.retry_with_feedback(code, test_results.errors)
        
        # Layer 3: Static analysis
        issues = self.static_analysis(code)
        if issues.critical:
            return self.retry_with_feedback(code, issues)
        
        return code
```

---

### 6. "Temperature Ignorance"

**Problem**: Using wrong temperature for task type.

```python
# ANTI-PATTERN: One temperature for all
temperature = 0.7  # Used for everything!

# Code generation (needs consistency)
code = llm.generate(prompt, temperature=0.7)

# Creative writing (needs variety)
story = llm.generate(prompt, temperature=0.7)

# Factual Q&A (needs accuracy)
fact = llm.generate(prompt, temperature=0.7)
```

**Impact**:
- Inconsistent code generation
- Hallucinated facts
- Poor task performance

**Solution**: Task-appropriate temperature.

```python
# PATTERN: Appropriate temperature
TEMPERATURES = {
    "code_generation": 0.1,      # Consistency
    "code_review": 0.1,          # Consistency
    "test_generation": 0.2,      # Mostly consistent
    "documentation": 0.3,        # Some creativity
    "brainstorming": 0.7,        # High creativity
    "factual_qa": 0.0,           # Deterministic
}

def generate(task_type, prompt):
    temp = TEMPERATURES.get(task_type, 0.3)
    return llm.generate(prompt, temperature=temp)
```

---

## Context Management Anti-Patterns

### 7. "Context Hoarding"

**Problem**: Sending entire codebase in every request.

```python
# ANTI-PATTERN: Full context every time
class ContextHoarder:
    def ask_question(self, question):
        # Sending 500K tokens every request!
        context = self.get_all_files()  # Entire codebase
        prompt = f"""
        Context: {context}
        Question: {question}
        """
        return self.llm.generate(prompt)  # $15 per request!
```

**Impact**:
- Excessive costs (10-50x)
- Slow response times
- Context window overflow
- Poor relevance

**Solution**: Intelligent context retrieval.

```python
# PATTERN: Smart context retrieval
class SmartContextAgent:
    def ask_question(self, question):
        # Retrieve only relevant context
        relevant_files = self.retriever.search(question, top_k=5)
        context = self.format_context(relevant_files)
        
        prompt = f"""
        Context: {context}
        Question: {question}
        """
        return self.llm.generate(prompt)  # $0.50 per request
```

---

### 8. "No Context Caching"

**Problem**: Repeatedly retrieving the same context.

```python
# ANTI-PATTERN: No caching
class NoCacheAgent:
    def process_file(self, file_path):
        # Retrieves context every time!
        for line in file:
            context = self.get_project_context()  # Same every time!
            suggestion = self.llm.generate(f"{context}\n{line}")
```

**Impact**:
- 3-5x unnecessary API calls
- Higher latency
- Increased costs

**Solution**: Semantic caching.

```python
# PATTERN: Semantic caching
class CachingAgent:
    def __init__(self):
        self.cache = SemanticCache()
    
    def process_file(self, file_path):
        context = self.get_project_context()
        
        for line in file:
            cache_key = f"{context.hash}:{line.hash}"
            
            if cached := self.cache.get(cache_key):
                suggestion = cached
            else:
                suggestion = self.llm.generate(f"{context}\n{line}")
                self.cache.set(cache_key, suggestion)
```

---

### 9. "Static Context Window"

**Problem**: Fixed context size regardless of task complexity.

```python
# ANTI-PATTERN: Fixed context
CONTEXT_SIZE = 100000  # Always this size

def process_task(task):
    context = get_context(size=CONTEXT_SIZE)  # Wasteful for simple tasks
    return llm.generate(context + task)
```

**Impact**:
- Wasted tokens on simple tasks
- Insufficient context for complex tasks
- Suboptimal performance

**Solution**: Dynamic context sizing.

```python
# PATTERN: Dynamic context
def process_task(task):
    complexity = estimate_complexity(task)
    
    context_sizes = {
        "simple": 10000,
        "medium": 50000,
        "complex": 150000,
    }
    
    size = context_sizes.get(complexity, 50000)
    context = get_context(size=size)
    return llm.generate(context + task)
```

---

## Security Anti-Patterns

### 10. "Secret in Prompt"

**Problem**: Including secrets in LLM prompts.

```python
# ANTI-PATTERN: Secrets in prompts
prompt = f"""
Connect to database with:
Host: db.company.com
Password: {os.getenv('DB_PASSWORD')}  # DANGER!
API Key: {os.getenv('API_KEY')}       # DANGER!
"""
```

**Impact**:
- Secrets in logs
- Secrets in model training data
- Compliance violations

**Solution**: Secret redaction and environment isolation.

```python
# PATTERN: Secret-safe prompts
prompt = """
Connect to database using environment variables:
- DB_HOST (set externally)
- DB_PASSWORD (set externally)
- API_KEY (set externally)

Use: os.getenv() to access these values in code.
"""

# Secrets never touch the LLM
```

---

### 11. "No Output Filtering"

**Problem**: Not filtering dangerous LLM outputs.

```python
# ANTI-PATTERN: Unfiltered output
code = llm.generate("Write a function to delete files")
# Might generate: os.system("rm -rf /")
exec(code)  # DANGER!
```

**Impact**:
- Arbitrary code execution
- Data loss
- System compromise

**Solution**: Multi-layer output filtering.

```python
# PATTERN: Filtered output
code = llm.generate("Write a function to delete files")

# Layer 1: Dangerous pattern detection
if contains_dangerous_patterns(code):
    raise SecurityError("Dangerous code detected")

# Layer 2: Static analysis
issues = security_scanner.scan(code)
if issues.critical:
    raise SecurityError(f"Security issues: {issues}")

# Layer 3: Sandboxed execution
with Sandbox() as sandbox:
    result = sandbox.test_execute(code)
    if result.safe:
        return code
```

---

### 12. "Over-Privileged Agents"

**Problem**: Agents with excessive permissions.

```yaml
# ANTI-PATTERN: Over-privileged
agent_permissions:
  - "*"  # Everything!
  - "sudo:*"
  - "network:*"
  - "filesystem:*"
```

**Impact**:
- Lateral movement if compromised
- Data breaches
- Unauthorized actions

**Solution**: Principle of least privilege.

```yaml
# PATTERN: Minimal permissions
agent_permissions:
  filesystem:
    read:
      - "./src/**"
      - "./tests/**"
    write:
      - "./src/**"
    deny:
      - "./secrets/**"
      - "./.env"
  
  network:
    allow:
      - "api.github.com"
      - "api.openai.com"
    deny:
      - "*"
  
  commands:
    allow:
      - "git"
      - "npm"
    deny:
      - "sudo"
      - "rm -rf"
```

---

## Operational Anti-Patterns

### 13. "No Observability"

**Problem**: Deploying AI systems without monitoring.

```python
# ANTI-PATTERN: No observability
def generate_code(request):
    return llm.generate(request)  # No logging, no metrics!
```

**Impact**:
- Can't debug issues
- No performance insights
- Undetected failures
- No improvement data

**Solution**: Comprehensive observability.

```python
# PATTERN: Full observability
from opentelemetry import trace
from langfuse import Langfuse

tracer = trace.get_tracer(__name__)
langfuse = Langfuse()

def generate_code(request):
    with tracer.start_as_current_span("code_generation") as span:
        span.set_attribute("request.size", len(request))
        
        start_time = time.time()
        response = llm.generate(request)
        latency = time.time() - start_time
        
        # Log to Langfuse
        langfuse.trace(
            input=request,
            output=response,
            latency=latency,
            tokens_used=response.tokens,
        )
        
        span.set_attribute("latency", latency)
        span.set_attribute("tokens", response.tokens)
        
        return response
```

---

### 14. "No Cost Controls"

**Problem**: Unlimited API usage without budgets or alerts.

```python
# ANTI-PATTERN: No cost controls
class UnlimitedAgent:
    def process(self, requests):
        for request in requests:
            # No limit on API calls!
            self.llm.generate(request)  # Could spend $10K!
```

**Impact**:
- Cost overruns
- Budget surprises
- Service denial

**Solution**: Cost controls and monitoring.

```python
# PATTERN: Cost-controlled
class CostControlledAgent:
    def __init__(self):
        self.daily_budget = 100  # USD
        self.spent_today = 0
    
    def process(self, requests):
        for request in requests:
            if self.spent_today >= self.daily_budget:
                raise BudgetExceededError("Daily budget exhausted")
            
            response = self.llm.generate(request)
            self.spent_today += response.cost
            
            if self.spent_today > self.daily_budget * 0.8:
                self.alert("Approaching budget limit")
```

---

### 15. "No Fallback Strategy"

**Problem**: Single point of failure with no backup.

```python
# ANTI-PATTERN: No fallback
def generate_with_claude(prompt):
    return claude.generate(prompt)  # If Claude fails, we're dead!
```

**Impact**:
- Complete service outage
- Poor reliability
- User frustration

**Solution**: Cascading fallback.

```python
# PATTERN: Cascading fallback
MODELS = [
    ("claude-3-5-sonnet", priority=1),
    ("gpt-4o", priority=2),
    ("claude-3-haiku", priority=3),
]

def generate_with_fallback(prompt):
    for model_name, _ in sorted(MODELS, key=lambda x: x[1]):
        try:
            model = get_model(model_name)
            return model.generate(prompt)
        except Exception as e:
            logger.warning(f"{model_name} failed: {e}")
            continue
    
    raise AllModelsFailedError("All models exhausted")
```

---

## Human Interaction Anti-Patterns

### 16. "Opaque AI Decisions"

**Problem**: AI makes decisions without explaining why.

```python
# ANTI-PATTERN: No explanation
agent = CodeReviewAgent()
result = agent.review(code)
# Result: "REJECTED"
# Why? No explanation provided!
```

**Impact**:
- User distrust
- Can't learn from mistakes
- Poor adoption

**Solution**: Explainable AI.

```python
# PATTERN: Explainable decisions
agent = CodeReviewAgent()
result = agent.review(code)

# Result with explanation
{
    "decision": "REJECTED",
    "confidence": 0.92,
    "reasoning": [
        "Line 45: Potential SQL injection",
        "Line 67: No input validation",
        "Line 89: Hardcoded secret"
    ],
    "suggestions": [
        "Use parameterized queries",
        "Add input validation",
        "Move secrets to environment"
    ]
}
```

---

### 17. "All-or-Nothing Automation"

**Problem**: No human oversight for critical decisions.

```python
# ANTI-PATTERN: Full automation
def deploy_to_production(code):
    tests_pass = run_tests(code)
    if tests_pass:
        deploy(code)  # No human review!
```

**Impact**:
- Production incidents
- Undetected bugs
- Compliance violations

**Solution**: Human-in-the-loop.

```python
# PATTERN: Human oversight
def deploy_to_production(code):
    tests_pass = run_tests(code)
    if not tests_pass:
        return "Tests failed"
    
    security_scan = scan(code)
    if security_scan.critical_issues:
        return "Security issues found"
    
    # Human approval required
    approval = request_human_approval(
        code=code,
        test_results=tests_pass,
        security_scan=security_scan,
    )
    
    if approval.granted:
        deploy(code)
    else:
        return f"Deployment rejected: {approval.reason}"
```

---

### 18. "False Confidence"

**Problem**: Presenting uncertain results as certain.

```python
# ANTI-PATTERN: False confidence
result = agent.analyze(code)
return {
    "answer": result.answer,  # No confidence indicator!
    "action": "deploy"
}
```

**Impact**:
- Wrong decisions
- Over-reliance on AI
- Missed edge cases

**Solution**: Confidence transparency.

```python
# PATTERN: Confidence transparency
result = agent.analyze(code)
return {
    "answer": result.answer,
    "confidence": result.confidence,  # 0.0 - 1.0
    "confidence_level": "high" if result.confidence > 0.9 else "medium" if result.confidence > 0.7 else "low",
    "uncertainty_areas": result.uncertain_parts,
    "recommended_action": "deploy" if result.confidence > 0.9 else "review"
}
```

---

## Quick Reference: Anti-Pattern Checklist

### Before Deployment

- [ ] No "God Agents" - responsibilities are distributed
- [ ] Agents communicate efficiently (not chatty)
- [ ] Gradual rollout plan exists
- [ ] Input validation implemented
- [ ] Output verification in place
- [ ] Temperature appropriate for task
- [ ] Context retrieval is intelligent
- [ ] Caching is implemented
- [ ] Context size is dynamic
- [ ] Secrets are never in prompts
- [ ] Output filtering enabled
- [ ] Permissions are minimal
- [ ] Observability configured
- [ ] Cost controls set
- [ ] Fallback strategy defined
- [ ] Decisions are explainable
- [ ] Human oversight configured
- [ ] Confidence is transparent

### Monitoring Checklist

- [ ] Error rates within SLO
- [ ] Latency within targets
- [ ] Costs within budget
- [ ] Hallucination rate tracked
- [ ] Human override rate monitored
- [ ] Cache hit rate acceptable
- [ ] Fallback usage tracked

---

## Related Resources

- [Best Practices](./BEST_PRACTICES.md) - What to do
- [Security Hardening](./SECURITY_HARDENING.md) - Security specifics
- [Troubleshooting Guide](./TROUBLESHOOTING_GUIDE.md) - Problem solving
- [Case Studies](./CASE_STUDIES.md) - Real-world lessons

---

*Anti-patterns are learned from production failures. Share your experiences to help others avoid the same mistakes.*
