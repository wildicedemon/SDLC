# Security Cross-Cutting Index

## Overview

This index links all security-related topics across the SDLC research repository taxonomy layers, including prompt injection, sandboxing, MCP isolation, credential vaulting, and supply chain security.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| **Security Architecture** | `01_meta_architecture/security_architecture/overview.md` | **Primary canonical document** - comprehensive security research |
| Security Comparisons | `01_meta_architecture/security_architecture/comparisons.md` | Security tool comparisons |
| Anti-Hallucination | `01_meta_architecture/security_architecture/anti_hallucination_overview.md` | Output validation, hallucination detection |
| Context Poisoning | `01_meta_architecture/security_architecture/roocode_context_poisoning_analysis.md` | Roo Code poisoning analysis |
| System Design | `01_meta_architecture/system_design_philosophy/spec_driven_critique_analysis.md` | Security-by-design principles |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP security, CVEs, threat model |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Multi-agent security, agent isolation |
| Kilo Auto Launch | `02_agent_orchestration/agent_system_design/kilo_auto_launch_analysis.md` | Secure agent deployment |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Context Management | `03_context_memory_intelligence/context_management/overview.md` | Context poisoning, input validation |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Memory security, data isolation |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | Pipeline security, secrets management |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Security testing, SAST/DAST |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Security approval workflows |

### Layer 8: Model Management

| Topic | Path | Relationship |
|-------|------|--------------|
| Model Capability Management | `08_model_management/model_capability_management/roocode_temperature_analysis.md` | Model behavior security |

---

## Security Domains Cross-Reference

### Prompt Injection
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Direct Injection | Jailbreak, adversarial suffixes | `security_architecture/overview.md` |
| Indirect Injection | Document poisoning, web content | `security_architecture/overview.md` |
| Multi-Turn Injection | Persistent context attacks | `security_architecture/overview.md` |
| CVEs | 30+ CVEs in 2025 | `security_architecture/overview.md` |

### Sandboxing
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Docker + gVisor | Syscall interception | `security_architecture/overview.md` |
| Kata Containers | VM-level isolation | `security_architecture/overview.md` |
| Firecracker microVMs | Full VM isolation | `security_architecture/overview.md` |
| SELinux + seccomp | Kernel policy | `security_architecture/overview.md` |

### MCP Isolation
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Confused Deputy | Authentication/authorization | `mcp_servers_overview.md` |
| Tool Poisoning | Malicious server responses | `mcp_servers_overview.md` |
| CVE Disclosures | CVE-2025-68143/4/5 | `mcp_servers_overview.md` |
| CE-MCP Security | Code execution risks | `mcp_servers_overview.md` |

### Credential Vaulting
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Secret Managers | Environment variables, rotation | `security_architecture/overview.md` |
| Backend Injection | Secret injection approach | `security_architecture/overview.md` |
| OAuth 2.1 | Per-user tokens | `security_architecture/overview.md` |
| DLP | Inline anomaly detection | `security_architecture/overview.md` |

### Supply Chain Security
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| MCP Server Vetting | Private registries | `mcp_servers_overview.md` |
| SBOM | Provenance tracking | `security_architecture/overview.md` |
| Dependency Scanning | Vulnerability detection | `security_architecture/overview.md` |
| Code Signing | Server integrity | `mcp_servers_overview.md` |

---

## Cross-Dependencies

### Defense-in-Depth Dependencies
```
Security Architecture
├── Layer 1: Input Governance (prompt injection detection)
├── Layer 2: Policy Enforcement (RBAC, DLP)
├── Layer 3: Sandboxing (container, microVM)
├── Layer 4: Output Handling (validation, filtering)
└── Layer 5: Governance (audit, monitoring)
```

### MCP Security Dependencies
```
MCP Security
├── Authentication (OAuth 2.1)
├── Authorization (per-user tokens)
├── Sandboxing (mandatory containerization)
├── Network Isolation (egress blocking)
└── Audit Logging (provenance tracking)
```

### Supply Chain Dependencies
```
Supply Chain Security
├── MCP Registries (vetted servers)
├── SBOM Generation (dependency tracking)
├── Vulnerability Scanning (CVE detection)
├── Code Signing (integrity verification)
└── Update Tracking (version pinning)
```

---

## Key Research Areas

### 1. Prompt Injection Attack Taxonomy
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Attack Types:**
  - Direct: Jailbreak, system prompt override
  - Indirect: Document poisoning, GitHub issue injection
  - Multi-Turn: Persistent context, memory poisoning

### 2. Sandboxing Approaches
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Comparison:**
  | Approach | Isolation Level | Performance | Security |
  |----------|-----------------|-------------|----------|
  | Docker | Process | High | Low |
  | Docker + gVisor | Syscall | Medium | Medium-High |
  | Kata | VM-level | Medium | High |
  | Firecracker | Full VM | Low-Medium | Very High |

### 3. MCP Threat Model
- **Location:** `02_agent_orchestration/agent_system_design/mcp_servers_overview.md`
- **Adversary Types:**
  1. Content-Injection Attackers
  2. Supply-Chain Attackers
  3. Inadvertent Agents

### 4. AI-Generated Code Security
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Key Findings:**
  - 10x more security issues in AI-generated code
  - 29.5% Python, 24.2% JavaScript contain weaknesses
  - 4x velocity, 10x vulnerabilities tradeoff

---

## Reference Documents

### Primary Sources
1. [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md) - Comprehensive security research
2. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP security analysis
3. [Context Poisoning](../01_meta_architecture/security_architecture/roocode_context_poisoning_analysis.md) - Roo Code poisoning

### Secondary Sources
4. [Anti-Hallucination](../01_meta_architecture/security_architecture/anti_hallucination_overview.md) - Output validation
5. [CI/CD & DevOps](../05_sdlc_automation/cicd_devops/overview.md) - Pipeline security
6. [Context Management](../03_context_memory_intelligence/context_management/overview.md) - Input validation

---

## Navigation

- **Previous Index:** [Context Management](context_management.md)
- **Next Index:** [Model Management](model_management.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*
