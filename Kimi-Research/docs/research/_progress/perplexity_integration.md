# Perplexity Space Research Integration: Smoke Test Framework

**Source:** https://www.perplexity.ai/spaces/smoke-test-framework-_L0_2o2dRyaDjDbhcmyOfw  
**Extraction Date:** 2025  
**Research Threads Analyzed:** 8+ substantive threads

---

## Executive Summary

This document synthesizes all substantive research from the "Smoke Test Framework" Perplexity Space, which contains extensive prior work on AI agentic SDLC frameworks, testing infrastructure, MCP servers, agent orchestration, and autonomous development workflows. The space represents 160+ research sources and multiple iterative refinement cycles on designing production-grade autonomous AI coding systems.

### Key Prior Work Identified:
1. **AI Agentic Autonomous SDLC Framework** - Comprehensive requirements across 3 major versions
2. **Smoke Testing Framework Architecture** - Playwright-based enterprise testing platform design
3. **Agent Skills & Workflows Research** - 200+ curated skills from major AI coding tools
4. **Tiny AI Models for Testing** - Docker-optimized models for selector adaptation
5. **ZenFlow Integration** - 24-step autonomous workflow for evidence-driven development
6. **Frontend Analysis Methodology** - Code relationship database approach

---

## 1. Agentic SDLC Patterns Research

### 1.1 Core Architecture Requirements (R-001 to R-014)

**Source Thread:** AI Agentic Autonomous SDLC Framework (Requirements v1-v3)

#### Key Findings:

**Autonomous Requirements Engineering (R-001)**
- Problem: AI agents fail when requirements are insufficient
- Solution: Multi-phase requirements engineering pipeline:
  - Intake → Intent Inference → Clarification Generation → Research Phase → Requirements Formalization → Adversarial Review → Stakeholder Validation Gate
- Format: BDD/Gherkin for unambiguous acceptance criteria
- Research Basis: Spec-driven development research shows under-investing in specs is the #1 failure mode

**Hierarchical Task Decomposition (R-002)**
- Following the Planning Pattern: Goal Analysis → Phase Decomposition → Task Decomposition → Dependency Mapping → Context Scoping → Task Specification
- Each atomic task receives its own concrete requirement document
- MINIMUM context principle to reduce token usage and hallucination risk

**Multi-Model Consensus Verification (R-003)**
- Primary model (Kimi K2.5) → Secondary verification (Sonnet 4.6) → Tertiary arbitration (GPT-5.3)
- Consensus scoring algorithm based on ICE and MUSE research
- Behavioral testing + adversarial challenge approach

**GitHub-Native Task Tracking Architecture**
- GitHub becomes single source of truth for all project state
- Framework Concept → GitHub Object mapping:
  - SDLC Project → GitHub Milestone
  - SDLC Phase → GitHub Label (phase:requirements, phase:design, etc.)
  - Atomic Task → GitHub Issue
  - Task Implementation → GitHub Branch + PR
  - Verification Results → PR Comment
  - Quality Gate Decision → GitHub Label (gate:pass, gate:fail)

### 1.2 Tool Capabilities Matrix

Research across 8 specified tools:

| Capability | Kilo Code | Roo Code | ZenFlow | GitHub Copilot | Claude Code | Codex | Continue | Cline |
|------------|-----------|----------|---------|----------------|-------------|-------|----------|-------|
| Custom modes/roles | YAML modes | Orchestrator + custom | Custom workflows | Custom agents | CLAUDE.md + skills | Skills system | ❌ | Custom modes |
| Multi-agent orchestration | Orchestrator mode | Cloud agents + orchestrator | Parallel agents | Coding agent + agents panel | Agent Teams (3-5) | Multi-threaded | ❌ | ❌ |
| Spec-driven development | Via custom workflows | Via modes | Core feature (SDD) | Via custom instructions | Via CLAUDE.md | Via skills | ❌ | Via rules |
| Multi-model verification | Manual mode switching | Provider-per-mode | Committee approach | ❌ | Team model selection | ❌ | ❌ | Model switching |
| Sandboxed execution | ❌ Local only | Cloud sandboxes | Isolated environments | GitHub Actions sandbox | Local execution | Native sandboxing | N/A | ❌ Local only |
| MCP support | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ Limited | ❌ | ✅ |

**Key Finding:** ZenFlow is the only tool with native spec-driven development and multi-agent verification ("committee approach") as core features.

### 1.3 Workflow Engine Evaluation

**Contenders Analyzed:**

| Framework | Core Paradigm | Primary Strength | Maturity |
|-----------|---------------|------------------|----------|
| LangGraph | Graph-based stateful workflows | Explicit DAG control, branching, debugging | Most mature (106k ★) |
| CrewAI | Role-based team coordination | YAML-driven, intuitive setup | Mid-maturity (30k+ ★) |
| AutoGen | Conversational multi-agent | Dialogue-driven, flexible topologies | Research-oriented (43.1k+ ★) |
| OpenAI Agents SDK | Lightweight primitives | Minimal abstractions, fast deployment | Newest |

**Head-to-Head Comparison (Key Criteria):**

| Criterion | LangGraph | CrewAI | AutoGen | OpenAI Agents SDK |
|-----------|-----------|--------|---------|-------------------|
| Workflow complexity | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| State management | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Parallelization | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Observability | ⭐⭐⭐⭐⭐ (LangSmith/Langfuse) | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Error handling | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Token efficiency | ⭐⭐⭐⭐⭐ (lowest latency) | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| Production readiness | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

**Recommendation:** LangGraph is superior for SDLC framework due to:
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability with state transition logs and visual graph traces
- Lowest latency and token usage in benchmarks
- Native parallel execution for independent subtasks
- Conditional edges for gating decisions and retry mechanisms

---

## 2. MCP Servers Research

### 2.1 Protocol Understanding

**MCP (Model Context Protocol)** by Anthropic:
- Standard for giving agents access to external tools, data sources, and APIs
- Official repository: `modelcontextprotocol/servers`
- Hundreds of community servers for GitHub, Git, Slack, databases, browsers

**A2A (Agent2Agent) Protocol** by Google (Linux Foundation):
- Enables agents built on different frameworks to discover each other
- Uses JSON-RPC 2.0 over HTTPS
- Complementary to MCP: A2A handles agent-to-agent, MCP handles agent-to-tool

### 2.2 GitHub MCP Server Integration

**Key Tools Available:**
- `create_issue` / `update_issue` — Task creation and status updates
- `create_pull_request` / `merge_pull_request` — Implementation tracking
- `create_branch` — Isolation for atomic tasks
- `add_issue_comment` — Posting verification results, cost data, adversarial findings
- `add_labels` — Phase tracking, gate status, priority
- `assign_copilot_to_issue` — Delegate additional work to Copilot agent
- `search_issues` / `list_pull_requests` — Orchestrator reads project state

### 2.3 Event-Driven Pipeline Architecture

```
Event Flow:
1. LangGraph orchestrator decomposes task → creates GitHub Issue
2. GitHub Issue creation triggers Kilo webhook
3. Kilo Cloud Agent clones repo, creates branch, implements task
4. Kilo Cloud Agent auto-commits and pushes → creates PR
5. PR creation triggers GitHub Agentic Workflow
6. Agentic Workflow runs verification (Code Reviews, tests)
7. Verification results posted as PR comments
8. LangGraph orchestrator reads PR state via GitHub MCP → decides gate
```

---

## 3. Agent Orchestration Research

### 3.1 Inter-Agent Communication Patterns

**Patterns Evaluated:**

| Pattern | How It Works | Best For | Limitations |
|---------|--------------|----------|-------------|
| Subagents | Parent spawns child, receives only results | Simple delegation | No ongoing collaboration |
| Skills | Reusable capabilities agents can invoke | Standardized tasks | Limited context sharing |
| Handoffs | Agent A passes control to Agent B | Sequential workflows | No parallel collaboration |
| Claude Code Agent Teams | Shared task lists, direct messaging, self-coordination | Complex collaboration | Requires Claude Code |
| Roo Code Orchestrator | Hierarchical meta-prompts, context-passing protocols | Structured workflows | Learning curve |

**Key Finding:** Claude Code Agent Teams represent the most advanced inter-agent communication model with shared task lists, direct messaging, and self-coordination capabilities.

### 3.2 Agent Skills Collections

**Top Repositories:**

| Repository | Stars | What It Does |
|------------|-------|--------------|
| anthropic/skills | 61k ★ | Official skills — document creation, design, MCP builder, webapp testing |
| VoltAgent/awesome-agent-skills | 4.7k ★ | Most comprehensive curated list — 200+ skills from major publishers |
| skillcreatorai/Ai-Agent-Skills | — | "Homebrew for AI Agent Skills" — universal installer |

**Standout Skill Categories:**
- **Context Engineering** (by muratcankoylan): context compression, degradation detection, multi-agent patterns, memory systems
- **Security** (by Trail of Bits): 20+ skills including audit context building, static analysis, property-based testing
- **Development** (by obra): subagent-driven development, systematic debugging, root-cause tracing

### 3.3 Multi-Agent Workflow Frameworks

| Framework | Stars | Best For | Approach |
|-----------|-------|----------|----------|
| LangGraph | 106k ★ | Complex workflows with branching logic | Graph-based DAG, explicit state management |
| CrewAI | 30k+ ★ | Fastest time-to-production | Role-based agents with task delegation |
| AutoGen | 43.1k+ ★ | Conversational multi-agent, human-in-loop | Agents chat and iterate naturally |
| Agno | 29k+ ★ | Full-stack multi-agent | Supports all major LLM providers |
| Letta | 15.9k+ ★ | Stateful long-running agents | Memory persistence across sessions |

**Token Efficiency Note:** LangGraph uses ~2,000 tokens per task vs. CrewAI's ~3,500 and AutoGen's ~8,000.

---

## 4. Context Management Research

### 4.1 Context Transfer Protocol

**Spec Artifact Chain Approach:**
- Each SDLC phase produces a spec artifact
- Artifacts are passed along the chain: Requirements Spec → Design Spec → Implementation Spec → Test Spec
- Each artifact includes: context scope, acceptance criteria, constraints, token budget

### 4.2 Context Scoping Principles

**For each atomic task, determine MINIMUM context required:**
- Files needed
- Specs relevant
- Constraints to enforce
- Token budget allocation

### 4.3 Token Optimization Strategies

- Task-specific context reduces bloat
- Avoid conversation history growth
- Use structured JSON output for machine-readable documentation
- Implement context compression for long-running sessions

---

## 5. Testing Frameworks Research

### 5.1 Smoke Testing Framework Architecture

**Core Capabilities (Target State):**

| Capability | Description |
|------------|-------------|
| Universal web interaction engine | Playwright-based, handles all element types, dynamic content, complex forms |
| Dynamic multi-stack orchestration | 3+ containerized test environments (aio, int, prod) with auto port allocation (9330-9399) |
| Intelligent resilience system | Auto retry, element detection strategies, timeout handling, latency tolerance |
| Parallel test execution | Across multiple sites and within same site simultaneously |
| Complete observability stack | WebSocket updates, Prometheus metrics, structured JSON logging, artifact management |
| Database state management | Bidirectional reset supporting PostgreSQL and Oracle |
| Configuration-driven architecture | YAML test definitions |
| Multiple execution interfaces | UI dashboard (Flask), REST API (Express), CLI, programmatic |
| Self-healing capabilities | Element locator fallbacks, intelligent wait strategies, adaptive selectors |

### 5.2 Deviation Detection System

**Deviation Types to Track:**
- Selector Deviations (configured vs. actual selector used)
- Timing Deviations (configured timeout vs. actual wait time)
- Validation Deviations (expected vs. actual error messages)
- Workflow Deviations (configured steps vs. actual execution)
- Data Deviations (expected vs. actual dropdown options)

**Deviation Dashboard Features:**
- Summary View: Total deviations by type, severity, status
- List View: Paginated table with test name, deviation type, timestamp, environment
- Detail View: Side-by-side comparison, visual diff, timeline, frequency chart
- Trend Analysis: Charts showing deviations over time, by module, most common types
- Review Workflow: Assign, comment, batch operations, export reports

### 5.3 Test-Driven Development of UI

**TDD Workflow for Dashboard:**
1. Write tests for desired UI features before implementation
2. Implement UI features to pass tests
3. Validate all UI components work correctly
4. Ensure accessibility compliance
5. Verify responsive design across viewports

---

## 6. CI/CD Patterns Research

### 6.1 GitHub-Native CI/CD Integration

**GitHub Agentic Workflows** (Technical Preview):
- Markdown-defined automations that run coding agents inside GitHub Actions
- Combined with Kilo Code's webhook triggers for event-driven pipeline

### 6.2 Jenkins Integration

**Smoke Test Pipeline:**
- Jenkins triggers deployment → Smoke tests start
- KEDA scales AI analyzer from 0 → 1 pod (5-10 seconds)
- 8 Playwright pods run parallel tests → Call AI service when selectors fail
- AI analyzer handles 20-30 requests/minute
- Tests complete → AI pod scales to 0 after cooldown

### 6.3 Kubernetes Deployment Strategy

**Shared AI Service Pattern (Recommended):**
```
┌─────────────────────────────────────────┐
│  8-Node Kubernetes Cluster              │
├─────────────────────────────────────────┤
│  Smoke Test Pods (6-8 parallel)         │
│  ├─ Playwright container (2GB RAM)      │
│  └─ Calls AI service via HTTP           │
├─────────────────────────────────────────┤
│  AI Analyzer Pod (1-2 replicas)         │
│  ├─ Qwen3-0.6B model (2-3GB RAM)       │
│  └─ Serves all smoke test pods          │
└─────────────────────────────────────────┘
```

**Resource Distribution (8 Nodes @ 4-8 cores, 16-32GB RAM each):**
- Total capacity: 64 CPU cores, 256GB RAM
- Smoke test allocation: 16GB RAM (Playwright) + 3-6GB RAM (AI) = ~20-25GB
- Total consumption: <10% of cluster resources

---

## 7. Tiny AI Models for Testing Research

### 7.1 Model Comparison

| Model | Parameters | Docker Size | Inference Speed | Best For |
|-------|------------|-------------|-----------------|----------|
| SmolLM2-360M | 360M | ~400MB | <100ms | Quick pattern matching, selector analysis |
| Qwen2-0.5B | 500M | ~500MB | ~150ms | Reasoning about failures, context understanding |
| Qwen3-0.6B | 600M | ~600MB | ~5ms/token | Complex decision-making, code understanding |
| Phi-3-mini | 3.8B | ~2.5GB | ~300ms | Complex decision-making, code understanding |

### 7.2 Qwen3-0.6B Deep Dive

**Key Advantages:**
- Released April 2025, trained on 36 trillion tokens across 119 languages
- 32K context window (can analyze entire test suites, DOM snapshots, git diffs)
- Benchmarks: 73% on MATH500, 79.2% on GSM8K, 30.5% on HumanEval
- Built-in agent capabilities for automation and workflow orchestration
- Dual reasoning modes: "thinking" and "non-thinking"

**Resource Requirements:**
- RAM: 8GB total system, ~3GB during inference
- Storage: 3GB for quantized model files
- CPU: 4-8 cores recommended, 2 cores minimum
- Inference speed: 10-30 tokens/second on CPU-only

**Kubernetes Configuration:**
```yaml
resources:
  requests:
    memory: "2Gi"
    cpu: "1000m"
  limits:
    memory: "3Gi"
    cpu: "2000m"
```

### 7.3 Selector Intelligence Layer

**Implementation Approach:**
1. Analyze selector failures and compare current vs. expected DOM structures
2. Evaluate error patterns against historical test data
3. Determine retry worthiness using context (commit messages, recent code changes, error frequency)
4. Provide confidence scores for "legitimate failure" vs. "trivial UI change"

**Decision Framework:**
- Legitimate test failure → FAIL
- Cosmetic change → RETRY
- Timing issue → RETRY
- Environmental → RETRY

---

## 8. ZenFlow Integration Research

### 8.1 ZenFlow Core Concepts

**Four Pillars:**
1. Structured Workflows
2. SDD (Spec-Driven Development)
3. Multi-Agent Verification
4. Parallel Execution

### 8.2 24-Step Custom Workflow

**Phases:**
1. Planning
2. Design
3. Architecture
4. Implementation
5. Review
6. Testing
7. Validation
8. Optimization
9. Refactoring
10. Performance Optimization
11. Production Polish

### 8.3 Evidence-Driven Development

**Zen Rules:**
- All decisions must be based on empirical evidence
- No assumptions without verification
- Continuous validation at each phase
- Automated verification gates

---

## 9. Frontend Analysis Methodology Research

### 9.1 Code Relationship Database Approach

**Core Problem Addressed:**
"I do not know what connects to what, code paths are uncertain, and I need a method to ensure everything is mapped, tested, and maintainable."

**Solution:** Graph database approach treating code as queryable graph structure
- Nodes = files, functions, components
- Edges = imports, calls, relationships
- Enables powerful queries about codebase

### 9.2 Deliverables Created

| Deliverable | Lines | Purpose |
|-------------|-------|---------|
| IMPLEMENTATION_SUMMARY.md | 600 | Complete system overview |
| frontend_analysis_plan.md | 929 | 22-day roadmap, 8 phases |
| quick_start_guide.md | 311 | 30-minute insights |
| tools/dependency_mapper.py | 341 | Automated codebase analysis |
| tools/generate_graph_visualization.html | 536 | Interactive dependency graph |
| VISUAL_ROADMAP.md | 738 | Flowcharts and diagrams |

### 9.3 Key Innovations

- **Graph Database Approach:** Queryable code relationships
- **AI Agent Compatibility:** Structured JSON output, machine-readable documentation
- **Evidence-Based Methods:** Tools from 2026 research (FalkorDB, GitKraken Codemaps, Vitest, Playwright)

---

## 10. Sources Discovered in Space

### 10.1 Official Documentation
- LangGraph Documentation (langchain-ai.github.io)
- Langfuse Documentation (langfuse.com)
- ZenFlow Documentation (zenflow.ai)
- Claude Code Documentation (code.claude.ai)
- GitHub Copilot Documentation (github.com)
- OpenAI Codex Documentation (openai.com)

### 10.2 Research Papers
- FastFlowLM: Efficient LLM Inference (github.com)
- Speculative Decoding Research (AMD dev reports)
- AI-SDLC Maturity Model (eleks.com)

### 10.3 GitHub Repositories
- modelcontextprotocol/servers (MCP servers)
- anthropic/skills (61k ★)
- VoltAgent/awesome-agent-skills (4.7k ★)
- langchain-ai/langgraph (106k ★)
- crewAIInc/crewAI (30k+ ★)
- microsoft/autogen (43.1k+ ★)

### 10.4 Industry Sources
- prnewswire.com (Claude Code Agent Teams)
- xebia.com (Kilo Code/Roo Code analysis)
- intuitionlabs.ai (OpenAI Codex automation)
- linkedin.com (BDD/Gherkin acceptance criteria)
- thoughtworks.com (shift-left involvement)

---

## 11. Research Gaps Identified

### 11.1 Remaining Gaps After Prior Work Integration

1. **MCP Server Ecosystem Deep Dive**
   - Prior work identified MCP protocol but didn't exhaustively catalog all available servers
   - Gap: Complete inventory of production-ready MCP servers by category

2. **A2A Protocol Implementation Details**
   - Prior work mentioned A2A but didn't explore implementation patterns
   - Gap: Concrete A2A integration examples for agent-to-agent communication

3. **Local LLM Deployment Patterns**
   - Prior work mentioned local models but focused on cloud
   - Gap: Comprehensive local LLM deployment architecture for air-gapped environments

4. **Cross-Framework Agent Interoperability**
   - Prior work compared frameworks but didn't address interoperability
   - Gap: Patterns for agents from different frameworks to collaborate

5. **Production Hardening Patterns**
   - Prior work focused on architecture design
   - Gap: Operational runbooks, monitoring, alerting for production agent systems

6. **Security & Compliance for Agent Systems**
   - Prior work mentioned security briefly
   - Gap: Comprehensive security framework for autonomous agent systems

7. **Cost Optimization at Scale**
   - Prior work mentioned cost tracking
   - Gap: Advanced cost optimization strategies for enterprise-scale deployments

### 11.2 Cross-References to Research Taxonomy

| Taxonomy Category | Prior Work Coverage | Gap Status |
|-------------------|---------------------|------------|
| Agentic SDLC Patterns | Comprehensive (v1-v3) | Minor gaps in implementation details |
| MCP Servers | Protocol identified | Needs server catalog |
| Agent Orchestration | LangGraph recommended | Needs A2A implementation |
| Context Management | Spec artifact chain defined | Needs compression strategies |
| Testing Frameworks | Smoke testing architecture | Needs production hardening |
| CI/CD Patterns | GitHub-native approach | Needs operational runbooks |

---

## 12. Key Decisions & Conclusions from Prior Work

### 12.1 Workflow Engine Decision
**Decision:** Use LangGraph  
**Rationale:** 
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability
- Lowest latency and token usage
- Native parallel execution

### 12.2 Model Selection Decision
**Decision:** Kimi K2.5 as primary, Sonnet 4.6, GPT-5.3, Gemini 3 Pro/Flash  
**Rationale:**
- Cost optimization (Kimi is cheapest)
- Escalation path for complex tasks
- Multi-model consensus verification

### 12.3 Task Tracking Decision
**Decision:** GitHub-native (Issues, PRs, branches)  
**Rationale:**
- Permanent, auditable record
- Human-readable project state
- Native CI/CD integration
- Built-in collaboration

### 12.4 Testing Approach Decision
**Decision:** Behavioral testing + consensus-based evaluation + adversarial challenge  
**Rationale:**
- Empirical verification
- Reduces false positives
- Catches edge cases

### 12.5 Local vs Cloud Decision
**Decision:** Hybrid approach  
**Rationale:**
- Local for planning/design (cost, privacy)
- Cloud for implementation (speed)
- Local for final validation (accuracy)

---

## 13. Integration Recommendations

### 13.1 For New Research

1. **Build on LangGraph Foundation**
   - Prior work already selected LangGraph; new research should assume this baseline
   - Focus on graph node/edge design patterns

2. **Extend GitHub-Native Approach**
   - Use GitHub as single source of truth
   - Leverage GitHub MCP server for automation

3. **Incorporate ZenFlow Patterns**
   - Use 24-step workflow as reference
   - Apply evidence-driven development principles

4. **Leverage Tiny AI Models**
   - Qwen3-0.6B for selector intelligence
   - Deploy as shared service in K8s

### 13.2 For Implementation

1. **Start with Smoke Testing Framework**
   - Prior work includes comprehensive architecture
   - Use as proving ground for agentic patterns

2. **Implement Deviation Detection Early**
   - Critical for self-healing capabilities
   - Enables continuous improvement

3. **Use Kilo Code Cloud Agents**
   - For PR reviews and webhook automation
   - Integrates with GitHub-native workflow

---

## 14. Summary Statistics

| Metric | Value |
|--------|-------|
| Research Threads Analyzed | 8+ |
| Sources Cited | 160+ |
| Requirements Versions | 3 (v1 → v2 → v3) |
| Tools Evaluated | 8 |
| Workflow Frameworks Compared | 4 |
| AI Models Analyzed | 4+ |
| SDLC Phases Defined | 7 |
| GitHub Repositories Referenced | 15+ |

---

## 15. Document Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025 | Initial extraction and synthesis from Perplexity Space |

---

*This document represents a comprehensive integration of all substantive research found in the "Smoke Test Framework" Perplexity Space. It should be treated as a living document and updated as new research emerges.*

# Perplexity Space Research Integration: Smoke Test Framework

**Source:** https://www.perplexity.ai/spaces/smoke-test-framework-_L0_2o2dRyaDjDbhcmyOfw  
**Extraction Date:** 2025  
**Research Threads Analyzed:** 8+ substantive threads

---

## Executive Summary

This document synthesizes all substantive research from the "Smoke Test Framework" Perplexity Space, which contains extensive prior work on AI agentic SDLC frameworks, testing infrastructure, MCP servers, agent orchestration, and autonomous development workflows. The space represents 160+ research sources and multiple iterative refinement cycles on designing production-grade autonomous AI coding systems.

### Key Prior Work Identified:
1. **AI Agentic Autonomous SDLC Framework** - Comprehensive requirements across 3 major versions
2. **Smoke Testing Framework Architecture** - Playwright-based enterprise testing platform design
3. **Agent Skills & Workflows Research** - 200+ curated skills from major AI coding tools
4. **Tiny AI Models for Testing** - Docker-optimized models for selector adaptation
5. **ZenFlow Integration** - 24-step autonomous workflow for evidence-driven development
6. **Frontend Analysis Methodology** - Code relationship database approach

---

## 1. Agentic SDLC Patterns Research

### 1.1 Core Architecture Requirements (R-001 to R-014)

**Source Thread:** AI Agentic Autonomous SDLC Framework (Requirements v1-v3)

#### Key Findings:

**Autonomous Requirements Engineering (R-001)**
- Problem: AI agents fail when requirements are insufficient
- Solution: Multi-phase requirements engineering pipeline:
  - Intake → Intent Inference → Clarification Generation → Research Phase → Requirements Formalization → Adversarial Review → Stakeholder Validation Gate
- Format: BDD/Gherkin for unambiguous acceptance criteria
- Research Basis: Spec-driven development research shows under-investing in specs is the #1 failure mode

**Hierarchical Task Decomposition (R-002)**
- Following the Planning Pattern: Goal Analysis → Phase Decomposition → Task Decomposition → Dependency Mapping → Context Scoping → Task Specification
- Each atomic task receives its own concrete requirement document
- MINIMUM context principle to reduce token usage and hallucination risk

**Multi-Model Consensus Verification (R-003)**
- Primary model (Kimi K2.5) → Secondary verification (Sonnet 4.6) → Tertiary arbitration (GPT-5.3)
- Consensus scoring algorithm based on ICE and MUSE research
- Behavioral testing + adversarial challenge approach

**GitHub-Native Task Tracking Architecture**
- GitHub becomes single source of truth for all project state
- Framework Concept → GitHub Object mapping:
  - SDLC Project → GitHub Milestone
  - SDLC Phase → GitHub Label (phase:requirements, phase:design, etc.)
  - Atomic Task → GitHub Issue
  - Task Implementation → GitHub Branch + PR
  - Verification Results → PR Comment
  - Quality Gate Decision → GitHub Label (gate:pass, gate:fail)

### 1.2 Tool Capabilities Matrix

Research across 8 specified tools:

| Capability | Kilo Code | Roo Code | ZenFlow | GitHub Copilot | Claude Code | Codex | Continue | Cline |
|------------|-----------|----------|---------|----------------|-------------|-------|----------|-------|
| Custom modes/roles | YAML modes | Orchestrator + custom | Custom workflows | Custom agents | CLAUDE.md + skills | Skills system | ❌ | Custom modes |
| Multi-agent orchestration | Orchestrator mode | Cloud agents + orchestrator | Parallel agents | Coding agent + agents panel | Agent Teams (3-5) | Multi-threaded | ❌ | ❌ |
| Spec-driven development | Via custom workflows | Via modes | Core feature (SDD) | Via custom instructions | Via CLAUDE.md | Via skills | ❌ | Via rules |
| Multi-model verification | Manual mode switching | Provider-per-mode | Committee approach | ❌ | Team model selection | ❌ | ❌ | Model switching |
| Sandboxed execution | ❌ Local only | Cloud sandboxes | Isolated environments | GitHub Actions sandbox | Local execution | Native sandboxing | N/A | ❌ Local only |
| MCP support | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ Limited | ❌ | ✅ |

**Key Finding:** ZenFlow is the only tool with native spec-driven development and multi-agent verification ("committee approach") as core features.

### 1.3 Workflow Engine Evaluation

**Contenders Analyzed:**

| Framework | Core Paradigm | Primary Strength | Maturity |
|-----------|---------------|------------------|----------|
| LangGraph | Graph-based stateful workflows | Explicit DAG control, branching, debugging | Most mature (106k ★) |
| CrewAI | Role-based team coordination | YAML-driven, intuitive setup | Mid-maturity (30k+ ★) |
| AutoGen | Conversational multi-agent | Dialogue-driven, flexible topologies | Research-oriented (43.1k+ ★) |
| OpenAI Agents SDK | Lightweight primitives | Minimal abstractions, fast deployment | Newest |

**Head-to-Head Comparison (Key Criteria):**

| Criterion | LangGraph | CrewAI | AutoGen | OpenAI Agents SDK |
|-----------|-----------|--------|---------|-------------------|
| Workflow complexity | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| State management | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Parallelization | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Observability | ⭐⭐⭐⭐⭐ (LangSmith/Langfuse) | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Error handling | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Token efficiency | ⭐⭐⭐⭐⭐ (lowest latency) | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| Production readiness | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

**Recommendation:** LangGraph is superior for SDLC framework due to:
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability with state transition logs and visual graph traces
- Lowest latency and token usage in benchmarks
- Native parallel execution for independent subtasks
- Conditional edges for gating decisions and retry mechanisms

---

## 2. MCP Servers Research

### 2.1 Protocol Understanding

**MCP (Model Context Protocol)** by Anthropic:
- Standard for giving agents access to external tools, data sources, and APIs
- Official repository: `modelcontextprotocol/servers`
- Hundreds of community servers for GitHub, Git, Slack, databases, browsers

**A2A (Agent2Agent) Protocol** by Google (Linux Foundation):
- Enables agents built on different frameworks to discover each other
- Uses JSON-RPC 2.0 over HTTPS
- Complementary to MCP: A2A handles agent-to-agent, MCP handles agent-to-tool

### 2.2 GitHub MCP Server Integration

**Key Tools Available:**
- `create_issue` / `update_issue` — Task creation and status updates
- `create_pull_request` / `merge_pull_request` — Implementation tracking
- `create_branch` — Isolation for atomic tasks
- `add_issue_comment` — Posting verification results, cost data, adversarial findings
- `add_labels` — Phase tracking, gate status, priority
- `assign_copilot_to_issue` — Delegate additional work to Copilot agent
- `search_issues` / `list_pull_requests` — Orchestrator reads project state

### 2.3 Event-Driven Pipeline Architecture

```
Event Flow:
1. LangGraph orchestrator decomposes task → creates GitHub Issue
2. GitHub Issue creation triggers Kilo webhook
3. Kilo Cloud Agent clones repo, creates branch, implements task
4. Kilo Cloud Agent auto-commits and pushes → creates PR
5. PR creation triggers GitHub Agentic Workflow
6. Agentic Workflow runs verification (Code Reviews, tests)
7. Verification results posted as PR comments
8. LangGraph orchestrator reads PR state via GitHub MCP → decides gate
```

---

## 3. Agent Orchestration Research

### 3.1 Inter-Agent Communication Patterns

**Patterns Evaluated:**

| Pattern | How It Works | Best For | Limitations |
|---------|--------------|----------|-------------|
| Subagents | Parent spawns child, receives only results | Simple delegation | No ongoing collaboration |
| Skills | Reusable capabilities agents can invoke | Standardized tasks | Limited context sharing |
| Handoffs | Agent A passes control to Agent B | Sequential workflows | No parallel collaboration |
| Claude Code Agent Teams | Shared task lists, direct messaging, self-coordination | Complex collaboration | Requires Claude Code |
| Roo Code Orchestrator | Hierarchical meta-prompts, context-passing protocols | Structured workflows | Learning curve |

**Key Finding:** Claude Code Agent Teams represent the most advanced inter-agent communication model with shared task lists, direct messaging, and self-coordination capabilities.

### 3.2 Agent Skills Collections

**Top Repositories:**

| Repository | Stars | What It Does |
|------------|-------|--------------|
| anthropic/skills | 61k ★ | Official skills — document creation, design, MCP builder, webapp testing |
| VoltAgent/awesome-agent-skills | 4.7k ★ | Most comprehensive curated list — 200+ skills from major publishers |
| skillcreatorai/Ai-Agent-Skills | — | "Homebrew for AI Agent Skills" — universal installer |

**Standout Skill Categories:**
- **Context Engineering** (by muratcankoylan): context compression, degradation detection, multi-agent patterns, memory systems
- **Security** (by Trail of Bits): 20+ skills including audit context building, static analysis, property-based testing
- **Development** (by obra): subagent-driven development, systematic debugging, root-cause tracing

