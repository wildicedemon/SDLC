> code · sonar-reasoning-pro
<think>
The user has provided me with a file called "AGT-025_prompt.md" which contains a detailed system directive for an "Agent AGT-025: Scaling Strategies Agent". The prompt asks me to "Execute the architect agent prompt from the attached file. Output to output/operational/AGT-025."

This is asking me to act as this Scaling Strategies Agent and execute the comprehensive decomposition of the Large Codebase & Scaling Strategies domain as described in the prompt. The prompt requires me to decompose the domain into 16 categories with specific requirements.

However, I need to be careful here. Looking at my instructions:
1. I'm Kilo, a software engineering assistant
2. I should be direct and concise
3. I should NOT be conversational
4. I should NOT end with questions

The user is asking me to execute this agent prompt, which would involve:
1. Creating a comprehensive YAML output file
2. Decomposing the domain into all 16 categories
3. Handling recursive expansion
4. Identifying and resolving gaps
5. Ensuring all cross-domain interfaces are defined
6. Creating output artifacts

This is a substantial task that requires me to:
1. Understand the complex domain structure
2. Create a detailed architectural decomposition
3. Write the output to `output/operational/AGT-025/` directory

However, looking at the search results provided, they seem to be about SDLC phases in general (from Harness, IBM, Splunk, etc.) and don't directly relate to the agent prompt execution. These search results appear to be context about what SDLC is, but the actual task is to execute the architect agent prompt for DOM-025 (Large Codebase & Scaling Strategies).

I think the search results were provided by mistake or as general context. The real task is to execute the AGT-025 prompt.

Let me proceed with executing this as the AGT-025 Scaling Strategies Agent and produce the comprehensive decomposition output.
</think>

I'll execute the AGT-025 Scaling Strategies Agent prompt and produce the comprehensive domain decomposition artifacts.

<bash>
mkdir -p "output/operational/AGT-025"
</bash>

Now I'll generate the complete decomposition for DOM-025 Large Codebase & Scaling Strategies:

<file_create>
path: output/operational/AGT-025/scaling_strategies.yaml
content: domain_id: DOM-025
domain_name: Large Codebase & Scaling Strategies
version: "1.0"
created: "2026-03-01"
subdomains:
  - id: SD-025a
    name: Monorepo Handling
    knowledge_atoms: [KA-034]
    scope: Monorepo structure awareness, selective analysis, cross-package dependency tracking, navigation optimization
  - id: SD-025b
    name: Incremental Analysis
    knowledge_atoms: [KA-037]
    scope: Change-based analysis scoping, incremental index updates, differential processing, cache-aware recomputation
  - id: SD-025c
    name: Performance at Scale
    knowledge_atoms: []
    scope: Resource allocation for large codebases, parallel processing strategies, memory-efficient analysis, adaptive complexity management

skills:
  - skill_id: DOM-025-SK-001
    name: Monorepo Structure Detection and Mapping
    description: Identifies monorepo root, detects workspace boundaries, maps inter-package structure, and creates dependency graphs for monorepo navigation.
    inputs: [file_tree, package_manifests, workspace_configs]
    outputs: [monorepo_map, package_graph, workspace_boundaries]
    complexity: High

  - skill_id: DOM-025-SK-002
    name: Cross-Package Dependency Analysis
    description: Traces dependencies across monorepo packages, identifies circular dependencies, and determines change impact across package boundaries.
    inputs: [monorepo_map, package_manifests, dependency_declarations]
    outputs: [dependency_graph, impact_analysis, circular_deps]
    complexity: High

  - skill_id: DOM-025-SK-003
    name: Incremental Analysis Scope Determination
    description: Analyzes file change deltas, determines affected packages/modules, and selects appropriate analysis depth based on change scope.
    inputs: [file_changes, dependency_graph, previous_analysis_state]
    outputs: [analysis_scope, affected_packages, analysis_depth]
    complexity: High

  - skill_id: DOM-025-SK-004
    name: Resource Allocation Optimization
    description: Calculates optimal resource distribution based on codebase size, complexity, and available system resources.
    inputs: [codebase_profile, system_resources, scaling_strategy]
    outputs: [resource_allocation, memory_budget, parallelism_config]
    complexity: Medium

  - skill_id: DOM-025-SK-005
    name: Parallel Processing Strategy Selection
    description: Determines optimal parallelization approach (worker count, work distribution, result merging) for large codebase analysis.
    inputs: [codebase_size, complexity_profile, resource_budget, analysis_type]
    outputs: [parallelism_strategy, worker_config, distribution_plan]
    complexity: Medium

  - skill_id: DOM-025-SK-006
    name: Memory-Efficient AST Processing
    description: Processes large source files using streaming, chunking, and incremental AST construction to avoid memory exhaustion.
    inputs: [large_file, analysis_requirements, memory_limit]
    outputs: [chunked_ast, streaming_results, memory_stats]
    complexity: High

  - skill_id: DOM-025-SK-007
    name: Adaptive Analysis Depth Configuration
    description: Determines appropriate analysis depth (shallow scan, full analysis, deep inspection) based on codebase scale and complexity class.
    inputs: [codebase_scale_profile, change_scope, performance_constraints]
    outputs: [analysis_depth, technique_selection, optimization_hints]
    complexity: Medium

  - skill_id: DOM-025-SK-008
    name: Cache Management and Invalidation
    description: Manages analysis result caching, tracks cache validity, implements selective invalidation based on dependency changes.
    inputs: [analysis_results, dependency_changes, cache_policy]
    outputs: [cache_state, invalidation_events, fresh_results]
    complexity: Medium

  - skill_id: DOM-025-SK-009
    name: Codebase Scale Classification
    description: Measures codebase metrics (file count, LOC, complexity) and assigns scale class (Small, Medium, Large, Enterprise).
    inputs: [file_tree, source_metrics, complexity_metrics]
    outputs: [scale_profile, complexity_class, strategy_recommendations]
    complexity: Medium

  - skill_id: DOM-025-SK-010
    name: Performance Benchmarking and Monitoring
    description: Establishes baseline performance metrics, monitors scaling efficiency, detects performance degradation, recommends optimizations.
    inputs: [operation_metrics, baseline_profile, current_state]
    outputs: [benchmark_report, anomalies, optimization_recommendations]
    complexity: Medium

