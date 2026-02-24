# Configuration Templates

Ready-to-use templates for common autonomous AI coding scenarios.

---

## Table of Contents

1. [Agent Configuration Templates](#agent-configuration-templates)
2. [MCP Server Configurations](#mcp-server-configurations)
3. [CI/CD Pipeline Templates](#cicd-pipeline-templates)
4. [Monitoring & Observability](#monitoring--observability)
5. [Security Policies](#security-policies)
6. [Cost Optimization Rules](#cost-optimization-rules)

---

## Agent Configuration Templates

### Template 1: Full-Stack Development Agent

```yaml
# fullstack_agent.yaml
agent:
  name: "fullstack-developer"
  version: "1.0.0"
  
  capabilities:
    - frontend_development
    - backend_development
    - database_design
    - api_design
    - testing
    
  model_config:
    primary:
      provider: "anthropic"
      model: "claude-3-5-sonnet-20241022"
      temperature: 0.3
      max_tokens: 8192
    fallback:
      provider: "openai"
      model: "gpt-4o"
      temperature: 0.3
      
  context:
    max_files: 50
    max_tokens: 150000
    cache_enabled: true
    cache_ttl: 3600
    
  tools:
    - file_operations
    - terminal_execution
    - web_search
    - code_analysis
    - git_operations
    
  constraints:
    allowed_directories:
      - "./src"
      - "./tests"
      - "./docs"
    blocked_commands:
      - "rm -rf /"
      - "sudo"
    max_execution_time: 300
    
  workflows:
    feature_development:
      steps:
        - analyze_requirements
        - design_architecture
        - implement_code
        - write_tests
        - run_tests
        - generate_documentation
        - create_pr
        
    bug_fix:
      steps:
        - reproduce_issue
        - root_cause_analysis
        - implement_fix
        - verify_fix
        - regression_test
        - create_pr
```

### Template 2: Code Review Agent

```yaml
# code_review_agent.yaml
agent:
  name: "code-reviewer"
  version: "1.0.0"
  
  capabilities:
    - static_analysis
    - security_scanning
    - performance_analysis
    - style_enforcement
    - best_practices
    
  model_config:
    primary:
      provider: "anthropic"
      model: "claude-3-5-sonnet-20241022"
      temperature: 0.1  # Low for consistency
      
  review_criteria:
    security:
      enabled: true
      severity_threshold: "medium"
      tools:
        - semgrep
        - bandit
        - dependency_check
        
    performance:
      enabled: true
      checks:
        - n_plus_one_queries
        - memory_leaks
        - inefficient_algorithms
        
    style:
      enabled: true
      config_file: ".styleguide.yaml"
      auto_fix: true
      
    testing:
      enabled: true
      min_coverage: 80
      require_unit_tests: true
      require_integration_tests: true
      
  output:
    format: "github_review"
    include_suggestions: true
    include_examples: true
    max_comments: 50
```

### Template 3: DevOps Automation Agent

```yaml
# devops_agent.yaml
agent:
  name: "devops-automation"
  version: "1.0.0"
  
  capabilities:
    - infrastructure_as_code
    - ci_cd_pipeline
    - monitoring_setup
    - security_hardening
    - cost_optimization
    
  model_config:
    primary:
      provider: "anthropic"
      model: "claude-3-5-sonnet-20241022"
      temperature: 0.2
      
  infrastructure:
    providers:
      - aws
      - kubernetes
      - terraform
    compliance:
      - soc2
      - iso27001
      
  automation:
    self_healing:
      enabled: true
      triggers:
        - high_error_rate
        - resource_exhaustion
        - dependency_failure
      actions:
        - restart_service
        - scale_resources
        - rollback_deployment
        
    cost_optimization:
      enabled: true
      schedule: "0 0 * * *"  # Daily
      actions:
        - identify_idle_resources
        - right_size_instances
        - optimize_storage
```

---

## MCP Server Configurations

### Template 4: Codebase Analysis MCP

```json
{
  "mcpServers": {
    "codebase-analyzer": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-codebase"],
      "env": {
        "CODEBASE_PATH": "/workspace",
        "ANALYSIS_DEPTH": "deep",
        "CACHE_ENABLED": "true"
      },
      "capabilities": {
        "tools": [
          {
            "name": "analyze_file",
            "description": "Analyze a single file for complexity, dependencies, and issues"
          },
          {
            "name": "analyze_module",
            "description": "Analyze a module/directory structure"
          },
          {
            "name": "find_dependencies",
            "description": "Find all dependencies of a given file or module"
          },
          {
            "name": "generate_metrics",
            "description": "Generate code quality metrics"
          }
        ]
      }
    }
  }
}
```

### Template 5: Git Operations MCP

```json
{
  "mcpServers": {
    "git-operations": {
      "command": "uvx",
      "args": ["mcp-server-git"],
      "env": {
        "REPO_PATH": "/workspace",
        "GIT_CONFIG_USER_NAME": "AI Agent",
        "GIT_CONFIG_USER_EMAIL": "ai-agent@company.com"
      },
      "capabilities": {
        "tools": [
          {
            "name": "git_status",
            "description": "Get current git status"
          },
          {
            "name": "git_diff",
            "description": "Show differences between commits or working tree"
          },
          {
            "name": "git_log",
            "description": "Show commit history"
          },
          {
            "name": "git_branch",
            "description": "List, create, or delete branches"
          },
          {
            "name": "git_commit",
            "description": "Create a new commit"
          }
        ]
      }
    }
  }
}
```

### Template 6: Database MCP

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost:5432/db",
        "READ_ONLY": "true",
        "QUERY_TIMEOUT": "30000"
      },
      "capabilities": {
        "tools": [
          {
            "name": "query",
            "description": "Execute a read-only SQL query"
          },
          {
            "name": "schema",
            "description": "Get database schema information"
          },
          {
            "name": "tables",
            "description": "List all tables in the database"
          }
        ]
      }
    }
  }
}
```

---

## CI/CD Pipeline Templates

### Template 7: AI-Assisted PR Pipeline

```yaml
# .github/workflows/ai-pr-assistant.yaml
name: AI PR Assistant

on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  ai-analysis:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
      
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          
      - name: Setup AI Agent
        uses: company/ai-agent-action@v1
        with:
          agent-config: .ai-agents/code-review.yaml
          api-key: ${{ secrets.AI_API_KEY }}
          
      - name: Code Analysis
        id: analysis
        run: |
          ai-agent analyze \
            --pr ${{ github.event.pull_request.number }} \
            --output-format json \
            --output-file analysis.json
            
      - name: Security Scan
        run: |
          ai-agent security-scan \
            --pr ${{ github.event.pull_request.number }} \
            --severity-threshold medium
            
      - name: Performance Check
        run: |
          ai-agent performance-check \
            --baseline main \
            --threshold 10%
            
      - name: Post Review Comments
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const analysis = JSON.parse(fs.readFileSync('analysis.json', 'utf8'));
            
            // Post summary
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: analysis.summary
            });
            
            // Post inline comments
            for (const comment of analysis.comments) {
              github.rest.pulls.createReviewComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                pull_number: context.issue.number,
                commit_id: context.payload.pull_request.head.sha,
                path: comment.file,
                line: comment.line,
                body: comment.message
              });
            }