### 3.3 Multi-Agent Workflow Frameworks

| Framework | Stars | Best For | Approach |
|-----------|-------|----------|----------|
| LangGraph | 106k ★ | Complex workflows with branching logic | Graph-based DAG, explicit state management |
| CrewAI | 30k+ ★ | Fastest time-to-production | Role-based agents with task delegation |
| AutoGen | 43.1k+ ★ | Conversational multi-agent, human-in-loop | Agents chat and iterate naturally |
| Agno | 29k+ ★ | Full-stack multi-agent | Supports all major LLM providers |
| Letta | 15.9k+ ★ | Stateful long-running agents | Memory persistence across sessions |

**Token Efficiency Note:** LangGraph uses ~2,000 tokens per task vs. CrewAI's ~3,500 and AutoGen's ~8,000.

---

## 4. Context Management Research

### 4.1 Context Transfer Protocol

**Spec Artifact Chain Approach:**
- Each SDLC phase produces a spec artifact
- Artifacts are passed along the chain: Requirements Spec → Design Spec → Implementation Spec → Test Spec
- Each artifact includes: context scope, acceptance criteria, constraints, token budget

### 4.2 Context Scoping Principles

**For each atomic task, determine MINIMUM context required:**
- Files needed
- Specs relevant
- Constraints to enforce
- Token budget allocation

### 4.3 Token Optimization Strategies

- Task-specific context reduces bloat
- Avoid conversation history growth
- Use structured JSON output for machine-readable documentation
- Implement context compression for long-running sessions

---

## 5. Testing Frameworks Research

### 5.1 Smoke Testing Framework Architecture

**Core Capabilities (Target State):**

| Capability | Description |
|------------|-------------|
| Universal web interaction engine | Playwright-based, handles all element types, dynamic content, complex forms |
| Dynamic multi-stack orchestration | 3+ containerized test environments (aio, int, prod) with auto port allocation (9330-9399) |
| Intelligent resilience system | Auto retry, element detection strategies, timeout handling, latency tolerance |
| Parallel test execution | Across multiple sites and within same site simultaneously |
| Complete observability stack | WebSocket updates, Prometheus metrics, structured JSON logging, artifact management |
| Database state management | Bidirectional reset supporting PostgreSQL and Oracle |
| Configuration-driven architecture | YAML test definitions |
| Multiple execution interfaces | UI dashboard (Flask), REST API (Express), CLI, programmatic |
| Self-healing capabilities | Element locator fallbacks, intelligent wait strategies, adaptive selectors |

### 5.2 Deviation Detection System

**Deviation Types to Track:**
- Selector Deviations (configured vs. actual selector used)
- Timing Deviations (configured timeout vs. actual wait time)
- Validation Deviations (expected vs. actual error messages)
- Workflow Deviations (configured steps vs. actual execution)
- Data Deviations (expected vs. actual dropdown options)

**Deviation Dashboard Features:**
- Summary View: Total deviations by type, severity, status
- List View: Paginated table with test name, deviation type, timestamp, environment
- Detail View: Side-by-side comparison, visual diff, timeline, frequency chart
- Trend Analysis: Charts showing deviations over time, by module, most common types
- Review Workflow: Assign, comment, batch operations, export reports

### 5.3 Test-Driven Development of UI

**TDD Workflow for Dashboard:**
1. Write tests for desired UI features before implementation
2. Implement UI features to pass tests
3. Validate all UI components work correctly
4. Ensure accessibility compliance
5. Verify responsive design across viewports

---

## 6. CI/CD Patterns Research

### 6.1 GitHub-Native CI/CD Integration

**GitHub Agentic Workflows** (Technical Preview):
- Markdown-defined automations that run coding agents inside GitHub Actions
- Combined with Kilo Code's webhook triggers for event-driven pipeline

### 6.2 Jenkins Integration

**Smoke Test Pipeline:**
- Jenkins triggers deployment → Smoke tests start
- KEDA scales AI analyzer from 0 → 1 pod (5-10 seconds)
- 8 Playwright pods run parallel tests → Call AI service when selectors fail
- AI analyzer handles 20-30 requests/minute
- Tests complete → AI pod scales to 0 after cooldown

### 6.3 Kubernetes Deployment Strategy

**Shared AI Service Pattern (Recommended):**
```
┌─────────────────────────────────────────┐
│  8-Node Kubernetes Cluster              │
├─────────────────────────────────────────┤
│  Smoke Test Pods (6-8 parallel)         │
│  ├─ Playwright container (2GB RAM)      │
│  └─ Calls AI service via HTTP           │
├─────────────────────────────────────────┤
│  AI Analyzer Pod (1-2 replicas)         │
│  ├─ Qwen3-0.6B model (2-3GB RAM)       │
│  └─ Serves all smoke test pods          │
└─────────────────────────────────────────┘
```

**Resource Distribution (8 Nodes @ 4-8 cores, 16-32GB RAM each):**
- Total capacity: 64 CPU cores, 256GB RAM
- Smoke test allocation: 16GB RAM (Playwright) + 3-6GB RAM (AI) = ~20-25GB
- Total consumption: <10% of cluster resources

---

## 7. Tiny AI Models for Testing Research

### 7.1 Model Comparison

| Model | Parameters | Docker Size | Inference Speed | Best For |
|-------|------------|-------------|-----------------|----------|
| SmolLM2-360M | 360M | ~400MB | <100ms | Quick pattern matching, selector analysis |
| Qwen2-0.5B | 500M | ~500MB | ~150ms | Reasoning about failures, context understanding |
| Qwen3-0.6B | 600M | ~600MB | ~5ms/token | Complex decision-making, code understanding |
| Phi-3-mini | 3.8B | ~2.5GB | ~300ms | Complex decision-making, code understanding |

### 7.2 Qwen3-0.6B Deep Dive

**Key Advantages:**
- Released April 2025, trained on 36 trillion tokens across 119 languages
- 32K context window (can analyze entire test suites, DOM snapshots, git diffs)
- Benchmarks: 73% on MATH500, 79.2% on GSM8K, 30.5% on HumanEval
- Built-in agent capabilities for automation and workflow orchestration
- Dual reasoning modes: "thinking" and "non-thinking"

**Resource Requirements:**
- RAM: 8GB total system, ~3GB during inference
- Storage: 3GB for quantized model files
- CPU: 4-8 cores recommended, 2 cores minimum
- Inference speed: 10-30 tokens/second on CPU-only

**Kubernetes Configuration:**
```yaml
resources:
  requests:
    memory: "2Gi"
    cpu: "1000m"
  limits:
    memory: "3Gi"
    cpu: "2000m"
```

### 7.3 Selector Intelligence Layer

**Implementation Approach:**
1. Analyze selector failures and compare current vs. expected DOM structures
2. Evaluate error patterns against historical test data
3. Determine retry worthiness using context (commit messages, recent code changes, error frequency)
4. Provide confidence scores for "legitimate failure" vs. "trivial UI change"

**Decision Framework:**
- Legitimate test failure → FAIL
- Cosmetic change → RETRY
- Timing issue → RETRY
- Environmental → RETRY

---

## 8. ZenFlow Integration Research

### 8.1 ZenFlow Core Concepts

**Four Pillars:**
1. Structured Workflows
2. SDD (Spec-Driven Development)
3. Multi-Agent Verification
4. Parallel Execution

### 8.2 24-Step Custom Workflow

**Phases:**
1. Planning
2. Design
3. Architecture
4. Implementation
5. Review
6. Testing
7. Validation
8. Optimization
9. Refactoring
10. Performance Optimization
11. Production Polish

### 8.3 Evidence-Driven Development

**Zen Rules:**
- All decisions must be based on empirical evidence
- No assumptions without verification
- Continuous validation at each phase
- Automated verification gates

---

## 9. Frontend Analysis Methodology Research

### 9.1 Code Relationship Database Approach

**Core Problem Addressed:**
"I do not know what connects to what, code paths are uncertain, and I need a method to ensure everything is mapped, tested, and maintainable."

**Solution:** Graph database approach treating code as queryable graph structure
- Nodes = files, functions, components
- Edges = imports, calls, relationships
- Enables powerful queries about codebase

### 9.2 Deliverables Created

| Deliverable | Lines | Purpose |
|-------------|-------|---------|
| IMPLEMENTATION_SUMMARY.md | 600 | Complete system overview |
| frontend_analysis_plan.md | 929 | 22-day roadmap, 8 phases |
| quick_start_guide.md | 311 | 30-minute insights |
| tools/dependency_mapper.py | 341 | Automated codebase analysis |
| tools/generate_graph_visualization.html | 536 | Interactive dependency graph |
| VISUAL_ROADMAP.md | 738 | Flowcharts and diagrams |

### 9.3 Key Innovations

- **Graph Database Approach:** Queryable code relationships
- **AI Agent Compatibility:** Structured JSON output, machine-readable documentation
- **Evidence-Based Methods:** Tools from 2026 research (FalkorDB, GitKraken Codemaps, Vitest, Playwright)

---

## 10. Sources Discovered in Space

### 10.1 Official Documentation
- LangGraph Documentation (langchain-ai.github.io)
- Langfuse Documentation (langfuse.com)
- ZenFlow Documentation (zenflow.ai)
- Claude Code Documentation (code.claude.ai)
- GitHub Copilot Documentation (github.com)
- OpenAI Codex Documentation (openai.com)

### 10.2 Research Papers
- FastFlowLM: Efficient LLM Inference (github.com)
- Speculative Decoding Research (AMD dev reports)
- AI-SDLC Maturity Model (eleks.com)

### 10.3 GitHub Repositories
- modelcontextprotocol/servers (MCP servers)
- anthropic/skills (61k ★)
- VoltAgent/awesome-agent-skills (4.7k ★)
- langchain-ai/langgraph (106k ★)
- crewAIInc/crewAI (30k+ ★)
- microsoft/autogen (43.1k+ ★)

### 10.4 Industry Sources
- prnewswire.com (Claude Code Agent Teams)
- xebia.com (Kilo Code/Roo Code analysis)
- intuitionlabs.ai (OpenAI Codex automation)
- linkedin.com (BDD/Gherkin acceptance criteria)
- thoughtworks.com (shift-left involvement)

---

## 11. Research Gaps Identified

### 11.1 Remaining Gaps After Prior Work Integration

1. **MCP Server Ecosystem Deep Dive**
   - Prior work identified MCP protocol but didn't exhaustively catalog all available servers
   - Gap: Complete inventory of production-ready MCP servers by category

2. **A2A Protocol Implementation Details**
   - Prior work mentioned A2A but didn't explore implementation patterns
   - Gap: Concrete A2A integration examples for agent-to-agent communication

3. **Local LLM Deployment Patterns**
   - Prior work mentioned local models but focused on cloud
   - Gap: Comprehensive local LLM deployment architecture for air-gapped environments

4. **Cross-Framework Agent Interoperability**
   - Prior work compared frameworks but didn't address interoperability
   - Gap: Patterns for agents from different frameworks to collaborate

5. **Production Hardening Patterns**
   - Prior work focused on architecture design
   - Gap: Operational runbooks, monitoring, alerting for production agent systems

6. **Security & Compliance for Agent Systems**
   - Prior work mentioned security briefly
   - Gap: Comprehensive security framework for autonomous agent systems

7. **Cost Optimization at Scale**
   - Prior work mentioned cost tracking
   - Gap: Advanced cost optimization strategies for enterprise-scale deployments

### 11.2 Cross-References to Research Taxonomy

| Taxonomy Category | Prior Work Coverage | Gap Status |
|-------------------|---------------------|------------|
| Agentic SDLC Patterns | Comprehensive (v1-v3) | Minor gaps in implementation details |
| MCP Servers | Protocol identified | Needs server catalog |
| Agent Orchestration | LangGraph recommended | Needs A2A implementation |
| Context Management | Spec artifact chain defined | Needs compression strategies |
| Testing Frameworks | Smoke testing architecture | Needs production hardening |
| CI/CD Patterns | GitHub-native approach | Needs operational runbooks |

---

## 12. Key Decisions & Conclusions from Prior Work

### 12.1 Workflow Engine Decision
**Decision:** Use LangGraph  
**Rationale:** 
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability
- Lowest latency and token usage
- Native parallel execution

### 12.2 Model Selection Decision
**Decision:** Kimi K2.5 as primary, Sonnet 4.6, GPT-5.3, Gemini 3 Pro/Flash  
**Rationale:**
- Cost optimization (Kimi is cheapest)
- Escalation path for complex tasks
- Multi-model consensus verification

### 12.3 Task Tracking Decision
**Decision:** GitHub-native (Issues, PRs, branches)  
**Rationale:**
- Permanent, auditable record
- Human-readable project state
- Native CI/CD integration
- Built-in collaboration

### 12.4 Testing Approach Decision
**Decision:** Behavioral testing + consensus-based evaluation + adversarial challenge  
**Rationale:**
- Empirical verification
- Reduces false positives
- Catches edge cases

### 12.5 Local vs Cloud Decision
**Decision:** Hybrid approach  
**Rationale:**
- Local for planning/design (cost, privacy)
- Cloud for implementation (speed)
- Local for final validation (accuracy)

---

## 13. Integration Recommendations

### 13.1 For New Research

1. **Build on LangGraph Foundation**
   - Prior work already selected LangGraph; new research should assume this baseline
   - Focus on graph node/edge design patterns

2. **Extend GitHub-Native Approach**
   - Use GitHub as single source of truth
   - Leverage GitHub MCP server for automation

3. **Incorporate ZenFlow Patterns**
   - Use 24-step workflow as reference
   - Apply evidence-driven development principles

4. **Leverage Tiny AI Models**
   - Qwen3-0.6B for selector intelligence
   - Deploy as shared service in K8s

### 13.2 For Implementation

1. **Start with Smoke Testing Framework**
   - Prior work includes comprehensive architecture
   - Use as proving ground for agentic patterns

2. **Implement Deviation Detection Early**
   - Critical for self-healing capabilities
   - Enables continuous improvement

3. **Use Kilo Code Cloud Agents**
   - For PR reviews and webhook automation
   - Integrates with GitHub-native workflow

---

## 14. Summary Statistics

| Metric | Value |
|--------|-------|
| Research Threads Analyzed | 8+ |
| Sources Cited | 160+ |
| Requirements Versions | 3 (v1 → v2 → v3) |
| Tools Evaluated | 8 |
| Workflow Frameworks Compared | 4 |
| AI Models Analyzed | 4+ |
| SDLC Phases Defined | 7 |
| GitHub Repositories Referenced | 15+ |

---

## 15. Document Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025 | Initial extraction and synthesis from Perplexity Space |

---

*This document represents a comprehensive integration of all substantive research found in the "Smoke Test Framework" Perplexity Space. It should be treated as a living document and updated as new research emerges.*

# Perplexity Space Research Integration: Smoke Test Framework

**Source:** https://www.perplexity.ai/spaces/smoke-test-framework-_L0_2o2dRyaDjDbhcmyOfw  
**Extraction Date:** 2025  
**Research Threads Analyzed:** 8+ substantive threads

---

## Executive Summary

This document synthesizes all substantive research from the "Smoke Test Framework" Perplexity Space, which contains extensive prior work on AI agentic SDLC frameworks, testing infrastructure, MCP servers, agent orchestration, and autonomous development workflows. The space represents 160+ research sources and multiple iterative refinement cycles on designing production-grade autonomous AI coding systems.

### Key Prior Work Identified:
1. **AI Agentic Autonomous SDLC Framework** - Comprehensive requirements across 3 major versions
2. **Smoke Testing Framework Architecture** - Playwright-based enterprise testing platform design
3. **Agent Skills & Workflows Research** - 200+ curated skills from major AI coding tools
4. **Tiny AI Models for Testing** - Docker-optimized models for selector adaptation
5. **ZenFlow Integration** - 24-step autonomous workflow for evidence-driven development
6. **Frontend Analysis Methodology** - Code relationship database approach

---

## 1. Agentic SDLC Patterns Research

### 1.1 Core Architecture Requirements (R-001 to R-014)

**Source Thread:** AI Agentic Autonomous SDLC Framework (Requirements v1-v3)

#### Key Findings:

**Autonomous Requirements Engineering (R-001)**
- Problem: AI agents fail when requirements are insufficient
- Solution: Multi-phase requirements engineering pipeline:
  - Intake → Intent Inference → Clarification Generation → Research Phase → Requirements Formalization → Adversarial Review → Stakeholder Validation Gate
- Format: BDD/Gherkin for unambiguous acceptance criteria
- Research Basis: Spec-driven development research shows under-investing in specs is the #1 failure mode

**Hierarchical Task Decomposition (R-002)**
- Following the Planning Pattern: Goal Analysis → Phase Decomposition → Task Decomposition → Dependency Mapping → Context Scoping → Task Specification
- Each atomic task receives its own concrete requirement document
- MINIMUM context principle to reduce token usage and hallucination risk

**Multi-Model Consensus Verification (R-003)**
- Primary model (Kimi K2.5) → Secondary verification (Sonnet 4.6) → Tertiary arbitration (GPT-5.3)
- Consensus scoring algorithm based on ICE and MUSE research
- Behavioral testing + adversarial challenge approach

**GitHub-Native Task Tracking Architecture**
- GitHub becomes single source of truth for all project state
- Framework Concept → GitHub Object mapping:
  - SDLC Project → GitHub Milestone
  - SDLC Phase → GitHub Label (phase:requirements, phase:design, etc.)
  - Atomic Task → GitHub Issue
  - Task Implementation → GitHub Branch + PR
  - Verification Results → PR Comment
  - Quality Gate Decision → GitHub Label (gate:pass, gate:fail)

### 1.2 Tool Capabilities Matrix

Research across 8 specified tools:

| Capability | Kilo Code | Roo Code | ZenFlow | GitHub Copilot | Claude Code | Codex | Continue | Cline |
|------------|-----------|----------|---------|----------------|-------------|-------|----------|-------|
| Custom modes/roles | YAML modes | Orchestrator + custom | Custom workflows | Custom agents | CLAUDE.md + skills | Skills system | ❌ | Custom modes |
| Multi-agent orchestration | Orchestrator mode | Cloud agents + orchestrator | Parallel agents | Coding agent + agents panel | Agent Teams (3-5) | Multi-threaded | ❌ | ❌ |
| Spec-driven development | Via custom workflows | Via modes | Core feature (SDD) | Via custom instructions | Via CLAUDE.md | Via skills | ❌ | Via rules |
| Multi-model verification | Manual mode switching | Provider-per-mode | Committee approach | ❌ | Team model selection | ❌ | ❌ | Model switching |
| Sandboxed execution | ❌ Local only | Cloud sandboxes | Isolated environments | GitHub Actions sandbox | Local execution | Native sandboxing | N/A | ❌ Local only |
| MCP support | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ Limited | ❌ | ✅ |

**Key Finding:** ZenFlow is the only tool with native spec-driven development and multi-agent verification ("committee approach") as core features.

### 1.3 Workflow Engine Evaluation

**Contenders Analyzed:**

| Framework | Core Paradigm | Primary Strength | Maturity |
|-----------|---------------|------------------|----------|
| LangGraph | Graph-based stateful workflows | Explicit DAG control, branching, debugging | Most mature (106k ★) |
| CrewAI | Role-based team coordination | YAML-driven, intuitive setup | Mid-maturity (30k+ ★) |
| AutoGen | Conversational multi-agent | Dialogue-driven, flexible topologies | Research-oriented (43.1k+ ★) |
| OpenAI Agents SDK | Lightweight primitives | Minimal abstractions, fast deployment | Newest |

**Head-to-Head Comparison (Key Criteria):**

| Criterion | LangGraph | CrewAI | AutoGen | OpenAI Agents SDK |
|-----------|-----------|--------|---------|-------------------|
| Workflow complexity | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| State management | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Parallelization | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Observability | ⭐⭐⭐⭐⭐ (LangSmith/Langfuse) | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Error handling | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Token efficiency | ⭐⭐⭐⭐⭐ (lowest latency) | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| Production readiness | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

**Recommendation:** LangGraph is superior for SDLC framework due to:
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability with state transition logs and visual graph traces
- Lowest latency and token usage in benchmarks
- Native parallel execution for independent subtasks
- Conditional edges for gating decisions and retry mechanisms

---

## 2. MCP Servers Research

### 2.1 Protocol Understanding

**MCP (Model Context Protocol)** by Anthropic:
- Standard for giving agents access to external tools, data sources, and APIs
- Official repository: `modelcontextprotocol/servers`
- Hundreds of community servers for GitHub, Git, Slack, databases, browsers

**A2A (Agent2Agent) Protocol** by Google (Linux Foundation):
- Enables agents built on different frameworks to discover each other
- Uses JSON-RPC 2.0 over HTTPS
- Complementary to MCP: A2A handles agent-to-agent, MCP handles agent-to-tool

### 2.2 GitHub MCP Server Integration

**Key Tools Available:**
- `create_issue` / `update_issue` — Task creation and status updates
- `create_pull_request` / `merge_pull_request` — Implementation tracking
- `create_branch` — Isolation for atomic tasks
- `add_issue_comment` — Posting verification results, cost data, adversarial findings
- `add_labels` — Phase tracking, gate status, priority
- `assign_copilot_to_issue` — Delegate additional work to Copilot agent
- `search_issues` / `list_pull_requests` — Orchestrator reads project state

### 2.3 Event-Driven Pipeline Architecture

```
Event Flow:
1. LangGraph orchestrator decomposes task → creates GitHub Issue
2. GitHub Issue creation triggers Kilo webhook
3. Kilo Cloud Agent clones repo, creates branch, implements task
4. Kilo Cloud Agent auto-commits and pushes → creates PR
5. PR creation triggers GitHub Agentic Workflow
6. Agentic Workflow runs verification (Code Reviews, tests)
7. Verification results posted as PR comments
8. LangGraph orchestrator reads PR state via GitHub MCP → decides gate
```

---

## 3. Agent Orchestration Research

### 3.1 Inter-Agent Communication Patterns

**Patterns Evaluated:**

| Pattern | How It Works | Best For | Limitations |
|---------|--------------|----------|-------------|
| Subagents | Parent spawns child, receives only results | Simple delegation | No ongoing collaboration |
| Skills | Reusable capabilities agents can invoke | Standardized tasks | Limited context sharing |
| Handoffs | Agent A passes control to Agent B | Sequential workflows | No parallel collaboration |
| Claude Code Agent Teams | Shared task lists, direct messaging, self-coordination | Complex collaboration | Requires Claude Code |
| Roo Code Orchestrator | Hierarchical meta-prompts, context-passing protocols | Structured workflows | Learning curve |

**Key Finding:** Claude Code Agent Teams represent the most advanced inter-agent communication model with shared task lists, direct messaging, and self-coordination capabilities.

### 3.2 Agent Skills Collections

**Top Repositories:**

| Repository | Stars | What It Does |
|------------|-------|--------------|
| anthropic/skills | 61k ★ | Official skills — document creation, design, MCP builder, webapp testing |
| VoltAgent/awesome-agent-skills | 4.7k ★ | Most comprehensive curated list — 200+ skills from major publishers |
| skillcreatorai/Ai-Agent-Skills | — | "Homebrew for AI Agent Skills" — universal installer |

**Standout Skill Categories:**
- **Context Engineering** (by muratcankoylan): context compression, degradation detection, multi-agent patterns, memory systems
- **Security** (by Trail of Bits): 20+ skills including audit context building, static analysis, property-based testing
- **Development** (by obra): subagent-driven development, systematic debugging, root-cause tracing

### 3.3 Multi-Agent Workflow Frameworks

| Framework | Stars | Best For | Approach |
|-----------|-------|----------|----------|
| LangGraph | 106k ★ | Complex workflows with branching logic | Graph-based DAG, explicit state management |
| CrewAI | 30k+ ★ | Fastest time-to-production | Role-based agents with task delegation |
| AutoGen | 43.1k+ ★ | Conversational multi-agent, human-in-loop | Agents chat and iterate naturally |
| Agno | 29k+ ★ | Full-stack multi-agent | Supports all major LLM providers |
| Letta | 15.9k+ ★ | Stateful long-running agents | Memory persistence across sessions |

**Token Efficiency Note:** LangGraph uses ~2,000 tokens per task vs. CrewAI's ~3,500 and AutoGen's ~8,000.

---

## 4. Context Management Research

### 4.1 Context Transfer Protocol

**Spec Artifact Chain Approach:**
- Each SDLC phase produces a spec artifact
- Artifacts are passed along the chain: Requirements Spec → Design Spec → Implementation Spec → Test Spec
- Each artifact includes: context scope, acceptance criteria, constraints, token budget

### 4.2 Context Scoping Principles

**For each atomic task, determine MINIMUM context required:**
- Files needed
- Specs relevant
- Constraints to enforce
- Token budget allocation

### 4.3 Token Optimization Strategies

- Task-specific context reduces bloat
- Avoid conversation history growth
- Use structured JSON output for machine-readable documentation
- Implement context compression for long-running sessions

---

## 5. Testing Frameworks Research

### 5.1 Smoke Testing Framework Architecture

**Core Capabilities (Target State):**

| Capability | Description |
|------------|-------------|
| Universal web interaction engine | Playwright-based, handles all element types, dynamic content, complex forms |
| Dynamic multi-stack orchestration | 3+ containerized test environments (aio, int, prod) with auto port allocation (9330-9399) |
| Intelligent resilience system | Auto retry, element detection strategies, timeout handling, latency tolerance |
| Parallel test execution | Across multiple sites and within same site simultaneously |
| Complete observability stack | WebSocket updates, Prometheus metrics, structured JSON logging, artifact management |
| Database state management | Bidirectional reset supporting PostgreSQL and Oracle |
| Configuration-driven architecture | YAML test definitions |
| Multiple execution interfaces | UI dashboard (Flask), REST API (Express), CLI, programmatic |
| Self-healing capabilities | Element locator fallbacks, intelligent wait strategies, adaptive selectors |

### 5.2 Deviation Detection System

**Deviation Types to Track:**
- Selector Deviations (configured vs. actual selector used)
- Timing Deviations (configured timeout vs. actual wait time)
- Validation Deviations (expected vs. actual error messages)
- Workflow Deviations (configured steps vs. actual execution)
- Data Deviations (expected vs. actual dropdown options)

**Deviation Dashboard Features:**
- Summary View: Total deviations by type, severity, status
- List View: Paginated table with test name, deviation type, timestamp, environment
- Detail View: Side-by-side comparison, visual diff, timeline, frequency chart
- Trend Analysis: Charts showing deviations over time, by module, most common types
- Review Workflow: Assign, comment, batch operations, export reports

### 5.3 Test-Driven Development of UI

**TDD Workflow for Dashboard:**
1. Write tests for desired UI features before implementation
2. Implement UI features to pass tests
3. Validate all UI components work correctly
4. Ensure accessibility compliance
5. Verify responsive design across viewports

---

## 6. CI/CD Patterns Research

### 6.1 GitHub-Native CI/CD Integration

**GitHub Agentic Workflows** (Technical Preview):
- Markdown-defined automations that run coding agents inside GitHub Actions
- Combined with Kilo Code's webhook triggers for event-driven pipeline

### 6.2 Jenkins Integration

**Smoke Test Pipeline:**
- Jenkins triggers deployment → Smoke tests start
- KEDA scales AI analyzer from 0 → 1 pod (5-10 seconds)
- 8 Playwright pods run parallel tests → Call AI service when selectors fail
- AI analyzer handles 20-30 requests/minute
- Tests complete → AI pod scales to 0 after cooldown

### 6.3 Kubernetes Deployment Strategy

**Shared AI Service Pattern (Recommended):**
```
┌─────────────────────────────────────────┐
│  8-Node Kubernetes Cluster              │
├─────────────────────────────────────────┤
│  Smoke Test Pods (6-8 parallel)         │
│  ├─ Playwright container (2GB RAM)      │
│  └─ Calls AI service via HTTP           │
├─────────────────────────────────────────┤
│  AI Analyzer Pod (1-2 replicas)         │
│  ├─ Qwen3-0.6B model (2-3GB RAM)       │
│  └─ Serves all smoke test pods          │
└─────────────────────────────────────────┘
```

**Resource Distribution (8 Nodes @ 4-8 cores, 16-32GB RAM each):**
- Total capacity: 64 CPU cores, 256GB RAM
- Smoke test allocation: 16GB RAM (Playwright) + 3-6GB RAM (AI) = ~20-25GB
- Total consumption: <10% of cluster resources

---

## 7. Tiny AI Models for Testing Research

### 7.1 Model Comparison

| Model | Parameters | Docker Size | Inference Speed | Best For |
|-------|------------|-------------|-----------------|----------|
| SmolLM2-360M | 360M | ~400MB | <100ms | Quick pattern matching, selector analysis |
| Qwen2-0.5B | 500M | ~500MB | ~150ms | Reasoning about failures, context understanding |
| Qwen3-0.6B | 600M | ~600MB | ~5ms/token | Complex decision-making, code understanding |
| Phi-3-mini | 3.8B | ~2.5GB | ~300ms | Complex decision-making, code understanding |

### 7.2 Qwen3-0.6B Deep Dive

**Key Advantages:**
- Released April 2025, trained on 36 trillion tokens across 119 languages
- 32K context window (can analyze entire test suites, DOM snapshots, git diffs)
- Benchmarks: 73% on MATH500, 79.2% on GSM8K, 30.5% on HumanEval
- Built-in agent capabilities for automation and workflow orchestration
- Dual reasoning modes: "thinking" and "non-thinking"

**Resource Requirements:**
- RAM: 8GB total system, ~3GB during inference
- Storage: 3GB for quantized model files
- CPU: 4-8 cores recommended, 2 cores minimum
- Inference speed: 10-30 tokens/second on CPU-only

**Kubernetes Configuration:**
```yaml
resources:
  requests:
    memory: "2Gi"
    cpu: "1000m"
  limits:
    memory: "3Gi"
    cpu: "2000m"
```

### 7.3 Selector Intelligence Layer

**Implementation Approach:**
1. Analyze selector failures and compare current vs. expected DOM structures
2. Evaluate error patterns against historical test data
3. Determine retry worthiness using context (commit messages, recent code changes, error frequency)
4. Provide confidence scores for "legitimate failure" vs. "trivial UI change"

**Decision Framework:**
- Legitimate test failure → FAIL
- Cosmetic change → RETRY
- Timing issue → RETRY
- Environmental → RETRY

---

## 8. ZenFlow Integration Research

### 8.1 ZenFlow Core Concepts

**Four Pillars:**
1. Structured Workflows
2. SDD (Spec-Driven Development)
3. Multi-Agent Verification
4. Parallel Execution

### 8.2 24-Step Custom Workflow

**Phases:**
1. Planning
2. Design
3. Architecture
4. Implementation
5. Review
6. Testing
7. Validation
8. Optimization
9. Refactoring
10. Performance Optimization
11. Production Polish

### 8.3 Evidence-Driven Development

**Zen Rules:**
- All decisions must be based on empirical evidence
- No assumptions without verification
- Continuous validation at each phase
- Automated verification gates

---

## 9. Frontend Analysis Methodology Research

### 9.1 Code Relationship Database Approach

**Core Problem Addressed:**
"I do not know what connects to what, code paths are uncertain, and I need a method to ensure everything is mapped, tested, and maintainable."

**Solution:** Graph database approach treating code as queryable graph structure
- Nodes = files, functions, components
- Edges = imports, calls, relationships
- Enables powerful queries about codebase

### 9.2 Deliverables Created

| Deliverable | Lines | Purpose |
|-------------|-------|---------|
| IMPLEMENTATION_SUMMARY.md | 600 | Complete system overview |
| frontend_analysis_plan.md | 929 | 22-day roadmap, 8 phases |
| quick_start_guide.md | 311 | 30-minute insights |
| tools/dependency_mapper.py | 341 | Automated codebase analysis |
| tools/generate_graph_visualization.html | 536 | Interactive dependency graph |
| VISUAL_ROADMAP.md | 738 | Flowcharts and diagrams |

### 9.3 Key Innovations

- **Graph Database Approach:** Queryable code relationships
- **AI Agent Compatibility:** Structured JSON output, machine-readable documentation
- **Evidence-Based Methods:** Tools from 2026 research (FalkorDB, GitKraken Codemaps, Vitest, Playwright)

