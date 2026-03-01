> code · sonar-reasoning-pro

<think>
The user wants me to execute the code agent prompt from the file `AGT-015_prompt.md`. This is a comprehensive prompt for the "Code Explorer Agent" that needs to fully decompose the "Code Exploration & Navigation" domain within an agentic AI coding system.

Looking at the file, this is a detailed system directive for an agent that needs to:
1. Define complete code exploration and navigation architecture
2. Decompose the domain into 16 categories (Skills, Workflows, Task Templates, Rules & Constraints, Interfaces, Dependencies, State Models, Data Models, Control Flows, Failure Modes & Recovery, Optimization Strategies, Coordination Mechanisms, Context Requirements, Memory Structures, Monitoring Requirements, and Evolution Mechanisms)
3. Recursively expand subdomains with max depth of 4 levels
4. Detect and resolve gaps
5. Output to `output/intelligence/AGT-015`

The user is asking me to execute this prompt - meaning I should follow the directive and produce the comprehensive decomposition as specified. However, I need to be careful here:

1. This is a very extensive decomposition task
2. The output should go to `output/intelligence/AGT-015`
3. I need to create YAML outputs for skills, workflows, and techniques/strategies

Given the scope and the nature of this task, I should:
1. Start by reading the file (already done)
2. Create the output directory structure
3. Begin the decomposition following the exact categories and structure specified
4. Output the required YAML files

Let me start by creating the necessary directory structure and then produce the comprehensive decomposition.
</think>

I'll execute the AGT-015 Code Explorer Agent prompt and produce the complete domain decomposition with outputs to `output/intelligence/AGT-015`.

```bash
mkdir -p "output/intelligence/AGT-015"
```

Now generating the comprehensive domain decomposition with all 16 categories across the four subdomains. This will be a substantial output covering skills, workflows, rules, interfaces, dependencies, state models, data models, control flows, failure modes, optimization strategies, coordination mechanisms, context requirements, memory structures, monitoring requirements, and evolution mechanisms.