```

### Template 8: Self-Healing Deployment

```yaml
# .github/workflows/self-healing-deploy.yaml
name: Self-Healing Deployment

on:
  push:
    branches: [main]

env:
  DEPLOYMENT_TIMEOUT: 600
  HEALTH_CHECK_RETRIES: 10
  ROLLBACK_ON_FAILURE: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Pre-Deployment Analysis
        run: |
          ai-agent analyze-deployment \
            --commit ${{ github.sha }} \
            --environment production
            
      - name: Deploy with Blue-Green
        run: |
          # Deploy to green environment
          kubectl apply -f k8s/green/
          
          # Wait for rollout
          kubectl rollout status deployment/app-green --timeout=${{ env.DEPLOYMENT_TIMEOUT }}s
          
      - name: AI Health Assessment
        id: health
        run: |
          ai-agent health-check \
            --service app-green \
            --retries ${{ env.HEALTH_CHECK_RETRIES }} \
            --output-file health-status.json
            
      - name: Switch Traffic
        if: steps.health.outcome == 'success'
        run: |
          # Update service to point to green
          kubectl patch service app -p '{"spec":{"selector":{"version":"green"}}}'
          
      - name: Monitor & Self-Heal
        run: |
          ai-agent monitor-deployment \
            --duration 300 \
            --error-threshold 5 \
            --auto-remediate true
            
      - name: Rollback on Failure
        if: failure() && env.ROLLBACK_ON_FAILURE == 'true'
        run: |
          echo "Deployment failed, initiating rollback..."
          kubectl patch service app -p '{"spec":{"selector":{"version":"blue"}}}'
          kubectl rollout undo deployment/app-green
          
          # Notify team
          ai-agent notify \
            --channel "#deployments" \
            --message "Rollback completed for ${{ github.sha }}"