---

## 10. Sources Discovered in Space

### 10.1 Official Documentation
- LangGraph Documentation (langchain-ai.github.io)
- Langfuse Documentation (langfuse.com)
- ZenFlow Documentation (zenflow.ai)
- Claude Code Documentation (code.claude.ai)
- GitHub Copilot Documentation (github.com)
- OpenAI Codex Documentation (openai.com)

### 10.2 Research Papers
- FastFlowLM: Efficient LLM Inference (github.com)
- Speculative Decoding Research (AMD dev reports)
- AI-SDLC Maturity Model (eleks.com)

### 10.3 GitHub Repositories
- modelcontextprotocol/servers (MCP servers)
- anthropic/skills (61k ★)
- VoltAgent/awesome-agent-skills (4.7k ★)
- langchain-ai/langgraph (106k ★)
- crewAIInc/crewAI (30k+ ★)
- microsoft/autogen (43.1k+ ★)

### 10.4 Industry Sources
- prnewswire.com (Claude Code Agent Teams)
- xebia.com (Kilo Code/Roo Code analysis)
- intuitionlabs.ai (OpenAI Codex automation)
- linkedin.com (BDD/Gherkin acceptance criteria)
- thoughtworks.com (shift-left involvement)

---

## 11. Research Gaps Identified

### 11.1 Remaining Gaps After Prior Work Integration

1. **MCP Server Ecosystem Deep Dive**
   - Prior work identified MCP protocol but didn't exhaustively catalog all available servers
   - Gap: Complete inventory of production-ready MCP servers by category

2. **A2A Protocol Implementation Details**
   - Prior work mentioned A2A but didn't explore implementation patterns
   - Gap: Concrete A2A integration examples for agent-to-agent communication

3. **Local LLM Deployment Patterns**
   - Prior work mentioned local models but focused on cloud
   - Gap: Comprehensive local LLM deployment architecture for air-gapped environments

4. **Cross-Framework Agent Interoperability**
   - Prior work compared frameworks but didn't address interoperability
   - Gap: Patterns for agents from different frameworks to collaborate

5. **Production Hardening Patterns**
   - Prior work focused on architecture design
   - Gap: Operational runbooks, monitoring, alerting for production agent systems

6. **Security & Compliance for Agent Systems**
   - Prior work mentioned security briefly
   - Gap: Comprehensive security framework for autonomous agent systems

7. **Cost Optimization at Scale**
   - Prior work mentioned cost tracking
   - Gap: Advanced cost optimization strategies for enterprise-scale deployments

### 11.2 Cross-References to Research Taxonomy

| Taxonomy Category | Prior Work Coverage | Gap Status |
|-------------------|---------------------|------------|
| Agentic SDLC Patterns | Comprehensive (v1-v3) | Minor gaps in implementation details |
| MCP Servers | Protocol identified | Needs server catalog |
| Agent Orchestration | LangGraph recommended | Needs A2A implementation |
| Context Management | Spec artifact chain defined | Needs compression strategies |
| Testing Frameworks | Smoke testing architecture | Needs production hardening |
| CI/CD Patterns | GitHub-native approach | Needs operational runbooks |

---

## 12. Key Decisions & Conclusions from Prior Work

### 12.1 Workflow Engine Decision
**Decision:** Use LangGraph  
**Rationale:** 
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability
- Lowest latency and token usage
- Native parallel execution

### 12.2 Model Selection Decision
**Decision:** Kimi K2.5 as primary, Sonnet 4.6, GPT-5.3, Gemini 3 Pro/Flash  
**Rationale:**
- Cost optimization (Kimi is cheapest)
- Escalation path for complex tasks
- Multi-model consensus verification

### 12.3 Task Tracking Decision
**Decision:** GitHub-native (Issues, PRs, branches)  
**Rationale:**
- Permanent, auditable record
- Human-readable project state
- Native CI/CD integration
- Built-in collaboration

### 12.4 Testing Approach Decision
**Decision:** Behavioral testing + consensus-based evaluation + adversarial challenge  
**Rationale:**
- Empirical verification
- Reduces false positives
- Catches edge cases

### 12.5 Local vs Cloud Decision
**Decision:** Hybrid approach  
**Rationale:**
- Local for planning/design (cost, privacy)
- Cloud for implementation (speed)
- Local for final validation (accuracy)

---

## 13. Integration Recommendations

### 13.1 For New Research

1. **Build on LangGraph Foundation**
   - Prior work already selected LangGraph; new research should assume this baseline
   - Focus on graph node/edge design patterns

2. **Extend GitHub-Native Approach**
   - Use GitHub as single source of truth
   - Leverage GitHub MCP server for automation

3. **Incorporate ZenFlow Patterns**
   - Use 24-step workflow as reference
   - Apply evidence-driven development principles

4. **Leverage Tiny AI Models**
   - Qwen3-0.6B for selector intelligence
   - Deploy as shared service in K8s

### 13.2 For Implementation

1. **Start with Smoke Testing Framework**
   - Prior work includes comprehensive architecture
   - Use as proving ground for agentic patterns

2. **Implement Deviation Detection Early**
   - Critical for self-healing capabilities
   - Enables continuous improvement

3. **Use Kilo Code Cloud Agents**
   - For PR reviews and webhook automation
   - Integrates with GitHub-native workflow

---

## 14. Summary Statistics

| Metric | Value |
|--------|-------|
| Research Threads Analyzed | 8+ |
| Sources Cited | 160+ |
| Requirements Versions | 3 (v1 → v2 → v3) |
| Tools Evaluated | 8 |
| Workflow Frameworks Compared | 4 |
| AI Models Analyzed | 4+ |
| SDLC Phases Defined | 7 |
| GitHub Repositories Referenced | 15+ |

---

## 15. Document Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025 | Initial extraction and synthesis from Perplexity Space |

---

*This document represents a comprehensive integration of all substantive research found in the "Smoke Test Framework" Perplexity Space. It should be treated as a living document and updated as new research emerges.*

# Perplexity Space Research Integration: Smoke Test Framework

**Source:** https://www.perplexity.ai/spaces/smoke-test-framework-_L0_2o2dRyaDjDbhcmyOfw  
**Extraction Date:** 2025  
**Research Threads Analyzed:** 8+ substantive threads

---

## Executive Summary

This document synthesizes all substantive research from the "Smoke Test Framework" Perplexity Space, which contains extensive prior work on AI agentic SDLC frameworks, testing infrastructure, MCP servers, agent orchestration, and autonomous development workflows. The space represents 160+ research sources and multiple iterative refinement cycles on designing production-grade autonomous AI coding systems.

### Key Prior Work Identified:
1. **AI Agentic Autonomous SDLC Framework** - Comprehensive requirements across 3 major versions
2. **Smoke Testing Framework Architecture** - Playwright-based enterprise testing platform design
3. **Agent Skills & Workflows Research** - 200+ curated skills from major AI coding tools
4. **Tiny AI Models for Testing** - Docker-optimized models for selector adaptation
5. **ZenFlow Integration** - 24-step autonomous workflow for evidence-driven development
6. **Frontend Analysis Methodology** - Code relationship database approach

---

## 1. Agentic SDLC Patterns Research

### 1.1 Core Architecture Requirements (R-001 to R-014)

**Source Thread:** AI Agentic Autonomous SDLC Framework (Requirements v1-v3)

#### Key Findings:

**Autonomous Requirements Engineering (R-001)**
- Problem: AI agents fail when requirements are insufficient
- Solution: Multi-phase requirements engineering pipeline:
  - Intake → Intent Inference → Clarification Generation → Research Phase → Requirements Formalization → Adversarial Review → Stakeholder Validation Gate
- Format: BDD/Gherkin for unambiguous acceptance criteria
- Research Basis: Spec-driven development research shows under-investing in specs is the #1 failure mode

**Hierarchical Task Decomposition (R-002)**
- Following the Planning Pattern: Goal Analysis → Phase Decomposition → Task Decomposition → Dependency Mapping → Context Scoping → Task Specification
- Each atomic task receives its own concrete requirement document
- MINIMUM context principle to reduce token usage and hallucination risk

**Multi-Model Consensus Verification (R-003)**
- Primary model (Kimi K2.5) → Secondary verification (Sonnet 4.6) → Tertiary arbitration (GPT-5.3)
- Consensus scoring algorithm based on ICE and MUSE research
- Behavioral testing + adversarial challenge approach

**GitHub-Native Task Tracking Architecture**
- GitHub becomes single source of truth for all project state
- Framework Concept → GitHub Object mapping:
  - SDLC Project → GitHub Milestone
  - SDLC Phase → GitHub Label (phase:requirements, phase:design, etc.)
  - Atomic Task → GitHub Issue
  - Task Implementation → GitHub Branch + PR
  - Verification Results → PR Comment
  - Quality Gate Decision → GitHub Label (gate:pass, gate:fail)

### 1.2 Tool Capabilities Matrix

Research across 8 specified tools:

| Capability | Kilo Code | Roo Code | ZenFlow | GitHub Copilot | Claude Code | Codex | Continue | Cline |
|------------|-----------|----------|---------|----------------|-------------|-------|----------|-------|
| Custom modes/roles | YAML modes | Orchestrator + custom | Custom workflows | Custom agents | CLAUDE.md + skills | Skills system | ❌ | Custom modes |
| Multi-agent orchestration | Orchestrator mode | Cloud agents + orchestrator | Parallel agents | Coding agent + agents panel | Agent Teams (3-5) | Multi-threaded | ❌ | ❌ |
| Spec-driven development | Via custom workflows | Via modes | Core feature (SDD) | Via custom instructions | Via CLAUDE.md | Via skills | ❌ | Via rules |
| Multi-model verification | Manual mode switching | Provider-per-mode | Committee approach | ❌ | Team model selection | ❌ | ❌ | Model switching |
| Sandboxed execution | ❌ Local only | Cloud sandboxes | Isolated environments | GitHub Actions sandbox | Local execution | Native sandboxing | N/A | ❌ Local only |
| MCP support | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ Limited | ❌ | ✅ |

**Key Finding:** ZenFlow is the only tool with native spec-driven development and multi-agent verification ("committee approach") as core features.

### 1.3 Workflow Engine Evaluation

**Contenders Analyzed:**

| Framework | Core Paradigm | Primary Strength | Maturity |
|-----------|---------------|------------------|----------|
| LangGraph | Graph-based stateful workflows | Explicit DAG control, branching, debugging | Most mature (106k ★) |
| CrewAI | Role-based team coordination | YAML-driven, intuitive setup | Mid-maturity (30k+ ★) |
| AutoGen | Conversational multi-agent | Dialogue-driven, flexible topologies | Research-oriented (43.1k+ ★) |
| OpenAI Agents SDK | Lightweight primitives | Minimal abstractions, fast deployment | Newest |

**Head-to-Head Comparison (Key Criteria):**

| Criterion | LangGraph | CrewAI | AutoGen | OpenAI Agents SDK |
|-----------|-----------|--------|---------|-------------------|
| Workflow complexity | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| State management | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Parallelization | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Observability | ⭐⭐⭐⭐⭐ (LangSmith/Langfuse) | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Error handling | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Token efficiency | ⭐⭐⭐⭐⭐ (lowest latency) | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| Production readiness | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

**Recommendation:** LangGraph is superior for SDLC framework due to:
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability with state transition logs and visual graph traces
- Lowest latency and token usage in benchmarks
- Native parallel execution for independent subtasks
- Conditional edges for gating decisions and retry mechanisms

---

## 2. MCP Servers Research

### 2.1 Protocol Understanding

**MCP (Model Context Protocol)** by Anthropic:
- Standard for giving agents access to external tools, data sources, and APIs
- Official repository: `modelcontextprotocol/servers`
- Hundreds of community servers for GitHub, Git, Slack, databases, browsers

**A2A (Agent2Agent) Protocol** by Google (Linux Foundation):
- Enables agents built on different frameworks to discover each other
- Uses JSON-RPC 2.0 over HTTPS
- Complementary to MCP: A2A handles agent-to-agent, MCP handles agent-to-tool

### 2.2 GitHub MCP Server Integration

**Key Tools Available:**
- `create_issue` / `update_issue` — Task creation and status updates
- `create_pull_request` / `merge_pull_request` — Implementation tracking
- `create_branch` — Isolation for atomic tasks
- `add_issue_comment` — Posting verification results, cost data, adversarial findings
- `add_labels` — Phase tracking, gate status, priority
- `assign_copilot_to_issue` — Delegate additional work to Copilot agent
- `search_issues` / `list_pull_requests` — Orchestrator reads project state

### 2.3 Event-Driven Pipeline Architecture

```
Event Flow:
1. LangGraph orchestrator decomposes task → creates GitHub Issue
2. GitHub Issue creation triggers Kilo webhook
3. Kilo Cloud Agent clones repo, creates branch, implements task
4. Kilo Cloud Agent auto-commits and pushes → creates PR
5. PR creation triggers GitHub Agentic Workflow
6. Agentic Workflow runs verification (Code Reviews, tests)
7. Verification results posted as PR comments
8. LangGraph orchestrator reads PR state via GitHub MCP → decides gate
```

---

## 3. Agent Orchestration Research

### 3.1 Inter-Agent Communication Patterns

**Patterns Evaluated:**

| Pattern | How It Works | Best For | Limitations |
|---------|--------------|----------|-------------|
| Subagents | Parent spawns child, receives only results | Simple delegation | No ongoing collaboration |
| Skills | Reusable capabilities agents can invoke | Standardized tasks | Limited context sharing |
| Handoffs | Agent A passes control to Agent B | Sequential workflows | No parallel collaboration |
| Claude Code Agent Teams | Shared task lists, direct messaging, self-coordination | Complex collaboration | Requires Claude Code |
| Roo Code Orchestrator | Hierarchical meta-prompts, context-passing protocols | Structured workflows | Learning curve |

**Key Finding:** Claude Code Agent Teams represent the most advanced inter-agent communication model with shared task lists, direct messaging, and self-coordination capabilities.

### 3.2 Agent Skills Collections

**Top Repositories:**

| Repository | Stars | What It Does |
|------------|-------|--------------|
| anthropic/skills | 61k ★ | Official skills — document creation, design, MCP builder, webapp testing |
| VoltAgent/awesome-agent-skills | 4.7k ★ | Most comprehensive curated list — 200+ skills from major publishers |
| skillcreatorai/Ai-Agent-Skills | — | "Homebrew for AI Agent Skills" — universal installer |

**Standout Skill Categories:**
- **Context Engineering** (by muratcankoylan): context compression, degradation detection, multi-agent patterns, memory systems
- **Security** (by Trail of Bits): 20+ skills including audit context building, static analysis, property-based testing
- **Development** (by obra): subagent-driven development, systematic debugging, root-cause tracing

### 3.3 Multi-Agent Workflow Frameworks

| Framework | Stars | Best For | Approach |
|-----------|-------|----------|----------|
| LangGraph | 106k ★ | Complex workflows with branching logic | Graph-based DAG, explicit state management |
| CrewAI | 30k+ ★ | Fastest time-to-production | Role-based agents with task delegation |
| AutoGen | 43.1k+ ★ | Conversational multi-agent, human-in-loop | Agents chat and iterate naturally |
| Agno | 29k+ ★ | Full-stack multi-agent | Supports all major LLM providers |
| Letta | 15.9k+ ★ | Stateful long-running agents | Memory persistence across sessions |

**Token Efficiency Note:** LangGraph uses ~2,000 tokens per task vs. CrewAI's ~3,500 and AutoGen's ~8,000.

---

## 4. Context Management Research

### 4.1 Context Transfer Protocol

**Spec Artifact Chain Approach:**
- Each SDLC phase produces a spec artifact
- Artifacts are passed along the chain: Requirements Spec → Design Spec → Implementation Spec → Test Spec
- Each artifact includes: context scope, acceptance criteria, constraints, token budget

### 4.2 Context Scoping Principles

**For each atomic task, determine MINIMUM context required:**
- Files needed
- Specs relevant
- Constraints to enforce
- Token budget allocation

### 4.3 Token Optimization Strategies

- Task-specific context reduces bloat
- Avoid conversation history growth
- Use structured JSON output for machine-readable documentation
- Implement context compression for long-running sessions

---

## 5. Testing Frameworks Research

### 5.1 Smoke Testing Framework Architecture

**Core Capabilities (Target State):**

| Capability | Description |
|------------|-------------|
| Universal web interaction engine | Playwright-based, handles all element types, dynamic content, complex forms |
| Dynamic multi-stack orchestration | 3+ containerized test environments (aio, int, prod) with auto port allocation (9330-9399) |
| Intelligent resilience system | Auto retry, element detection strategies, timeout handling, latency tolerance |
| Parallel test execution | Across multiple sites and within same site simultaneously |
| Complete observability stack | WebSocket updates, Prometheus metrics, structured JSON logging, artifact management |
| Database state management | Bidirectional reset supporting PostgreSQL and Oracle |
| Configuration-driven architecture | YAML test definitions |
| Multiple execution interfaces | UI dashboard (Flask), REST API (Express), CLI, programmatic |
| Self-healing capabilities | Element locator fallbacks, intelligent wait strategies, adaptive selectors |

### 5.2 Deviation Detection System

**Deviation Types to Track:**
- Selector Deviations (configured vs. actual selector used)
- Timing Deviations (configured timeout vs. actual wait time)
- Validation Deviations (expected vs. actual error messages)
- Workflow Deviations (configured steps vs. actual execution)
- Data Deviations (expected vs. actual dropdown options)

**Deviation Dashboard Features:**
- Summary View: Total deviations by type, severity, status
- List View: Paginated table with test name, deviation type, timestamp, environment
- Detail View: Side-by-side comparison, visual diff, timeline, frequency chart
- Trend Analysis: Charts showing deviations over time, by module, most common types
- Review Workflow: Assign, comment, batch operations, export reports

### 5.3 Test-Driven Development of UI

**TDD Workflow for Dashboard:**
1. Write tests for desired UI features before implementation
2. Implement UI features to pass tests
3. Validate all UI components work correctly
4. Ensure accessibility compliance
5. Verify responsive design across viewports

---

## 6. CI/CD Patterns Research

### 6.1 GitHub-Native CI/CD Integration

**GitHub Agentic Workflows** (Technical Preview):
- Markdown-defined automations that run coding agents inside GitHub Actions
- Combined with Kilo Code's webhook triggers for event-driven pipeline

### 6.2 Jenkins Integration

**Smoke Test Pipeline:**
- Jenkins triggers deployment → Smoke tests start
- KEDA scales AI analyzer from 0 → 1 pod (5-10 seconds)
- 8 Playwright pods run parallel tests → Call AI service when selectors fail
- AI analyzer handles 20-30 requests/minute
- Tests complete → AI pod scales to 0 after cooldown

### 6.3 Kubernetes Deployment Strategy

**Shared AI Service Pattern (Recommended):**
```
┌─────────────────────────────────────────┐
│  8-Node Kubernetes Cluster              │
├─────────────────────────────────────────┤
│  Smoke Test Pods (6-8 parallel)         │
│  ├─ Playwright container (2GB RAM)      │
│  └─ Calls AI service via HTTP           │
├─────────────────────────────────────────┤
│  AI Analyzer Pod (1-2 replicas)         │
│  ├─ Qwen3-0.6B model (2-3GB RAM)       │
│  └─ Serves all smoke test pods          │
└─────────────────────────────────────────┘
```

**Resource Distribution (8 Nodes @ 4-8 cores, 16-32GB RAM each):**
- Total capacity: 64 CPU cores, 256GB RAM
- Smoke test allocation: 16GB RAM (Playwright) + 3-6GB RAM (AI) = ~20-25GB
- Total consumption: <10% of cluster resources

---

## 7. Tiny AI Models for Testing Research

### 7.1 Model Comparison

| Model | Parameters | Docker Size | Inference Speed | Best For |
|-------|------------|-------------|-----------------|----------|
| SmolLM2-360M | 360M | ~400MB | <100ms | Quick pattern matching, selector analysis |
| Qwen2-0.5B | 500M | ~500MB | ~150ms | Reasoning about failures, context understanding |
| Qwen3-0.6B | 600M | ~600MB | ~5ms/token | Complex decision-making, code understanding |
| Phi-3-mini | 3.8B | ~2.5GB | ~300ms | Complex decision-making, code understanding |

### 7.2 Qwen3-0.6B Deep Dive

**Key Advantages:**
- Released April 2025, trained on 36 trillion tokens across 119 languages
- 32K context window (can analyze entire test suites, DOM snapshots, git diffs)
- Benchmarks: 73% on MATH500, 79.2% on GSM8K, 30.5% on HumanEval
- Built-in agent capabilities for automation and workflow orchestration
- Dual reasoning modes: "thinking" and "non-thinking"

**Resource Requirements:**
- RAM: 8GB total system, ~3GB during inference
- Storage: 3GB for quantized model files
- CPU: 4-8 cores recommended, 2 cores minimum
- Inference speed: 10-30 tokens/second on CPU-only

**Kubernetes Configuration:**
```yaml
resources:
  requests:
    memory: "2Gi"
    cpu: "1000m"
  limits:
    memory: "3Gi"
    cpu: "2000m"
```

### 7.3 Selector Intelligence Layer

**Implementation Approach:**
1. Analyze selector failures and compare current vs. expected DOM structures
2. Evaluate error patterns against historical test data
3. Determine retry worthiness using context (commit messages, recent code changes, error frequency)
4. Provide confidence scores for "legitimate failure" vs. "trivial UI change"

**Decision Framework:**
- Legitimate test failure → FAIL
- Cosmetic change → RETRY
- Timing issue → RETRY
- Environmental → RETRY

---

## 8. ZenFlow Integration Research

### 8.1 ZenFlow Core Concepts

**Four Pillars:**
1. Structured Workflows
2. SDD (Spec-Driven Development)
3. Multi-Agent Verification
4. Parallel Execution

### 8.2 24-Step Custom Workflow

**Phases:**
1. Planning
2. Design
3. Architecture
4. Implementation
5. Review
6. Testing
7. Validation
8. Optimization
9. Refactoring
10. Performance Optimization
11. Production Polish

### 8.3 Evidence-Driven Development

**Zen Rules:**
- All decisions must be based on empirical evidence
- No assumptions without verification
- Continuous validation at each phase
- Automated verification gates

---

## 9. Frontend Analysis Methodology Research

### 9.1 Code Relationship Database Approach

**Core Problem Addressed:**
"I do not know what connects to what, code paths are uncertain, and I need a method to ensure everything is mapped, tested, and maintainable."

**Solution:** Graph database approach treating code as queryable graph structure
- Nodes = files, functions, components
- Edges = imports, calls, relationships
- Enables powerful queries about codebase

### 9.2 Deliverables Created

| Deliverable | Lines | Purpose |
|-------------|-------|---------|
| IMPLEMENTATION_SUMMARY.md | 600 | Complete system overview |
| frontend_analysis_plan.md | 929 | 22-day roadmap, 8 phases |
| quick_start_guide.md | 311 | 30-minute insights |
| tools/dependency_mapper.py | 341 | Automated codebase analysis |
| tools/generate_graph_visualization.html | 536 | Interactive dependency graph |
| VISUAL_ROADMAP.md | 738 | Flowcharts and diagrams |

### 9.3 Key Innovations

- **Graph Database Approach:** Queryable code relationships
- **AI Agent Compatibility:** Structured JSON output, machine-readable documentation
- **Evidence-Based Methods:** Tools from 2026 research (FalkorDB, GitKraken Codemaps, Vitest, Playwright)

---

## 10. Sources Discovered in Space

### 10.1 Official Documentation
- LangGraph Documentation (langchain-ai.github.io)
- Langfuse Documentation (langfuse.com)
- ZenFlow Documentation (zenflow.ai)
- Claude Code Documentation (code.claude.ai)
- GitHub Copilot Documentation (github.com)
- OpenAI Codex Documentation (openai.com)

### 10.2 Research Papers
- FastFlowLM: Efficient LLM Inference (github.com)
- Speculative Decoding Research (AMD dev reports)
- AI-SDLC Maturity Model (eleks.com)

### 10.3 GitHub Repositories
- modelcontextprotocol/servers (MCP servers)
- anthropic/skills (61k ★)
- VoltAgent/awesome-agent-skills (4.7k ★)
- langchain-ai/langgraph (106k ★)
- crewAIInc/crewAI (30k+ ★)
- microsoft/autogen (43.1k+ ★)

### 10.4 Industry Sources
- prnewswire.com (Claude Code Agent Teams)
- xebia.com (Kilo Code/Roo Code analysis)
- intuitionlabs.ai (OpenAI Codex automation)
- linkedin.com (BDD/Gherkin acceptance criteria)
- thoughtworks.com (shift-left involvement)

---

## 11. Research Gaps Identified

### 11.1 Remaining Gaps After Prior Work Integration

1. **MCP Server Ecosystem Deep Dive**
   - Prior work identified MCP protocol but didn't exhaustively catalog all available servers
   - Gap: Complete inventory of production-ready MCP servers by category

2. **A2A Protocol Implementation Details**
   - Prior work mentioned A2A but didn't explore implementation patterns
   - Gap: Concrete A2A integration examples for agent-to-agent communication

3. **Local LLM Deployment Patterns**
   - Prior work mentioned local models but focused on cloud
   - Gap: Comprehensive local LLM deployment architecture for air-gapped environments

4. **Cross-Framework Agent Interoperability**
   - Prior work compared frameworks but didn't address interoperability
   - Gap: Patterns for agents from different frameworks to collaborate

5. **Production Hardening Patterns**
   - Prior work focused on architecture design
   - Gap: Operational runbooks, monitoring, alerting for production agent systems

6. **Security & Compliance for Agent Systems**
   - Prior work mentioned security briefly
   - Gap: Comprehensive security framework for autonomous agent systems

7. **Cost Optimization at Scale**
   - Prior work mentioned cost tracking
   - Gap: Advanced cost optimization strategies for enterprise-scale deployments

### 11.2 Cross-References to Research Taxonomy

| Taxonomy Category | Prior Work Coverage | Gap Status |
|-------------------|---------------------|------------|
| Agentic SDLC Patterns | Comprehensive (v1-v3) | Minor gaps in implementation details |
| MCP Servers | Protocol identified | Needs server catalog |
| Agent Orchestration | LangGraph recommended | Needs A2A implementation |
| Context Management | Spec artifact chain defined | Needs compression strategies |
| Testing Frameworks | Smoke testing architecture | Needs production hardening |
| CI/CD Patterns | GitHub-native approach | Needs operational runbooks |

---

## 12. Key Decisions & Conclusions from Prior Work

### 12.1 Workflow Engine Decision
**Decision:** Use LangGraph  
**Rationale:** 
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability
- Lowest latency and token usage
- Native parallel execution

### 12.2 Model Selection Decision
**Decision:** Kimi K2.5 as primary, Sonnet 4.6, GPT-5.3, Gemini 3 Pro/Flash  
**Rationale:**
- Cost optimization (Kimi is cheapest)
- Escalation path for complex tasks
- Multi-model consensus verification

### 12.3 Task Tracking Decision
**Decision:** GitHub-native (Issues, PRs, branches)  
**Rationale:**
- Permanent, auditable record
- Human-readable project state
- Native CI/CD integration
- Built-in collaboration

### 12.4 Testing Approach Decision
**Decision:** Behavioral testing + consensus-based evaluation + adversarial challenge  
**Rationale:**
- Empirical verification
- Reduces false positives
- Catches edge cases

### 12.5 Local vs Cloud Decision
**Decision:** Hybrid approach  
**Rationale:**
- Local for planning/design (cost, privacy)
- Cloud for implementation (speed)
- Local for final validation (accuracy)

---

## 13. Integration Recommendations

### 13.1 For New Research

1. **Build on LangGraph Foundation**
   - Prior work already selected LangGraph; new research should assume this baseline
   - Focus on graph node/edge design patterns

2. **Extend GitHub-Native Approach**
   - Use GitHub as single source of truth
   - Leverage GitHub MCP server for automation

3. **Incorporate ZenFlow Patterns**
   - Use 24-step workflow as reference
   - Apply evidence-driven development principles

4. **Leverage Tiny AI Models**
   - Qwen3-0.6B for selector intelligence
   - Deploy as shared service in K8s

### 13.2 For Implementation

1. **Start with Smoke Testing Framework**
   - Prior work includes comprehensive architecture
   - Use as proving ground for agentic patterns

2. **Implement Deviation Detection Early**
   - Critical for self-healing capabilities
   - Enables continuous improvement

3. **Use Kilo Code Cloud Agents**
   - For PR reviews and webhook automation
   - Integrates with GitHub-native workflow

---

## 14. Summary Statistics

| Metric | Value |
|--------|-------|
| Research Threads Analyzed | 8+ |
| Sources Cited | 160+ |
| Requirements Versions | 3 (v1 → v2 → v3) |
| Tools Evaluated | 8 |
| Workflow Frameworks Compared | 4 |
| AI Models Analyzed | 4+ |
| SDLC Phases Defined | 7 |
| GitHub Repositories Referenced | 15+ |

---

## 15. Document Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025 | Initial extraction and synthesis from Perplexity Space |

---

*This document represents a comprehensive integration of all substantive research found in the "Smoke Test Framework" Perplexity Space. It should be treated as a living document and updated as new research emerges.*

# Perplexity Space Research Integration: Smoke Test Framework

**Source:** https://www.perplexity.ai/spaces/smoke-test-framework-_L0_2o2dRyaDjDbhcmyOfw  
**Extraction Date:** 2025  
**Research Threads Analyzed:** 8+ substantive threads

---

## Executive Summary

This document synthesizes all substantive research from the "Smoke Test Framework" Perplexity Space, which contains extensive prior work on AI agentic SDLC frameworks, testing infrastructure, MCP servers, agent orchestration, and autonomous development workflows. The space represents 160+ research sources and multiple iterative refinement cycles on designing production-grade autonomous AI coding systems.

### Key Prior Work Identified:
1. **AI Agentic Autonomous SDLC Framework** - Comprehensive requirements across 3 major versions
2. **Smoke Testing Framework Architecture** - Playwright-based enterprise testing platform design
3. **Agent Skills & Workflows Research** - 200+ curated skills from major AI coding tools
4. **Tiny AI Models for Testing** - Docker-optimized models for selector adaptation
5. **ZenFlow Integration** - 24-step autonomous workflow for evidence-driven development
6. **Frontend Analysis Methodology** - Code relationship database approach

---

## 1. Agentic SDLC Patterns Research

### 1.1 Core Architecture Requirements (R-001 to R-014)

**Source Thread:** AI Agentic Autonomous SDLC Framework (Requirements v1-v3)

#### Key Findings:

**Autonomous Requirements Engineering (R-001)**
- Problem: AI agents fail when requirements are insufficient
- Solution: Multi-phase requirements engineering pipeline:
  - Intake → Intent Inference → Clarification Generation → Research Phase → Requirements Formalization → Adversarial Review → Stakeholder Validation Gate
- Format: BDD/Gherkin for unambiguous acceptance criteria
- Research Basis: Spec-driven development research shows under-investing in specs is the #1 failure mode

**Hierarchical Task Decomposition (R-002)**
- Following the Planning Pattern: Goal Analysis → Phase Decomposition → Task Decomposition → Dependency Mapping → Context Scoping → Task Specification
- Each atomic task receives its own concrete requirement document
- MINIMUM context principle to reduce token usage and hallucination risk

**Multi-Model Consensus Verification (R-003)**
- Primary model (Kimi K2.5) → Secondary verification (Sonnet 4.6) → Tertiary arbitration (GPT-5.3)
- Consensus scoring algorithm based on ICE and MUSE research
- Behavioral testing + adversarial challenge approach

**GitHub-Native Task Tracking Architecture**
- GitHub becomes single source of truth for all project state
- Framework Concept → GitHub Object mapping:
  - SDLC Project → GitHub Milestone
  - SDLC Phase → GitHub Label (phase:requirements, phase:design, etc.)
  - Atomic Task → GitHub Issue
  - Task Implementation → GitHub Branch + PR
  - Verification Results → PR Comment
  - Quality Gate Decision → GitHub Label (gate:pass, gate:fail)

### 1.2 Tool Capabilities Matrix