workflows:
  - workflow_id: DOM-025-WF-001
    name: Monorepo Analysis and Indexing Workflow
    trigger: "Initial system setup or monorepo structure change detected"
    steps:
      - step: 1
        name: Detect Monorepo Root
        entry_criteria: "File tree available"
        exit_criteria: "Monorepo root identified or single-repo confirmed"
      - step: 2
        name: Map Package Boundaries
        entry_criteria: "Monorepo root identified"
        exit_criteria: "All workspace/package boundaries mapped"
      - step: 3
        name: Extract Package Manifests
        entry_criteria: "Package boundaries known"
        exit_criteria: "All package.json, tsconfig.json, etc. parsed"
      - step: 4
        name: Build Dependency Graph
        entry_criteria: "Package manifests extracted"
        exit_criteria: "Complete inter-package dependency graph created"
      - step: 5
        name: Detect Circular Dependencies
        entry_criteria: "Dependency graph built"
        exit_criteria: "Circular dependencies identified and logged"
      - step: 6
        name: Index for Navigation
        entry_criteria: "Dependency graph complete"
        exit_criteria: "Monorepo index ready for queries"
    completion_criteria: "Monorepo map created, dependency graph valid, index queryable, no unresolved circular dependencies"
    rollback_plan: "Revert to previous monorepo map version, restart detection"

  - workflow_id: DOM-025-WF-002
    name: Incremental Change Analysis Workflow
    trigger: "File changes detected in workspace"
    steps:
      - step: 1
        name: Detect Changed Files
        entry_criteria: "File system events available"
        exit_criteria: "Changed files list generated"
      - step: 2
        name: Determine Impact Scope
        entry_criteria: "Changed files identified"
        exit_criteria: "Affected packages and modules identified"
      - step: 3
        name: Estimate Change Magnitude
        entry_criteria: "Impact scope determined"
        exit_criteria: "Change classified as Small/Medium/Large"
      - step: 4
        name: Select Analysis Mode
        entry_criteria: "Change magnitude classified"
        exit_criteria: "Incremental or Full analysis selected"
      - step: 5
        name: Execute Scoped Analysis
        entry_criteria: "Analysis mode selected"
        exit_criteria: "Analysis results produced for affected scope"
      - step: 6
        name: Invalidate Dependent Caches
        entry_criteria: "Analysis complete"
        exit_criteria: "Downstream caches invalidated based on dependency graph"
      - step: 7
        name: Integrate Results
        entry_criteria: "Caches invalidated"
        exit_criteria: "New analysis merged with existing state"
    completion_criteria: "Change fully analyzed, impacted caches invalidated, results integrated, state consistent"
    rollback_plan: "Restore previous analysis state, revert cache invalidations, rerun full analysis if needed"

  - workflow_id: DOM-025-WF-003
    name: Scale-Adaptive Resource Allocation Workflow
    trigger: "Codebase scale assessment or resource constraints change"
    steps:
      - step: 1
        name: Classify Codebase Scale
        entry_criteria: "Codebase metrics available"
        exit_criteria: "Scale class assigned (Small/Medium/Large/Enterprise)"
      - step: 2
        name: Measure Available Resources
        entry_criteria: "Scale class assigned"
        exit_criteria: "Available CPU, memory, I/O measured"
      - step: 3
        name: Select Scaling Strategy
        entry_criteria: "Scale class and resources known"
        exit_criteria: "Appropriate strategy (sequential, parallel, distributed) selected"
      - step: 4
        name: Allocate Resources
        entry_criteria: "Strategy selected"
        exit_criteria: "CPU, memory, parallelism parameters configured"
      - step: 5
        name: Configure Parallelism
        entry_criteria: "Resources allocated"
        exit_criteria: "Worker pool size, work distribution policy configured"
      - step: 6
        name: Deploy Configuration
        entry_criteria: "Parallelism configured"
        exit_criteria: "Configuration active in system"
    completion_criteria: "Resources allocated, parallelism configured, strategy deployed, monitoring active"
    rollback_plan: "Restore previous resource configuration, revert to default parallelism, alert administrator"

  - workflow_id: DOM-025-WF-004
    name: Large Codebase Initial Onboarding Workflow
    trigger: "New large codebase (>10K files) added to system"
    steps:
      - step: 1
        name: Profile Codebase
        entry_criteria: "Codebase root available"
        exit_criteria: "Codebase profile created (size, complexity, structure)"
      - step: 2
        name: Classify Scale
        entry_criteria: "Codebase profile complete"
        exit_criteria: "Scale class assigned"
      - step: 3
        name: Detect Monorepo Structure
        entry_criteria: "Codebase classified"
        exit_criteria: "Monorepo structure mapped or single-repo confirmed"
      - step: 4
        name: Build Initial Index
        entry_criteria: "Structure detected"
        exit_criteria: "Symbol index and file index built"
      - step: 5
        name: Configure Scaling Strategy
        entry_criteria: "Index built"
        exit_criteria: "Scale-appropriate analysis strategy configured"
      - step: 6
        name: Establish Performance Baseline
        entry_criteria: "Strategy configured"
        exit_criteria: "Performance baseline established for future comparisons"
      - step: 7
        name: Activate Monitoring
        entry_criteria: "Baseline established"
        exit_criteria: "Continuous monitoring active, alerts configured"
    completion_criteria: "Codebase fully profiled, strategy configured, baseline established, monitoring active"
    rollback_plan: "Clear indexes and caches, return to pre-onboarding state, alert operator"

  - workflow_id: DOM-025-WF-005
    name: Performance Benchmark and Optimization Workflow
    trigger: "Performance SLA threshold breached or periodic benchmark scheduled"
    steps:
      - step: 1
        name: Collect Performance Metrics
        entry_criteria: "Monitoring data available"
        exit_criteria: "Comprehensive metrics collected (latency, memory, CPU)"
      - step: 2
        name: Compare to Baseline
        entry_criteria: "Metrics collected"
        exit_criteria: "Deviations from baseline identified"
      - step: 3
        name: Identify Bottlenecks
        entry_criteria: "Deviations identified"
        exit_criteria: "Root causes of performance issues determined"
      - step: 4
        name: Recommend Optimizations
        entry_criteria: "Bottlenecks identified"
        exit_criteria: "Ranked list of optimization strategies produced"
      - step: 5
        name: Execute Optimizations
        entry_criteria: "Optimizations recommended"
        exit_criteria: "Selected optimizations applied"
      - step: 6
        name: Measure Impact
        entry_criteria: "Optimizations applied"
        exit_criteria: "Post-optimization metrics collected and compared"
      - step: 7
        name: Lock or Revert
        entry_criteria: "Impact measured"
        exit_criteria: "Optimization locked if successful, reverted if degraded"
    completion_criteria: "Bottlenecks resolved, performance restored to acceptable range, optimization results documented"
    rollback_plan: "Revert applied optimizations, restore previous configuration, investigate root cause"