```

---

## Monitoring & Observability

### Template 9: Langfuse Configuration

```yaml
# langfuse-config.yaml
langfuse:
  host: ${LANGFUSE_HOST}
  public_key: ${LANGFUSE_PUBLIC_KEY}
  secret_key: ${LANGFUSE_SECRET_KEY}
  
tracing:
  enabled: true
  sample_rate: 1.0  # 100% in development
  
  # Production: Sample 10% of traces
  # sample_rate: 0.1
  
  capture:
    prompts: true
    responses: true
    metadata: true
    scores: true
    
  masking:
    # Redact sensitive information
    patterns:
      - regex: "\\b\\d{4}[- ]?\\d{4}[- ]?\\d{4}[- ]?\\d{4}\\b"
        replacement: "[CREDIT_CARD_REDACTED]"
      - regex: "\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b"
        replacement: "[EMAIL_REDACTED]"
        
scoring:
  automated:
    - name: "response_quality"
      criteria: "accuracy, relevance, completeness"
      threshold: 0.8
      
    - name: "latency"
      criteria: "time_to_first_token, total_time"
      threshold_ms: 5000
      
    - name: "cost_efficiency"
      criteria: "tokens_used, cost_per_request"
      threshold: 0.01  # $0.01 per request
      
dashboards:
  - name: "Agent Performance"
    widgets:
      - type: "latency_trend"
      - type: "error_rate"
      - type: "cost_per_day"
      - type: "quality_score"
      
  - name: "Model Comparison"
    widgets:
      - type: "model_usage"
      - type: "cost_comparison"
      - type: "quality_by_model"