Research across 8 specified tools:

| Capability | Kilo Code | Roo Code | ZenFlow | GitHub Copilot | Claude Code | Codex | Continue | Cline |
|------------|-----------|----------|---------|----------------|-------------|-------|----------|-------|
| Custom modes/roles | YAML modes | Orchestrator + custom | Custom workflows | Custom agents | CLAUDE.md + skills | Skills system | ❌ | Custom modes |
| Multi-agent orchestration | Orchestrator mode | Cloud agents + orchestrator | Parallel agents | Coding agent + agents panel | Agent Teams (3-5) | Multi-threaded | ❌ | ❌ |
| Spec-driven development | Via custom workflows | Via modes | Core feature (SDD) | Via custom instructions | Via CLAUDE.md | Via skills | ❌ | Via rules |
| Multi-model verification | Manual mode switching | Provider-per-mode | Committee approach | ❌ | Team model selection | ❌ | ❌ | Model switching |
| Sandboxed execution | ❌ Local only | Cloud sandboxes | Isolated environments | GitHub Actions sandbox | Local execution | Native sandboxing | N/A | ❌ Local only |
| MCP support | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ Limited | ❌ | ✅ |

**Key Finding:** ZenFlow is the only tool with native spec-driven development and multi-agent verification ("committee approach") as core features.

### 1.3 Workflow Engine Evaluation

**Contenders Analyzed:**

| Framework | Core Paradigm | Primary Strength | Maturity |
|-----------|---------------|------------------|----------|
| LangGraph | Graph-based stateful workflows | Explicit DAG control, branching, debugging | Most mature (106k ★) |
| CrewAI | Role-based team coordination | YAML-driven, intuitive setup | Mid-maturity (30k+ ★) |
| AutoGen | Conversational multi-agent | Dialogue-driven, flexible topologies | Research-oriented (43.1k+ ★) |
| OpenAI Agents SDK | Lightweight primitives | Minimal abstractions, fast deployment | Newest |

**Head-to-Head Comparison (Key Criteria):**

| Criterion | LangGraph | CrewAI | AutoGen | OpenAI Agents SDK |
|-----------|-----------|--------|---------|-------------------|
| Workflow complexity | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| State management | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Parallelization | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Observability | ⭐⭐⭐⭐⭐ (LangSmith/Langfuse) | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Error handling | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Token efficiency | ⭐⭐⭐⭐⭐ (lowest latency) | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| Production readiness | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

**Recommendation:** LangGraph is superior for SDLC framework due to:
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability with state transition logs and visual graph traces
- Lowest latency and token usage in benchmarks
- Native parallel execution for independent subtasks
- Conditional edges for gating decisions and retry mechanisms

---

## 2. MCP Servers Research

### 2.1 Protocol Understanding

**MCP (Model Context Protocol)** by Anthropic:
- Standard for giving agents access to external tools, data sources, and APIs
- Official repository: `modelcontextprotocol/servers`
- Hundreds of community servers for GitHub, Git, Slack, databases, browsers

**A2A (Agent2Agent) Protocol** by Google (Linux Foundation):
- Enables agents built on different frameworks to discover each other
- Uses JSON-RPC 2.0 over HTTPS
- Complementary to MCP: A2A handles agent-to-agent, MCP handles agent-to-tool

### 2.2 GitHub MCP Server Integration

**Key Tools Available:**
- `create_issue` / `update_issue` — Task creation and status updates
- `create_pull_request` / `merge_pull_request` — Implementation tracking
- `create_branch` — Isolation for atomic tasks
- `add_issue_comment` — Posting verification results, cost data, adversarial findings
- `add_labels` — Phase tracking, gate status, priority
- `assign_copilot_to_issue` — Delegate additional work to Copilot agent
- `search_issues` / `list_pull_requests` — Orchestrator reads project state

### 2.3 Event-Driven Pipeline Architecture

```
Event Flow:
1. LangGraph orchestrator decomposes task → creates GitHub Issue
2. GitHub Issue creation triggers Kilo webhook
3. Kilo Cloud Agent clones repo, creates branch, implements task
4. Kilo Cloud Agent auto-commits and pushes → creates PR
5. PR creation triggers GitHub Agentic Workflow
6. Agentic Workflow runs verification (Code Reviews, tests)
7. Verification results posted as PR comments
8. LangGraph orchestrator reads PR state via GitHub MCP → decides gate
```

---

## 3. Agent Orchestration Research

### 3.1 Inter-Agent Communication Patterns

**Patterns Evaluated:**

| Pattern | How It Works | Best For | Limitations |
|---------|--------------|----------|-------------|
| Subagents | Parent spawns child, receives only results | Simple delegation | No ongoing collaboration |
| Skills | Reusable capabilities agents can invoke | Standardized tasks | Limited context sharing |
| Handoffs | Agent A passes control to Agent B | Sequential workflows | No parallel collaboration |
| Claude Code Agent Teams | Shared task lists, direct messaging, self-coordination | Complex collaboration | Requires Claude Code |
| Roo Code Orchestrator | Hierarchical meta-prompts, context-passing protocols | Structured workflows | Learning curve |

**Key Finding:** Claude Code Agent Teams represent the most advanced inter-agent communication model with shared task lists, direct messaging, and self-coordination capabilities.

### 3.2 Agent Skills Collections

**Top Repositories:**

| Repository | Stars | What It Does |
|------------|-------|--------------|
| anthropic/skills | 61k ★ | Official skills — document creation, design, MCP builder, webapp testing |
| VoltAgent/awesome-agent-skills | 4.7k ★ | Most comprehensive curated list — 200+ skills from major publishers |
| skillcreatorai/Ai-Agent-Skills | — | "Homebrew for AI Agent Skills" — universal installer |

**Standout Skill Categories:**
- **Context Engineering** (by muratcankoylan): context compression, degradation detection, multi-agent patterns, memory systems
- **Security** (by Trail of Bits): 20+ skills including audit context building, static analysis, property-based testing
- **Development** (by obra): subagent-driven development, systematic debugging, root-cause tracing

### 3.3 Multi-Agent Workflow Frameworks

| Framework | Stars | Best For | Approach |
|-----------|-------|----------|----------|
| LangGraph | 106k ★ | Complex workflows with branching logic | Graph-based DAG, explicit state management |
| CrewAI | 30k+ ★ | Fastest time-to-production | Role-based agents with task delegation |
| AutoGen | 43.1k+ ★ | Conversational multi-agent, human-in-loop | Agents chat and iterate naturally |
| Agno | 29k+ ★ | Full-stack multi-agent | Supports all major LLM providers |
| Letta | 15.9k+ ★ | Stateful long-running agents | Memory persistence across sessions |

**Token Efficiency Note:** LangGraph uses ~2,000 tokens per task vs. CrewAI's ~3,500 and AutoGen's ~8,000.

---

## 4. Context Management Research

### 4.1 Context Transfer Protocol

**Spec Artifact Chain Approach:**
- Each SDLC phase produces a spec artifact
- Artifacts are passed along the chain: Requirements Spec → Design Spec → Implementation Spec → Test Spec
- Each artifact includes: context scope, acceptance criteria, constraints, token budget

### 4.2 Context Scoping Principles

**For each atomic task, determine MINIMUM context required:**
- Files needed
- Specs relevant
- Constraints to enforce
- Token budget allocation

### 4.3 Token Optimization Strategies

- Task-specific context reduces bloat
- Avoid conversation history growth
- Use structured JSON output for machine-readable documentation
- Implement context compression for long-running sessions

---

## 5. Testing Frameworks Research

### 5.1 Smoke Testing Framework Architecture

**Core Capabilities (Target State):**

| Capability | Description |
|------------|-------------|
| Universal web interaction engine | Playwright-based, handles all element types, dynamic content, complex forms |
| Dynamic multi-stack orchestration | 3+ containerized test environments (aio, int, prod) with auto port allocation (9330-9399) |
| Intelligent resilience system | Auto retry, element detection strategies, timeout handling, latency tolerance |
| Parallel test execution | Across multiple sites and within same site simultaneously |
| Complete observability stack | WebSocket updates, Prometheus metrics, structured JSON logging, artifact management |
| Database state management | Bidirectional reset supporting PostgreSQL and Oracle |
| Configuration-driven architecture | YAML test definitions |
| Multiple execution interfaces | UI dashboard (Flask), REST API (Express), CLI, programmatic |
| Self-healing capabilities | Element locator fallbacks, intelligent wait strategies, adaptive selectors |

### 5.2 Deviation Detection System

**Deviation Types to Track:**
- Selector Deviations (configured vs. actual selector used)
- Timing Deviations (configured timeout vs. actual wait time)
- Validation Deviations (expected vs. actual error messages)
- Workflow Deviations (configured steps vs. actual execution)
- Data Deviations (expected vs. actual dropdown options)

**Deviation Dashboard Features:**
- Summary View: Total deviations by type, severity, status
- List View: Paginated table with test name, deviation type, timestamp, environment
- Detail View: Side-by-side comparison, visual diff, timeline, frequency chart
- Trend Analysis: Charts showing deviations over time, by module, most common types
- Review Workflow: Assign, comment, batch operations, export reports

### 5.3 Test-Driven Development of UI

**TDD Workflow for Dashboard:**
1. Write tests for desired UI features before implementation
2. Implement UI features to pass tests
3. Validate all UI components work correctly
4. Ensure accessibility compliance
5. Verify responsive design across viewports

---

## 6. CI/CD Patterns Research

### 6.1 GitHub-Native CI/CD Integration

**GitHub Agentic Workflows** (Technical Preview):
- Markdown-defined automations that run coding agents inside GitHub Actions
- Combined with Kilo Code's webhook triggers for event-driven pipeline

### 6.2 Jenkins Integration

**Smoke Test Pipeline:**
- Jenkins triggers deployment → Smoke tests start
- KEDA scales AI analyzer from 0 → 1 pod (5-10 seconds)
- 8 Playwright pods run parallel tests → Call AI service when selectors fail
- AI analyzer handles 20-30 requests/minute
- Tests complete → AI pod scales to 0 after cooldown

### 6.3 Kubernetes Deployment Strategy

**Shared AI Service Pattern (Recommended):**
```
┌─────────────────────────────────────────┐
│  8-Node Kubernetes Cluster              │
├─────────────────────────────────────────┤
│  Smoke Test Pods (6-8 parallel)         │
│  ├─ Playwright container (2GB RAM)      │
│  └─ Calls AI service via HTTP           │
├─────────────────────────────────────────┤
│  AI Analyzer Pod (1-2 replicas)         │
│  ├─ Qwen3-0.6B model (2-3GB RAM)       │
│  └─ Serves all smoke test pods          │
└─────────────────────────────────────────┘
```

**Resource Distribution (8 Nodes @ 4-8 cores, 16-32GB RAM each):**
- Total capacity: 64 CPU cores, 256GB RAM
- Smoke test allocation: 16GB RAM (Playwright) + 3-6GB RAM (AI) = ~20-25GB
- Total consumption: <10% of cluster resources

---

## 7. Tiny AI Models for Testing Research

### 7.1 Model Comparison

| Model | Parameters | Docker Size | Inference Speed | Best For |
|-------|------------|-------------|-----------------|----------|
| SmolLM2-360M | 360M | ~400MB | <100ms | Quick pattern matching, selector analysis |
| Qwen2-0.5B | 500M | ~500MB | ~150ms | Reasoning about failures, context understanding |
| Qwen3-0.6B | 600M | ~600MB | ~5ms/token | Complex decision-making, code understanding |
| Phi-3-mini | 3.8B | ~2.5GB | ~300ms | Complex decision-making, code understanding |

### 7.2 Qwen3-0.6B Deep Dive

**Key Advantages:**
- Released April 2025, trained on 36 trillion tokens across 119 languages
- 32K context window (can analyze entire test suites, DOM snapshots, git diffs)
- Benchmarks: 73% on MATH500, 79.2% on GSM8K, 30.5% on HumanEval
- Built-in agent capabilities for automation and workflow orchestration
- Dual reasoning modes: "thinking" and "non-thinking"

**Resource Requirements:**
- RAM: 8GB total system, ~3GB during inference
- Storage: 3GB for quantized model files
- CPU: 4-8 cores recommended, 2 cores minimum
- Inference speed: 10-30 tokens/second on CPU-only

**Kubernetes Configuration:**
```yaml
resources:
  requests:
    memory: "2Gi"
    cpu: "1000m"
  limits:
    memory: "3Gi"
    cpu: "2000m"
```

### 7.3 Selector Intelligence Layer

**Implementation Approach:**
1. Analyze selector failures and compare current vs. expected DOM structures
2. Evaluate error patterns against historical test data
3. Determine retry worthiness using context (commit messages, recent code changes, error frequency)
4. Provide confidence scores for "legitimate failure" vs. "trivial UI change"

**Decision Framework:**
- Legitimate test failure → FAIL
- Cosmetic change → RETRY
- Timing issue → RETRY
- Environmental → RETRY

---

## 8. ZenFlow Integration Research

### 8.1 ZenFlow Core Concepts

**Four Pillars:**
1. Structured Workflows
2. SDD (Spec-Driven Development)
3. Multi-Agent Verification
4. Parallel Execution

### 8.2 24-Step Custom Workflow

**Phases:**
1. Planning
2. Design
3. Architecture
4. Implementation
5. Review
6. Testing
7. Validation
8. Optimization
9. Refactoring
10. Performance Optimization
11. Production Polish

### 8.3 Evidence-Driven Development

**Zen Rules:**
- All decisions must be based on empirical evidence
- No assumptions without verification
- Continuous validation at each phase
- Automated verification gates

---

## 9. Frontend Analysis Methodology Research

### 9.1 Code Relationship Database Approach

**Core Problem Addressed:**
"I do not know what connects to what, code paths are uncertain, and I need a method to ensure everything is mapped, tested, and maintainable."

**Solution:** Graph database approach treating code as queryable graph structure
- Nodes = files, functions, components
- Edges = imports, calls, relationships
- Enables powerful queries about codebase

### 9.2 Deliverables Created

| Deliverable | Lines | Purpose |
|-------------|-------|---------|
| IMPLEMENTATION_SUMMARY.md | 600 | Complete system overview |
| frontend_analysis_plan.md | 929 | 22-day roadmap, 8 phases |
| quick_start_guide.md | 311 | 30-minute insights |
| tools/dependency_mapper.py | 341 | Automated codebase analysis |
| tools/generate_graph_visualization.html | 536 | Interactive dependency graph |
| VISUAL_ROADMAP.md | 738 | Flowcharts and diagrams |

### 9.3 Key Innovations

- **Graph Database Approach:** Queryable code relationships
- **AI Agent Compatibility:** Structured JSON output, machine-readable documentation
- **Evidence-Based Methods:** Tools from 2026 research (FalkorDB, GitKraken Codemaps, Vitest, Playwright)

---

## 10. Sources Discovered in Space

### 10.1 Official Documentation
- LangGraph Documentation (langchain-ai.github.io)
- Langfuse Documentation (langfuse.com)
- ZenFlow Documentation (zenflow.ai)
- Claude Code Documentation (code.claude.ai)
- GitHub Copilot Documentation (github.com)
- OpenAI Codex Documentation (openai.com)

### 10.2 Research Papers
- FastFlowLM: Efficient LLM Inference (github.com)
- Speculative Decoding Research (AMD dev reports)
- AI-SDLC Maturity Model (eleks.com)

### 10.3 GitHub Repositories
- modelcontextprotocol/servers (MCP servers)
- anthropic/skills (61k ★)
- VoltAgent/awesome-agent-skills (4.7k ★)
- langchain-ai/langgraph (106k ★)
- crewAIInc/crewAI (30k+ ★)
- microsoft/autogen (43.1k+ ★)

### 10.4 Industry Sources
- prnewswire.com (Claude Code Agent Teams)
- xebia.com (Kilo Code/Roo Code analysis)
- intuitionlabs.ai (OpenAI Codex automation)
- linkedin.com (BDD/Gherkin acceptance criteria)
- thoughtworks.com (shift-left involvement)

---

## 11. Research Gaps Identified

### 11.1 Remaining Gaps After Prior Work Integration

1. **MCP Server Ecosystem Deep Dive**
   - Prior work identified MCP protocol but didn't exhaustively catalog all available servers
   - Gap: Complete inventory of production-ready MCP servers by category

2. **A2A Protocol Implementation Details**
   - Prior work mentioned A2A but didn't explore implementation patterns
   - Gap: Concrete A2A integration examples for agent-to-agent communication

3. **Local LLM Deployment Patterns**
   - Prior work mentioned local models but focused on cloud
   - Gap: Comprehensive local LLM deployment architecture for air-gapped environments

4. **Cross-Framework Agent Interoperability**
   - Prior work compared frameworks but didn't address interoperability
   - Gap: Patterns for agents from different frameworks to collaborate

5. **Production Hardening Patterns**
   - Prior work focused on architecture design
   - Gap: Operational runbooks, monitoring, alerting for production agent systems

6. **Security & Compliance for Agent Systems**
   - Prior work mentioned security briefly
   - Gap: Comprehensive security framework for autonomous agent systems

7. **Cost Optimization at Scale**
   - Prior work mentioned cost tracking
   - Gap: Advanced cost optimization strategies for enterprise-scale deployments

### 11.2 Cross-References to Research Taxonomy

| Taxonomy Category | Prior Work Coverage | Gap Status |
|-------------------|---------------------|------------|
| Agentic SDLC Patterns | Comprehensive (v1-v3) | Minor gaps in implementation details |
| MCP Servers | Protocol identified | Needs server catalog |
| Agent Orchestration | LangGraph recommended | Needs A2A implementation |
| Context Management | Spec artifact chain defined | Needs compression strategies |
| Testing Frameworks | Smoke testing architecture | Needs production hardening |
| CI/CD Patterns | GitHub-native approach | Needs operational runbooks |

---

## 12. Key Decisions & Conclusions from Prior Work

### 12.1 Workflow Engine Decision
**Decision:** Use LangGraph  
**Rationale:** 
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability
- Lowest latency and token usage
- Native parallel execution

### 12.2 Model Selection Decision
**Decision:** Kimi K2.5 as primary, Sonnet 4.6, GPT-5.3, Gemini 3 Pro/Flash  
**Rationale:**
- Cost optimization (Kimi is cheapest)
- Escalation path for complex tasks
- Multi-model consensus verification

### 12.3 Task Tracking Decision
**Decision:** GitHub-native (Issues, PRs, branches)  
**Rationale:**
- Permanent, auditable record
- Human-readable project state
- Native CI/CD integration
- Built-in collaboration

### 12.4 Testing Approach Decision
**Decision:** Behavioral testing + consensus-based evaluation + adversarial challenge  
**Rationale:**
- Empirical verification
- Reduces false positives
- Catches edge cases

### 12.5 Local vs Cloud Decision
**Decision:** Hybrid approach  
**Rationale:**
- Local for planning/design (cost, privacy)
- Cloud for implementation (speed)
- Local for final validation (accuracy)

---

## 13. Integration Recommendations

### 13.1 For New Research

1. **Build on LangGraph Foundation**
   - Prior work already selected LangGraph; new research should assume this baseline
   - Focus on graph node/edge design patterns

2. **Extend GitHub-Native Approach**
   - Use GitHub as single source of truth
   - Leverage GitHub MCP server for automation

3. **Incorporate ZenFlow Patterns**
   - Use 24-step workflow as reference
   - Apply evidence-driven development principles

4. **Leverage Tiny AI Models**
   - Qwen3-0.6B for selector intelligence
   - Deploy as shared service in K8s

### 13.2 For Implementation

1. **Start with Smoke Testing Framework**
   - Prior work includes comprehensive architecture
   - Use as proving ground for agentic patterns

2. **Implement Deviation Detection Early**
   - Critical for self-healing capabilities
   - Enables continuous improvement

3. **Use Kilo Code Cloud Agents**
   - For PR reviews and webhook automation
   - Integrates with GitHub-native workflow

---

## 14. Summary Statistics

| Metric | Value |
|--------|-------|
| Research Threads Analyzed | 8+ |
| Sources Cited | 160+ |
| Requirements Versions | 3 (v1 → v2 → v3) |
| Tools Evaluated | 8 |
| Workflow Frameworks Compared | 4 |
| AI Models Analyzed | 4+ |
| SDLC Phases Defined | 7 |
| GitHub Repositories Referenced | 15+ |

---

## 15. Document Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025 | Initial extraction and synthesis from Perplexity Space |

---

*This document represents a comprehensive integration of all substantive research found in the "Smoke Test Framework" Perplexity Space. It should be treated as a living document and updated as new research emerges.*

# Perplexity Space Research Integration: Smoke Test Framework

**Source:** https://www.perplexity.ai/spaces/smoke-test-framework-_L0_2o2dRyaDjDbhcmyOfw  
**Extraction Date:** 2025  
**Research Threads Analyzed:** 8+ substantive threads

---

## Executive Summary

This document synthesizes all substantive research from the "Smoke Test Framework" Perplexity Space, which contains extensive prior work on AI agentic SDLC frameworks, testing infrastructure, MCP servers, agent orchestration, and autonomous development workflows. The space represents 160+ research sources and multiple iterative refinement cycles on designing production-grade autonomous AI coding systems.

### Key Prior Work Identified:
1. **AI Agentic Autonomous SDLC Framework** - Comprehensive requirements across 3 major versions
2. **Smoke Testing Framework Architecture** - Playwright-based enterprise testing platform design
3. **Agent Skills & Workflows Research** - 200+ curated skills from major AI coding tools
4. **Tiny AI Models for Testing** - Docker-optimized models for selector adaptation
5. **ZenFlow Integration** - 24-step autonomous workflow for evidence-driven development
6. **Frontend Analysis Methodology** - Code relationship database approach

---

## 1. Agentic SDLC Patterns Research

### 1.1 Core Architecture Requirements (R-001 to R-014)

**Source Thread:** AI Agentic Autonomous SDLC Framework (Requirements v1-v3)

#### Key Findings:

**Autonomous Requirements Engineering (R-001)**
- Problem: AI agents fail when requirements are insufficient
- Solution: Multi-phase requirements engineering pipeline:
  - Intake → Intent Inference → Clarification Generation → Research Phase → Requirements Formalization → Adversarial Review → Stakeholder Validation Gate
- Format: BDD/Gherkin for unambiguous acceptance criteria
- Research Basis: Spec-driven development research shows under-investing in specs is the #1 failure mode

**Hierarchical Task Decomposition (R-002)**
- Following the Planning Pattern: Goal Analysis → Phase Decomposition → Task Decomposition → Dependency Mapping → Context Scoping → Task Specification
- Each atomic task receives its own concrete requirement document
- MINIMUM context principle to reduce token usage and hallucination risk

**Multi-Model Consensus Verification (R-003)**
- Primary model (Kimi K2.5) → Secondary verification (Sonnet 4.6) → Tertiary arbitration (GPT-5.3)
- Consensus scoring algorithm based on ICE and MUSE research
- Behavioral testing + adversarial challenge approach

**GitHub-Native Task Tracking Architecture**
- GitHub becomes single source of truth for all project state
- Framework Concept → GitHub Object mapping:
  - SDLC Project → GitHub Milestone
  - SDLC Phase → GitHub Label (phase:requirements, phase:design, etc.)
  - Atomic Task → GitHub Issue
  - Task Implementation → GitHub Branch + PR
  - Verification Results → PR Comment
  - Quality Gate Decision → GitHub Label (gate:pass, gate:fail)

### 1.2 Tool Capabilities Matrix

Research across 8 specified tools:

| Capability | Kilo Code | Roo Code | ZenFlow | GitHub Copilot | Claude Code | Codex | Continue | Cline |
|------------|-----------|----------|---------|----------------|-------------|-------|----------|-------|
| Custom modes/roles | YAML modes | Orchestrator + custom | Custom workflows | Custom agents | CLAUDE.md + skills | Skills system | ❌ | Custom modes |
| Multi-agent orchestration | Orchestrator mode | Cloud agents + orchestrator | Parallel agents | Coding agent + agents panel | Agent Teams (3-5) | Multi-threaded | ❌ | ❌ |
| Spec-driven development | Via custom workflows | Via modes | Core feature (SDD) | Via custom instructions | Via CLAUDE.md | Via skills | ❌ | Via rules |
| Multi-model verification | Manual mode switching | Provider-per-mode | Committee approach | ❌ | Team model selection | ❌ | ❌ | Model switching |
| Sandboxed execution | ❌ Local only | Cloud sandboxes | Isolated environments | GitHub Actions sandbox | Local execution | Native sandboxing | N/A | ❌ Local only |
| MCP support | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ Limited | ❌ | ✅ |

**Key Finding:** ZenFlow is the only tool with native spec-driven development and multi-agent verification ("committee approach") as core features.

### 1.3 Workflow Engine Evaluation

**Contenders Analyzed:**

| Framework | Core Paradigm | Primary Strength | Maturity |
|-----------|---------------|------------------|----------|
| LangGraph | Graph-based stateful workflows | Explicit DAG control, branching, debugging | Most mature (106k ★) |
| CrewAI | Role-based team coordination | YAML-driven, intuitive setup | Mid-maturity (30k+ ★) |
| AutoGen | Conversational multi-agent | Dialogue-driven, flexible topologies | Research-oriented (43.1k+ ★) |
| OpenAI Agents SDK | Lightweight primitives | Minimal abstractions, fast deployment | Newest |

**Head-to-Head Comparison (Key Criteria):**

| Criterion | LangGraph | CrewAI | AutoGen | OpenAI Agents SDK |
|-----------|-----------|--------|---------|-------------------|
| Workflow complexity | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| State management | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Parallelization | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Observability | ⭐⭐⭐⭐⭐ (LangSmith/Langfuse) | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Error handling | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Token efficiency | ⭐⭐⭐⭐⭐ (lowest latency) | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| Production readiness | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

**Recommendation:** LangGraph is superior for SDLC framework due to:
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability with state transition logs and visual graph traces
- Lowest latency and token usage in benchmarks
- Native parallel execution for independent subtasks
- Conditional edges for gating decisions and retry mechanisms

---

## 2. MCP Servers Research

### 2.1 Protocol Understanding

**MCP (Model Context Protocol)** by Anthropic:
- Standard for giving agents access to external tools, data sources, and APIs
- Official repository: `modelcontextprotocol/servers`
- Hundreds of community servers for GitHub, Git, Slack, databases, browsers

**A2A (Agent2Agent) Protocol** by Google (Linux Foundation):
- Enables agents built on different frameworks to discover each other
- Uses JSON-RPC 2.0 over HTTPS
- Complementary to MCP: A2A handles agent-to-agent, MCP handles agent-to-tool

### 2.2 GitHub MCP Server Integration

**Key Tools Available:**
- `create_issue` / `update_issue` — Task creation and status updates
- `create_pull_request` / `merge_pull_request` — Implementation tracking
- `create_branch` — Isolation for atomic tasks
- `add_issue_comment` — Posting verification results, cost data, adversarial findings
- `add_labels` — Phase tracking, gate status, priority
- `assign_copilot_to_issue` — Delegate additional work to Copilot agent
- `search_issues` / `list_pull_requests` — Orchestrator reads project state

### 2.3 Event-Driven Pipeline Architecture

```
Event Flow:
1. LangGraph orchestrator decomposes task → creates GitHub Issue
2. GitHub Issue creation triggers Kilo webhook
3. Kilo Cloud Agent clones repo, creates branch, implements task
4. Kilo Cloud Agent auto-commits and pushes → creates PR
5. PR creation triggers GitHub Agentic Workflow
6. Agentic Workflow runs verification (Code Reviews, tests)
7. Verification results posted as PR comments
8. LangGraph orchestrator reads PR state via GitHub MCP → decides gate
```

---

## 3. Agent Orchestration Research

### 3.1 Inter-Agent Communication Patterns

**Patterns Evaluated:**

| Pattern | How It Works | Best For | Limitations |
|---------|--------------|----------|-------------|
| Subagents | Parent spawns child, receives only results | Simple delegation | No ongoing collaboration |
| Skills | Reusable capabilities agents can invoke | Standardized tasks | Limited context sharing |
| Handoffs | Agent A passes control to Agent B | Sequential workflows | No parallel collaboration |
| Claude Code Agent Teams | Shared task lists, direct messaging, self-coordination | Complex collaboration | Requires Claude Code |
| Roo Code Orchestrator | Hierarchical meta-prompts, context-passing protocols | Structured workflows | Learning curve |

**Key Finding:** Claude Code Agent Teams represent the most advanced inter-agent communication model with shared task lists, direct messaging, and self-coordination capabilities.

### 3.2 Agent Skills Collections

**Top Repositories:**

| Repository | Stars | What It Does |
|------------|-------|--------------|
| anthropic/skills | 61k ★ | Official skills — document creation, design, MCP builder, webapp testing |
| VoltAgent/awesome-agent-skills | 4.7k ★ | Most comprehensive curated list — 200+ skills from major publishers |
| skillcreatorai/Ai-Agent-Skills | — | "Homebrew for AI Agent Skills" — universal installer |

**Standout Skill Categories:**
- **Context Engineering** (by muratcankoylan): context compression, degradation detection, multi-agent patterns, memory systems
- **Security** (by Trail of Bits): 20+ skills including audit context building, static analysis, property-based testing
- **Development** (by obra): subagent-driven development, systematic debugging, root-cause tracing

### 3.3 Multi-Agent Workflow Frameworks

| Framework | Stars | Best For | Approach |
|-----------|-------|----------|----------|
| LangGraph | 106k ★ | Complex workflows with branching logic | Graph-based DAG, explicit state management |
| CrewAI | 30k+ ★ | Fastest time-to-production | Role-based agents with task delegation |
| AutoGen | 43.1k+ ★ | Conversational multi-agent, human-in-loop | Agents chat and iterate naturally |
| Agno | 29k+ ★ | Full-stack multi-agent | Supports all major LLM providers |
| Letta | 15.9k+ ★ | Stateful long-running agents | Memory persistence across sessions |

**Token Efficiency Note:** LangGraph uses ~2,000 tokens per task vs. CrewAI's ~3,500 and AutoGen's ~8,000.

---

## 4. Context Management Research

### 4.1 Context Transfer Protocol

**Spec Artifact Chain Approach:**
- Each SDLC phase produces a spec artifact
- Artifacts are passed along the chain: Requirements Spec → Design Spec → Implementation Spec → Test Spec
- Each artifact includes: context scope, acceptance criteria, constraints, token budget

### 4.2 Context Scoping Principles

**For each atomic task, determine MINIMUM context required:**
- Files needed
- Specs relevant
- Constraints to enforce
- Token budget allocation

### 4.3 Token Optimization Strategies

- Task-specific context reduces bloat
- Avoid conversation history growth
- Use structured JSON output for machine-readable documentation
- Implement context compression for long-running sessions

---

## 5. Testing Frameworks Research

### 5.1 Smoke Testing Framework Architecture

**Core Capabilities (Target State):**

| Capability | Description |
|------------|-------------|
| Universal web interaction engine | Playwright-based, handles all element types, dynamic content, complex forms |
| Dynamic multi-stack orchestration | 3+ containerized test environments (aio, int, prod) with auto port allocation (9330-9399) |
| Intelligent resilience system | Auto retry, element detection strategies, timeout handling, latency tolerance |
| Parallel test execution | Across multiple sites and within same site simultaneously |
| Complete observability stack | WebSocket updates, Prometheus metrics, structured JSON logging, artifact management |
| Database state management | Bidirectional reset supporting PostgreSQL and Oracle |
| Configuration-driven architecture | YAML test definitions |
| Multiple execution interfaces | UI dashboard (Flask), REST API (Express), CLI, programmatic |
| Self-healing capabilities | Element locator fallbacks, intelligent wait strategies, adaptive selectors |

### 5.2 Deviation Detection System

**Deviation Types to Track:**
- Selector Deviations (configured vs. actual selector used)
- Timing Deviations (configured timeout vs. actual wait time)
- Validation Deviations (expected vs. actual error messages)
- Workflow Deviations (configured steps vs. actual execution)
- Data Deviations (expected vs. actual dropdown options)

