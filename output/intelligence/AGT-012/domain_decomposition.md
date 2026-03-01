> code · sonar-reasoning-pro<think>
The user is asking me to execute the architect agent prompt from a file. This appears to be part of an SDLC (Software Development Lifecycle) system with agents, domains, and structured decomposition requirements.

Looking at the file content, it's the prompt for "Agent AGT-012: Memory Systems Agent" - a specialized autonomous agent responsible for decomposing the Memory Systems & Persistence domain within an agentic AI coding system architecture.

The prompt is very detailed and asks me to:
1. Decompose the Memory Systems & Persistence domain (DOM-012)
2. Create 16 categories of outputs (Skills, Workflows, Task Templates, Rules & Constraints, Interfaces, Dependencies, State Models, Data Models, Control Flows, Failure Modes & Recovery, Optimization Strategies, Coordination Mechanisms, Context Requirements, Memory Structures, Monitoring Requirements, Evolution Mechanisms)
3. Recursively expand subdomains (SD-012a, SD-012b, SD-012c, SD-012d)
4. Output to `output/intelligence/AGT-012`

This is asking me to act as the Memory Systems Agent (AGT-012) and produce comprehensive documentation about memory architecture for agentic AI systems.

However, I need to be careful here. This seems like a legitimate SDLC/architecture exercise, but I should:
1. Check if this directory structure exists
2. Execute the task by creating the required outputs
3. Place them in the output directory as requested

The task is to decompose the Memory Systems & Persistence domain comprehensively across those 16 categories. This is a complex architectural task that requires me to synthesize knowledge from:
- The search results about agentic AI memory systems
- The prompt requirements
- Architectural best practices

Let me start by creating the output directory and then generating the comprehensive decomposition.
</think>

I'll execute the AGT-012 Memory Systems Agent prompt and generate the comprehensive domain decomposition to `output/intelligence/AGT-012`.

First, let me create the output directory structure and generate the memory systems architecture artifacts:

```bash
mkdir -p output/intelligence/AGT-012
```

Now I'll create the primary output artifact - the complete memory systems decomposition:

```yaml
# output/intelligence/AGT-012/memory_architecture.yaml
domain_id: DOM-012
domain_name: Memory Systems & Persistence
agent: AGT-012
execution_phase: Phase 3 (Intelligence)
generated_timestamp: 2026-03-01T15:59:30Z

# ============================================================================
# 1. SKILLS (DOM-012-SK-*)
# ============================================================================

skills:
  SK-001:
    name: Memory Architecture Design
    description: Design multi-tier memory systems integrating short-term working memory, long-term persistent storage, and vector embeddings for optimal agent cognition and retrieval.
    inputs: [agent_objectives, task_complexity, domain_context, storage_constraints]
    outputs: [memory_tier_specification, integration_patterns, scalability_roadmap]
    complexity: High
    
  SK-002:
    name: Vector Embedding Generation
    description: Transform semantic content into high-dimensional vector representations using configured embedding models with consistency guarantees across sessions.
    inputs: [raw_content, embedding_model_spec, domain_vocabulary]
    outputs: [vector_embeddings, embedding_metadata, confidence_scores]
    complexity: Medium
    
  SK-003:
    name: Similarity Search Execution
    description: Execute optimized vector similarity searches against indexed embeddings using distance metrics, with tuning for recall/precision tradeoffs.
    inputs: [query_vector, index_config, distance_metric, k_results]
    outputs: [ranked_results, similarity_scores, search_latency_metrics]
    complexity: Medium
    
  SK-004:
    name: Memory Consolidation (Short→Long)
    description: Consolidate ephemeral working memory into persistent long-term storage while preserving semantic integrity and preventing information loss.
    inputs: [short_term_memory_buffer, consolidation_policy, retention_rules]
    outputs: [consolidated_memory_entries, archival_manifest, loss_audit_log]
    complexity: High
    
  SK-005:
    name: Retrieval-Augmented Generation (RAG) Execution
    description: Orchestrate RAG pipeline to retrieve relevant context, rank results, and inject curated knowledge into agent reasoning processes.
    inputs: [query, retrieval_config, ranking_strategy, context_window_limit]
    outputs: [ranked_context_results, retrieval_provenance, confidence_metadata]
    complexity: High
    
  SK-006:
    name: Hallucination-Aware Retrieval Filtering
    description: Filter retrieved results against known hallucination patterns (KA-013: 19.7% fabricated package rate) and flag unreliable content with confidence scores.
    inputs: [retrieved_results, hallucination_patterns_db, confidence_thresholds]
    outputs: [filtered_results, hallucination_flags, reliability_scores]
    complexity: High
    
  SK-007:
    name: Memory Decay Management
    description: Implement time-based and access-frequency-based decay policies to gracefully age out stale memories while preserving evergreen knowledge.
    inputs: [memory_entries, decay_policy, access_history, importance_weights]
    outputs: [decayed_entries, decay_schedule, expiration_markers]
    complexity: Medium
    
  SK-008:
    name: Re-ranking and Relevance Scoring
    description: Apply multi-stage re-ranking algorithms to improve retrieval quality by considering query-result semantic alignment, recency, and domain-specific relevance signals.
    inputs: [initial_results, ranking_signals, query_context, domain_rules]
    outputs: [reranked_results, relevance_scores, ranking_rationale]
    complexity: High
    
  SK-009:
    name: Memory Integrity Validation
    description: Validate memory entries against semantic constraints, consistency rules, and vulnerability indicators (KA-014) to detect corruption or poisoning.
    inputs: [memory_entries, validation_rules, threat_patterns]
    outputs: [validation_report, integrity_violations, remediation_actions]
    complexity: High
    
  SK-010:
    name: Vector Index Optimization
    description: Tune vector database indexing strategies (quantization, partitioning, replication) to optimize search latency, recall, and storage efficiency.
    inputs: [vector_corpus, query_patterns, storage_constraints, latency_targets]
    outputs: [optimized_index_config, performance_baseline, tuning_recommendations]
    complexity: High

# ============================================================================
# 2. WORKFLOWS (DOM-012-WF-*)
# ============================================================================

workflows:
  WF-001:
    name: Memory Consolidation Workflow
    trigger: On schedule (configurable interval) OR on threshold (working memory exceeds limit)
    steps:
      - step: 1
        action: Select consolidation candidates from working memory buffer
        entry_criteria: Memory buffer populated with session interactions
        exit_criteria: Candidates identified with consolidation priority scores
      - step: 2
        action: Validate semantic integrity and detect duplicates
        entry_criteria: Candidates selected
        exit_criteria: Deduplicated, integrity-validated candidate set
      - step: 3
        action: Generate/update embeddings for persistent entries
        entry_criteria: Validated candidate set
        exit_criteria: Vector embeddings computed and indexed
      - step: 4
        action: Persist to long-term memory with metadata
        entry_criteria: Embeddings ready
        exit_criteria: Entries stored in persistent layer with audit trail
      - step: 5
        action: Purge consolidation candidates from working memory
        entry_criteria: Persistence confirmed
        exit_criteria: Working memory buffer reduced
    completion_criteria: All candidates persisted, working memory freed, audit logged
    rollback_plan: Restore working memory from transaction log; skip consolidation for failed batch; alert monitoring

  WF-002:
    name: RAG Retrieval Pipeline Workflow
    trigger: Agent requires context for reasoning task
    steps:
      - step: 1
        action: Format query according to context strategies (DOM-011)
        entry_criteria: Raw agent query
        exit_criteria: Formatted query with metadata (domain, intent, keywords)
      - step: 2
        action: Generate query embeddings
        entry_criteria: Formatted query
        exit_criteria: Query vector with confidence scores
      - step: 3
        action: Execute similarity search against indexed vectors
        entry_criteria: Query vector ready
        exit_criteria: Top-k candidate results with similarity scores
      - step: 4
        action: Apply hallucination detection filters (KA-013)
        entry_criteria: Candidate results
        exit_criteria: Hallucination-flagged results with reliability scores
      - step: 5
        action: Re-rank results using multi-stage ranker
        entry_criteria: Filtered candidates
        exit_criteria: Re-ranked results with final relevance scores
      - step: 6
        action: Format results for reasoning context injection
        entry_criteria: Ranked results
        exit_criteria: Contextualized results ready for agent reasoning
    completion_criteria: Results formatted, metadata attached, provenance tracked
    rollback_plan: Return empty context; log retrieval failure; escalate to fallback reasoning

  WF-003:
    name: Vector DB Indexing Workflow
    trigger: On new large batch of memory entries OR periodic index maintenance
    steps:
      - step: 1
        action: Partition vectors into index shards (if using sharding)
        entry_criteria: Vector batch ready
        exit_criteria: Shards allocated to index partitions
      - step: 2
        action: Build/update index structures (tree, graph, hash)
        entry_criteria: Sharded vectors
        exit_criteria: Index structures built with performance metrics
      - step: 3
        action: Validate index integrity and query coverage
        entry_criteria: Index built
        exit_criteria: Index passes integrity checks; test queries return expected results
      - step: 4
        action: Activate index for production queries
        entry_criteria: Validation passed
        exit_criteria: Index serving queries; old index remains for fallback
      - step: 5
        action: Monitor index performance and queue stale index for cleanup
        entry_criteria: Index active
        exit_criteria: Performance metrics baseline established
    completion_criteria: Index online, performance baseline met, old index scheduled for removal
    rollback_plan: Revert to previous index version; investigate build failure; alert ops

  WF-004:
    name: Memory Cleanup and Decay Workflow
    trigger: On schedule (daily/weekly) OR on threshold (total memory exceeds capacity)
    steps:
      - step: 1
        action: Identify memory entries subject to decay
        entry_criteria: Current memory state
        exit_criteria: Entries marked with decay eligibility
      - step: 2
        action: Apply decay function based on access patterns and age
        entry_criteria: Eligible entries
        exit_criteria: Entries with updated decay scores
      - step: 3
        action: Identify expired entries per retention policy
        entry_criteria: Decayed entries
        exit_criteria: Expiration list with justification
      - step: 4
        action: Archive or purge expired entries
        entry_criteria: Expiration list
        exit_criteria: Entries removed from active memory; archive created
      - step: 5
        action: Update vector index to reflect removals
        entry_criteria: Entries purged
        exit_criteria: Index stale markers removed, rebuild scheduled if needed
    completion_criteria: Memory freed, archive created, index updated
    rollback_plan: Restore from archive if needed; revert index changes; alert if capacity remains

  WF-005:
    name: Memory Integrity Validation Workflow
    trigger: On schedule (hourly) OR on anomaly detection
    steps:
      - step: 1
        action: Sample memory entries across all tiers
        entry_criteria: Validation triggered
        exit_criteria: Representative sample selected
      - step: 2
        action: Validate semantic consistency and detect anomalies
        entry_criteria: Sample entries
        exit_criteria: Anomalies flagged with confidence scores
      - step: 3
        action: Check against hallucination patterns and vulnerability indicators
        entry_criteria: Anomalies identified
        exit_criteria: Threat assessment completed
      - step: 4
        action: Generate integrity report and recommendations
        entry_criteria: Threat assessment
        exit_criteria: Report with remediation actions
      - step: 5
        action: Alert if integrity compromised or quarantine suspicious entries
        entry_criteria: Report completed
        exit_criteria: Notifications sent; suspicious entries isolated
    completion_criteria: Validation report generated; alerts sent; suspicious entries quarantined
    rollback_plan: Investigate false positives; refine detection rules; maintain audit trail

# ============================================================================
# 3. TASK TEMPLATES (DOM-012-TT-*)
# ============================================================================

task_templates:
  TT-001:
    name: Memory Lookup Task
    purpose: Retrieve memory entries matching a query with confidence scoring
    structure: |
      input: {query, filter_criteria, max_results, confidence_threshold}
      retrieval: similarity_search(query_embedding, filter_criteria, k=max_results)
      filtering: apply_confidence_filter(results, threshold)
      output: {results, confidence_scores, retrieval_time_ms}

  TT-002:
    name: Memory Store Task
    purpose: Store new memory entry with embeddings and metadata
    structure: |
      input: {content, memory_type, source, priority, retention_days}
      embed: generate_embedding(content)
      validate: check_integrity(content, memory_type)
      store: persist_entry({content, embedding, metadata, timestamp})
      index: update_vector_index()
      output: {entry_id, storage_location, embedding_id}

  TT-003:
    name: Memory Update Task
    purpose: Update existing memory entry and re-index
    structure: |
      input: {entry_id, updated_content, rationale}
      retrieve: fetch_entry(entry_id)
      validate: check_update_consistency(original, updated)
      embed: regenerate_embedding(updated_content)
      persist: update_entry_with_new_embedding()
      reindex: update_vector_index()
      audit: log_update(entry_id, rationale, timestamp)
      output: {entry_id, update_timestamp}

# ============================================================================
# 4. RULES & CONSTRAINTS (DOM-012-RL-*)
# ============================================================================

rules:
  RL-001:
    constraint: Retrieved content must be validated against hallucination indicators (KA-013)
    rationale: AI-generated content has 19.7% fabrication rate; unreliable content corrupts reasoning
    enforcement: Hallucination filter applied to all retrieval results with confidence threshold
    exceptions: Explicit hallucination override for research/exploration tasks with audit logging

  RL-002:
    constraint: Vulnerability-prone code patterns must be flagged on retrieval (KA-014)
    rationale: Generated code contains vulnerability patterns; flagging prevents unsafe execution
    enforcement: Pattern matching against vulnerability DB during retrieval; flag attached to results
    exceptions: None without security review and explicit override

  RL-003:
    constraint: Memory consolidation must preserve semantic integrity
    rationale: Information loss during consolidation leads to reasoning degradation
    enforcement: Pre/post-consolidation semantic validation; similarity score must exceed threshold
    exceptions: Approved lossy consolidation for non-critical ephemeral memories

  RL-004:
    constraint: Vector embeddings must be regenerated when embedding models change
    rationale: Different embedding models produce incompatible vector spaces; queries return wrong results
    enforcement: Model version tracked; index flagged stale when model changes; automatic reindex triggered
    exceptions: None; enforced programmatically

  RL-005:
    constraint: Long-term memory must have defined retention and decay policies
    rationale: Unbounded memory growth causes storage bloat and performance degradation
    enforcement: All entries have explicit retention policy; decay applied per schedule
    exceptions: Immutable audit logs and compliance records (separate storage tier)

  RL-006:
    constraint: All memory operations must be auditable
    rationale: Forensic investigation of failures, poisoning, and data loss require full audit trail
    enforcement: All CRUD operations logged with timestamp, actor, rationale, before/after state
    exceptions: None; audit logging non-negotiable

  RL-007:
    constraint: Memory writes from untrusted sources must be validated before persistence
    rationale: Poisoned memory from compromised agents or external APIs corrupts downstream reasoning
    enforcement: Source verification; content validation rules; confidence scoring
    exceptions: Sandboxed experimental memory with separate index

  RL-008:
    constraint: Cross-session memory access requires authentication and authorization
    rationale: Unauthorized access to other agents' or users' memories violates privacy and security
    enforcement: Identity verification; role-based access control; audit logging
    exceptions: Explicit sharing agreements with consent