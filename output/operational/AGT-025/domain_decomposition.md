> code · sonar-reasoning-pro


<think>
The user has provided:
1. Search results about SDLC (Software Development Life Cycle) phases
2. A file containing an "Agent AGT-025: Scaling Strategies Agent" prompt
3. An instruction to execute the architect agent prompt from the attached file and output to `output/operational/AGT-025`

However, looking at my instructions carefully:
- I'm instructed to NOT be conversational
- I should be direct and to the point
- I should NOT ask for more information than necessary
- I should accomplish tasks iteratively and methodically

The user is asking me to "Execute the architect agent prompt from the attached file." This appears to be asking me to run some kind of architectural decomposition based on the AGT-025 prompt that was provided.

However, looking at the prompt file (AGT-025_prompt.md), this appears to be a system directive for an autonomous agent (not for me to execute). It's asking for a complete decomposition of a domain into 16 categories (Skills, Workflows, Task Templates, Rules & Constraints, etc.).

The search results about SDLC appear to be unrelated to the actual task - they seem to be context that was accidentally included or not properly integrated into the query.

I need to clarify: Should I:
1. Generate the decomposition output as described in AGT-025?
2. Create the YAML/output files referenced in the prompt?

Given my role as Kilo (a software engineer), I should interpret this as: Generate the complete domain decomposition for AGT-025 (Scaling Strategies Agent) according to the specification in the prompt, and output it to `output/operational/AGT-025`.

This is a substantial task that requires creating:
- 16 categories of architectural components
- 3 recursive subdomains decomposed
- All gaps resolved
- Output artifacts (YAML files)

I should start by creating the directory structure and then generating the comprehensive decomposition.
</think>

I'll execute the AGT-025 Scaling Strategies Agent architectural decomposition and output the complete domain definition to `output/operational/AGT-025`.
<function_calls>
<invoke name="bash">
<parameter name="command">mkdir -p "c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\operational\AGT-025"</parameter>
</invoke>
</function_calls>
<invoke name="file">
<parameter name="action">write</parameter>
<parameter name="filePath">c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\operational\AGT-025\domain_decomposition.yaml</parameter>
<parameter name="content">agent: AGT-025
domain: DOM-025 Large Codebase & Scaling Strategies
category: Operational
execution_phase: Phase 4 (Operational)
timestamp: "2026-03-01T05:06:58Z"

---

section_1_skills:
  - id: DOM-025-SK-001
    name: Monorepo Structure Detection and Mapping
    description: Analyzes repository topology to identify monorepo patterns, package boundaries, and structural organization. Maps relationships between workspaces.
    inputs:
      - Repository file system structure
      - Package manifests (package.json, Cargo.toml, etc.)
      - Workspace configuration files
    outputs:
      - Monorepo topology map (packages, boundaries, relationships)
      - Workspace hierarchy
      - Dependency graph skeleton
    complexity: High
    knowledge_atoms: [KA-034]

  - id: DOM-025-SK-002
    name: Incremental Analysis Scope Determination
    description: Determines which packages, modules, and files must be reanalyzed based on detected changes. Computes transitive impact scope.
    inputs:
      - Changed files list
      - Dependency graph
      - Previous analysis state
    outputs:
      - Affected scope (files, packages, modules)
      - Analysis depth recommendation
      - Cache invalidation set
    complexity: High
    knowledge_atoms: [KA-037]

  - id: DOM-025-SK-003
    name: Resource Allocation Optimization for Large Codebases
    description: Determines optimal resource distribution (CPU, memory, parallelism) based on codebase scale, complexity, and available infrastructure.
    inputs:
      - Codebase Scale Profile
      - System resource constraints
      - Performance SLAs
      - Current load metrics
    outputs:
      - Resource allocation plan (CPU cores, memory limits, worker counts)
      - Parallelism strategy
      - Estimated completion time
    complexity: Medium
    knowledge_atoms: []

  - id: DOM-025-SK-004
    name: Parallel Processing Strategy Selection
    description: Selects optimal parallelism strategy (horizontal scaling, task batching, pipeline parallelism) based on workload characteristics and resource constraints.
    inputs:
      - Workload dependency graph
      - Available parallelism levels
      - Resource constraints
      - Latency requirements
    outputs:
      - Parallelism strategy configuration
      - Worker pool sizing
      - Batch grouping recommendations
    complexity: High
    knowledge_atoms: []

  - id: DOM-025-SK-005
    name: Memory-Efficient AST Processing for Large Files
    description: Implements streaming and chunked AST processing to handle large source files without memory exhaustion. Uses iterative analysis and garbage collection awareness.
    inputs:
      - Large source file
      - Memory budget
      - Analysis requirements
    outputs:
      - Streamed analysis results
      - Partial AST artifacts
      - Memory usage telemetry
    complexity: High
    knowledge_atoms: [KA-037]

  - id: DOM-025-SK-006
    name: Cross-Package Dependency Analysis in Monorepos
    description: Analyzes and bounds dependency relationships across packages in monorepos. Detects dependency cycles and transitive impacts.
    inputs:
      - Package manifests
      - Import statements across packages
      - Monorepo topology
    outputs:
      - Cross-package dependency matrix
      - Cycle detection report
      - Impact transitive closure
      - Bounded scope recommendations
    complexity: High
    knowledge_atoms: [KA-034]

  - id: DOM-025-SK-007
    name: Adaptive Analysis Depth Based on Codebase Scale
    description: Adjusts analysis depth (shallow vs. deep, selective vs. comprehensive) dynamically based on detected codebase size, complexity, and performance constraints.
    inputs:
      - Codebase Scale Profile
      - Current performance metrics
      - Analysis requirements
      - Time budget
    outputs:
      - Analysis depth configuration
      - Feature enablement/disablement set
      - Precision/recall tradeoff rationale
    complexity: Medium
    knowledge_atoms: []

  - id: DOM-025-SK-008
    name: Cache Management for Reusable Analysis Results
    description: Manages lifecycle of cached analysis artifacts including invalidation, reuse, coherence, and garbage collection.
    inputs:
      - Changed artifacts
      - Dependency change set
      - Cache state
      - Memory constraints
    outputs:
      - Cache invalidation commands
      - Reuse recommendations
      - Purge decisions
      - Cache coherence report
    complexity: Medium
    knowledge_atoms: [KA-037]

  - id: DOM-025-SK-009
    name: Codebase Scale Classification
    description: Classifies codebase into scale categories (Small <5K LOC, Medium 5K-50K, Large 50K-500K, Enterprise >500K) with complexity metrics.
    inputs:
      - File count
      - Total LOC
      - Language breakdown
      - Dependency density
      - Module count
    outputs:
      - Scale classification (Small|Medium|Large|Enterprise)
      - Complexity score
      - Scaling strategy recommendation
    complexity: Low
    knowledge_atoms: []

  - id: DOM-025-SK-010
    name: Incremental Index Update Strategy
    description: Determines optimal approach to update search indexes and analysis indices when changes are detected (full rebuild vs. incremental).
    inputs:
      - Change scope
      - Index state
      - Performance metrics
      - Current load
    outputs:
      - Index update strategy
      - Rebuild vs. incremental decision
      - Update plan with timing
    complexity: Medium
    knowledge_atoms: [KA-037]

  - id: DOM-025-SK-011
    name: Performance Benchmark Definition and Measurement
    description: Defines and measures performance characteristics for scaling operations across different codebase sizes.
    inputs:
      - Scale class
      - Operation type
      - System configuration
      - Execution metrics
    outputs:
      - Benchmark results
      - Baseline establishment
      - Variance analysis
      - SLA compliance report
    complexity: Medium
    knowledge_atoms: []

  - id: DOM-025-SK-012
    name: Workspace Conflict Detection and Resolution
    description: Detects and resolves conflicts when multiple analysis processes operate on shared workspace in monorepos.
    inputs:
      - Active workspace locks
      - File access patterns
      - Process state
    outputs:
      - Conflict detection report
      - Resolution recommendations
      - Lock acquisition strategy
    complexity: Medium
    knowledge_atoms: []

---

section_2_workflows:
  - id: DOM-025-WF-001
    name: Monorepo Analysis and Indexing Workflow
    trigger: "Initial codebase onboarding or periodic reindex"
    steps:
      - step: 1
        name: Detect Monorepo Structure
        entry_criteria: "Repository path provided"
        action: "Execute DOM-025-SK-001 to detect topology"
        exit_criteria: "Monorepo topology map generated"
      - step: 2
        name: Extract Package Manifests
        entry_criteria: "Topology map available"
        action: "Scan all packages for manifests, extract dependencies"
        exit_criteria: "Manifest data indexed"
      - step: 3
        name: Build Dependency Graph
        entry_criteria: "Manifest data available"
        action: "Construct transitive dependency closure"
        exit_criteria: "Complete dependency graph available"
      - step: 4
        name: Identify Analysis Boundaries
        entry_criteria: "Dependency graph available"
        action: "Determine package-level analysis units"
        exit_criteria: "Analysis boundaries defined"
      - step: 5
        name: Create Monorepo Index
        entry_criteria: "Boundaries defined"
        action: "Build searchable index of all packages and cross-dependencies"
        exit_criteria: "Monorepo index queryable"
    completion_criteria: "Monorepo index complete, all packages indexed, dependency graph traversable"
    rollback_plan: "Delete partial index, restore from backup, resume from step 1"

  - id: DOM-025-WF-002
    name: Incremental Change Analysis Workflow
    trigger: "File change detected in watched repository"
    steps:
      - step: 1
        name: Detect Changed Files
        entry_criteria: "File system event received"
        action: "Collect all changed/added/deleted files"
        exit_criteria: "Change set identified"
      - step: 2
        name: Determine Impact Scope
        entry_criteria: "Change set available"
        action: "Execute DOM-025-SK-002 to compute affected packages and modules"
        exit_criteria: "Impact scope and affected packages determined"
      - step: 3
        name: Classify Scope Size
        entry_criteria: "Impact scope determined"
        action: "Evaluate if scope is small (<=10 packages) or large"
        exit_criteria: "Scope classification (small|large) determined"
      - step: 4a
        name: Execute Incremental Analysis
        entry_criteria: "Scope classified as small"
        action: "Reanalyze only affected packages, reuse cached results for unaffected"
        exit_criteria: "Incremental analysis complete"
      - step: 4b
        name: Execute Full Reanalysis
        entry_criteria: "Scope classified as large"
        action: "Trigger full codebase reanalysis with scale-aware strategies"
        exit_criteria: "Full analysis complete"
      - step: 5
        name: Invalidate Dependent Cache
        entry_criteria: "Analysis complete"
        action: "Execute DOM-025-SK-008 to invalidate cache entries for affected analyses"
        exit_criteria: "Cache coherence restored"
      - step: 6
        name: Update Indices
        entry_criteria: "Cache invalidated"
        action: "Update search indices with new analysis results"
        exit_criteria: "Indices consistent with latest analysis"
    completion_criteria: "All affected packages reanalyzed, cache valid, indices updated"
    rollback_plan: "Restore previous analysis state from backup, resume from last valid checkpoint"

  - id: DOM-025-WF-003
    name: Scale-Adaptive Resource Allocation Workflow
    trigger: "Codebase scale assessment or performance degradation detected"
    steps:
      - step: 1
        name: Assess Codebase Scale
        entry_criteria: "Codebase metrics available"
        action: "Execute DOM-025-SK-009 to classify codebase size"
        exit_criteria: "Scale classification determined"
      - step: 2
        name: Measure System Resources
        entry_criteria: "Scale classification available"
        action: "Query available CPU, memory, parallelism capability"
        exit_criteria: "System resource inventory complete"
      - step: 3
        name: Determine Resource Constraints
        entry_criteria: "System resources and SLAs known"
        action: "Execute DOM-025-SK-003 to compute optimal allocation"
        exit_criteria: "Resource allocation plan generated"
      - step: 4
        name: Select Parallelism Strategy
        entry_criteria: "Resource plan available"
        action: "Execute DOM-025-SK-004 to choose parallelism approach"
        exit_criteria: "Parallelism strategy determined"
      - step: 5
        name: Configure Execution Environment
        entry_criteria: "Allocation and parallelism strategy known"
        action: "Apply resource limits, spawn worker pools, configure batching"
        exit_criteria: "Execution environment configured"
      - step: 6
        name: Monitor and Adjust
        entry_criteria: "Execution started"
        action: "Continuously monitor performance; adjust allocation if metrics degrade"
        exit_criteria: "Performance within SLA"
    completion_criteria: "Execution within resource constraints, performance SLA met"
    rollback_plan: "Reduce parallelism, increase time budget, switch to sequential processing"

  - id: DOM-025-WF-004
    name: Large Codebase Initial Onboarding Workflow
    trigger: "New large codebase added to system"
    steps:
      - step: 1
        name: Inventory Codebase
        entry_criteria: "Codebase path provided"
        action: "Count files, compute LOC, extract language breakdown"
        exit_criteria: "Codebase metrics collected"
      - step: 2
        name: Classify Scale and Complexity
        entry_criteria: "Metrics collected"
        action: "Execute DOM-025-SK-009 to classify codebase"
        exit_criteria: "Scale classification and complexity score assigned"
      - step: 3
        name: Detect Structure Type
        entry_criteria: "Codebase classified"
        action: "Determine if monorepo, polyrepo, or single-package; execute appropriate detection"
        exit_criteria: "Structure type and topology identified"
      - step: 4
        name: Plan Analysis Strategy
        entry_criteria: "Structure known"
        action: "If monorepo: execute WF-001; else: plan single-package analysis"
        exit_criteria: "Analysis strategy defined"
      - step: 5
        name: Execute Phased Analysis
        entry_criteria: "Strategy defined"
        action: "Perform initial shallow analysis, incrementally deepen"
        exit_criteria: "Initial analysis checkpoint reached"
      - step: 6
        name: Establish Performance Baseline
        entry_criteria: "Initial analysis complete"
        action: "Execute DOM-025-SK-011 to establish performance baseline"
        exit_criteria: "Baseline metrics recorded"
    completion_criteria: "Codebase indexed, metrics baseline established, ready for incremental updates"
    rollback_plan: "Delete partial index, mark codebase as failed onboarding, log error for manual intervention"

  - id: DOM-025-WF-005
    name: Performance Benchmark and Optimization Workflow
    trigger: "Periodic (weekly) or performance SLA breach"
    steps:
      - step: 1
        name: Collect Performance Metrics
        entry_criteria: "