**Deviation Dashboard Features:**
- Summary View: Total deviations by type, severity, status
- List View: Paginated table with test name, deviation type, timestamp, environment
- Detail View: Side-by-side comparison, visual diff, timeline, frequency chart
- Trend Analysis: Charts showing deviations over time, by module, most common types
- Review Workflow: Assign, comment, batch operations, export reports

### 5.3 Test-Driven Development of UI

**TDD Workflow for Dashboard:**
1. Write tests for desired UI features before implementation
2. Implement UI features to pass tests
3. Validate all UI components work correctly
4. Ensure accessibility compliance
5. Verify responsive design across viewports

---

## 6. CI/CD Patterns Research

### 6.1 GitHub-Native CI/CD Integration

**GitHub Agentic Workflows** (Technical Preview):
- Markdown-defined automations that run coding agents inside GitHub Actions
- Combined with Kilo Code's webhook triggers for event-driven pipeline

### 6.2 Jenkins Integration

**Smoke Test Pipeline:**
- Jenkins triggers deployment → Smoke tests start
- KEDA scales AI analyzer from 0 → 1 pod (5-10 seconds)
- 8 Playwright pods run parallel tests → Call AI service when selectors fail
- AI analyzer handles 20-30 requests/minute
- Tests complete → AI pod scales to 0 after cooldown

### 6.3 Kubernetes Deployment Strategy

**Shared AI Service Pattern (Recommended):**
```
┌─────────────────────────────────────────┐
│  8-Node Kubernetes Cluster              │
├─────────────────────────────────────────┤
│  Smoke Test Pods (6-8 parallel)         │
│  ├─ Playwright container (2GB RAM)      │
│  └─ Calls AI service via HTTP           │
├─────────────────────────────────────────┤
│  AI Analyzer Pod (1-2 replicas)         │
│  ├─ Qwen3-0.6B model (2-3GB RAM)       │
│  └─ Serves all smoke test pods          │
└─────────────────────────────────────────┘
```

**Resource Distribution (8 Nodes @ 4-8 cores, 16-32GB RAM each):**
- Total capacity: 64 CPU cores, 256GB RAM
- Smoke test allocation: 16GB RAM (Playwright) + 3-6GB RAM (AI) = ~20-25GB
- Total consumption: <10% of cluster resources

---

## 7. Tiny AI Models for Testing Research

### 7.1 Model Comparison

| Model | Parameters | Docker Size | Inference Speed | Best For |
|-------|------------|-------------|-----------------|----------|
| SmolLM2-360M | 360M | ~400MB | <100ms | Quick pattern matching, selector analysis |
| Qwen2-0.5B | 500M | ~500MB | ~150ms | Reasoning about failures, context understanding |
| Qwen3-0.6B | 600M | ~600MB | ~5ms/token | Complex decision-making, code understanding |
| Phi-3-mini | 3.8B | ~2.5GB | ~300ms | Complex decision-making, code understanding |

### 7.2 Qwen3-0.6B Deep Dive

**Key Advantages:**
- Released April 2025, trained on 36 trillion tokens across 119 languages
- 32K context window (can analyze entire test suites, DOM snapshots, git diffs)
- Benchmarks: 73% on MATH500, 79.2% on GSM8K, 30.5% on HumanEval
- Built-in agent capabilities for automation and workflow orchestration
- Dual reasoning modes: "thinking" and "non-thinking"

**Resource Requirements:**
- RAM: 8GB total system, ~3GB during inference
- Storage: 3GB for quantized model files
- CPU: 4-8 cores recommended, 2 cores minimum
- Inference speed: 10-30 tokens/second on CPU-only

**Kubernetes Configuration:**
```yaml
resources:
  requests:
    memory: "2Gi"
    cpu: "1000m"
  limits:
    memory: "3Gi"
    cpu: "2000m"
```

### 7.3 Selector Intelligence Layer

**Implementation Approach:**
1. Analyze selector failures and compare current vs. expected DOM structures
2. Evaluate error patterns against historical test data
3. Determine retry worthiness using context (commit messages, recent code changes, error frequency)
4. Provide confidence scores for "legitimate failure" vs. "trivial UI change"

**Decision Framework:**
- Legitimate test failure → FAIL
- Cosmetic change → RETRY
- Timing issue → RETRY
- Environmental → RETRY

---

## 8. ZenFlow Integration Research

### 8.1 ZenFlow Core Concepts

**Four Pillars:**
1. Structured Workflows
2. SDD (Spec-Driven Development)
3. Multi-Agent Verification
4. Parallel Execution

### 8.2 24-Step Custom Workflow

**Phases:**
1. Planning
2. Design
3. Architecture
4. Implementation
5. Review
6. Testing
7. Validation
8. Optimization
9. Refactoring
10. Performance Optimization
11. Production Polish

### 8.3 Evidence-Driven Development

**Zen Rules:**
- All decisions must be based on empirical evidence
- No assumptions without verification
- Continuous validation at each phase
- Automated verification gates

---

## 9. Frontend Analysis Methodology Research

### 9.1 Code Relationship Database Approach

**Core Problem Addressed:**
"I do not know what connects to what, code paths are uncertain, and I need a method to ensure everything is mapped, tested, and maintainable."

**Solution:** Graph database approach treating code as queryable graph structure
- Nodes = files, functions, components
- Edges = imports, calls, relationships
- Enables powerful queries about codebase

### 9.2 Deliverables Created

| Deliverable | Lines | Purpose |
|-------------|-------|---------|
| IMPLEMENTATION_SUMMARY.md | 600 | Complete system overview |
| frontend_analysis_plan.md | 929 | 22-day roadmap, 8 phases |
| quick_start_guide.md | 311 | 30-minute insights |
| tools/dependency_mapper.py | 341 | Automated codebase analysis |
| tools/generate_graph_visualization.html | 536 | Interactive dependency graph |
| VISUAL_ROADMAP.md | 738 | Flowcharts and diagrams |

### 9.3 Key Innovations

- **Graph Database Approach:** Queryable code relationships
- **AI Agent Compatibility:** Structured JSON output, machine-readable documentation
- **Evidence-Based Methods:** Tools from 2026 research (FalkorDB, GitKraken Codemaps, Vitest, Playwright)

---

## 10. Sources Discovered in Space

### 10.1 Official Documentation
- LangGraph Documentation (langchain-ai.github.io)
- Langfuse Documentation (langfuse.com)
- ZenFlow Documentation (zenflow.ai)
- Claude Code Documentation (code.claude.ai)
- GitHub Copilot Documentation (github.com)
- OpenAI Codex Documentation (openai.com)

### 10.2 Research Papers
- FastFlowLM: Efficient LLM Inference (github.com)
- Speculative Decoding Research (AMD dev reports)
- AI-SDLC Maturity Model (eleks.com)

### 10.3 GitHub Repositories
- modelcontextprotocol/servers (MCP servers)
- anthropic/skills (61k ★)
- VoltAgent/awesome-agent-skills (4.7k ★)
- langchain-ai/langgraph (106k ★)
- crewAIInc/crewAI (30k+ ★)
- microsoft/autogen (43.1k+ ★)

### 10.4 Industry Sources
- prnewswire.com (Claude Code Agent Teams)
- xebia.com (Kilo Code/Roo Code analysis)
- intuitionlabs.ai (OpenAI Codex automation)
- linkedin.com (BDD/Gherkin acceptance criteria)
- thoughtworks.com (shift-left involvement)

---

## 11. Research Gaps Identified

### 11.1 Remaining Gaps After Prior Work Integration

1. **MCP Server Ecosystem Deep Dive**
   - Prior work identified MCP protocol but didn't exhaustively catalog all available servers
   - Gap: Complete inventory of production-ready MCP servers by category

2. **A2A Protocol Implementation Details**
   - Prior work mentioned A2A but didn't explore implementation patterns
   - Gap: Concrete A2A integration examples for agent-to-agent communication

3. **Local LLM Deployment Patterns**
   - Prior work mentioned local models but focused on cloud
   - Gap: Comprehensive local LLM deployment architecture for air-gapped environments

4. **Cross-Framework Agent Interoperability**
   - Prior work compared frameworks but didn't address interoperability
   - Gap: Patterns for agents from different frameworks to collaborate

5. **Production Hardening Patterns**
   - Prior work focused on architecture design
   - Gap: Operational runbooks, monitoring, alerting for production agent systems

6. **Security & Compliance for Agent Systems**
   - Prior work mentioned security briefly
   - Gap: Comprehensive security framework for autonomous agent systems

7. **Cost Optimization at Scale**
   - Prior work mentioned cost tracking
   - Gap: Advanced cost optimization strategies for enterprise-scale deployments

### 11.2 Cross-References to Research Taxonomy

| Taxonomy Category | Prior Work Coverage | Gap Status |
|-------------------|---------------------|------------|
| Agentic SDLC Patterns | Comprehensive (v1-v3) | Minor gaps in implementation details |
| MCP Servers | Protocol identified | Needs server catalog |
| Agent Orchestration | LangGraph recommended | Needs A2A implementation |
| Context Management | Spec artifact chain defined | Needs compression strategies |
| Testing Frameworks | Smoke testing architecture | Needs production hardening |
| CI/CD Patterns | GitHub-native approach | Needs operational runbooks |

---

## 12. Key Decisions & Conclusions from Prior Work

### 12.1 Workflow Engine Decision
**Decision:** Use LangGraph  
**Rationale:** 
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability
- Lowest latency and token usage
- Native parallel execution

### 12.2 Model Selection Decision
**Decision:** Kimi K2.5 as primary, Sonnet 4.6, GPT-5.3, Gemini 3 Pro/Flash  
**Rationale:**
- Cost optimization (Kimi is cheapest)
- Escalation path for complex tasks
- Multi-model consensus verification

### 12.3 Task Tracking Decision
**Decision:** GitHub-native (Issues, PRs, branches)  
**Rationale:**
- Permanent, auditable record
- Human-readable project state
- Native CI/CD integration
- Built-in collaboration

### 12.4 Testing Approach Decision
**Decision:** Behavioral testing + consensus-based evaluation + adversarial challenge  
**Rationale:**
- Empirical verification
- Reduces false positives
- Catches edge cases

### 12.5 Local vs Cloud Decision
**Decision:** Hybrid approach  
**Rationale:**
- Local for planning/design (cost, privacy)
- Cloud for implementation (speed)
- Local for final validation (accuracy)

---

## 13. Integration Recommendations

### 13.1 For New Research

1. **Build on LangGraph Foundation**
   - Prior work already selected LangGraph; new research should assume this baseline
   - Focus on graph node/edge design patterns

2. **Extend GitHub-Native Approach**
   - Use GitHub as single source of truth
   - Leverage GitHub MCP server for automation

3. **Incorporate ZenFlow Patterns**
   - Use 24-step workflow as reference
   - Apply evidence-driven development principles

4. **Leverage Tiny AI Models**
   - Qwen3-0.6B for selector intelligence
   - Deploy as shared service in K8s

### 13.2 For Implementation

1. **Start with Smoke Testing Framework**
   - Prior work includes comprehensive architecture
   - Use as proving ground for agentic patterns

2. **Implement Deviation Detection Early**
   - Critical for self-healing capabilities
   - Enables continuous improvement

3. **Use Kilo Code Cloud Agents**
   - For PR reviews and webhook automation
   - Integrates with GitHub-native workflow

---

## 14. Summary Statistics

| Metric | Value |
|--------|-------|
| Research Threads Analyzed | 8+ |
| Sources Cited | 160+ |
| Requirements Versions | 3 (v1 → v2 → v3) |
| Tools Evaluated | 8 |
| Workflow Frameworks Compared | 4 |
| AI Models Analyzed | 4+ |
| SDLC Phases Defined | 7 |
| GitHub Repositories Referenced | 15+ |

---

## 15. Document Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025 | Initial extraction and synthesis from Perplexity Space |

---

*This document represents a comprehensive integration of all substantive research found in the "Smoke Test Framework" Perplexity Space. It should be treated as a living document and updated as new research emerges.*

# Perplexity Space Research Integration: Smoke Test Framework

**Source:** https://www.perplexity.ai/spaces/smoke-test-framework-_L0_2o2dRyaDjDbhcmyOfw  
**Extraction Date:** 2025  
**Research Threads Analyzed:** 8+ substantive threads

---

## Executive Summary

This document synthesizes all substantive research from the "Smoke Test Framework" Perplexity Space, which contains extensive prior work on AI agentic SDLC frameworks, testing infrastructure, MCP servers, agent orchestration, and autonomous development workflows. The space represents 160+ research sources and multiple iterative refinement cycles on designing production-grade autonomous AI coding systems.

### Key Prior Work Identified:
1. **AI Agentic Autonomous SDLC Framework** - Comprehensive requirements across 3 major versions
2. **Smoke Testing Framework Architecture** - Playwright-based enterprise testing platform design
3. **Agent Skills & Workflows Research** - 200+ curated skills from major AI coding tools
4. **Tiny AI Models for Testing** - Docker-optimized models for selector adaptation
5. **ZenFlow Integration** - 24-step autonomous workflow for evidence-driven development
6. **Frontend Analysis Methodology** - Code relationship database approach

---

## 1. Agentic SDLC Patterns Research

### 1.1 Core Architecture Requirements (R-001 to R-014)

**Source Thread:** AI Agentic Autonomous SDLC Framework (Requirements v1-v3)

#### Key Findings:

**Autonomous Requirements Engineering (R-001)**
- Problem: AI agents fail when requirements are insufficient
- Solution: Multi-phase requirements engineering pipeline:
  - Intake → Intent Inference → Clarification Generation → Research Phase → Requirements Formalization → Adversarial Review → Stakeholder Validation Gate
- Format: BDD/Gherkin for unambiguous acceptance criteria
- Research Basis: Spec-driven development research shows under-investing in specs is the #1 failure mode

**Hierarchical Task Decomposition (R-002)**
- Following the Planning Pattern: Goal Analysis → Phase Decomposition → Task Decomposition → Dependency Mapping → Context Scoping → Task Specification
- Each atomic task receives its own concrete requirement document
- MINIMUM context principle to reduce token usage and hallucination risk

**Multi-Model Consensus Verification (R-003)**
- Primary model (Kimi K2.5) → Secondary verification (Sonnet 4.6) → Tertiary arbitration (GPT-5.3)
- Consensus scoring algorithm based on ICE and MUSE research
- Behavioral testing + adversarial challenge approach

**GitHub-Native Task Tracking Architecture**
- GitHub becomes single source of truth for all project state
- Framework Concept → GitHub Object mapping:
  - SDLC Project → GitHub Milestone
  - SDLC Phase → GitHub Label (phase:requirements, phase:design, etc.)
  - Atomic Task → GitHub Issue
  - Task Implementation → GitHub Branch + PR
  - Verification Results → PR Comment
  - Quality Gate Decision → GitHub Label (gate:pass, gate:fail)

### 1.2 Tool Capabilities Matrix

Research across 8 specified tools:

| Capability | Kilo Code | Roo Code | ZenFlow | GitHub Copilot | Claude Code | Codex | Continue | Cline |
|------------|-----------|----------|---------|----------------|-------------|-------|----------|-------|
| Custom modes/roles | YAML modes | Orchestrator + custom | Custom workflows | Custom agents | CLAUDE.md + skills | Skills system | ❌ | Custom modes |
| Multi-agent orchestration | Orchestrator mode | Cloud agents + orchestrator | Parallel agents | Coding agent + agents panel | Agent Teams (3-5) | Multi-threaded | ❌ | ❌ |
| Spec-driven development | Via custom workflows | Via modes | Core feature (SDD) | Via custom instructions | Via CLAUDE.md | Via skills | ❌ | Via rules |
| Multi-model verification | Manual mode switching | Provider-per-mode | Committee approach | ❌ | Team model selection | ❌ | ❌ | Model switching |
| Sandboxed execution | ❌ Local only | Cloud sandboxes | Isolated environments | GitHub Actions sandbox | Local execution | Native sandboxing | N/A | ❌ Local only |
| MCP support | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ Limited | ❌ | ✅ |

**Key Finding:** ZenFlow is the only tool with native spec-driven development and multi-agent verification ("committee approach") as core features.

### 1.3 Workflow Engine Evaluation

**Contenders Analyzed:**

| Framework | Core Paradigm | Primary Strength | Maturity |
|-----------|---------------|------------------|----------|
| LangGraph | Graph-based stateful workflows | Explicit DAG control, branching, debugging | Most mature (106k ★) |
| CrewAI | Role-based team coordination | YAML-driven, intuitive setup | Mid-maturity (30k+ ★) |
| AutoGen | Conversational multi-agent | Dialogue-driven, flexible topologies | Research-oriented (43.1k+ ★) |
| OpenAI Agents SDK | Lightweight primitives | Minimal abstractions, fast deployment | Newest |

**Head-to-Head Comparison (Key Criteria):**

| Criterion | LangGraph | CrewAI | AutoGen | OpenAI Agents SDK |
|-----------|-----------|--------|---------|-------------------|
| Workflow complexity | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| State management | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Parallelization | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Observability | ⭐⭐⭐⭐⭐ (LangSmith/Langfuse) | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Error handling | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Token efficiency | ⭐⭐⭐⭐⭐ (lowest latency) | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| Production readiness | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

**Recommendation:** LangGraph is superior for SDLC framework due to:
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability with state transition logs and visual graph traces
- Lowest latency and token usage in benchmarks
- Native parallel execution for independent subtasks
- Conditional edges for gating decisions and retry mechanisms

---

## 2. MCP Servers Research

### 2.1 Protocol Understanding

**MCP (Model Context Protocol)** by Anthropic:
- Standard for giving agents access to external tools, data sources, and APIs
- Official repository: `modelcontextprotocol/servers`
- Hundreds of community servers for GitHub, Git, Slack, databases, browsers

**A2A (Agent2Agent) Protocol** by Google (Linux Foundation):
- Enables agents built on different frameworks to discover each other
- Uses JSON-RPC 2.0 over HTTPS
- Complementary to MCP: A2A handles agent-to-agent, MCP handles agent-to-tool

### 2.2 GitHub MCP Server Integration

**Key Tools Available:**
- `create_issue` / `update_issue` — Task creation and status updates
- `create_pull_request` / `merge_pull_request` — Implementation tracking
- `create_branch` — Isolation for atomic tasks
- `add_issue_comment` — Posting verification results, cost data, adversarial findings
- `add_labels` — Phase tracking, gate status, priority
- `assign_copilot_to_issue` — Delegate additional work to Copilot agent
- `search_issues` / `list_pull_requests` — Orchestrator reads project state

### 2.3 Event-Driven Pipeline Architecture

```
Event Flow:
1. LangGraph orchestrator decomposes task → creates GitHub Issue
2. GitHub Issue creation triggers Kilo webhook
3. Kilo Cloud Agent clones repo, creates branch, implements task
4. Kilo Cloud Agent auto-commits and pushes → creates PR
5. PR creation triggers GitHub Agentic Workflow
6. Agentic Workflow runs verification (Code Reviews, tests)
7. Verification results posted as PR comments
8. LangGraph orchestrator reads PR state via GitHub MCP → decides gate
```

---

## 3. Agent Orchestration Research

### 3.1 Inter-Agent Communication Patterns

**Patterns Evaluated:**

| Pattern | How It Works | Best For | Limitations |
|---------|--------------|----------|-------------|
| Subagents | Parent spawns child, receives only results | Simple delegation | No ongoing collaboration |
| Skills | Reusable capabilities agents can invoke | Standardized tasks | Limited context sharing |
| Handoffs | Agent A passes control to Agent B | Sequential workflows | No parallel collaboration |
| Claude Code Agent Teams | Shared task lists, direct messaging, self-coordination | Complex collaboration | Requires Claude Code |
| Roo Code Orchestrator | Hierarchical meta-prompts, context-passing protocols | Structured workflows | Learning curve |

**Key Finding:** Claude Code Agent Teams represent the most advanced inter-agent communication model with shared task lists, direct messaging, and self-coordination capabilities.

### 3.2 Agent Skills Collections

**Top Repositories:**

| Repository | Stars | What It Does |
|------------|-------|--------------|
| anthropic/skills | 61k ★ | Official skills — document creation, design, MCP builder, webapp testing |
| VoltAgent/awesome-agent-skills | 4.7k ★ | Most comprehensive curated list — 200+ skills from major publishers |
| skillcreatorai/Ai-Agent-Skills | — | "Homebrew for AI Agent Skills" — universal installer |

**Standout Skill Categories:**
- **Context Engineering** (by muratcankoylan): context compression, degradation detection, multi-agent patterns, memory systems
- **Security** (by Trail of Bits): 20+ skills including audit context building, static analysis, property-based testing
- **Development** (by obra): subagent-driven development, systematic debugging, root-cause tracing

### 3.3 Multi-Agent Workflow Frameworks

| Framework | Stars | Best For | Approach |
|-----------|-------|----------|----------|
| LangGraph | 106k ★ | Complex workflows with branching logic | Graph-based DAG, explicit state management |
| CrewAI | 30k+ ★ | Fastest time-to-production | Role-based agents with task delegation |
| AutoGen | 43.1k+ ★ | Conversational multi-agent, human-in-loop | Agents chat and iterate naturally |
| Agno | 29k+ ★ | Full-stack multi-agent | Supports all major LLM providers |
| Letta | 15.9k+ ★ | Stateful long-running agents | Memory persistence across sessions |

**Token Efficiency Note:** LangGraph uses ~2,000 tokens per task vs. CrewAI's ~3,500 and AutoGen's ~8,000.

---

## 4. Context Management Research

### 4.1 Context Transfer Protocol

**Spec Artifact Chain Approach:**
- Each SDLC phase produces a spec artifact
- Artifacts are passed along the chain: Requirements Spec → Design Spec → Implementation Spec → Test Spec
- Each artifact includes: context scope, acceptance criteria, constraints, token budget

### 4.2 Context Scoping Principles

**For each atomic task, determine MINIMUM context required:**
- Files needed
- Specs relevant
- Constraints to enforce
- Token budget allocation

### 4.3 Token Optimization Strategies

- Task-specific context reduces bloat
- Avoid conversation history growth
- Use structured JSON output for machine-readable documentation
- Implement context compression for long-running sessions

---

## 5. Testing Frameworks Research

### 5.1 Smoke Testing Framework Architecture

**Core Capabilities (Target State):**

| Capability | Description |
|------------|-------------|
| Universal web interaction engine | Playwright-based, handles all element types, dynamic content, complex forms |
| Dynamic multi-stack orchestration | 3+ containerized test environments (aio, int, prod) with auto port allocation (9330-9399) |
| Intelligent resilience system | Auto retry, element detection strategies, timeout handling, latency tolerance |
| Parallel test execution | Across multiple sites and within same site simultaneously |
| Complete observability stack | WebSocket updates, Prometheus metrics, structured JSON logging, artifact management |
| Database state management | Bidirectional reset supporting PostgreSQL and Oracle |
| Configuration-driven architecture | YAML test definitions |
| Multiple execution interfaces | UI dashboard (Flask), REST API (Express), CLI, programmatic |
| Self-healing capabilities | Element locator fallbacks, intelligent wait strategies, adaptive selectors |

### 5.2 Deviation Detection System

**Deviation Types to Track:**
- Selector Deviations (configured vs. actual selector used)
- Timing Deviations (configured timeout vs. actual wait time)
- Validation Deviations (expected vs. actual error messages)
- Workflow Deviations (configured steps vs. actual execution)
- Data Deviations (expected vs. actual dropdown options)

**Deviation Dashboard Features:**
- Summary View: Total deviations by type, severity, status
- List View: Paginated table with test name, deviation type, timestamp, environment
- Detail View: Side-by-side comparison, visual diff, timeline, frequency chart
- Trend Analysis: Charts showing deviations over time, by module, most common types
- Review Workflow: Assign, comment, batch operations, export reports

### 5.3 Test-Driven Development of UI

**TDD Workflow for Dashboard:**
1. Write tests for desired UI features before implementation
2. Implement UI features to pass tests
3. Validate all UI components work correctly
4. Ensure accessibility compliance
5. Verify responsive design across viewports

---

## 6. CI/CD Patterns Research

### 6.1 GitHub-Native CI/CD Integration

**GitHub Agentic Workflows** (Technical Preview):
- Markdown-defined automations that run coding agents inside GitHub Actions
- Combined with Kilo Code's webhook triggers for event-driven pipeline

### 6.2 Jenkins Integration

**Smoke Test Pipeline:**
- Jenkins triggers deployment → Smoke tests start
- KEDA scales AI analyzer from 0 → 1 pod (5-10 seconds)
- 8 Playwright pods run parallel tests → Call AI service when selectors fail
- AI analyzer handles 20-30 requests/minute
- Tests complete → AI pod scales to 0 after cooldown

### 6.3 Kubernetes Deployment Strategy

**Shared AI Service Pattern (Recommended):**
```
┌─────────────────────────────────────────┐
│  8-Node Kubernetes Cluster              │
├─────────────────────────────────────────┤
│  Smoke Test Pods (6-8 parallel)         │
│  ├─ Playwright container (2GB RAM)      │
│  └─ Calls AI service via HTTP           │
├─────────────────────────────────────────┤
│  AI Analyzer Pod (1-2 replicas)         │
│  ├─ Qwen3-0.6B model (2-3GB RAM)       │
│  └─ Serves all smoke test pods          │
└─────────────────────────────────────────┘
```

**Resource Distribution (8 Nodes @ 4-8 cores, 16-32GB RAM each):**
- Total capacity: 64 CPU cores, 256GB RAM
- Smoke test allocation: 16GB RAM (Playwright) + 3-6GB RAM (AI) = ~20-25GB
- Total consumption: <10% of cluster resources

---

## 7. Tiny AI Models for Testing Research

### 7.1 Model Comparison

| Model | Parameters | Docker Size | Inference Speed | Best For |
|-------|------------|-------------|-----------------|----------|
| SmolLM2-360M | 360M | ~400MB | <100ms | Quick pattern matching, selector analysis |
| Qwen2-0.5B | 500M | ~500MB | ~150ms | Reasoning about failures, context understanding |
| Qwen3-0.6B | 600M | ~600MB | ~5ms/token | Complex decision-making, code understanding |
| Phi-3-mini | 3.8B | ~2.5GB | ~300ms | Complex decision-making, code understanding |

### 7.2 Qwen3-0.6B Deep Dive

**Key Advantages:**
- Released April 2025, trained on 36 trillion tokens across 119 languages
- 32K context window (can analyze entire test suites, DOM snapshots, git diffs)
- Benchmarks: 73% on MATH500, 79.2% on GSM8K, 30.5% on HumanEval
- Built-in agent capabilities for automation and workflow orchestration
- Dual reasoning modes: "thinking" and "non-thinking"

**Resource Requirements:**
- RAM: 8GB total system, ~3GB during inference
- Storage: 3GB for quantized model files
- CPU: 4-8 cores recommended, 2 cores minimum
- Inference speed: 10-30 tokens/second on CPU-only

**Kubernetes Configuration:**
```yaml
resources:
  requests:
    memory: "2Gi"
    cpu: "1000m"
  limits:
    memory: "3Gi"
    cpu: "2000m"
```

### 7.3 Selector Intelligence Layer

**Implementation Approach:**
1. Analyze selector failures and compare current vs. expected DOM structures
2. Evaluate error patterns against historical test data
3. Determine retry worthiness using context (commit messages, recent code changes, error frequency)
4. Provide confidence scores for "legitimate failure" vs. "trivial UI change"

**Decision Framework:**
- Legitimate test failure → FAIL
- Cosmetic change → RETRY
- Timing issue → RETRY
- Environmental → RETRY

---

## 8. ZenFlow Integration Research

### 8.1 ZenFlow Core Concepts

**Four Pillars:**
1. Structured Workflows
2. SDD (Spec-Driven Development)
3. Multi-Agent Verification
4. Parallel Execution

### 8.2 24-Step Custom Workflow

**Phases:**
1. Planning
2. Design
3. Architecture
4. Implementation
5. Review
6. Testing
7. Validation
8. Optimization
9. Refactoring
10. Performance Optimization
11. Production Polish

### 8.3 Evidence-Driven Development

**Zen Rules:**
- All decisions must be based on empirical evidence
- No assumptions without verification
- Continuous validation at each phase
- Automated verification gates

---

## 9. Frontend Analysis Methodology Research

### 9.1 Code Relationship Database Approach

**Core Problem Addressed:**
"I do not know what connects to what, code paths are uncertain, and I need a method to ensure everything is mapped, tested, and maintainable."

**Solution:** Graph database approach treating code as queryable graph structure
- Nodes = files, functions, components
- Edges = imports, calls, relationships
- Enables powerful queries about codebase

### 9.2 Deliverables Created

| Deliverable | Lines | Purpose |
|-------------|-------|---------|
| IMPLEMENTATION_SUMMARY.md | 600 | Complete system overview |
| frontend_analysis_plan.md | 929 | 22-day roadmap, 8 phases |
| quick_start_guide.md | 311 | 30-minute insights |
| tools/dependency_mapper.py | 341 | Automated codebase analysis |
| tools/generate_graph_visualization.html | 536 | Interactive dependency graph |
| VISUAL_ROADMAP.md | 738 | Flowcharts and diagrams |

### 9.3 Key Innovations

- **Graph Database Approach:** Queryable code relationships
- **AI Agent Compatibility:** Structured JSON output, machine-readable documentation
- **Evidence-Based Methods:** Tools from 2026 research (FalkorDB, GitKraken Codemaps, Vitest, Playwright)

---

## 10. Sources Discovered in Space

### 10.1 Official Documentation
- LangGraph Documentation (langchain-ai.github.io)
- Langfuse Documentation (langfuse.com)
- ZenFlow Documentation (zenflow.ai)
- Claude Code Documentation (code.claude.ai)
- GitHub Copilot Documentation (github.com)
- OpenAI Codex Documentation (openai.com)

### 10.2 Research Papers
- FastFlowLM: Efficient LLM Inference (github.com)
- Speculative Decoding Research (AMD dev reports)
- AI-SDLC Maturity Model (eleks.com)

### 10.3 GitHub Repositories
- modelcontextprotocol/servers (MCP servers)
- anthropic/skills (61k ★)
- VoltAgent/awesome-agent-skills (4.7k ★)
- langchain-ai/langgraph (106k ★)
- crewAIInc/crewAI (30k+ ★)
- microsoft/autogen (43.1k+ ★)

### 10.4 Industry Sources
- prnewswire.com (Claude Code Agent Teams)
- xebia.com (Kilo Code/Roo Code analysis)
- intuitionlabs.ai (OpenAI Codex automation)
- linkedin.com (BDD/Gherkin acceptance criteria)
- thoughtworks.com (shift-left involvement)

---

## 11. Research Gaps Identified

### 11.1 Remaining Gaps After Prior Work Integration

1. **MCP Server Ecosystem Deep Dive**
   - Prior work identified MCP protocol but didn't exhaustively catalog all available servers
   - Gap: Complete inventory of production-ready MCP servers by category

2. **A2A Protocol Implementation Details**
   - Prior work mentioned A2A but didn't explore implementation patterns
   - Gap: Concrete A2A integration examples for agent-to-agent communication

3. **Local LLM Deployment Patterns**
   - Prior work mentioned local models but focused on cloud
   - Gap: Comprehensive local LLM deployment architecture for air-gapped environments

4. **Cross-Framework Agent Interoperability**
   - Prior work compared frameworks but didn't address interoperability
   - Gap: Patterns for agents from different frameworks to collaborate

5. **Production Hardening Patterns**
   - Prior work focused on architecture design
   - Gap: Operational runbooks, monitoring, alerting for production agent systems

6. **Security & Compliance for Agent Systems**
   - Prior work mentioned security briefly
   - Gap: Comprehensive security framework for autonomous agent systems

7. **Cost Optimization at Scale**
   - Prior work mentioned cost tracking
   - Gap: Advanced cost optimization strategies for enterprise-scale deployments

### 11.2 Cross-References to Research Taxonomy

| Taxonomy Category | Prior Work Coverage | Gap Status |
|-------------------|---------------------|------------|
| Agentic SDLC Patterns | Comprehensive (v1-v3) | Minor gaps in implementation details |
| MCP Servers | Protocol identified | Needs server catalog |
| Agent Orchestration | LangGraph recommended | Needs A2A implementation |
| Context Management | Spec artifact chain defined | Needs compression strategies |
| Testing Frameworks | Smoke testing architecture | Needs production hardening |
| CI/CD Patterns | GitHub-native approach | Needs operational runbooks |