```yaml
# output/intelligence/AGT-015/code_exploration_skills.yaml
domain: DOM-015
domain_name: Code Exploration & Navigation
skills:
  # SD-015a: AST Analysis Skills
  - skill_id: DOM-015-SK-001
    name: AST Parsing and Traversal
    description: Parse source code into Abstract Syntax Trees and traverse AST nodes with context preservation.
    inputs: [source_code, language, grammar_version]
    outputs: [ast_root, node_map, parse_errors]
    complexity: High
    dependencies: [KA-037]
    subdomain: SD-015a

  - skill_id: DOM-015-SK-002
    name: Control Flow Graph Construction
    description: Build CFGs from AST representation tracking conditional branches and loop structures.
    inputs: [ast_root, function_scope]
    outputs: [cfg_graph, entry_point, exit_points]
    complexity: High
    dependencies: [DOM-015-SK-001, KA-037]
    subdomain: SD-015a

  - skill_id: DOM-015-SK-003
    name: Data Flow Graph Analysis
    description: Construct DFGs tracking variable definitions, uses, and propagation through code paths.
    inputs: [cfg_graph, symbol_table]
    outputs: [dfg_graph, def_use_chains, reaching_definitions]
    complexity: High
    dependencies: [DOM-015-SK-002, DOM-015-SK-005]
    subdomain: SD-015a

  - skill_id: DOM-015-SK-004
    name: Code Property Graph Generation
    description: Merge AST, CFG, and DFG into unified Code Property Graph for multi-level analysis.
    inputs: [ast_root, cfg_graph, dfg_graph]
    outputs: [cpg, node_index, edge_types]
    complexity: High
    dependencies: [DOM-015-SK-001, DOM-015-SK-002, DOM-015-SK-003]
    subdomain: SD-015a

  - skill_id: DOM-015-SK-005
    name: Tree-sitter Grammar Loading and Incremental Parsing
    description: Load and manage Tree-sitter grammars with support for incremental parsing on large files.
    inputs: [language, grammar_path, previous_tree, edit_range]
    outputs: [tree, parse_status, incremental_delta]
    complexity: Medium
    dependencies: [KA-037]
    subdomain: SD-015a

  - skill_id: DOM-015-SK-006
    name: Cross-Language AST Normalization
    description: Convert language-specific ASTs to normalized intermediate representation for unified analysis.
    inputs: [ast_root, source_language, target_language]
    outputs: [normalized_ast, type_mappings, language_features]
    complexity: High
    dependencies: [DOM-015-SK-001, KA-037]
    subdomain: SD-015a

  # SD-015b: Semantic Search Skills
  - skill_id: DOM-015-SK-007
    name: Code Embedding Generation
    description: Generate semantic embeddings for code snippets and symbols for similarity-based search.
    inputs: [code_snippet, symbol_info, context]
    outputs: [embedding_vector, embedding_metadata]
    complexity: Medium
    dependencies: [DOM-015-SK-001, DOM-015-SK-011]
    subdomain: SD-015b

  - skill_id: DOM-015-SK-008
    name: Semantic Code Search
    description: Search codebases using semantic similarity rather than syntax matching.
    inputs: [query_embedding, index, search_scope]
    outputs: [search_results, relevance_scores, context_windows]
    complexity: Medium
    dependencies: [DOM-015-SK-007, DOM-015-SK-009]
    subdomain: SD-015b

  - skill_id: DOM-015-SK-009
    name: Natural Language to Code Search
    description: Translate natural language queries to code search operations with semantic understanding.
    inputs: [nl_query, codebase_index, context_strategy]
    outputs: [code_matches, nl_interpretation, confidence_score]
    complexity: High
    dependencies: [DOM-015-SK-007, DOM-015-SK-008]
    subdomain: SD-015b

  - skill_id: DOM-015-SK-010
    name: Semantic Similarity Scoring
    description: Compute semantic similarity between code artifacts using multiple scoring dimensions.
    inputs: [artifact_a, artifact_b, similarity_dimensions]
    outputs: [similarity_score, dimension_scores, explanation]
    complexity: Medium
    dependencies: [DOM-015-SK-007]
    subdomain: SD-015b

  # SD-015c: Codebase Mapping Skills
  - skill_id: DOM-015-SK-011
    name: Codebase Structure Mapping
    description: Create complete hierarchical map of codebase structure including files, modules, and packages.
    inputs: [root_path, ignore_rules, language_list]
    outputs: [structure_map, module_hierarchy, entry_points]
    complexity: Medium
    dependencies: [DOM-015-SK-001]
    subdomain: SD-015c

  - skill_id: DOM-015-SK-012
    name: Dependency Graph Extraction
    description: Extract and build dependency graphs tracking imports, includes, and cross-references.
    inputs: [codebase_map, symbol_table, scope_info]
    outputs: [dependency_graph, circular_deps, dependency_metadata]
    complexity: High
    dependencies: [DOM-015-SK-011, DOM-015-SK-013]
    subdomain: SD-015c

  - skill_id: DOM-015-SK-013
    name: Symbol Resolution Across Files
    description: Resolve symbol definitions and references across file and module boundaries.
    inputs: [symbol_name, scope_context, module_boundaries]
    outputs: [definition_location, references, scope_chain]
    complexity: High
    dependencies: [DOM-015-SK-001, DOM-015-SK-011]
    subdomain: SD-015c

  - skill_id: DOM-015-SK-014
    name: Call Graph Construction and Analysis
    description: Build and analyze call graphs tracking function invocations and dynamic dispatch.
    inputs: [cpg, function_definitions, call_sites]
    outputs: [call_graph, entry_points, reachability_sets]
    complexity: High
    dependencies: [DOM-015-SK-004, DOM-015-SK-012]
    subdomain: SD-015c

  - skill_id: DOM-015-SK-015
    name: Module Relationship Visualization
    description: Generate dependency and relationship visualizations for module interconnections.
    inputs: [dependency_graph, call_graph, scope_hierarchy]
    outputs: [visual_representation, relationship_data, layout_data]
    complexity: Medium
    dependencies: [DOM-015-SK-012, DOM-015-SK-014]
    subdomain: SD-015c

  - skill_id: DOM-015-SK-016
    name: Architectural Pattern Detection
    description: Identify common architectural patterns and design patterns in codebase structure.
    inputs: [codebase_map, call_graph, dependency_graph]
    outputs: [patterns_detected, pattern_instances, architectural_type]
    complexity: High
    dependencies: [DOM-015-SK-012, DOM-015-SK-014]
    subdomain: SD-015c

  # SD-015d: Navigation Strategies Skills
  - skill_id: DOM-015-SK-017
    name: Definition/Reference Resolution
    description: Efficiently resolve symbol definitions and find all references with context awareness.
    inputs: [symbol_name, location, scope_depth_limit]
    outputs: [definition_locations, references, resolution_confidence]
    complexity: Medium
    dependencies: [DOM-015-SK-013]
    subdomain: SD-015d

  - skill_id: DOM-015-SK-018
    name: Cross-File Navigation Strategies
    description: Plan efficient navigation paths through multi-file codebases considering dependencies.
    inputs: [start_location, target_concept, navigation_context]
    outputs: [navigation_path, intermediate_points, relevance_scores]
    complexity: High
    dependencies: [DOM-015-SK-013, DOM-015-SK-012]
    subdomain: SD-015d

  - skill_id: DOM-015-SK-019
    name: Symbol Table Management
    description: Maintain and query symbol tables across scopes with efficient lookup and update.
    inputs: [symbol_definitions, scope_stack, mutation_operations]
    outputs: [symbol_table_state, query_results, scope_info]
    complexity: Medium
    dependencies: [DOM-015-SK-013]
    subdomain: SD-015d

  - skill_id: DOM-015-SK-020
    name: Context-Aware Navigation Ordering
    description: Order navigation results by relevance to current task context and developer intent.
    inputs: [navigation_candidates, task_context, relevance_weights]
    outputs: [ordered_results, relevance_justification]
    complexity: Medium
    dependencies: [DOM-015-SK-018, DOM-015-SK-008]
    subdomain: SD-015d

  - skill_id: DOM-015-SK-021
    name: Efficient Code Navigation Algorithms
    description: Implement breadth-first, depth-first, and bidirectional navigation through code graphs.
    inputs: [code_graph, start_node, traversal_type, depth_limit]
    outputs: [traversal_path, reachability_set, traversal_metadata]
    complexity: High
    dependencies: [DOM-015-SK-014]
    subdomain: SD-015d

---
export_date: 2026-03-01
total_skills: 21
coverage: [SD-015a:6, SD-015b:4, SD-015c:6, SD-015d:5]
```

