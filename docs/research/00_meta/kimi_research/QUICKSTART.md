# Quick Start Guides

Get up and running with autonomous AI coding in minutes.

---

## Choose Your Path

| Role | Guide | Time | Goal |
|------|-------|------|------|
| **Developer** | [Developer Quick Start](#developer-quick-start) | 15 min | First AI-assisted coding |
| **Team Lead** | [Team Lead Quick Start](#team-lead-quick-start) | 30 min | Team onboarding |
| **Architect** | [Architect Quick Start](#architect-quick-start) | 45 min | System design |
| **DevOps** | [DevOps Quick Start](#devops-quick-start) | 30 min | Infrastructure setup |
| **Stakeholder** | [Stakeholder Quick Start](#stakeholder-quick-start) | 10 min | Understanding value |

---

## Developer Quick Start

### Prerequisites

```bash
# Check versions
node --version  # >= 18
npm --version   # >= 9
git --version   # Any recent version
```

### Step 1: Install AI Agent CLI (2 min)

```bash
# Install globally
npm install -g @company/ai-agent-cli

# Verify installation
ai-agent --version
```

### Step 2: Configure API Key (2 min)

```bash
# Get API key from dashboard
export AI_API_KEY="your-api-key-here"

# Or add to ~/.bashrc or ~/.zshrc
echo 'export AI_API_KEY="your-api-key-here"' >> ~/.bashrc
```

### Step 3: Initialize Project (3 min)

```bash
# Navigate to your project
cd /path/to/your/project

# Initialize AI agent
ai-agent init

# Answer prompts:
# - Project type: (select yours)
# - Primary language: (select yours)
# - Framework: (select yours)
```

### Step 4: First AI-Assisted Task (5 min)

```bash
# Generate a function
ai-agent generate "Create a function to validate email addresses"

# Review the output
# The AI will generate code and explain it

# Generate tests for your code
ai-agent test --file src/validator.js
```

### Step 5: IDE Integration (3 min)

#### VS Code

1. Install "AI Agent" extension
2. Open Command Palette (`Cmd/Ctrl + Shift + P`)
3. Type "AI Agent: Configure"
4. Enter your API key
5. Use `Cmd/Ctrl + Shift + A` to invoke

#### JetBrains

1. Install "AI Agent" plugin from marketplace
2. Go to Settings → AI Agent
3. Enter your API key
4. Use `Alt + A` to invoke

### Common Commands

```bash
# Generate code
ai-agent generate "description of what you want"

# Review code
ai-agent review --file src/file.js

# Generate tests
ai-agent test --file src/file.js --coverage 80

# Explain code
ai-agent explain --file src/file.js

# Refactor code
ai-agent refactor --file src/file.js --goal "improve performance"
```

### Next Steps

- Read [Best Practices](./BEST_PRACTICES.md)
- Check [Quick Reference](./QUICK_REFERENCE.md)
- Explore [Templates](./TEMPLATES.md)

---

## Team Lead Quick Start

### Prerequisites

- Admin access to team repositories
- API key with team quota
- Understanding of team workflows

### Step 1: Team Assessment (5 min)

```bash
# Analyze current codebase
ai-agent analyze --depth team

# Review the report
# Focus on:
# - Code complexity
# - Test coverage
# - Documentation gaps
```

### Step 2: Pilot Team Setup (10 min)

```bash
# Create pilot team configuration
cat > ai-team-config.yaml << EOF
pilot_team:
  name: "Alpha Squad"
  size: 5
  repositories:
    - frontend-app
    - backend-api
  
  ai_features:
    code_review: true
    test_generation: true
    documentation: true
    
  guardrails:
    require_approval: true
    max_tokens_per_day: 100000
    blocked_patterns:
      - "password"
      - "secret"
EOF

# Apply configuration
ai-agent team setup --config ai-team-config.yaml
```

### Step 3: Onboard Pilot Team (10 min)

```bash
# Send onboarding invitations
ai-agent team invite --team alpha-squad --emails "dev1@company.com,dev2@company.com"

# Schedule onboarding session
ai-agent team schedule-training --team alpha-squad --date "2025-02-01"
```

### Step 4: Set Up Monitoring (5 min)

```bash
# Enable team metrics
ai-agent team metrics enable

# Configure alerts
ai-agent team alerts configure \
  --daily-cost-limit 50 \
  --error-rate-threshold 5
```

### Team Metrics Dashboard

Access at: `https://dashboard.company.com/ai-team/alpha-squad`

Key metrics to watch:
- Adoption rate (target: >80% in 2 weeks)
- Code quality score (should improve)
- Time saved per developer
- Cost per feature delivered

### Rollout Plan

| Week | Action | Success Criteria |
|------|--------|------------------|
| 1 | Pilot with 5 developers | 80% daily usage |
| 2 | Expand to 15 developers | Positive feedback |
| 3 | Full team rollout | 70% adoption |
| 4 | Measure impact | 20% productivity gain |

---

## Architect Quick Start

### Prerequisites

- Understanding of system design
- Knowledge of existing architecture
- Access to architecture documentation

### Step 1: Architecture Analysis (10 min)

```bash
# Analyze current architecture
ai-agent analyze --type architecture

# Review findings
# Look for:
# - Integration points
# - Scalability constraints
# - Security considerations
```

### Step 2: Design AI Integration (15 min)

```yaml
# Create architecture specification
# ai-architecture.yaml
ai_system:
  name: "Code Assistant Platform"
  
  components:
    api_gateway:
      type: kong
      rate_limiting: 1000/min
      
    agent_orchestrator:
      type: langgraph
      max_agents: 10
      
    context_manager:
      type: hybrid
      vector_db: pinecone
      cache: redis
      
    model_router:
      strategy: tiered_cascading
      models:
        - claude-3-5-sonnet
        - gpt-4o
        - claude-3-haiku
        
  security:
    input_validation: true
    output_filtering: true
    sandboxing: gvisor
    
  observability:
    tracing: langfuse
    metrics: prometheus
    logs: elasticsearch
```

### Step 3: Review Decision Records (10 min)

```bash
# Review architecture decisions
cat ADRS.md

# Key decisions to understand:
# - Why hybrid orchestration?
# - Why tiered model selection?
# - Why RAG + long context?
```

### Step 4: Create Implementation Plan (10 min)

```bash
# Generate implementation roadmap
ai-agent roadmap generate \
  --architecture ai-architecture.yaml \
  --duration 20-weeks \
  --output roadmap.md
```

### Architecture Review Checklist

- [ ] Scalability requirements met
- [ ] Security controls defined
- [ ] Observability configured
- [ ] Cost controls in place
- [ ] Fallback strategies defined
- [ ] Human oversight configured

---

## DevOps Quick Start

### Prerequisites

- Kubernetes cluster access
- CI/CD pipeline admin access
- Monitoring stack access

### Step 1: Infrastructure Setup (10 min)

```bash
# Deploy AI agent infrastructure
kubectl apply -f k8s/ai-agents/

# Verify deployment
kubectl get pods -n ai-agents
```

### Step 2: Configure CI/CD Integration (10 min)

```yaml
# .github/workflows/ai-assist.yaml
name: AI Assistance

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  ai-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: AI Code Review
        uses: company/ai-review-action@v1
        with:
          api-key: ${{ secrets.AI_API_KEY }}
          config: .ai-config.yaml
```

### Step 3: Set Up Monitoring (5 min)

```bash
# Deploy Prometheus rules
kubectl apply -f monitoring/prometheus-rules.yaml

# Deploy Grafana dashboards
kubectl apply -f monitoring/grafana-dashboards.yaml

# Verify
kubectl get configmaps -n monitoring
```

### Step 4: Configure Alerts (5 min)

```yaml
# alertmanager-config.yaml
alerts:
  - name: high_ai_cost
    condition: daily_cost > 100
    severity: warning
    channel: #devops-alerts
    
  - name: high_error_rate
    condition: error_rate > 5%
    severity: critical
    channel: #on-call
```

### Operational Runbooks

| Scenario | Runbook | Command |
|----------|---------|---------|
| High Cost | [Cost Runbook](./runbooks/high-cost.md) | `ai-agent ops cost-analysis` |
| High Errors | [Error Runbook](./runbooks/high-errors.md) | `ai-agent ops error-analysis` |
| Model Down | [Fallback Runbook](./runbooks/model-down.md) | `ai-agent ops switch-model` |

---

## Stakeholder Quick Start

### What is AI-Assisted Development?

AI-assisted development uses artificial intelligence to help software teams:

- **Write code faster** - AI suggests code completions and generates functions
- **Catch bugs earlier** - AI reviews code for issues before deployment
- **Improve quality** - AI generates tests and documentation
- **Reduce costs** - AI automates repetitive tasks

### Business Value

| Metric | Typical Improvement |
|--------|---------------------|
| Development Speed | 2-3x faster |
| Bug Detection | 60-70% earlier |
| Code Review Time | 50% reduction |
| Documentation | 80% automated |
| Developer Satisfaction | +40% |

### ROI Calculator

```
Team Size: 20 developers
Average Salary: $150,000/year
AI Investment: $50,000/year

Productivity Gain: 30%
Time Saved: 6 hours/week per developer
Annual Value: $900,000

ROI: 1,700%
Payback Period: 3 weeks
```

### Implementation Timeline

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| Assessment | 1 week | Current state analysis |
| Pilot | 4 weeks | 5-person pilot team |
| Expansion | 8 weeks | Full team rollout |
| Optimization | Ongoing | Continuous improvement |

### Success Metrics

Track these KPIs:
- **Velocity**: Story points per sprint
- **Quality**: Bug escape rate
- **Efficiency**: Time to merge
- **Satisfaction**: Developer NPS
- **Cost**: Cost per feature

### Executive Dashboard

Access at: `https://dashboard.company.com/ai-executive`

Key views:
- Team adoption rates
- Productivity metrics
- Cost analysis
- ROI tracking

### Next Steps

1. **Schedule Demo** - See AI in action
2. **Read Executive Summary** - [Executive Summary](./EXECUTIVE_SUMMARY.md)
3. **Review Case Studies** - [Case Studies](./CASE_STUDIES.md)
4. **Assess Readiness** - [Risk Assessment](./RISK_ASSESSMENT.md)

---

## Troubleshooting

### Common Issues

#### "API Key Invalid"

```bash
# Check API key is set
echo $AI_API_KEY

# Verify key format (should start with sk-...)
# Get new key from dashboard if needed
```

#### "Model Not Responding"

```bash
# Check model status
ai-agent status

# Switch to fallback model
ai-agent config set-model gpt-4o
```

#### "Context Too Large"

```bash
# Reduce context size
ai-agent config set-context-max 50000

# Use RAG instead
ai-agent config set-context-strategy rag
```

### Getting Help

| Resource | Link |
|----------|------|
| Documentation | https://docs.company.com |
| Support | support@company.com |
| Community | https://community.company.com |
| Status | https://status.company.com |

---

## Related Resources

- [FAQ](./FAQ.md) - Common questions
- [Troubleshooting Guide](./TROUBLESHOOTING_GUIDE.md) - Detailed problem solving
- [Best Practices](./BEST_PRACTICES.md) - Implementation guidelines
- [Workshop Materials](./WORKSHOP_MATERIALS.md) - Training resources

---

*Quick starts are updated monthly. Last updated: 2025-01-21*