---

## 12. Key Decisions & Conclusions from Prior Work

### 12.1 Workflow Engine Decision
**Decision:** Use LangGraph  
**Rationale:** 
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability
- Lowest latency and token usage
- Native parallel execution

### 12.2 Model Selection Decision
**Decision:** Kimi K2.5 as primary, Sonnet 4.6, GPT-5.3, Gemini 3 Pro/Flash  
**Rationale:**
- Cost optimization (Kimi is cheapest)
- Escalation path for complex tasks
- Multi-model consensus verification

### 12.3 Task Tracking Decision
**Decision:** GitHub-native (Issues, PRs, branches)  
**Rationale:**
- Permanent, auditable record
- Human-readable project state
- Native CI/CD integration
- Built-in collaboration

### 12.4 Testing Approach Decision
**Decision:** Behavioral testing + consensus-based evaluation + adversarial challenge  
**Rationale:**
- Empirical verification
- Reduces false positives
- Catches edge cases

### 12.5 Local vs Cloud Decision
**Decision:** Hybrid approach  
**Rationale:**
- Local for planning/design (cost, privacy)
- Cloud for implementation (speed)
- Local for final validation (accuracy)

---

## 13. Integration Recommendations

### 13.1 For New Research

1. **Build on LangGraph Foundation**
   - Prior work already selected LangGraph; new research should assume this baseline
   - Focus on graph node/edge design patterns

2. **Extend GitHub-Native Approach**
   - Use GitHub as single source of truth
   - Leverage GitHub MCP server for automation

3. **Incorporate ZenFlow Patterns**
   - Use 24-step workflow as reference
   - Apply evidence-driven development principles

4. **Leverage Tiny AI Models**
   - Qwen3-0.6B for selector intelligence
   - Deploy as shared service in K8s

### 13.2 For Implementation

1. **Start with Smoke Testing Framework**
   - Prior work includes comprehensive architecture
   - Use as proving ground for agentic patterns

2. **Implement Deviation Detection Early**
   - Critical for self-healing capabilities
   - Enables continuous improvement

3. **Use Kilo Code Cloud Agents**
   - For PR reviews and webhook automation
   - Integrates with GitHub-native workflow

---

## 14. Summary Statistics

| Metric | Value |
|--------|-------|
| Research Threads Analyzed | 8+ |
| Sources Cited | 160+ |
| Requirements Versions | 3 (v1 → v2 → v3) |
| Tools Evaluated | 8 |
| Workflow Frameworks Compared | 4 |
| AI Models Analyzed | 4+ |
| SDLC Phases Defined | 7 |
| GitHub Repositories Referenced | 15+ |

---

## 15. Document Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025 | Initial extraction and synthesis from Perplexity Space |

---

*This document represents a comprehensive integration of all substantive research found in the "Smoke Test Framework" Perplexity Space. It should be treated as a living document and updated as new research emerges.*

# Perplexity Space Research Integration: Smoke Test Framework

**Source:** https://www.perplexity.ai/spaces/smoke-test-framework-_L0_2o2dRyaDjDbhcmyOfw  
**Extraction Date:** 2025  
**Research Threads Analyzed:** 8+ substantive threads

---

## Executive Summary

This document synthesizes all substantive research from the "Smoke Test Framework" Perplexity Space, which contains extensive prior work on AI agentic SDLC frameworks, testing infrastructure, MCP servers, agent orchestration, and autonomous development workflows. The space represents 160+ research sources and multiple iterative refinement cycles on designing production-grade autonomous AI coding systems.

### Key Prior Work Identified:
1. **AI Agentic Autonomous SDLC Framework** - Comprehensive requirements across 3 major versions
2. **Smoke Testing Framework Architecture** - Playwright-based enterprise testing platform design
3. **Agent Skills & Workflows Research** - 200+ curated skills from major AI coding tools
4. **Tiny AI Models for Testing** - Docker-optimized models for selector adaptation
5. **ZenFlow Integration** - 24-step autonomous workflow for evidence-driven development
6. **Frontend Analysis Methodology** - Code relationship database approach

---

## 1. Agentic SDLC Patterns Research

### 1.1 Core Architecture Requirements (R-001 to R-014)

**Source Thread:** AI Agentic Autonomous SDLC Framework (Requirements v1-v3)

#### Key Findings:

**Autonomous Requirements Engineering (R-001)**
- Problem: AI agents fail when requirements are insufficient
- Solution: Multi-phase requirements engineering pipeline:
  - Intake → Intent Inference → Clarification Generation → Research Phase → Requirements Formalization → Adversarial Review → Stakeholder Validation Gate
- Format: BDD/Gherkin for unambiguous acceptance criteria
- Research Basis: Spec-driven development research shows under-investing in specs is the #1 failure mode

**Hierarchical Task Decomposition (R-002)**
- Following the Planning Pattern: Goal Analysis → Phase Decomposition → Task Decomposition → Dependency Mapping → Context Scoping → Task Specification
- Each atomic task receives its own concrete requirement document
- MINIMUM context principle to reduce token usage and hallucination risk

**Multi-Model Consensus Verification (R-003)**
- Primary model (Kimi K2.5) → Secondary verification (Sonnet 4.6) → Tertiary arbitration (GPT-5.3)
- Consensus scoring algorithm based on ICE and MUSE research
- Behavioral testing + adversarial challenge approach

**GitHub-Native Task Tracking Architecture**
- GitHub becomes single source of truth for all project state
- Framework Concept → GitHub Object mapping:
  - SDLC Project → GitHub Milestone
  - SDLC Phase → GitHub Label (phase:requirements, phase:design, etc.)
  - Atomic Task → GitHub Issue
  - Task Implementation → GitHub Branch + PR
  - Verification Results → PR Comment
  - Quality Gate Decision → GitHub Label (gate:pass, gate:fail)

### 1.2 Tool Capabilities Matrix

Research across 8 specified tools:

| Capability | Kilo Code | Roo Code | ZenFlow | GitHub Copilot | Claude Code | Codex | Continue | Cline |
|------------|-----------|----------|---------|----------------|-------------|-------|----------|-------|
| Custom modes/roles | YAML modes | Orchestrator + custom | Custom workflows | Custom agents | CLAUDE.md + skills | Skills system | ❌ | Custom modes |
| Multi-agent orchestration | Orchestrator mode | Cloud agents + orchestrator | Parallel agents | Coding agent + agents panel | Agent Teams (3-5) | Multi-threaded | ❌ | ❌ |
| Spec-driven development | Via custom workflows | Via modes | Core feature (SDD) | Via custom instructions | Via CLAUDE.md | Via skills | ❌ | Via rules |
| Multi-model verification | Manual mode switching | Provider-per-mode | Committee approach | ❌ | Team model selection | ❌ | ❌ | Model switching |
| Sandboxed execution | ❌ Local only | Cloud sandboxes | Isolated environments | GitHub Actions sandbox | Local execution | Native sandboxing | N/A | ❌ Local only |
| MCP support | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ Limited | ❌ | ✅ |

**Key Finding:** ZenFlow is the only tool with native spec-driven development and multi-agent verification ("committee approach") as core features.

### 1.3 Workflow Engine Evaluation

**Contenders Analyzed:**

| Framework | Core Paradigm | Primary Strength | Maturity |
|-----------|---------------|------------------|----------|
| LangGraph | Graph-based stateful workflows | Explicit DAG control, branching, debugging | Most mature (106k ★) |
| CrewAI | Role-based team coordination | YAML-driven, intuitive setup | Mid-maturity (30k+ ★) |
| AutoGen | Conversational multi-agent | Dialogue-driven, flexible topologies | Research-oriented (43.1k+ ★) |
| OpenAI Agents SDK | Lightweight primitives | Minimal abstractions, fast deployment | Newest |

**Head-to-Head Comparison (Key Criteria):**

| Criterion | LangGraph | CrewAI | AutoGen | OpenAI Agents SDK |
|-----------|-----------|--------|---------|-------------------|
| Workflow complexity | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| State management | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Parallelization | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Observability | ⭐⭐⭐⭐⭐ (LangSmith/Langfuse) | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Error handling | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Token efficiency | ⭐⭐⭐⭐⭐ (lowest latency) | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| Production readiness | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

**Recommendation:** LangGraph is superior for SDLC framework due to:
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability with state transition logs and visual graph traces
- Lowest latency and token usage in benchmarks
- Native parallel execution for independent subtasks
- Conditional edges for gating decisions and retry mechanisms

---

## 2. MCP Servers Research

### 2.1 Protocol Understanding

**MCP (Model Context Protocol)** by Anthropic:
- Standard for giving agents access to external tools, data sources, and APIs
- Official repository: `modelcontextprotocol/servers`
- Hundreds of community servers for GitHub, Git, Slack, databases, browsers

**A2A (Agent2Agent) Protocol** by Google (Linux Foundation):
- Enables agents built on different frameworks to discover each other
- Uses JSON-RPC 2.0 over HTTPS
- Complementary to MCP: A2A handles agent-to-agent, MCP handles agent-to-tool

### 2.2 GitHub MCP Server Integration

**Key Tools Available:**
- `create_issue` / `update_issue` — Task creation and status updates
- `create_pull_request` / `merge_pull_request` — Implementation tracking
- `create_branch` — Isolation for atomic tasks
- `add_issue_comment` — Posting verification results, cost data, adversarial findings
- `add_labels` — Phase tracking, gate status, priority
- `assign_copilot_to_issue` — Delegate additional work to Copilot agent
- `search_issues` / `list_pull_requests` — Orchestrator reads project state

### 2.3 Event-Driven Pipeline Architecture

```
Event Flow:
1. LangGraph orchestrator decomposes task → creates GitHub Issue
2. GitHub Issue creation triggers Kilo webhook
3. Kilo Cloud Agent clones repo, creates branch, implements task
4. Kilo Cloud Agent auto-commits and pushes → creates PR
5. PR creation triggers GitHub Agentic Workflow
6. Agentic Workflow runs verification (Code Reviews, tests)
7. Verification results posted as PR comments
8. LangGraph orchestrator reads PR state via GitHub MCP → decides gate
```

---

## 3. Agent Orchestration Research

### 3.1 Inter-Agent Communication Patterns

**Patterns Evaluated:**

| Pattern | How It Works | Best For | Limitations |
|---------|--------------|----------|-------------|
| Subagents | Parent spawns child, receives only results | Simple delegation | No ongoing collaboration |
| Skills | Reusable capabilities agents can invoke | Standardized tasks | Limited context sharing |
| Handoffs | Agent A passes control to Agent B | Sequential workflows | No parallel collaboration |
| Claude Code Agent Teams | Shared task lists, direct messaging, self-coordination | Complex collaboration | Requires Claude Code |
| Roo Code Orchestrator | Hierarchical meta-prompts, context-passing protocols | Structured workflows | Learning curve |

**Key Finding:** Claude Code Agent Teams represent the most advanced inter-agent communication model with shared task lists, direct messaging, and self-coordination capabilities.

### 3.2 Agent Skills Collections

**Top Repositories:**

| Repository | Stars | What It Does |
|------------|-------|--------------|
| anthropic/skills | 61k ★ | Official skills — document creation, design, MCP builder, webapp testing |
| VoltAgent/awesome-agent-skills | 4.7k ★ | Most comprehensive curated list — 200+ skills from major publishers |
| skillcreatorai/Ai-Agent-Skills | — | "Homebrew for AI Agent Skills" — universal installer |

**Standout Skill Categories:**
- **Context Engineering** (by muratcankoylan): context compression, degradation detection, multi-agent patterns, memory systems
- **Security** (by Trail of Bits): 20+ skills including audit context building, static analysis, property-based testing
- **Development** (by obra): subagent-driven development, systematic debugging, root-cause tracing

### 3.3 Multi-Agent Workflow Frameworks

| Framework | Stars | Best For | Approach |
|-----------|-------|----------|----------|
| LangGraph | 106k ★ | Complex workflows with branching logic | Graph-based DAG, explicit state management |
| CrewAI | 30k+ ★ | Fastest time-to-production | Role-based agents with task delegation |
| AutoGen | 43.1k+ ★ | Conversational multi-agent, human-in-loop | Agents chat and iterate naturally |
| Agno | 29k+ ★ | Full-stack multi-agent | Supports all major LLM providers |
| Letta | 15.9k+ ★ | Stateful long-running agents | Memory persistence across sessions |

**Token Efficiency Note:** LangGraph uses ~2,000 tokens per task vs. CrewAI's ~3,500 and AutoGen's ~8,000.

---

## 4. Context Management Research

### 4.1 Context Transfer Protocol

**Spec Artifact Chain Approach:**
- Each SDLC phase produces a spec artifact
- Artifacts are passed along the chain: Requirements Spec → Design Spec → Implementation Spec → Test Spec
- Each artifact includes: context scope, acceptance criteria, constraints, token budget

### 4.2 Context Scoping Principles

**For each atomic task, determine MINIMUM context required:**
- Files needed
- Specs relevant
- Constraints to enforce
- Token budget allocation

### 4.3 Token Optimization Strategies

- Task-specific context reduces bloat
- Avoid conversation history growth
- Use structured JSON output for machine-readable documentation
- Implement context compression for long-running sessions

---

## 5. Testing Frameworks Research

### 5.1 Smoke Testing Framework Architecture

**Core Capabilities (Target State):**

| Capability | Description |
|------------|-------------|
| Universal web interaction engine | Playwright-based, handles all element types, dynamic content, complex forms |
| Dynamic multi-stack orchestration | 3+ containerized test environments (aio, int, prod) with auto port allocation (9330-9399) |
| Intelligent resilience system | Auto retry, element detection strategies, timeout handling, latency tolerance |
| Parallel test execution | Across multiple sites and within same site simultaneously |
| Complete observability stack | WebSocket updates, Prometheus metrics, structured JSON logging, artifact management |
| Database state management | Bidirectional reset supporting PostgreSQL and Oracle |
| Configuration-driven architecture | YAML test definitions |
| Multiple execution interfaces | UI dashboard (Flask), REST API (Express), CLI, programmatic |
| Self-healing capabilities | Element locator fallbacks, intelligent wait strategies, adaptive selectors |

### 5.2 Deviation Detection System

**Deviation Types to Track:**
- Selector Deviations (configured vs. actual selector used)
- Timing Deviations (configured timeout vs. actual wait time)
- Validation Deviations (expected vs. actual error messages)
- Workflow Deviations (configured steps vs. actual execution)
- Data Deviations (expected vs. actual dropdown options)

**Deviation Dashboard Features:**
- Summary View: Total deviations by type, severity, status
- List View: Paginated table with test name, deviation type, timestamp, environment
- Detail View: Side-by-side comparison, visual diff, timeline, frequency chart
- Trend Analysis: Charts showing deviations over time, by module, most common types
- Review Workflow: Assign, comment, batch operations, export reports

### 5.3 Test-Driven Development of UI

**TDD Workflow for Dashboard:**
1. Write tests for desired UI features before implementation
2. Implement UI features to pass tests
3. Validate all UI components work correctly
4. Ensure accessibility compliance
5. Verify responsive design across viewports

---

## 6. CI/CD Patterns Research

### 6.1 GitHub-Native CI/CD Integration

**GitHub Agentic Workflows** (Technical Preview):
- Markdown-defined automations that run coding agents inside GitHub Actions
- Combined with Kilo Code's webhook triggers for event-driven pipeline

### 6.2 Jenkins Integration

**Smoke Test Pipeline:**
- Jenkins triggers deployment → Smoke tests start
- KEDA scales AI analyzer from 0 → 1 pod (5-10 seconds)
- 8 Playwright pods run parallel tests → Call AI service when selectors fail
- AI analyzer handles 20-30 requests/minute
- Tests complete → AI pod scales to 0 after cooldown

### 6.3 Kubernetes Deployment Strategy

**Shared AI Service Pattern (Recommended):**
```
┌─────────────────────────────────────────┐
│  8-Node Kubernetes Cluster              │
├─────────────────────────────────────────┤
│  Smoke Test Pods (6-8 parallel)         │
│  ├─ Playwright container (2GB RAM)      │
│  └─ Calls AI service via HTTP           │
├─────────────────────────────────────────┤
│  AI Analyzer Pod (1-2 replicas)         │
│  ├─ Qwen3-0.6B model (2-3GB RAM)       │
│  └─ Serves all smoke test pods          │
└─────────────────────────────────────────┘
```

**Resource Distribution (8 Nodes @ 4-8 cores, 16-32GB RAM each):**
- Total capacity: 64 CPU cores, 256GB RAM
- Smoke test allocation: 16GB RAM (Playwright) + 3-6GB RAM (AI) = ~20-25GB
- Total consumption: <10% of cluster resources

---

## 7. Tiny AI Models for Testing Research

### 7.1 Model Comparison

| Model | Parameters | Docker Size | Inference Speed | Best For |
|-------|------------|-------------|-----------------|----------|
| SmolLM2-360M | 360M | ~400MB | <100ms | Quick pattern matching, selector analysis |
| Qwen2-0.5B | 500M | ~500MB | ~150ms | Reasoning about failures, context understanding |
| Qwen3-0.6B | 600M | ~600MB | ~5ms/token | Complex decision-making, code understanding |
| Phi-3-mini | 3.8B | ~2.5GB | ~300ms | Complex decision-making, code understanding |

### 7.2 Qwen3-0.6B Deep Dive

**Key Advantages:**
- Released April 2025, trained on 36 trillion tokens across 119 languages
- 32K context window (can analyze entire test suites, DOM snapshots, git diffs)
- Benchmarks: 73% on MATH500, 79.2% on GSM8K, 30.5% on HumanEval
- Built-in agent capabilities for automation and workflow orchestration
- Dual reasoning modes: "thinking" and "non-thinking"

**Resource Requirements:**
- RAM: 8GB total system, ~3GB during inference
- Storage: 3GB for quantized model files
- CPU: 4-8 cores recommended, 2 cores minimum
- Inference speed: 10-30 tokens/second on CPU-only

**Kubernetes Configuration:**
```yaml
resources:
  requests:
    memory: "2Gi"
    cpu: "1000m"
  limits:
    memory: "3Gi"
    cpu: "2000m"
```

### 7.3 Selector Intelligence Layer

**Implementation Approach:**
1. Analyze selector failures and compare current vs. expected DOM structures
2. Evaluate error patterns against historical test data
3. Determine retry worthiness using context (commit messages, recent code changes, error frequency)
4. Provide confidence scores for "legitimate failure" vs. "trivial UI change"

**Decision Framework:**
- Legitimate test failure → FAIL
- Cosmetic change → RETRY
- Timing issue → RETRY
- Environmental → RETRY

---

## 8. ZenFlow Integration Research

### 8.1 ZenFlow Core Concepts

**Four Pillars:**
1. Structured Workflows
2. SDD (Spec-Driven Development)
3. Multi-Agent Verification
4. Parallel Execution

### 8.2 24-Step Custom Workflow

**Phases:**
1. Planning
2. Design
3. Architecture
4. Implementation
5. Review
6. Testing
7. Validation
8. Optimization
9. Refactoring
10. Performance Optimization
11. Production Polish

### 8.3 Evidence-Driven Development

**Zen Rules:**
- All decisions must be based on empirical evidence
- No assumptions without verification
- Continuous validation at each phase
- Automated verification gates

---

## 9. Frontend Analysis Methodology Research

### 9.1 Code Relationship Database Approach

**Core Problem Addressed:**
"I do not know what connects to what, code paths are uncertain, and I need a method to ensure everything is mapped, tested, and maintainable."

**Solution:** Graph database approach treating code as queryable graph structure
- Nodes = files, functions, components
- Edges = imports, calls, relationships
- Enables powerful queries about codebase

### 9.2 Deliverables Created

| Deliverable | Lines | Purpose |
|-------------|-------|---------|
| IMPLEMENTATION_SUMMARY.md | 600 | Complete system overview |
| frontend_analysis_plan.md | 929 | 22-day roadmap, 8 phases |
| quick_start_guide.md | 311 | 30-minute insights |
| tools/dependency_mapper.py | 341 | Automated codebase analysis |
| tools/generate_graph_visualization.html | 536 | Interactive dependency graph |
| VISUAL_ROADMAP.md | 738 | Flowcharts and diagrams |

### 9.3 Key Innovations

- **Graph Database Approach:** Queryable code relationships
- **AI Agent Compatibility:** Structured JSON output, machine-readable documentation
- **Evidence-Based Methods:** Tools from 2026 research (FalkorDB, GitKraken Codemaps, Vitest, Playwright)

---

## 10. Sources Discovered in Space

### 10.1 Official Documentation
- LangGraph Documentation (langchain-ai.github.io)
- Langfuse Documentation (langfuse.com)
- ZenFlow Documentation (zenflow.ai)
- Claude Code Documentation (code.claude.ai)
- GitHub Copilot Documentation (github.com)
- OpenAI Codex Documentation (openai.com)

### 10.2 Research Papers
- FastFlowLM: Efficient LLM Inference (github.com)
- Speculative Decoding Research (AMD dev reports)
- AI-SDLC Maturity Model (eleks.com)

### 10.3 GitHub Repositories
- modelcontextprotocol/servers (MCP servers)
- anthropic/skills (61k ★)
- VoltAgent/awesome-agent-skills (4.7k ★)
- langchain-ai/langgraph (106k ★)
- crewAIInc/crewAI (30k+ ★)
- microsoft/autogen (43.1k+ ★)

### 10.4 Industry Sources
- prnewswire.com (Claude Code Agent Teams)
- xebia.com (Kilo Code/Roo Code analysis)
- intuitionlabs.ai (OpenAI Codex automation)
- linkedin.com (BDD/Gherkin acceptance criteria)
- thoughtworks.com (shift-left involvement)

---

## 11. Research Gaps Identified

### 11.1 Remaining Gaps After Prior Work Integration

1. **MCP Server Ecosystem Deep Dive**
   - Prior work identified MCP protocol but didn't exhaustively catalog all available servers
   - Gap: Complete inventory of production-ready MCP servers by category

2. **A2A Protocol Implementation Details**
   - Prior work mentioned A2A but didn't explore implementation patterns
   - Gap: Concrete A2A integration examples for agent-to-agent communication

3. **Local LLM Deployment Patterns**
   - Prior work mentioned local models but focused on cloud
   - Gap: Comprehensive local LLM deployment architecture for air-gapped environments

4. **Cross-Framework Agent Interoperability**
   - Prior work compared frameworks but didn't address interoperability
   - Gap: Patterns for agents from different frameworks to collaborate

5. **Production Hardening Patterns**
   - Prior work focused on architecture design
   - Gap: Operational runbooks, monitoring, alerting for production agent systems

6. **Security & Compliance for Agent Systems**
   - Prior work mentioned security briefly
   - Gap: Comprehensive security framework for autonomous agent systems

7. **Cost Optimization at Scale**
   - Prior work mentioned cost tracking
   - Gap: Advanced cost optimization strategies for enterprise-scale deployments

### 11.2 Cross-References to Research Taxonomy

| Taxonomy Category | Prior Work Coverage | Gap Status |
|-------------------|---------------------|------------|
| Agentic SDLC Patterns | Comprehensive (v1-v3) | Minor gaps in implementation details |
| MCP Servers | Protocol identified | Needs server catalog |
| Agent Orchestration | LangGraph recommended | Needs A2A implementation |
| Context Management | Spec artifact chain defined | Needs compression strategies |
| Testing Frameworks | Smoke testing architecture | Needs production hardening |
| CI/CD Patterns | GitHub-native approach | Needs operational runbooks |

---

## 12. Key Decisions & Conclusions from Prior Work

### 12.1 Workflow Engine Decision
**Decision:** Use LangGraph  
**Rationale:** 
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability
- Lowest latency and token usage
- Native parallel execution

### 12.2 Model Selection Decision
**Decision:** Kimi K2.5 as primary, Sonnet 4.6, GPT-5.3, Gemini 3 Pro/Flash  
**Rationale:**
- Cost optimization (Kimi is cheapest)
- Escalation path for complex tasks
- Multi-model consensus verification

### 12.3 Task Tracking Decision
**Decision:** GitHub-native (Issues, PRs, branches)  
**Rationale:**
- Permanent, auditable record
- Human-readable project state
- Native CI/CD integration
- Built-in collaboration

### 12.4 Testing Approach Decision
**Decision:** Behavioral testing + consensus-based evaluation + adversarial challenge  
**Rationale:**
- Empirical verification
- Reduces false positives
- Catches edge cases

### 12.5 Local vs Cloud Decision
**Decision:** Hybrid approach  
**Rationale:**
- Local for planning/design (cost, privacy)
- Cloud for implementation (speed)
- Local for final validation (accuracy)

---

## 13. Integration Recommendations

### 13.1 For New Research

1. **Build on LangGraph Foundation**
   - Prior work already selected LangGraph; new research should assume this baseline
   - Focus on graph node/edge design patterns

2. **Extend GitHub-Native Approach**
   - Use GitHub as single source of truth
   - Leverage GitHub MCP server for automation

3. **Incorporate ZenFlow Patterns**
   - Use 24-step workflow as reference
   - Apply evidence-driven development principles

4. **Leverage Tiny AI Models**
   - Qwen3-0.6B for selector intelligence
   - Deploy as shared service in K8s

### 13.2 For Implementation

1. **Start with Smoke Testing Framework**
   - Prior work includes comprehensive architecture
   - Use as proving ground for agentic patterns

2. **Implement Deviation Detection Early**
   - Critical for self-healing capabilities
   - Enables continuous improvement

3. **Use Kilo Code Cloud Agents**
   - For PR reviews and webhook automation
   - Integrates with GitHub-native workflow

---

## 14. Summary Statistics

| Metric | Value |
|--------|-------|
| Research Threads Analyzed | 8+ |
| Sources Cited | 160+ |
| Requirements Versions | 3 (v1 → v2 → v3) |
| Tools Evaluated | 8 |
| Workflow Frameworks Compared | 4 |
| AI Models Analyzed | 4+ |
| SDLC Phases Defined | 7 |
| GitHub Repositories Referenced | 15+ |

---

## 15. Document Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025 | Initial extraction and synthesis from Perplexity Space |

---

*This document represents a comprehensive integration of all substantive research found in the "Smoke Test Framework" Perplexity Space. It should be treated as a living document and updated as new research emerges.*

# Perplexity Space Research Integration: Smoke Test Framework

**Source:** https://www.perplexity.ai/spaces/smoke-test-framework-_L0_2o2dRyaDjDbhcmyOfw  
**Extraction Date:** 2025  
**Research Threads Analyzed:** 8+ substantive threads

---

## Executive Summary

This document synthesizes all substantive research from the "Smoke Test Framework" Perplexity Space, which contains extensive prior work on AI agentic SDLC frameworks, testing infrastructure, MCP servers, agent orchestration, and autonomous development workflows. The space represents 160+ research sources and multiple iterative refinement cycles on designing production-grade autonomous AI coding systems.

### Key Prior Work Identified:
1. **AI Agentic Autonomous SDLC Framework** - Comprehensive requirements across 3 major versions
2. **Smoke Testing Framework Architecture** - Playwright-based enterprise testing platform design
3. **Agent Skills & Workflows Research** - 200+ curated skills from major AI coding tools
4. **Tiny AI Models for Testing** - Docker-optimized models for selector adaptation
5. **ZenFlow Integration** - 24-step autonomous workflow for evidence-driven development
6. **Frontend Analysis Methodology** - Code relationship database approach

---

## 1. Agentic SDLC Patterns Research

### 1.1 Core Architecture Requirements (R-001 to R-014)

**Source Thread:** AI Agentic Autonomous SDLC Framework (Requirements v1-v3)

#### Key Findings:

**Autonomous Requirements Engineering (R-001)**
- Problem: AI agents fail when requirements are insufficient
- Solution: Multi-phase requirements engineering pipeline:
  - Intake → Intent Inference → Clarification Generation → Research Phase → Requirements Formalization → Adversarial Review → Stakeholder Validation Gate
- Format: BDD/Gherkin for unambiguous acceptance criteria
- Research Basis: Spec-driven development research shows under-investing in specs is the #1 failure mode

**Hierarchical Task Decomposition (R-002)**
- Following the Planning Pattern: Goal Analysis → Phase Decomposition → Task Decomposition → Dependency Mapping → Context Scoping → Task Specification
- Each atomic task receives its own concrete requirement document
- MINIMUM context principle to reduce token usage and hallucination risk

**Multi-Model Consensus Verification (R-003)**
- Primary model (Kimi K2.5) → Secondary verification (Sonnet 4.6) → Tertiary arbitration (GPT-5.3)
- Consensus scoring algorithm based on ICE and MUSE research
- Behavioral testing + adversarial challenge approach

**GitHub-Native Task Tracking Architecture**
- GitHub becomes single source of truth for all project state
- Framework Concept → GitHub Object mapping:
  - SDLC Project → GitHub Milestone
  - SDLC Phase → GitHub Label (phase:requirements, phase:design, etc.)
  - Atomic Task → GitHub Issue
  - Task Implementation → GitHub Branch + PR
  - Verification Results → PR Comment
  - Quality Gate Decision → GitHub Label (gate:pass, gate:fail)

### 1.2 Tool Capabilities Matrix

Research across 8 specified tools:

| Capability | Kilo Code | Roo Code | ZenFlow | GitHub Copilot | Claude Code | Codex | Continue | Cline |
|------------|-----------|----------|---------|----------------|-------------|-------|----------|-------|
| Custom modes/roles | YAML modes | Orchestrator + custom | Custom workflows | Custom agents | CLAUDE.md + skills | Skills system | ❌ | Custom modes |
| Multi-agent orchestration | Orchestrator mode | Cloud agents + orchestrator | Parallel agents | Coding agent + agents panel | Agent Teams (3-5) | Multi-threaded | ❌ | ❌ |
| Spec-driven development | Via custom workflows | Via modes | Core feature (SDD) | Via custom instructions | Via CLAUDE.md | Via skills | ❌ | Via rules |
| Multi-model verification | Manual mode switching | Provider-per-mode | Committee approach | ❌ | Team model selection | ❌ | ❌ | Model switching |
| Sandboxed execution | ❌ Local only | Cloud sandboxes | Isolated environments | GitHub Actions sandbox | Local execution | Native sandboxing | N/A | ❌ Local only |
| MCP support | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ Limited | ❌ | ✅ |

**Key Finding:** ZenFlow is the only tool with native spec-driven development and multi-agent verification ("committee approach") as core features.

### 1.3 Workflow Engine Evaluation

**Contenders Analyzed:**

| Framework | Core Paradigm | Primary Strength | Maturity |
|-----------|---------------|------------------|----------|
| LangGraph | Graph-based stateful workflows | Explicit DAG control, branching, debugging | Most mature (106k ★) |
| CrewAI | Role-based team coordination | YAML-driven, intuitive setup | Mid-maturity (30k+ ★) |
| AutoGen | Conversational multi-agent | Dialogue-driven, flexible topologies | Research-oriented (43.1k+ ★) |
| OpenAI Agents SDK | Lightweight primitives | Minimal abstractions, fast deployment | Newest |

**Head-to-Head Comparison (Key Criteria):**

| Criterion | LangGraph | CrewAI | AutoGen | OpenAI Agents SDK |
|-----------|-----------|--------|---------|-------------------|
| Workflow complexity | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| State management | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Parallelization | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Observability | ⭐⭐⭐⭐⭐ (LangSmith/Langfuse) | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Error handling | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Token efficiency | ⭐⭐⭐⭐⭐ (lowest latency) | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| Production readiness | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

**Recommendation:** LangGraph is superior for SDLC framework due to:
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability with state transition logs and visual graph traces
- Lowest latency and token usage in benchmarks
- Native parallel execution for independent subtasks
- Conditional edges for gating decisions and retry mechanisms

---

## 2. MCP Servers Research

### 2.1 Protocol Understanding

**MCP (Model Context Protocol)** by Anthropic:
- Standard for giving agents access to external tools, data sources, and APIs
- Official repository: `modelcontextprotocol/servers`
- Hundreds of community servers for GitHub, Git, Slack, databases, browsers