```

### Template 10: Prometheus Metrics

```yaml
# prometheus-rules.yaml
groups:
  - name: ai_agent_alerts
    interval: 30s
    rules:
      # Latency alerts
      - alert: HighAgentLatency
        expr: |
          histogram_quantile(0.95, 
            rate(ai_agent_request_duration_seconds_bucket[5m])
          ) > 10
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "AI agent latency is high"
          description: "95th percentile latency is {{ $value }}s"
          
      # Error rate alerts
      - alert: HighAgentErrorRate
        expr: |
          rate(ai_agent_requests_failed_total[5m]) /
          rate(ai_agent_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "AI agent error rate is high"
          description: "Error rate is {{ $value | humanizePercentage }}"
          
      # Cost alerts
      - alert: HighDailyCost
        expr: |
          sum(increase(ai_agent_cost_dollars[1d])) > 100
        labels:
          severity: warning
        annotations:
          summary: "Daily AI cost exceeded $100"
          description: "Current daily cost: ${{ $value }}"
          
      # Token usage alerts
      - alert: HighTokenUsage
        expr: |
          rate(ai_agent_tokens_used_total[1h]) > 1000000
        for: 15m
        labels:
          severity: info
        annotations:
          summary: "High token usage detected"
          description: "Token usage: {{ $value }}/hour"
```

---

## Security Policies

### Template 11: AI Security Policy

```yaml
# ai-security-policy.yaml
policy:
  version: "1.0.0"
  enforcement: strict  # strict | warn | audit
  
  data_protection:
    pii_detection:
      enabled: true
      auto_redact: true
      patterns:
        - credit_cards
        - social_security_numbers
        - email_addresses
        - phone_numbers
        - api_keys
        - passwords
        
    code_exposure:
      enabled: true
      blocked_patterns:
        - "\.env"
        - "secrets\\."
        - "password"
        - "api_key"
        - "private_key"
        - "token"
        
    proprietary_code:
      enabled: true
      detection_method: "embedding_similarity"
      threshold: 0.85
      
  access_control:
    rbac:
      enabled: true
      roles:
        - name: "ai_admin"
          permissions:
            - "*"
            
        - name: "ai_developer"
          permissions:
            - "agent:read"
            - "agent:execute"
            - "context:read"
            
        - name: "ai_viewer"
          permissions:
            - "agent:read"
            - "context:read"
            
    audit_logging:
      enabled: true
      retention_days: 365
      log_events:
        - agent_execution
        - context_access
        - model_invocation
        - policy_violation
        
  model_security:
    prompt_injection:
      detection: true
      mitigation: block_and_alert
      
    jailbreak_attempts:
      detection: true
      mitigation: block_and_alert
      
    output_filtering:
      enabled: true
      categories:
        - hate_speech
        - harassment
        - dangerous_content
        - code_vulnerabilities
```

---

## Cost Optimization Rules

### Template 12: LLM Cascading Configuration

```yaml
# llm-cascading.yaml
cascading:
  enabled: true
  default_model: "claude-3-5-sonnet"
  
  rules:
    # Simple tasks → Cheaper models
    - name: "simple_tasks"
      condition:
        task_complexity: "low"
        estimated_tokens: "< 500"
      model: "claude-3-haiku"
      fallback: "claude-3-5-sonnet"
      
    # Code analysis → Balanced
    - name: "code_analysis"
      condition:
        task_type: "code_analysis"
        file_size: "< 1000 lines"
      model: "gpt-4o-mini"
      fallback: "gpt-4o"
      
    # Complex architecture → Premium
    - name: "complex_architecture"
      condition:
        task_type: "architecture_design"
        complexity: "high"
      model: "claude-3-5-sonnet"
      fallback: "claude-3-opus"
      
    # Emergency fixes → Fastest
    - name: "emergency_fix"
      condition:
        priority: "critical"
        sla: "< 5 minutes"
      model: "gpt-4o"
      timeout: 30
      
  caching:
    enabled: true
    ttl_seconds: 3600
    similarity_threshold: 0.95
    cache_key_fields:
      - prompt_hash
      - model_name
      - temperature
      
  batching:
    enabled: true
    max_batch_size: 10
    max_wait_ms: 100
    
  cost_limits:
    daily_budget: 500  # USD
    per_request_max: 5  # USD
    alert_threshold: 80  # Percentage of budget
```

### Template 13: Resource Optimization

```yaml
# resource-optimization.yaml
optimization:
  context_management:
    strategy: "hybrid"
    
    rag:
      enabled: true
      chunk_size: 512
      overlap: 128
      top_k: 5
      use_for: ["codebase_wide_queries", "documentation_search"]
      
    long_context:
      enabled: true
      max_tokens: 150000
      use_for: ["focused_file_analysis", "debugging_sessions"]
      
    caching:
      enabled: true
      strategy: "semantic"
      ttl: 3600
      
  compute:
    auto_scaling:
      enabled: true
      min_instances: 2
      max_instances: 20
      target_cpu: 70
      target_memory: 80
      
    spot_instances:
      enabled: true
      percentage: 50
      fallback_on_interrupt: true
      
  storage:
    vector_db:
      type: "pinecone"  # pinecone | weaviate | qdrant
      tier: "standard"  # standard | enterprise
      
    log_retention:
      hot_storage_days: 7
      cold_storage_days: 90
      archive_days: 365
```

---

## Quick Start Commands

### Initialize Agent

```bash
# Install CLI
npm install -g @company/ai-agent-cli

# Initialize project
ai-agent init --template fullstack

# Configure environment
ai-agent config set-model claude-3-5-sonnet
ai-agent config set-context-max 150000
ai-agent config enable-cache

# Verify setup
ai-agent doctor
```

### Run Analysis

```bash
# Analyze codebase
ai-agent analyze --depth deep --output report.json

# Security scan
ai-agent security-scan --severity medium

# Performance check
ai-agent perf-check --baseline main
```

### Deploy Agent

```bash
# Deploy to Kubernetes
ai-agent deploy --environment production --strategy blue-green

# Monitor deployment
ai-agent monitor --duration 300 --auto-remediate
```

---

## Environment Variables

```bash
# Required
export AI_API_KEY="your-api-key"
export LANGFUSE_PUBLIC_KEY="your-public-key"
export LANGFUSE_SECRET_KEY="your-secret-key"

# Optional
export AI_MODEL_DEFAULT="claude-3-5-sonnet"
export AI_TEMPERATURE="0.3"
export AI_MAX_TOKENS="8192"
export AI_CACHE_ENABLED="true"
export AI_LOG_LEVEL="info"
export AI_COST_LIMIT_DAILY="500"
```

---

## Related Resources

- [Integration Patterns](./INTEGRATION_PATTERNS.md) - Detailed integration guides
- [Monitoring Guide](./MONITORING_GUIDE.md) - Observability setup
- [Cost Optimization Playbook](./COST_OPTIMIZATION_PLAYBOOK.md) - Cost reduction strategies
- [Security Hardening](./SECURITY_HARDENING.md) - Security configuration

---

*Templates are provided as starting points. Customize based on your specific requirements and infrastructure.*
