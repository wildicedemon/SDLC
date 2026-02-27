# Context Management Cross-Cutting Index

## Overview

This index links all context management related topics across the SDLC research repository taxonomy layers, including context windows, compression, poisoning, cross-repo context, and limits.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| Security Architecture | `01_meta_architecture/security_architecture/overview.md` | Context poisoning attacks, input validation |
| Context Poisoning Analysis | `01_meta_architecture/security_architecture/roocode_context_poisoning_analysis.md` | Roo Code specific poisoning vulnerabilities |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP context consumption, tool descriptions |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent context handling, multi-agent context sharing |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| **Context Management** | `03_context_memory_intelligence/context_management/overview.md` | **Primary canonical document** - context window, compression, limits |
| Context Comparisons | `03_context_memory_intelligence/context_management/comparisons.md` | Comparative context system analysis |
| Context Engine MCP | `03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md` | Augment's semantic context engine |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Persistent context, memory-context integration |
| Memory Comparisons | `03_context_memory_intelligence/memory_systems/comparisons.md` | Memory system tradeoffs |

### Layer 4: Code Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Code Exploration | `04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md` | Large codebase context handling |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | CI context management, build context |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Test context generation |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Human context provision |

### Layer 8: Model Management

| Topic | Path | Relationship |
|-------|------|--------------|
| Model Temperature | `08_model_management/model_capability_management/roocode_temperature_analysis.md` | Context-aware temperature selection |

---

## Context Management Sub-Topics

### Context Windows
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Advertised vs Effective | 10-30% effective utilization | `context_management/overview.md` |
| "Lost in the Middle" | U-shaped performance curve | `context_management/overview.md` |
| Model Comparison | GPT-4, Claude, Gemini windows | `context_management/overview.md` |

### Context Compression
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Compression Ratios | 4-64x with minimal degradation | `context_management/overview.md` |
| Soft Prompt Compression | ICAE, AutoCompressors | `context_management/overview.md` |
| KV Cache Optimization | CompilerKV, RAP | `context_management/overview.md` |

### Context Poisoning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Attack Vectors | Comments, README, metadata | `context_management/overview.md` |
| Detection Strategies | Repository hygiene, IDE guardrails | `context_management/overview.md` |
| Roo Code Specific | `roocode_context_poisoning_analysis.md` | Poisoning in Roo Code |

### Cross-Repository Context
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Augment Context Engine | 70%+ improvement | `augment_context_engine_mcp_analysis.md` |
| Multi-Repo Support | Service-to-service mapping | `augment_context_engine_mcp_analysis.md` |
| Monorepo Handling | Large codebase strategies | `zencoder_repo_grokking_analysis.md` |

### Context Limits
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Token Budgeting | Cost optimization | `context_management/overview.md` |
| Progressive Compaction | 85% threshold triggers | `context_management/overview.md` |
| Multi-Session Architecture | Parallel context handling | `context_management/overview.md` |

---

## Cross-Dependencies

### Context Window Dependencies
```
Context Windows
├── Model Management (model-specific limits)
├── Memory Systems (external memory extension)
├── MCP Servers (tool description consumption)
├── RAG Systems (retrieval augmentation)
└── Compression (context optimization)
```

### Context Poisoning Dependencies
```
Context Poisoning
├── Security Architecture (attack taxonomy)
├── Input Validation (sanitization)
├── Sandboxing (isolation)
├── Audit Logging (detection)
└── Human-in-the-Loop (validation)
```

### Cross-Repo Context Dependencies
```
Cross-Repo Context
├── Context Engine MCP (Augment)
├── Knowledge Graphs (relationship mapping)
├── Vector Databases (semantic search)
├── Code Intelligence (repo understanding)
└── CI/CD (multi-repo pipelines)
```

---

## Key Research Areas

### 1. RAG vs Long-Context Tradeoffs
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Key Findings:**
  - RAG: 1,250x lower cost, 45x faster
  - Long-Context: Superior accuracy for complex reasoning
  - Hybrid approaches (Self-Route, Pre-Route) emerging

### 2. Context Compression Techniques
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Methods:**
  - Context Window Extension (PI, YaRN)
  - Pre-Trained Models (AutoCompressors, RECOMP)
  - Retriever-Based (LLMChainExtractor)

### 3. Memory-Context Integration
- **Location:** `03_context_memory_intelligence/memory_systems/overview.md`
- **Architecture:**
  - Short-Term Memory (context window)
  - Long-Term Memory (vector/graph stores)
  - Write-Through Cache Pattern

### 4. Context Poisoning Mitigation
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Strategies:**
  - Repository hygiene practices
  - IDE guardrails
  - MCP output validation
  - Real-time context scanning (Kirin)

---

## Reference Documents

### Primary Sources
1. [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md) - Comprehensive context research
2. [Augment Context Engine MCP](../03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md) - Context Engine analysis
3. [Memory Systems](../03_context_memory_intelligence/memory_systems/overview.md) - Memory-context integration

### Secondary Sources
4. [Security Architecture](../01_meta_architecture/security_architecture/overview.md) - Context poisoning
5. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP context consumption
6. [Code Exploration](../04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md) - Large codebase context

---

## Navigation

- **Previous Index:** [Testing Strategies](testing_strategies.md)
- **Next Index:** [Security](security.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Context Management Cross-Cutting Index

## Overview

This index links all context management related topics across the SDLC research repository taxonomy layers, including context windows, compression, poisoning, cross-repo context, and limits.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| Security Architecture | `01_meta_architecture/security_architecture/overview.md` | Context poisoning attacks, input validation |
| Context Poisoning Analysis | `01_meta_architecture/security_architecture/roocode_context_poisoning_analysis.md` | Roo Code specific poisoning vulnerabilities |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP context consumption, tool descriptions |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent context handling, multi-agent context sharing |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| **Context Management** | `03_context_memory_intelligence/context_management/overview.md` | **Primary canonical document** - context window, compression, limits |
| Context Comparisons | `03_context_memory_intelligence/context_management/comparisons.md` | Comparative context system analysis |
| Context Engine MCP | `03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md` | Augment's semantic context engine |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Persistent context, memory-context integration |
| Memory Comparisons | `03_context_memory_intelligence/memory_systems/comparisons.md` | Memory system tradeoffs |

### Layer 4: Code Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Code Exploration | `04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md` | Large codebase context handling |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | CI context management, build context |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Test context generation |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Human context provision |

### Layer 8: Model Management

| Topic | Path | Relationship |
|-------|------|--------------|
| Model Temperature | `08_model_management/model_capability_management/roocode_temperature_analysis.md` | Context-aware temperature selection |

---

## Context Management Sub-Topics

### Context Windows
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Advertised vs Effective | 10-30% effective utilization | `context_management/overview.md` |
| "Lost in the Middle" | U-shaped performance curve | `context_management/overview.md` |
| Model Comparison | GPT-4, Claude, Gemini windows | `context_management/overview.md` |

### Context Compression
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Compression Ratios | 4-64x with minimal degradation | `context_management/overview.md` |
| Soft Prompt Compression | ICAE, AutoCompressors | `context_management/overview.md` |
| KV Cache Optimization | CompilerKV, RAP | `context_management/overview.md` |

### Context Poisoning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Attack Vectors | Comments, README, metadata | `context_management/overview.md` |
| Detection Strategies | Repository hygiene, IDE guardrails | `context_management/overview.md` |
| Roo Code Specific | `roocode_context_poisoning_analysis.md` | Poisoning in Roo Code |

### Cross-Repository Context
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Augment Context Engine | 70%+ improvement | `augment_context_engine_mcp_analysis.md` |
| Multi-Repo Support | Service-to-service mapping | `augment_context_engine_mcp_analysis.md` |
| Monorepo Handling | Large codebase strategies | `zencoder_repo_grokking_analysis.md` |

### Context Limits
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Token Budgeting | Cost optimization | `context_management/overview.md` |
| Progressive Compaction | 85% threshold triggers | `context_management/overview.md` |
| Multi-Session Architecture | Parallel context handling | `context_management/overview.md` |

---

## Cross-Dependencies

### Context Window Dependencies
```
Context Windows
├── Model Management (model-specific limits)
├── Memory Systems (external memory extension)
├── MCP Servers (tool description consumption)
├── RAG Systems (retrieval augmentation)
└── Compression (context optimization)
```

### Context Poisoning Dependencies
```
Context Poisoning
├── Security Architecture (attack taxonomy)
├── Input Validation (sanitization)
├── Sandboxing (isolation)
├── Audit Logging (detection)
└── Human-in-the-Loop (validation)
```

### Cross-Repo Context Dependencies
```
Cross-Repo Context
├── Context Engine MCP (Augment)
├── Knowledge Graphs (relationship mapping)
├── Vector Databases (semantic search)
├── Code Intelligence (repo understanding)
└── CI/CD (multi-repo pipelines)
```

---

## Key Research Areas

### 1. RAG vs Long-Context Tradeoffs
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Key Findings:**
  - RAG: 1,250x lower cost, 45x faster
  - Long-Context: Superior accuracy for complex reasoning
  - Hybrid approaches (Self-Route, Pre-Route) emerging

### 2. Context Compression Techniques
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Methods:**
  - Context Window Extension (PI, YaRN)
  - Pre-Trained Models (AutoCompressors, RECOMP)
  - Retriever-Based (LLMChainExtractor)

### 3. Memory-Context Integration
- **Location:** `03_context_memory_intelligence/memory_systems/overview.md`
- **Architecture:**
  - Short-Term Memory (context window)
  - Long-Term Memory (vector/graph stores)
  - Write-Through Cache Pattern

### 4. Context Poisoning Mitigation
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Strategies:**
  - Repository hygiene practices
  - IDE guardrails
  - MCP output validation
  - Real-time context scanning (Kirin)

---

## Reference Documents

### Primary Sources
1. [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md) - Comprehensive context research
2. [Augment Context Engine MCP](../03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md) - Context Engine analysis
3. [Memory Systems](../03_context_memory_intelligence/memory_systems/overview.md) - Memory-context integration

### Secondary Sources
4. [Security Architecture](../01_meta_architecture/security_architecture/overview.md) - Context poisoning
5. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP context consumption
6. [Code Exploration](../04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md) - Large codebase context

---

## Navigation

- **Previous Index:** [Testing Strategies](testing_strategies.md)
- **Next Index:** [Security](security.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Context Management Cross-Cutting Index

## Overview

This index links all context management related topics across the SDLC research repository taxonomy layers, including context windows, compression, poisoning, cross-repo context, and limits.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| Security Architecture | `01_meta_architecture/security_architecture/overview.md` | Context poisoning attacks, input validation |
| Context Poisoning Analysis | `01_meta_architecture/security_architecture/roocode_context_poisoning_analysis.md` | Roo Code specific poisoning vulnerabilities |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP context consumption, tool descriptions |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent context handling, multi-agent context sharing |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| **Context Management** | `03_context_memory_intelligence/context_management/overview.md` | **Primary canonical document** - context window, compression, limits |
| Context Comparisons | `03_context_memory_intelligence/context_management/comparisons.md` | Comparative context system analysis |
| Context Engine MCP | `03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md` | Augment's semantic context engine |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Persistent context, memory-context integration |
| Memory Comparisons | `03_context_memory_intelligence/memory_systems/comparisons.md` | Memory system tradeoffs |

### Layer 4: Code Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Code Exploration | `04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md` | Large codebase context handling |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | CI context management, build context |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Test context generation |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Human context provision |

### Layer 8: Model Management

| Topic | Path | Relationship |
|-------|------|--------------|
| Model Temperature | `08_model_management/model_capability_management/roocode_temperature_analysis.md` | Context-aware temperature selection |

---

## Context Management Sub-Topics

### Context Windows
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Advertised vs Effective | 10-30% effective utilization | `context_management/overview.md` |
| "Lost in the Middle" | U-shaped performance curve | `context_management/overview.md` |
| Model Comparison | GPT-4, Claude, Gemini windows | `context_management/overview.md` |

### Context Compression
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Compression Ratios | 4-64x with minimal degradation | `context_management/overview.md` |
| Soft Prompt Compression | ICAE, AutoCompressors | `context_management/overview.md` |
| KV Cache Optimization | CompilerKV, RAP | `context_management/overview.md` |

### Context Poisoning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Attack Vectors | Comments, README, metadata | `context_management/overview.md` |
| Detection Strategies | Repository hygiene, IDE guardrails | `context_management/overview.md` |
| Roo Code Specific | `roocode_context_poisoning_analysis.md` | Poisoning in Roo Code |

### Cross-Repository Context
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Augment Context Engine | 70%+ improvement | `augment_context_engine_mcp_analysis.md` |
| Multi-Repo Support | Service-to-service mapping | `augment_context_engine_mcp_analysis.md` |
| Monorepo Handling | Large codebase strategies | `zencoder_repo_grokking_analysis.md` |

### Context Limits
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Token Budgeting | Cost optimization | `context_management/overview.md` |
| Progressive Compaction | 85% threshold triggers | `context_management/overview.md` |
| Multi-Session Architecture | Parallel context handling | `context_management/overview.md` |

---

## Cross-Dependencies

### Context Window Dependencies
```
Context Windows
├── Model Management (model-specific limits)
├── Memory Systems (external memory extension)
├── MCP Servers (tool description consumption)
├── RAG Systems (retrieval augmentation)
└── Compression (context optimization)
```

### Context Poisoning Dependencies
```
Context Poisoning
├── Security Architecture (attack taxonomy)
├── Input Validation (sanitization)
├── Sandboxing (isolation)
├── Audit Logging (detection)
└── Human-in-the-Loop (validation)
```

### Cross-Repo Context Dependencies
```
Cross-Repo Context
├── Context Engine MCP (Augment)
├── Knowledge Graphs (relationship mapping)
├── Vector Databases (semantic search)
├── Code Intelligence (repo understanding)
└── CI/CD (multi-repo pipelines)
```

---

## Key Research Areas

### 1. RAG vs Long-Context Tradeoffs
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Key Findings:**
  - RAG: 1,250x lower cost, 45x faster
  - Long-Context: Superior accuracy for complex reasoning
  - Hybrid approaches (Self-Route, Pre-Route) emerging

### 2. Context Compression Techniques
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Methods:**
  - Context Window Extension (PI, YaRN)
  - Pre-Trained Models (AutoCompressors, RECOMP)
  - Retriever-Based (LLMChainExtractor)

### 3. Memory-Context Integration
- **Location:** `03_context_memory_intelligence/memory_systems/overview.md`
- **Architecture:**
  - Short-Term Memory (context window)
  - Long-Term Memory (vector/graph stores)
  - Write-Through Cache Pattern

### 4. Context Poisoning Mitigation
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Strategies:**
  - Repository hygiene practices
  - IDE guardrails
  - MCP output validation
  - Real-time context scanning (Kirin)

---

## Reference Documents

### Primary Sources
1. [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md) - Comprehensive context research
2. [Augment Context Engine MCP](../03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md) - Context Engine analysis
3. [Memory Systems](../03_context_memory_intelligence/memory_systems/overview.md) - Memory-context integration

### Secondary Sources
4. [Security Architecture](../01_meta_architecture/security_architecture/overview.md) - Context poisoning
5. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP context consumption
6. [Code Exploration](../04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md) - Large codebase context

---

## Navigation

- **Previous Index:** [Testing Strategies](testing_strategies.md)
- **Next Index:** [Security](security.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Context Management Cross-Cutting Index

## Overview

This index links all context management related topics across the SDLC research repository taxonomy layers, including context windows, compression, poisoning, cross-repo context, and limits.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| Security Architecture | `01_meta_architecture/security_architecture/overview.md` | Context poisoning attacks, input validation |
| Context Poisoning Analysis | `01_meta_architecture/security_architecture/roocode_context_poisoning_analysis.md` | Roo Code specific poisoning vulnerabilities |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP context consumption, tool descriptions |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent context handling, multi-agent context sharing |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| **Context Management** | `03_context_memory_intelligence/context_management/overview.md` | **Primary canonical document** - context window, compression, limits |
| Context Comparisons | `03_context_memory_intelligence/context_management/comparisons.md` | Comparative context system analysis |
| Context Engine MCP | `03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md` | Augment's semantic context engine |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Persistent context, memory-context integration |
| Memory Comparisons | `03_context_memory_intelligence/memory_systems/comparisons.md` | Memory system tradeoffs |

### Layer 4: Code Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Code Exploration | `04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md` | Large codebase context handling |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | CI context management, build context |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Test context generation |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Human context provision |

### Layer 8: Model Management

| Topic | Path | Relationship |
|-------|------|--------------|
| Model Temperature | `08_model_management/model_capability_management/roocode_temperature_analysis.md` | Context-aware temperature selection |

---

## Context Management Sub-Topics

### Context Windows
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Advertised vs Effective | 10-30% effective utilization | `context_management/overview.md` |
| "Lost in the Middle" | U-shaped performance curve | `context_management/overview.md` |
| Model Comparison | GPT-4, Claude, Gemini windows | `context_management/overview.md` |

### Context Compression
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Compression Ratios | 4-64x with minimal degradation | `context_management/overview.md` |
| Soft Prompt Compression | ICAE, AutoCompressors | `context_management/overview.md` |
| KV Cache Optimization | CompilerKV, RAP | `context_management/overview.md` |

### Context Poisoning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Attack Vectors | Comments, README, metadata | `context_management/overview.md` |
| Detection Strategies | Repository hygiene, IDE guardrails | `context_management/overview.md` |
| Roo Code Specific | `roocode_context_poisoning_analysis.md` | Poisoning in Roo Code |

### Cross-Repository Context
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Augment Context Engine | 70%+ improvement | `augment_context_engine_mcp_analysis.md` |
| Multi-Repo Support | Service-to-service mapping | `augment_context_engine_mcp_analysis.md` |
| Monorepo Handling | Large codebase strategies | `zencoder_repo_grokking_analysis.md` |

### Context Limits
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Token Budgeting | Cost optimization | `context_management/overview.md` |
| Progressive Compaction | 85% threshold triggers | `context_management/overview.md` |
| Multi-Session Architecture | Parallel context handling | `context_management/overview.md` |

---

## Cross-Dependencies

### Context Window Dependencies
```
Context Windows
├── Model Management (model-specific limits)
├── Memory Systems (external memory extension)
├── MCP Servers (tool description consumption)
├── RAG Systems (retrieval augmentation)
└── Compression (context optimization)
```

### Context Poisoning Dependencies
```
Context Poisoning
├── Security Architecture (attack taxonomy)
├── Input Validation (sanitization)
├── Sandboxing (isolation)
├── Audit Logging (detection)
└── Human-in-the-Loop (validation)
```

### Cross-Repo Context Dependencies
```
Cross-Repo Context
├── Context Engine MCP (Augment)
├── Knowledge Graphs (relationship mapping)
├── Vector Databases (semantic search)
├── Code Intelligence (repo understanding)
└── CI/CD (multi-repo pipelines)
```

---

## Key Research Areas

### 1. RAG vs Long-Context Tradeoffs
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Key Findings:**
  - RAG: 1,250x lower cost, 45x faster
  - Long-Context: Superior accuracy for complex reasoning
  - Hybrid approaches (Self-Route, Pre-Route) emerging

### 2. Context Compression Techniques
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Methods:**
  - Context Window Extension (PI, YaRN)
  - Pre-Trained Models (AutoCompressors, RECOMP)
  - Retriever-Based (LLMChainExtractor)

### 3. Memory-Context Integration
- **Location:** `03_context_memory_intelligence/memory_systems/overview.md`
- **Architecture:**
  - Short-Term Memory (context window)
  - Long-Term Memory (vector/graph stores)
  - Write-Through Cache Pattern

### 4. Context Poisoning Mitigation
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Strategies:**
  - Repository hygiene practices
  - IDE guardrails
  - MCP output validation
  - Real-time context scanning (Kirin)

---

## Reference Documents

### Primary Sources
1. [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md) - Comprehensive context research
2. [Augment Context Engine MCP](../03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md) - Context Engine analysis
3. [Memory Systems](../03_context_memory_intelligence/memory_systems/overview.md) - Memory-context integration

### Secondary Sources
4. [Security Architecture](../01_meta_architecture/security_architecture/overview.md) - Context poisoning
5. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP context consumption
6. [Code Exploration](../04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md) - Large codebase context

---

## Navigation

- **Previous Index:** [Testing Strategies](testing_strategies.md)
- **Next Index:** [Security](security.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Context Management Cross-Cutting Index

## Overview

This index links all context management related topics across the SDLC research repository taxonomy layers, including context windows, compression, poisoning, cross-repo context, and limits.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| Security Architecture | `01_meta_architecture/security_architecture/overview.md` | Context poisoning attacks, input validation |
| Context Poisoning Analysis | `01_meta_architecture/security_architecture/roocode_context_poisoning_analysis.md` | Roo Code specific poisoning vulnerabilities |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP context consumption, tool descriptions |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent context handling, multi-agent context sharing |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| **Context Management** | `03_context_memory_intelligence/context_management/overview.md` | **Primary canonical document** - context window, compression, limits |
| Context Comparisons | `03_context_memory_intelligence/context_management/comparisons.md` | Comparative context system analysis |
| Context Engine MCP | `03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md` | Augment's semantic context engine |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Persistent context, memory-context integration |
| Memory Comparisons | `03_context_memory_intelligence/memory_systems/comparisons.md` | Memory system tradeoffs |

### Layer 4: Code Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Code Exploration | `04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md` | Large codebase context handling |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | CI context management, build context |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Test context generation |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Human context provision |

### Layer 8: Model Management

| Topic | Path | Relationship |
|-------|------|--------------|
| Model Temperature | `08_model_management/model_capability_management/roocode_temperature_analysis.md` | Context-aware temperature selection |

---

## Context Management Sub-Topics

### Context Windows
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Advertised vs Effective | 10-30% effective utilization | `context_management/overview.md` |
| "Lost in the Middle" | U-shaped performance curve | `context_management/overview.md` |
| Model Comparison | GPT-4, Claude, Gemini windows | `context_management/overview.md` |

### Context Compression
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Compression Ratios | 4-64x with minimal degradation | `context_management/overview.md` |
| Soft Prompt Compression | ICAE, AutoCompressors | `context_management/overview.md` |
| KV Cache Optimization | CompilerKV, RAP | `context_management/overview.md` |

### Context Poisoning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Attack Vectors | Comments, README, metadata | `context_management/overview.md` |
| Detection Strategies | Repository hygiene, IDE guardrails | `context_management/overview.md` |
| Roo Code Specific | `roocode_context_poisoning_analysis.md` | Poisoning in Roo Code |

### Cross-Repository Context
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Augment Context Engine | 70%+ improvement | `augment_context_engine_mcp_analysis.md` |
| Multi-Repo Support | Service-to-service mapping | `augment_context_engine_mcp_analysis.md` |
| Monorepo Handling | Large codebase strategies | `zencoder_repo_grokking_analysis.md` |

### Context Limits
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Token Budgeting | Cost optimization | `context_management/overview.md` |
| Progressive Compaction | 85% threshold triggers | `context_management/overview.md` |
| Multi-Session Architecture | Parallel context handling | `context_management/overview.md` |

---

## Cross-Dependencies

### Context Window Dependencies
```
Context Windows
├── Model Management (model-specific limits)
├── Memory Systems (external memory extension)
├── MCP Servers (tool description consumption)
├── RAG Systems (retrieval augmentation)
└── Compression (context optimization)
```

### Context Poisoning Dependencies
```
Context Poisoning
├── Security Architecture (attack taxonomy)
├── Input Validation (sanitization)
├── Sandboxing (isolation)
├── Audit Logging (detection)
└── Human-in-the-Loop (validation)
```

### Cross-Repo Context Dependencies
```
Cross-Repo Context
├── Context Engine MCP (Augment)
├── Knowledge Graphs (relationship mapping)
├── Vector Databases (semantic search)
├── Code Intelligence (repo understanding)
└── CI/CD (multi-repo pipelines)
```

---

## Key Research Areas

### 1. RAG vs Long-Context Tradeoffs
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Key Findings:**
  - RAG: 1,250x lower cost, 45x faster
  - Long-Context: Superior accuracy for complex reasoning
  - Hybrid approaches (Self-Route, Pre-Route) emerging

### 2. Context Compression Techniques
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Methods:**
  - Context Window Extension (PI, YaRN)
  - Pre-Trained Models (AutoCompressors, RECOMP)
  - Retriever-Based (LLMChainExtractor)

### 3. Memory-Context Integration
- **Location:** `03_context_memory_intelligence/memory_systems/overview.md`
- **Architecture:**
  - Short-Term Memory (context window)
  - Long-Term Memory (vector/graph stores)
  - Write-Through Cache Pattern

### 4. Context Poisoning Mitigation
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Strategies:**
  - Repository hygiene practices
  - IDE guardrails
  - MCP output validation
  - Real-time context scanning (Kirin)

---

## Reference Documents

### Primary Sources
1. [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md) - Comprehensive context research
2. [Augment Context Engine MCP](../03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md) - Context Engine analysis
3. [Memory Systems](../03_context_memory_intelligence/memory_systems/overview.md) - Memory-context integration

### Secondary Sources
4. [Security Architecture](../01_meta_architecture/security_architecture/overview.md) - Context poisoning
5. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP context consumption
6. [Code Exploration](../04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md) - Large codebase context

---

## Navigation

- **Previous Index:** [Testing Strategies](testing_strategies.md)
- **Next Index:** [Security](security.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Context Management Cross-Cutting Index

## Overview

This index links all context management related topics across the SDLC research repository taxonomy layers, including context windows, compression, poisoning, cross-repo context, and limits.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| Security Architecture | `01_meta_architecture/security_architecture/overview.md` | Context poisoning attacks, input validation |
| Context Poisoning Analysis | `01_meta_architecture/security_architecture/roocode_context_poisoning_analysis.md` | Roo Code specific poisoning vulnerabilities |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP context consumption, tool descriptions |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent context handling, multi-agent context sharing |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| **Context Management** | `03_context_memory_intelligence/context_management/overview.md` | **Primary canonical document** - context window, compression, limits |
| Context Comparisons | `03_context_memory_intelligence/context_management/comparisons.md` | Comparative context system analysis |
| Context Engine MCP | `03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md` | Augment's semantic context engine |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Persistent context, memory-context integration |
| Memory Comparisons | `03_context_memory_intelligence/memory_systems/comparisons.md` | Memory system tradeoffs |

### Layer 4: Code Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Code Exploration | `04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md` | Large codebase context handling |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | CI context management, build context |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Test context generation |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Human context provision |

### Layer 8: Model Management

| Topic | Path | Relationship |
|-------|------|--------------|
| Model Temperature | `08_model_management/model_capability_management/roocode_temperature_analysis.md` | Context-aware temperature selection |

---

## Context Management Sub-Topics

### Context Windows
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Advertised vs Effective | 10-30% effective utilization | `context_management/overview.md` |
| "Lost in the Middle" | U-shaped performance curve | `context_management/overview.md` |
| Model Comparison | GPT-4, Claude, Gemini windows | `context_management/overview.md` |

### Context Compression
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Compression Ratios | 4-64x with minimal degradation | `context_management/overview.md` |
| Soft Prompt Compression | ICAE, AutoCompressors | `context_management/overview.md` |
| KV Cache Optimization | CompilerKV, RAP | `context_management/overview.md` |

### Context Poisoning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Attack Vectors | Comments, README, metadata | `context_management/overview.md` |
| Detection Strategies | Repository hygiene, IDE guardrails | `context_management/overview.md` |
| Roo Code Specific | `roocode_context_poisoning_analysis.md` | Poisoning in Roo Code |

### Cross-Repository Context
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Augment Context Engine | 70%+ improvement | `augment_context_engine_mcp_analysis.md` |
| Multi-Repo Support | Service-to-service mapping | `augment_context_engine_mcp_analysis.md` |
| Monorepo Handling | Large codebase strategies | `zencoder_repo_grokking_analysis.md` |

### Context Limits
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Token Budgeting | Cost optimization | `context_management/overview.md` |
| Progressive Compaction | 85% threshold triggers | `context_management/overview.md` |
| Multi-Session Architecture | Parallel context handling | `context_management/overview.md` |

---

## Cross-Dependencies

### Context Window Dependencies
```
Context Windows
├── Model Management (model-specific limits)
├── Memory Systems (external memory extension)
├── MCP Servers (tool description consumption)
├── RAG Systems (retrieval augmentation)
└── Compression (context optimization)
```

### Context Poisoning Dependencies
```
Context Poisoning
├── Security Architecture (attack taxonomy)
├── Input Validation (sanitization)
├── Sandboxing (isolation)
├── Audit Logging (detection)
└── Human-in-the-Loop (validation)
```

### Cross-Repo Context Dependencies
```
Cross-Repo Context
├── Context Engine MCP (Augment)
├── Knowledge Graphs (relationship mapping)
├── Vector Databases (semantic search)
├── Code Intelligence (repo understanding)
└── CI/CD (multi-repo pipelines)
```

---

## Key Research Areas

### 1. RAG vs Long-Context Tradeoffs
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Key Findings:**
  - RAG: 1,250x lower cost, 45x faster
  - Long-Context: Superior accuracy for complex reasoning
  - Hybrid approaches (Self-Route, Pre-Route) emerging

### 2. Context Compression Techniques
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Methods:**
  - Context Window Extension (PI, YaRN)
  - Pre-Trained Models (AutoCompressors, RECOMP)
  - Retriever-Based (LLMChainExtractor)

### 3. Memory-Context Integration
- **Location:** `03_context_memory_intelligence/memory_systems/overview.md`
- **Architecture:**
  - Short-Term Memory (context window)
  - Long-Term Memory (vector/graph stores)
  - Write-Through Cache Pattern

### 4. Context Poisoning Mitigation
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Strategies:**
  - Repository hygiene practices
  - IDE guardrails
  - MCP output validation
  - Real-time context scanning (Kirin)

---

## Reference Documents

### Primary Sources
1. [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md) - Comprehensive context research
2. [Augment Context Engine MCP](../03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md) - Context Engine analysis
3. [Memory Systems](../03_context_memory_intelligence/memory_systems/overview.md) - Memory-context integration

### Secondary Sources
4. [Security Architecture](../01_meta_architecture/security_architecture/overview.md) - Context poisoning
5. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP context consumption
6. [Code Exploration](../04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md) - Large codebase context

---

## Navigation

- **Previous Index:** [Testing Strategies](testing_strategies.md)
- **Next Index:** [Security](security.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Context Management Cross-Cutting Index

## Overview

This index links all context management related topics across the SDLC research repository taxonomy layers, including context windows, compression, poisoning, cross-repo context, and limits.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| Security Architecture | `01_meta_architecture/security_architecture/overview.md` | Context poisoning attacks, input validation |
| Context Poisoning Analysis | `01_meta_architecture/security_architecture/roocode_context_poisoning_analysis.md` | Roo Code specific poisoning vulnerabilities |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP context consumption, tool descriptions |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent context handling, multi-agent context sharing |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| **Context Management** | `03_context_memory_intelligence/context_management/overview.md` | **Primary canonical document** - context window, compression, limits |
| Context Comparisons | `03_context_memory_intelligence/context_management/comparisons.md` | Comparative context system analysis |
| Context Engine MCP | `03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md` | Augment's semantic context engine |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Persistent context, memory-context integration |
| Memory Comparisons | `03_context_memory_intelligence/memory_systems/comparisons.md` | Memory system tradeoffs |

### Layer 4: Code Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Code Exploration | `04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md` | Large codebase context handling |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | CI context management, build context |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Test context generation |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Human context provision |

### Layer 8: Model Management

| Topic | Path | Relationship |
|-------|------|--------------|
| Model Temperature | `08_model_management/model_capability_management/roocode_temperature_analysis.md` | Context-aware temperature selection |

---

## Context Management Sub-Topics

### Context Windows
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Advertised vs Effective | 10-30% effective utilization | `context_management/overview.md` |
| "Lost in the Middle" | U-shaped performance curve | `context_management/overview.md` |
| Model Comparison | GPT-4, Claude, Gemini windows | `context_management/overview.md` |

### Context Compression
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Compression Ratios | 4-64x with minimal degradation | `context_management/overview.md` |
| Soft Prompt Compression | ICAE, AutoCompressors | `context_management/overview.md` |
| KV Cache Optimization | CompilerKV, RAP | `context_management/overview.md` |

### Context Poisoning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Attack Vectors | Comments, README, metadata | `context_management/overview.md` |
| Detection Strategies | Repository hygiene, IDE guardrails | `context_management/overview.md` |
| Roo Code Specific | `roocode_context_poisoning_analysis.md` | Poisoning in Roo Code |

### Cross-Repository Context
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Augment Context Engine | 70%+ improvement | `augment_context_engine_mcp_analysis.md` |
| Multi-Repo Support | Service-to-service mapping | `augment_context_engine_mcp_analysis.md` |
| Monorepo Handling | Large codebase strategies | `zencoder_repo_grokking_analysis.md` |

### Context Limits
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Token Budgeting | Cost optimization | `context_management/overview.md` |
| Progressive Compaction | 85% threshold triggers | `context_management/overview.md` |
| Multi-Session Architecture | Parallel context handling | `context_management/overview.md` |

---

## Cross-Dependencies

### Context Window Dependencies
```
Context Windows
├── Model Management (model-specific limits)
├── Memory Systems (external memory extension)
├── MCP Servers (tool description consumption)
├── RAG Systems (retrieval augmentation)
└── Compression (context optimization)
```

### Context Poisoning Dependencies
```
Context Poisoning
├── Security Architecture (attack taxonomy)
├── Input Validation (sanitization)
├── Sandboxing (isolation)
├── Audit Logging (detection)
└── Human-in-the-Loop (validation)
```

### Cross-Repo Context Dependencies
```
Cross-Repo Context
├── Context Engine MCP (Augment)
├── Knowledge Graphs (relationship mapping)
├── Vector Databases (semantic search)
├── Code Intelligence (repo understanding)
└── CI/CD (multi-repo pipelines)
```

---

## Key Research Areas

### 1. RAG vs Long-Context Tradeoffs
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Key Findings:**
  - RAG: 1,250x lower cost, 45x faster
  - Long-Context: Superior accuracy for complex reasoning
  - Hybrid approaches (Self-Route, Pre-Route) emerging

### 2. Context Compression Techniques
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Methods:**
  - Context Window Extension (PI, YaRN)
  - Pre-Trained Models (AutoCompressors, RECOMP)
  - Retriever-Based (LLMChainExtractor)

### 3. Memory-Context Integration
- **Location:** `03_context_memory_intelligence/memory_systems/overview.md`
- **Architecture:**
  - Short-Term Memory (context window)
  - Long-Term Memory (vector/graph stores)
  - Write-Through Cache Pattern

### 4. Context Poisoning Mitigation
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Strategies:**
  - Repository hygiene practices
  - IDE guardrails
  - MCP output validation
  - Real-time context scanning (Kirin)

---

## Reference Documents

### Primary Sources
1. [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md) - Comprehensive context research
2. [Augment Context Engine MCP](../03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md) - Context Engine analysis
3. [Memory Systems](../03_context_memory_intelligence/memory_systems/overview.md) - Memory-context integration

### Secondary Sources
4. [Security Architecture](../01_meta_architecture/security_architecture/overview.md) - Context poisoning
5. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP context consumption
6. [Code Exploration](../04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md) - Large codebase context

---

## Navigation

- **Previous Index:** [Testing Strategies](testing_strategies.md)
- **Next Index:** [Security](security.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Context Management Cross-Cutting Index

## Overview

This index links all context management related topics across the SDLC research repository taxonomy layers, including context windows, compression, poisoning, cross-repo context, and limits.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| Security Architecture | `01_meta_architecture/security_architecture/overview.md` | Context poisoning attacks, input validation |
| Context Poisoning Analysis | `01_meta_architecture/security_architecture/roocode_context_poisoning_analysis.md` | Roo Code specific poisoning vulnerabilities |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP context consumption, tool descriptions |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent context handling, multi-agent context sharing |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| **Context Management** | `03_context_memory_intelligence/context_management/overview.md` | **Primary canonical document** - context window, compression, limits |
| Context Comparisons | `03_context_memory_intelligence/context_management/comparisons.md` | Comparative context system analysis |
| Context Engine MCP | `03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md` | Augment's semantic context engine |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Persistent context, memory-context integration |
| Memory Comparisons | `03_context_memory_intelligence/memory_systems/comparisons.md` | Memory system tradeoffs |

### Layer 4: Code Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Code Exploration | `04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md` | Large codebase context handling |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | CI context management, build context |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Test context generation |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Human context provision |

### Layer 8: Model Management

| Topic | Path | Relationship |
|-------|------|--------------|
| Model Temperature | `08_model_management/model_capability_management/roocode_temperature_analysis.md` | Context-aware temperature selection |

---

## Context Management Sub-Topics

### Context Windows
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Advertised vs Effective | 10-30% effective utilization | `context_management/overview.md` |
| "Lost in the Middle" | U-shaped performance curve | `context_management/overview.md` |
| Model Comparison | GPT-4, Claude, Gemini windows | `context_management/overview.md` |

### Context Compression
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Compression Ratios | 4-64x with minimal degradation | `context_management/overview.md` |
| Soft Prompt Compression | ICAE, AutoCompressors | `context_management/overview.md` |
| KV Cache Optimization | CompilerKV, RAP | `context_management/overview.md` |

### Context Poisoning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Attack Vectors | Comments, README, metadata | `context_management/overview.md` |
| Detection Strategies | Repository hygiene, IDE guardrails | `context_management/overview.md` |
| Roo Code Specific | `roocode_context_poisoning_analysis.md` | Poisoning in Roo Code |

### Cross-Repository Context
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Augment Context Engine | 70%+ improvement | `augment_context_engine_mcp_analysis.md` |
| Multi-Repo Support | Service-to-service mapping | `augment_context_engine_mcp_analysis.md` |
| Monorepo Handling | Large codebase strategies | `zencoder_repo_grokking_analysis.md` |

### Context Limits
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Token Budgeting | Cost optimization | `context_management/overview.md` |
| Progressive Compaction | 85% threshold triggers | `context_management/overview.md` |
| Multi-Session Architecture | Parallel context handling | `context_management/overview.md` |

---

## Cross-Dependencies

### Context Window Dependencies
```
Context Windows
├── Model Management (model-specific limits)
├── Memory Systems (external memory extension)
├── MCP Servers (tool description consumption)
├── RAG Systems (retrieval augmentation)
└── Compression (context optimization)
```

### Context Poisoning Dependencies
```
Context Poisoning
├── Security Architecture (attack taxonomy)
├── Input Validation (sanitization)
├── Sandboxing (isolation)
├── Audit Logging (detection)
└── Human-in-the-Loop (validation)
```

### Cross-Repo Context Dependencies
```
Cross-Repo Context
├── Context Engine MCP (Augment)
├── Knowledge Graphs (relationship mapping)
├── Vector Databases (semantic search)
├── Code Intelligence (repo understanding)
└── CI/CD (multi-repo pipelines)
```

---

## Key Research Areas

### 1. RAG vs Long-Context Tradeoffs
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Key Findings:**
  - RAG: 1,250x lower cost, 45x faster
  - Long-Context: Superior accuracy for complex reasoning
  - Hybrid approaches (Self-Route, Pre-Route) emerging

### 2. Context Compression Techniques
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Methods:**
  - Context Window Extension (PI, YaRN)
  - Pre-Trained Models (AutoCompressors, RECOMP)
  - Retriever-Based (LLMChainExtractor)

### 3. Memory-Context Integration
- **Location:** `03_context_memory_intelligence/memory_systems/overview.md`
- **Architecture:**
  - Short-Term Memory (context window)
  - Long-Term Memory (vector/graph stores)
  - Write-Through Cache Pattern

### 4. Context Poisoning Mitigation
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Strategies:**
  - Repository hygiene practices
  - IDE guardrails
  - MCP output validation
  - Real-time context scanning (Kirin)

---

## Reference Documents

### Primary Sources
1. [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md) - Comprehensive context research
2. [Augment Context Engine MCP](../03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md) - Context Engine analysis
3. [Memory Systems](../03_context_memory_intelligence/memory_systems/overview.md) - Memory-context integration

### Secondary Sources
4. [Security Architecture](../01_meta_architecture/security_architecture/overview.md) - Context poisoning
5. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP context consumption
6. [Code Exploration](../04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md) - Large codebase context

---

## Navigation

- **Previous Index:** [Testing Strategies](testing_strategies.md)
- **Next Index:** [Security](security.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Context Management Cross-Cutting Index

## Overview

This index links all context management related topics across the SDLC research repository taxonomy layers, including context windows, compression, poisoning, cross-repo context, and limits.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| Security Architecture | `01_meta_architecture/security_architecture/overview.md` | Context poisoning attacks, input validation |
| Context Poisoning Analysis | `01_meta_architecture/security_architecture/roocode_context_poisoning_analysis.md` | Roo Code specific poisoning vulnerabilities |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP context consumption, tool descriptions |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent context handling, multi-agent context sharing |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| **Context Management** | `03_context_memory_intelligence/context_management/overview.md` | **Primary canonical document** - context window, compression, limits |
| Context Comparisons | `03_context_memory_intelligence/context_management/comparisons.md` | Comparative context system analysis |
| Context Engine MCP | `03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md` | Augment's semantic context engine |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Persistent context, memory-context integration |
| Memory Comparisons | `03_context_memory_intelligence/memory_systems/comparisons.md` | Memory system tradeoffs |

### Layer 4: Code Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Code Exploration | `04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md` | Large codebase context handling |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | CI context management, build context |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Test context generation |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Human context provision |

### Layer 8: Model Management

| Topic | Path | Relationship |
|-------|------|--------------|
| Model Temperature | `08_model_management/model_capability_management/roocode_temperature_analysis.md` | Context-aware temperature selection |

---

## Context Management Sub-Topics

### Context Windows
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Advertised vs Effective | 10-30% effective utilization | `context_management/overview.md` |
| "Lost in the Middle" | U-shaped performance curve | `context_management/overview.md` |
| Model Comparison | GPT-4, Claude, Gemini windows | `context_management/overview.md` |

### Context Compression
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Compression Ratios | 4-64x with minimal degradation | `context_management/overview.md` |
| Soft Prompt Compression | ICAE, AutoCompressors | `context_management/overview.md` |
| KV Cache Optimization | CompilerKV, RAP | `context_management/overview.md` |

### Context Poisoning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Attack Vectors | Comments, README, metadata | `context_management/overview.md` |
| Detection Strategies | Repository hygiene, IDE guardrails | `context_management/overview.md` |
| Roo Code Specific | `roocode_context_poisoning_analysis.md` | Poisoning in Roo Code |

### Cross-Repository Context
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Augment Context Engine | 70%+ improvement | `augment_context_engine_mcp_analysis.md` |
| Multi-Repo Support | Service-to-service mapping | `augment_context_engine_mcp_analysis.md` |
| Monorepo Handling | Large codebase strategies | `zencoder_repo_grokking_analysis.md` |

### Context Limits
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Token Budgeting | Cost optimization | `context_management/overview.md` |
| Progressive Compaction | 85% threshold triggers | `context_management/overview.md` |
| Multi-Session Architecture | Parallel context handling | `context_management/overview.md` |

---

## Cross-Dependencies

### Context Window Dependencies
```
Context Windows
├── Model Management (model-specific limits)
├── Memory Systems (external memory extension)
├── MCP Servers (tool description consumption)
├── RAG Systems (retrieval augmentation)
└── Compression (context optimization)
```

### Context Poisoning Dependencies
```
Context Poisoning
├── Security Architecture (attack taxonomy)
├── Input Validation (sanitization)
├── Sandboxing (isolation)
├── Audit Logging (detection)
└── Human-in-the-Loop (validation)
```

### Cross-Repo Context Dependencies
```
Cross-Repo Context
├── Context Engine MCP (Augment)
├── Knowledge Graphs (relationship mapping)
├── Vector Databases (semantic search)
├── Code Intelligence (repo understanding)
└── CI/CD (multi-repo pipelines)
```

---

## Key Research Areas

### 1. RAG vs Long-Context Tradeoffs
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Key Findings:**
  - RAG: 1,250x lower cost, 45x faster
  - Long-Context: Superior accuracy for complex reasoning
  - Hybrid approaches (Self-Route, Pre-Route) emerging

### 2. Context Compression Techniques
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Methods:**
  - Context Window Extension (PI, YaRN)
  - Pre-Trained Models (AutoCompressors, RECOMP)
  - Retriever-Based (LLMChainExtractor)

### 3. Memory-Context Integration
- **Location:** `03_context_memory_intelligence/memory_systems/overview.md`
- **Architecture:**
  - Short-Term Memory (context window)
  - Long-Term Memory (vector/graph stores)
  - Write-Through Cache Pattern

### 4. Context Poisoning Mitigation
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Strategies:**
  - Repository hygiene practices
  - IDE guardrails
  - MCP output validation
  - Real-time context scanning (Kirin)

---

## Reference Documents

### Primary Sources
1. [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md) - Comprehensive context research
2. [Augment Context Engine MCP](../03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md) - Context Engine analysis
3. [Memory Systems](../03_context_memory_intelligence/memory_systems/overview.md) - Memory-context integration

### Secondary Sources
4. [Security Architecture](../01_meta_architecture/security_architecture/overview.md) - Context poisoning
5. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP context consumption
6. [Code Exploration](../04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md) - Large codebase context

---

## Navigation

- **Previous Index:** [Testing Strategies](testing_strategies.md)
- **Next Index:** [Security](security.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Context Management Cross-Cutting Index

## Overview

This index links all context management related topics across the SDLC research repository taxonomy layers, including context windows, compression, poisoning, cross-repo context, and limits.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| Security Architecture | `01_meta_architecture/security_architecture/overview.md` | Context poisoning attacks, input validation |
| Context Poisoning Analysis | `01_meta_architecture/security_architecture/roocode_context_poisoning_analysis.md` | Roo Code specific poisoning vulnerabilities |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP context consumption, tool descriptions |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent context handling, multi-agent context sharing |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| **Context Management** | `03_context_memory_intelligence/context_management/overview.md` | **Primary canonical document** - context window, compression, limits |
| Context Comparisons | `03_context_memory_intelligence/context_management/comparisons.md` | Comparative context system analysis |
| Context Engine MCP | `03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md` | Augment's semantic context engine |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Persistent context, memory-context integration |
| Memory Comparisons | `03_context_memory_intelligence/memory_systems/comparisons.md` | Memory system tradeoffs |

### Layer 4: Code Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Code Exploration | `04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md` | Large codebase context handling |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | CI context management, build context |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Test context generation |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Human context provision |

### Layer 8: Model Management

| Topic | Path | Relationship |
|-------|------|--------------|
| Model Temperature | `08_model_management/model_capability_management/roocode_temperature_analysis.md` | Context-aware temperature selection |

---

## Context Management Sub-Topics

### Context Windows
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Advertised vs Effective | 10-30% effective utilization | `context_management/overview.md` |
| "Lost in the Middle" | U-shaped performance curve | `context_management/overview.md` |
| Model Comparison | GPT-4, Claude, Gemini windows | `context_management/overview.md` |

### Context Compression
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Compression Ratios | 4-64x with minimal degradation | `context_management/overview.md` |
| Soft Prompt Compression | ICAE, AutoCompressors | `context_management/overview.md` |
| KV Cache Optimization | CompilerKV, RAP | `context_management/overview.md` |

### Context Poisoning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Attack Vectors | Comments, README, metadata | `context_management/overview.md` |
| Detection Strategies | Repository hygiene, IDE guardrails | `context_management/overview.md` |
| Roo Code Specific | `roocode_context_poisoning_analysis.md` | Poisoning in Roo Code |

### Cross-Repository Context
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Augment Context Engine | 70%+ improvement | `augment_context_engine_mcp_analysis.md` |
| Multi-Repo Support | Service-to-service mapping | `augment_context_engine_mcp_analysis.md` |
| Monorepo Handling | Large codebase strategies | `zencoder_repo_grokking_analysis.md` |

### Context Limits
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Token Budgeting | Cost optimization | `context_management/overview.md` |
| Progressive Compaction | 85% threshold triggers | `context_management/overview.md` |
| Multi-Session Architecture | Parallel context handling | `context_management/overview.md` |

---

## Cross-Dependencies

### Context Window Dependencies
```
Context Windows
├── Model Management (model-specific limits)
├── Memory Systems (external memory extension)
├── MCP Servers (tool description consumption)
├── RAG Systems (retrieval augmentation)
└── Compression (context optimization)
```

### Context Poisoning Dependencies
```
Context Poisoning
├── Security Architecture (attack taxonomy)
├── Input Validation (sanitization)
├── Sandboxing (isolation)
├── Audit Logging (detection)
└── Human-in-the-Loop (validation)
```

### Cross-Repo Context Dependencies
```
Cross-Repo Context
├── Context Engine MCP (Augment)
├── Knowledge Graphs (relationship mapping)
├── Vector Databases (semantic search)
├── Code Intelligence (repo understanding)
└── CI/CD (multi-repo pipelines)
```

---

## Key Research Areas

### 1. RAG vs Long-Context Tradeoffs
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Key Findings:**
  - RAG: 1,250x lower cost, 45x faster
  - Long-Context: Superior accuracy for complex reasoning
  - Hybrid approaches (Self-Route, Pre-Route) emerging

### 2. Context Compression Techniques
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Methods:**
  - Context Window Extension (PI, YaRN)
  - Pre-Trained Models (AutoCompressors, RECOMP)
  - Retriever-Based (LLMChainExtractor)

### 3. Memory-Context Integration
- **Location:** `03_context_memory_intelligence/memory_systems/overview.md`
- **Architecture:**
  - Short-Term Memory (context window)
  - Long-Term Memory (vector/graph stores)
  - Write-Through Cache Pattern

### 4. Context Poisoning Mitigation
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Strategies:**
  - Repository hygiene practices
  - IDE guardrails
  - MCP output validation
  - Real-time context scanning (Kirin)

---

## Reference Documents

### Primary Sources
1. [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md) - Comprehensive context research
2. [Augment Context Engine MCP](../03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md) - Context Engine analysis
3. [Memory Systems](../03_context_memory_intelligence/memory_systems/overview.md) - Memory-context integration

### Secondary Sources
4. [Security Architecture](../01_meta_architecture/security_architecture/overview.md) - Context poisoning
5. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP context consumption
6. [Code Exploration](../04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md) - Large codebase context

---

## Navigation

- **Previous Index:** [Testing Strategies](testing_strategies.md)
- **Next Index:** [Security](security.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Context Management Cross-Cutting Index

## Overview

This index links all context management related topics across the SDLC research repository taxonomy layers, including context windows, compression, poisoning, cross-repo context, and limits.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| Security Architecture | `01_meta_architecture/security_architecture/overview.md` | Context poisoning attacks, input validation |
| Context Poisoning Analysis | `01_meta_architecture/security_architecture/roocode_context_poisoning_analysis.md` | Roo Code specific poisoning vulnerabilities |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP context consumption, tool descriptions |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent context handling, multi-agent context sharing |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| **Context Management** | `03_context_memory_intelligence/context_management/overview.md` | **Primary canonical document** - context window, compression, limits |
| Context Comparisons | `03_context_memory_intelligence/context_management/comparisons.md` | Comparative context system analysis |
| Context Engine MCP | `03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md` | Augment's semantic context engine |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Persistent context, memory-context integration |
| Memory Comparisons | `03_context_memory_intelligence/memory_systems/comparisons.md` | Memory system tradeoffs |

### Layer 4: Code Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Code Exploration | `04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md` | Large codebase context handling |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | CI context management, build context |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Test context generation |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Human context provision |

### Layer 8: Model Management

| Topic | Path | Relationship |
|-------|------|--------------|
| Model Temperature | `08_model_management/model_capability_management/roocode_temperature_analysis.md` | Context-aware temperature selection |

---

## Context Management Sub-Topics

### Context Windows
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Advertised vs Effective | 10-30% effective utilization | `context_management/overview.md` |
| "Lost in the Middle" | U-shaped performance curve | `context_management/overview.md` |
| Model Comparison | GPT-4, Claude, Gemini windows | `context_management/overview.md` |

### Context Compression
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Compression Ratios | 4-64x with minimal degradation | `context_management/overview.md` |
| Soft Prompt Compression | ICAE, AutoCompressors | `context_management/overview.md` |
| KV Cache Optimization | CompilerKV, RAP | `context_management/overview.md` |

### Context Poisoning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Attack Vectors | Comments, README, metadata | `context_management/overview.md` |
| Detection Strategies | Repository hygiene, IDE guardrails | `context_management/overview.md` |
| Roo Code Specific | `roocode_context_poisoning_analysis.md` | Poisoning in Roo Code |

### Cross-Repository Context
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Augment Context Engine | 70%+ improvement | `augment_context_engine_mcp_analysis.md` |
| Multi-Repo Support | Service-to-service mapping | `augment_context_engine_mcp_analysis.md` |
| Monorepo Handling | Large codebase strategies | `zencoder_repo_grokking_analysis.md` |

### Context Limits
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Token Budgeting | Cost optimization | `context_management/overview.md` |
| Progressive Compaction | 85% threshold triggers | `context_management/overview.md` |
| Multi-Session Architecture | Parallel context handling | `context_management/overview.md` |

---

## Cross-Dependencies

### Context Window Dependencies
```
Context Windows
├── Model Management (model-specific limits)
├── Memory Systems (external memory extension)
├── MCP Servers (tool description consumption)
├── RAG Systems (retrieval augmentation)
└── Compression (context optimization)
```

### Context Poisoning Dependencies
```
Context Poisoning
├── Security Architecture (attack taxonomy)
├── Input Validation (sanitization)
├── Sandboxing (isolation)
├── Audit Logging (detection)
└── Human-in-the-Loop (validation)
```

### Cross-Repo Context Dependencies
```
Cross-Repo Context
├── Context Engine MCP (Augment)
├── Knowledge Graphs (relationship mapping)
├── Vector Databases (semantic search)
├── Code Intelligence (repo understanding)
└── CI/CD (multi-repo pipelines)
```

---

## Key Research Areas

### 1. RAG vs Long-Context Tradeoffs
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Key Findings:**
  - RAG: 1,250x lower cost, 45x faster
  - Long-Context: Superior accuracy for complex reasoning
  - Hybrid approaches (Self-Route, Pre-Route) emerging

### 2. Context Compression Techniques
- **Location:** `03_context_memory_intelligence/context_management/overview.md`
- **Methods:**
  - Context Window Extension (PI, YaRN)
  - Pre-Trained Models (AutoCompressors, RECOMP)
  - Retriever-Based (LLMChainExtractor)

### 3. Memory-Context Integration
- **Location:** `03_context_memory_intelligence/memory_systems/overview.md`
- **Architecture:**
  - Short-Term Memory (context window)
  - Long-Term Memory (vector/graph stores)
  - Write-Through Cache Pattern

### 4. Context Poisoning Mitigation
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Strategies:**
  - Repository hygiene practices
  - IDE guardrails
  - MCP output validation
  - Real-time context scanning (Kirin)

---

## Reference Documents

### Primary Sources
1. [Context Management Overview](../03_context_memory_intelligence/context_management/overview.md) - Comprehensive context research
2. [Augment Context Engine MCP](../03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md) - Context Engine analysis
3. [Memory Systems](../03_context_memory_intelligence/memory_systems/overview.md) - Memory-context integration

### Secondary Sources
4. [Security Architecture](../01_meta_architecture/security_architecture/overview.md) - Context poisoning
5. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP context consumption
6. [Code Exploration](../04_code_intelligence/code_exploration/zencoder_repo_grokking_analysis.md) - Large codebase context

---

## Navigation

- **Previous Index:** [Testing Strategies](testing_strategies.md)
- **Next Index:** [Security](security.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*