**A2A (Agent2Agent) Protocol** by Google (Linux Foundation):
- Enables agents built on different frameworks to discover each other
- Uses JSON-RPC 2.0 over HTTPS
- Complementary to MCP: A2A handles agent-to-agent, MCP handles agent-to-tool

### 2.2 GitHub MCP Server Integration

**Key Tools Available:**
- `create_issue` / `update_issue` — Task creation and status updates
- `create_pull_request` / `merge_pull_request` — Implementation tracking
- `create_branch` — Isolation for atomic tasks
- `add_issue_comment` — Posting verification results, cost data, adversarial findings
- `add_labels` — Phase tracking, gate status, priority
- `assign_copilot_to_issue` — Delegate additional work to Copilot agent
- `search_issues` / `list_pull_requests` — Orchestrator reads project state

### 2.3 Event-Driven Pipeline Architecture

```
Event Flow:
1. LangGraph orchestrator decomposes task → creates GitHub Issue
2. GitHub Issue creation triggers Kilo webhook
3. Kilo Cloud Agent clones repo, creates branch, implements task
4. Kilo Cloud Agent auto-commits and pushes → creates PR
5. PR creation triggers GitHub Agentic Workflow
6. Agentic Workflow runs verification (Code Reviews, tests)
7. Verification results posted as PR comments
8. LangGraph orchestrator reads PR state via GitHub MCP → decides gate
```

---

## 3. Agent Orchestration Research

### 3.1 Inter-Agent Communication Patterns

**Patterns Evaluated:**

| Pattern | How It Works | Best For | Limitations |
|---------|--------------|----------|-------------|
| Subagents | Parent spawns child, receives only results | Simple delegation | No ongoing collaboration |
| Skills | Reusable capabilities agents can invoke | Standardized tasks | Limited context sharing |
| Handoffs | Agent A passes control to Agent B | Sequential workflows | No parallel collaboration |
| Claude Code Agent Teams | Shared task lists, direct messaging, self-coordination | Complex collaboration | Requires Claude Code |
| Roo Code Orchestrator | Hierarchical meta-prompts, context-passing protocols | Structured workflows | Learning curve |

**Key Finding:** Claude Code Agent Teams represent the most advanced inter-agent communication model with shared task lists, direct messaging, and self-coordination capabilities.

### 3.2 Agent Skills Collections

**Top Repositories:**

| Repository | Stars | What It Does |
|------------|-------|--------------|
| anthropic/skills | 61k ★ | Official skills — document creation, design, MCP builder, webapp testing |
| VoltAgent/awesome-agent-skills | 4.7k ★ | Most comprehensive curated list — 200+ skills from major publishers |
| skillcreatorai/Ai-Agent-Skills | — | "Homebrew for AI Agent Skills" — universal installer |

**Standout Skill Categories:**
- **Context Engineering** (by muratcankoylan): context compression, degradation detection, multi-agent patterns, memory systems
- **Security** (by Trail of Bits): 20+ skills including audit context building, static analysis, property-based testing
- **Development** (by obra): subagent-driven development, systematic debugging, root-cause tracing

### 3.3 Multi-Agent Workflow Frameworks

| Framework | Stars | Best For | Approach |
|-----------|-------|----------|----------|
| LangGraph | 106k ★ | Complex workflows with branching logic | Graph-based DAG, explicit state management |
| CrewAI | 30k+ ★ | Fastest time-to-production | Role-based agents with task delegation |
| AutoGen | 43.1k+ ★ | Conversational multi-agent, human-in-loop | Agents chat and iterate naturally |
| Agno | 29k+ ★ | Full-stack multi-agent | Supports all major LLM providers |
| Letta | 15.9k+ ★ | Stateful long-running agents | Memory persistence across sessions |

**Token Efficiency Note:** LangGraph uses ~2,000 tokens per task vs. CrewAI's ~3,500 and AutoGen's ~8,000.

---

## 4. Context Management Research

### 4.1 Context Transfer Protocol

**Spec Artifact Chain Approach:**
- Each SDLC phase produces a spec artifact
- Artifacts are passed along the chain: Requirements Spec → Design Spec → Implementation Spec → Test Spec
- Each artifact includes: context scope, acceptance criteria, constraints, token budget

### 4.2 Context Scoping Principles

**For each atomic task, determine MINIMUM context required:**
- Files needed
- Specs relevant
- Constraints to enforce
- Token budget allocation

### 4.3 Token Optimization Strategies

- Task-specific context reduces bloat
- Avoid conversation history growth
- Use structured JSON output for machine-readable documentation
- Implement context compression for long-running sessions

---

## 5. Testing Frameworks Research

### 5.1 Smoke Testing Framework Architecture

**Core Capabilities (Target State):**

| Capability | Description |
|------------|-------------|
| Universal web interaction engine | Playwright-based, handles all element types, dynamic content, complex forms |
| Dynamic multi-stack orchestration | 3+ containerized test environments (aio, int, prod) with auto port allocation (9330-9399) |
| Intelligent resilience system | Auto retry, element detection strategies, timeout handling, latency tolerance |
| Parallel test execution | Across multiple sites and within same site simultaneously |
| Complete observability stack | WebSocket updates, Prometheus metrics, structured JSON logging, artifact management |
| Database state management | Bidirectional reset supporting PostgreSQL and Oracle |
| Configuration-driven architecture | YAML test definitions |
| Multiple execution interfaces | UI dashboard (Flask), REST API (Express), CLI, programmatic |
| Self-healing capabilities | Element locator fallbacks, intelligent wait strategies, adaptive selectors |

### 5.2 Deviation Detection System

**Deviation Types to Track:**
- Selector Deviations (configured vs. actual selector used)
- Timing Deviations (configured timeout vs. actual wait time)
- Validation Deviations (expected vs. actual error messages)
- Workflow Deviations (configured steps vs. actual execution)
- Data Deviations (expected vs. actual dropdown options)

**Deviation Dashboard Features:**
- Summary View: Total deviations by type, severity, status
- List View: Paginated table with test name, deviation type, timestamp, environment
- Detail View: Side-by-side comparison, visual diff, timeline, frequency chart
- Trend Analysis: Charts showing deviations over time, by module, most common types
- Review Workflow: Assign, comment, batch operations, export reports

### 5.3 Test-Driven Development of UI

**TDD Workflow for Dashboard:**
1. Write tests for desired UI features before implementation
2. Implement UI features to pass tests
3. Validate all UI components work correctly
4. Ensure accessibility compliance
5. Verify responsive design across viewports

---

## 6. CI/CD Patterns Research

### 6.1 GitHub-Native CI/CD Integration

**GitHub Agentic Workflows** (Technical Preview):
- Markdown-defined automations that run coding agents inside GitHub Actions
- Combined with Kilo Code's webhook triggers for event-driven pipeline

### 6.2 Jenkins Integration

**Smoke Test Pipeline:**
- Jenkins triggers deployment → Smoke tests start
- KEDA scales AI analyzer from 0 → 1 pod (5-10 seconds)
- 8 Playwright pods run parallel tests → Call AI service when selectors fail
- AI analyzer handles 20-30 requests/minute
- Tests complete → AI pod scales to 0 after cooldown

### 6.3 Kubernetes Deployment Strategy

**Shared AI Service Pattern (Recommended):**
```
┌─────────────────────────────────────────┐
│  8-Node Kubernetes Cluster              │
├─────────────────────────────────────────┤
│  Smoke Test Pods (6-8 parallel)         │
│  ├─ Playwright container (2GB RAM)      │
│  └─ Calls AI service via HTTP           │
├─────────────────────────────────────────┤
│  AI Analyzer Pod (1-2 replicas)         │
│  ├─ Qwen3-0.6B model (2-3GB RAM)       │
│  └─ Serves all smoke test pods          │
└─────────────────────────────────────────┘
```

**Resource Distribution (8 Nodes @ 4-8 cores, 16-32GB RAM each):**
- Total capacity: 64 CPU cores, 256GB RAM
- Smoke test allocation: 16GB RAM (Playwright) + 3-6GB RAM (AI) = ~20-25GB
- Total consumption: <10% of cluster resources

---

## 7. Tiny AI Models for Testing Research

### 7.1 Model Comparison

| Model | Parameters | Docker Size | Inference Speed | Best For |
|-------|------------|-------------|-----------------|----------|
| SmolLM2-360M | 360M | ~400MB | <100ms | Quick pattern matching, selector analysis |
| Qwen2-0.5B | 500M | ~500MB | ~150ms | Reasoning about failures, context understanding |
| Qwen3-0.6B | 600M | ~600MB | ~5ms/token | Complex decision-making, code understanding |
| Phi-3-mini | 3.8B | ~2.5GB | ~300ms | Complex decision-making, code understanding |

### 7.2 Qwen3-0.6B Deep Dive

**Key Advantages:**
- Released April 2025, trained on 36 trillion tokens across 119 languages
- 32K context window (can analyze entire test suites, DOM snapshots, git diffs)
- Benchmarks: 73% on MATH500, 79.2% on GSM8K, 30.5% on HumanEval
- Built-in agent capabilities for automation and workflow orchestration
- Dual reasoning modes: "thinking" and "non-thinking"

**Resource Requirements:**
- RAM: 8GB total system, ~3GB during inference
- Storage: 3GB for quantized model files
- CPU: 4-8 cores recommended, 2 cores minimum
- Inference speed: 10-30 tokens/second on CPU-only

**Kubernetes Configuration:**
```yaml
resources:
  requests:
    memory: "2Gi"
    cpu: "1000m"
  limits:
    memory: "3Gi"
    cpu: "2000m"
```

### 7.3 Selector Intelligence Layer

**Implementation Approach:**
1. Analyze selector failures and compare current vs. expected DOM structures
2. Evaluate error patterns against historical test data
3. Determine retry worthiness using context (commit messages, recent code changes, error frequency)
4. Provide confidence scores for "legitimate failure" vs. "trivial UI change"

**Decision Framework:**
- Legitimate test failure → FAIL
- Cosmetic change → RETRY
- Timing issue → RETRY
- Environmental → RETRY

---

## 8. ZenFlow Integration Research

### 8.1 ZenFlow Core Concepts

**Four Pillars:**
1. Structured Workflows
2. SDD (Spec-Driven Development)
3. Multi-Agent Verification
4. Parallel Execution

### 8.2 24-Step Custom Workflow

**Phases:**
1. Planning
2. Design
3. Architecture
4. Implementation
5. Review
6. Testing
7. Validation
8. Optimization
9. Refactoring
10. Performance Optimization
11. Production Polish

### 8.3 Evidence-Driven Development

**Zen Rules:**
- All decisions must be based on empirical evidence
- No assumptions without verification
- Continuous validation at each phase
- Automated verification gates

---

## 9. Frontend Analysis Methodology Research

### 9.1 Code Relationship Database Approach

**Core Problem Addressed:**
"I do not know what connects to what, code paths are uncertain, and I need a method to ensure everything is mapped, tested, and maintainable."

**Solution:** Graph database approach treating code as queryable graph structure
- Nodes = files, functions, components
- Edges = imports, calls, relationships
- Enables powerful queries about codebase

### 9.2 Deliverables Created

| Deliverable | Lines | Purpose |
|-------------|-------|---------|
| IMPLEMENTATION_SUMMARY.md | 600 | Complete system overview |
| frontend_analysis_plan.md | 929 | 22-day roadmap, 8 phases |
| quick_start_guide.md | 311 | 30-minute insights |
| tools/dependency_mapper.py | 341 | Automated codebase analysis |
| tools/generate_graph_visualization.html | 536 | Interactive dependency graph |
| VISUAL_ROADMAP.md | 738 | Flowcharts and diagrams |

### 9.3 Key Innovations

- **Graph Database Approach:** Queryable code relationships
- **AI Agent Compatibility:** Structured JSON output, machine-readable documentation
- **Evidence-Based Methods:** Tools from 2026 research (FalkorDB, GitKraken Codemaps, Vitest, Playwright)

---

## 10. Sources Discovered in Space

### 10.1 Official Documentation
- LangGraph Documentation (langchain-ai.github.io)
- Langfuse Documentation (langfuse.com)
- ZenFlow Documentation (zenflow.ai)
- Claude Code Documentation (code.claude.ai)
- GitHub Copilot Documentation (github.com)
- OpenAI Codex Documentation (openai.com)

### 10.2 Research Papers
- FastFlowLM: Efficient LLM Inference (github.com)
- Speculative Decoding Research (AMD dev reports)
- AI-SDLC Maturity Model (eleks.com)

### 10.3 GitHub Repositories
- modelcontextprotocol/servers (MCP servers)
- anthropic/skills (61k ★)
- VoltAgent/awesome-agent-skills (4.7k ★)
- langchain-ai/langgraph (106k ★)
- crewAIInc/crewAI (30k+ ★)
- microsoft/autogen (43.1k+ ★)

### 10.4 Industry Sources
- prnewswire.com (Claude Code Agent Teams)
- xebia.com (Kilo Code/Roo Code analysis)
- intuitionlabs.ai (OpenAI Codex automation)
- linkedin.com (BDD/Gherkin acceptance criteria)
- thoughtworks.com (shift-left involvement)

---

## 11. Research Gaps Identified

### 11.1 Remaining Gaps After Prior Work Integration

1. **MCP Server Ecosystem Deep Dive**
   - Prior work identified MCP protocol but didn't exhaustively catalog all available servers
   - Gap: Complete inventory of production-ready MCP servers by category

2. **A2A Protocol Implementation Details**
   - Prior work mentioned A2A but didn't explore implementation patterns
   - Gap: Concrete A2A integration examples for agent-to-agent communication

3. **Local LLM Deployment Patterns**
   - Prior work mentioned local models but focused on cloud
   - Gap: Comprehensive local LLM deployment architecture for air-gapped environments

4. **Cross-Framework Agent Interoperability**
   - Prior work compared frameworks but didn't address interoperability
   - Gap: Patterns for agents from different frameworks to collaborate

5. **Production Hardening Patterns**
   - Prior work focused on architecture design
   - Gap: Operational runbooks, monitoring, alerting for production agent systems

6. **Security & Compliance for Agent Systems**
   - Prior work mentioned security briefly
   - Gap: Comprehensive security framework for autonomous agent systems

7. **Cost Optimization at Scale**
   - Prior work mentioned cost tracking
   - Gap: Advanced cost optimization strategies for enterprise-scale deployments

### 11.2 Cross-References to Research Taxonomy

| Taxonomy Category | Prior Work Coverage | Gap Status |
|-------------------|---------------------|------------|
| Agentic SDLC Patterns | Comprehensive (v1-v3) | Minor gaps in implementation details |
| MCP Servers | Protocol identified | Needs server catalog |
| Agent Orchestration | LangGraph recommended | Needs A2A implementation |
| Context Management | Spec artifact chain defined | Needs compression strategies |
| Testing Frameworks | Smoke testing architecture | Needs production hardening |
| CI/CD Patterns | GitHub-native approach | Needs operational runbooks |

---

## 12. Key Decisions & Conclusions from Prior Work

### 12.1 Workflow Engine Decision
**Decision:** Use LangGraph  
**Rationale:** 
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability
- Lowest latency and token usage
- Native parallel execution

### 12.2 Model Selection Decision
**Decision:** Kimi K2.5 as primary, Sonnet 4.6, GPT-5.3, Gemini 3 Pro/Flash  
**Rationale:**
- Cost optimization (Kimi is cheapest)
- Escalation path for complex tasks
- Multi-model consensus verification

### 12.3 Task Tracking Decision
**Decision:** GitHub-native (Issues, PRs, branches)  
**Rationale:**
- Permanent, auditable record
- Human-readable project state
- Native CI/CD integration
- Built-in collaboration

### 12.4 Testing Approach Decision
**Decision:** Behavioral testing + consensus-based evaluation + adversarial challenge  
**Rationale:**
- Empirical verification
- Reduces false positives
- Catches edge cases

### 12.5 Local vs Cloud Decision
**Decision:** Hybrid approach  
**Rationale:**
- Local for planning/design (cost, privacy)
- Cloud for implementation (speed)
- Local for final validation (accuracy)

---

## 13. Integration Recommendations

### 13.1 For New Research

1. **Build on LangGraph Foundation**
   - Prior work already selected LangGraph; new research should assume this baseline
   - Focus on graph node/edge design patterns

2. **Extend GitHub-Native Approach**
   - Use GitHub as single source of truth
   - Leverage GitHub MCP server for automation

3. **Incorporate ZenFlow Patterns**
   - Use 24-step workflow as reference
   - Apply evidence-driven development principles

4. **Leverage Tiny AI Models**
   - Qwen3-0.6B for selector intelligence
   - Deploy as shared service in K8s

### 13.2 For Implementation

1. **Start with Smoke Testing Framework**
   - Prior work includes comprehensive architecture
   - Use as proving ground for agentic patterns

2. **Implement Deviation Detection Early**
   - Critical for self-healing capabilities
   - Enables continuous improvement

3. **Use Kilo Code Cloud Agents**
   - For PR reviews and webhook automation
   - Integrates with GitHub-native workflow

---

## 14. Summary Statistics

| Metric | Value |
|--------|-------|
| Research Threads Analyzed | 8+ |
| Sources Cited | 160+ |
| Requirements Versions | 3 (v1 → v2 → v3) |
| Tools Evaluated | 8 |
| Workflow Frameworks Compared | 4 |
| AI Models Analyzed | 4+ |
| SDLC Phases Defined | 7 |
| GitHub Repositories Referenced | 15+ |

---

## 15. Document Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025 | Initial extraction and synthesis from Perplexity Space |

---

*This document represents a comprehensive integration of all substantive research found in the "Smoke Test Framework" Perplexity Space. It should be treated as a living document and updated as new research emerges.*

# Perplexity Space Research Integration: Smoke Test Framework

**Source:** https://www.perplexity.ai/spaces/smoke-test-framework-_L0_2o2dRyaDjDbhcmyOfw  
**Extraction Date:** 2025  
**Research Threads Analyzed:** 8+ substantive threads

---

## Executive Summary

This document synthesizes all substantive research from the "Smoke Test Framework" Perplexity Space, which contains extensive prior work on AI agentic SDLC frameworks, testing infrastructure, MCP servers, agent orchestration, and autonomous development workflows. The space represents 160+ research sources and multiple iterative refinement cycles on designing production-grade autonomous AI coding systems.

### Key Prior Work Identified:
1. **AI Agentic Autonomous SDLC Framework** - Comprehensive requirements across 3 major versions
2. **Smoke Testing Framework Architecture** - Playwright-based enterprise testing platform design
3. **Agent Skills & Workflows Research** - 200+ curated skills from major AI coding tools
4. **Tiny AI Models for Testing** - Docker-optimized models for selector adaptation
5. **ZenFlow Integration** - 24-step autonomous workflow for evidence-driven development
6. **Frontend Analysis Methodology** - Code relationship database approach

---

## 1. Agentic SDLC Patterns Research

### 1.1 Core Architecture Requirements (R-001 to R-014)

**Source Thread:** AI Agentic Autonomous SDLC Framework (Requirements v1-v3)

#### Key Findings:

**Autonomous Requirements Engineering (R-001)**
- Problem: AI agents fail when requirements are insufficient
- Solution: Multi-phase requirements engineering pipeline:
  - Intake → Intent Inference → Clarification Generation → Research Phase → Requirements Formalization → Adversarial Review → Stakeholder Validation Gate
- Format: BDD/Gherkin for unambiguous acceptance criteria
- Research Basis: Spec-driven development research shows under-investing in specs is the #1 failure mode

**Hierarchical Task Decomposition (R-002)**
- Following the Planning Pattern: Goal Analysis → Phase Decomposition → Task Decomposition → Dependency Mapping → Context Scoping → Task Specification
- Each atomic task receives its own concrete requirement document
- MINIMUM context principle to reduce token usage and hallucination risk

**Multi-Model Consensus Verification (R-003)**
- Primary model (Kimi K2.5) → Secondary verification (Sonnet 4.6) → Tertiary arbitration (GPT-5.3)
- Consensus scoring algorithm based on ICE and MUSE research
- Behavioral testing + adversarial challenge approach

**GitHub-Native Task Tracking Architecture**
- GitHub becomes single source of truth for all project state
- Framework Concept → GitHub Object mapping:
  - SDLC Project → GitHub Milestone
  - SDLC Phase → GitHub Label (phase:requirements, phase:design, etc.)
  - Atomic Task → GitHub Issue
  - Task Implementation → GitHub Branch + PR
  - Verification Results → PR Comment
  - Quality Gate Decision → GitHub Label (gate:pass, gate:fail)

### 1.2 Tool Capabilities Matrix

Research across 8 specified tools:

| Capability | Kilo Code | Roo Code | ZenFlow | GitHub Copilot | Claude Code | Codex | Continue | Cline |
|------------|-----------|----------|---------|----------------|-------------|-------|----------|-------|
| Custom modes/roles | YAML modes | Orchestrator + custom | Custom workflows | Custom agents | CLAUDE.md + skills | Skills system | ❌ | Custom modes |
| Multi-agent orchestration | Orchestrator mode | Cloud agents + orchestrator | Parallel agents | Coding agent + agents panel | Agent Teams (3-5) | Multi-threaded | ❌ | ❌ |
| Spec-driven development | Via custom workflows | Via modes | Core feature (SDD) | Via custom instructions | Via CLAUDE.md | Via skills | ❌ | Via rules |
| Multi-model verification | Manual mode switching | Provider-per-mode | Committee approach | ❌ | Team model selection | ❌ | ❌ | Model switching |
| Sandboxed execution | ❌ Local only | Cloud sandboxes | Isolated environments | GitHub Actions sandbox | Local execution | Native sandboxing | N/A | ❌ Local only |
| MCP support | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ Limited | ❌ | ✅ |

**Key Finding:** ZenFlow is the only tool with native spec-driven development and multi-agent verification ("committee approach") as core features.

### 1.3 Workflow Engine Evaluation

**Contenders Analyzed:**

| Framework | Core Paradigm | Primary Strength | Maturity |
|-----------|---------------|------------------|----------|
| LangGraph | Graph-based stateful workflows | Explicit DAG control, branching, debugging | Most mature (106k ★) |
| CrewAI | Role-based team coordination | YAML-driven, intuitive setup | Mid-maturity (30k+ ★) |
| AutoGen | Conversational multi-agent | Dialogue-driven, flexible topologies | Research-oriented (43.1k+ ★) |
| OpenAI Agents SDK | Lightweight primitives | Minimal abstractions, fast deployment | Newest |

**Head-to-Head Comparison (Key Criteria):**

| Criterion | LangGraph | CrewAI | AutoGen | OpenAI Agents SDK |
|-----------|-----------|--------|---------|-------------------|
| Workflow complexity | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| State management | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Parallelization | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Observability | ⭐⭐⭐⭐⭐ (LangSmith/Langfuse) | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Error handling | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Token efficiency | ⭐⭐⭐⭐⭐ (lowest latency) | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| Production readiness | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

**Recommendation:** LangGraph is superior for SDLC framework due to:
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability with state transition logs and visual graph traces
- Lowest latency and token usage in benchmarks
- Native parallel execution for independent subtasks
- Conditional edges for gating decisions and retry mechanisms

---

## 2. MCP Servers Research

### 2.1 Protocol Understanding

**MCP (Model Context Protocol)** by Anthropic:
- Standard for giving agents access to external tools, data sources, and APIs
- Official repository: `modelcontextprotocol/servers`
- Hundreds of community servers for GitHub, Git, Slack, databases, browsers

**A2A (Agent2Agent) Protocol** by Google (Linux Foundation):
- Enables agents built on different frameworks to discover each other
- Uses JSON-RPC 2.0 over HTTPS
- Complementary to MCP: A2A handles agent-to-agent, MCP handles agent-to-tool

### 2.2 GitHub MCP Server Integration

**Key Tools Available:**
- `create_issue` / `update_issue` — Task creation and status updates
- `create_pull_request` / `merge_pull_request` — Implementation tracking
- `create_branch` — Isolation for atomic tasks
- `add_issue_comment` — Posting verification results, cost data, adversarial findings
- `add_labels` — Phase tracking, gate status, priority
- `assign_copilot_to_issue` — Delegate additional work to Copilot agent
- `search_issues` / `list_pull_requests` — Orchestrator reads project state

### 2.3 Event-Driven Pipeline Architecture

```
Event Flow:
1. LangGraph orchestrator decomposes task → creates GitHub Issue
2. GitHub Issue creation triggers Kilo webhook
3. Kilo Cloud Agent clones repo, creates branch, implements task
4. Kilo Cloud Agent auto-commits and pushes → creates PR
5. PR creation triggers GitHub Agentic Workflow
6. Agentic Workflow runs verification (Code Reviews, tests)
7. Verification results posted as PR comments
8. LangGraph orchestrator reads PR state via GitHub MCP → decides gate
```

---

## 3. Agent Orchestration Research

### 3.1 Inter-Agent Communication Patterns

**Patterns Evaluated:**

| Pattern | How It Works | Best For | Limitations |
|---------|--------------|----------|-------------|
| Subagents | Parent spawns child, receives only results | Simple delegation | No ongoing collaboration |
| Skills | Reusable capabilities agents can invoke | Standardized tasks | Limited context sharing |
| Handoffs | Agent A passes control to Agent B | Sequential workflows | No parallel collaboration |
| Claude Code Agent Teams | Shared task lists, direct messaging, self-coordination | Complex collaboration | Requires Claude Code |
| Roo Code Orchestrator | Hierarchical meta-prompts, context-passing protocols | Structured workflows | Learning curve |

**Key Finding:** Claude Code Agent Teams represent the most advanced inter-agent communication model with shared task lists, direct messaging, and self-coordination capabilities.

### 3.2 Agent Skills Collections

**Top Repositories:**

| Repository | Stars | What It Does |
|------------|-------|--------------|
| anthropic/skills | 61k ★ | Official skills — document creation, design, MCP builder, webapp testing |
| VoltAgent/awesome-agent-skills | 4.7k ★ | Most comprehensive curated list — 200+ skills from major publishers |
| skillcreatorai/Ai-Agent-Skills | — | "Homebrew for AI Agent Skills" — universal installer |

**Standout Skill Categories:**
- **Context Engineering** (by muratcankoylan): context compression, degradation detection, multi-agent patterns, memory systems
- **Security** (by Trail of Bits): 20+ skills including audit context building, static analysis, property-based testing
- **Development** (by obra): subagent-driven development, systematic debugging, root-cause tracing

### 3.3 Multi-Agent Workflow Frameworks

| Framework | Stars | Best For | Approach |
|-----------|-------|----------|----------|
| LangGraph | 106k ★ | Complex workflows with branching logic | Graph-based DAG, explicit state management |
| CrewAI | 30k+ ★ | Fastest time-to-production | Role-based agents with task delegation |
| AutoGen | 43.1k+ ★ | Conversational multi-agent, human-in-loop | Agents chat and iterate naturally |
| Agno | 29k+ ★ | Full-stack multi-agent | Supports all major LLM providers |
| Letta | 15.9k+ ★ | Stateful long-running agents | Memory persistence across sessions |

**Token Efficiency Note:** LangGraph uses ~2,000 tokens per task vs. CrewAI's ~3,500 and AutoGen's ~8,000.

---

## 4. Context Management Research

### 4.1 Context Transfer Protocol

**Spec Artifact Chain Approach:**
- Each SDLC phase produces a spec artifact
- Artifacts are passed along the chain: Requirements Spec → Design Spec → Implementation Spec → Test Spec
- Each artifact includes: context scope, acceptance criteria, constraints, token budget

### 4.2 Context Scoping Principles

**For each atomic task, determine MINIMUM context required:**
- Files needed
- Specs relevant
- Constraints to enforce
- Token budget allocation

### 4.3 Token Optimization Strategies

- Task-specific context reduces bloat
- Avoid conversation history growth
- Use structured JSON output for machine-readable documentation
- Implement context compression for long-running sessions

---

## 5. Testing Frameworks Research

### 5.1 Smoke Testing Framework Architecture

**Core Capabilities (Target State):**

| Capability | Description |
|------------|-------------|
| Universal web interaction engine | Playwright-based, handles all element types, dynamic content, complex forms |
| Dynamic multi-stack orchestration | 3+ containerized test environments (aio, int, prod) with auto port allocation (9330-9399) |
| Intelligent resilience system | Auto retry, element detection strategies, timeout handling, latency tolerance |
| Parallel test execution | Across multiple sites and within same site simultaneously |
| Complete observability stack | WebSocket updates, Prometheus metrics, structured JSON logging, artifact management |
| Database state management | Bidirectional reset supporting PostgreSQL and Oracle |
| Configuration-driven architecture | YAML test definitions |
| Multiple execution interfaces | UI dashboard (Flask), REST API (Express), CLI, programmatic |
| Self-healing capabilities | Element locator fallbacks, intelligent wait strategies, adaptive selectors |

### 5.2 Deviation Detection System

**Deviation Types to Track:**
- Selector Deviations (configured vs. actual selector used)
- Timing Deviations (configured timeout vs. actual wait time)
- Validation Deviations (expected vs. actual error messages)
- Workflow Deviations (configured steps vs. actual execution)
- Data Deviations (expected vs. actual dropdown options)

**Deviation Dashboard Features:**
- Summary View: Total deviations by type, severity, status
- List View: Paginated table with test name, deviation type, timestamp, environment
- Detail View: Side-by-side comparison, visual diff, timeline, frequency chart
- Trend Analysis: Charts showing deviations over time, by module, most common types
- Review Workflow: Assign, comment, batch operations, export reports

### 5.3 Test-Driven Development of UI

**TDD Workflow for Dashboard:**
1. Write tests for desired UI features before implementation
2. Implement UI features to pass tests
3. Validate all UI components work correctly
4. Ensure accessibility compliance
5. Verify responsive design across viewports

---

## 6. CI/CD Patterns Research

### 6.1 GitHub-Native CI/CD Integration

**GitHub Agentic Workflows** (Technical Preview):
- Markdown-defined automations that run coding agents inside GitHub Actions
- Combined with Kilo Code's webhook triggers for event-driven pipeline

### 6.2 Jenkins Integration

**Smoke Test Pipeline:**
- Jenkins triggers deployment → Smoke tests start
- KEDA scales AI analyzer from 0 → 1 pod (5-10 seconds)
- 8 Playwright pods run parallel tests → Call AI service when selectors fail
- AI analyzer handles 20-30 requests/minute
- Tests complete → AI pod scales to 0 after cooldown

### 6.3 Kubernetes Deployment Strategy

**Shared AI Service Pattern (Recommended):**
```
┌─────────────────────────────────────────┐
│  8-Node Kubernetes Cluster              │
├─────────────────────────────────────────┤
│  Smoke Test Pods (6-8 parallel)         │
│  ├─ Playwright container (2GB RAM)      │
│  └─ Calls AI service via HTTP           │
├─────────────────────────────────────────┤
│  AI Analyzer Pod (1-2 replicas)         │
│  ├─ Qwen3-0.6B model (2-3GB RAM)       │
│  └─ Serves all smoke test pods          │
└─────────────────────────────────────────┘
```

**Resource Distribution (8 Nodes @ 4-8 cores, 16-32GB RAM each):**
- Total capacity: 64 CPU cores, 256GB RAM
- Smoke test allocation: 16GB RAM (Playwright) + 3-6GB RAM (AI) = ~20-25GB
- Total consumption: <10% of cluster resources

---

## 7. Tiny AI Models for Testing Research

### 7.1 Model Comparison

| Model | Parameters | Docker Size | Inference Speed | Best For |
|-------|------------|-------------|-----------------|----------|
| SmolLM2-360M | 360M | ~400MB | <100ms | Quick pattern matching, selector analysis |
| Qwen2-0.5B | 500M | ~500MB | ~150ms | Reasoning about failures, context understanding |
| Qwen3-0.6B | 600M | ~600MB | ~5ms/token | Complex decision-making, code understanding |
| Phi-3-mini | 3.8B | ~2.5GB | ~300ms | Complex decision-making, code understanding |

### 7.2 Qwen3-0.6B Deep Dive

**Key Advantages:**
- Released April 2025, trained on 36 trillion tokens across 119 languages
- 32K context window (can analyze entire test suites, DOM snapshots, git diffs)
- Benchmarks: 73% on MATH500, 79.2% on GSM8K, 30.5% on HumanEval
- Built-in agent capabilities for automation and workflow orchestration
- Dual reasoning modes: "thinking" and "non-thinking"

