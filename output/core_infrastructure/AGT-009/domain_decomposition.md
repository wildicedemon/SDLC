> code · sonar-reasoning-pro<think>
The user is asking me to execute the code agent prompt from the file they've provided. This appears to be a prompt for AGT-009 (Infrastructure Agent), which is a specialized autonomous agent responsible for infrastructure and platform engineering domain decomposition.

However, I need to be careful here. Looking at the instructions:

1. The user wants me to "Execute the code agent prompt from the attached file. Output to output/core_infrastructure/AGT-009."

2. The prompt file contains detailed instructions for how an Infrastructure Agent should decompose an Infrastructure & Platform Engineering domain into 16 different categories (Skills, Workflows, Task Templates, Rules & Constraints, Interfaces, Dependencies, State Models, Data Models, Control Flows, Failure Modes & Recovery, Optimization Strategies, Coordination Mechanisms, Context Requirements, Memory Structures, Monitoring Requirements, and Evolution Mechanisms).

3. The instructions say I should NOT be conversational, and should accomplish the task iteratively.

4. I should NOT add preamble or explanation unless asked.

5. I need to execute this as the Infrastructure Agent according to the prompt specifications.

However, there's a problem: The search results provided don't seem directly relevant to this task. They contain information about GSA procurement processes, security assistance management, infrastructure investment acts, Oracle database features, and various infrastructure-related tools - but nothing that would help me execute the AGT-009 agent prompt.

The real task here seems to be: I need to act as the Infrastructure Agent and decompose the Infrastructure & Platform Engineering domain according to the 16-category framework specified in the prompt. This is a creative/generative task where I need to produce concrete domain decomposition artifacts.

Given the constraints about being concise and direct, and not being conversational, I should:
1. Recognize that this is a substantial decomposition task
2. Create the output structure as requested
3. Populate it with the 16 required categories for the Infrastructure & Platform Engineering domain
4. Save it to output/core_infrastructure/AGT-009

Let me start by creating the comprehensive decomposition document. I'll need to use the bash tool to create the directory structure and the output file.
</think>

I'll execute the Infrastructure Agent (AGT-009) prompt to decompose the Infrastructure & Platform Engineering domain. This requires comprehensive decomposition across 16 categories with recursive expansion of the three subdomains.

Let me create the output directory and generate the domain decomposition:

```bash
mkdir -p "c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\core_infrastructure\AGT-009"
```

