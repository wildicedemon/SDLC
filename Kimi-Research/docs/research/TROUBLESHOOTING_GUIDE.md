# Troubleshooting Guide

Common issues and solutions for autonomous AI coding systems.

## Issue Categories

### 1. Performance Issues

#### High Latency

**Symptoms**: Responses taking longer than expected

**Diagnosis Steps**:
1. Check current latency metrics (p50, p95, p99)
2. Review context size being sent
3. Check model being used
4. Analyze infrastructure metrics

**Common Causes & Solutions**:

| Cause | Solution |
|-------|----------|
| Large context | Enable compression, use RAG |
| Wrong model | Implement model routing |
| Cold start | Use pre-warmed instances |
| Resource limits | Scale up or optimize |
| Network latency | Check connectivity, use CDN |

**Quick Fix**:
```python
# Check context size
if len(context) > 10000:
    context = compress_context(context)

# Use faster model for simple queries
if complexity < 0.3:
    model = "gpt-3.5-turbo"
```

#### Low Throughput

**Symptoms**: System can't handle load

**Diagnosis Steps**:
1. Check concurrent request count
2. Review resource utilization
3. Analyze queue depth
4. Check for bottlenecks

**Solutions**:
- Implement request batching
- Add caching layer
- Scale horizontally
- Optimize database queries

### 2. Quality Issues

#### Hallucinations

**Symptoms**: AI generating incorrect or nonsensical content

**Diagnosis Steps**:
1. Measure hallucination rate
2. Review prompt quality
3. Check context relevance
4. Analyze model confidence

**Solutions**:

| Approach | Implementation |
|----------|----------------|
| Multi-agent verification | Have multiple agents review |
| Self-consistency | Generate multiple answers, compare |
| RAG grounding | Use retrieved context |
| Human review | Add approval for critical code |
| AST validation | Validate generated code |

**Example**:
```python
# Multi-agent verification
responses = []
for _ in range(3):
    responses.append(agent.generate(prompt))

# Check consistency
if len(set(responses)) == 1:
    return responses[0]  # All agree
else:
    return human_review(responses)  # Escalate
```

#### Incorrect Logic

**Symptoms**: Code compiles but doesn't work correctly

**Solutions**:
- Add more examples to prompt
- Improve test coverage
- Implement property-based testing
- Add runtime assertions

### 3. Cost Issues

#### Unexpected Cost Spikes

**Symptoms**: Costs significantly higher than expected

**Diagnosis Steps**:
1. Check daily spend vs budget
2. Analyze model distribution
3. Review token usage patterns
4. Check for abuse/loops

**Common Causes**:

| Cause | Solution |
|-------|----------|
| Wrong model used | Implement routing |
| No caching | Enable semantic caching |
| Infinite loops | Add iteration limits |
| Large contexts | Compress or use RAG |
| Token waste | Optimize prompts |

**Quick Fix**:
```python
# Add cost tracking
@track_cost
async def generate(prompt):
    response = await llm.generate(prompt)
    return response

# Set limits
MAX_TOKENS = 4000
if estimate_tokens(prompt) > MAX_TOKENS:
    prompt = compress_prompt(prompt)
```

### 4. Integration Issues

#### API Errors

**Symptoms**: External API calls failing

**Common Errors**:

| Error | Cause | Solution |
|-------|-------|----------|
| 429 Rate Limit | Too many requests | Implement backoff |
| 500 Server Error | Provider issue | Add retry logic |
| 401 Unauthorized | Invalid key | Check credentials |
| 408 Timeout | Request too long | Reduce context |

**Retry Logic**:
```python
import backoff

@backoff.on_exception(
    backoff.expo,
    (RateLimitError, ServiceUnavailableError),
    max_tries=5
)
async def call_with_retry(prompt):
    return await llm.generate(prompt)
```

#### Tool Execution Failures

**Symptoms**: Tools failing to execute

**Solutions**:
- Check tool permissions
- Verify tool availability
- Add timeout handling
- Implement fallback tools

### 5. Memory Issues

#### Out of Memory

**Symptoms**: System running out of memory

**Causes**:
- Large context windows
- Memory leaks
- Insufficient resources
- Unbounded caches

**Solutions**:
```python
# Limit context size
MAX_CONTEXT = 10000
context = context[:MAX_CONTEXT]

# Clear caches periodically
def clear_expired_cache():
    for key, value in list(cache.items()):
        if is_expired(value):
            del cache[key]

# Use streaming for large responses
async for chunk in llm.generate_stream(prompt):
    yield chunk
```

### 6. Context Issues

#### Context Not Found

**Symptoms**: RAG not retrieving relevant context

**Solutions**:
- Check embedding model
- Verify index is up to date
- Adjust similarity threshold
- Improve chunking strategy

**Debug Query**:
```python
# Test retrieval
query_embedding = embed(query)
results = vector_db.search(query_embedding, top_k=5)

print(f"Query: {query}")
print(f"Top results:")
for i, result in enumerate(results):
    print(f"  {i+1}. Score: {result.score}")
    print(f"     Content: {result.content[:100]}...")
```

#### Context Too Large

**Symptoms**: Context exceeding token limits

**Solutions**:
- Implement compression
- Use summarization
- Select most relevant chunks
- Increase token budget

### 7. Security Issues

#### Suspicious Activity

**Symptoms**: Unusual patterns detected

**Checks**:
- Review access logs
- Check for prompt injection attempts
- Monitor for data exfiltration
- Verify tool permissions

**Response**:
1. Isolate affected systems
2. Review audit logs
3. Reset compromised credentials
4. Update security rules

### 8. Deployment Issues

#### Failed Deployments

**Symptoms**: New version not working

**Troubleshooting**:
1. Check deployment logs
2. Verify configuration
3. Test in staging
4. Review resource limits

**Rollback**:
```bash
# Kubernetes rollback
kubectl rollout undo deployment/ai-agent

# Check rollout status
kubectl rollout status deployment/ai-agent
```

## Debugging Tools

### Log Analysis

```bash
# View recent logs
kubectl logs -l app=ai-agent --tail=100

# Follow logs
kubectl logs -l app=ai-agent -f

# Search for errors
kubectl logs -l app=ai-agent | grep ERROR

# View specific pod
kubectl logs ai-agent-pod-123
```

### Metrics Inspection

```bash
# Check Prometheus metrics
curl http://prometheus:9090/api/v1/query?query=request_latency_seconds

# View Grafana dashboard
open http://grafana:3000/d/ai-agent-dashboard
```

### Tracing

```python
# Enable tracing
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("generate_code") as span:
    span.set_attribute("model", "gpt-4")
    span.set_attribute("tokens", 150)
    result = await generate(prompt)
```

## Common Error Messages

### LLM API Errors

| Error | Meaning | Solution |
|-------|---------|----------|
| `context_length_exceeded` | Too many tokens | Reduce context |
| `rate_limit_exceeded` | Too many requests | Add backoff |
| `invalid_api_key` | Authentication failed | Check key |
| `server_error` | Provider issue | Retry |

### Container Errors

| Error | Meaning | Solution |
|-------|---------|----------|
| `OOMKilled` | Out of memory | Increase limits |
| `CrashLoopBackOff` | Repeated crashes | Check logs |
| `ImagePullBackOff` | Can't pull image | Check registry |
| `Pending` | Can't schedule | Check resources |

### Database Errors

| Error | Meaning | Solution |
|-------|---------|----------|
| `Connection refused` | DB unavailable | Check service |
| `Timeout` | Query too slow | Optimize query |
| `Deadlock` | Concurrent access | Retry transaction |

## Diagnostic Commands

### System Health

```bash
# Check pod status
kubectl get pods -l app=ai-agent

# Check resource usage
kubectl top pods -l app=ai-agent

# Check events
kubectl get events --sort-by=.lastTimestamp

# Check services
kubectl get svc -l app=ai-agent
```

### Network Diagnostics

```bash
# Test connectivity
kubectl exec -it ai-agent-pod -- ping google.com

# Check DNS
kubectl exec -it ai-agent-pod -- nslookup kubernetes.default

# Test API endpoint
curl -v https://api.openai.com/v1/models   -H "Authorization: Bearer $API_KEY"
```

### Performance Testing

```bash
# Load test
ab -n 1000 -c 10 http://ai-agent-service/generate

# Profile Python
python -m cProfile -o profile.stats app.py

# Memory profiling
python -m memory_profiler app.py
```

## Recovery Procedures

### Service Restart

```bash
# Rolling restart
kubectl rollout restart deployment/ai-agent

# Scale to zero and back
kubectl scale deployment ai-agent --replicas=0
kubectl scale deployment ai-agent --replicas=3
```

### Cache Clear

```bash
# Clear Redis cache
redis-cli FLUSHDB

# Clear vector DB index
python -c "from vector_db import clear_index; clear_index()"
```

### Configuration Reload

```bash
# Update ConfigMap
kubectl apply -f configmap.yaml

# Rollout to apply
kubectl rollout restart deployment/ai-agent
```

## Getting Help

### Internal Resources
1. Check runbooks
2. Review incident history
3. Consult team members
4. Check documentation

### External Resources
1. Vendor documentation
2. Community forums
3. GitHub issues
4. Stack Overflow

### Escalation Path
1. L1: On-call engineer
2. L2: Team lead
3. L3: Architecture team
4. L4: Vendor support

## Prevention

### Proactive Monitoring
- Set up comprehensive alerts
- Monitor key metrics
- Review logs regularly
- Track error trends

### Testing
- Unit tests
- Integration tests
- Load tests
- Chaos engineering

### Documentation
- Update runbooks
- Document fixes
- Share learnings
- Train team

---

*When in doubt, check logs, measure metrics, and isolate variables.*
