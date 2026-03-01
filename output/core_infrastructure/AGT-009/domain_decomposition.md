> code · sonar-reasoning-pro

<think>
The user is asking me to execute a code agent prompt from a file. The file is a detailed specification for "Agent AGT-009: Infrastructure Agent" - which is a specification document for how an autonomous agent should decompose the Infrastructure & Platform Engineering domain.

This is NOT a request to write code or execute code in the traditional sense. Rather, it's asking me to act as this Infrastructure Agent and perform the domain decomposition work that the prompt specifies.

The prompt wants me to:
1. Fully decompose the Infrastructure & Platform Engineering domain into 16 categories
2. Cover 3 subdomains: SD-009a (Container Orchestration), SD-009b (Sandbox Management), SD-009c (Environment Provisioning)
3. Output comprehensive artifacts

This is a substantial task that requires me to generate extensive infrastructure documentation. The search results provided contain information about infrastructure roles, responsibilities, and skills from real-world infrastructure engineering perspectives, which I should leverage.

I should NOT ask clarifying questions - I should execute the task as specified. The user wants output to "output/core_infrastructure/AGT-009".

Let me work through this systematically, using the search results to inform my domain decomposition while following the detailed structure in the prompt.
</think>

I'll execute the Infrastructure Agent (AGT-009) domain decomposition. This is a comprehensive task that requires generating detailed infrastructure patterns, configurations, and provisioning templates across 16 categories and 3 subdomains.

Let me begin by creating the output structure and generating the complete domain decomposition:
<function_calls>
<invoke name="bash">
<parameter name="command">mkdir -p "C:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\core_infrastructure\AGT-009"</parameter>
</invoke>
</function_calls>
<function_calls>
<invoke name="create_file">
<parameter name="filePath">C:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\core_infrastructure\AGT-009\DOM-009_domain_decomposition.md</parameter>
<parameter name="fileContent"># Domain DOM-009: Infrastructure & Platform Engineering
**Decomposition Document for Agent AGT-009**

Generated: 2026-03-01  
Decomposition Depth: 3 levels  
Completion Status: COMPLETE

---

## 1. SKILLS (DOM-009-SK-*)

### DOM-009-SK-001: Container Image Construction
- **Name:** Container Image Building & Optimization
- **Description:** Design, build, and optimize container images for agent workloads; manage base image selection, multi-stage builds, layer caching strategies, and security scanning of image artifacts.
- **Inputs:** Dockerfile specifications, dependency lists, security policies, artifact repositories
- **Outputs:** Optimized container images, image manifests, SBOM reports, vulnerability assessments
- **Complexity:** Medium
- **Subdomain:** SD-009a

### DOM-009-SK-002: Container Registry Management
- **Name:** Container Registry Administration
- **Description:** Manage container image registries including access control, image versioning, garbage collection, replication policies, and registry security.
- **Inputs:** Registry credentials, replication rules, retention policies, security configurations
- **Outputs:** Configured registries, replication status, audit logs, policy enforcement reports
- **Complexity:** Medium
- **Subdomain:** SD-009a

### DOM-009-SK-003: Kubernetes Orchestration
- **Name:** Kubernetes Cluster Design & Management
- **Description:** Design, provision, and manage Kubernetes clusters including node configuration, network policies, storage classes, RBAC, and cluster lifecycle management.
- **Inputs:** Cluster specifications, workload requirements, infrastructure constraints, security policies
- **Outputs:** Kubernetes manifests, cluster configurations, resource quotas, policy definitions
- **Complexity:** High
- **Subdomain:** SD-009a

### DOM-009-SK-004: Service Mesh Configuration
- **Name:** Service Mesh Pattern Implementation
- **Description:** Implement service mesh patterns (Istio, Linkerd) for traffic management, observability, security policies, and circuit breaking across agent microservices.
- **Inputs:** Service topology, traffic policies, security requirements, observability goals
- **Outputs:** VirtualService definitions, DestinationRule configs, AuthorizationPolicy specs
- **Complexity:** High
- **Subdomain:** SD-009a