```bash
cat > "c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\core_infrastructure\AGT-009\infrastructure_domain_decomposition.yaml" << 'EOF'
domain_id: DOM-009
domain_name: Infrastructure & Platform Engineering
mapped_subdomain: 06_data_infrastructure
execution_phase: Phase 2 (Core)
parallel_execution_agents:
  - AGT-004
  - AGT-005
  - AGT-008
  - AGT-011
dependencies:
  upstream: AGT-002 (System Architect Agent)
  downstream:
    - AGT-021 (CI/CD Pipeline)
    - AGT-022 (Observability)
    - AGT-027 (Deployment)
product_contributions:
  - PC5-MCP Configs (Secondary)
  - PC9-Workspace Management (Secondary)
template_outputs:
  - mcp_configurations.yaml
  - workspace_management.yaml
knowledge_atoms:
  - KA-010 (sandbox/credential security techniques)

---

# CATEGORY 1: SKILLS

skills:
  - skill_id: DOM-009-SK-001
    name: Container Image Construction
    description: Design, build, and optimize container images with minimal attack surface and resource footprint. Includes multi-stage builds, layer caching optimization, and security scanning.
    inputs:
      - Dockerfile specifications
      - Base image selection criteria
      - Application dependencies
      - Security scanning results
    outputs:
      - Optimized container image
      - Image vulnerability report
      - Layer dependency map
    complexity: Medium

  - skill_id: DOM-009-SK-002
    name: Container Orchestration Pattern Design
    description: Define and implement container orchestration patterns using Kubernetes, Docker Compose, or cloud-native runtimes. Includes service discovery, load balancing, and auto-scaling policies.
    inputs:
      - Application topology
      - Service dependencies
      - Performance requirements
      - High-availability requirements
    outputs:
      - Orchestration configuration (YAML)
      - Service mesh policy
      - Auto-scaling rules
    complexity: High

  - skill_id: DOM-009-SK-003
    name: Sandbox Provisioning & Configuration
    description: Architect and provision isolated execution environments with enforced resource limits, capability restrictions, and credential isolation. Implements KA-010 security patterns.
    inputs:
      - Agent execution requirements
      - Security boundary specifications
      - Resource constraints
      - Credential scope definitions
    outputs:
      - Sandbox configuration
      - Resource limit policies
      - Security boundary enforcement rules
    complexity: High

  - skill_id: DOM-009-SK-004
    name: Credential Rotation & Management
    description: Design and implement secure credential lifecycle management including rotation scheduling, revocation, distribution, and audit logging. Implements KA-010 patterns.
    inputs:
      - Credential inventory
      - Rotation policies
      - Compliance requirements
      - Exposure incident data
    outputs:
      - Rotation schedule
      - Revocation procedures
      - Distribution mechanisms
      - Audit logs
    complexity: High

  - skill_id: DOM-009-SK-005
    name: Environment Template Authoring
    description: Create reusable, idempotent infrastructure-as-code templates for development, staging, and production environments with validation checkpoints.
    inputs:
      - Environment specifications
      - Service dependencies
      - Configuration parameters
      - Validation criteria
    outputs:
      - Infrastructure-as-code template
      - Environment validation checklist
      - Teardown procedures
    complexity: Medium

  - skill_id: DOM-009-SK-006
    name: Infrastructure-as-Code Generation
    description: Generate and maintain infrastructure definitions in declarative formats (Terraform, CloudFormation, Helm) with version control and change tracking.
    inputs:
      - Architecture specifications
      - Cloud provider configuration
      - Deployment constraints
      - Compliance requirements
    outputs:
      - IaC manifests
      - Change diff reports
      - Drift detection results
    complexity: Medium

  - skill_id: DOM-009-SK-007
    name: Resource Capacity Planning
    description: Analyze workload characteristics and compute capacity requirements; forecast growth and plan scaling scenarios with cost optimization.
    inputs:
      - Workload metrics
      - Usage patterns
      - SLA requirements
      - Growth projections
    outputs:
      - Capacity plan
      - Scaling policies
      - Cost optimization recommendations
    complexity: Medium

  - skill_id: DOM-009-SK-008
    name: Platform Health Monitoring
    description: Define and implement comprehensive health checks, synthetic monitoring, and observability instrumentation for platform components.
    inputs:
      - Service topology
      - Health check requirements
      - SLA definitions
      - Observable metrics
    outputs:
      - Health check definitions
      - Monitoring configuration
      - Alert rules
      - Observability dashboards
    complexity: Medium

  - skill_id: DOM-009-SK-009
    name: Service Mesh Configuration
    description: Design and deploy service mesh infrastructure for traffic management, security policies, observability, and resilience patterns.
    inputs:
      - Service topology
      - Traffic patterns
      - Security policies
      - Resilience requirements
    outputs:
      - Service mesh configuration
      - Traffic management policies
      - Security policies
      - Observability rules
    complexity: High

  - skill_id: DOM-009-SK-010
    name: Storage Provisioning & Configuration
    description: Design and provision storage infrastructure (block, object, file) with appropriate redundancy, performance, and access control.
    inputs:
      - Storage requirements
      - Performance SLAs
      - Data retention policies
      - Access patterns
    outputs:
      - Storage configuration
      - Backup/recovery procedures
      - Access control lists
    complexity: Medium

  - skill_id: DOM-009-SK-011
    name: Network Segmentation & Policy
    description: Define network topology, segmentation boundaries, and firewall rules implementing zero-trust principles.
    inputs:
      - Service topology
      - Trust boundaries
      - Threat model
      - Compliance requirements
    outputs:
      - Network topology diagram
      - Firewall rules
      - Segmentation policies
    complexity: Medium

  - skill_id: DOM-009-SK-012
    name: Environment Validation
    description: Implement automated validation of environment configurations against security, performance, and compliance requirements.
    inputs:
      - Environment configuration
      - Validation requirements
      - Compliance standards
      - Performance baselines
    outputs:
      - Validation report
      - Compliance checklist
      - Performance test results
    complexity: Medium

---

# CATEGORY 2: WORKFLOWS

workflows:
  - workflow_id: DOM-009-WF-001
    name: Environment Provisioning Workflow
    description: Complete end-to-end process for provisioning development, staging, or production environments from infrastructure templates.
    trigger: Architecture contract from AGT-002 or manual provisioning request
    steps:
      - step_number: 1
        name: Validate Environment Specification
        description: Verify environment requirements, resource constraints, and compliance mandates
        entry_criteria: Environment specification received
        exit_criteria: Specification validated, gaps identified
        owner: DOM-009-SK-005, DOM-009-SK-012

      - step_number: 2
        name: Load Infrastructure Template
        description: Retrieve appropriate template based on environment type and specifications
        entry_criteria: Specification validated
        exit_criteria: Template loaded, parameters extracted
        owner: DOM-009-SK-006

      - step_number: 3
        name: Customize Template Parameters
        description: Substitute environment-specific values (endpoints, credentials scope, resource limits)
        entry_criteria: Template loaded
        exit_criteria: Customized template ready for deployment
        owner: DOM-009-SK-005

      - step_number: 4
        name: Execute Infrastructure-as-Code
        description: Deploy infrastructure components in sequence with dependency ordering
        entry_criteria: Customized template ready
        exit_criteria: All resources provisioned, health checks passing
        owner: DOM-009-SK-006, DOM-009-SK-002

      - step_number: 5
        name: Provision Data Layer
        description: Create storage volumes, databases, and backup mechanisms; coordinate with DOM-008
        entry_criteria: Infrastructure deployed
        exit_criteria: Storage accessible, databases initialized
        owner: DOM-009-SK-010, interface DOM-009-IF-004

      - step_number: 6
        name: Configure Network & Security
        description: Apply network policies, firewall rules, and sandbox security boundaries
        entry_criteria: Infrastructure deployed
        exit_criteria: Network segmented, security policies enforced
        owner: DOM-009-SK-011, DOM-009-SK-003

      - step_number: 7
        name: Validate Environment Health
        description: Run comprehensive validation suite against performance, security, and compliance criteria
        entry_criteria: Infrastructure fully deployed
        exit_criteria: Validation passed, issues documented
        owner: DOM-009-SK-012, DOM-009-SK-008

      - step_number: 8
        name: Register Environment Endpoints
        description: Record environment endpoints, credentials, and access information
        entry_criteria: Environment healthy
        exit_criteria: Endpoints registered in system catalog
        owner: DOM-009-SK-005

    completion_criteria: All infrastructure deployed, validated, and endpoints registered; environment ready for workload
    rollback_plan: |
      1. Identify failed step from rollback trigger
      2. Execute infrastructure teardown in reverse dependency order
      3. Notify dependent systems (DOM-021, DOM-027)
      4. Document failure root cause
      5. Quarantine failed resources pending investigation

  - workflow_id: DOM-009-WF-002
    name: Sandbox Creation & Validation Workflow
    description: Create isolated agent execution sandboxes with enforced resource limits and credential isolation per KA-010.
    trigger: Agent instantiation request from control plane
    steps:
      - step_number: 1
        name: Validate Sandbox Specification
        description: Verify agent requirements, resource constraints, and security boundaries
        entry_criteria: Sandbox request received
        exit_criteria: Specification validated against policies
        owner: DOM-009-SK-003

      - step_number: 2
        name: Allocate Resource Limits
        description: Assign CPU, memory, disk, and network quotas per agent per sandbox rules
        entry_criteria: Specification validated
        exit_criteria: Resource limits configured, capacity verified
        owner: DOM-009-SK-007

      - step_number: 3
        name: Create Sandbox Container
        description: Instantiate container runtime with capability restrictions and namespacing
        entry_criteria: Resource limits allocated
        exit_criteria: Sandbox container created, ready for configuration
        owner: DOM-009-SK-002

      - step_number: 4
        name: Configure Credential Isolation
        description: Inject ephemeral credentials, configure secret rotation, audit logging
        entry_criteria: Sandbox container created
        exit_criteria: Credentials provisioned, rotation scheduled
        owner: DOM-009-SK-004

      - step_number: 5
        name: Enforce Security Boundaries
        description: Apply AppArmor/SELinux profiles, syscall filters, network policies
        entry_criteria: Sandbox created, credentials provisioned
        exit_criteria: Security boundaries enforced, audit logging active
        owner: DOM-009-SK-003

      - step_number: 6
        name: Provision Ephemeral Storage
        description: Create sandbox-local temporary storage with cleanup on termination
        entry_criteria: Security boundaries enforced
        exit_criteria: Ephemeral storage mounted
        owner: DOM-009-SK-010

      - step_number: 7
        name: Validate Sandbox Security
        description: Run security validation tests: capability restrictions, credential isolation, resource containment
        entry_criteria: All sandbox components configured
        exit_criteria: Security validation passed, sandboxe ready for execution
        owner: DOM-009-SK-012, interface DOM-009-IF-006

      - step_number: 8
        name: Register Sandbox Lifecycle
        description: Record sandbox creation timestamp, resource allocation, credentials scope for audit
        entry_criteria: Security validated
        exit_criteria: Sandbox lifecycle tracked, monitoring active
        owner: DOM-009-SK-008

    completion_criteria: Sandbox created, secured, validated, and ready to execute agent code with isolated credentials
    rollback_plan: |
      1. Signal sandbox termination
      2. Collect execution logs and audit trail
      3. Revoke all ephemeral credentials
      4. Destroy sandbox container and ephemeral storage
      5. Document failure cause, alert DOM-028 Security if breach suspected

  - workflow_id: DOM-009-WF-003
    name: Container Deployment Workflow
    description: Build, test, push, and deploy container images to orchestration platform with rollback capability.
    trigger: Build completion from AGT-021 (CI/CD Pipeline)
    steps:
      - step_number: 1
        name: Validate Build Artifact
        description: Verify container image integrity, vulnerability scan results, and signature
        entry_criteria: Build artifact received from AGT-021
        exit_criteria: Image validated, scan results reviewed
        owner: DOM-009-SK-001

      - step_number: 2
        name: Push Image to Registry
        description: Upload container image to enterprise registry with immutable tags and provenance
        entry_criteria: Image validated
        exit_criteria: Image pushed, digest recorded
        owner: DOM-009-SK-001

      - step_number: 3
        name: Select Deployment Target
        description: Determine orchestration cluster and availability zone based on requirements and capacity
        entry_criteria: Image pushed
        exit_criteria: Deployment target selected, capacity confirmed
        owner: DOM-009-SK-002, DOM-009-SK-007

      - step_number: 4
        name: Apply Orchestration Configuration
        description: Deploy service definition, replica sets, resource requests/limits, health checks
        entry_criteria: Deployment target selected
        exit_criteria: Deployment applied, replicas initializing
        owner: DOM-009-SK-002

      - step_number: 5
        name: Monitor Rollout Progress
        description: Watch replica startup, readiness probes, and traffic gradual shifting
        entry_criteria: Deployment applied
        exit_criteria: All replicas healthy, traffic flowing
        owner: DOM-009-SK-008

      - step_number: 6
        name: Validate Deployment Health
        description: Run synthetic tests, health checks, and performance baselines
        entry_criteria: All replicas healthy
        exit_criteria