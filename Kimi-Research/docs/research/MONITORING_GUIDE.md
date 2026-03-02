# Monitoring and Alerting Guide

Comprehensive guide for monitoring autonomous AI coding systems.

## Monitoring Philosophy

### Key Principles
1. **Monitor what matters**: Focus on metrics that indicate system health and user value
2. **Alert on symptoms, not causes**: Alert when user experience degrades
3. **Actionable alerts**: Every alert should have a clear response
4. **Progressive disclosure**: Start with high-level metrics, drill down as needed

### The Three Pillars
1. **Metrics**: Numerical data over time
2. **Logs**: Detailed event records
3. **Traces**: Request flow visualization

## Metric Categories

### 1. Technical Metrics

#### Latency
| Metric | Description | Target |
|--------|-------------|--------|
| p50 Latency | Median response time | < 500ms |
| p95 Latency | 95th percentile | < 2s |
| p99 Latency | 99th percentile | < 5s |
| Time to First Token | Streaming start | < 200ms |

**Dashboard Query**:
```promql
histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m]))
```

#### Throughput
| Metric | Description | Target |
|--------|-------------|--------|
| Requests/sec | Total requests | Baseline + 20% |
| Tokens/sec | Processing rate | Monitor trend |
| Concurrent Requests | Active requests | < 80% capacity |

**Dashboard Query**:
```promql
rate(requests_total[1m])
```

#### Error Rates
| Metric | Description | Target |
|--------|-------------|--------|
| Error Rate % | Failed requests | < 1% |
| 5xx Errors | Server errors | < 0.1% |
| Timeout Rate | Timed out requests | < 0.5% |

**Dashboard Query**:
```promql
rate(errors_total[5m]) / rate(requests_total[5m]) * 100
```

#### Resource Utilization
| Metric | Description | Target |
|--------|-------------|--------|
| CPU Usage | Processor utilization | < 70% |
| Memory Usage | RAM utilization | < 80% |
| GPU Utilization | GPU usage | < 90% |
| Disk I/O | Storage operations | < 50% capacity |

### 2. Business Metrics

#### Cost Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Cost per Request | Average cost | Trend down |
| Cost per Token | Token efficiency | Trend down |
| Daily Spend | Total daily cost | Within budget |
| Model Distribution | Usage by model | Optimize mix |

**Dashboard Query**:
```promql
sum(cost_dollars) by (model)
```

#### Usage Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Daily Active Users | Unique users/day | Growth |
| Requests per User | Average usage | Engagement |
| Feature Adoption | Feature usage | > 50% |
| Session Duration | Time per session | Engagement |

### 3. Quality Metrics

#### Semantic Quality
| Metric | Description | Target |
|--------|-------------|--------|
| Hallucination Rate | Incorrect outputs | < 5% |
| Factual Correctness | Accuracy score | > 90% |
| Topic Relevancy | Relevance score | > 85% |
| User Satisfaction | Rating | > 4.0/5 |

**Measurement**:
```python
# LLM-as-judge evaluation
def evaluate_quality(output, expected):
    prompt = f"Rate the quality of: {output}
Expected: {expected}"
    score = llm.generate(prompt)
    return parse_score(score)
```

#### Code Quality (for code generation)
| Metric | Description | Target |
|--------|-------------|--------|
| Compilation Success | Code compiles | > 95% |
| Test Pass Rate | Generated tests pass | > 80% |
| Security Issues | Vulnerabilities | 0 critical |
| Style Compliance | Follows guidelines | > 90% |

### 4. Agent-Specific Metrics

#### Agent Performance
| Metric | Description | Target |
|--------|-------------|--------|
| Task Completion Rate | Successful tasks | > 90% |
| Average Steps per Task | Efficiency | Minimize |
| Tool Call Success | Tool execution | > 95% |
| Context Utilization | Token efficiency | > 70% |

#### Multi-Agent Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Coordination Success | Successful handoffs | > 95% |
| Conflict Rate | Agent conflicts | < 1% |
| Consensus Time | Decision time | < 5s |
| Message Volume | Inter-agent traffic | Monitor |

## Alerting Strategy

### Alert Severity Levels

#### P0 - Critical (Immediate Response)
**Conditions**:
- Error rate > 5%
- p99 latency > 10s
- System unavailable
- Security incident

**Response Time**: < 15 minutes
**Escalation**: Page on-call engineer

**Example**:
```yaml
alert: HighErrorRate
expr: rate(errors_total[5m]) / rate(requests_total[5m]) > 0.05
for: 2m
labels:
  severity: critical
annotations:
  summary: "Error rate is {{ $value }}%"
  runbook_url: "https://wiki/runbooks/high-error-rate"
```

#### P1 - High (Urgent Response)
**Conditions**:
- Error rate > 1%
- p95 latency > 5s
- Resource usage > 90%
- Cost spike > 200%

**Response Time**: < 1 hour
**Escalation**: Notify team channel

**Example**:
```yaml
alert: ElevatedLatency
expr: histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m])) > 5
for: 5m
labels:
  severity: high
annotations:
  summary: "p95 latency is {{ $value }}s"
```

#### P2 - Medium (Standard Response)
**Conditions**:
- Error rate > 0.5%
- p50 latency > 1s
- Resource usage > 80%
- Cost variance > 50%

**Response Time**: < 4 hours
**Escalation**: Create ticket

#### P3 - Low (Planned Response)
**Conditions**:
- Minor performance degradation
- Non-critical issues
- Enhancement opportunities

**Response Time**: < 1 week
**Escalation**: Backlog item

### Alert Best Practices

#### Do
- [ ] Include runbook links
- [ ] Provide context in alert
- [ ] Set appropriate thresholds
- [ ] Test alert routing
- [ ] Regular alert review

#### Don't
- [ ] Alert on causes (alert on symptoms)
- [ ] Create alert fatigue
- [ ] Set static thresholds without context
- [ ] Ignore false positives
- [ ] Forget to update runbooks

## Dashboard Design

### Executive Dashboard
**Audience**: Leadership, stakeholders

**Metrics**:
- System availability (SLA)
- Cost trends
- User adoption
- Key incidents

**Layout**:
```
┌─────────────────────────────────────────┐
│  Availability    Cost Trend    Users   │
│    99.9%         ↓ 15%        ↑ 25%    │
├─────────────────────────────────────────┤
│         Incidents (Last 30 Days)        │
│  P0: 0    P1: 2    P2: 5    P3: 12     │
└─────────────────────────────────────────┘
```

### Engineering Dashboard
**Audience**: Engineering team

**Metrics**:
- Latency percentiles
- Error rates
- Throughput
- Resource utilization

**Layout**:
```
┌─────────────────────────────────────────┐
│  Latency (p50/p95/p99)   Error Rate    │
│  200ms / 800ms / 2s        0.5%        │
├─────────────────────────────────────────┤
│  Requests/sec    CPU    Memory    GPU   │
│    150           45%     60%      70%   │
└─────────────────────────────────────────┘
```

### AI-Specific Dashboard
**Audience**: ML/AI team

**Metrics**:
- Hallucination rate
- Token efficiency
- Model distribution
- Quality scores

**Layout**:
```
┌─────────────────────────────────────────┐
│  Hallucination    Token Eff.   Quality │
│     3.2%           72%          4.2/5  │
├─────────────────────────────────────────┤
│         Model Usage Distribution        │
│  GPT-4: 20%  GPT-3.5: 60%  Claude: 20% │
└─────────────────────────────────────────┘
```

### Cost Dashboard
**Audience**: Finance, engineering

**Metrics**:
- Daily spend
- Cost per request
- Model costs
- Budget variance

**Layout**:
```
┌─────────────────────────────────────────┐
│  Daily Spend    Cost/Request   Budget   │
│   $450            $0.03        85%      │
├─────────────────────────────────────────┤
│           Cost by Model ($/day)         │
│  GPT-4: $200  GPT-3.5: $150  Other: $100│
└─────────────────────────────────────────┘
```

## Log Management

### Log Levels
| Level | Use Case | Retention |
|-------|----------|-----------|
| DEBUG | Development troubleshooting | 7 days |
| INFO | Normal operations | 30 days |
| WARN | Issues requiring attention | 90 days |
| ERROR | Errors requiring investigation | 1 year |
| CRITICAL | System failures | 1 year |

### Structured Logging
```json
{
  "timestamp": "2025-01-21T10:30:00Z",
  "level": "INFO",
  "service": "ai-agent",
  "trace_id": "abc-123",
  "user_id": "user-456",
  "event": "code_generated",
  "model": "gpt-4",
  "tokens": 150,
  "latency_ms": 1200,
  "success": true
}
```

### Log Analysis Queries
```sql
-- Error analysis
SELECT error_type, COUNT(*) 
FROM logs 
WHERE level = 'ERROR' 
  AND timestamp > NOW() - INTERVAL '1 hour'
GROUP BY error_type;

-- Slow requests
SELECT trace_id, latency_ms 
FROM logs 
WHERE latency_ms > 5000 
  AND timestamp > NOW() - INTERVAL '1 hour';
```

## Distributed Tracing

### Trace Structure
```
Trace: request-123
├── Span: api-gateway (100ms)
├── Span: auth-service (50ms)
├── Span: ai-agent (2000ms)
│   ├── Span: context-retrieval (500ms)
│   ├── Span: llm-call (1200ms)
│   └── Span: post-processing (300ms)
└── Span: response-formatting (100ms)
```

### Key Spans to Trace
- API gateway entry
- Authentication
- Context retrieval
- LLM calls
- Tool executions
- Response formatting

## SLOs and SLIs

### Service Level Indicators (SLIs)
| SLI | Definition | Measurement |
|-----|------------|-------------|
| Availability | % of successful requests | (total - errors) / total |
| Latency | Response time | p95 over 1 minute |
| Quality | Output correctness | Human/AI evaluation |
| Cost | $ per request | Total cost / requests |

### Service Level Objectives (SLOs)
| SLO | Target | Error Budget |
|-----|--------|--------------|
| Availability | 99.9% | 0.1% (43 min/month) |
| Latency p95 | < 2s | 5% of requests |
| Quality Score | > 4.0/5 | 10% of outputs |
| Cost per Request | <$0.05 | 20% variance |

### Error Budget Policy
```
Error Budget = 100% - SLO

If error budget exhausted:
1. Halt feature releases
2. Focus on reliability
3. Review and improve
4. Reset budget next period
```

## Incident Response

### Incident Severity
| Level | Description | Response |
|-------|-------------|----------|
| SEV1 | Complete outage | All hands |
| SEV2 | Major degradation | On-call + team |
| SEV3 | Minor issues | On-call |
| SEV4 | Low impact | Ticket |

### Response Runbook
1. **Detect**: Alert fires
2. **Acknowledge**: Claim the incident
3. **Assess**: Determine severity
4. **Mitigate**: Stop the bleeding
5. **Fix**: Root cause resolution
6. **Verify**: Confirm resolution
7. **Document**: Post-mortem

## Monitoring Tools

### Recommended Stack
| Layer | Tool | Purpose |
|-------|------|---------|
| Metrics | Prometheus | Time-series data |
| Visualization | Grafana | Dashboards |
| Logs | ELK / Loki | Log aggregation |
| Tracing | Jaeger / Zipkin | Distributed traces |
| Alerting | PagerDuty / Opsgenie | Incident management |
| APM | Datadog / New Relic | Full observability |

### Open Source Alternative
- Metrics: Prometheus + Grafana
- Logs: Loki + Grafana
- Tracing: Jaeger
- Alerting: Alertmanager

## Monitoring Checklist

### Setup
- [ ] Metrics collection configured
- [ ] Dashboards created
- [ ] Alerts defined
- [ ] Runbooks written
- [ ] On-call rotation set

### Validation
- [ ] Test alerts fire correctly
- [ ] Verify dashboard accuracy
- [ ] Confirm log aggregation
- [ ] Test trace collection
- [ ] Validate SLOs

### Maintenance
- [ ] Weekly alert review
- [ ] Monthly dashboard updates
- [ ] Quarterly SLO review
- [ ] Annual monitoring audit

---

*Effective monitoring is essential for operating AI coding systems at scale. Start with the basics and iterate based on operational experience.*

# Monitoring and Alerting Guide

Comprehensive guide for monitoring autonomous AI coding systems.

## Monitoring Philosophy

### Key Principles
1. **Monitor what matters**: Focus on metrics that indicate system health and user value
2. **Alert on symptoms, not causes**: Alert when user experience degrades
3. **Actionable alerts**: Every alert should have a clear response
4. **Progressive disclosure**: Start with high-level metrics, drill down as needed

### The Three Pillars
1. **Metrics**: Numerical data over time
2. **Logs**: Detailed event records
3. **Traces**: Request flow visualization

## Metric Categories

### 1. Technical Metrics

#### Latency
| Metric | Description | Target |
|--------|-------------|--------|
| p50 Latency | Median response time | < 500ms |
| p95 Latency | 95th percentile | < 2s |
| p99 Latency | 99th percentile | < 5s |
| Time to First Token | Streaming start | < 200ms |

**Dashboard Query**:
```promql
histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m]))
```

#### Throughput
| Metric | Description | Target |
|--------|-------------|--------|
| Requests/sec | Total requests | Baseline + 20% |
| Tokens/sec | Processing rate | Monitor trend |
| Concurrent Requests | Active requests | < 80% capacity |

**Dashboard Query**:
```promql
rate(requests_total[1m])
```

#### Error Rates
| Metric | Description | Target |
|--------|-------------|--------|
| Error Rate % | Failed requests | < 1% |
| 5xx Errors | Server errors | < 0.1% |
| Timeout Rate | Timed out requests | < 0.5% |

**Dashboard Query**:
```promql
rate(errors_total[5m]) / rate(requests_total[5m]) * 100
```

#### Resource Utilization
| Metric | Description | Target |
|--------|-------------|--------|
| CPU Usage | Processor utilization | < 70% |
| Memory Usage | RAM utilization | < 80% |
| GPU Utilization | GPU usage | < 90% |
| Disk I/O | Storage operations | < 50% capacity |

### 2. Business Metrics

#### Cost Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Cost per Request | Average cost | Trend down |
| Cost per Token | Token efficiency | Trend down |
| Daily Spend | Total daily cost | Within budget |
| Model Distribution | Usage by model | Optimize mix |

**Dashboard Query**:
```promql
sum(cost_dollars) by (model)
```

#### Usage Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Daily Active Users | Unique users/day | Growth |
| Requests per User | Average usage | Engagement |
| Feature Adoption | Feature usage | > 50% |
| Session Duration | Time per session | Engagement |

### 3. Quality Metrics

#### Semantic Quality
| Metric | Description | Target |
|--------|-------------|--------|
| Hallucination Rate | Incorrect outputs | < 5% |
| Factual Correctness | Accuracy score | > 90% |
| Topic Relevancy | Relevance score | > 85% |
| User Satisfaction | Rating | > 4.0/5 |

**Measurement**:
```python
# LLM-as-judge evaluation
def evaluate_quality(output, expected):
    prompt = f"Rate the quality of: {output}
Expected: {expected}"
    score = llm.generate(prompt)
    return parse_score(score)
```

#### Code Quality (for code generation)
| Metric | Description | Target |
|--------|-------------|--------|
| Compilation Success | Code compiles | > 95% |
| Test Pass Rate | Generated tests pass | > 80% |
| Security Issues | Vulnerabilities | 0 critical |
| Style Compliance | Follows guidelines | > 90% |

### 4. Agent-Specific Metrics

#### Agent Performance
| Metric | Description | Target |
|--------|-------------|--------|
| Task Completion Rate | Successful tasks | > 90% |
| Average Steps per Task | Efficiency | Minimize |
| Tool Call Success | Tool execution | > 95% |
| Context Utilization | Token efficiency | > 70% |

#### Multi-Agent Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Coordination Success | Successful handoffs | > 95% |
| Conflict Rate | Agent conflicts | < 1% |
| Consensus Time | Decision time | < 5s |
| Message Volume | Inter-agent traffic | Monitor |

## Alerting Strategy

### Alert Severity Levels

#### P0 - Critical (Immediate Response)
**Conditions**:
- Error rate > 5%
- p99 latency > 10s
- System unavailable
- Security incident

**Response Time**: < 15 minutes
**Escalation**: Page on-call engineer

**Example**:
```yaml
alert: HighErrorRate
expr: rate(errors_total[5m]) / rate(requests_total[5m]) > 0.05
for: 2m
labels:
  severity: critical
annotations:
  summary: "Error rate is {{ $value }}%"
  runbook_url: "https://wiki/runbooks/high-error-rate"
```

#### P1 - High (Urgent Response)
**Conditions**:
- Error rate > 1%
- p95 latency > 5s
- Resource usage > 90%
- Cost spike > 200%

**Response Time**: < 1 hour
**Escalation**: Notify team channel

**Example**:
```yaml
alert: ElevatedLatency
expr: histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m])) > 5
for: 5m
labels:
  severity: high
annotations:
  summary: "p95 latency is {{ $value }}s"
```

#### P2 - Medium (Standard Response)
**Conditions**:
- Error rate > 0.5%
- p50 latency > 1s
- Resource usage > 80%
- Cost variance > 50%

**Response Time**: < 4 hours
**Escalation**: Create ticket

#### P3 - Low (Planned Response)
**Conditions**:
- Minor performance degradation
- Non-critical issues
- Enhancement opportunities

**Response Time**: < 1 week
**Escalation**: Backlog item

### Alert Best Practices

#### Do
- [ ] Include runbook links
- [ ] Provide context in alert
- [ ] Set appropriate thresholds
- [ ] Test alert routing
- [ ] Regular alert review

#### Don't
- [ ] Alert on causes (alert on symptoms)
- [ ] Create alert fatigue
- [ ] Set static thresholds without context
- [ ] Ignore false positives
- [ ] Forget to update runbooks

## Dashboard Design

### Executive Dashboard
**Audience**: Leadership, stakeholders

**Metrics**:
- System availability (SLA)
- Cost trends
- User adoption
- Key incidents

**Layout**:
```
┌─────────────────────────────────────────┐
│  Availability    Cost Trend    Users   │
│    99.9%         ↓ 15%        ↑ 25%    │
├─────────────────────────────────────────┤
│         Incidents (Last 30 Days)        │
│  P0: 0    P1: 2    P2: 5    P3: 12     │
└─────────────────────────────────────────┘
```

### Engineering Dashboard
**Audience**: Engineering team

**Metrics**:
- Latency percentiles
- Error rates
- Throughput
- Resource utilization

**Layout**:
```
┌─────────────────────────────────────────┐
│  Latency (p50/p95/p99)   Error Rate    │
│  200ms / 800ms / 2s        0.5%        │
├─────────────────────────────────────────┤
│  Requests/sec    CPU    Memory    GPU   │
│    150           45%     60%      70%   │
└─────────────────────────────────────────┘
```

### AI-Specific Dashboard
**Audience**: ML/AI team

**Metrics**:
- Hallucination rate
- Token efficiency
- Model distribution
- Quality scores

**Layout**:
```
┌─────────────────────────────────────────┐
│  Hallucination    Token Eff.   Quality │
│     3.2%           72%          4.2/5  │
├─────────────────────────────────────────┤
│         Model Usage Distribution        │
│  GPT-4: 20%  GPT-3.5: 60%  Claude: 20% │
└─────────────────────────────────────────┘
```

### Cost Dashboard
**Audience**: Finance, engineering

**Metrics**:
- Daily spend
- Cost per request
- Model costs
- Budget variance

**Layout**:
```
┌─────────────────────────────────────────┐
│  Daily Spend    Cost/Request   Budget   │
│   $450            $0.03        85%      │
├─────────────────────────────────────────┤
│           Cost by Model ($/day)         │
│  GPT-4: $200  GPT-3.5: $150  Other: $100│
└─────────────────────────────────────────┘
```

## Log Management

### Log Levels
| Level | Use Case | Retention |
|-------|----------|-----------|
| DEBUG | Development troubleshooting | 7 days |
| INFO | Normal operations | 30 days |
| WARN | Issues requiring attention | 90 days |
| ERROR | Errors requiring investigation | 1 year |
| CRITICAL | System failures | 1 year |

### Structured Logging
```json
{
  "timestamp": "2025-01-21T10:30:00Z",
  "level": "INFO",
  "service": "ai-agent",
  "trace_id": "abc-123",
  "user_id": "user-456",
  "event": "code_generated",
  "model": "gpt-4",
  "tokens": 150,
  "latency_ms": 1200,
  "success": true
}
```

### Log Analysis Queries
```sql
-- Error analysis
SELECT error_type, COUNT(*) 
FROM logs 
WHERE level = 'ERROR' 
  AND timestamp > NOW() - INTERVAL '1 hour'
GROUP BY error_type;

-- Slow requests
SELECT trace_id, latency_ms 
FROM logs 
WHERE latency_ms > 5000 
  AND timestamp > NOW() - INTERVAL '1 hour';
```

## Distributed Tracing

### Trace Structure
```
Trace: request-123
├── Span: api-gateway (100ms)
├── Span: auth-service (50ms)
├── Span: ai-agent (2000ms)
│   ├── Span: context-retrieval (500ms)
│   ├── Span: llm-call (1200ms)
│   └── Span: post-processing (300ms)
└── Span: response-formatting (100ms)
```

### Key Spans to Trace
- API gateway entry
- Authentication
- Context retrieval
- LLM calls
- Tool executions
- Response formatting

## SLOs and SLIs

### Service Level Indicators (SLIs)
| SLI | Definition | Measurement |
|-----|------------|-------------|
| Availability | % of successful requests | (total - errors) / total |
| Latency | Response time | p95 over 1 minute |
| Quality | Output correctness | Human/AI evaluation |
| Cost | $ per request | Total cost / requests |

### Service Level Objectives (SLOs)
| SLO | Target | Error Budget |
|-----|--------|--------------|
| Availability | 99.9% | 0.1% (43 min/month) |
| Latency p95 | < 2s | 5% of requests |
| Quality Score | > 4.0/5 | 10% of outputs |
| Cost per Request | <$0.05 | 20% variance |

### Error Budget Policy
```
Error Budget = 100% - SLO

If error budget exhausted:
1. Halt feature releases
2. Focus on reliability
3. Review and improve
4. Reset budget next period
```

## Incident Response

### Incident Severity
| Level | Description | Response |
|-------|-------------|----------|
| SEV1 | Complete outage | All hands |
| SEV2 | Major degradation | On-call + team |
| SEV3 | Minor issues | On-call |
| SEV4 | Low impact | Ticket |

### Response Runbook
1. **Detect**: Alert fires
2. **Acknowledge**: Claim the incident
3. **Assess**: Determine severity
4. **Mitigate**: Stop the bleeding
5. **Fix**: Root cause resolution
6. **Verify**: Confirm resolution
7. **Document**: Post-mortem

## Monitoring Tools

### Recommended Stack
| Layer | Tool | Purpose |
|-------|------|---------|
| Metrics | Prometheus | Time-series data |
| Visualization | Grafana | Dashboards |
| Logs | ELK / Loki | Log aggregation |
| Tracing | Jaeger / Zipkin | Distributed traces |
| Alerting | PagerDuty / Opsgenie | Incident management |
| APM | Datadog / New Relic | Full observability |

### Open Source Alternative
- Metrics: Prometheus + Grafana
- Logs: Loki + Grafana
- Tracing: Jaeger
- Alerting: Alertmanager

## Monitoring Checklist

### Setup
- [ ] Metrics collection configured
- [ ] Dashboards created
- [ ] Alerts defined
- [ ] Runbooks written
- [ ] On-call rotation set

### Validation
- [ ] Test alerts fire correctly
- [ ] Verify dashboard accuracy
- [ ] Confirm log aggregation
- [ ] Test trace collection
- [ ] Validate SLOs

### Maintenance
- [ ] Weekly alert review
- [ ] Monthly dashboard updates
- [ ] Quarterly SLO review
- [ ] Annual monitoring audit

---

*Effective monitoring is essential for operating AI coding systems at scale. Start with the basics and iterate based on operational experience.*

# Monitoring and Alerting Guide

Comprehensive guide for monitoring autonomous AI coding systems.

## Monitoring Philosophy

### Key Principles
1. **Monitor what matters**: Focus on metrics that indicate system health and user value
2. **Alert on symptoms, not causes**: Alert when user experience degrades
3. **Actionable alerts**: Every alert should have a clear response
4. **Progressive disclosure**: Start with high-level metrics, drill down as needed

### The Three Pillars
1. **Metrics**: Numerical data over time
2. **Logs**: Detailed event records
3. **Traces**: Request flow visualization

## Metric Categories

### 1. Technical Metrics

#### Latency
| Metric | Description | Target |
|--------|-------------|--------|
| p50 Latency | Median response time | < 500ms |
| p95 Latency | 95th percentile | < 2s |
| p99 Latency | 99th percentile | < 5s |
| Time to First Token | Streaming start | < 200ms |

**Dashboard Query**:
```promql
histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m]))
```

#### Throughput
| Metric | Description | Target |
|--------|-------------|--------|
| Requests/sec | Total requests | Baseline + 20% |
| Tokens/sec | Processing rate | Monitor trend |
| Concurrent Requests | Active requests | < 80% capacity |

**Dashboard Query**:
```promql
rate(requests_total[1m])
```

#### Error Rates
| Metric | Description | Target |
|--------|-------------|--------|
| Error Rate % | Failed requests | < 1% |
| 5xx Errors | Server errors | < 0.1% |
| Timeout Rate | Timed out requests | < 0.5% |

**Dashboard Query**:
```promql
rate(errors_total[5m]) / rate(requests_total[5m]) * 100
```

#### Resource Utilization
| Metric | Description | Target |
|--------|-------------|--------|
| CPU Usage | Processor utilization | < 70% |
| Memory Usage | RAM utilization | < 80% |
| GPU Utilization | GPU usage | < 90% |
| Disk I/O | Storage operations | < 50% capacity |

### 2. Business Metrics

#### Cost Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Cost per Request | Average cost | Trend down |
| Cost per Token | Token efficiency | Trend down |
| Daily Spend | Total daily cost | Within budget |
| Model Distribution | Usage by model | Optimize mix |

**Dashboard Query**:
```promql
sum(cost_dollars) by (model)
```

#### Usage Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Daily Active Users | Unique users/day | Growth |
| Requests per User | Average usage | Engagement |
| Feature Adoption | Feature usage | > 50% |
| Session Duration | Time per session | Engagement |

### 3. Quality Metrics

#### Semantic Quality
| Metric | Description | Target |
|--------|-------------|--------|
| Hallucination Rate | Incorrect outputs | < 5% |
| Factual Correctness | Accuracy score | > 90% |
| Topic Relevancy | Relevance score | > 85% |
| User Satisfaction | Rating | > 4.0/5 |

**Measurement**:
```python
# LLM-as-judge evaluation
def evaluate_quality(output, expected):
    prompt = f"Rate the quality of: {output}
Expected: {expected}"
    score = llm.generate(prompt)
    return parse_score(score)
```

#### Code Quality (for code generation)
| Metric | Description | Target |
|--------|-------------|--------|
| Compilation Success | Code compiles | > 95% |
| Test Pass Rate | Generated tests pass | > 80% |
| Security Issues | Vulnerabilities | 0 critical |
| Style Compliance | Follows guidelines | > 90% |

### 4. Agent-Specific Metrics

#### Agent Performance
| Metric | Description | Target |
|--------|-------------|--------|
| Task Completion Rate | Successful tasks | > 90% |
| Average Steps per Task | Efficiency | Minimize |
| Tool Call Success | Tool execution | > 95% |
| Context Utilization | Token efficiency | > 70% |

#### Multi-Agent Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Coordination Success | Successful handoffs | > 95% |
| Conflict Rate | Agent conflicts | < 1% |
| Consensus Time | Decision time | < 5s |
| Message Volume | Inter-agent traffic | Monitor |

## Alerting Strategy

### Alert Severity Levels

#### P0 - Critical (Immediate Response)
**Conditions**:
- Error rate > 5%
- p99 latency > 10s
- System unavailable
- Security incident

**Response Time**: < 15 minutes
**Escalation**: Page on-call engineer

**Example**:
```yaml
alert: HighErrorRate
expr: rate(errors_total[5m]) / rate(requests_total[5m]) > 0.05
for: 2m
labels:
  severity: critical
annotations:
  summary: "Error rate is {{ $value }}%"
  runbook_url: "https://wiki/runbooks/high-error-rate"
```

#### P1 - High (Urgent Response)
**Conditions**:
- Error rate > 1%
- p95 latency > 5s
- Resource usage > 90%
- Cost spike > 200%

**Response Time**: < 1 hour
**Escalation**: Notify team channel

**Example**:
```yaml
alert: ElevatedLatency
expr: histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m])) > 5
for: 5m
labels:
  severity: high
annotations:
  summary: "p95 latency is {{ $value }}s"
```

#### P2 - Medium (Standard Response)
**Conditions**:
- Error rate > 0.5%
- p50 latency > 1s
- Resource usage > 80%
- Cost variance > 50%

**Response Time**: < 4 hours
**Escalation**: Create ticket

#### P3 - Low (Planned Response)
**Conditions**:
- Minor performance degradation
- Non-critical issues
- Enhancement opportunities

**Response Time**: < 1 week
**Escalation**: Backlog item

### Alert Best Practices

#### Do
- [ ] Include runbook links
- [ ] Provide context in alert
- [ ] Set appropriate thresholds
- [ ] Test alert routing
- [ ] Regular alert review

#### Don't
- [ ] Alert on causes (alert on symptoms)
- [ ] Create alert fatigue
- [ ] Set static thresholds without context
- [ ] Ignore false positives
- [ ] Forget to update runbooks

## Dashboard Design

### Executive Dashboard
**Audience**: Leadership, stakeholders

**Metrics**:
- System availability (SLA)
- Cost trends
- User adoption
- Key incidents

**Layout**:
```
┌─────────────────────────────────────────┐
│  Availability    Cost Trend    Users   │
│    99.9%         ↓ 15%        ↑ 25%    │
├─────────────────────────────────────────┤
│         Incidents (Last 30 Days)        │
│  P0: 0    P1: 2    P2: 5    P3: 12     │
└─────────────────────────────────────────┘
```

### Engineering Dashboard
**Audience**: Engineering team

**Metrics**:
- Latency percentiles
- Error rates
- Throughput
- Resource utilization

**Layout**:
```
┌─────────────────────────────────────────┐
│  Latency (p50/p95/p99)   Error Rate    │
│  200ms / 800ms / 2s        0.5%        │
├─────────────────────────────────────────┤
│  Requests/sec    CPU    Memory    GPU   │
│    150           45%     60%      70%   │
└─────────────────────────────────────────┘
```

### AI-Specific Dashboard
**Audience**: ML/AI team

**Metrics**:
- Hallucination rate
- Token efficiency
- Model distribution
- Quality scores

**Layout**:
```
┌─────────────────────────────────────────┐
│  Hallucination    Token Eff.   Quality │
│     3.2%           72%          4.2/5  │
├─────────────────────────────────────────┤
│         Model Usage Distribution        │
│  GPT-4: 20%  GPT-3.5: 60%  Claude: 20% │
└─────────────────────────────────────────┘
```

### Cost Dashboard
**Audience**: Finance, engineering

**Metrics**:
- Daily spend
- Cost per request
- Model costs
- Budget variance

**Layout**:
```
┌─────────────────────────────────────────┐
│  Daily Spend    Cost/Request   Budget   │
│   $450            $0.03        85%      │
├─────────────────────────────────────────┤
│           Cost by Model ($/day)         │
│  GPT-4: $200  GPT-3.5: $150  Other: $100│
└─────────────────────────────────────────┘
```

## Log Management

### Log Levels
| Level | Use Case | Retention |
|-------|----------|-----------|
| DEBUG | Development troubleshooting | 7 days |
| INFO | Normal operations | 30 days |
| WARN | Issues requiring attention | 90 days |
| ERROR | Errors requiring investigation | 1 year |
| CRITICAL | System failures | 1 year |

### Structured Logging
```json
{
  "timestamp": "2025-01-21T10:30:00Z",
  "level": "INFO",
  "service": "ai-agent",
  "trace_id": "abc-123",
  "user_id": "user-456",
  "event": "code_generated",
  "model": "gpt-4",
  "tokens": 150,
  "latency_ms": 1200,
  "success": true
}
```

### Log Analysis Queries
```sql
-- Error analysis
SELECT error_type, COUNT(*) 
FROM logs 
WHERE level = 'ERROR' 
  AND timestamp > NOW() - INTERVAL '1 hour'
GROUP BY error_type;

-- Slow requests
SELECT trace_id, latency_ms 
FROM logs 
WHERE latency_ms > 5000 
  AND timestamp > NOW() - INTERVAL '1 hour';
```

## Distributed Tracing

### Trace Structure
```
Trace: request-123
├── Span: api-gateway (100ms)
├── Span: auth-service (50ms)
├── Span: ai-agent (2000ms)
│   ├── Span: context-retrieval (500ms)
│   ├── Span: llm-call (1200ms)
│   └── Span: post-processing (300ms)
└── Span: response-formatting (100ms)
```

### Key Spans to Trace
- API gateway entry
- Authentication
- Context retrieval
- LLM calls
- Tool executions
- Response formatting

## SLOs and SLIs

### Service Level Indicators (SLIs)
| SLI | Definition | Measurement |
|-----|------------|-------------|
| Availability | % of successful requests | (total - errors) / total |
| Latency | Response time | p95 over 1 minute |
| Quality | Output correctness | Human/AI evaluation |
| Cost | $ per request | Total cost / requests |

### Service Level Objectives (SLOs)
| SLO | Target | Error Budget |
|-----|--------|--------------|
| Availability | 99.9% | 0.1% (43 min/month) |
| Latency p95 | < 2s | 5% of requests |
| Quality Score | > 4.0/5 | 10% of outputs |
| Cost per Request | <$0.05 | 20% variance |

### Error Budget Policy
```
Error Budget = 100% - SLO

If error budget exhausted:
1. Halt feature releases
2. Focus on reliability
3. Review and improve
4. Reset budget next period
```

## Incident Response

### Incident Severity
| Level | Description | Response |
|-------|-------------|----------|
| SEV1 | Complete outage | All hands |
| SEV2 | Major degradation | On-call + team |
| SEV3 | Minor issues | On-call |
| SEV4 | Low impact | Ticket |

### Response Runbook
1. **Detect**: Alert fires
2. **Acknowledge**: Claim the incident
3. **Assess**: Determine severity
4. **Mitigate**: Stop the bleeding
5. **Fix**: Root cause resolution
6. **Verify**: Confirm resolution
7. **Document**: Post-mortem

## Monitoring Tools

### Recommended Stack
| Layer | Tool | Purpose |
|-------|------|---------|
| Metrics | Prometheus | Time-series data |
| Visualization | Grafana | Dashboards |
| Logs | ELK / Loki | Log aggregation |
| Tracing | Jaeger / Zipkin | Distributed traces |
| Alerting | PagerDuty / Opsgenie | Incident management |
| APM | Datadog / New Relic | Full observability |

### Open Source Alternative
- Metrics: Prometheus + Grafana
- Logs: Loki + Grafana
- Tracing: Jaeger
- Alerting: Alertmanager

## Monitoring Checklist

### Setup
- [ ] Metrics collection configured
- [ ] Dashboards created
- [ ] Alerts defined
- [ ] Runbooks written
- [ ] On-call rotation set

### Validation
- [ ] Test alerts fire correctly
- [ ] Verify dashboard accuracy
- [ ] Confirm log aggregation
- [ ] Test trace collection
- [ ] Validate SLOs

### Maintenance
- [ ] Weekly alert review
- [ ] Monthly dashboard updates
- [ ] Quarterly SLO review
- [ ] Annual monitoring audit

---

*Effective monitoring is essential for operating AI coding systems at scale. Start with the basics and iterate based on operational experience.*

# Monitoring and Alerting Guide

Comprehensive guide for monitoring autonomous AI coding systems.

## Monitoring Philosophy

### Key Principles
1. **Monitor what matters**: Focus on metrics that indicate system health and user value
2. **Alert on symptoms, not causes**: Alert when user experience degrades
3. **Actionable alerts**: Every alert should have a clear response
4. **Progressive disclosure**: Start with high-level metrics, drill down as needed

### The Three Pillars
1. **Metrics**: Numerical data over time
2. **Logs**: Detailed event records
3. **Traces**: Request flow visualization

## Metric Categories

### 1. Technical Metrics

#### Latency
| Metric | Description | Target |
|--------|-------------|--------|
| p50 Latency | Median response time | < 500ms |
| p95 Latency | 95th percentile | < 2s |
| p99 Latency | 99th percentile | < 5s |
| Time to First Token | Streaming start | < 200ms |

**Dashboard Query**:
```promql
histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m]))
```

#### Throughput
| Metric | Description | Target |
|--------|-------------|--------|
| Requests/sec | Total requests | Baseline + 20% |
| Tokens/sec | Processing rate | Monitor trend |
| Concurrent Requests | Active requests | < 80% capacity |

**Dashboard Query**:
```promql
rate(requests_total[1m])
```

#### Error Rates
| Metric | Description | Target |
|--------|-------------|--------|
| Error Rate % | Failed requests | < 1% |
| 5xx Errors | Server errors | < 0.1% |
| Timeout Rate | Timed out requests | < 0.5% |

**Dashboard Query**:
```promql
rate(errors_total[5m]) / rate(requests_total[5m]) * 100
```

#### Resource Utilization
| Metric | Description | Target |
|--------|-------------|--------|
| CPU Usage | Processor utilization | < 70% |
| Memory Usage | RAM utilization | < 80% |
| GPU Utilization | GPU usage | < 90% |
| Disk I/O | Storage operations | < 50% capacity |

### 2. Business Metrics

#### Cost Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Cost per Request | Average cost | Trend down |
| Cost per Token | Token efficiency | Trend down |
| Daily Spend | Total daily cost | Within budget |
| Model Distribution | Usage by model | Optimize mix |

**Dashboard Query**:
```promql
sum(cost_dollars) by (model)
```

#### Usage Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Daily Active Users | Unique users/day | Growth |
| Requests per User | Average usage | Engagement |
| Feature Adoption | Feature usage | > 50% |
| Session Duration | Time per session | Engagement |

### 3. Quality Metrics

#### Semantic Quality
| Metric | Description | Target |
|--------|-------------|--------|
| Hallucination Rate | Incorrect outputs | < 5% |
| Factual Correctness | Accuracy score | > 90% |
| Topic Relevancy | Relevance score | > 85% |
| User Satisfaction | Rating | > 4.0/5 |

**Measurement**:
```python
# LLM-as-judge evaluation
def evaluate_quality(output, expected):
    prompt = f"Rate the quality of: {output}
Expected: {expected}"
    score = llm.generate(prompt)
    return parse_score(score)
```

#### Code Quality (for code generation)
| Metric | Description | Target |
|--------|-------------|--------|
| Compilation Success | Code compiles | > 95% |
| Test Pass Rate | Generated tests pass | > 80% |
| Security Issues | Vulnerabilities | 0 critical |
| Style Compliance | Follows guidelines | > 90% |

### 4. Agent-Specific Metrics

#### Agent Performance
| Metric | Description | Target |
|--------|-------------|--------|
| Task Completion Rate | Successful tasks | > 90% |
| Average Steps per Task | Efficiency | Minimize |
| Tool Call Success | Tool execution | > 95% |
| Context Utilization | Token efficiency | > 70% |

#### Multi-Agent Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Coordination Success | Successful handoffs | > 95% |
| Conflict Rate | Agent conflicts | < 1% |
| Consensus Time | Decision time | < 5s |
| Message Volume | Inter-agent traffic | Monitor |

## Alerting Strategy

### Alert Severity Levels

#### P0 - Critical (Immediate Response)
**Conditions**:
- Error rate > 5%
- p99 latency > 10s
- System unavailable
- Security incident

**Response Time**: < 15 minutes
**Escalation**: Page on-call engineer

**Example**:
```yaml
alert: HighErrorRate
expr: rate(errors_total[5m]) / rate(requests_total[5m]) > 0.05
for: 2m
labels:
  severity: critical
annotations:
  summary: "Error rate is {{ $value }}%"
  runbook_url: "https://wiki/runbooks/high-error-rate"
```

#### P1 - High (Urgent Response)
**Conditions**:
- Error rate > 1%
- p95 latency > 5s
- Resource usage > 90%
- Cost spike > 200%

**Response Time**: < 1 hour
**Escalation**: Notify team channel

**Example**:
```yaml
alert: ElevatedLatency
expr: histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m])) > 5
for: 5m
labels:
  severity: high
annotations:
  summary: "p95 latency is {{ $value }}s"
```

#### P2 - Medium (Standard Response)
**Conditions**:
- Error rate > 0.5%
- p50 latency > 1s
- Resource usage > 80%
- Cost variance > 50%

**Response Time**: < 4 hours
**Escalation**: Create ticket

#### P3 - Low (Planned Response)
**Conditions**:
- Minor performance degradation
- Non-critical issues
- Enhancement opportunities

**Response Time**: < 1 week
**Escalation**: Backlog item

### Alert Best Practices

#### Do
- [ ] Include runbook links
- [ ] Provide context in alert
- [ ] Set appropriate thresholds
- [ ] Test alert routing
- [ ] Regular alert review

#### Don't
- [ ] Alert on causes (alert on symptoms)
- [ ] Create alert fatigue
- [ ] Set static thresholds without context
- [ ] Ignore false positives
- [ ] Forget to update runbooks

## Dashboard Design

### Executive Dashboard
**Audience**: Leadership, stakeholders

**Metrics**:
- System availability (SLA)
- Cost trends
- User adoption
- Key incidents

**Layout**:
```
┌─────────────────────────────────────────┐
│  Availability    Cost Trend    Users   │
│    99.9%         ↓ 15%        ↑ 25%    │
├─────────────────────────────────────────┤
│         Incidents (Last 30 Days)        │
│  P0: 0    P1: 2    P2: 5    P3: 12     │
└─────────────────────────────────────────┘
```

### Engineering Dashboard
**Audience**: Engineering team

**Metrics**:
- Latency percentiles
- Error rates
- Throughput
- Resource utilization

**Layout**:
```
┌─────────────────────────────────────────┐
│  Latency (p50/p95/p99)   Error Rate    │
│  200ms / 800ms / 2s        0.5%        │
├─────────────────────────────────────────┤
│  Requests/sec    CPU    Memory    GPU   │
│    150           45%     60%      70%   │
└─────────────────────────────────────────┘
```

### AI-Specific Dashboard
**Audience**: ML/AI team

**Metrics**:
- Hallucination rate
- Token efficiency
- Model distribution
- Quality scores

**Layout**:
```
┌─────────────────────────────────────────┐
│  Hallucination    Token Eff.   Quality │
│     3.2%           72%          4.2/5  │
├─────────────────────────────────────────┤
│         Model Usage Distribution        │
│  GPT-4: 20%  GPT-3.5: 60%  Claude: 20% │
└─────────────────────────────────────────┘
```

### Cost Dashboard
**Audience**: Finance, engineering

**Metrics**:
- Daily spend
- Cost per request
- Model costs
- Budget variance

**Layout**:
```
┌─────────────────────────────────────────┐
│  Daily Spend    Cost/Request   Budget   │
│   $450            $0.03        85%      │
├─────────────────────────────────────────┤
│           Cost by Model ($/day)         │
│  GPT-4: $200  GPT-3.5: $150  Other: $100│
└─────────────────────────────────────────┘
```

## Log Management

### Log Levels
| Level | Use Case | Retention |
|-------|----------|-----------|
| DEBUG | Development troubleshooting | 7 days |
| INFO | Normal operations | 30 days |
| WARN | Issues requiring attention | 90 days |
| ERROR | Errors requiring investigation | 1 year |
| CRITICAL | System failures | 1 year |

### Structured Logging
```json
{
  "timestamp": "2025-01-21T10:30:00Z",
  "level": "INFO",
  "service": "ai-agent",
  "trace_id": "abc-123",
  "user_id": "user-456",
  "event": "code_generated",
  "model": "gpt-4",
  "tokens": 150,
  "latency_ms": 1200,
  "success": true
}
```

### Log Analysis Queries
```sql
-- Error analysis
SELECT error_type, COUNT(*) 
FROM logs 
WHERE level = 'ERROR' 
  AND timestamp > NOW() - INTERVAL '1 hour'
GROUP BY error_type;

-- Slow requests
SELECT trace_id, latency_ms 
FROM logs 
WHERE latency_ms > 5000 
  AND timestamp > NOW() - INTERVAL '1 hour';
```

## Distributed Tracing

### Trace Structure
```
Trace: request-123
├── Span: api-gateway (100ms)
├── Span: auth-service (50ms)
├── Span: ai-agent (2000ms)
│   ├── Span: context-retrieval (500ms)
│   ├── Span: llm-call (1200ms)
│   └── Span: post-processing (300ms)
└── Span: response-formatting (100ms)
```

### Key Spans to Trace
- API gateway entry
- Authentication
- Context retrieval
- LLM calls
- Tool executions
- Response formatting

## SLOs and SLIs

### Service Level Indicators (SLIs)
| SLI | Definition | Measurement |
|-----|------------|-------------|
| Availability | % of successful requests | (total - errors) / total |
| Latency | Response time | p95 over 1 minute |
| Quality | Output correctness | Human/AI evaluation |
| Cost | $ per request | Total cost / requests |

### Service Level Objectives (SLOs)
| SLO | Target | Error Budget |
|-----|--------|--------------|
| Availability | 99.9% | 0.1% (43 min/month) |
| Latency p95 | < 2s | 5% of requests |
| Quality Score | > 4.0/5 | 10% of outputs |
| Cost per Request | <$0.05 | 20% variance |

### Error Budget Policy
```
Error Budget = 100% - SLO

If error budget exhausted:
1. Halt feature releases
2. Focus on reliability
3. Review and improve
4. Reset budget next period
```

## Incident Response

### Incident Severity
| Level | Description | Response |
|-------|-------------|----------|
| SEV1 | Complete outage | All hands |
| SEV2 | Major degradation | On-call + team |
| SEV3 | Minor issues | On-call |
| SEV4 | Low impact | Ticket |

### Response Runbook
1. **Detect**: Alert fires
2. **Acknowledge**: Claim the incident
3. **Assess**: Determine severity
4. **Mitigate**: Stop the bleeding
5. **Fix**: Root cause resolution
6. **Verify**: Confirm resolution
7. **Document**: Post-mortem

## Monitoring Tools

### Recommended Stack
| Layer | Tool | Purpose |
|-------|------|---------|
| Metrics | Prometheus | Time-series data |
| Visualization | Grafana | Dashboards |
| Logs | ELK / Loki | Log aggregation |
| Tracing | Jaeger / Zipkin | Distributed traces |
| Alerting | PagerDuty / Opsgenie | Incident management |
| APM | Datadog / New Relic | Full observability |

### Open Source Alternative
- Metrics: Prometheus + Grafana
- Logs: Loki + Grafana
- Tracing: Jaeger
- Alerting: Alertmanager

## Monitoring Checklist

### Setup
- [ ] Metrics collection configured
- [ ] Dashboards created
- [ ] Alerts defined
- [ ] Runbooks written
- [ ] On-call rotation set

### Validation
- [ ] Test alerts fire correctly
- [ ] Verify dashboard accuracy
- [ ] Confirm log aggregation
- [ ] Test trace collection
- [ ] Validate SLOs

### Maintenance
- [ ] Weekly alert review
- [ ] Monthly dashboard updates
- [ ] Quarterly SLO review
- [ ] Annual monitoring audit

---

*Effective monitoring is essential for operating AI coding systems at scale. Start with the basics and iterate based on operational experience.*

# Monitoring and Alerting Guide

Comprehensive guide for monitoring autonomous AI coding systems.

## Monitoring Philosophy

### Key Principles
1. **Monitor what matters**: Focus on metrics that indicate system health and user value
2. **Alert on symptoms, not causes**: Alert when user experience degrades
3. **Actionable alerts**: Every alert should have a clear response
4. **Progressive disclosure**: Start with high-level metrics, drill down as needed

### The Three Pillars
1. **Metrics**: Numerical data over time
2. **Logs**: Detailed event records
3. **Traces**: Request flow visualization

## Metric Categories

### 1. Technical Metrics

#### Latency
| Metric | Description | Target |
|--------|-------------|--------|
| p50 Latency | Median response time | < 500ms |
| p95 Latency | 95th percentile | < 2s |
| p99 Latency | 99th percentile | < 5s |
| Time to First Token | Streaming start | < 200ms |

**Dashboard Query**:
```promql
histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m]))
```

#### Throughput
| Metric | Description | Target |
|--------|-------------|--------|
| Requests/sec | Total requests | Baseline + 20% |
| Tokens/sec | Processing rate | Monitor trend |
| Concurrent Requests | Active requests | < 80% capacity |

**Dashboard Query**:
```promql
rate(requests_total[1m])
```

#### Error Rates
| Metric | Description | Target |
|--------|-------------|--------|
| Error Rate % | Failed requests | < 1% |
| 5xx Errors | Server errors | < 0.1% |
| Timeout Rate | Timed out requests | < 0.5% |

**Dashboard Query**:
```promql
rate(errors_total[5m]) / rate(requests_total[5m]) * 100
```

#### Resource Utilization
| Metric | Description | Target |
|--------|-------------|--------|
| CPU Usage | Processor utilization | < 70% |
| Memory Usage | RAM utilization | < 80% |
| GPU Utilization | GPU usage | < 90% |
| Disk I/O | Storage operations | < 50% capacity |

### 2. Business Metrics

#### Cost Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Cost per Request | Average cost | Trend down |
| Cost per Token | Token efficiency | Trend down |
| Daily Spend | Total daily cost | Within budget |
| Model Distribution | Usage by model | Optimize mix |

**Dashboard Query**:
```promql
sum(cost_dollars) by (model)
```

#### Usage Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Daily Active Users | Unique users/day | Growth |
| Requests per User | Average usage | Engagement |
| Feature Adoption | Feature usage | > 50% |
| Session Duration | Time per session | Engagement |

### 3. Quality Metrics

#### Semantic Quality
| Metric | Description | Target |
|--------|-------------|--------|
| Hallucination Rate | Incorrect outputs | < 5% |
| Factual Correctness | Accuracy score | > 90% |
| Topic Relevancy | Relevance score | > 85% |
| User Satisfaction | Rating | > 4.0/5 |

**Measurement**:
```python
# LLM-as-judge evaluation
def evaluate_quality(output, expected):
    prompt = f"Rate the quality of: {output}
Expected: {expected}"
    score = llm.generate(prompt)
    return parse_score(score)
```

#### Code Quality (for code generation)
| Metric | Description | Target |
|--------|-------------|--------|
| Compilation Success | Code compiles | > 95% |
| Test Pass Rate | Generated tests pass | > 80% |
| Security Issues | Vulnerabilities | 0 critical |
| Style Compliance | Follows guidelines | > 90% |

### 4. Agent-Specific Metrics

#### Agent Performance
| Metric | Description | Target |
|--------|-------------|--------|
| Task Completion Rate | Successful tasks | > 90% |
| Average Steps per Task | Efficiency | Minimize |
| Tool Call Success | Tool execution | > 95% |
| Context Utilization | Token efficiency | > 70% |

#### Multi-Agent Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Coordination Success | Successful handoffs | > 95% |
| Conflict Rate | Agent conflicts | < 1% |
| Consensus Time | Decision time | < 5s |
| Message Volume | Inter-agent traffic | Monitor |

## Alerting Strategy

### Alert Severity Levels

#### P0 - Critical (Immediate Response)
**Conditions**:
- Error rate > 5%
- p99 latency > 10s
- System unavailable
- Security incident

**Response Time**: < 15 minutes
**Escalation**: Page on-call engineer

**Example**:
```yaml
alert: HighErrorRate
expr: rate(errors_total[5m]) / rate(requests_total[5m]) > 0.05
for: 2m
labels:
  severity: critical
annotations:
  summary: "Error rate is {{ $value }}%"
  runbook_url: "https://wiki/runbooks/high-error-rate"
```

#### P1 - High (Urgent Response)
**Conditions**:
- Error rate > 1%
- p95 latency > 5s
- Resource usage > 90%
- Cost spike > 200%

**Response Time**: < 1 hour
**Escalation**: Notify team channel

**Example**:
```yaml
alert: ElevatedLatency
expr: histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m])) > 5
for: 5m
labels:
  severity: high
annotations:
  summary: "p95 latency is {{ $value }}s"
```

#### P2 - Medium (Standard Response)
**Conditions**:
- Error rate > 0.5%
- p50 latency > 1s
- Resource usage > 80%
- Cost variance > 50%

**Response Time**: < 4 hours
**Escalation**: Create ticket

#### P3 - Low (Planned Response)
**Conditions**:
- Minor performance degradation
- Non-critical issues
- Enhancement opportunities

**Response Time**: < 1 week
**Escalation**: Backlog item

### Alert Best Practices

#### Do
- [ ] Include runbook links
- [ ] Provide context in alert
- [ ] Set appropriate thresholds
- [ ] Test alert routing
- [ ] Regular alert review

#### Don't
- [ ] Alert on causes (alert on symptoms)
- [ ] Create alert fatigue
- [ ] Set static thresholds without context
- [ ] Ignore false positives
- [ ] Forget to update runbooks

## Dashboard Design

### Executive Dashboard
**Audience**: Leadership, stakeholders

**Metrics**:
- System availability (SLA)
- Cost trends
- User adoption
- Key incidents

**Layout**:
```
┌─────────────────────────────────────────┐
│  Availability    Cost Trend    Users   │
│    99.9%         ↓ 15%        ↑ 25%    │
├─────────────────────────────────────────┤
│         Incidents (Last 30 Days)        │
│  P0: 0    P1: 2    P2: 5    P3: 12     │
└─────────────────────────────────────────┘
```

### Engineering Dashboard
**Audience**: Engineering team

**Metrics**:
- Latency percentiles
- Error rates
- Throughput
- Resource utilization

**Layout**:
```
┌─────────────────────────────────────────┐
│  Latency (p50/p95/p99)   Error Rate    │
│  200ms / 800ms / 2s        0.5%        │
├─────────────────────────────────────────┤
│  Requests/sec    CPU    Memory    GPU   │
│    150           45%     60%      70%   │
└─────────────────────────────────────────┘
```

### AI-Specific Dashboard
**Audience**: ML/AI team

**Metrics**:
- Hallucination rate
- Token efficiency
- Model distribution
- Quality scores

**Layout**:
```
┌─────────────────────────────────────────┐
│  Hallucination    Token Eff.   Quality │
│     3.2%           72%          4.2/5  │
├─────────────────────────────────────────┤
│         Model Usage Distribution        │
│  GPT-4: 20%  GPT-3.5: 60%  Claude: 20% │
└─────────────────────────────────────────┘
```

### Cost Dashboard
**Audience**: Finance, engineering

**Metrics**:
- Daily spend
- Cost per request
- Model costs
- Budget variance

**Layout**:
```
┌─────────────────────────────────────────┐
│  Daily Spend    Cost/Request   Budget   │
│   $450            $0.03        85%      │
├─────────────────────────────────────────┤
│           Cost by Model ($/day)         │
│  GPT-4: $200  GPT-3.5: $150  Other: $100│
└─────────────────────────────────────────┘
```

## Log Management

### Log Levels
| Level | Use Case | Retention |
|-------|----------|-----------|
| DEBUG | Development troubleshooting | 7 days |
| INFO | Normal operations | 30 days |
| WARN | Issues requiring attention | 90 days |
| ERROR | Errors requiring investigation | 1 year |
| CRITICAL | System failures | 1 year |

### Structured Logging
```json
{
  "timestamp": "2025-01-21T10:30:00Z",
  "level": "INFO",
  "service": "ai-agent",
  "trace_id": "abc-123",
  "user_id": "user-456",
  "event": "code_generated",
  "model": "gpt-4",
  "tokens": 150,
  "latency_ms": 1200,
  "success": true
}
```

### Log Analysis Queries
```sql
-- Error analysis
SELECT error_type, COUNT(*) 
FROM logs 
WHERE level = 'ERROR' 
  AND timestamp > NOW() - INTERVAL '1 hour'
GROUP BY error_type;

-- Slow requests
SELECT trace_id, latency_ms 
FROM logs 
WHERE latency_ms > 5000 
  AND timestamp > NOW() - INTERVAL '1 hour';
```

## Distributed Tracing

### Trace Structure
```
Trace: request-123
├── Span: api-gateway (100ms)
├── Span: auth-service (50ms)
├── Span: ai-agent (2000ms)
│   ├── Span: context-retrieval (500ms)
│   ├── Span: llm-call (1200ms)
│   └── Span: post-processing (300ms)
└── Span: response-formatting (100ms)
```

### Key Spans to Trace
- API gateway entry
- Authentication
- Context retrieval
- LLM calls
- Tool executions
- Response formatting

## SLOs and SLIs

### Service Level Indicators (SLIs)
| SLI | Definition | Measurement |
|-----|------------|-------------|
| Availability | % of successful requests | (total - errors) / total |
| Latency | Response time | p95 over 1 minute |
| Quality | Output correctness | Human/AI evaluation |
| Cost | $ per request | Total cost / requests |

### Service Level Objectives (SLOs)
| SLO | Target | Error Budget |
|-----|--------|--------------|
| Availability | 99.9% | 0.1% (43 min/month) |
| Latency p95 | < 2s | 5% of requests |
| Quality Score | > 4.0/5 | 10% of outputs |
| Cost per Request | <$0.05 | 20% variance |

### Error Budget Policy
```
Error Budget = 100% - SLO

If error budget exhausted:
1. Halt feature releases
2. Focus on reliability
3. Review and improve
4. Reset budget next period
```

## Incident Response

### Incident Severity
| Level | Description | Response |
|-------|-------------|----------|
| SEV1 | Complete outage | All hands |
| SEV2 | Major degradation | On-call + team |
| SEV3 | Minor issues | On-call |
| SEV4 | Low impact | Ticket |

### Response Runbook
1. **Detect**: Alert fires
2. **Acknowledge**: Claim the incident
3. **Assess**: Determine severity
4. **Mitigate**: Stop the bleeding
5. **Fix**: Root cause resolution
6. **Verify**: Confirm resolution
7. **Document**: Post-mortem

## Monitoring Tools

### Recommended Stack
| Layer | Tool | Purpose |
|-------|------|---------|
| Metrics | Prometheus | Time-series data |
| Visualization | Grafana | Dashboards |
| Logs | ELK / Loki | Log aggregation |
| Tracing | Jaeger / Zipkin | Distributed traces |
| Alerting | PagerDuty / Opsgenie | Incident management |
| APM | Datadog / New Relic | Full observability |

### Open Source Alternative
- Metrics: Prometheus + Grafana
- Logs: Loki + Grafana
- Tracing: Jaeger
- Alerting: Alertmanager

## Monitoring Checklist

### Setup
- [ ] Metrics collection configured
- [ ] Dashboards created
- [ ] Alerts defined
- [ ] Runbooks written
- [ ] On-call rotation set

### Validation
- [ ] Test alerts fire correctly
- [ ] Verify dashboard accuracy
- [ ] Confirm log aggregation
- [ ] Test trace collection
- [ ] Validate SLOs

### Maintenance
- [ ] Weekly alert review
- [ ] Monthly dashboard updates
- [ ] Quarterly SLO review
- [ ] Annual monitoring audit

---

*Effective monitoring is essential for operating AI coding systems at scale. Start with the basics and iterate based on operational experience.*

# Monitoring and Alerting Guide

Comprehensive guide for monitoring autonomous AI coding systems.

## Monitoring Philosophy

### Key Principles
1. **Monitor what matters**: Focus on metrics that indicate system health and user value
2. **Alert on symptoms, not causes**: Alert when user experience degrades
3. **Actionable alerts**: Every alert should have a clear response
4. **Progressive disclosure**: Start with high-level metrics, drill down as needed

### The Three Pillars
1. **Metrics**: Numerical data over time
2. **Logs**: Detailed event records
3. **Traces**: Request flow visualization

## Metric Categories

### 1. Technical Metrics

#### Latency
| Metric | Description | Target |
|--------|-------------|--------|
| p50 Latency | Median response time | < 500ms |
| p95 Latency | 95th percentile | < 2s |
| p99 Latency | 99th percentile | < 5s |
| Time to First Token | Streaming start | < 200ms |

**Dashboard Query**:
```promql
histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m]))
```

#### Throughput
| Metric | Description | Target |
|--------|-------------|--------|
| Requests/sec | Total requests | Baseline + 20% |
| Tokens/sec | Processing rate | Monitor trend |
| Concurrent Requests | Active requests | < 80% capacity |

**Dashboard Query**:
```promql
rate(requests_total[1m])
```

#### Error Rates
| Metric | Description | Target |
|--------|-------------|--------|
| Error Rate % | Failed requests | < 1% |
| 5xx Errors | Server errors | < 0.1% |
| Timeout Rate | Timed out requests | < 0.5% |

**Dashboard Query**:
```promql
rate(errors_total[5m]) / rate(requests_total[5m]) * 100
```

#### Resource Utilization
| Metric | Description | Target |
|--------|-------------|--------|
| CPU Usage | Processor utilization | < 70% |
| Memory Usage | RAM utilization | < 80% |
| GPU Utilization | GPU usage | < 90% |
| Disk I/O | Storage operations | < 50% capacity |

### 2. Business Metrics

#### Cost Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Cost per Request | Average cost | Trend down |
| Cost per Token | Token efficiency | Trend down |
| Daily Spend | Total daily cost | Within budget |
| Model Distribution | Usage by model | Optimize mix |

**Dashboard Query**:
```promql
sum(cost_dollars) by (model)
```

#### Usage Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Daily Active Users | Unique users/day | Growth |
| Requests per User | Average usage | Engagement |
| Feature Adoption | Feature usage | > 50% |
| Session Duration | Time per session | Engagement |

### 3. Quality Metrics

#### Semantic Quality
| Metric | Description | Target |
|--------|-------------|--------|
| Hallucination Rate | Incorrect outputs | < 5% |
| Factual Correctness | Accuracy score | > 90% |
| Topic Relevancy | Relevance score | > 85% |
| User Satisfaction | Rating | > 4.0/5 |

**Measurement**:
```python
# LLM-as-judge evaluation
def evaluate_quality(output, expected):
    prompt = f"Rate the quality of: {output}
Expected: {expected}"
    score = llm.generate(prompt)
    return parse_score(score)
```

#### Code Quality (for code generation)
| Metric | Description | Target |
|--------|-------------|--------|
| Compilation Success | Code compiles | > 95% |
| Test Pass Rate | Generated tests pass | > 80% |
| Security Issues | Vulnerabilities | 0 critical |
| Style Compliance | Follows guidelines | > 90% |

### 4. Agent-Specific Metrics

#### Agent Performance
| Metric | Description | Target |
|--------|-------------|--------|
| Task Completion Rate | Successful tasks | > 90% |
| Average Steps per Task | Efficiency | Minimize |
| Tool Call Success | Tool execution | > 95% |
| Context Utilization | Token efficiency | > 70% |

#### Multi-Agent Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Coordination Success | Successful handoffs | > 95% |
| Conflict Rate | Agent conflicts | < 1% |
| Consensus Time | Decision time | < 5s |
| Message Volume | Inter-agent traffic | Monitor |

## Alerting Strategy

### Alert Severity Levels

#### P0 - Critical (Immediate Response)
**Conditions**:
- Error rate > 5%
- p99 latency > 10s
- System unavailable
- Security incident

**Response Time**: < 15 minutes
**Escalation**: Page on-call engineer

**Example**:
```yaml
alert: HighErrorRate
expr: rate(errors_total[5m]) / rate(requests_total[5m]) > 0.05
for: 2m
labels:
  severity: critical
annotations:
  summary: "Error rate is {{ $value }}%"
  runbook_url: "https://wiki/runbooks/high-error-rate"
```

#### P1 - High (Urgent Response)
**Conditions**:
- Error rate > 1%
- p95 latency > 5s
- Resource usage > 90%
- Cost spike > 200%

**Response Time**: < 1 hour
**Escalation**: Notify team channel

**Example**:
```yaml
alert: ElevatedLatency
expr: histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m])) > 5
for: 5m
labels:
  severity: high
annotations:
  summary: "p95 latency is {{ $value }}s"
```

#### P2 - Medium (Standard Response)
**Conditions**:
- Error rate > 0.5%
- p50 latency > 1s
- Resource usage > 80%
- Cost variance > 50%

**Response Time**: < 4 hours
**Escalation**: Create ticket

#### P3 - Low (Planned Response)
**Conditions**:
- Minor performance degradation
- Non-critical issues
- Enhancement opportunities

**Response Time**: < 1 week
**Escalation**: Backlog item

### Alert Best Practices

#### Do
- [ ] Include runbook links
- [ ] Provide context in alert
- [ ] Set appropriate thresholds
- [ ] Test alert routing
- [ ] Regular alert review

#### Don't
- [ ] Alert on causes (alert on symptoms)
- [ ] Create alert fatigue
- [ ] Set static thresholds without context
- [ ] Ignore false positives
- [ ] Forget to update runbooks

## Dashboard Design

### Executive Dashboard
**Audience**: Leadership, stakeholders

**Metrics**:
- System availability (SLA)
- Cost trends
- User adoption
- Key incidents

**Layout**:
```
┌─────────────────────────────────────────┐
│  Availability    Cost Trend    Users   │
│    99.9%         ↓ 15%        ↑ 25%    │
├─────────────────────────────────────────┤
│         Incidents (Last 30 Days)        │
│  P0: 0    P1: 2    P2: 5    P3: 12     │
└─────────────────────────────────────────┘
```

### Engineering Dashboard
**Audience**: Engineering team

**Metrics**:
- Latency percentiles
- Error rates
- Throughput
- Resource utilization

**Layout**:
```
┌─────────────────────────────────────────┐
│  Latency (p50/p95/p99)   Error Rate    │
│  200ms / 800ms / 2s        0.5%        │
├─────────────────────────────────────────┤
│  Requests/sec    CPU    Memory    GPU   │
│    150           45%     60%      70%   │
└─────────────────────────────────────────┘
```

### AI-Specific Dashboard
**Audience**: ML/AI team

**Metrics**:
- Hallucination rate
- Token efficiency
- Model distribution
- Quality scores

**Layout**:
```
┌─────────────────────────────────────────┐
│  Hallucination    Token Eff.   Quality │
│     3.2%           72%          4.2/5  │
├─────────────────────────────────────────┤
│         Model Usage Distribution        │
│  GPT-4: 20%  GPT-3.5: 60%  Claude: 20% │
└─────────────────────────────────────────┘
```

### Cost Dashboard
**Audience**: Finance, engineering

**Metrics**:
- Daily spend
- Cost per request
- Model costs
- Budget variance

**Layout**:
```
┌─────────────────────────────────────────┐
│  Daily Spend    Cost/Request   Budget   │
│   $450            $0.03        85%      │
├─────────────────────────────────────────┤
│           Cost by Model ($/day)         │
│  GPT-4: $200  GPT-3.5: $150  Other: $100│
└─────────────────────────────────────────┘
```

## Log Management

### Log Levels
| Level | Use Case | Retention |
|-------|----------|-----------|
| DEBUG | Development troubleshooting | 7 days |
| INFO | Normal operations | 30 days |
| WARN | Issues requiring attention | 90 days |
| ERROR | Errors requiring investigation | 1 year |
| CRITICAL | System failures | 1 year |

### Structured Logging
```json
{
  "timestamp": "2025-01-21T10:30:00Z",
  "level": "INFO",
  "service": "ai-agent",
  "trace_id": "abc-123",
  "user_id": "user-456",
  "event": "code_generated",
  "model": "gpt-4",
  "tokens": 150,
  "latency_ms": 1200,
  "success": true
}
```

### Log Analysis Queries
```sql
-- Error analysis
SELECT error_type, COUNT(*) 
FROM logs 
WHERE level = 'ERROR' 
  AND timestamp > NOW() - INTERVAL '1 hour'
GROUP BY error_type;

-- Slow requests
SELECT trace_id, latency_ms 
FROM logs 
WHERE latency_ms > 5000 
  AND timestamp > NOW() - INTERVAL '1 hour';
```

## Distributed Tracing

### Trace Structure
```
Trace: request-123
├── Span: api-gateway (100ms)
├── Span: auth-service (50ms)
├── Span: ai-agent (2000ms)
│   ├── Span: context-retrieval (500ms)
│   ├── Span: llm-call (1200ms)
│   └── Span: post-processing (300ms)
└── Span: response-formatting (100ms)
```

### Key Spans to Trace
- API gateway entry
- Authentication
- Context retrieval
- LLM calls
- Tool executions
- Response formatting

## SLOs and SLIs

### Service Level Indicators (SLIs)
| SLI | Definition | Measurement |
|-----|------------|-------------|
| Availability | % of successful requests | (total - errors) / total |
| Latency | Response time | p95 over 1 minute |
| Quality | Output correctness | Human/AI evaluation |
| Cost | $ per request | Total cost / requests |

### Service Level Objectives (SLOs)
| SLO | Target | Error Budget |
|-----|--------|--------------|
| Availability | 99.9% | 0.1% (43 min/month) |
| Latency p95 | < 2s | 5% of requests |
| Quality Score | > 4.0/5 | 10% of outputs |
| Cost per Request | <$0.05 | 20% variance |

### Error Budget Policy
```
Error Budget = 100% - SLO

If error budget exhausted:
1. Halt feature releases
2. Focus on reliability
3. Review and improve
4. Reset budget next period
```

## Incident Response

### Incident Severity
| Level | Description | Response |
|-------|-------------|----------|
| SEV1 | Complete outage | All hands |
| SEV2 | Major degradation | On-call + team |
| SEV3 | Minor issues | On-call |
| SEV4 | Low impact | Ticket |

### Response Runbook
1. **Detect**: Alert fires
2. **Acknowledge**: Claim the incident
3. **Assess**: Determine severity
4. **Mitigate**: Stop the bleeding
5. **Fix**: Root cause resolution
6. **Verify**: Confirm resolution
7. **Document**: Post-mortem

## Monitoring Tools

### Recommended Stack
| Layer | Tool | Purpose |
|-------|------|---------|
| Metrics | Prometheus | Time-series data |
| Visualization | Grafana | Dashboards |
| Logs | ELK / Loki | Log aggregation |
| Tracing | Jaeger / Zipkin | Distributed traces |
| Alerting | PagerDuty / Opsgenie | Incident management |
| APM | Datadog / New Relic | Full observability |

### Open Source Alternative
- Metrics: Prometheus + Grafana
- Logs: Loki + Grafana
- Tracing: Jaeger
- Alerting: Alertmanager

## Monitoring Checklist

### Setup
- [ ] Metrics collection configured
- [ ] Dashboards created
- [ ] Alerts defined
- [ ] Runbooks written
- [ ] On-call rotation set

### Validation
- [ ] Test alerts fire correctly
- [ ] Verify dashboard accuracy
- [ ] Confirm log aggregation
- [ ] Test trace collection
- [ ] Validate SLOs

### Maintenance
- [ ] Weekly alert review
- [ ] Monthly dashboard updates
- [ ] Quarterly SLO review
- [ ] Annual monitoring audit

---

*Effective monitoring is essential for operating AI coding systems at scale. Start with the basics and iterate based on operational experience.*

# Monitoring and Alerting Guide

Comprehensive guide for monitoring autonomous AI coding systems.

## Monitoring Philosophy

### Key Principles
1. **Monitor what matters**: Focus on metrics that indicate system health and user value
2. **Alert on symptoms, not causes**: Alert when user experience degrades
3. **Actionable alerts**: Every alert should have a clear response
4. **Progressive disclosure**: Start with high-level metrics, drill down as needed

### The Three Pillars
1. **Metrics**: Numerical data over time
2. **Logs**: Detailed event records
3. **Traces**: Request flow visualization

## Metric Categories

### 1. Technical Metrics

#### Latency
| Metric | Description | Target |
|--------|-------------|--------|
| p50 Latency | Median response time | < 500ms |
| p95 Latency | 95th percentile | < 2s |
| p99 Latency | 99th percentile | < 5s |
| Time to First Token | Streaming start | < 200ms |

**Dashboard Query**:
```promql
histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m]))
```

#### Throughput
| Metric | Description | Target |
|--------|-------------|--------|
| Requests/sec | Total requests | Baseline + 20% |
| Tokens/sec | Processing rate | Monitor trend |
| Concurrent Requests | Active requests | < 80% capacity |

**Dashboard Query**:
```promql
rate(requests_total[1m])
```

#### Error Rates
| Metric | Description | Target |
|--------|-------------|--------|
| Error Rate % | Failed requests | < 1% |
| 5xx Errors | Server errors | < 0.1% |
| Timeout Rate | Timed out requests | < 0.5% |

**Dashboard Query**:
```promql
rate(errors_total[5m]) / rate(requests_total[5m]) * 100
```

#### Resource Utilization
| Metric | Description | Target |
|--------|-------------|--------|
| CPU Usage | Processor utilization | < 70% |
| Memory Usage | RAM utilization | < 80% |
| GPU Utilization | GPU usage | < 90% |
| Disk I/O | Storage operations | < 50% capacity |

### 2. Business Metrics

#### Cost Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Cost per Request | Average cost | Trend down |
| Cost per Token | Token efficiency | Trend down |
| Daily Spend | Total daily cost | Within budget |
| Model Distribution | Usage by model | Optimize mix |

**Dashboard Query**:
```promql
sum(cost_dollars) by (model)
```

#### Usage Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Daily Active Users | Unique users/day | Growth |
| Requests per User | Average usage | Engagement |
| Feature Adoption | Feature usage | > 50% |
| Session Duration | Time per session | Engagement |

### 3. Quality Metrics

#### Semantic Quality
| Metric | Description | Target |
|--------|-------------|--------|
| Hallucination Rate | Incorrect outputs | < 5% |
| Factual Correctness | Accuracy score | > 90% |
| Topic Relevancy | Relevance score | > 85% |
| User Satisfaction | Rating | > 4.0/5 |

**Measurement**:
```python
# LLM-as-judge evaluation
def evaluate_quality(output, expected):
    prompt = f"Rate the quality of: {output}
Expected: {expected}"
    score = llm.generate(prompt)
    return parse_score(score)
```

#### Code Quality (for code generation)
| Metric | Description | Target |
|--------|-------------|--------|
| Compilation Success | Code compiles | > 95% |
| Test Pass Rate | Generated tests pass | > 80% |
| Security Issues | Vulnerabilities | 0 critical |
| Style Compliance | Follows guidelines | > 90% |

### 4. Agent-Specific Metrics

#### Agent Performance
| Metric | Description | Target |
|--------|-------------|--------|
| Task Completion Rate | Successful tasks | > 90% |
| Average Steps per Task | Efficiency | Minimize |
| Tool Call Success | Tool execution | > 95% |
| Context Utilization | Token efficiency | > 70% |

#### Multi-Agent Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Coordination Success | Successful handoffs | > 95% |
| Conflict Rate | Agent conflicts | < 1% |
| Consensus Time | Decision time | < 5s |
| Message Volume | Inter-agent traffic | Monitor |

## Alerting Strategy

### Alert Severity Levels

#### P0 - Critical (Immediate Response)
**Conditions**:
- Error rate > 5%
- p99 latency > 10s
- System unavailable
- Security incident

**Response Time**: < 15 minutes
**Escalation**: Page on-call engineer

**Example**:
```yaml
alert: HighErrorRate
expr: rate(errors_total[5m]) / rate(requests_total[5m]) > 0.05
for: 2m
labels:
  severity: critical
annotations:
  summary: "Error rate is {{ $value }}%"
  runbook_url: "https://wiki/runbooks/high-error-rate"
```

#### P1 - High (Urgent Response)
**Conditions**:
- Error rate > 1%
- p95 latency > 5s
- Resource usage > 90%
- Cost spike > 200%

**Response Time**: < 1 hour
**Escalation**: Notify team channel

**Example**:
```yaml
alert: ElevatedLatency
expr: histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m])) > 5
for: 5m
labels:
  severity: high
annotations:
  summary: "p95 latency is {{ $value }}s"
```

#### P2 - Medium (Standard Response)
**Conditions**:
- Error rate > 0.5%
- p50 latency > 1s
- Resource usage > 80%
- Cost variance > 50%

**Response Time**: < 4 hours
**Escalation**: Create ticket

#### P3 - Low (Planned Response)
**Conditions**:
- Minor performance degradation
- Non-critical issues
- Enhancement opportunities

**Response Time**: < 1 week
**Escalation**: Backlog item

### Alert Best Practices

#### Do
- [ ] Include runbook links
- [ ] Provide context in alert
- [ ] Set appropriate thresholds
- [ ] Test alert routing
- [ ] Regular alert review

#### Don't
- [ ] Alert on causes (alert on symptoms)
- [ ] Create alert fatigue
- [ ] Set static thresholds without context
- [ ] Ignore false positives
- [ ] Forget to update runbooks

## Dashboard Design

### Executive Dashboard
**Audience**: Leadership, stakeholders

**Metrics**:
- System availability (SLA)
- Cost trends
- User adoption
- Key incidents

**Layout**:
```
┌─────────────────────────────────────────┐
│  Availability    Cost Trend    Users   │
│    99.9%         ↓ 15%        ↑ 25%    │
├─────────────────────────────────────────┤
│         Incidents (Last 30 Days)        │
│  P0: 0    P1: 2    P2: 5    P3: 12     │
└─────────────────────────────────────────┘
```

### Engineering Dashboard
**Audience**: Engineering team

**Metrics**:
- Latency percentiles
- Error rates
- Throughput
- Resource utilization

**Layout**:
```
┌─────────────────────────────────────────┐
│  Latency (p50/p95/p99)   Error Rate    │
│  200ms / 800ms / 2s        0.5%        │
├─────────────────────────────────────────┤
│  Requests/sec    CPU    Memory    GPU   │
│    150           45%     60%      70%   │
└─────────────────────────────────────────┘
```

### AI-Specific Dashboard
**Audience**: ML/AI team

**Metrics**:
- Hallucination rate
- Token efficiency
- Model distribution
- Quality scores

**Layout**:
```
┌─────────────────────────────────────────┐
│  Hallucination    Token Eff.   Quality │
│     3.2%           72%          4.2/5  │
├─────────────────────────────────────────┤
│         Model Usage Distribution        │
│  GPT-4: 20%  GPT-3.5: 60%  Claude: 20% │
└─────────────────────────────────────────┘
```

### Cost Dashboard
**Audience**: Finance, engineering

**Metrics**:
- Daily spend
- Cost per request
- Model costs
- Budget variance

**Layout**:
```
┌─────────────────────────────────────────┐
│  Daily Spend    Cost/Request   Budget   │
│   $450            $0.03        85%      │
├─────────────────────────────────────────┤
│           Cost by Model ($/day)         │
│  GPT-4: $200  GPT-3.5: $150  Other: $100│
└─────────────────────────────────────────┘
```

## Log Management

### Log Levels
| Level | Use Case | Retention |
|-------|----------|-----------|
| DEBUG | Development troubleshooting | 7 days |
| INFO | Normal operations | 30 days |
| WARN | Issues requiring attention | 90 days |
| ERROR | Errors requiring investigation | 1 year |
| CRITICAL | System failures | 1 year |

### Structured Logging
```json
{
  "timestamp": "2025-01-21T10:30:00Z",
  "level": "INFO",
  "service": "ai-agent",
  "trace_id": "abc-123",
  "user_id": "user-456",
  "event": "code_generated",
  "model": "gpt-4",
  "tokens": 150,
  "latency_ms": 1200,
  "success": true
}
```

### Log Analysis Queries
```sql
-- Error analysis
SELECT error_type, COUNT(*) 
FROM logs 
WHERE level = 'ERROR' 
  AND timestamp > NOW() - INTERVAL '1 hour'
GROUP BY error_type;

-- Slow requests
SELECT trace_id, latency_ms 
FROM logs 
WHERE latency_ms > 5000 
  AND timestamp > NOW() - INTERVAL '1 hour';
```

## Distributed Tracing

### Trace Structure
```
Trace: request-123
├── Span: api-gateway (100ms)
├── Span: auth-service (50ms)
├── Span: ai-agent (2000ms)
│   ├── Span: context-retrieval (500ms)
│   ├── Span: llm-call (1200ms)
│   └── Span: post-processing (300ms)
└── Span: response-formatting (100ms)
```

### Key Spans to Trace
- API gateway entry
- Authentication
- Context retrieval
- LLM calls
- Tool executions
- Response formatting

## SLOs and SLIs

### Service Level Indicators (SLIs)
| SLI | Definition | Measurement |
|-----|------------|-------------|
| Availability | % of successful requests | (total - errors) / total |
| Latency | Response time | p95 over 1 minute |
| Quality | Output correctness | Human/AI evaluation |
| Cost | $ per request | Total cost / requests |

### Service Level Objectives (SLOs)
| SLO | Target | Error Budget |
|-----|--------|--------------|
| Availability | 99.9% | 0.1% (43 min/month) |
| Latency p95 | < 2s | 5% of requests |
| Quality Score | > 4.0/5 | 10% of outputs |
| Cost per Request | <$0.05 | 20% variance |

### Error Budget Policy
```
Error Budget = 100% - SLO

If error budget exhausted:
1. Halt feature releases
2. Focus on reliability
3. Review and improve
4. Reset budget next period
```

## Incident Response

### Incident Severity
| Level | Description | Response |
|-------|-------------|----------|
| SEV1 | Complete outage | All hands |
| SEV2 | Major degradation | On-call + team |
| SEV3 | Minor issues | On-call |
| SEV4 | Low impact | Ticket |

### Response Runbook
1. **Detect**: Alert fires
2. **Acknowledge**: Claim the incident
3. **Assess**: Determine severity
4. **Mitigate**: Stop the bleeding
5. **Fix**: Root cause resolution
6. **Verify**: Confirm resolution
7. **Document**: Post-mortem

## Monitoring Tools

### Recommended Stack
| Layer | Tool | Purpose |
|-------|------|---------|
| Metrics | Prometheus | Time-series data |
| Visualization | Grafana | Dashboards |
| Logs | ELK / Loki | Log aggregation |
| Tracing | Jaeger / Zipkin | Distributed traces |
| Alerting | PagerDuty / Opsgenie | Incident management |
| APM | Datadog / New Relic | Full observability |

### Open Source Alternative
- Metrics: Prometheus + Grafana
- Logs: Loki + Grafana
- Tracing: Jaeger
- Alerting: Alertmanager

## Monitoring Checklist

### Setup
- [ ] Metrics collection configured
- [ ] Dashboards created
- [ ] Alerts defined
- [ ] Runbooks written
- [ ] On-call rotation set

### Validation
- [ ] Test alerts fire correctly
- [ ] Verify dashboard accuracy
- [ ] Confirm log aggregation
- [ ] Test trace collection
- [ ] Validate SLOs

### Maintenance
- [ ] Weekly alert review
- [ ] Monthly dashboard updates
- [ ] Quarterly SLO review
- [ ] Annual monitoring audit

---

*Effective monitoring is essential for operating AI coding systems at scale. Start with the basics and iterate based on operational experience.*

# Monitoring and Alerting Guide

Comprehensive guide for monitoring autonomous AI coding systems.

## Monitoring Philosophy

### Key Principles
1. **Monitor what matters**: Focus on metrics that indicate system health and user value
2. **Alert on symptoms, not causes**: Alert when user experience degrades
3. **Actionable alerts**: Every alert should have a clear response
4. **Progressive disclosure**: Start with high-level metrics, drill down as needed

### The Three Pillars
1. **Metrics**: Numerical data over time
2. **Logs**: Detailed event records
3. **Traces**: Request flow visualization

## Metric Categories

### 1. Technical Metrics

#### Latency
| Metric | Description | Target |
|--------|-------------|--------|
| p50 Latency | Median response time | < 500ms |
| p95 Latency | 95th percentile | < 2s |
| p99 Latency | 99th percentile | < 5s |
| Time to First Token | Streaming start | < 200ms |

**Dashboard Query**:
```promql
histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m]))
```

#### Throughput
| Metric | Description | Target |
|--------|-------------|--------|
| Requests/sec | Total requests | Baseline + 20% |
| Tokens/sec | Processing rate | Monitor trend |
| Concurrent Requests | Active requests | < 80% capacity |

**Dashboard Query**:
```promql
rate(requests_total[1m])
```

#### Error Rates
| Metric | Description | Target |
|--------|-------------|--------|
| Error Rate % | Failed requests | < 1% |
| 5xx Errors | Server errors | < 0.1% |
| Timeout Rate | Timed out requests | < 0.5% |

**Dashboard Query**:
```promql
rate(errors_total[5m]) / rate(requests_total[5m]) * 100
```

#### Resource Utilization
| Metric | Description | Target |
|--------|-------------|--------|
| CPU Usage | Processor utilization | < 70% |
| Memory Usage | RAM utilization | < 80% |
| GPU Utilization | GPU usage | < 90% |
| Disk I/O | Storage operations | < 50% capacity |

### 2. Business Metrics

#### Cost Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Cost per Request | Average cost | Trend down |
| Cost per Token | Token efficiency | Trend down |
| Daily Spend | Total daily cost | Within budget |
| Model Distribution | Usage by model | Optimize mix |

**Dashboard Query**:
```promql
sum(cost_dollars) by (model)
```

#### Usage Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Daily Active Users | Unique users/day | Growth |
| Requests per User | Average usage | Engagement |
| Feature Adoption | Feature usage | > 50% |
| Session Duration | Time per session | Engagement |

### 3. Quality Metrics

#### Semantic Quality
| Metric | Description | Target |
|--------|-------------|--------|
| Hallucination Rate | Incorrect outputs | < 5% |
| Factual Correctness | Accuracy score | > 90% |
| Topic Relevancy | Relevance score | > 85% |
| User Satisfaction | Rating | > 4.0/5 |

**Measurement**:
```python
# LLM-as-judge evaluation
def evaluate_quality(output, expected):
    prompt = f"Rate the quality of: {output}
Expected: {expected}"
    score = llm.generate(prompt)
    return parse_score(score)
```

#### Code Quality (for code generation)
| Metric | Description | Target |
|--------|-------------|--------|
| Compilation Success | Code compiles | > 95% |
| Test Pass Rate | Generated tests pass | > 80% |
| Security Issues | Vulnerabilities | 0 critical |
| Style Compliance | Follows guidelines | > 90% |

### 4. Agent-Specific Metrics

#### Agent Performance
| Metric | Description | Target |
|--------|-------------|--------|
| Task Completion Rate | Successful tasks | > 90% |
| Average Steps per Task | Efficiency | Minimize |
| Tool Call Success | Tool execution | > 95% |
| Context Utilization | Token efficiency | > 70% |

#### Multi-Agent Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Coordination Success | Successful handoffs | > 95% |
| Conflict Rate | Agent conflicts | < 1% |
| Consensus Time | Decision time | < 5s |
| Message Volume | Inter-agent traffic | Monitor |

## Alerting Strategy

### Alert Severity Levels

#### P0 - Critical (Immediate Response)
**Conditions**:
- Error rate > 5%
- p99 latency > 10s
- System unavailable
- Security incident

**Response Time**: < 15 minutes
**Escalation**: Page on-call engineer

**Example**:
```yaml
alert: HighErrorRate
expr: rate(errors_total[5m]) / rate(requests_total[5m]) > 0.05
for: 2m
labels:
  severity: critical
annotations:
  summary: "Error rate is {{ $value }}%"
  runbook_url: "https://wiki/runbooks/high-error-rate"
```

#### P1 - High (Urgent Response)
**Conditions**:
- Error rate > 1%
- p95 latency > 5s
- Resource usage > 90%
- Cost spike > 200%

**Response Time**: < 1 hour
**Escalation**: Notify team channel

**Example**:
```yaml
alert: ElevatedLatency
expr: histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m])) > 5
for: 5m
labels:
  severity: high
annotations:
  summary: "p95 latency is {{ $value }}s"
```

#### P2 - Medium (Standard Response)
**Conditions**:
- Error rate > 0.5%
- p50 latency > 1s
- Resource usage > 80%
- Cost variance > 50%

**Response Time**: < 4 hours
**Escalation**: Create ticket

#### P3 - Low (Planned Response)
**Conditions**:
- Minor performance degradation
- Non-critical issues
- Enhancement opportunities

**Response Time**: < 1 week
**Escalation**: Backlog item

### Alert Best Practices

#### Do
- [ ] Include runbook links
- [ ] Provide context in alert
- [ ] Set appropriate thresholds
- [ ] Test alert routing
- [ ] Regular alert review

#### Don't
- [ ] Alert on causes (alert on symptoms)
- [ ] Create alert fatigue
- [ ] Set static thresholds without context
- [ ] Ignore false positives
- [ ] Forget to update runbooks

## Dashboard Design

### Executive Dashboard
**Audience**: Leadership, stakeholders

**Metrics**:
- System availability (SLA)
- Cost trends
- User adoption
- Key incidents

**Layout**:
```
┌─────────────────────────────────────────┐
│  Availability    Cost Trend    Users   │
│    99.9%         ↓ 15%        ↑ 25%    │
├─────────────────────────────────────────┤
│         Incidents (Last 30 Days)        │
│  P0: 0    P1: 2    P2: 5    P3: 12     │
└─────────────────────────────────────────┘
```

### Engineering Dashboard
**Audience**: Engineering team

**Metrics**:
- Latency percentiles
- Error rates
- Throughput
- Resource utilization

**Layout**:
```
┌─────────────────────────────────────────┐
│  Latency (p50/p95/p99)   Error Rate    │
│  200ms / 800ms / 2s        0.5%        │
├─────────────────────────────────────────┤
│  Requests/sec    CPU    Memory    GPU   │
│    150           45%     60%      70%   │
└─────────────────────────────────────────┘
```

### AI-Specific Dashboard
**Audience**: ML/AI team

**Metrics**:
- Hallucination rate
- Token efficiency
- Model distribution
- Quality scores

**Layout**:
```
┌─────────────────────────────────────────┐
│  Hallucination    Token Eff.   Quality │
│     3.2%           72%          4.2/5  │
├─────────────────────────────────────────┤
│         Model Usage Distribution        │
│  GPT-4: 20%  GPT-3.5: 60%  Claude: 20% │
└─────────────────────────────────────────┘
```

### Cost Dashboard
**Audience**: Finance, engineering

**Metrics**:
- Daily spend
- Cost per request
- Model costs
- Budget variance

**Layout**:
```
┌─────────────────────────────────────────┐
│  Daily Spend    Cost/Request   Budget   │
│   $450            $0.03        85%      │
├─────────────────────────────────────────┤
│           Cost by Model ($/day)         │
│  GPT-4: $200  GPT-3.5: $150  Other: $100│
└─────────────────────────────────────────┘
```

## Log Management

### Log Levels
| Level | Use Case | Retention |
|-------|----------|-----------|
| DEBUG | Development troubleshooting | 7 days |
| INFO | Normal operations | 30 days |
| WARN | Issues requiring attention | 90 days |
| ERROR | Errors requiring investigation | 1 year |
| CRITICAL | System failures | 1 year |

### Structured Logging
```json
{
  "timestamp": "2025-01-21T10:30:00Z",
  "level": "INFO",
  "service": "ai-agent",
  "trace_id": "abc-123",
  "user_id": "user-456",
  "event": "code_generated",
  "model": "gpt-4",
  "tokens": 150,
  "latency_ms": 1200,
  "success": true
}
```

### Log Analysis Queries
```sql
-- Error analysis
SELECT error_type, COUNT(*) 
FROM logs 
WHERE level = 'ERROR' 
  AND timestamp > NOW() - INTERVAL '1 hour'
GROUP BY error_type;

-- Slow requests
SELECT trace_id, latency_ms 
FROM logs 
WHERE latency_ms > 5000 
  AND timestamp > NOW() - INTERVAL '1 hour';
```

## Distributed Tracing

### Trace Structure
```
Trace: request-123
├── Span: api-gateway (100ms)
├── Span: auth-service (50ms)
├── Span: ai-agent (2000ms)
│   ├── Span: context-retrieval (500ms)
│   ├── Span: llm-call (1200ms)
│   └── Span: post-processing (300ms)
└── Span: response-formatting (100ms)
```

### Key Spans to Trace
- API gateway entry
- Authentication
- Context retrieval
- LLM calls
- Tool executions
- Response formatting

## SLOs and SLIs

### Service Level Indicators (SLIs)
| SLI | Definition | Measurement |
|-----|------------|-------------|
| Availability | % of successful requests | (total - errors) / total |
| Latency | Response time | p95 over 1 minute |
| Quality | Output correctness | Human/AI evaluation |
| Cost | $ per request | Total cost / requests |

### Service Level Objectives (SLOs)
| SLO | Target | Error Budget |
|-----|--------|--------------|
| Availability | 99.9% | 0.1% (43 min/month) |
| Latency p95 | < 2s | 5% of requests |
| Quality Score | > 4.0/5 | 10% of outputs |
| Cost per Request | <$0.05 | 20% variance |

### Error Budget Policy
```
Error Budget = 100% - SLO

If error budget exhausted:
1. Halt feature releases
2. Focus on reliability
3. Review and improve
4. Reset budget next period
```

## Incident Response

### Incident Severity
| Level | Description | Response |
|-------|-------------|----------|
| SEV1 | Complete outage | All hands |
| SEV2 | Major degradation | On-call + team |
| SEV3 | Minor issues | On-call |
| SEV4 | Low impact | Ticket |

### Response Runbook
1. **Detect**: Alert fires
2. **Acknowledge**: Claim the incident
3. **Assess**: Determine severity
4. **Mitigate**: Stop the bleeding
5. **Fix**: Root cause resolution
6. **Verify**: Confirm resolution
7. **Document**: Post-mortem

## Monitoring Tools

### Recommended Stack
| Layer | Tool | Purpose |
|-------|------|---------|
| Metrics | Prometheus | Time-series data |
| Visualization | Grafana | Dashboards |
| Logs | ELK / Loki | Log aggregation |
| Tracing | Jaeger / Zipkin | Distributed traces |
| Alerting | PagerDuty / Opsgenie | Incident management |
| APM | Datadog / New Relic | Full observability |

### Open Source Alternative
- Metrics: Prometheus + Grafana
- Logs: Loki + Grafana
- Tracing: Jaeger
- Alerting: Alertmanager

## Monitoring Checklist

### Setup
- [ ] Metrics collection configured
- [ ] Dashboards created
- [ ] Alerts defined
- [ ] Runbooks written
- [ ] On-call rotation set

### Validation
- [ ] Test alerts fire correctly
- [ ] Verify dashboard accuracy
- [ ] Confirm log aggregation
- [ ] Test trace collection
- [ ] Validate SLOs

### Maintenance
- [ ] Weekly alert review
- [ ] Monthly dashboard updates
- [ ] Quarterly SLO review
- [ ] Annual monitoring audit

---

*Effective monitoring is essential for operating AI coding systems at scale. Start with the basics and iterate based on operational experience.*

# Monitoring and Alerting Guide

Comprehensive guide for monitoring autonomous AI coding systems.

## Monitoring Philosophy

### Key Principles
1. **Monitor what matters**: Focus on metrics that indicate system health and user value
2. **Alert on symptoms, not causes**: Alert when user experience degrades
3. **Actionable alerts**: Every alert should have a clear response
4. **Progressive disclosure**: Start with high-level metrics, drill down as needed

### The Three Pillars
1. **Metrics**: Numerical data over time
2. **Logs**: Detailed event records
3. **Traces**: Request flow visualization

## Metric Categories

### 1. Technical Metrics

#### Latency
| Metric | Description | Target |
|--------|-------------|--------|
| p50 Latency | Median response time | < 500ms |
| p95 Latency | 95th percentile | < 2s |
| p99 Latency | 99th percentile | < 5s |
| Time to First Token | Streaming start | < 200ms |

**Dashboard Query**:
```promql
histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m]))
```

#### Throughput
| Metric | Description | Target |
|--------|-------------|--------|
| Requests/sec | Total requests | Baseline + 20% |
| Tokens/sec | Processing rate | Monitor trend |
| Concurrent Requests | Active requests | < 80% capacity |

**Dashboard Query**:
```promql
rate(requests_total[1m])
```

#### Error Rates
| Metric | Description | Target |
|--------|-------------|--------|
| Error Rate % | Failed requests | < 1% |
| 5xx Errors | Server errors | < 0.1% |
| Timeout Rate | Timed out requests | < 0.5% |

**Dashboard Query**:
```promql
rate(errors_total[5m]) / rate(requests_total[5m]) * 100
```

#### Resource Utilization
| Metric | Description | Target |
|--------|-------------|--------|
| CPU Usage | Processor utilization | < 70% |
| Memory Usage | RAM utilization | < 80% |
| GPU Utilization | GPU usage | < 90% |
| Disk I/O | Storage operations | < 50% capacity |

### 2. Business Metrics

#### Cost Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Cost per Request | Average cost | Trend down |
| Cost per Token | Token efficiency | Trend down |
| Daily Spend | Total daily cost | Within budget |
| Model Distribution | Usage by model | Optimize mix |

**Dashboard Query**:
```promql
sum(cost_dollars) by (model)
```

#### Usage Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Daily Active Users | Unique users/day | Growth |
| Requests per User | Average usage | Engagement |
| Feature Adoption | Feature usage | > 50% |
| Session Duration | Time per session | Engagement |

### 3. Quality Metrics

#### Semantic Quality
| Metric | Description | Target |
|--------|-------------|--------|
| Hallucination Rate | Incorrect outputs | < 5% |
| Factual Correctness | Accuracy score | > 90% |
| Topic Relevancy | Relevance score | > 85% |
| User Satisfaction | Rating | > 4.0/5 |

**Measurement**:
```python
# LLM-as-judge evaluation
def evaluate_quality(output, expected):
    prompt = f"Rate the quality of: {output}
Expected: {expected}"
    score = llm.generate(prompt)
    return parse_score(score)
```

#### Code Quality (for code generation)
| Metric | Description | Target |
|--------|-------------|--------|
| Compilation Success | Code compiles | > 95% |
| Test Pass Rate | Generated tests pass | > 80% |
| Security Issues | Vulnerabilities | 0 critical |
| Style Compliance | Follows guidelines | > 90% |

### 4. Agent-Specific Metrics

#### Agent Performance
| Metric | Description | Target |
|--------|-------------|--------|
| Task Completion Rate | Successful tasks | > 90% |
| Average Steps per Task | Efficiency | Minimize |
| Tool Call Success | Tool execution | > 95% |
| Context Utilization | Token efficiency | > 70% |

#### Multi-Agent Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Coordination Success | Successful handoffs | > 95% |
| Conflict Rate | Agent conflicts | < 1% |
| Consensus Time | Decision time | < 5s |
| Message Volume | Inter-agent traffic | Monitor |

## Alerting Strategy

### Alert Severity Levels

#### P0 - Critical (Immediate Response)
**Conditions**:
- Error rate > 5%
- p99 latency > 10s
- System unavailable
- Security incident

**Response Time**: < 15 minutes
**Escalation**: Page on-call engineer

**Example**:
```yaml
alert: HighErrorRate
expr: rate(errors_total[5m]) / rate(requests_total[5m]) > 0.05
for: 2m
labels:
  severity: critical
annotations:
  summary: "Error rate is {{ $value }}%"
  runbook_url: "https://wiki/runbooks/high-error-rate"
```

#### P1 - High (Urgent Response)
**Conditions**:
- Error rate > 1%
- p95 latency > 5s
- Resource usage > 90%
- Cost spike > 200%

**Response Time**: < 1 hour
**Escalation**: Notify team channel

**Example**:
```yaml
alert: ElevatedLatency
expr: histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m])) > 5
for: 5m
labels:
  severity: high
annotations:
  summary: "p95 latency is {{ $value }}s"
```

#### P2 - Medium (Standard Response)
**Conditions**:
- Error rate > 0.5%
- p50 latency > 1s
- Resource usage > 80%
- Cost variance > 50%

**Response Time**: < 4 hours
**Escalation**: Create ticket

#### P3 - Low (Planned Response)
**Conditions**:
- Minor performance degradation
- Non-critical issues
- Enhancement opportunities

**Response Time**: < 1 week
**Escalation**: Backlog item

### Alert Best Practices

#### Do
- [ ] Include runbook links
- [ ] Provide context in alert
- [ ] Set appropriate thresholds
- [ ] Test alert routing
- [ ] Regular alert review

#### Don't
- [ ] Alert on causes (alert on symptoms)
- [ ] Create alert fatigue
- [ ] Set static thresholds without context
- [ ] Ignore false positives
- [ ] Forget to update runbooks

## Dashboard Design

### Executive Dashboard
**Audience**: Leadership, stakeholders

**Metrics**:
- System availability (SLA)
- Cost trends
- User adoption
- Key incidents

**Layout**:
```
┌─────────────────────────────────────────┐
│  Availability    Cost Trend    Users   │
│    99.9%         ↓ 15%        ↑ 25%    │
├─────────────────────────────────────────┤
│         Incidents (Last 30 Days)        │
│  P0: 0    P1: 2    P2: 5    P3: 12     │
└─────────────────────────────────────────┘
```

### Engineering Dashboard
**Audience**: Engineering team

**Metrics**:
- Latency percentiles
- Error rates
- Throughput
- Resource utilization

**Layout**:
```
┌─────────────────────────────────────────┐
│  Latency (p50/p95/p99)   Error Rate    │
│  200ms / 800ms / 2s        0.5%        │
├─────────────────────────────────────────┤
│  Requests/sec    CPU    Memory    GPU   │
│    150           45%     60%      70%   │
└─────────────────────────────────────────┘
```

### AI-Specific Dashboard
**Audience**: ML/AI team

**Metrics**:
- Hallucination rate
- Token efficiency
- Model distribution
- Quality scores

**Layout**:
```
┌─────────────────────────────────────────┐
│  Hallucination    Token Eff.   Quality │
│     3.2%           72%          4.2/5  │
├─────────────────────────────────────────┤
│         Model Usage Distribution        │
│  GPT-4: 20%  GPT-3.5: 60%  Claude: 20% │
└─────────────────────────────────────────┘
```

### Cost Dashboard
**Audience**: Finance, engineering

**Metrics**:
- Daily spend
- Cost per request
- Model costs
- Budget variance

**Layout**:
```
┌─────────────────────────────────────────┐
│  Daily Spend    Cost/Request   Budget   │
│   $450            $0.03        85%      │
├─────────────────────────────────────────┤
│           Cost by Model ($/day)         │
│  GPT-4: $200  GPT-3.5: $150  Other: $100│
└─────────────────────────────────────────┘
```

## Log Management

### Log Levels
| Level | Use Case | Retention |
|-------|----------|-----------|
| DEBUG | Development troubleshooting | 7 days |
| INFO | Normal operations | 30 days |
| WARN | Issues requiring attention | 90 days |
| ERROR | Errors requiring investigation | 1 year |
| CRITICAL | System failures | 1 year |

### Structured Logging
```json
{
  "timestamp": "2025-01-21T10:30:00Z",
  "level": "INFO",
  "service": "ai-agent",
  "trace_id": "abc-123",
  "user_id": "user-456",
  "event": "code_generated",
  "model": "gpt-4",
  "tokens": 150,
  "latency_ms": 1200,
  "success": true
}
```

### Log Analysis Queries
```sql
-- Error analysis
SELECT error_type, COUNT(*) 
FROM logs 
WHERE level = 'ERROR' 
  AND timestamp > NOW() - INTERVAL '1 hour'
GROUP BY error_type;

-- Slow requests
SELECT trace_id, latency_ms 
FROM logs 
WHERE latency_ms > 5000 
  AND timestamp > NOW() - INTERVAL '1 hour';
```

## Distributed Tracing

### Trace Structure
```
Trace: request-123
├── Span: api-gateway (100ms)
├── Span: auth-service (50ms)
├── Span: ai-agent (2000ms)
│   ├── Span: context-retrieval (500ms)
│   ├── Span: llm-call (1200ms)
│   └── Span: post-processing (300ms)
└── Span: response-formatting (100ms)
```

### Key Spans to Trace
- API gateway entry
- Authentication
- Context retrieval
- LLM calls
- Tool executions
- Response formatting

## SLOs and SLIs

### Service Level Indicators (SLIs)
| SLI | Definition | Measurement |
|-----|------------|-------------|
| Availability | % of successful requests | (total - errors) / total |
| Latency | Response time | p95 over 1 minute |
| Quality | Output correctness | Human/AI evaluation |
| Cost | $ per request | Total cost / requests |

### Service Level Objectives (SLOs)
| SLO | Target | Error Budget |
|-----|--------|--------------|
| Availability | 99.9% | 0.1% (43 min/month) |
| Latency p95 | < 2s | 5% of requests |
| Quality Score | > 4.0/5 | 10% of outputs |
| Cost per Request | <$0.05 | 20% variance |

### Error Budget Policy
```
Error Budget = 100% - SLO

If error budget exhausted:
1. Halt feature releases
2. Focus on reliability
3. Review and improve
4. Reset budget next period
```

## Incident Response

### Incident Severity
| Level | Description | Response |
|-------|-------------|----------|
| SEV1 | Complete outage | All hands |
| SEV2 | Major degradation | On-call + team |
| SEV3 | Minor issues | On-call |
| SEV4 | Low impact | Ticket |

### Response Runbook
1. **Detect**: Alert fires
2. **Acknowledge**: Claim the incident
3. **Assess**: Determine severity
4. **Mitigate**: Stop the bleeding
5. **Fix**: Root cause resolution
6. **Verify**: Confirm resolution
7. **Document**: Post-mortem

## Monitoring Tools

### Recommended Stack
| Layer | Tool | Purpose |
|-------|------|---------|
| Metrics | Prometheus | Time-series data |
| Visualization | Grafana | Dashboards |
| Logs | ELK / Loki | Log aggregation |
| Tracing | Jaeger / Zipkin | Distributed traces |
| Alerting | PagerDuty / Opsgenie | Incident management |
| APM | Datadog / New Relic | Full observability |

### Open Source Alternative
- Metrics: Prometheus + Grafana
- Logs: Loki + Grafana
- Tracing: Jaeger
- Alerting: Alertmanager

## Monitoring Checklist

### Setup
- [ ] Metrics collection configured
- [ ] Dashboards created
- [ ] Alerts defined
- [ ] Runbooks written
- [ ] On-call rotation set

### Validation
- [ ] Test alerts fire correctly
- [ ] Verify dashboard accuracy
- [ ] Confirm log aggregation
- [ ] Test trace collection
- [ ] Validate SLOs

### Maintenance
- [ ] Weekly alert review
- [ ] Monthly dashboard updates
- [ ] Quarterly SLO review
- [ ] Annual monitoring audit

---

*Effective monitoring is essential for operating AI coding systems at scale. Start with the basics and iterate based on operational experience.*

# Monitoring and Alerting Guide

Comprehensive guide for monitoring autonomous AI coding systems.

## Monitoring Philosophy

### Key Principles
1. **Monitor what matters**: Focus on metrics that indicate system health and user value
2. **Alert on symptoms, not causes**: Alert when user experience degrades
3. **Actionable alerts**: Every alert should have a clear response
4. **Progressive disclosure**: Start with high-level metrics, drill down as needed

### The Three Pillars
1. **Metrics**: Numerical data over time
2. **Logs**: Detailed event records
3. **Traces**: Request flow visualization

## Metric Categories

### 1. Technical Metrics

#### Latency
| Metric | Description | Target |
|--------|-------------|--------|
| p50 Latency | Median response time | < 500ms |
| p95 Latency | 95th percentile | < 2s |
| p99 Latency | 99th percentile | < 5s |
| Time to First Token | Streaming start | < 200ms |

**Dashboard Query**:
```promql
histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m]))
```

#### Throughput
| Metric | Description | Target |
|--------|-------------|--------|
| Requests/sec | Total requests | Baseline + 20% |
| Tokens/sec | Processing rate | Monitor trend |
| Concurrent Requests | Active requests | < 80% capacity |

**Dashboard Query**:
```promql
rate(requests_total[1m])
```

#### Error Rates
| Metric | Description | Target |
|--------|-------------|--------|
| Error Rate % | Failed requests | < 1% |
| 5xx Errors | Server errors | < 0.1% |
| Timeout Rate | Timed out requests | < 0.5% |

**Dashboard Query**:
```promql
rate(errors_total[5m]) / rate(requests_total[5m]) * 100
```

#### Resource Utilization
| Metric | Description | Target |
|--------|-------------|--------|
| CPU Usage | Processor utilization | < 70% |
| Memory Usage | RAM utilization | < 80% |
| GPU Utilization | GPU usage | < 90% |
| Disk I/O | Storage operations | < 50% capacity |

### 2. Business Metrics

#### Cost Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Cost per Request | Average cost | Trend down |
| Cost per Token | Token efficiency | Trend down |
| Daily Spend | Total daily cost | Within budget |
| Model Distribution | Usage by model | Optimize mix |

**Dashboard Query**:
```promql
sum(cost_dollars) by (model)
```

#### Usage Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Daily Active Users | Unique users/day | Growth |
| Requests per User | Average usage | Engagement |
| Feature Adoption | Feature usage | > 50% |
| Session Duration | Time per session | Engagement |

### 3. Quality Metrics

#### Semantic Quality
| Metric | Description | Target |
|--------|-------------|--------|
| Hallucination Rate | Incorrect outputs | < 5% |
| Factual Correctness | Accuracy score | > 90% |
| Topic Relevancy | Relevance score | > 85% |
| User Satisfaction | Rating | > 4.0/5 |

**Measurement**:
```python
# LLM-as-judge evaluation
def evaluate_quality(output, expected):
    prompt = f"Rate the quality of: {output}
Expected: {expected}"
    score = llm.generate(prompt)
    return parse_score(score)
```

#### Code Quality (for code generation)
| Metric | Description | Target |
|--------|-------------|--------|
| Compilation Success | Code compiles | > 95% |
| Test Pass Rate | Generated tests pass | > 80% |
| Security Issues | Vulnerabilities | 0 critical |
| Style Compliance | Follows guidelines | > 90% |

### 4. Agent-Specific Metrics

#### Agent Performance
| Metric | Description | Target |
|--------|-------------|--------|
| Task Completion Rate | Successful tasks | > 90% |
| Average Steps per Task | Efficiency | Minimize |
| Tool Call Success | Tool execution | > 95% |
| Context Utilization | Token efficiency | > 70% |

#### Multi-Agent Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Coordination Success | Successful handoffs | > 95% |
| Conflict Rate | Agent conflicts | < 1% |
| Consensus Time | Decision time | < 5s |
| Message Volume | Inter-agent traffic | Monitor |

## Alerting Strategy

### Alert Severity Levels

#### P0 - Critical (Immediate Response)
**Conditions**:
- Error rate > 5%
- p99 latency > 10s
- System unavailable
- Security incident

**Response Time**: < 15 minutes
**Escalation**: Page on-call engineer

**Example**:
```yaml
alert: HighErrorRate
expr: rate(errors_total[5m]) / rate(requests_total[5m]) > 0.05
for: 2m
labels:
  severity: critical
annotations:
  summary: "Error rate is {{ $value }}%"
  runbook_url: "https://wiki/runbooks/high-error-rate"
```

#### P1 - High (Urgent Response)
**Conditions**:
- Error rate > 1%
- p95 latency > 5s
- Resource usage > 90%
- Cost spike > 200%

**Response Time**: < 1 hour
**Escalation**: Notify team channel

**Example**:
```yaml
alert: ElevatedLatency
expr: histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m])) > 5
for: 5m
labels:
  severity: high
annotations:
  summary: "p95 latency is {{ $value }}s"
```

#### P2 - Medium (Standard Response)
**Conditions**:
- Error rate > 0.5%
- p50 latency > 1s
- Resource usage > 80%
- Cost variance > 50%

**Response Time**: < 4 hours
**Escalation**: Create ticket

#### P3 - Low (Planned Response)
**Conditions**:
- Minor performance degradation
- Non-critical issues
- Enhancement opportunities

**Response Time**: < 1 week
**Escalation**: Backlog item

### Alert Best Practices

#### Do
- [ ] Include runbook links
- [ ] Provide context in alert
- [ ] Set appropriate thresholds
- [ ] Test alert routing
- [ ] Regular alert review

#### Don't
- [ ] Alert on causes (alert on symptoms)
- [ ] Create alert fatigue
- [ ] Set static thresholds without context
- [ ] Ignore false positives
- [ ] Forget to update runbooks

## Dashboard Design

### Executive Dashboard
**Audience**: Leadership, stakeholders

**Metrics**:
- System availability (SLA)
- Cost trends
- User adoption
- Key incidents

**Layout**:
```
┌─────────────────────────────────────────┐
│  Availability    Cost Trend    Users   │
│    99.9%         ↓ 15%        ↑ 25%    │
├─────────────────────────────────────────┤
│         Incidents (Last 30 Days)        │
│  P0: 0    P1: 2    P2: 5    P3: 12     │
└─────────────────────────────────────────┘
```

### Engineering Dashboard
**Audience**: Engineering team

**Metrics**:
- Latency percentiles
- Error rates
- Throughput
- Resource utilization

**Layout**:
```
┌─────────────────────────────────────────┐
│  Latency (p50/p95/p99)   Error Rate    │
│  200ms / 800ms / 2s        0.5%        │
├─────────────────────────────────────────┤
│  Requests/sec    CPU    Memory    GPU   │
│    150           45%     60%      70%   │
└─────────────────────────────────────────┘
```

### AI-Specific Dashboard
**Audience**: ML/AI team

**Metrics**:
- Hallucination rate
- Token efficiency
- Model distribution
- Quality scores

**Layout**:
```
┌─────────────────────────────────────────┐
│  Hallucination    Token Eff.   Quality │
│     3.2%           72%          4.2/5  │
├─────────────────────────────────────────┤
│         Model Usage Distribution        │
│  GPT-4: 20%  GPT-3.5: 60%  Claude: 20% │
└─────────────────────────────────────────┘
```

### Cost Dashboard
**Audience**: Finance, engineering

**Metrics**:
- Daily spend
- Cost per request
- Model costs
- Budget variance

**Layout**:
```
┌─────────────────────────────────────────┐
│  Daily Spend    Cost/Request   Budget   │
│   $450            $0.03        85%      │
├─────────────────────────────────────────┤
│           Cost by Model ($/day)         │
│  GPT-4: $200  GPT-3.5: $150  Other: $100│
└─────────────────────────────────────────┘
```

## Log Management

### Log Levels
| Level | Use Case | Retention |
|-------|----------|-----------|
| DEBUG | Development troubleshooting | 7 days |
| INFO | Normal operations | 30 days |
| WARN | Issues requiring attention | 90 days |
| ERROR | Errors requiring investigation | 1 year |
| CRITICAL | System failures | 1 year |

### Structured Logging
```json
{
  "timestamp": "2025-01-21T10:30:00Z",
  "level": "INFO",
  "service": "ai-agent",
  "trace_id": "abc-123",
  "user_id": "user-456",
  "event": "code_generated",
  "model": "gpt-4",
  "tokens": 150,
  "latency_ms": 1200,
  "success": true
}
```

### Log Analysis Queries
```sql
-- Error analysis
SELECT error_type, COUNT(*) 
FROM logs 
WHERE level = 'ERROR' 
  AND timestamp > NOW() - INTERVAL '1 hour'
GROUP BY error_type;

-- Slow requests
SELECT trace_id, latency_ms 
FROM logs 
WHERE latency_ms > 5000 
  AND timestamp > NOW() - INTERVAL '1 hour';
```

## Distributed Tracing

### Trace Structure
```
Trace: request-123
├── Span: api-gateway (100ms)
├── Span: auth-service (50ms)
├── Span: ai-agent (2000ms)
│   ├── Span: context-retrieval (500ms)
│   ├── Span: llm-call (1200ms)
│   └── Span: post-processing (300ms)
└── Span: response-formatting (100ms)
```

### Key Spans to Trace
- API gateway entry
- Authentication
- Context retrieval
- LLM calls
- Tool executions
- Response formatting

## SLOs and SLIs

### Service Level Indicators (SLIs)
| SLI | Definition | Measurement |
|-----|------------|-------------|
| Availability | % of successful requests | (total - errors) / total |
| Latency | Response time | p95 over 1 minute |
| Quality | Output correctness | Human/AI evaluation |
| Cost | $ per request | Total cost / requests |

### Service Level Objectives (SLOs)
| SLO | Target | Error Budget |
|-----|--------|--------------|
| Availability | 99.9% | 0.1% (43 min/month) |
| Latency p95 | < 2s | 5% of requests |
| Quality Score | > 4.0/5 | 10% of outputs |
| Cost per Request | <$0.05 | 20% variance |

### Error Budget Policy
```
Error Budget = 100% - SLO

If error budget exhausted:
1. Halt feature releases
2. Focus on reliability
3. Review and improve
4. Reset budget next period
```

## Incident Response

### Incident Severity
| Level | Description | Response |
|-------|-------------|----------|
| SEV1 | Complete outage | All hands |
| SEV2 | Major degradation | On-call + team |
| SEV3 | Minor issues | On-call |
| SEV4 | Low impact | Ticket |

### Response Runbook
1. **Detect**: Alert fires
2. **Acknowledge**: Claim the incident
3. **Assess**: Determine severity
4. **Mitigate**: Stop the bleeding
5. **Fix**: Root cause resolution
6. **Verify**: Confirm resolution
7. **Document**: Post-mortem

## Monitoring Tools

### Recommended Stack
| Layer | Tool | Purpose |
|-------|------|---------|
| Metrics | Prometheus | Time-series data |
| Visualization | Grafana | Dashboards |
| Logs | ELK / Loki | Log aggregation |
| Tracing | Jaeger / Zipkin | Distributed traces |
| Alerting | PagerDuty / Opsgenie | Incident management |
| APM | Datadog / New Relic | Full observability |

### Open Source Alternative
- Metrics: Prometheus + Grafana
- Logs: Loki + Grafana
- Tracing: Jaeger
- Alerting: Alertmanager

## Monitoring Checklist

### Setup
- [ ] Metrics collection configured
- [ ] Dashboards created
- [ ] Alerts defined
- [ ] Runbooks written
- [ ] On-call rotation set

### Validation
- [ ] Test alerts fire correctly
- [ ] Verify dashboard accuracy
- [ ] Confirm log aggregation
- [ ] Test trace collection
- [ ] Validate SLOs

### Maintenance
- [ ] Weekly alert review
- [ ] Monthly dashboard updates
- [ ] Quarterly SLO review
- [ ] Annual monitoring audit

---

*Effective monitoring is essential for operating AI coding systems at scale. Start with the basics and iterate based on operational experience.*

# Monitoring and Alerting Guide

Comprehensive guide for monitoring autonomous AI coding systems.

## Monitoring Philosophy

### Key Principles
1. **Monitor what matters**: Focus on metrics that indicate system health and user value
2. **Alert on symptoms, not causes**: Alert when user experience degrades
3. **Actionable alerts**: Every alert should have a clear response
4. **Progressive disclosure**: Start with high-level metrics, drill down as needed

### The Three Pillars
1. **Metrics**: Numerical data over time
2. **Logs**: Detailed event records
3. **Traces**: Request flow visualization

## Metric Categories

### 1. Technical Metrics

#### Latency
| Metric | Description | Target |
|--------|-------------|--------|
| p50 Latency | Median response time | < 500ms |
| p95 Latency | 95th percentile | < 2s |
| p99 Latency | 99th percentile | < 5s |
| Time to First Token | Streaming start | < 200ms |

**Dashboard Query**:
```promql
histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m]))
```

#### Throughput
| Metric | Description | Target |
|--------|-------------|--------|
| Requests/sec | Total requests | Baseline + 20% |
| Tokens/sec | Processing rate | Monitor trend |
| Concurrent Requests | Active requests | < 80% capacity |

**Dashboard Query**:
```promql
rate(requests_total[1m])
```

#### Error Rates
| Metric | Description | Target |
|--------|-------------|--------|
| Error Rate % | Failed requests | < 1% |
| 5xx Errors | Server errors | < 0.1% |
| Timeout Rate | Timed out requests | < 0.5% |

**Dashboard Query**:
```promql
rate(errors_total[5m]) / rate(requests_total[5m]) * 100
```

#### Resource Utilization
| Metric | Description | Target |
|--------|-------------|--------|
| CPU Usage | Processor utilization | < 70% |
| Memory Usage | RAM utilization | < 80% |
| GPU Utilization | GPU usage | < 90% |
| Disk I/O | Storage operations | < 50% capacity |

### 2. Business Metrics

#### Cost Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Cost per Request | Average cost | Trend down |
| Cost per Token | Token efficiency | Trend down |
| Daily Spend | Total daily cost | Within budget |
| Model Distribution | Usage by model | Optimize mix |

**Dashboard Query**:
```promql
sum(cost_dollars) by (model)
```

#### Usage Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Daily Active Users | Unique users/day | Growth |
| Requests per User | Average usage | Engagement |
| Feature Adoption | Feature usage | > 50% |
| Session Duration | Time per session | Engagement |

### 3. Quality Metrics

#### Semantic Quality
| Metric | Description | Target |
|--------|-------------|--------|
| Hallucination Rate | Incorrect outputs | < 5% |
| Factual Correctness | Accuracy score | > 90% |
| Topic Relevancy | Relevance score | > 85% |
| User Satisfaction | Rating | > 4.0/5 |

**Measurement**:
```python
# LLM-as-judge evaluation
def evaluate_quality(output, expected):
    prompt = f"Rate the quality of: {output}
Expected: {expected}"
    score = llm.generate(prompt)
    return parse_score(score)
```

#### Code Quality (for code generation)
| Metric | Description | Target |
|--------|-------------|--------|
| Compilation Success | Code compiles | > 95% |
| Test Pass Rate | Generated tests pass | > 80% |
| Security Issues | Vulnerabilities | 0 critical |
| Style Compliance | Follows guidelines | > 90% |

### 4. Agent-Specific Metrics

#### Agent Performance
| Metric | Description | Target |
|--------|-------------|--------|
| Task Completion Rate | Successful tasks | > 90% |
| Average Steps per Task | Efficiency | Minimize |
| Tool Call Success | Tool execution | > 95% |
| Context Utilization | Token efficiency | > 70% |

#### Multi-Agent Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Coordination Success | Successful handoffs | > 95% |
| Conflict Rate | Agent conflicts | < 1% |
| Consensus Time | Decision time | < 5s |
| Message Volume | Inter-agent traffic | Monitor |

## Alerting Strategy

### Alert Severity Levels

#### P0 - Critical (Immediate Response)
**Conditions**:
- Error rate > 5%
- p99 latency > 10s
- System unavailable
- Security incident

**Response Time**: < 15 minutes
**Escalation**: Page on-call engineer

**Example**:
```yaml
alert: HighErrorRate
expr: rate(errors_total[5m]) / rate(requests_total[5m]) > 0.05
for: 2m
labels:
  severity: critical
annotations:
  summary: "Error rate is {{ $value }}%"
  runbook_url: "https://wiki/runbooks/high-error-rate"
```

#### P1 - High (Urgent Response)
**Conditions**:
- Error rate > 1%
- p95 latency > 5s
- Resource usage > 90%
- Cost spike > 200%

**Response Time**: < 1 hour
**Escalation**: Notify team channel

**Example**:
```yaml
alert: ElevatedLatency
expr: histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m])) > 5
for: 5m
labels:
  severity: high
annotations:
  summary: "p95 latency is {{ $value }}s"
```

#### P2 - Medium (Standard Response)
**Conditions**:
- Error rate > 0.5%
- p50 latency > 1s
- Resource usage > 80%
- Cost variance > 50%

**Response Time**: < 4 hours
**Escalation**: Create ticket

#### P3 - Low (Planned Response)
**Conditions**:
- Minor performance degradation
- Non-critical issues
- Enhancement opportunities

**Response Time**: < 1 week
**Escalation**: Backlog item

### Alert Best Practices

#### Do
- [ ] Include runbook links
- [ ] Provide context in alert
- [ ] Set appropriate thresholds
- [ ] Test alert routing
- [ ] Regular alert review

#### Don't
- [ ] Alert on causes (alert on symptoms)
- [ ] Create alert fatigue
- [ ] Set static thresholds without context
- [ ] Ignore false positives
- [ ] Forget to update runbooks

## Dashboard Design

### Executive Dashboard
**Audience**: Leadership, stakeholders

**Metrics**:
- System availability (SLA)
- Cost trends
- User adoption
- Key incidents

**Layout**:
```
┌─────────────────────────────────────────┐
│  Availability    Cost Trend    Users   │
│    99.9%         ↓ 15%        ↑ 25%    │
├─────────────────────────────────────────┤
│         Incidents (Last 30 Days)        │
│  P0: 0    P1: 2    P2: 5    P3: 12     │
└─────────────────────────────────────────┘
```

### Engineering Dashboard
**Audience**: Engineering team

**Metrics**:
- Latency percentiles
- Error rates
- Throughput
- Resource utilization

**Layout**:
```
┌─────────────────────────────────────────┐
│  Latency (p50/p95/p99)   Error Rate    │
│  200ms / 800ms / 2s        0.5%        │
├─────────────────────────────────────────┤
│  Requests/sec    CPU    Memory    GPU   │
│    150           45%     60%      70%   │
└─────────────────────────────────────────┘
```

### AI-Specific Dashboard
**Audience**: ML/AI team

**Metrics**:
- Hallucination rate
- Token efficiency
- Model distribution
- Quality scores

**Layout**:
```
┌─────────────────────────────────────────┐
│  Hallucination    Token Eff.   Quality │
│     3.2%           72%          4.2/5  │
├─────────────────────────────────────────┤
│         Model Usage Distribution        │
│  GPT-4: 20%  GPT-3.5: 60%  Claude: 20% │
└─────────────────────────────────────────┘
```

### Cost Dashboard
**Audience**: Finance, engineering

**Metrics**:
- Daily spend
- Cost per request
- Model costs
- Budget variance

**Layout**:
```
┌─────────────────────────────────────────┐
│  Daily Spend    Cost/Request   Budget   │
│   $450            $0.03        85%      │
├─────────────────────────────────────────┤
│           Cost by Model ($/day)         │
│  GPT-4: $200  GPT-3.5: $150  Other: $100│
└─────────────────────────────────────────┘
```

## Log Management

### Log Levels
| Level | Use Case | Retention |
|-------|----------|-----------|
| DEBUG | Development troubleshooting | 7 days |
| INFO | Normal operations | 30 days |
| WARN | Issues requiring attention | 90 days |
| ERROR | Errors requiring investigation | 1 year |
| CRITICAL | System failures | 1 year |

### Structured Logging
```json
{
  "timestamp": "2025-01-21T10:30:00Z",
  "level": "INFO",
  "service": "ai-agent",
  "trace_id": "abc-123",
  "user_id": "user-456",
  "event": "code_generated",
  "model": "gpt-4",
  "tokens": 150,
  "latency_ms": 1200,
  "success": true
}
```

### Log Analysis Queries
```sql
-- Error analysis
SELECT error_type, COUNT(*) 
FROM logs 
WHERE level = 'ERROR' 
  AND timestamp > NOW() - INTERVAL '1 hour'
GROUP BY error_type;

-- Slow requests
SELECT trace_id, latency_ms 
FROM logs 
WHERE latency_ms > 5000 
  AND timestamp > NOW() - INTERVAL '1 hour';
```

## Distributed Tracing

### Trace Structure
```
Trace: request-123
├── Span: api-gateway (100ms)
├── Span: auth-service (50ms)
├── Span: ai-agent (2000ms)
│   ├── Span: context-retrieval (500ms)
│   ├── Span: llm-call (1200ms)
│   └── Span: post-processing (300ms)
└── Span: response-formatting (100ms)
```

### Key Spans to Trace
- API gateway entry
- Authentication
- Context retrieval
- LLM calls
- Tool executions
- Response formatting

## SLOs and SLIs

### Service Level Indicators (SLIs)
| SLI | Definition | Measurement |
|-----|------------|-------------|
| Availability | % of successful requests | (total - errors) / total |
| Latency | Response time | p95 over 1 minute |
| Quality | Output correctness | Human/AI evaluation |
| Cost | $ per request | Total cost / requests |

### Service Level Objectives (SLOs)
| SLO | Target | Error Budget |
|-----|--------|--------------|
| Availability | 99.9% | 0.1% (43 min/month) |
| Latency p95 | < 2s | 5% of requests |
| Quality Score | > 4.0/5 | 10% of outputs |
| Cost per Request | <$0.05 | 20% variance |

### Error Budget Policy
```
Error Budget = 100% - SLO

If error budget exhausted:
1. Halt feature releases
2. Focus on reliability
3. Review and improve
4. Reset budget next period
```

## Incident Response

### Incident Severity
| Level | Description | Response |
|-------|-------------|----------|
| SEV1 | Complete outage | All hands |
| SEV2 | Major degradation | On-call + team |
| SEV3 | Minor issues | On-call |
| SEV4 | Low impact | Ticket |

### Response Runbook
1. **Detect**: Alert fires
2. **Acknowledge**: Claim the incident
3. **Assess**: Determine severity
4. **Mitigate**: Stop the bleeding
5. **Fix**: Root cause resolution
6. **Verify**: Confirm resolution
7. **Document**: Post-mortem

## Monitoring Tools

### Recommended Stack
| Layer | Tool | Purpose |
|-------|------|---------|
| Metrics | Prometheus | Time-series data |
| Visualization | Grafana | Dashboards |
| Logs | ELK / Loki | Log aggregation |
| Tracing | Jaeger / Zipkin | Distributed traces |
| Alerting | PagerDuty / Opsgenie | Incident management |
| APM | Datadog / New Relic | Full observability |

### Open Source Alternative
- Metrics: Prometheus + Grafana
- Logs: Loki + Grafana
- Tracing: Jaeger
- Alerting: Alertmanager

## Monitoring Checklist

### Setup
- [ ] Metrics collection configured
- [ ] Dashboards created
- [ ] Alerts defined
- [ ] Runbooks written
- [ ] On-call rotation set

### Validation
- [ ] Test alerts fire correctly
- [ ] Verify dashboard accuracy
- [ ] Confirm log aggregation
- [ ] Test trace collection
- [ ] Validate SLOs

### Maintenance
- [ ] Weekly alert review
- [ ] Monthly dashboard updates
- [ ] Quarterly SLO review
- [ ] Annual monitoring audit

---

*Effective monitoring is essential for operating AI coding systems at scale. Start with the basics and iterate based on operational experience.*