### DOM-009-SK-005: Sandbox Provisioning
- **Name:** Agent Execution Sandbox Creation
- **Description:** Provision isolated execution environments for agents with resource limits, network isolation, filesystem restrictions, and capability constraints per KA-010.
- **Inputs:** Agent specifications, resource requirements, isolation requirements, security policies
- **Outputs:** Sandbox configurations, cgroup definitions, seccomp profiles, namespace configs
- **Complexity:** High
- **Subdomain:** SD-009b

### DOM-009-SK-006: Credential Rotation & Management
- **Name:** Secrets Lifecycle & Rotation Automation
- **Description:** Implement credential lifecycle management including generation, rotation, revocation, and secure distribution to sandboxes per KA-010; prevent credential exposure in logs/output.
- **Inputs:** Secret policies, rotation schedules, credential templates, audit requirements
- **Outputs:** Rotation schedules, secret templates, audit trails, distribution configs
- **Complexity:** High
- **Subdomain:** SD-009b

### DOM-009-SK-007: Resource Isolation & Enforcement
- **Name:** Multi-level Resource Constraint Management
- **Description:** Enforce resource isolation at multiple levels (CPU, memory, disk I/O, network) using cgroups, namespaces, and kernel capabilities to prevent sandbox escape and resource exhaustion.
- **Inputs:** Resource limits, isolation levels, constraint policies, workload profiles
- **Outputs:** Isolation policies, constraint configurations, monitoring rules, enforcement logs
- **Complexity:** High
- **Subdomain:** SD-009b

### DOM-009-SK-008: Environment Template Authoring
- **Name:** Infrastructure-as-Code Pattern Development
- **Description:** Author reusable, idempotent IaC templates (Terraform, Helm, Kustomize) for dev/staging/production environments with validation and drift detection.
- **Inputs:** Environment specifications, infrastructure requirements, compliance policies, resource baselines
- **Outputs:** IaC modules, Helm charts, Kustomize overlays, validation scripts
- **Complexity:** Medium
- **Subdomain:** SD-009c

### DOM-009-SK-009: Infrastructure-as-Code Generation
- **Name:** Declarative Infrastructure Specification & Synthesis
- **Description:** Generate IaC configurations programmatically from high-level domain specifications; ensure generated code follows conventions and passes validation.
- **Inputs:** Domain specifications, architecture contracts, policy definitions, environmental variables
- **Outputs:** Validated IaC code, syntax-checked manifests, deployment-ready configurations
- **Complexity:** Medium
- **Subdomain:** SD-009c

### DOM-009-SK-010: Environment Validation
- **Name:** Infrastructure Readiness Assessment
- **Description:** Validate provisioned environments against requirements including connectivity, resource availability, security posture, and configuration compliance.
- **Inputs:** Environment configs, validation rules, compliance policies, baseline expectations
- **Outputs:** Validation reports, readiness status, gap identification, remediation recommendations
- **Complexity:** Medium
- **Subdomain:** SD-009c

### DOM-009-SK-011: Environment Teardown & Cleanup
- **Name:** Infrastructure Deprovisioning & State Cleanup
- **Description:** Safely destroy ephemeral environments, manage state cleanup, verify complete resource deallocation, and audit teardown operations.
- **Inputs:** Environment state, cleanup policies, audit requirements, dependency graphs
- **Outputs:** Cleanup logs, state confirmation, audit records, resource allocation reports
- **Complexity:** Medium
- **Subdomain:** SD-009c

### DOM-009-SK-012: Resource Capacity Planning
- **Name:** Workload-Driven Capacity Forecasting
- **Description:** Analyze agent workload patterns, forecast resource requirements, identify scaling thresholds, and recommend capacity adjustments.
- **Inputs:** Workload metrics, historical usage, growth projections, cost constraints
- **Outputs:** Capacity forecasts, scaling recommendations, cost projections, threshold configurations
- **Complexity:** Medium
- **Subdomain:** SD-009c

### DOM-009-SK-013: Platform Health Monitoring
- **Name:** Infrastructure Observability & Metrics Collection
- **Description:** Design monitoring infrastructure for platform components including metrics collection, alerting, log aggregation, and health check implementations.
- **Inputs:** Infrastructure topology, monitoring policies, alert definitions, baseline thresholds
- **Outputs:** Monitoring configs, alert rules, dashboard definitions, collection specifications
- **Complexity:** Medium
- **Subdomain:** SD-009a/b/c

### DOM-009-SK-014: Disaster Recovery Planning
- **Name:** Backup & Recovery Strategy Development
- **Description:** Design and implement disaster recovery strategies including backup policies, recovery time objectives (RTO), recovery point objectives (RPO), and failover procedures.
- **Inputs:** Infrastructure state, RTO/RPO requirements, failure scenarios, compliance policies
- **Outputs:** DR plans, backup policies, recovery procedures, failover configurations
- **Complexity:** High
- **Subdomain:** SD-009c

### DOM-009-SK-015: Infrastructure Security Hardening
- **Name:** Security Posture Enhancement & Compliance
- **Description:** Apply security hardening practices including vulnerability patching, least privilege enforcement, network segmentation, and compliance validation.
- **Inputs:** Infrastructure state, security policies, compliance frameworks, threat landscape
- **Outputs:** Hardening guidelines, policy implementations, security audit reports, compliance documentation
- **Complexity:** High
- **Subdomain:** SD-009b/c

### DOM-009-SK-016: Docker Compose Configuration
- **Name:** Multi-container Orchestration for Development
- **Description:** Design Docker Compose configurations for development and testing environments with service dependencies, networking, volumes, and environment variables.
- **Inputs:** Service specifications, dependency graphs, port mappings, environment requirements
- **Outputs:** docker-compose.yaml files, override configurations, startup scripts
- **Complexity:** Low
- **Subdomain:** SD-009a

---

## 2. WORKFLOWS (DOM-009-WF-*)

### DOM-009-WF-001: Environment Provisioning Workflow
- **Workflow ID:** DOM-009-WF-001
- **Name:** Complete Environment Setup & Validation
- **Trigger:** Architecture contract received from AGT-002; deployment request from AGT-027
- **Steps:**
  1. [ENTRY] Receive environment specification and IaC requirements
  2. [VALIDATE] Parse and validate IaC templates against schema and policies
  3. [PLAN] Execute infrastructure plan to identify changes
  4. [APPROVE] Wait for deployment approval (if required by policy)
  5. [APPLY] Execute IaC to provision infrastructure
  6. [VERIFY] Verify resource creation and connectivity
  7. [CONFIGURE] Apply configuration management and post-deployment scripts
  8. [TEST] Run environment validation tests
  9. [REGISTER] Register environment in inventory and observability systems
  10. [NOTIFY] Send environment ready notification to AGT-021, AGT-022, AGT-027
  11. [EXIT] Environment operational and ready for workload deployment
- **Completion Criteria:**
  - All IaC resources created successfully
  - All validation tests pass
  - Environment registered in observability system
  - Monitoring and alerting configured
  - Deployment notification sent
- **Rollback Plan:**
  - If validation fails at step 8: destroy environment, alert operations team
  - If deployment fails at step 5: apply destroy plan, investigate root cause
  - If configuration fails at step 7: restore from baseline, rollback changes

### DOM-009-WF-002: Sandbox Creation & Validation Workflow
- **Workflow ID:** DOM-009-WF-002
- **Name:** Secure Agent Execution Sandbox Setup (KA-010)
- **Trigger:** Agent instantiation request; new workload deployment
- **Steps:**
  1. [ENTRY] Receive agent requirements and security constraints
  2. [VALIDATE] Validate agent specifications against sandbox policies
  3. [ALLOCATE] Reserve resources from capacity pool
  4. [CREATE] Create Linux namespaces (PID, NET, IPC, MNT, UTS)
  5. [CONFIGURE] Configure cgroups with resource limits (CPU, memory, I/O)
  6. [SECURE] Apply seccomp profile and AppArmor/SELinux policies
  7. [INJECT] Inject credentials (rotated secrets) to sandbox via secure channel
  8. [VALIDATE_ISOLATION] Verify isolation using capability tests
  9. [MONITOR] Establish monitoring of sandbox resource usage
  10. [HANDOFF] Pass sandbox handle to agent execution layer
  11. [EXIT] Sandbox ready for agent execution
- **Completion Criteria:**
  - All namespaces created and isolated
  - Resource limits enforced and verified
  - Security policies applied and tested
  - No sandbox escape vectors present
  - Monitoring active and alerting configured
- **Rollback Plan:**
  - If isolation fails: destroy sandbox, escalate to security team
  - If credential injection fails: destroy sandbox, never execute agent
  - If monitoring fails: suspend sandbox, investigate before resumption

### DOM-009-WF-003: Container Deployment Workflow
- **Workflow ID:** DOM-009-WF-003
- **Name:** Container Image Build, Push, & Deploy
- **Trigger:** New agent version released; container update request
- **Steps:**
  1. [ENTRY] Receive Dockerfile and build specifications
  2. [VALIDATE] Validate Dockerfile against security policies
  3. [BUILD] Build container image with BuildKit
  4. [SCAN] Scan image for vulnerabilities and policy violations
  5. [SIGN] Sign image with cosign/notary
  6. [PUSH] Push image to registry with metadata
  7. [UPDATE] Update Kubernetes deployment manifest
  8. [DEPLOY] Apply manifest to cluster (rolling update)
  9. [VERIFY] Verify new pods are healthy
  10. [DRAIN_OLD] Gracefully drain old pod instances
  11. [MONITOR] Watch deployment metrics for anomalies
  12. [EXIT] Deployment complete, new version live
- **Completion Criteria:**
  - Image built, scanned, signed, and pushed
  - No high/critical vulnerabilities found
  - All pods healthy and serving traffic
  - Rollout complete with zero downtime
  - Metrics show stable performance
- **Rollback Plan:**
  - If vulnerability scan fails: block push to registry, alert team
  - If deployment fails: automatic rollback to previous version
  - If new version unstable: trigger canary rollback

### DOM-009-WF-004: Infrastructure Scaling Workflow
- **Workflow ID:** DOM-009-WF-004
- **Name:** Dynamic Resource Scaling & Capacity Adjustment
- **Trigger:** Capacity threshold exceeded; load increase detected; manual scaling request
- **Steps:**
  1. [ENTRY] Receive scaling trigger (metric threshold, manual request)
  2. [ANALYZE] Analyze current load and forecast demand
  3. [PLAN] Calculate required additional resources
  4. [VALIDATE] Validate availability of resources and capacity
  5. [PROVISION] Provision new infrastructure resources (nodes/storage)
  6. [INITIALIZE] Initialize and join new nodes to cluster
  7. [CONFIGURE] Apply configuration and labels to new nodes
  8. [REBALANCE] Rebalance workloads across new infrastructure
  9. [MONITOR] Monitor metrics during rebalancing
  10. [VERIFY] Verify all workloads healthy on new resources
  11. [OPTIMIZE] Update capacity plans and autoscaling policies
  12. [EXIT] Scaling complete, system at target capacity
- **Completion Criteria:**
  - New resources provisioned and healthy
  - Workloads rebalanced with no service interruption
  - Monitoring shows improved resource utilization
  - Autoscaling policies updated
- **Rollback Plan:**
  - If new resources unhealthy: mark as unschedulable, investigate
  - If rebalancing fails: manual intervention, preserve existing workloads

### DOM-009-WF-005: Credential Rotation Workflow
- **Workflow ID:** DOM-009-WF-005
- **Name:** Automated Secret Lifecycle Management (KA-010)
- **Trigger:** Rotation schedule elapsed; credential compromise detected; policy change
- **Steps:**
  1. [ENTRY] Receive rotation trigger (scheduled or emergency)
  2. [VALIDATE] Validate rotation policies and compliance requirements
  3. [GENERATE] Generate new credentials with secure entropy
  4. [BACKUP] Backup old credentials (encrypted, audit logged)
  5. [DISTRIBUTE_NEW] Distribute new credentials to all consuming services
  6. [VERIFY] Verify all services switched to new credentials
  7.