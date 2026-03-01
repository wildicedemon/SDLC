> code · sonar-reasoning-pro


<think>
The user is asking me to execute the code agent prompt from the file `AGT-015_prompt.md` and output to `output/intelligence/AGT-015`.

Looking at the file, this is a system directive for the "Code Explorer Agent (AGT-015)" which is a specialized autonomous agent responsible for decomposing the "Code Exploration & Navigation" domain. The prompt requires comprehensive decomposition into 16 categories including skills, workflows, task templates, rules, interfaces, dependencies, state models, data models, control flows, failure modes, optimization strategies, coordination mechanisms, context requirements, memory structures, monitoring requirements, and evolution mechanisms.

This is a very detailed and complex decomposition task. The prompt is asking me to:
1. Define skills for code exploration
2. Define workflows
3. Define task templates
4. Define rules and constraints
5. Define interfaces to other domains
6. Map dependencies
7. Define state models
8. Define data models
9. Define control flows
10. Identify failure modes and recovery
11. Define optimization strategies
12. Define coordination mechanisms
13. Define context requirements
14. Define memory structures
15. Define monitoring requirements
16. Define evolution mechanisms

Plus recursively expand subdomains: SD-015a (AST Analysis), SD-015b (Semantic Search), SD-015c (Codebase Mapping), SD-015d (Navigation Strategies).

This is essentially asking me to act as the Code Explorer Agent and produce a comprehensive decomposition document. Given the scope and complexity, I should create a structured output file in YAML or markdown format that covers all these categories.

Let me create this output systematically. I'll need to output to `output/intelligence/AGT-015`. Since this is a Kilo environment, I should use the file writing tool to create this comprehensive decomposition.
</think>

I'll execute the Code Explorer Agent (AGT-015) prompt to decompose the Code Exploration & Navigation domain. This is a comprehensive decomposition task requiring structured outputs across 16 categories and 4 subdomains.
<function_calls>
<invoke name="bash">
<parameter name="command">mkdir -p "c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\intelligence\AGT-015"</parameter>
</invoke>
</function_calls>
<function_calls>
<invoke name="write_file">
<parameter name="path">c:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\intelligence\AGT-015\code_exploration_skills.yaml</parameter>
<parameter name="content">domain: DOM-015 Code Exploration & Navigation
agent: AGT-015 Code Explorer Agent
category: Skills
generation_date: 2026-03-01
version: 1.0

skills:
  # SD-015a: AST Analysis Skills
  ast_parsing_and_traversal:
    id: DOM-015-SK-001
    name: AST Parsing and Traversal
    description: Parse source code into Abstract Syntax Trees and traverse the tree structure to extract syntactic information and relationships.
    inputs:
      - source_code (string)
      - language (string)
      - grammar_version (string)
    outputs:
      - ast_tree (TreeNode[])
      - parse_errors (ParseError[])
      - token_stream (Token[])
    complexity: High
    knowledge_atoms:
      - KA-037 (AST/CFG/DFG/CPG analysis, Tree-sitter integration)
    dependencies:
      - Tree-sitter grammar loading capability
      - Incremental parsing support

  control_flow_graph_construction:
    id: DOM-015-SK-002
    name: Control Flow Graph Construction
    description: Analyze code structure and build control flow graphs representing all possible execution paths through the code.
    inputs:
      - ast_tree (TreeNode[])
      - function_scope (CodeBlock)
      - language_semantics (LanguageSpec)
    outputs:
      - cfg_nodes (CFGNode[])
      - cfg_edges (CFGEdge[])
      - entry_points (CFGNode[])
      - exit_points (CFGNode[])
    complexity: High
    knowledge_atoms:
      - KA-037 (CFG analysis)
    handles:
      - Branching (if/else, switch)
      - Loops (for, while, do-while)
      - Exception handling
      - Function calls
      - Non-deterministic paths

  data_flow_graph_analysis:
    id: DOM-015-SK-003
    name: Data Flow Graph Analysis
    description: Track variable definitions, uses, and dependencies across code to understand data movement and transformations.
    inputs:
      - ast_tree (TreeNode[])
      - symbol_table (SymbolTable)
      - cfg_nodes (CFGNode[])
    outputs:
      - dfg_nodes (DFGNode[])
      - dfg_edges (DFGEdge[])
      - def_use_chains (DefUseChain[])
      - reaching_definitions (ReachingDef[])
    complexity: High
    knowledge_atoms:
      - KA-037 (DFG analysis)
    enables:
      - Liveness analysis
      - Available expression analysis
      - Very busy expression analysis

  code_property_graph_generation:
    id: DOM-015-SK-004
    name: Code Property Graph Generation
    description: Combine AST, CFG, and DFG into unified Code Property Graph enabling comprehensive code analysis at multiple abstraction levels.
    inputs:
      - ast_tree (TreeNode[])
      - cfg_nodes (CFGNode[])
      - dfg_nodes (DFGNode[])
      - semantic_info (SemanticInfo)
    outputs:
      - cpg (CodePropertyGraph)
      - cpg_serialized (GraphML | JSON)
      - node_metadata (Map<NodeID, Metadata>)
    complexity: High
    knowledge_atoms:
      - KA-037 (CPG generation)
    integration_targets:
      - Code generation (AGT-017)
      - Refactoring analysis (AGT-018)
      - Debugging (AGT-026)

  tree_sitter_grammar_integration:
    id: DOM-015-SK-005
    name: Tree-sitter Grammar Integration
    description: Load, validate, and apply Tree-sitter grammars for incremental parsing with performance optimization on large files.
    inputs:
      - language (string)
      - grammar_source (URL | Path)
      - grammar_version (semver)
    outputs:
      - grammar_parser (Parser)
      - supported_constructs (LanguageConstruct[])
      - parsing_performance_profile (PerformanceProfile)
    complexity: Medium
    knowledge_atoms:
      - KA-037 (Tree-sitter integration)
    ensures:
      - Incremental parsing on edits
      - Error recovery
      - Language version compatibility

  cross_language_ast_normalization:
    id: DOM-015-SK-006
    name: Cross-Language AST Normalization
    description: Normalize ASTs from different languages into a common representation enabling language-agnostic code analysis.
    inputs:
      - ast_tree (TreeNode[])
      - source_language (string)
      - target_abstraction (AbstractionLevel)
    outputs:
      - normalized_ast (NormalizedAST)
      - normalization_mapping (BiMap<SourceNode, NormalizedNode>)
      - coverage_report (Map<LanguageFeature, bool>)
    complexity: High
    supported_languages:
      - Python, JavaScript/TypeScript, Java, C/C++, Go, Rust, C#
    abstraction_levels:
      - Statement-level
      - Expression-level
      - Declaration-level

  # SD-015b: Semantic Search Skills
  semantic_code_search:
    id: DOM-015-SK-007
    name: Semantic Code Search using Embeddings
    description: Search codebase using semantic embeddings to find functionally similar code regardless of syntactic differences.
    inputs:
      - query (string | CodeSnippet)
      - embedding_model (EmbeddingModel)
      - search_scope (CodeRange[])
      - top_k (int)
    outputs:
      - results (SearchResult[])
      - relevance_scores (float[])
      - result_explanations (string[])
    complexity: High
    dependencies:
      - Code embedding model (pre-trained)
      - Vector index (FAISS, Annoy, or equivalent)
    enables:
      - Function similarity detection
      - Copy-paste detection
      - Refactoring opportunity identification

  natural_language_to_code_search:
    id: DOM-015-SK-008
    name: Natural Language to Code Search
    description: Convert natural language descriptions into code search queries and return matching code artifacts.
    inputs:
      - nl_query (string)
      - domain_context (DomainKnowledge)
      - language (string)
    outputs:
      - code_results (CodeArtifact[])
      - search_explanation (string)
      - confidence_scores (float[])
    complexity: High
    powered_by:
      - NL→Code embeddings
      - Code annotation/documentation
    handles:
      - Intent extraction
      - Entity recognition (function, class, pattern names)
      - Temporal/structural relationships

  concept_based_code_discovery:
    id: DOM-015-SK-009
    name: Concept-Based Code Discovery
    description: Discover code implementing specific programming concepts (design patterns, algorithms, idioms) across the codebase.
    inputs:
      - concept (ProgrammingConcept)
      - codebase_graph (CodePropertyGraph)
      - language (string)
    outputs:
      - implementations (CodeLocation[])
      - pattern_matches (PatternMatch[])
      - confidence_scores (float[])
    complexity: Medium
    concepts_supported:
      - Design patterns (Singleton, Observer, Factory, etc.)
      - Algorithms (sorting, searching, graph traversal)
      - Idioms (property getters/setters, builder pattern)
      - Anti-patterns (God object, spaghetti code)

  semantic_similarity_scoring:
    id: DOM-015-SK-010
    name: Semantic Similarity Scoring
    description: Calculate semantic similarity between code artifacts using multiple similarity metrics and aggregation strategies.
    inputs:
      - artifact_a (CodeArtifact)
      - artifact_b (CodeArtifact)
      - similarity_metrics (SimilarityMetric[])
      - aggregation_strategy (AggregationMethod)
    outputs:
      - similarity_score (float [0, 1])
      - metric_breakdown (Map<Metric, float>)
      - explanation (string)
    complexity: Medium
    metrics_supported:
      - Cosine similarity (embeddings)
      - Structural similarity (AST)
      - Syntactic similarity (token overlap)
      - Semantic similarity (data flow)

  # SD-015c: Codebase Mapping Skills
  codebase_structure_mapping:
    id: DOM-015-SK-011
    name: Codebase Structure Mapping
    description: Scan entire codebase and create comprehensive map of all modules, packages, files, and their organization.
    inputs:
      - root_path (Path)
      - include_patterns (Glob[])
      - exclude_patterns (Glob[])
      - depth_limit (int)
    outputs:
      - structure_map (CodebaseMap)
      - file_inventory (FileNode[])
      - directory_hierarchy (DirNode[])
      - total_loc (int)
    complexity: Medium
    handles:
      - Multi-language codebases
      - Symlinks
      - Generated code detection
      - Build artifact filtering

  dependency_graph_extraction:
    id: DOM-015-SK-012
    name: Dependency Graph Extraction
    description: Extract all dependencies (imports, requires, includes) and build complete dependency graph for the codebase.
    inputs:
      - codebase_map (CodebaseMap)
      - ast_trees (Map<File, AST>)
      - language_import_rules (ImportRuleSet)
    outputs:
      - dependency_graph (DependencyGraph)
      - import_edges (ImportEdge[])
      - circular_dependencies (Cycle[])
      - dependency_layers (Layer[])
    complexity: High
    detects:
      - Direct imports
      - Transitive dependencies
      - Circular dependencies
      - Unused imports
      - Missing dependencies

  module_relationship_visualization:
    id: DOM-015-SK-013
    name: Module Relationship Visualization
    description: Generate visual representations of module relationships and architectural layers for comprehension and analysis.
    inputs:
      - dependency_graph (DependencyGraph)
      - layout_algorithm (LayoutAlgorithm)
      - visualization_format (Format)
    outputs:
      - visualization (GraphViz | Mermaid | SVG)
      - architecture_layers (ArchLayer[])
      - coupling_metrics (CouplingMetric[])
    complexity: Medium
    formats:
      - Graphviz DOT
      - Mermaid diagram
      - Interactive SVG
      - ASCII art

  call_graph_construction:
    id: DOM-015-SK-014
    name: Call Graph Construction and Analysis
    description: Build call graphs showing all function/method invocations and analyze call patterns for reachability and complexity.
    inputs:
      - ast_trees (Map<File, AST>)
      - cfg_nodes (Map<Function, CFG>)
      - symbol_table (SymbolTable)
    outputs:
      - call_graph (CallGraph)
      - call_edges (CallEdge[])
      - entry_points (Function[])
      - strongly_connected_components (SCC[])
    complexity: High
    enables:
      - Dead code detection
      - Reachability analysis
      - Call path tracing
      - Recursion detection
      - Complexity analysis

  architectural_pattern_detection:
    id: DOM-015-SK-015
    name: Architectural Pattern Detection
    description: Identify architectural patterns (layered, microservices, MVC, etc.) from codebase structure and relationships.
    inputs:
      - codebase_map (CodebaseMap)
      - dependency_graph (DependencyGraph)
      - module_boundaries (ModuleBoundary[])
    outputs:
      - detected_patterns (Pattern[])
      - pattern_confidence (float[])
      - architecture_description (string)
    complexity: High
    patterns:
      - Layered architecture
      - Microservices
      - MVC/MVVM
      - Domain-driven design
      - Vertical slicing
      - Modular monolith

  # SD-015d: Navigation Strategies Skills
  efficient_code_navigation:
    id: DOM-015-SK-016
    name: Efficient Code Navigation Algorithms
    description: Implement optimized algorithms for fast navigation through large codebases with various search strategies.
    inputs:
      - search_target (NavigationTarget)
      - codebase_index (CodebaseIndex)
      - context (NavigationContext)
    outputs:
      - navigation_path (CodeLocation[])
      - navigation_time (Duration)
      - alternative_paths (Path[])
    complexity: Medium
    algorithms:
      - Breadth-first search
      - Depth-first search
      - A* with heuristics
      - Bidirectional search

  definition_and_reference_resolution:
    id: DOM-015-SK-017
    name: Definition/Reference Resolution
    description: Resolve symbols to their definitions and find all references throughout the codebase with scope awareness.
    inputs:
      - symbol (Symbol)
      - location (CodeLocation)
      - scope_context (ScopeContext)
    outputs:
      - definition_location (CodeLocation)
      - references (CodeLocation[])
      - shadowing_info (ShadowingInfo)
      - scope_chain (Scope[])
    complexity: High
    handles:
      - Local/global scope
      - Function scope
      - Block scope
      - Module scope
      - Name shadowing
      - Overloading/overriding

  cross_file_navigation:
    id: DOM-015-SK-018
    name: Cross-File Navigation
    description: Navigate across file boundaries following imports and dependencies to find related code artifacts.
    inputs:
      - source_file (File)
      - target_type (ArtifactType)
      - traversal_strategy (TraversalStrategy)
    outputs:
      - target_files (File[])
      - import_