# SDLC Research Corpus: Global Index

**Last Updated:** February 23, 2026

## Overview

This research corpus provides a comprehensive, research-grade knowledge base on autonomous AI coding systems, agentic SDLC orchestration, and related domains. Research is organized across 12 taxonomy layers covering 100+ topics, each meeting rigorous depth requirements:

- ≥5 peer-reviewed papers analyzed
- ≥20 high-quality web sources analyzed  
- ≥7 community discussion threads analyzed

## Research Tiers

### Tier 1 — CRITICAL (deepest coverage, 7+ papers when available)
- Agent orchestration and multi-agent patterns
- Context management and context limits
- Memory systems (persistent, auto-learning)
- MCP servers (capabilities, selection, security, context-engine)
- Task decomposition and agent coordination
- Testing architecture and automated validation
- CI/CD and self-healing pipelines
- Anti-hallucination and guardrails
- Model routing, switching, and fallback
- Security (prompt injection, sandboxing, context poisoning)

### Tier 2 — HIGH (standard depth, strict minimums)
### Tier 3 — STANDARD (full coverage, slightly narrower)
### Tier 4 — EXPLORATORY (fewer academic sources, expand to adjacent concepts)

## Taxonomy Structure

### I. Meta Architecture Layer
- [System Design & Philosophy](./01_meta_architecture/system_design_philosophy/)
- [Economic & Optimization Modeling](./01_meta_architecture/economic_optimization_modeling/)
- [Governance & Compliance](./01_meta_architecture/governance_compliance/)
- [Security Architecture](./01_meta_architecture/security_architecture/)

### II. Agent & Orchestration Architecture
- [Agent System Design](./02_agent_orchestration/agent_system_design/)
- [Task Architecture](./02_agent_orchestration/task_architecture/)
- [Distributed Orchestration](./02_agent_orchestration/distributed_orchestration/)

### III. Context, Memory & Intelligence
- [Context Management](./03_context_memory_intelligence/context_management/)
- [Memory Systems](./03_context_memory_intelligence/memory_systems/)
- [Reasoning Architecture](./03_context_memory_intelligence/reasoning_architecture/)
- [Knowledge Representation](./03_context_memory_intelligence/knowledge_representation/)

### IV. Code Intelligence & Exploration
- [Code Exploration](./04_code_intelligence/code_exploration/)
- [Specification & Design](./04_code_intelligence/specification_design/)
- [Refactoring & Optimization](./04_code_intelligence/refactoring_optimization/)

### V. SDLC Automation
- [Testing Architecture](./05_sdlc_automation/testing_architecture/)
- [CI/CD & DevOps](./05_sdlc_automation/cicd_devops/)
- [Observability & Feedback Loops](./05_sdlc_automation/observability_feedback_loops/)

### VI. Data & Infrastructure
- [Database & Data Engineering](./06_data_infrastructure/database_data_engineering/)
- [Infrastructure Engineering](./06_data_infrastructure/infrastructure_engineering/)

### VII. Human Interaction Layer
- [Human-in-the-Loop Systems](./07_human_interaction/human_in_the_loop_systems/)

### VIII. Model Management
- [Model Capability Management](./08_model_management/model_capability_management/)

### IX. Research Discipline
- [Research & Benchmarking Framework](./09_research_discipline/research_benchmarking_framework/)

### X. Scaling & Enterprise Layer
- [Large Codebase Handling](./10_scaling_enterprise/large_codebase_handling/)
- [Ecosystem Intelligence](./10_scaling_enterprise/ecosystem_intelligence/)

### XI. Advanced & Bleeding Edge
- [Autonomous Runtime Systems](./11_advanced_runtime/autonomous_runtime_systems/)

### XII. Meta-Control
- [System Self-Improvement](./12_self_improvement/system_self_improvement/)

## Cross-Topic Indices

These indices link related topics across taxonomy layers:

- [MCP Servers Index](./_indices/mcp_servers.md)
- [Testing Strategies Index](./_indices/testing_strategies.md)
- [Context Management Index](./_indices/context_management.md)
- [Agent Coordination Index](./_indices/agent_coordination.md)
- [Security Index](./_indices/security.md)
- [Model Management Index](./_indices/model_management.md)
- [Memory Systems Index](./_indices/memory_systems.md)
- [CI/CD & DevOps Index](./_indices/cicd_devops.md)
- [Code Quality Index](./_indices/code_quality.md)
- [Governance & Compliance Index](./_indices/governance_compliance.md)
- [Scaling & Enterprise Index](./_indices/scaling_enterprise.md)
- [Reasoning & Intelligence Index](./_indices/reasoning_intelligence.md)

## Progress Tracking

See [Completion Tracker](./_progress/completion_tracker.md) for current research status across all topics.

See [Research Log](./_progress/research_log.md) for chronological research activity.

## Deduplication Map

Original List Items → Canonical Taxonomy Locations:

- "Context Management (operational)" → `03_context_memory_intelligence/context_management/`
- "Preventing scope creep" → `01_meta_architecture/system_design_philosophy/`
- "MCP servers" → `02_agent_orchestration/agent_system_design/` (MCP integration)
- "Testing methodologies" → `05_sdlc_automation/testing_architecture/`
- "Memory Management" → `03_context_memory_intelligence/memory_systems/`
- "Agent coordination" → `02_agent_orchestration/agent_system_design/`
- "CI/CD patterns" → `05_sdlc_automation/cicd_devops/`

## Methodology

All research follows a standardized methodology documented in each topic's overview:

1. **Topic Framing**: Define scope and relation to autonomous AI coding
2. **Source Discovery**: Papers (≥5), Web (≥20), Community (≥7)
3. **Evaluation & Filtering**: Quality scoring 1-5
4. **Deep Analysis & Synthesis**: Extract patterns, frameworks, tradeoffs
5. **Comparative View**: Build comparison tables
6. **Implications**: Note future architecture questions

## Prior Research Integration

All topics must integrate findings from:
- **Perplexity Space**: "Smoke Test Framework" — https://www.perplexity.ai/spaces/smoke-test-framework-_L0_2o2dRyaDjDbhcmyOfw
- **ChatGPT Project**: "Smoke" — https://chatgpt.com/g/g-p-67f545accafc81919310480207135d23-smoke/project

## Seed Sources

Mandatory starting points for relevant topics:
- Kilo Auto Launch: https://kilo.ai/docs/automate/extending/auto-launch
- Kilo Ask Follow-up: https://kilo.ai/docs/automate/tools/ask-followup-question
- Zencoder Repo Grokking: https://zencoder.ai/blog/about-repo-grokking
- AugmentCode Spec-Driven Critique: https://www.augmentcode.com/blog/what-spec-driven-development-gets-wrong
- AugmentCode Context Engine MCP: https://www.augmentcode.com/blog/context-engine-mcp-now-live
- Cline Prompts: https://cline.bot/prompts
- Roocode Context Poisoning: https://docs.roocode.com/advanced-usage/context-poisoning
- Roocode Model Temperature: https://docs.roocode.com/features/model-temperature
- Apprise Notifications: https://github.com/caronc/apprise

---

*This research corpus is continuously expanding. Topics are researched iteratively according to tier prioritization.*