rules_and_constraints:
  - rule_id: DOM-025-RL-001
    constraint: "Analysis scope in monorepos must be bounded by directly affected packages and modules (KA-034)"
    rationale: "Prevents unbounded transitive dependency analysis explosion that could consume all available resources"
    enforcement: "Validate affected_packages list against dependency_graph; reject analysis requests with scope exceeding threshold"
    exceptions: "Full-system analysis explicitly requested with operator approval and resource pre-allocation"

  - rule_id: DOM-025-RL-002
    constraint: "Incremental analysis must be preferred over full reanalysis when change scope is Small or Medium (KA-037)"
    rationale: "Incremental analysis provides faster feedback and reduces resource consumption for common small-change scenarios"
    enforcement: "Classify change magnitude; automatically select incremental mode if Small/Medium; require explicit override for Full analysis"
    exceptions: "Incremental analysis cache corrupted or unavailable; then fall back to Full analysis"

  - rule_id: DOM-025-RL-003
    constraint: "Resource consumption must scale sub-linearly or linearly with codebase size (not super-linear)"
    rationale: "Ensures system remains performant even on very large codebases; prevents quadratic or exponential degradation"
    enforcement: "Monitor resource usage vs. codebase size; alert if resource growth exceeds O(n) trend; trigger optimization workflow"
    exceptions: "None; this is a hard architectural constraint"

  - rule_id: DOM-025-RL-004
    constraint: "Large files (>1MB) must be analyzed using streaming or chunked processing, not full AST construction"
    rationale: "Prevents memory exhaustion when processing unusually large source files"
    enforcement: "Check file size before parsing; route large files to streaming processor; block full-AST parsing for large files"
    exceptions: "Language-specific constraints may require full parsing; document and monitor resource usage"

  - rule_id: DOM-025-RL-005
    constraint: