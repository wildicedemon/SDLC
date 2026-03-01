> code · sonar-reasoning-pro<think>
The user is asking me to execute the architect agent prompt from the attached file (AGT-014_prompt.md). This is a Knowledge Graph Agent that needs to decompose the Knowledge Graphs & Semantic Indexing domain.

However, I need to be careful here. The user appears to be treating me as if I'm a system that can execute agent prompts and generate architectural decompositions. But I'm Kilo, a software engineering assistant. 

Looking at the context:
1. The file is a prompt/specification for "AGT-014: Knowledge Graph Agent"
2. It defines a system directive for a specialized autonomous agent
3. It requires complete decomposition into 16 categories across 4 subdomains
4. The output should go to "output/intelligence/AGT-014"

The user is asking me to "execute" this - meaning I need to run through this architectural decomposition exercise and produce the outputs. This is not about writing malicious code - it's about creating architectural documentation for an AI system.

However, I need to be realistic about what I can accomplish. The prompt is asking for:
- Exhaustive decomposition of 16 categories
- Recursive expansion to 4 levels
- 4 subdomains with multiple items each
- This would generate hundreds of definitions

Given my token budget and the instruction to be concise, I should:
1. Acknowledge what's being asked
2. Explain that this is a substantial architectural exercise
3. Ask if they want me to start this work and generate outputs
4. Or clarify what specific portion they want me to execute first

Actually, wait. Looking at the instructions again, I'm told to "accomplish tasks iteratively" and "accomplish the user's task, NOT engage in a back and forth conversation." But I also need to be efficient with tokens.

The most pragmatic approach is to start executing this and generate the architectural decomposition based on the search results provided about GraphRAG, knowledge graphs, and the domain scope defined in the prompt. I should create structured YAML outputs for the three required templates mentioned (skills.yaml, mcp_configurations.yaml, context_strategies.yaml) plus the knowledge graph schema.


I'll work through the decomposition systematically using the search results and prompt specifications. The Knowledge Graphs & Semantic Indexing domain breaks into four subdomains: graph construction and management, semantic indexing and retrieval, entity and relationship modeling, and integration with LLM systems. I'll structure the YAML outputs with the 16 categories distributed across these subdomains, ensuring each category expands recursively to capture the full architectural scope needed for the agent.
</think>

I'll execute the AGT-014 Knowledge Graph Agent architectural decomposition using the provided search results and domain specifications.

```bash
mkdir -p "output/intelligence/AGT-014"
```

Generating comprehensive architectural decomposition:

**output/intelligence/AGT-014/knowledge_graph_schema.yaml**
```yaml
version: "1.0"
domain: "DOM-014: Knowledge Graphs & Semantic Indexing"

subdomains:
  SD-014a: "Graph Construction"
  SD-014b: "GraphRAG Integration"
  SD-014c: "Vector Search"
  SD-014d: "Semantic Indexing"

# SKILLS (DOM-014-SK-[NNN])
skills:
  DOM-014-SK-001:
    name: "Knowledge Graph Schema Design"
    description: "Design entity and relationship schemas for domain-specific knowledge graphs with proper typing, metadata, and provenance tracking."
    inputs: ["domain_requirements", "entity_definitions", "relationship_taxonomy"]
    outputs: ["kg_schema.yaml", "entity_type_mapping", "relationship_type_mapping"]
    complexity: "High"
    subdomain: "SD-014a"

  DOM-014-SK-002:
    name: "Entity and Relationship Extraction"
    description: "Extract entities, relationships, and claims from unstructured text using LLM-based and rule-based NLP techniques."
    inputs: ["unstructured_text", "entity_type_definitions", "relationship_patterns"]
    outputs: ["extracted_entities[]", "extracted_relationships[]", "confidence_scores"]
    complexity: "High"
    subdomain: "SD-014a"
    references: ["[2]", "[4]", "[5]"]

  DOM-014-SK-003:
    name: "Graph Population Pipeline"
    description: "Construct and populate knowledge graphs in graph databases (Neo4j, Neptune) with extracted entities, relationships, and provenance metadata."
    inputs: ["extracted_entities", "extracted_relationships", "graph_database_config"]
    outputs: ["graph_database", "population_statistics", "quality_metrics"]
    complexity: "Medium"
    subdomain: "SD-014a"
    references: ["[1]", "[3]"]

  DOM-014-SK-004:
    name: "Graph Quality Validation"
    description: "Validate knowledge graph consistency, detect contradictions, verify relationship integrity, and measure data quality metrics."
    inputs: ["knowledge_graph", "validation_rules", "consistency_constraints"]
    outputs: ["quality_report", "inconsistency_list", "remediation_plan"]
    complexity: "Medium"
    subdomain: "SD-014a"

  DOM-014-SK-005:
    name: "GraphRAG Pipeline Construction"
    description: "Integrate knowledge graphs with RAG pipelines to enable graph-enhanced retrieval with subgraph extraction and context augmentation."
    inputs: ["knowledge_graph", "rag_config", "embedding_model", "llm_model"]
    outputs: ["graphrag_pipeline", "retrieval_index", "augmentation_strategy"]
    complexity: "High"
    subdomain: "SD-014b"
    references: ["[1]", "[2]", "[3]", "[5]"]

  DOM-014-SK-006:
    name: "Subgraph Extraction"
    description: "Extract bounded subgraphs from knowledge graphs using graph traversal with configurable depth, relationship types, and entity filters."
    inputs: ["seed_nodes", "extraction_depth", "relationship_filters", "knowledge_graph"]
    outputs: ["subgraph", "traversal_path", "context_metadata"]
    complexity: "Medium"
    subdomain: "SD-014b"
    references: ["[2]"]

  DOM-014-SK-007:
    name: "Hybrid Search Query Optimization"
    description: "Optimize queries combining vector similarity, graph traversal, and keyword matching for efficient multi-modal retrieval."
    inputs: ["user_query", "vector_index", "knowledge_graph", "search_config"]
    outputs: ["optimized_query", "results_ranking", "retrieval_metrics"]
    complexity: "High"
    subdomain: "SD-014c"
    references: ["[1]"]

  DOM-014-SK-008:
    name: "Vector Embedding Generation"
    description: "Generate and manage vector embeddings for documents, chunks, entities, and relationships using stable embedding models."
    inputs: ["text_content", "embedding_model", "batch_config"]
    outputs: ["embedding_vectors[]", "metadata_mapping", "model_version"]
    complexity: "Medium"
    subdomain: "SD-014c"

  DOM-014-SK-009:
    name: "Vector Search Index Construction"
    description: "Build approximate nearest neighbor (ANN) indexes using FAISS, Chroma, Pinecone, or similar technologies with optimal configuration."
    inputs: ["embeddings[]", "index_config", "storage_backend"]
    outputs: ["search_index", "index_metadata", "performance_stats"]
    complexity: "Medium"
    subdomain: "SD-014c"
    references: ["[1]"]

  DOM-014-SK-010:
    name: "Semantic Codebase Indexing"
    description: "Extract semantic concepts from code repositories, build hierarchical code-to-concept mappings, and enable cross-language semantic search."
    inputs: ["code_repository", "language_parsers", "concept_taxonomy"]
    outputs: ["semantic_index", "code_concept_map", "traversal_graph"]
    complexity: "High"
    subdomain: "SD-014d"

  DOM-014-SK-011:
    name: "Incremental Index Updates"
    description: "Efficiently update semantic and vector indexes when code or documentation changes without full rebuilds."
    inputs: ["change_set", "existing_index", "update_strategy"]
    outputs: ["updated_index", "index_diff", "staleness_metrics"]
    complexity: "Medium"
    subdomain: "SD-014d"

  DOM-014-SK-012:
    name: "Graph-Aware Prompt Augmentation"
    description: "Augment LLM prompts with relevant graph context, entity information, and relationship chains to improve reasoning and accuracy."
    inputs: ["original_prompt", "subgraph", "entity_context", "relationship_chains"]
    outputs: ["augmented_prompt", "context_tokens", "relevance_scores"]
    complexity: "Medium"
    subdomain: "SD-014b"
    references: ["[3]"]

  DOM-014-SK-013:
    name: "Embedding Model Management"
    description: "Monitor, version, and migrate embedding models while ensuring backward compatibility and consistency across all indexes."
    inputs: ["embedding_models[]", "version_manifest", "migration_config"]
    outputs: ["model_registry", "compatibility_matrix", "migration_plan"]
    complexity: "Medium"
    subdomain: "SD-014c"
    references: ["[1]"]

  DOM-014-SK-014:
    name: "Community Detection and Hierarchical Clustering"
    description: "Detect entity communities in knowledge graphs using Leiden algorithm and build hierarchical community summaries for multi-level retrieval."
    inputs: ["knowledge_graph", "clustering_config", "community_depth"]
    outputs: ["community_hierarchy", "community_summaries", "cluster_metrics"]
    complexity: "High"
    subdomain: "SD-014a"
    references: ["[5]"]

# WORKFLOWS (DOM-014-WF-[NNN])
workflows:
  DOM-014-WF-001:
    name: "Knowledge Graph Construction Workflow"
    trigger: "New data ingestion or graph rebuild requested"
    steps:
      - step: 1
        name: "Schema Definition"
        entry_criteria: ["domain_requirements_available"]
        exit_criteria: ["kg_schema_approved"]
        action: "Use DOM-014-SK-001 to design graph schema"
      
      - step: 2
        name: "Data Extraction"
        entry_criteria: ["kg_schema_defined", "raw_data_available"]
        exit_criteria: ["entities_extracted", "relationships_extracted"]
        action: "Use DOM-014-SK-002 to extract entities and relationships"
      
      - step: 3
        name: "Graph Population"
        entry_criteria: ["extracted_data_available"]
        exit_criteria: ["graph_populated", "indexes_created"]
        action: "Use DOM-014-SK-003 to populate graph database"
      
      - step: 4
        name: "Quality Validation"
        entry_criteria: ["graph_populated"]
        exit_criteria: ["validation_complete", "quality_threshold_met"]
        action: "Use DOM-014-SK-004 to validate graph"
      
      - step: 5
        name: "Community Detection"
        entry_criteria: ["graph_validated"]
        exit_criteria: ["communities_detected", "hierarchy_built"]
        action: "Use DOM-014-SK-014 to detect communities"
    
    completion_criteria: "Graph is populated, validated, indexed, and ready for queries"
    rollback_plan: "Restore previous graph backup, revert schema changes, re-run validation"
    subdomain: "SD-014a"
    references: ["[2]", "[3]", "[5]"]

  DOM-014-WF-002:
    name: "GraphRAG Retrieval Pipeline Workflow"
    trigger: "User query received; requires graph-enhanced context"
    steps:
      - step: 1
        name: "Query Analysis"
        entry_criteria: ["user_query_received"]
        exit_criteria: ["query_analyzed", "intent_determined"]
        action: "Parse query and determine retrieval strategy"
      
      - step: 2
        name: "Subgraph Extraction"
        entry_criteria: ["query_analyzed"]
        exit_criteria: ["subgraph_extracted", "depth_bounded"]
        action: "Use DOM-014-SK-006 to extract relevant subgraph"
      
      - step: 3
        name: "Context Augmentation"
        entry_criteria: ["subgraph_extracted"]
        exit_criteria: ["prompt_augmented", "context_assembled"]
        action: "Use DOM-014-SK-012 to augment prompt with graph context"
      
      - step: 4
        name: "Hybrid Search"
        entry_criteria: ["prompt_augmented"]
        exit_criteria: ["vector_results", "graph_results", "combined_ranking"]
        action: "Use DOM-014-SK-007 to perform hybrid search"
      
      - step: 5
        name: "Response Generation"
        entry_criteria: ["search_complete"]
        exit_criteria: ["response_generated", "provenance_tracked"]
        action: "Generate LLM response using augmented context"
    
    completion_criteria: "Response generated with traced provenance to graph entities"
    rollback_plan: "Reduce subgraph depth, fall back to vector search, timeout after max_latency"
    subdomain: "SD-014b"
    references: ["[1]", "[2]", "[3]"]

  DOM-014-WF-003:
    name: "Semantic Index Build and Update Workflow"
    trigger: "Codebase snapshot or change detection"
    steps:
      - step: 1
        name: "Code Analysis"
        entry_criteria: ["code_repository_available"]
        exit_criteria: ["semantic_concepts_extracted"]
        action: "Use DOM-014-SK-010 to extract semantic concepts from code"
      
      - step: 2
        name: "Embedding Generation"
        entry_criteria: ["semantic_concepts_extracted"]
        exit_criteria: ["embeddings_generated", "model_version_recorded"]
        action: "Use DOM-014-SK-008 to generate embeddings"
      
      - step: 3
        name: "Index Construction"
        entry_criteria: ["embeddings_available"]
        exit_criteria: ["index_built", "search_ready"]
        action: "Use DOM-014-SK-009 to build search indexes"
      
      - step: 4
        name: "Staleness Monitoring"
        entry_criteria: ["index_ready"]
        exit_criteria: ["monitoring_active"]
        action: "Activate staleness detection; track code changes"
    
    completion_criteria: "Semantic index is built, ready, and monitoring changes"
    rollback_plan: "Restore previous index snapshot; re-run embedding generation"
    subdomain: "SD-014d"

  DOM-014-WF-004:
    name: "Graph Validation and Consistency Check Workflow"
    trigger: "Scheduled check or manual validation request"
    steps:
      - step: 1
        name: "Consistency Scan"
        entry_criteria: ["knowledge_graph_available"]
        exit_criteria: ["inconsistencies_detected"]
        action: "Scan for contradictory relationships and broken references"
      
      - step: 2
        name: "Provenance Verification"
        entry_criteria: ["consistency_scan_complete"]
        exit_criteria: ["provenance_verified"]
        action: "Verify all entities have source references and metadata"
      
      - step: 3
        name: "Remediation"
        entry_criteria: ["issues_detected"]
        exit_criteria: ["remediation_complete", "validation_passed"]
        action: "Apply fixes, merge duplicates, or flag unresolvable conflicts"
    
    completion_criteria: "Graph passes all consistency checks or issues are documented"
    rollback_plan: "Restore to last known-good graph state"
    subdomain: "SD-014a"

  DOM-014-WF-005:
    name: "Incremental Index Update Workflow"
    trigger: "Code change detected; staleness threshold exceeded"
    steps:
      - step: 1
        name: "Change Detection"
        entry_criteria: ["file_change_event"]
        exit_criteria: ["change_set_identified"]
        action: "Identify modified code files and semantic impact"
      
      - step: 2
        name: "Selective Re-indexing"
        entry_criteria: ["change_set_identified"]
        exit_criteria: ["affected_concepts_reindexed"]
        action: "Use DOM-014-SK-011 to incrementally update indexes"
      
      - step: 3
        name: "Validation and Activation"
        entry_criteria: ["reindexing_complete"]
        exit_criteria: ["new_index_active"]
        action: "Validate updated index; activate for queries"
    
    completion_criteria: "Updated index is validated and active;