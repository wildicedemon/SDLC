# MCP Servers Cross-Cutting Index

## Overview

This index links all Model Context Protocol (MCP) related topics across the SDLC research repository taxonomy layers.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [MCP Servers Overview](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| Security Architecture | `01_meta_architecture/security_architecture/overview.md` | MCP security threat model, CVE disclosures (CVE-2025-68143/4/5), supply chain risks |
| System Design Philosophy | `01_meta_architecture/system_design_philosophy/spec_driven_critique_analysis.md` | Spec-driven approach to MCP server design |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| **MCP Servers Overview** | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | **Primary canonical document** - comprehensive MCP analysis |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | MCP as tool-use layer in multi-agent systems |
| Agent System Comparisons | `02_agent_orchestration/agent_system_design/comparisons.md` | Comparative analysis of MCP implementations |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Context Engine MCP Analysis | `03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md` | Augment's Context Engine MCP with 70%+ performance improvement |
| Context Management | `03_context_memory_intelligence/context_management/overview.md` | MCP's relationship to long-context windows and RAG |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | MCP integration with persistent memory |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | MCP server deployment patterns, CI/CD integration |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | MCP tool testing, validation pipelines |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Cline Prompts Analysis | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Human-in-the-loop for MCP tool approval |

### Layer 8: Model Management

| Topic | Path | Relationship |
|-------|------|--------------|
| Model Temperature Analysis | `08_model_management/model_capability_management/roocode_temperature_analysis.md` | MCP tool selection accuracy |

---

## Cross-Dependencies

### MCP Security Dependencies
```
MCP Servers
├── Security Architecture (prompt injection via MCP)
├── Context Poisoning (malicious tool descriptions)
├── Sandboxing (MCP server isolation)
└── Supply Chain (unverified MCP servers)
```

### MCP Context Dependencies
```
MCP Servers
├── Context Window (tool descriptions consume tokens)
├── Context Engine (Augment MCP for semantic search)
├── Memory Systems (MCP as memory interface)
└── RAG Systems (MCP vs. RAG tradeoffs)
```

### MCP Orchestration Dependencies
```
MCP Servers
├── Agent Architecture (MCP as tool layer)
├── Multi-Agent Systems (cross-agent MCP sharing)
├── Human-in-the-Loop (MCP tool approval)
└── CI/CD (MCP server deployment)
```

---

## Key Research Areas

### 1. MCP Selection & Evaluation
- **Location:** `02_agent_orchestration/agent_system_design/mcp_servers_overview.md`
- **Key Topics:**
  - Tool description quality (97.1% contain "smells")
  - Server evaluation criteria
  - CE-MCP (Code Execution MCP) architecture
  - Performance tradeoffs (token waste vs. capability)

### 2. MCP Privilege Isolation
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Key Topics:**
  - Confused deputy attacks
  - OAuth 2.1 authentication
  - Per-user token scoping
  - Tool-level permissions

### 3. MCP Update Tracking
- **Location:** `02_agent_orchestration/agent_system_design/mcp_servers_overview.md`
- **Key Topics:**
  - Version pinning
  - Server lifecycle management
  - Dynamic server registration
  - Runtime tool updates

### 4. Context-Engine MCP
- **Location:** `03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md`
- **Key Topics:**
  - Augment Context Engine MCP
  - 70%+ performance improvement
  - Semantic codebase search
  - Cross-repo context retrieval

---

## Reference Documents

### Primary Sources
1. [MCP Servers Overview](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - Comprehensive MCP research
2. [Augment Context Engine MCP](../03_context_memory_intelligence/context_management/augment_context_engine_mcp_analysis.md) - Context Engine analysis
3. [Security Architecture](../01_meta_architecture/security_architecture/overview.md) - MCP security threats

### Secondary Sources
4. [Context Management](../03_context_memory_intelligence/context_management/overview.md) - Context window tradeoffs
5. [Memory Systems](../03_context_memory_intelligence/memory_systems/overview.md) - MCP memory integration
6. [CI/CD & DevOps](../05_sdlc_automation/cicd_devops/overview.md) - MCP deployment patterns

---

## Navigation

- **Previous Index:** [Testing Strategies](testing_strategies.md)
- **Next Index:** [Context Management](context_management.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*