```yaml
# output/intelligence/AGT-015/code_exploration_workflows.yaml
domain: DOM-015
domain_name: Code Exploration & Navigation
workflows:
  - workflow_id: DOM-015-WF-001
    name: Full Codebase Indexing and Mapping
    trigger: Initial agent activation, manual indexing request, significant codebase changes detected
    steps:
      - step: 1
        name: Enumerate Source Files
        entry_criteria: Root path available, ignore rules defined
        actions: 
          - Traverse filesystem respecting ignore patterns
          - Detect file types and language associations
          - Build file manifest with metadata
        exit_criteria: Complete file list with language mappings
      
      - step: 2
        name: Parse ASTs for All Files
        entry_criteria: File manifest complete
        actions:
          - Load appropriate Tree-sitter grammars
          - Parse each file with error handling
          - Build per-file ASTs
          - Cache parse results
        exit_criteria: AST cache populated, parse errors logged
      
      - step: 3
        name: Extract Symbols and Definitions
        entry_criteria: All ASTs available
        actions:
          - Traverse each AST extracting symbol definitions
          - Build initial symbol table with scopes
          - Extract type information where available
          - Map definition locations
        exit_criteria: Global symbol table created
      
      - step: 4
        name: Build Dependency Graphs
        entry_criteria: Symbol table complete
        actions:
          - Extract import/include statements
          - Resolve symbol dependencies across files
          - Build call graphs from function definitions
          - Detect circular dependencies
        exit_criteria: Dependency and call graphs complete
      
      - step: 5
        name: Create Unified Index
        entry_criteria: All graphs built
        actions:
          - Merge ASTs, CFGs, DFGs into CPGs
          - Build searchable index with embeddings
          - Create architectural pattern catalog
          - Store index in persistent cache
        exit_criteria: Full codebase index ready for queries
    
    completion_criteria: |
      - All source files processed
      - AST cache populated and validated
      - Symbol table complete and consistent
      - Dependency graphs built without unresolved dependencies
      - Searchable index created
      - Index passes self-consistency checks
    
    rollback_plan: |
      - If parse error rate > 5%: halt and report language support gaps
      - If circular dependencies detected: mark as warning, continue with cycle detection
      - If index corruption: restore from previous checkpoint
      - If memory exhaustion: switch to streaming mode with bounded window

  - workflow_id: DOM-015-WF-002
    name: Incremental Code Change Analysis
    trigger: File modification detected, SCM commit received, manual refresh requested
    steps:
      - step: 1
        name: Detect Changed Files
        entry_criteria: Change notification or SCM diff available
        actions:
          - Identify modified, added, deleted files
          - Determine scope of change impact
          - Mark files requiring re-analysis
        exit_criteria: Change manifest created
      
      - step: 2
        name: Re-Parse Affected Files
        entry_criteria: Change manifest available
        actions:
          - Use incremental parsing for modified files
          - Build new ASTs preserving stable nodes
          - Identify structural changes
        exit_criteria: Updated ASTs for affected files
      
      - step: 3
        name: Update Symbol Tables
        entry_criteria: New ASTs available
        actions:
          - Remove stale symbol entries
          - Add new symbol definitions
          - Update scope information
          - Resolve new references
        exit_criteria: Symbol table consistency verified
      
      - step: 4
        name: Propagate Graph Updates
        entry_criteria: Symbol table updated
        actions:
          - Update call graphs for affected functions
          - Recompute dependency edges
          - Update reachability sets
          - Invalidate affected caches
        exit_criteria: All dependent graphs synchronized
      
      - step: 5
        name: Update Search Index
        entry_criteria: Graphs updated
        actions:
          - Regenerate embeddings for changed symbols
          - Update search index entries
          - Mark index fresh for current timestamp
        exit_criteria: Index reflects all changes
    
    completion_criteria: |
      - All changed files re-parsed
      - Symbol table consistency verified
      - No stale references in graphs
      - Search results reflect changes
      - Performance metrics acceptable
    
    rollback_plan: |
      - If update fails: restore previous index from checkpoint
      - If inconsistency detected: revert to full re-index
      - If performance degradation: trigger background optimization

  - workflow_id: DOM-015-WF-003
    name: Semantic Search Query Resolution
    trigger: Search request from AGT-017 Code Generation or other consumers
    steps:
      - step: 1
        name: