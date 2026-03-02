# Governance & Compliance Cross-Cutting Index

## Overview

This index links all governance and compliance related topics across the SDLC research repository taxonomy layers, including audit trails, SBOM, license scanning, reproducibility, and policy enforcement.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| **Security Architecture** | `01_meta_architecture/security_architecture/overview.md` | **Primary canonical document** - governance frameworks |
| Security Comparisons | `01_meta_architecture/security_architecture/comparisons.md` | Compliance tool comparisons |
| System Design | `01_meta_architecture/system_design_philosophy/spec_driven_critique_analysis.md` | Governance-by-design |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP governance, centralized registries |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent policy enforcement |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Context Management | `03_context_memory_intelligence/context_management/overview.md` | Data governance, privacy |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Data retention policies |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | Pipeline governance, audit logging |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Compliance testing |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Approval workflows, accountability |

---

## Governance & Compliance Sub-Topics

### Audit Trails
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Provenance Tracking | Cryptographic verification | `security_architecture/overview.md` |
| Action Logging | Agent activity logs | `security_architecture/overview.md` |
| Tamper-Evident Logs | Hash chains | `security_architecture/overview.md` |
| DORA Metrics | Deployment tracking | `cicd_devops/overview.md` |

### SBOM (Software Bill of Materials)
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Tracking | Supply chain visibility | `security_architecture/overview.md` |
| Vulnerability Mapping | CVE correlation | `security_architecture/overview.md` |
| MCP Server SBOM | Server provenance | `mcp_servers_overview.md` |
| Generation Tools | Automated SBOM creation | `cicd_devops/overview.md` |

### License Scanning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Licenses | License compliance | `security_architecture/overview.md` |
| MCP Server Licenses | Server license tracking | `mcp_servers_overview.md` |
| Policy Enforcement | License policy gates | `cicd_devops/overview.md` |
| Risk Assessment | License risk scoring | `security_architecture/overview.md` |

### Reproducibility
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Build Reproducibility | Deterministic builds | `cicd_devops/overview.md` |
| Environment Locking | Container pinning | `cicd_devops/overview.md` |
| Model Versioning | Model artifact tracking | `cicd_devops/overview.md` |
| Experiment Tracking | ML experiment reproducibility | `cicd_devops/overview.md` |

### Policy Enforcement
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| RBAC | Role-based access control | `security_architecture/overview.md` |
| Tool-Level Permissions | MCP tool restrictions | `mcp_servers_overview.md` |
| Pipeline Gates | CI/CD policy checks | `cicd_devops/overview.md` |
| Inline DLP | Data loss prevention | `security_architecture/overview.md` |

---

## Cross-Dependencies

### Governance Framework Dependencies
```
Governance & Compliance
├── Audit Trails (activity logging)
├── SBOM (supply chain)
├── License Scanning (compliance)
├── Reproducibility (verification)
├── Policy Enforcement (controls)
└── Human Oversight (accountability)
```

### Audit Trail Dependencies
```
Audit Trails
├── Agent Actions (logging)
├── MCP Tool Calls (provenance)
├── Code Changes (version control)
├── Deployments (CI/CD logs)
├── Security Events (monitoring)
└── Human Approvals (workflow)
```

### Compliance Dependencies
```
Compliance
├── NIST AI RMF (framework mapping)
├── ISO/IEC 42001 (AI management)
├── ISO/IEC 27001 (security)
├── GDPR (data protection)
├── SOC 2 (controls)
└── Industry-Specific (healthcare, finance)
```

---

## Key Research Areas

### 1. Framework Mappings
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Mappings:**
  | Control Category | NIST AI RMF | ISO/IEC 27001 | ISO/IEC 42001 |
  |-----------------|-------------|---------------|---------------|
  | Authentication | Govern, Manage | 5.15-5.18 | A.4.2-A.4.5 |
  | Provenance | Map, Measure | 8.15, 8.16 | A.7.5, A.6.2.8 |
  | Sandboxing | Manage | 8.20, 8.22 | A.4.2-A.4.5 |
  | Policy | Manage | 5.10, 5.34 | A.2.2, A.2.3 |

### 2. MCP Governance
- **Location:** `02_agent_orchestration/agent_system_design/mcp_servers_overview.md`
- **Controls:**
  - Centralized MCP registries
  - Server vetting pipelines
  - Version pinning
  - Audit logging

### 3. Supply Chain Security
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Components:**
  - SBOM generation
  - Dependency scanning
  - Vulnerability tracking
  - License compliance

### 4. Reproducibility Patterns
- **Location:** `05_sdlc_automation/cicd_devops/overview.md`
- **Practices:**
  - Container image pinning
  - Lock files (package, poetry)
  - Model artifact versioning
  - Environment as Code

---

## Reference Documents

### Primary Sources
1. [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md) - Governance frameworks
2. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP governance
3. [CI/CD & DevOps](../05_sdlc_automation/cicd_devops/overview.md) - Pipeline governance

### Secondary Sources
4. [Context Management](../03_context_memory_intelligence/context_management/overview.md) - Data governance
5. [Human-in-the-Loop](../07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md) - Approval workflows

---

## Navigation

- **Previous Index:** [Code Quality](code_quality.md)
- **Next Index:** [Scaling & Enterprise](scaling_enterprise.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Governance & Compliance Cross-Cutting Index

## Overview

This index links all governance and compliance related topics across the SDLC research repository taxonomy layers, including audit trails, SBOM, license scanning, reproducibility, and policy enforcement.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| **Security Architecture** | `01_meta_architecture/security_architecture/overview.md` | **Primary canonical document** - governance frameworks |
| Security Comparisons | `01_meta_architecture/security_architecture/comparisons.md` | Compliance tool comparisons |
| System Design | `01_meta_architecture/system_design_philosophy/spec_driven_critique_analysis.md` | Governance-by-design |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP governance, centralized registries |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent policy enforcement |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Context Management | `03_context_memory_intelligence/context_management/overview.md` | Data governance, privacy |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Data retention policies |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | Pipeline governance, audit logging |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Compliance testing |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Approval workflows, accountability |

---

## Governance & Compliance Sub-Topics

### Audit Trails
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Provenance Tracking | Cryptographic verification | `security_architecture/overview.md` |
| Action Logging | Agent activity logs | `security_architecture/overview.md` |
| Tamper-Evident Logs | Hash chains | `security_architecture/overview.md` |
| DORA Metrics | Deployment tracking | `cicd_devops/overview.md` |

### SBOM (Software Bill of Materials)
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Tracking | Supply chain visibility | `security_architecture/overview.md` |
| Vulnerability Mapping | CVE correlation | `security_architecture/overview.md` |
| MCP Server SBOM | Server provenance | `mcp_servers_overview.md` |
| Generation Tools | Automated SBOM creation | `cicd_devops/overview.md` |

### License Scanning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Licenses | License compliance | `security_architecture/overview.md` |
| MCP Server Licenses | Server license tracking | `mcp_servers_overview.md` |
| Policy Enforcement | License policy gates | `cicd_devops/overview.md` |
| Risk Assessment | License risk scoring | `security_architecture/overview.md` |

### Reproducibility
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Build Reproducibility | Deterministic builds | `cicd_devops/overview.md` |
| Environment Locking | Container pinning | `cicd_devops/overview.md` |
| Model Versioning | Model artifact tracking | `cicd_devops/overview.md` |
| Experiment Tracking | ML experiment reproducibility | `cicd_devops/overview.md` |

### Policy Enforcement
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| RBAC | Role-based access control | `security_architecture/overview.md` |
| Tool-Level Permissions | MCP tool restrictions | `mcp_servers_overview.md` |
| Pipeline Gates | CI/CD policy checks | `cicd_devops/overview.md` |
| Inline DLP | Data loss prevention | `security_architecture/overview.md` |

---

## Cross-Dependencies

### Governance Framework Dependencies
```
Governance & Compliance
├── Audit Trails (activity logging)
├── SBOM (supply chain)
├── License Scanning (compliance)
├── Reproducibility (verification)
├── Policy Enforcement (controls)
└── Human Oversight (accountability)
```

### Audit Trail Dependencies
```
Audit Trails
├── Agent Actions (logging)
├── MCP Tool Calls (provenance)
├── Code Changes (version control)
├── Deployments (CI/CD logs)
├── Security Events (monitoring)
└── Human Approvals (workflow)
```

### Compliance Dependencies
```
Compliance
├── NIST AI RMF (framework mapping)
├── ISO/IEC 42001 (AI management)
├── ISO/IEC 27001 (security)
├── GDPR (data protection)
├── SOC 2 (controls)
└── Industry-Specific (healthcare, finance)
```

---

## Key Research Areas

### 1. Framework Mappings
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Mappings:**
  | Control Category | NIST AI RMF | ISO/IEC 27001 | ISO/IEC 42001 |
  |-----------------|-------------|---------------|---------------|
  | Authentication | Govern, Manage | 5.15-5.18 | A.4.2-A.4.5 |
  | Provenance | Map, Measure | 8.15, 8.16 | A.7.5, A.6.2.8 |
  | Sandboxing | Manage | 8.20, 8.22 | A.4.2-A.4.5 |
  | Policy | Manage | 5.10, 5.34 | A.2.2, A.2.3 |

### 2. MCP Governance
- **Location:** `02_agent_orchestration/agent_system_design/mcp_servers_overview.md`
- **Controls:**
  - Centralized MCP registries
  - Server vetting pipelines
  - Version pinning
  - Audit logging

### 3. Supply Chain Security
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Components:**
  - SBOM generation
  - Dependency scanning
  - Vulnerability tracking
  - License compliance

### 4. Reproducibility Patterns
- **Location:** `05_sdlc_automation/cicd_devops/overview.md`
- **Practices:**
  - Container image pinning
  - Lock files (package, poetry)
  - Model artifact versioning
  - Environment as Code

---

## Reference Documents

### Primary Sources
1. [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md) - Governance frameworks
2. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP governance
3. [CI/CD & DevOps](../05_sdlc_automation/cicd_devops/overview.md) - Pipeline governance

### Secondary Sources
4. [Context Management](../03_context_memory_intelligence/context_management/overview.md) - Data governance
5. [Human-in-the-Loop](../07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md) - Approval workflows

---

## Navigation

- **Previous Index:** [Code Quality](code_quality.md)
- **Next Index:** [Scaling & Enterprise](scaling_enterprise.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Governance & Compliance Cross-Cutting Index

## Overview

This index links all governance and compliance related topics across the SDLC research repository taxonomy layers, including audit trails, SBOM, license scanning, reproducibility, and policy enforcement.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| **Security Architecture** | `01_meta_architecture/security_architecture/overview.md` | **Primary canonical document** - governance frameworks |
| Security Comparisons | `01_meta_architecture/security_architecture/comparisons.md` | Compliance tool comparisons |
| System Design | `01_meta_architecture/system_design_philosophy/spec_driven_critique_analysis.md` | Governance-by-design |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP governance, centralized registries |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent policy enforcement |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Context Management | `03_context_memory_intelligence/context_management/overview.md` | Data governance, privacy |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Data retention policies |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | Pipeline governance, audit logging |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Compliance testing |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Approval workflows, accountability |

---

## Governance & Compliance Sub-Topics

### Audit Trails
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Provenance Tracking | Cryptographic verification | `security_architecture/overview.md` |
| Action Logging | Agent activity logs | `security_architecture/overview.md` |
| Tamper-Evident Logs | Hash chains | `security_architecture/overview.md` |
| DORA Metrics | Deployment tracking | `cicd_devops/overview.md` |

### SBOM (Software Bill of Materials)
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Tracking | Supply chain visibility | `security_architecture/overview.md` |
| Vulnerability Mapping | CVE correlation | `security_architecture/overview.md` |
| MCP Server SBOM | Server provenance | `mcp_servers_overview.md` |
| Generation Tools | Automated SBOM creation | `cicd_devops/overview.md` |

### License Scanning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Licenses | License compliance | `security_architecture/overview.md` |
| MCP Server Licenses | Server license tracking | `mcp_servers_overview.md` |
| Policy Enforcement | License policy gates | `cicd_devops/overview.md` |
| Risk Assessment | License risk scoring | `security_architecture/overview.md` |

### Reproducibility
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Build Reproducibility | Deterministic builds | `cicd_devops/overview.md` |
| Environment Locking | Container pinning | `cicd_devops/overview.md` |
| Model Versioning | Model artifact tracking | `cicd_devops/overview.md` |
| Experiment Tracking | ML experiment reproducibility | `cicd_devops/overview.md` |

### Policy Enforcement
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| RBAC | Role-based access control | `security_architecture/overview.md` |
| Tool-Level Permissions | MCP tool restrictions | `mcp_servers_overview.md` |
| Pipeline Gates | CI/CD policy checks | `cicd_devops/overview.md` |
| Inline DLP | Data loss prevention | `security_architecture/overview.md` |

---

## Cross-Dependencies

### Governance Framework Dependencies
```
Governance & Compliance
├── Audit Trails (activity logging)
├── SBOM (supply chain)
├── License Scanning (compliance)
├── Reproducibility (verification)
├── Policy Enforcement (controls)
└── Human Oversight (accountability)
```

### Audit Trail Dependencies
```
Audit Trails
├── Agent Actions (logging)
├── MCP Tool Calls (provenance)
├── Code Changes (version control)
├── Deployments (CI/CD logs)
├── Security Events (monitoring)
└── Human Approvals (workflow)
```

### Compliance Dependencies
```
Compliance
├── NIST AI RMF (framework mapping)
├── ISO/IEC 42001 (AI management)
├── ISO/IEC 27001 (security)
├── GDPR (data protection)
├── SOC 2 (controls)
└── Industry-Specific (healthcare, finance)
```

---

## Key Research Areas

### 1. Framework Mappings
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Mappings:**
  | Control Category | NIST AI RMF | ISO/IEC 27001 | ISO/IEC 42001 |
  |-----------------|-------------|---------------|---------------|
  | Authentication | Govern, Manage | 5.15-5.18 | A.4.2-A.4.5 |
  | Provenance | Map, Measure | 8.15, 8.16 | A.7.5, A.6.2.8 |
  | Sandboxing | Manage | 8.20, 8.22 | A.4.2-A.4.5 |
  | Policy | Manage | 5.10, 5.34 | A.2.2, A.2.3 |

### 2. MCP Governance
- **Location:** `02_agent_orchestration/agent_system_design/mcp_servers_overview.md`
- **Controls:**
  - Centralized MCP registries
  - Server vetting pipelines
  - Version pinning
  - Audit logging

### 3. Supply Chain Security
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Components:**
  - SBOM generation
  - Dependency scanning
  - Vulnerability tracking
  - License compliance

### 4. Reproducibility Patterns
- **Location:** `05_sdlc_automation/cicd_devops/overview.md`
- **Practices:**
  - Container image pinning
  - Lock files (package, poetry)
  - Model artifact versioning
  - Environment as Code

---

## Reference Documents

### Primary Sources
1. [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md) - Governance frameworks
2. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP governance
3. [CI/CD & DevOps](../05_sdlc_automation/cicd_devops/overview.md) - Pipeline governance

### Secondary Sources
4. [Context Management](../03_context_memory_intelligence/context_management/overview.md) - Data governance
5. [Human-in-the-Loop](../07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md) - Approval workflows

---

## Navigation

- **Previous Index:** [Code Quality](code_quality.md)
- **Next Index:** [Scaling & Enterprise](scaling_enterprise.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Governance & Compliance Cross-Cutting Index

## Overview

This index links all governance and compliance related topics across the SDLC research repository taxonomy layers, including audit trails, SBOM, license scanning, reproducibility, and policy enforcement.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| **Security Architecture** | `01_meta_architecture/security_architecture/overview.md` | **Primary canonical document** - governance frameworks |
| Security Comparisons | `01_meta_architecture/security_architecture/comparisons.md` | Compliance tool comparisons |
| System Design | `01_meta_architecture/system_design_philosophy/spec_driven_critique_analysis.md` | Governance-by-design |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP governance, centralized registries |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent policy enforcement |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Context Management | `03_context_memory_intelligence/context_management/overview.md` | Data governance, privacy |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Data retention policies |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | Pipeline governance, audit logging |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Compliance testing |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Approval workflows, accountability |

---

## Governance & Compliance Sub-Topics

### Audit Trails
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Provenance Tracking | Cryptographic verification | `security_architecture/overview.md` |
| Action Logging | Agent activity logs | `security_architecture/overview.md` |
| Tamper-Evident Logs | Hash chains | `security_architecture/overview.md` |
| DORA Metrics | Deployment tracking | `cicd_devops/overview.md` |

### SBOM (Software Bill of Materials)
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Tracking | Supply chain visibility | `security_architecture/overview.md` |
| Vulnerability Mapping | CVE correlation | `security_architecture/overview.md` |
| MCP Server SBOM | Server provenance | `mcp_servers_overview.md` |
| Generation Tools | Automated SBOM creation | `cicd_devops/overview.md` |

### License Scanning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Licenses | License compliance | `security_architecture/overview.md` |
| MCP Server Licenses | Server license tracking | `mcp_servers_overview.md` |
| Policy Enforcement | License policy gates | `cicd_devops/overview.md` |
| Risk Assessment | License risk scoring | `security_architecture/overview.md` |

### Reproducibility
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Build Reproducibility | Deterministic builds | `cicd_devops/overview.md` |
| Environment Locking | Container pinning | `cicd_devops/overview.md` |
| Model Versioning | Model artifact tracking | `cicd_devops/overview.md` |
| Experiment Tracking | ML experiment reproducibility | `cicd_devops/overview.md` |

### Policy Enforcement
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| RBAC | Role-based access control | `security_architecture/overview.md` |
| Tool-Level Permissions | MCP tool restrictions | `mcp_servers_overview.md` |
| Pipeline Gates | CI/CD policy checks | `cicd_devops/overview.md` |
| Inline DLP | Data loss prevention | `security_architecture/overview.md` |

---

## Cross-Dependencies

### Governance Framework Dependencies
```
Governance & Compliance
├── Audit Trails (activity logging)
├── SBOM (supply chain)
├── License Scanning (compliance)
├── Reproducibility (verification)
├── Policy Enforcement (controls)
└── Human Oversight (accountability)
```

### Audit Trail Dependencies
```
Audit Trails
├── Agent Actions (logging)
├── MCP Tool Calls (provenance)
├── Code Changes (version control)
├── Deployments (CI/CD logs)
├── Security Events (monitoring)
└── Human Approvals (workflow)
```

### Compliance Dependencies
```
Compliance
├── NIST AI RMF (framework mapping)
├── ISO/IEC 42001 (AI management)
├── ISO/IEC 27001 (security)
├── GDPR (data protection)
├── SOC 2 (controls)
└── Industry-Specific (healthcare, finance)
```

---

## Key Research Areas

### 1. Framework Mappings
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Mappings:**
  | Control Category | NIST AI RMF | ISO/IEC 27001 | ISO/IEC 42001 |
  |-----------------|-------------|---------------|---------------|
  | Authentication | Govern, Manage | 5.15-5.18 | A.4.2-A.4.5 |
  | Provenance | Map, Measure | 8.15, 8.16 | A.7.5, A.6.2.8 |
  | Sandboxing | Manage | 8.20, 8.22 | A.4.2-A.4.5 |
  | Policy | Manage | 5.10, 5.34 | A.2.2, A.2.3 |

### 2. MCP Governance
- **Location:** `02_agent_orchestration/agent_system_design/mcp_servers_overview.md`
- **Controls:**
  - Centralized MCP registries
  - Server vetting pipelines
  - Version pinning
  - Audit logging

### 3. Supply Chain Security
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Components:**
  - SBOM generation
  - Dependency scanning
  - Vulnerability tracking
  - License compliance

### 4. Reproducibility Patterns
- **Location:** `05_sdlc_automation/cicd_devops/overview.md`
- **Practices:**
  - Container image pinning
  - Lock files (package, poetry)
  - Model artifact versioning
  - Environment as Code

---

## Reference Documents

### Primary Sources
1. [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md) - Governance frameworks
2. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP governance
3. [CI/CD & DevOps](../05_sdlc_automation/cicd_devops/overview.md) - Pipeline governance

### Secondary Sources
4. [Context Management](../03_context_memory_intelligence/context_management/overview.md) - Data governance
5. [Human-in-the-Loop](../07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md) - Approval workflows

---

## Navigation

- **Previous Index:** [Code Quality](code_quality.md)
- **Next Index:** [Scaling & Enterprise](scaling_enterprise.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Governance & Compliance Cross-Cutting Index

## Overview

This index links all governance and compliance related topics across the SDLC research repository taxonomy layers, including audit trails, SBOM, license scanning, reproducibility, and policy enforcement.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| **Security Architecture** | `01_meta_architecture/security_architecture/overview.md` | **Primary canonical document** - governance frameworks |
| Security Comparisons | `01_meta_architecture/security_architecture/comparisons.md` | Compliance tool comparisons |
| System Design | `01_meta_architecture/system_design_philosophy/spec_driven_critique_analysis.md` | Governance-by-design |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP governance, centralized registries |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent policy enforcement |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Context Management | `03_context_memory_intelligence/context_management/overview.md` | Data governance, privacy |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Data retention policies |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | Pipeline governance, audit logging |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Compliance testing |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Approval workflows, accountability |

---

## Governance & Compliance Sub-Topics

### Audit Trails
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Provenance Tracking | Cryptographic verification | `security_architecture/overview.md` |
| Action Logging | Agent activity logs | `security_architecture/overview.md` |
| Tamper-Evident Logs | Hash chains | `security_architecture/overview.md` |
| DORA Metrics | Deployment tracking | `cicd_devops/overview.md` |

### SBOM (Software Bill of Materials)
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Tracking | Supply chain visibility | `security_architecture/overview.md` |
| Vulnerability Mapping | CVE correlation | `security_architecture/overview.md` |
| MCP Server SBOM | Server provenance | `mcp_servers_overview.md` |
| Generation Tools | Automated SBOM creation | `cicd_devops/overview.md` |

### License Scanning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Licenses | License compliance | `security_architecture/overview.md` |
| MCP Server Licenses | Server license tracking | `mcp_servers_overview.md` |
| Policy Enforcement | License policy gates | `cicd_devops/overview.md` |
| Risk Assessment | License risk scoring | `security_architecture/overview.md` |

### Reproducibility
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Build Reproducibility | Deterministic builds | `cicd_devops/overview.md` |
| Environment Locking | Container pinning | `cicd_devops/overview.md` |
| Model Versioning | Model artifact tracking | `cicd_devops/overview.md` |
| Experiment Tracking | ML experiment reproducibility | `cicd_devops/overview.md` |

### Policy Enforcement
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| RBAC | Role-based access control | `security_architecture/overview.md` |
| Tool-Level Permissions | MCP tool restrictions | `mcp_servers_overview.md` |
| Pipeline Gates | CI/CD policy checks | `cicd_devops/overview.md` |
| Inline DLP | Data loss prevention | `security_architecture/overview.md` |

---

## Cross-Dependencies

### Governance Framework Dependencies
```
Governance & Compliance
├── Audit Trails (activity logging)
├── SBOM (supply chain)
├── License Scanning (compliance)
├── Reproducibility (verification)
├── Policy Enforcement (controls)
└── Human Oversight (accountability)
```

### Audit Trail Dependencies
```
Audit Trails
├── Agent Actions (logging)
├── MCP Tool Calls (provenance)
├── Code Changes (version control)
├── Deployments (CI/CD logs)
├── Security Events (monitoring)
└── Human Approvals (workflow)
```

### Compliance Dependencies
```
Compliance
├── NIST AI RMF (framework mapping)
├── ISO/IEC 42001 (AI management)
├── ISO/IEC 27001 (security)
├── GDPR (data protection)
├── SOC 2 (controls)
└── Industry-Specific (healthcare, finance)
```

---

## Key Research Areas

### 1. Framework Mappings
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Mappings:**
  | Control Category | NIST AI RMF | ISO/IEC 27001 | ISO/IEC 42001 |
  |-----------------|-------------|---------------|---------------|
  | Authentication | Govern, Manage | 5.15-5.18 | A.4.2-A.4.5 |
  | Provenance | Map, Measure | 8.15, 8.16 | A.7.5, A.6.2.8 |
  | Sandboxing | Manage | 8.20, 8.22 | A.4.2-A.4.5 |
  | Policy | Manage | 5.10, 5.34 | A.2.2, A.2.3 |

### 2. MCP Governance
- **Location:** `02_agent_orchestration/agent_system_design/mcp_servers_overview.md`
- **Controls:**
  - Centralized MCP registries
  - Server vetting pipelines
  - Version pinning
  - Audit logging

### 3. Supply Chain Security
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Components:**
  - SBOM generation
  - Dependency scanning
  - Vulnerability tracking
  - License compliance

### 4. Reproducibility Patterns
- **Location:** `05_sdlc_automation/cicd_devops/overview.md`
- **Practices:**
  - Container image pinning
  - Lock files (package, poetry)
  - Model artifact versioning
  - Environment as Code

---

## Reference Documents

### Primary Sources
1. [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md) - Governance frameworks
2. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP governance
3. [CI/CD & DevOps](../05_sdlc_automation/cicd_devops/overview.md) - Pipeline governance

### Secondary Sources
4. [Context Management](../03_context_memory_intelligence/context_management/overview.md) - Data governance
5. [Human-in-the-Loop](../07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md) - Approval workflows

---

## Navigation

- **Previous Index:** [Code Quality](code_quality.md)
- **Next Index:** [Scaling & Enterprise](scaling_enterprise.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Governance & Compliance Cross-Cutting Index

## Overview

This index links all governance and compliance related topics across the SDLC research repository taxonomy layers, including audit trails, SBOM, license scanning, reproducibility, and policy enforcement.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| **Security Architecture** | `01_meta_architecture/security_architecture/overview.md` | **Primary canonical document** - governance frameworks |
| Security Comparisons | `01_meta_architecture/security_architecture/comparisons.md` | Compliance tool comparisons |
| System Design | `01_meta_architecture/system_design_philosophy/spec_driven_critique_analysis.md` | Governance-by-design |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP governance, centralized registries |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent policy enforcement |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Context Management | `03_context_memory_intelligence/context_management/overview.md` | Data governance, privacy |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Data retention policies |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | Pipeline governance, audit logging |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Compliance testing |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Approval workflows, accountability |

---

## Governance & Compliance Sub-Topics

### Audit Trails
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Provenance Tracking | Cryptographic verification | `security_architecture/overview.md` |
| Action Logging | Agent activity logs | `security_architecture/overview.md` |
| Tamper-Evident Logs | Hash chains | `security_architecture/overview.md` |
| DORA Metrics | Deployment tracking | `cicd_devops/overview.md` |

### SBOM (Software Bill of Materials)
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Tracking | Supply chain visibility | `security_architecture/overview.md` |
| Vulnerability Mapping | CVE correlation | `security_architecture/overview.md` |
| MCP Server SBOM | Server provenance | `mcp_servers_overview.md` |
| Generation Tools | Automated SBOM creation | `cicd_devops/overview.md` |

### License Scanning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Licenses | License compliance | `security_architecture/overview.md` |
| MCP Server Licenses | Server license tracking | `mcp_servers_overview.md` |
| Policy Enforcement | License policy gates | `cicd_devops/overview.md` |
| Risk Assessment | License risk scoring | `security_architecture/overview.md` |

### Reproducibility
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Build Reproducibility | Deterministic builds | `cicd_devops/overview.md` |
| Environment Locking | Container pinning | `cicd_devops/overview.md` |
| Model Versioning | Model artifact tracking | `cicd_devops/overview.md` |
| Experiment Tracking | ML experiment reproducibility | `cicd_devops/overview.md` |

### Policy Enforcement
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| RBAC | Role-based access control | `security_architecture/overview.md` |
| Tool-Level Permissions | MCP tool restrictions | `mcp_servers_overview.md` |
| Pipeline Gates | CI/CD policy checks | `cicd_devops/overview.md` |
| Inline DLP | Data loss prevention | `security_architecture/overview.md` |

---

## Cross-Dependencies

### Governance Framework Dependencies
```
Governance & Compliance
├── Audit Trails (activity logging)
├── SBOM (supply chain)
├── License Scanning (compliance)
├── Reproducibility (verification)
├── Policy Enforcement (controls)
└── Human Oversight (accountability)
```

### Audit Trail Dependencies
```
Audit Trails
├── Agent Actions (logging)
├── MCP Tool Calls (provenance)
├── Code Changes (version control)
├── Deployments (CI/CD logs)
├── Security Events (monitoring)
└── Human Approvals (workflow)
```

### Compliance Dependencies
```
Compliance
├── NIST AI RMF (framework mapping)
├── ISO/IEC 42001 (AI management)
├── ISO/IEC 27001 (security)
├── GDPR (data protection)
├── SOC 2 (controls)
└── Industry-Specific (healthcare, finance)
```

---

## Key Research Areas

### 1. Framework Mappings
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Mappings:**
  | Control Category | NIST AI RMF | ISO/IEC 27001 | ISO/IEC 42001 |
  |-----------------|-------------|---------------|---------------|
  | Authentication | Govern, Manage | 5.15-5.18 | A.4.2-A.4.5 |
  | Provenance | Map, Measure | 8.15, 8.16 | A.7.5, A.6.2.8 |
  | Sandboxing | Manage | 8.20, 8.22 | A.4.2-A.4.5 |
  | Policy | Manage | 5.10, 5.34 | A.2.2, A.2.3 |

### 2. MCP Governance
- **Location:** `02_agent_orchestration/agent_system_design/mcp_servers_overview.md`
- **Controls:**
  - Centralized MCP registries
  - Server vetting pipelines
  - Version pinning
  - Audit logging

### 3. Supply Chain Security
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Components:**
  - SBOM generation
  - Dependency scanning
  - Vulnerability tracking
  - License compliance

### 4. Reproducibility Patterns
- **Location:** `05_sdlc_automation/cicd_devops/overview.md`
- **Practices:**
  - Container image pinning
  - Lock files (package, poetry)
  - Model artifact versioning
  - Environment as Code

---

## Reference Documents

### Primary Sources
1. [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md) - Governance frameworks
2. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP governance
3. [CI/CD & DevOps](../05_sdlc_automation/cicd_devops/overview.md) - Pipeline governance

### Secondary Sources
4. [Context Management](../03_context_memory_intelligence/context_management/overview.md) - Data governance
5. [Human-in-the-Loop](../07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md) - Approval workflows

---

## Navigation

- **Previous Index:** [Code Quality](code_quality.md)
- **Next Index:** [Scaling & Enterprise](scaling_enterprise.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Governance & Compliance Cross-Cutting Index

## Overview

This index links all governance and compliance related topics across the SDLC research repository taxonomy layers, including audit trails, SBOM, license scanning, reproducibility, and policy enforcement.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| **Security Architecture** | `01_meta_architecture/security_architecture/overview.md` | **Primary canonical document** - governance frameworks |
| Security Comparisons | `01_meta_architecture/security_architecture/comparisons.md` | Compliance tool comparisons |
| System Design | `01_meta_architecture/system_design_philosophy/spec_driven_critique_analysis.md` | Governance-by-design |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP governance, centralized registries |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent policy enforcement |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Context Management | `03_context_memory_intelligence/context_management/overview.md` | Data governance, privacy |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Data retention policies |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | Pipeline governance, audit logging |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Compliance testing |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Approval workflows, accountability |

---

## Governance & Compliance Sub-Topics

### Audit Trails
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Provenance Tracking | Cryptographic verification | `security_architecture/overview.md` |
| Action Logging | Agent activity logs | `security_architecture/overview.md` |
| Tamper-Evident Logs | Hash chains | `security_architecture/overview.md` |
| DORA Metrics | Deployment tracking | `cicd_devops/overview.md` |

### SBOM (Software Bill of Materials)
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Tracking | Supply chain visibility | `security_architecture/overview.md` |
| Vulnerability Mapping | CVE correlation | `security_architecture/overview.md` |
| MCP Server SBOM | Server provenance | `mcp_servers_overview.md` |
| Generation Tools | Automated SBOM creation | `cicd_devops/overview.md` |

### License Scanning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Licenses | License compliance | `security_architecture/overview.md` |
| MCP Server Licenses | Server license tracking | `mcp_servers_overview.md` |
| Policy Enforcement | License policy gates | `cicd_devops/overview.md` |
| Risk Assessment | License risk scoring | `security_architecture/overview.md` |

### Reproducibility
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Build Reproducibility | Deterministic builds | `cicd_devops/overview.md` |
| Environment Locking | Container pinning | `cicd_devops/overview.md` |
| Model Versioning | Model artifact tracking | `cicd_devops/overview.md` |
| Experiment Tracking | ML experiment reproducibility | `cicd_devops/overview.md` |

### Policy Enforcement
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| RBAC | Role-based access control | `security_architecture/overview.md` |
| Tool-Level Permissions | MCP tool restrictions | `mcp_servers_overview.md` |
| Pipeline Gates | CI/CD policy checks | `cicd_devops/overview.md` |
| Inline DLP | Data loss prevention | `security_architecture/overview.md` |

---

## Cross-Dependencies

### Governance Framework Dependencies
```
Governance & Compliance
├── Audit Trails (activity logging)
├── SBOM (supply chain)
├── License Scanning (compliance)
├── Reproducibility (verification)
├── Policy Enforcement (controls)
└── Human Oversight (accountability)
```

### Audit Trail Dependencies
```
Audit Trails
├── Agent Actions (logging)
├── MCP Tool Calls (provenance)
├── Code Changes (version control)
├── Deployments (CI/CD logs)
├── Security Events (monitoring)
└── Human Approvals (workflow)
```

### Compliance Dependencies
```
Compliance
├── NIST AI RMF (framework mapping)
├── ISO/IEC 42001 (AI management)
├── ISO/IEC 27001 (security)
├── GDPR (data protection)
├── SOC 2 (controls)
└── Industry-Specific (healthcare, finance)
```

---

## Key Research Areas

### 1. Framework Mappings
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Mappings:**
  | Control Category | NIST AI RMF | ISO/IEC 27001 | ISO/IEC 42001 |
  |-----------------|-------------|---------------|---------------|
  | Authentication | Govern, Manage | 5.15-5.18 | A.4.2-A.4.5 |
  | Provenance | Map, Measure | 8.15, 8.16 | A.7.5, A.6.2.8 |
  | Sandboxing | Manage | 8.20, 8.22 | A.4.2-A.4.5 |
  | Policy | Manage | 5.10, 5.34 | A.2.2, A.2.3 |

### 2. MCP Governance
- **Location:** `02_agent_orchestration/agent_system_design/mcp_servers_overview.md`
- **Controls:**
  - Centralized MCP registries
  - Server vetting pipelines
  - Version pinning
  - Audit logging

### 3. Supply Chain Security
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Components:**
  - SBOM generation
  - Dependency scanning
  - Vulnerability tracking
  - License compliance

### 4. Reproducibility Patterns
- **Location:** `05_sdlc_automation/cicd_devops/overview.md`
- **Practices:**
  - Container image pinning
  - Lock files (package, poetry)
  - Model artifact versioning
  - Environment as Code

---

## Reference Documents

### Primary Sources
1. [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md) - Governance frameworks
2. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP governance
3. [CI/CD & DevOps](../05_sdlc_automation/cicd_devops/overview.md) - Pipeline governance

### Secondary Sources
4. [Context Management](../03_context_memory_intelligence/context_management/overview.md) - Data governance
5. [Human-in-the-Loop](../07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md) - Approval workflows

---

## Navigation

- **Previous Index:** [Code Quality](code_quality.md)
- **Next Index:** [Scaling & Enterprise](scaling_enterprise.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Governance & Compliance Cross-Cutting Index

## Overview

This index links all governance and compliance related topics across the SDLC research repository taxonomy layers, including audit trails, SBOM, license scanning, reproducibility, and policy enforcement.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| **Security Architecture** | `01_meta_architecture/security_architecture/overview.md` | **Primary canonical document** - governance frameworks |
| Security Comparisons | `01_meta_architecture/security_architecture/comparisons.md` | Compliance tool comparisons |
| System Design | `01_meta_architecture/system_design_philosophy/spec_driven_critique_analysis.md` | Governance-by-design |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP governance, centralized registries |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent policy enforcement |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Context Management | `03_context_memory_intelligence/context_management/overview.md` | Data governance, privacy |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Data retention policies |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | Pipeline governance, audit logging |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Compliance testing |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Approval workflows, accountability |

---

## Governance & Compliance Sub-Topics

### Audit Trails
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Provenance Tracking | Cryptographic verification | `security_architecture/overview.md` |
| Action Logging | Agent activity logs | `security_architecture/overview.md` |
| Tamper-Evident Logs | Hash chains | `security_architecture/overview.md` |
| DORA Metrics | Deployment tracking | `cicd_devops/overview.md` |

### SBOM (Software Bill of Materials)
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Tracking | Supply chain visibility | `security_architecture/overview.md` |
| Vulnerability Mapping | CVE correlation | `security_architecture/overview.md` |
| MCP Server SBOM | Server provenance | `mcp_servers_overview.md` |
| Generation Tools | Automated SBOM creation | `cicd_devops/overview.md` |

### License Scanning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Licenses | License compliance | `security_architecture/overview.md` |
| MCP Server Licenses | Server license tracking | `mcp_servers_overview.md` |
| Policy Enforcement | License policy gates | `cicd_devops/overview.md` |
| Risk Assessment | License risk scoring | `security_architecture/overview.md` |

### Reproducibility
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Build Reproducibility | Deterministic builds | `cicd_devops/overview.md` |
| Environment Locking | Container pinning | `cicd_devops/overview.md` |
| Model Versioning | Model artifact tracking | `cicd_devops/overview.md` |
| Experiment Tracking | ML experiment reproducibility | `cicd_devops/overview.md` |

### Policy Enforcement
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| RBAC | Role-based access control | `security_architecture/overview.md` |
| Tool-Level Permissions | MCP tool restrictions | `mcp_servers_overview.md` |
| Pipeline Gates | CI/CD policy checks | `cicd_devops/overview.md` |
| Inline DLP | Data loss prevention | `security_architecture/overview.md` |

---

## Cross-Dependencies

### Governance Framework Dependencies
```
Governance & Compliance
├── Audit Trails (activity logging)
├── SBOM (supply chain)
├── License Scanning (compliance)
├── Reproducibility (verification)
├── Policy Enforcement (controls)
└── Human Oversight (accountability)
```

### Audit Trail Dependencies
```
Audit Trails
├── Agent Actions (logging)
├── MCP Tool Calls (provenance)
├── Code Changes (version control)
├── Deployments (CI/CD logs)
├── Security Events (monitoring)
└── Human Approvals (workflow)
```

### Compliance Dependencies
```
Compliance
├── NIST AI RMF (framework mapping)
├── ISO/IEC 42001 (AI management)
├── ISO/IEC 27001 (security)
├── GDPR (data protection)
├── SOC 2 (controls)
└── Industry-Specific (healthcare, finance)
```

---

## Key Research Areas

### 1. Framework Mappings
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Mappings:**
  | Control Category | NIST AI RMF | ISO/IEC 27001 | ISO/IEC 42001 |
  |-----------------|-------------|---------------|---------------|
  | Authentication | Govern, Manage | 5.15-5.18 | A.4.2-A.4.5 |
  | Provenance | Map, Measure | 8.15, 8.16 | A.7.5, A.6.2.8 |
  | Sandboxing | Manage | 8.20, 8.22 | A.4.2-A.4.5 |
  | Policy | Manage | 5.10, 5.34 | A.2.2, A.2.3 |

### 2. MCP Governance
- **Location:** `02_agent_orchestration/agent_system_design/mcp_servers_overview.md`
- **Controls:**
  - Centralized MCP registries
  - Server vetting pipelines
  - Version pinning
  - Audit logging

### 3. Supply Chain Security
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Components:**
  - SBOM generation
  - Dependency scanning
  - Vulnerability tracking
  - License compliance

### 4. Reproducibility Patterns
- **Location:** `05_sdlc_automation/cicd_devops/overview.md`
- **Practices:**
  - Container image pinning
  - Lock files (package, poetry)
  - Model artifact versioning
  - Environment as Code

---

## Reference Documents

### Primary Sources
1. [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md) - Governance frameworks
2. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP governance
3. [CI/CD & DevOps](../05_sdlc_automation/cicd_devops/overview.md) - Pipeline governance

### Secondary Sources
4. [Context Management](../03_context_memory_intelligence/context_management/overview.md) - Data governance
5. [Human-in-the-Loop](../07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md) - Approval workflows

---

## Navigation

- **Previous Index:** [Code Quality](code_quality.md)
- **Next Index:** [Scaling & Enterprise](scaling_enterprise.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Governance & Compliance Cross-Cutting Index

## Overview

This index links all governance and compliance related topics across the SDLC research repository taxonomy layers, including audit trails, SBOM, license scanning, reproducibility, and policy enforcement.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| **Security Architecture** | `01_meta_architecture/security_architecture/overview.md` | **Primary canonical document** - governance frameworks |
| Security Comparisons | `01_meta_architecture/security_architecture/comparisons.md` | Compliance tool comparisons |
| System Design | `01_meta_architecture/system_design_philosophy/spec_driven_critique_analysis.md` | Governance-by-design |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP governance, centralized registries |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent policy enforcement |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Context Management | `03_context_memory_intelligence/context_management/overview.md` | Data governance, privacy |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Data retention policies |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | Pipeline governance, audit logging |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Compliance testing |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Approval workflows, accountability |

---

## Governance & Compliance Sub-Topics

### Audit Trails
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Provenance Tracking | Cryptographic verification | `security_architecture/overview.md` |
| Action Logging | Agent activity logs | `security_architecture/overview.md` |
| Tamper-Evident Logs | Hash chains | `security_architecture/overview.md` |
| DORA Metrics | Deployment tracking | `cicd_devops/overview.md` |

### SBOM (Software Bill of Materials)
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Tracking | Supply chain visibility | `security_architecture/overview.md` |
| Vulnerability Mapping | CVE correlation | `security_architecture/overview.md` |
| MCP Server SBOM | Server provenance | `mcp_servers_overview.md` |
| Generation Tools | Automated SBOM creation | `cicd_devops/overview.md` |

### License Scanning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Licenses | License compliance | `security_architecture/overview.md` |
| MCP Server Licenses | Server license tracking | `mcp_servers_overview.md` |
| Policy Enforcement | License policy gates | `cicd_devops/overview.md` |
| Risk Assessment | License risk scoring | `security_architecture/overview.md` |

### Reproducibility
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Build Reproducibility | Deterministic builds | `cicd_devops/overview.md` |
| Environment Locking | Container pinning | `cicd_devops/overview.md` |
| Model Versioning | Model artifact tracking | `cicd_devops/overview.md` |
| Experiment Tracking | ML experiment reproducibility | `cicd_devops/overview.md` |

### Policy Enforcement
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| RBAC | Role-based access control | `security_architecture/overview.md` |
| Tool-Level Permissions | MCP tool restrictions | `mcp_servers_overview.md` |
| Pipeline Gates | CI/CD policy checks | `cicd_devops/overview.md` |
| Inline DLP | Data loss prevention | `security_architecture/overview.md` |

---

## Cross-Dependencies

### Governance Framework Dependencies
```
Governance & Compliance
├── Audit Trails (activity logging)
├── SBOM (supply chain)
├── License Scanning (compliance)
├── Reproducibility (verification)
├── Policy Enforcement (controls)
└── Human Oversight (accountability)
```

### Audit Trail Dependencies
```
Audit Trails
├── Agent Actions (logging)
├── MCP Tool Calls (provenance)
├── Code Changes (version control)
├── Deployments (CI/CD logs)
├── Security Events (monitoring)
└── Human Approvals (workflow)
```

### Compliance Dependencies
```
Compliance
├── NIST AI RMF (framework mapping)
├── ISO/IEC 42001 (AI management)
├── ISO/IEC 27001 (security)
├── GDPR (data protection)
├── SOC 2 (controls)
└── Industry-Specific (healthcare, finance)
```

---

## Key Research Areas

### 1. Framework Mappings
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Mappings:**
  | Control Category | NIST AI RMF | ISO/IEC 27001 | ISO/IEC 42001 |
  |-----------------|-------------|---------------|---------------|
  | Authentication | Govern, Manage | 5.15-5.18 | A.4.2-A.4.5 |
  | Provenance | Map, Measure | 8.15, 8.16 | A.7.5, A.6.2.8 |
  | Sandboxing | Manage | 8.20, 8.22 | A.4.2-A.4.5 |
  | Policy | Manage | 5.10, 5.34 | A.2.2, A.2.3 |

### 2. MCP Governance
- **Location:** `02_agent_orchestration/agent_system_design/mcp_servers_overview.md`
- **Controls:**
  - Centralized MCP registries
  - Server vetting pipelines
  - Version pinning
  - Audit logging

### 3. Supply Chain Security
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Components:**
  - SBOM generation
  - Dependency scanning
  - Vulnerability tracking
  - License compliance

### 4. Reproducibility Patterns
- **Location:** `05_sdlc_automation/cicd_devops/overview.md`
- **Practices:**
  - Container image pinning
  - Lock files (package, poetry)
  - Model artifact versioning
  - Environment as Code

---

## Reference Documents

### Primary Sources
1. [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md) - Governance frameworks
2. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP governance
3. [CI/CD & DevOps](../05_sdlc_automation/cicd_devops/overview.md) - Pipeline governance

### Secondary Sources
4. [Context Management](../03_context_memory_intelligence/context_management/overview.md) - Data governance
5. [Human-in-the-Loop](../07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md) - Approval workflows

---

## Navigation

- **Previous Index:** [Code Quality](code_quality.md)
- **Next Index:** [Scaling & Enterprise](scaling_enterprise.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Governance & Compliance Cross-Cutting Index

## Overview

This index links all governance and compliance related topics across the SDLC research repository taxonomy layers, including audit trails, SBOM, license scanning, reproducibility, and policy enforcement.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| **Security Architecture** | `01_meta_architecture/security_architecture/overview.md` | **Primary canonical document** - governance frameworks |
| Security Comparisons | `01_meta_architecture/security_architecture/comparisons.md` | Compliance tool comparisons |
| System Design | `01_meta_architecture/system_design_philosophy/spec_driven_critique_analysis.md` | Governance-by-design |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP governance, centralized registries |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent policy enforcement |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Context Management | `03_context_memory_intelligence/context_management/overview.md` | Data governance, privacy |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Data retention policies |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | Pipeline governance, audit logging |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Compliance testing |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Approval workflows, accountability |

---

## Governance & Compliance Sub-Topics

### Audit Trails
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Provenance Tracking | Cryptographic verification | `security_architecture/overview.md` |
| Action Logging | Agent activity logs | `security_architecture/overview.md` |
| Tamper-Evident Logs | Hash chains | `security_architecture/overview.md` |
| DORA Metrics | Deployment tracking | `cicd_devops/overview.md` |

### SBOM (Software Bill of Materials)
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Tracking | Supply chain visibility | `security_architecture/overview.md` |
| Vulnerability Mapping | CVE correlation | `security_architecture/overview.md` |
| MCP Server SBOM | Server provenance | `mcp_servers_overview.md` |
| Generation Tools | Automated SBOM creation | `cicd_devops/overview.md` |

### License Scanning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Licenses | License compliance | `security_architecture/overview.md` |
| MCP Server Licenses | Server license tracking | `mcp_servers_overview.md` |
| Policy Enforcement | License policy gates | `cicd_devops/overview.md` |
| Risk Assessment | License risk scoring | `security_architecture/overview.md` |

### Reproducibility
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Build Reproducibility | Deterministic builds | `cicd_devops/overview.md` |
| Environment Locking | Container pinning | `cicd_devops/overview.md` |
| Model Versioning | Model artifact tracking | `cicd_devops/overview.md` |
| Experiment Tracking | ML experiment reproducibility | `cicd_devops/overview.md` |

### Policy Enforcement
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| RBAC | Role-based access control | `security_architecture/overview.md` |
| Tool-Level Permissions | MCP tool restrictions | `mcp_servers_overview.md` |
| Pipeline Gates | CI/CD policy checks | `cicd_devops/overview.md` |
| Inline DLP | Data loss prevention | `security_architecture/overview.md` |

---

## Cross-Dependencies

### Governance Framework Dependencies
```
Governance & Compliance
├── Audit Trails (activity logging)
├── SBOM (supply chain)
├── License Scanning (compliance)
├── Reproducibility (verification)
├── Policy Enforcement (controls)
└── Human Oversight (accountability)
```

### Audit Trail Dependencies
```
Audit Trails
├── Agent Actions (logging)
├── MCP Tool Calls (provenance)
├── Code Changes (version control)
├── Deployments (CI/CD logs)
├── Security Events (monitoring)
└── Human Approvals (workflow)
```

### Compliance Dependencies
```
Compliance
├── NIST AI RMF (framework mapping)
├── ISO/IEC 42001 (AI management)
├── ISO/IEC 27001 (security)
├── GDPR (data protection)
├── SOC 2 (controls)
└── Industry-Specific (healthcare, finance)
```

---

## Key Research Areas

### 1. Framework Mappings
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Mappings:**
  | Control Category | NIST AI RMF | ISO/IEC 27001 | ISO/IEC 42001 |
  |-----------------|-------------|---------------|---------------|
  | Authentication | Govern, Manage | 5.15-5.18 | A.4.2-A.4.5 |
  | Provenance | Map, Measure | 8.15, 8.16 | A.7.5, A.6.2.8 |
  | Sandboxing | Manage | 8.20, 8.22 | A.4.2-A.4.5 |
  | Policy | Manage | 5.10, 5.34 | A.2.2, A.2.3 |

### 2. MCP Governance
- **Location:** `02_agent_orchestration/agent_system_design/mcp_servers_overview.md`
- **Controls:**
  - Centralized MCP registries
  - Server vetting pipelines
  - Version pinning
  - Audit logging

### 3. Supply Chain Security
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Components:**
  - SBOM generation
  - Dependency scanning
  - Vulnerability tracking
  - License compliance

### 4. Reproducibility Patterns
- **Location:** `05_sdlc_automation/cicd_devops/overview.md`
- **Practices:**
  - Container image pinning
  - Lock files (package, poetry)
  - Model artifact versioning
  - Environment as Code

---

## Reference Documents

### Primary Sources
1. [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md) - Governance frameworks
2. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP governance
3. [CI/CD & DevOps](../05_sdlc_automation/cicd_devops/overview.md) - Pipeline governance

### Secondary Sources
4. [Context Management](../03_context_memory_intelligence/context_management/overview.md) - Data governance
5. [Human-in-the-Loop](../07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md) - Approval workflows

---

## Navigation

- **Previous Index:** [Code Quality](code_quality.md)
- **Next Index:** [Scaling & Enterprise](scaling_enterprise.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*

# Governance & Compliance Cross-Cutting Index

## Overview

This index links all governance and compliance related topics across the SDLC research repository taxonomy layers, including audit trails, SBOM, license scanning, reproducibility, and policy enforcement.

**Last Updated:** February 2026  
**Index Type:** Cross-Cutting Topic Index  
**Related Overview:** [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md)

---

## Related Topics by Taxonomy Layer

### Layer 1: Meta-Architecture

| Topic | Path | Relationship |
|-------|------|--------------|
| **Security Architecture** | `01_meta_architecture/security_architecture/overview.md` | **Primary canonical document** - governance frameworks |
| Security Comparisons | `01_meta_architecture/security_architecture/comparisons.md` | Compliance tool comparisons |
| System Design | `01_meta_architecture/system_design_philosophy/spec_driven_critique_analysis.md` | Governance-by-design |

### Layer 2: Agent Orchestration

| Topic | Path | Relationship |
|-------|------|--------------|
| MCP Servers | `02_agent_orchestration/agent_system_design/mcp_servers_overview.md` | MCP governance, centralized registries |
| Agent System Design | `02_agent_orchestration/agent_system_design/overview.md` | Agent policy enforcement |

### Layer 3: Context & Memory Intelligence

| Topic | Path | Relationship |
|-------|------|--------------|
| Context Management | `03_context_memory_intelligence/context_management/overview.md` | Data governance, privacy |
| Memory Systems | `03_context_memory_intelligence/memory_systems/overview.md` | Data retention policies |

### Layer 5: SDLC Automation

| Topic | Path | Relationship |
|-------|------|--------------|
| CI/CD & DevOps | `05_sdlc_automation/cicd_devops/overview.md` | Pipeline governance, audit logging |
| Testing Architecture | `05_sdlc_automation/testing_architecture/overview.md` | Compliance testing |

### Layer 7: Human Interaction

| Topic | Path | Relationship |
|-------|------|--------------|
| Human-in-the-Loop | `07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md` | Approval workflows, accountability |

---

## Governance & Compliance Sub-Topics

### Audit Trails
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Provenance Tracking | Cryptographic verification | `security_architecture/overview.md` |
| Action Logging | Agent activity logs | `security_architecture/overview.md` |
| Tamper-Evident Logs | Hash chains | `security_architecture/overview.md` |
| DORA Metrics | Deployment tracking | `cicd_devops/overview.md` |

### SBOM (Software Bill of Materials)
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Tracking | Supply chain visibility | `security_architecture/overview.md` |
| Vulnerability Mapping | CVE correlation | `security_architecture/overview.md` |
| MCP Server SBOM | Server provenance | `mcp_servers_overview.md` |
| Generation Tools | Automated SBOM creation | `cicd_devops/overview.md` |

### License Scanning
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Dependency Licenses | License compliance | `security_architecture/overview.md` |
| MCP Server Licenses | Server license tracking | `mcp_servers_overview.md` |
| Policy Enforcement | License policy gates | `cicd_devops/overview.md` |
| Risk Assessment | License risk scoring | `security_architecture/overview.md` |

### Reproducibility
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| Build Reproducibility | Deterministic builds | `cicd_devops/overview.md` |
| Environment Locking | Container pinning | `cicd_devops/overview.md` |
| Model Versioning | Model artifact tracking | `cicd_devops/overview.md` |
| Experiment Tracking | ML experiment reproducibility | `cicd_devops/overview.md` |

### Policy Enforcement
| Aspect | Coverage | Key Documents |
|--------|----------|---------------|
| RBAC | Role-based access control | `security_architecture/overview.md` |
| Tool-Level Permissions | MCP tool restrictions | `mcp_servers_overview.md` |
| Pipeline Gates | CI/CD policy checks | `cicd_devops/overview.md` |
| Inline DLP | Data loss prevention | `security_architecture/overview.md` |

---

## Cross-Dependencies

### Governance Framework Dependencies
```
Governance & Compliance
├── Audit Trails (activity logging)
├── SBOM (supply chain)
├── License Scanning (compliance)
├── Reproducibility (verification)
├── Policy Enforcement (controls)
└── Human Oversight (accountability)
```

### Audit Trail Dependencies
```
Audit Trails
├── Agent Actions (logging)
├── MCP Tool Calls (provenance)
├── Code Changes (version control)
├── Deployments (CI/CD logs)
├── Security Events (monitoring)
└── Human Approvals (workflow)
```

### Compliance Dependencies
```
Compliance
├── NIST AI RMF (framework mapping)
├── ISO/IEC 42001 (AI management)
├── ISO/IEC 27001 (security)
├── GDPR (data protection)
├── SOC 2 (controls)
└── Industry-Specific (healthcare, finance)
```

---

## Key Research Areas

### 1. Framework Mappings
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Mappings:**
  | Control Category | NIST AI RMF | ISO/IEC 27001 | ISO/IEC 42001 |
  |-----------------|-------------|---------------|---------------|
  | Authentication | Govern, Manage | 5.15-5.18 | A.4.2-A.4.5 |
  | Provenance | Map, Measure | 8.15, 8.16 | A.7.5, A.6.2.8 |
  | Sandboxing | Manage | 8.20, 8.22 | A.4.2-A.4.5 |
  | Policy | Manage | 5.10, 5.34 | A.2.2, A.2.3 |

### 2. MCP Governance
- **Location:** `02_agent_orchestration/agent_system_design/mcp_servers_overview.md`
- **Controls:**
  - Centralized MCP registries
  - Server vetting pipelines
  - Version pinning
  - Audit logging

### 3. Supply Chain Security
- **Location:** `01_meta_architecture/security_architecture/overview.md`
- **Components:**
  - SBOM generation
  - Dependency scanning
  - Vulnerability tracking
  - License compliance

### 4. Reproducibility Patterns
- **Location:** `05_sdlc_automation/cicd_devops/overview.md`
- **Practices:**
  - Container image pinning
  - Lock files (package, poetry)
  - Model artifact versioning
  - Environment as Code

---

## Reference Documents

### Primary Sources
1. [Security Architecture Overview](../01_meta_architecture/security_architecture/overview.md) - Governance frameworks
2. [MCP Servers](../02_agent_orchestration/agent_system_design/mcp_servers_overview.md) - MCP governance
3. [CI/CD & DevOps](../05_sdlc_automation/cicd_devops/overview.md) - Pipeline governance

### Secondary Sources
4. [Context Management](../03_context_memory_intelligence/context_management/overview.md) - Data governance
5. [Human-in-the-Loop](../07_human_interaction/human_in_the_loop_systems/cline_prompts_analysis.md) - Approval workflows

---

## Navigation

- **Previous Index:** [Code Quality](code_quality.md)
- **Next Index:** [Scaling & Enterprise](scaling_enterprise.md)
- **Return to:** [Research Repository Root](../)

---

*This index is automatically cross-referenced with all taxonomy layers. Last updated: February 2026*