**Resource Requirements:**
- RAM: 8GB total system, ~3GB during inference
- Storage: 3GB for quantized model files
- CPU: 4-8 cores recommended, 2 cores minimum
- Inference speed: 10-30 tokens/second on CPU-only

**Kubernetes Configuration:**
```yaml
resources:
  requests:
    memory: "2Gi"
    cpu: "1000m"
  limits:
    memory: "3Gi"
    cpu: "2000m"
```

### 7.3 Selector Intelligence Layer

**Implementation Approach:**
1. Analyze selector failures and compare current vs. expected DOM structures
2. Evaluate error patterns against historical test data
3. Determine retry worthiness using context (commit messages, recent code changes, error frequency)
4. Provide confidence scores for "legitimate failure" vs. "trivial UI change"

**Decision Framework:**
- Legitimate test failure → FAIL
- Cosmetic change → RETRY
- Timing issue → RETRY
- Environmental → RETRY

---

## 8. ZenFlow Integration Research

### 8.1 ZenFlow Core Concepts

**Four Pillars:**
1. Structured Workflows
2. SDD (Spec-Driven Development)
3. Multi-Agent Verification
4. Parallel Execution

### 8.2 24-Step Custom Workflow

**Phases:**
1. Planning
2. Design
3. Architecture
4. Implementation
5. Review
6. Testing
7. Validation
8. Optimization
9. Refactoring
10. Performance Optimization
11. Production Polish

### 8.3 Evidence-Driven Development

**Zen Rules:**
- All decisions must be based on empirical evidence
- No assumptions without verification
- Continuous validation at each phase
- Automated verification gates

---

## 9. Frontend Analysis Methodology Research

### 9.1 Code Relationship Database Approach

**Core Problem Addressed:**
"I do not know what connects to what, code paths are uncertain, and I need a method to ensure everything is mapped, tested, and maintainable."

**Solution:** Graph database approach treating code as queryable graph structure
- Nodes = files, functions, components
- Edges = imports, calls, relationships
- Enables powerful queries about codebase

### 9.2 Deliverables Created

| Deliverable | Lines | Purpose |
|-------------|-------|---------|
| IMPLEMENTATION_SUMMARY.md | 600 | Complete system overview |
| frontend_analysis_plan.md | 929 | 22-day roadmap, 8 phases |
| quick_start_guide.md | 311 | 30-minute insights |
| tools/dependency_mapper.py | 341 | Automated codebase analysis |
| tools/generate_graph_visualization.html | 536 | Interactive dependency graph |
| VISUAL_ROADMAP.md | 738 | Flowcharts and diagrams |

### 9.3 Key Innovations

- **Graph Database Approach:** Queryable code relationships
- **AI Agent Compatibility:** Structured JSON output, machine-readable documentation
- **Evidence-Based Methods:** Tools from 2026 research (FalkorDB, GitKraken Codemaps, Vitest, Playwright)

---

## 10. Sources Discovered in Space

### 10.1 Official Documentation
- LangGraph Documentation (langchain-ai.github.io)
- Langfuse Documentation (langfuse.com)
- ZenFlow Documentation (zenflow.ai)
- Claude Code Documentation (code.claude.ai)
- GitHub Copilot Documentation (github.com)
- OpenAI Codex Documentation (openai.com)

### 10.2 Research Papers
- FastFlowLM: Efficient LLM Inference (github.com)
- Speculative Decoding Research (AMD dev reports)
- AI-SDLC Maturity Model (eleks.com)

### 10.3 GitHub Repositories
- modelcontextprotocol/servers (MCP servers)
- anthropic/skills (61k ★)
- VoltAgent/awesome-agent-skills (4.7k ★)
- langchain-ai/langgraph (106k ★)
- crewAIInc/crewAI (30k+ ★)
- microsoft/autogen (43.1k+ ★)

### 10.4 Industry Sources
- prnewswire.com (Claude Code Agent Teams)
- xebia.com (Kilo Code/Roo Code analysis)
- intuitionlabs.ai (OpenAI Codex automation)
- linkedin.com (BDD/Gherkin acceptance criteria)
- thoughtworks.com (shift-left involvement)

---

## 11. Research Gaps Identified

### 11.1 Remaining Gaps After Prior Work Integration

1. **MCP Server Ecosystem Deep Dive**
   - Prior work identified MCP protocol but didn't exhaustively catalog all available servers
   - Gap: Complete inventory of production-ready MCP servers by category

2. **A2A Protocol Implementation Details**
   - Prior work mentioned A2A but didn't explore implementation patterns
   - Gap: Concrete A2A integration examples for agent-to-agent communication

3. **Local LLM Deployment Patterns**
   - Prior work mentioned local models but focused on cloud
   - Gap: Comprehensive local LLM deployment architecture for air-gapped environments

4. **Cross-Framework Agent Interoperability**
   - Prior work compared frameworks but didn't address interoperability
   - Gap: Patterns for agents from different frameworks to collaborate

5. **Production Hardening Patterns**
   - Prior work focused on architecture design
   - Gap: Operational runbooks, monitoring, alerting for production agent systems

6. **Security & Compliance for Agent Systems**
   - Prior work mentioned security briefly
   - Gap: Comprehensive security framework for autonomous agent systems

7. **Cost Optimization at Scale**
   - Prior work mentioned cost tracking
   - Gap: Advanced cost optimization strategies for enterprise-scale deployments

### 11.2 Cross-References to Research Taxonomy

| Taxonomy Category | Prior Work Coverage | Gap Status |
|-------------------|---------------------|------------|
| Agentic SDLC Patterns | Comprehensive (v1-v3) | Minor gaps in implementation details |
| MCP Servers | Protocol identified | Needs server catalog |
| Agent Orchestration | LangGraph recommended | Needs A2A implementation |
| Context Management | Spec artifact chain defined | Needs compression strategies |
| Testing Frameworks | Smoke testing architecture | Needs production hardening |
| CI/CD Patterns | GitHub-native approach | Needs operational runbooks |

---

## 12. Key Decisions & Conclusions from Prior Work

### 12.1 Workflow Engine Decision
**Decision:** Use LangGraph  
**Rationale:** 
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability
- Lowest latency and token usage
- Native parallel execution

### 12.2 Model Selection Decision
**Decision:** Kimi K2.5 as primary, Sonnet 4.6, GPT-5.3, Gemini 3 Pro/Flash  
**Rationale:**
- Cost optimization (Kimi is cheapest)
- Escalation path for complex tasks
- Multi-model consensus verification

### 12.3 Task Tracking Decision
**Decision:** GitHub-native (Issues, PRs, branches)  
**Rationale:**
- Permanent, auditable record
- Human-readable project state
- Native CI/CD integration
- Built-in collaboration

### 12.4 Testing Approach Decision
**Decision:** Behavioral testing + consensus-based evaluation + adversarial challenge  
**Rationale:**
- Empirical verification
- Reduces false positives
- Catches edge cases

### 12.5 Local vs Cloud Decision
**Decision:** Hybrid approach  
**Rationale:**
- Local for planning/design (cost, privacy)
- Cloud for implementation (speed)
- Local for final validation (accuracy)

---

## 13. Integration Recommendations

### 13.1 For New Research

1. **Build on LangGraph Foundation**
   - Prior work already selected LangGraph; new research should assume this baseline
   - Focus on graph node/edge design patterns

2. **Extend GitHub-Native Approach**
   - Use GitHub as single source of truth
   - Leverage GitHub MCP server for automation

3. **Incorporate ZenFlow Patterns**
   - Use 24-step workflow as reference
   - Apply evidence-driven development principles

4. **Leverage Tiny AI Models**
   - Qwen3-0.6B for selector intelligence
   - Deploy as shared service in K8s

### 13.2 For Implementation

1. **Start with Smoke Testing Framework**
   - Prior work includes comprehensive architecture
   - Use as proving ground for agentic patterns

2. **Implement Deviation Detection Early**
   - Critical for self-healing capabilities
   - Enables continuous improvement

3. **Use Kilo Code Cloud Agents**
   - For PR reviews and webhook automation
   - Integrates with GitHub-native workflow

---

## 14. Summary Statistics

| Metric | Value |
|--------|-------|
| Research Threads Analyzed | 8+ |
| Sources Cited | 160+ |
| Requirements Versions | 3 (v1 → v2 → v3) |
| Tools Evaluated | 8 |
| Workflow Frameworks Compared | 4 |
| AI Models Analyzed | 4+ |
| SDLC Phases Defined | 7 |
| GitHub Repositories Referenced | 15+ |

---

## 15. Document Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025 | Initial extraction and synthesis from Perplexity Space |

---

*This document represents a comprehensive integration of all substantive research found in the "Smoke Test Framework" Perplexity Space. It should be treated as a living document and updated as new research emerges.*

# Perplexity Space Research Integration: Smoke Test Framework

**Source:** https://www.perplexity.ai/spaces/smoke-test-framework-_L0_2o2dRyaDjDbhcmyOfw  
**Extraction Date:** 2025  
**Research Threads Analyzed:** 8+ substantive threads

---

## Executive Summary

This document synthesizes all substantive research from the "Smoke Test Framework" Perplexity Space, which contains extensive prior work on AI agentic SDLC frameworks, testing infrastructure, MCP servers, agent orchestration, and autonomous development workflows. The space represents 160+ research sources and multiple iterative refinement cycles on designing production-grade autonomous AI coding systems.

### Key Prior Work Identified:
1. **AI Agentic Autonomous SDLC Framework** - Comprehensive requirements across 3 major versions
2. **Smoke Testing Framework Architecture** - Playwright-based enterprise testing platform design
3. **Agent Skills & Workflows Research** - 200+ curated skills from major AI coding tools
4. **Tiny AI Models for Testing** - Docker-optimized models for selector adaptation
5. **ZenFlow Integration** - 24-step autonomous workflow for evidence-driven development
6. **Frontend Analysis Methodology** - Code relationship database approach

---

## 1. Agentic SDLC Patterns Research

### 1.1 Core Architecture Requirements (R-001 to R-014)

**Source Thread:** AI Agentic Autonomous SDLC Framework (Requirements v1-v3)

#### Key Findings:

**Autonomous Requirements Engineering (R-001)**
- Problem: AI agents fail when requirements are insufficient
- Solution: Multi-phase requirements engineering pipeline:
  - Intake → Intent Inference → Clarification Generation → Research Phase → Requirements Formalization → Adversarial Review → Stakeholder Validation Gate
- Format: BDD/Gherkin for unambiguous acceptance criteria
- Research Basis: Spec-driven development research shows under-investing in specs is the #1 failure mode

**Hierarchical Task Decomposition (R-002)**
- Following the Planning Pattern: Goal Analysis → Phase Decomposition → Task Decomposition → Dependency Mapping → Context Scoping → Task Specification
- Each atomic task receives its own concrete requirement document
- MINIMUM context principle to reduce token usage and hallucination risk

**Multi-Model Consensus Verification (R-003)**
- Primary model (Kimi K2.5) → Secondary verification (Sonnet 4.6) → Tertiary arbitration (GPT-5.3)
- Consensus scoring algorithm based on ICE and MUSE research
- Behavioral testing + adversarial challenge approach

**GitHub-Native Task Tracking Architecture**
- GitHub becomes single source of truth for all project state
- Framework Concept → GitHub Object mapping:
  - SDLC Project → GitHub Milestone
  - SDLC Phase → GitHub Label (phase:requirements, phase:design, etc.)
  - Atomic Task → GitHub Issue
  - Task Implementation → GitHub Branch + PR
  - Verification Results → PR Comment
  - Quality Gate Decision → GitHub Label (gate:pass, gate:fail)

### 1.2 Tool Capabilities Matrix

Research across 8 specified tools:

| Capability | Kilo Code | Roo Code | ZenFlow | GitHub Copilot | Claude Code | Codex | Continue | Cline |
|------------|-----------|----------|---------|----------------|-------------|-------|----------|-------|
| Custom modes/roles | YAML modes | Orchestrator + custom | Custom workflows | Custom agents | CLAUDE.md + skills | Skills system | ❌ | Custom modes |
| Multi-agent orchestration | Orchestrator mode | Cloud agents + orchestrator | Parallel agents | Coding agent + agents panel | Agent Teams (3-5) | Multi-threaded | ❌ | ❌ |
| Spec-driven development | Via custom workflows | Via modes | Core feature (SDD) | Via custom instructions | Via CLAUDE.md | Via skills | ❌ | Via rules |
| Multi-model verification | Manual mode switching | Provider-per-mode | Committee approach | ❌ | Team model selection | ❌ | ❌ | Model switching |
| Sandboxed execution | ❌ Local only | Cloud sandboxes | Isolated environments | GitHub Actions sandbox | Local execution | Native sandboxing | N/A | ❌ Local only |
| MCP support | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ Limited | ❌ | ✅ |

**Key Finding:** ZenFlow is the only tool with native spec-driven development and multi-agent verification ("committee approach") as core features.

### 1.3 Workflow Engine Evaluation

**Contenders Analyzed:**

| Framework | Core Paradigm | Primary Strength | Maturity |
|-----------|---------------|------------------|----------|
| LangGraph | Graph-based stateful workflows | Explicit DAG control, branching, debugging | Most mature (106k ★) |
| CrewAI | Role-based team coordination | YAML-driven, intuitive setup | Mid-maturity (30k+ ★) |
| AutoGen | Conversational multi-agent | Dialogue-driven, flexible topologies | Research-oriented (43.1k+ ★) |
| OpenAI Agents SDK | Lightweight primitives | Minimal abstractions, fast deployment | Newest |

**Head-to-Head Comparison (Key Criteria):**

| Criterion | LangGraph | CrewAI | AutoGen | OpenAI Agents SDK |
|-----------|-----------|--------|---------|-------------------|
| Workflow complexity | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| State management | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Parallelization | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Observability | ⭐⭐⭐⭐⭐ (LangSmith/Langfuse) | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Error handling | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Token efficiency | ⭐⭐⭐⭐⭐ (lowest latency) | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| Production readiness | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

**Recommendation:** LangGraph is superior for SDLC framework due to:
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability with state transition logs and visual graph traces
- Lowest latency and token usage in benchmarks
- Native parallel execution for independent subtasks
- Conditional edges for gating decisions and retry mechanisms

---

## 2. MCP Servers Research

### 2.1 Protocol Understanding

**MCP (Model Context Protocol)** by Anthropic:
- Standard for giving agents access to external tools, data sources, and APIs
- Official repository: `modelcontextprotocol/servers`
- Hundreds of community servers for GitHub, Git, Slack, databases, browsers

**A2A (Agent2Agent) Protocol** by Google (Linux Foundation):
- Enables agents built on different frameworks to discover each other
- Uses JSON-RPC 2.0 over HTTPS
- Complementary to MCP: A2A handles agent-to-agent, MCP handles agent-to-tool

### 2.2 GitHub MCP Server Integration

**Key Tools Available:**
- `create_issue` / `update_issue` — Task creation and status updates
- `create_pull_request` / `merge_pull_request` — Implementation tracking
- `create_branch` — Isolation for atomic tasks
- `add_issue_comment` — Posting verification results, cost data, adversarial findings
- `add_labels` — Phase tracking, gate status, priority
- `assign_copilot_to_issue` — Delegate additional work to Copilot agent
- `search_issues` / `list_pull_requests` — Orchestrator reads project state

### 2.3 Event-Driven Pipeline Architecture

```
Event Flow:
1. LangGraph orchestrator decomposes task → creates GitHub Issue
2. GitHub Issue creation triggers Kilo webhook
3. Kilo Cloud Agent clones repo, creates branch, implements task
4. Kilo Cloud Agent auto-commits and pushes → creates PR
5. PR creation triggers GitHub Agentic Workflow
6. Agentic Workflow runs verification (Code Reviews, tests)
7. Verification results posted as PR comments
8. LangGraph orchestrator reads PR state via GitHub MCP → decides gate
```

---

## 3. Agent Orchestration Research

### 3.1 Inter-Agent Communication Patterns

**Patterns Evaluated:**

| Pattern | How It Works | Best For | Limitations |
|---------|--------------|----------|-------------|
| Subagents | Parent spawns child, receives only results | Simple delegation | No ongoing collaboration |
| Skills | Reusable capabilities agents can invoke | Standardized tasks | Limited context sharing |
| Handoffs | Agent A passes control to Agent B | Sequential workflows | No parallel collaboration |
| Claude Code Agent Teams | Shared task lists, direct messaging, self-coordination | Complex collaboration | Requires Claude Code |
| Roo Code Orchestrator | Hierarchical meta-prompts, context-passing protocols | Structured workflows | Learning curve |

**Key Finding:** Claude Code Agent Teams represent the most advanced inter-agent communication model with shared task lists, direct messaging, and self-coordination capabilities.

### 3.2 Agent Skills Collections

**Top Repositories:**

| Repository | Stars | What It Does |
|------------|-------|--------------|
| anthropic/skills | 61k ★ | Official skills — document creation, design, MCP builder, webapp testing |
| VoltAgent/awesome-agent-skills | 4.7k ★ | Most comprehensive curated list — 200+ skills from major publishers |
| skillcreatorai/Ai-Agent-Skills | — | "Homebrew for AI Agent Skills" — universal installer |

**Standout Skill Categories:**
- **Context Engineering** (by muratcankoylan): context compression, degradation detection, multi-agent patterns, memory systems
- **Security** (by Trail of Bits): 20+ skills including audit context building, static analysis, property-based testing
- **Development** (by obra): subagent-driven development, systematic debugging, root-cause tracing

### 3.3 Multi-Agent Workflow Frameworks

| Framework | Stars | Best For | Approach |
|-----------|-------|----------|----------|
| LangGraph | 106k ★ | Complex workflows with branching logic | Graph-based DAG, explicit state management |
| CrewAI | 30k+ ★ | Fastest time-to-production | Role-based agents with task delegation |
| AutoGen | 43.1k+ ★ | Conversational multi-agent, human-in-loop | Agents chat and iterate naturally |
| Agno | 29k+ ★ | Full-stack multi-agent | Supports all major LLM providers |
| Letta | 15.9k+ ★ | Stateful long-running agents | Memory persistence across sessions |

**Token Efficiency Note:** LangGraph uses ~2,000 tokens per task vs. CrewAI's ~3,500 and AutoGen's ~8,000.

---

## 4. Context Management Research

### 4.1 Context Transfer Protocol

**Spec Artifact Chain Approach:**
- Each SDLC phase produces a spec artifact
- Artifacts are passed along the chain: Requirements Spec → Design Spec → Implementation Spec → Test Spec
- Each artifact includes: context scope, acceptance criteria, constraints, token budget

### 4.2 Context Scoping Principles

**For each atomic task, determine MINIMUM context required:**
- Files needed
- Specs relevant
- Constraints to enforce
- Token budget allocation

### 4.3 Token Optimization Strategies

- Task-specific context reduces bloat
- Avoid conversation history growth
- Use structured JSON output for machine-readable documentation
- Implement context compression for long-running sessions

---

## 5. Testing Frameworks Research

### 5.1 Smoke Testing Framework Architecture

**Core Capabilities (Target State):**

| Capability | Description |
|------------|-------------|
| Universal web interaction engine | Playwright-based, handles all element types, dynamic content, complex forms |
| Dynamic multi-stack orchestration | 3+ containerized test environments (aio, int, prod) with auto port allocation (9330-9399) |
| Intelligent resilience system | Auto retry, element detection strategies, timeout handling, latency tolerance |
| Parallel test execution | Across multiple sites and within same site simultaneously |
| Complete observability stack | WebSocket updates, Prometheus metrics, structured JSON logging, artifact management |
| Database state management | Bidirectional reset supporting PostgreSQL and Oracle |
| Configuration-driven architecture | YAML test definitions |
| Multiple execution interfaces | UI dashboard (Flask), REST API (Express), CLI, programmatic |
| Self-healing capabilities | Element locator fallbacks, intelligent wait strategies, adaptive selectors |

### 5.2 Deviation Detection System

**Deviation Types to Track:**
- Selector Deviations (configured vs. actual selector used)
- Timing Deviations (configured timeout vs. actual wait time)
- Validation Deviations (expected vs. actual error messages)
- Workflow Deviations (configured steps vs. actual execution)
- Data Deviations (expected vs. actual dropdown options)

**Deviation Dashboard Features:**
- Summary View: Total deviations by type, severity, status
- List View: Paginated table with test name, deviation type, timestamp, environment
- Detail View: Side-by-side comparison, visual diff, timeline, frequency chart
- Trend Analysis: Charts showing deviations over time, by module, most common types
- Review Workflow: Assign, comment, batch operations, export reports

### 5.3 Test-Driven Development of UI

**TDD Workflow for Dashboard:**
1. Write tests for desired UI features before implementation
2. Implement UI features to pass tests
3. Validate all UI components work correctly
4. Ensure accessibility compliance
5. Verify responsive design across viewports

---

## 6. CI/CD Patterns Research

### 6.1 GitHub-Native CI/CD Integration

**GitHub Agentic Workflows** (Technical Preview):
- Markdown-defined automations that run coding agents inside GitHub Actions
- Combined with Kilo Code's webhook triggers for event-driven pipeline

### 6.2 Jenkins Integration

**Smoke Test Pipeline:**
- Jenkins triggers deployment → Smoke tests start
- KEDA scales AI analyzer from 0 → 1 pod (5-10 seconds)
- 8 Playwright pods run parallel tests → Call AI service when selectors fail
- AI analyzer handles 20-30 requests/minute
- Tests complete → AI pod scales to 0 after cooldown

### 6.3 Kubernetes Deployment Strategy

**Shared AI Service Pattern (Recommended):**
```
┌─────────────────────────────────────────┐
│  8-Node Kubernetes Cluster              │
├─────────────────────────────────────────┤
│  Smoke Test Pods (6-8 parallel)         │
│  ├─ Playwright container (2GB RAM)      │
│  └─ Calls AI service via HTTP           │
├─────────────────────────────────────────┤
│  AI Analyzer Pod (1-2 replicas)         │
│  ├─ Qwen3-0.6B model (2-3GB RAM)       │
│  └─ Serves all smoke test pods          │
└─────────────────────────────────────────┘
```

**Resource Distribution (8 Nodes @ 4-8 cores, 16-32GB RAM each):**
- Total capacity: 64 CPU cores, 256GB RAM
- Smoke test allocation: 16GB RAM (Playwright) + 3-6GB RAM (AI) = ~20-25GB
- Total consumption: <10% of cluster resources

---

## 7. Tiny AI Models for Testing Research

### 7.1 Model Comparison

| Model | Parameters | Docker Size | Inference Speed | Best For |
|-------|------------|-------------|-----------------|----------|
| SmolLM2-360M | 360M | ~400MB | <100ms | Quick pattern matching, selector analysis |
| Qwen2-0.5B | 500M | ~500MB | ~150ms | Reasoning about failures, context understanding |
| Qwen3-0.6B | 600M | ~600MB | ~5ms/token | Complex decision-making, code understanding |
| Phi-3-mini | 3.8B | ~2.5GB | ~300ms | Complex decision-making, code understanding |

### 7.2 Qwen3-0.6B Deep Dive

**Key Advantages:**
- Released April 2025, trained on 36 trillion tokens across 119 languages
- 32K context window (can analyze entire test suites, DOM snapshots, git diffs)
- Benchmarks: 73% on MATH500, 79.2% on GSM8K, 30.5% on HumanEval
- Built-in agent capabilities for automation and workflow orchestration
- Dual reasoning modes: "thinking" and "non-thinking"

**Resource Requirements:**
- RAM: 8GB total system, ~3GB during inference
- Storage: 3GB for quantized model files
- CPU: 4-8 cores recommended, 2 cores minimum
- Inference speed: 10-30 tokens/second on CPU-only

**Kubernetes Configuration:**
```yaml
resources:
  requests:
    memory: "2Gi"
    cpu: "1000m"
  limits:
    memory: "3Gi"
    cpu: "2000m"
```

### 7.3 Selector Intelligence Layer

**Implementation Approach:**
1. Analyze selector failures and compare current vs. expected DOM structures
2. Evaluate error patterns against historical test data
3. Determine retry worthiness using context (commit messages, recent code changes, error frequency)
4. Provide confidence scores for "legitimate failure" vs. "trivial UI change"

**Decision Framework:**
- Legitimate test failure → FAIL
- Cosmetic change → RETRY
- Timing issue → RETRY
- Environmental → RETRY

---

## 8. ZenFlow Integration Research

### 8.1 ZenFlow Core Concepts

**Four Pillars:**
1. Structured Workflows
2. SDD (Spec-Driven Development)
3. Multi-Agent Verification
4. Parallel Execution

### 8.2 24-Step Custom Workflow

**Phases:**
1. Planning
2. Design
3. Architecture
4. Implementation
5. Review
6. Testing
7. Validation
8. Optimization
9. Refactoring
10. Performance Optimization
11. Production Polish

### 8.3 Evidence-Driven Development

**Zen Rules:**
- All decisions must be based on empirical evidence
- No assumptions without verification
- Continuous validation at each phase
- Automated verification gates

---

## 9. Frontend Analysis Methodology Research

### 9.1 Code Relationship Database Approach

**Core Problem Addressed:**
"I do not know what connects to what, code paths are uncertain, and I need a method to ensure everything is mapped, tested, and maintainable."

**Solution:** Graph database approach treating code as queryable graph structure
- Nodes = files, functions, components
- Edges = imports, calls, relationships
- Enables powerful queries about codebase

### 9.2 Deliverables Created

| Deliverable | Lines | Purpose |
|-------------|-------|---------|
| IMPLEMENTATION_SUMMARY.md | 600 | Complete system overview |
| frontend_analysis_plan.md | 929 | 22-day roadmap, 8 phases |
| quick_start_guide.md | 311 | 30-minute insights |
| tools/dependency_mapper.py | 341 | Automated codebase analysis |
| tools/generate_graph_visualization.html | 536 | Interactive dependency graph |
| VISUAL_ROADMAP.md | 738 | Flowcharts and diagrams |

### 9.3 Key Innovations

- **Graph Database Approach:** Queryable code relationships
- **AI Agent Compatibility:** Structured JSON output, machine-readable documentation
- **Evidence-Based Methods:** Tools from 2026 research (FalkorDB, GitKraken Codemaps, Vitest, Playwright)

---

## 10. Sources Discovered in Space

### 10.1 Official Documentation
- LangGraph Documentation (langchain-ai.github.io)
- Langfuse Documentation (langfuse.com)
- ZenFlow Documentation (zenflow.ai)
- Claude Code Documentation (code.claude.ai)
- GitHub Copilot Documentation (github.com)
- OpenAI Codex Documentation (openai.com)

### 10.2 Research Papers
- FastFlowLM: Efficient LLM Inference (github.com)
- Speculative Decoding Research (AMD dev reports)
- AI-SDLC Maturity Model (eleks.com)

### 10.3 GitHub Repositories
- modelcontextprotocol/servers (MCP servers)
- anthropic/skills (61k ★)
- VoltAgent/awesome-agent-skills (4.7k ★)
- langchain-ai/langgraph (106k ★)
- crewAIInc/crewAI (30k+ ★)
- microsoft/autogen (43.1k+ ★)

### 10.4 Industry Sources
- prnewswire.com (Claude Code Agent Teams)
- xebia.com (Kilo Code/Roo Code analysis)
- intuitionlabs.ai (OpenAI Codex automation)
- linkedin.com (BDD/Gherkin acceptance criteria)
- thoughtworks.com (shift-left involvement)

---

## 11. Research Gaps Identified

### 11.1 Remaining Gaps After Prior Work Integration

1. **MCP Server Ecosystem Deep Dive**
   - Prior work identified MCP protocol but didn't exhaustively catalog all available servers
   - Gap: Complete inventory of production-ready MCP servers by category

2. **A2A Protocol Implementation Details**
   - Prior work mentioned A2A but didn't explore implementation patterns
   - Gap: Concrete A2A integration examples for agent-to-agent communication

3. **Local LLM Deployment Patterns**
   - Prior work mentioned local models but focused on cloud
   - Gap: Comprehensive local LLM deployment architecture for air-gapped environments

4. **Cross-Framework Agent Interoperability**
   - Prior work compared frameworks but didn't address interoperability
   - Gap: Patterns for agents from different frameworks to collaborate

5. **Production Hardening Patterns**
   - Prior work focused on architecture design
   - Gap: Operational runbooks, monitoring, alerting for production agent systems

6. **Security & Compliance for Agent Systems**
   - Prior work mentioned security briefly
   - Gap: Comprehensive security framework for autonomous agent systems

7. **Cost Optimization at Scale**
   - Prior work mentioned cost tracking
   - Gap: Advanced cost optimization strategies for enterprise-scale deployments

### 11.2 Cross-References to Research Taxonomy

| Taxonomy Category | Prior Work Coverage | Gap Status |
|-------------------|---------------------|------------|
| Agentic SDLC Patterns | Comprehensive (v1-v3) | Minor gaps in implementation details |
| MCP Servers | Protocol identified | Needs server catalog |
| Agent Orchestration | LangGraph recommended | Needs A2A implementation |
| Context Management | Spec artifact chain defined | Needs compression strategies |
| Testing Frameworks | Smoke testing architecture | Needs production hardening |
| CI/CD Patterns | GitHub-native approach | Needs operational runbooks |

---

## 12. Key Decisions & Conclusions from Prior Work

### 12.1 Workflow Engine Decision
**Decision:** Use LangGraph  
**Rationale:** 
- Stateful graph-based workflows match SDLC pipeline perfectly
- Best-in-class observability
- Lowest latency and token usage
- Native parallel execution

### 12.2 Model Selection Decision
**Decision:** Kimi K2.5 as primary, Sonnet 4.6, GPT-5.3, Gemini 3 Pro/Flash  
**Rationale:**
- Cost optimization (Kimi is cheapest)
- Escalation path for complex tasks
- Multi-model consensus verification

### 12.3 Task Tracking Decision
**Decision:** GitHub-native (Issues, PRs, branches)  
**Rationale:**
- Permanent, auditable record
- Human-readable project state
- Native CI/CD integration
- Built-in collaboration

### 12.4 Testing Approach Decision
**Decision:** Behavioral testing + consensus-based evaluation + adversarial challenge  
**Rationale:**
- Empirical verification
- Reduces false positives
- Catches edge cases

### 12.5 Local vs Cloud Decision
**Decision:** Hybrid approach  
**Rationale:**
- Local for planning/design (cost, privacy)
- Cloud for implementation (speed)
- Local for final validation (accuracy)

---

## 13. Integration Recommendations

### 13.1 For New Research

1. **Build on LangGraph Foundation**
   - Prior work already selected LangGraph; new research should assume this baseline
   - Focus on graph node/edge design patterns

2. **Extend GitHub-Native Approach**
   - Use GitHub as single source of truth
   - Leverage GitHub MCP server for automation

3. **Incorporate ZenFlow Patterns**
   - Use 24-step workflow as reference
   - Apply evidence-driven development principles

4. **Leverage Tiny AI Models**
   - Qwen3-0.6B for selector intelligence
   - Deploy as shared service in K8s

### 13.2 For Implementation

1. **Start with Smoke Testing Framework**
   - Prior work includes comprehensive architecture
   - Use as proving ground for agentic patterns

2. **Implement Deviation Detection Early**
   - Critical for self-healing capabilities
   - Enables continuous improvement

3. **Use Kilo Code Cloud Agents**
   - For PR reviews and webhook automation
   - Integrates with GitHub-native workflow

---

## 14. Summary Statistics

| Metric | Value |
|--------|-------|
| Research Threads Analyzed | 8+ |
| Sources Cited | 160+ |
| Requirements Versions | 3 (v1 → v2 → v3) |
| Tools Evaluated | 8 |
| Workflow Frameworks Compared | 4 |
| AI Models Analyzed | 4+ |
| SDLC Phases Defined | 7 |
| GitHub Repositories Referenced | 15+ |

---

## 15. Document Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025 | Initial extraction and synthesis from Perplexity Space |

---

*This document represents a comprehensive integration of all substantive research found in the "Smoke Test Framework" Perplexity Space. It should be treated as a living document and updated as new research emerges.*
