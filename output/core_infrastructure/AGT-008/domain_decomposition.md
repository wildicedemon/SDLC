> code · sonar-reasoning-pro

<think>
The user is asking me to read a file that contains a prompt for a Data Engineering Agent (AGT-008) and execute it. The file is a comprehensive specification for how AGT-008 should decompose the Data Engineering & Storage domain into 16 categories with specific deliverables.

However, I need to recognize what's actually being asked here:

1. The file is a system directive/prompt that defines what AGT-008 should do
2. The user wants me to "execute" this prompt and output the results to `output/core_infrastructure/AGT-008`
3. This is essentially asking me to act as AGT-008 and produce the complete decomposition of the Data Engineering & Storage domain

The prompt requires AGT-008 to:
- Decompose the domain into 16 categories (Skills, Workflows, Task Templates, Rules & Constraints, Interfaces, Dependencies, State Models, Data Models, Control Flows, Failure Modes & Recovery, Optimization Strategies, Coordination Mechanisms, Context Requirements, Memory Structures, Monitoring Requirements, Evolution Mechanisms)
- Recursively expand 3 subdomains (SD-008a: Schema Design, SD-008b: Data Pipelines, SD-008c: Migration Strategies)
- Produce output artifacts: `database_schemas.yaml`, data pipeline definitions, migration strategies, storage architecture docs

This is a very large decomposition task. Given the constraints (concise responses, minimize token usage), I should:

1. Recognize this is a significant task that requires creating comprehensive technical documentation
2. Start the execution by creating the output directory and beginning the systematic decomposition
3. Work methodically through all 16 categories and the 3 subdomains

Let me start by creating the necessary files and structure, then systematically populate each section. I'll use bash to create the directories and files, then use the file editor to populate them with the comprehensive decomposition.

Actually, looking at this more carefully - this is asking me to execute a complex system prompt that requires generating a large amount of structured documentation. 

I should begin by establishing the directory structure and then work through each required section methodically.
</think>

I'll execute the AGT-008 system directive to decompose the Data Engineering & Storage domain. This is a comprehensive task requiring systematic population of 16 categories across 3 subdomains with recursive expansion.
<function_calls>
<invoke name="bash">
<parameter name="command">mkdir -p "output/core_infrastructure/AGT-008"</parameter>
</invoke>
</function_calls>

Now generating the complete decomposition:
<function_calls>
<invoke name="createFile">
<parameter name="filePath">output/core_infrastructure/AGT-008/1_skills.yaml</parameter>
<parameter name="content"># DOM-008: Data Engineering & Storage - Skills Decomposition
# Recursive Expansion Level: 3

skills:
  # ============================================================================
  # SD-008a: Schema Design Skills
  # ============================================================================
  
  - skill_id: DOM-008-SK-001
    name: Schema Normalization & ER Modeling
    domain: SD-008a
    description: Design normalized database schemas following ACID/BASE principles; create entity-relationship models; identify functional dependencies and normal forms.
    inputs:
      - Entity definitions from architecture contracts
      - Business relationship mappings
      - Access pattern requirements
    outputs:
      - Normalized ER diagrams
      - Normal form assessment (1NF-5NF)
      - Entity definitions with attributes
    complexity: High
    specializations:
      - DOM-008-SK-001-A: Relational normalization (3NF/BCNF design)
      - DOM-008-SK-001-B: Denormalization strategy (for performance tradeoffs)
      - DOM-008-SK-001-C: Cross-store schema mapping (relational↔document↔graph)

  - skill_id: DOM-008-SK-002
    name: Multi-Storage-Engine Schema Management
    domain: SD-008a
    description: Design schemas that work across SQL, NoSQL (document/key-value), graph, and vector stores; manage schema dialect translation and consistency constraints.
    inputs:
      - Access pattern requirements
      - Scalability targets
      - Consistency requirements
    outputs:
      - Multi-engine schema definitions
      - Storage engine selection justification
      - Cross-store consistency rules
    complexity: High
    specializations:
      - DOM-008-SK-002-A: Relational schema design (PostgreSQL, MySQL)
      - DOM-008-SK-002-B: Document schema design (MongoDB, DynamoDB)
      - DOM-008-SK-002-C: Graph schema design (Neo4j, ArangoDB)
      - DOM-008-SK-002-D: Vector store schema design (Pinecone, Weaviate)
      - DOM-008-SK-002-E: Key-value schema design (Redis, Memcached)

  - skill_id: DOM-008-SK-003
    name: Schema Versioning & Evolution
    domain: SD-008a
    description: Implement schema versioning strategies; track schema history; manage schema compatibility across versions; generate migration paths.
    inputs:
      - Current schema version
      - Desired schema changes
      - Backward compatibility constraints
    outputs:
      - Versioned schema definitions
      - Migration compatibility matrix
      - Deprecation schedules
    complexity: Medium
    specializations:
      - DOM-008-SK-003-A: Semantic versioning for schemas
      - DOM-008-SK-003-B: Compatibility analysis (breaking vs. non-breaking)
      - DOM-008-SK-003-C: Deprecation path planning

  - skill_id: DOM-008-SK-004
    name: Index Design & Query Optimization
    domain: SD-008a
    description: Design optimal indexes for query patterns; analyze query execution plans; balance read/write performance; manage index lifecycle.
    inputs:
      - Query workload patterns
      - Table/collection statistics
      - Storage constraints
    outputs:
      - Index designs (B-tree, hash, full-text, composite)
      - Execution plan analyses
      - Performance improvement estimates
    complexity: High
    specializations:
      - DOM-008-SK-004-A: B-tree and hash index optimization
      - DOM-008-SK-004-B: Composite index design
      - DOM-008-SK-004-C: Full-text and vector index optimization
      - DOM-008-SK-004-D: Partitioning strategy design

  - skill_id: DOM-008-SK-005
    name: Data Integrity & Validation Rules
    domain: SD-008a
    description: Define and implement data integrity constraints (PK, FK, unique, check, domain constraints); implement validation rules; design referential integrity strategies.
    inputs:
      - Entity relationships
      - Business validation rules
      - Constraint dependencies
    outputs:
      - Constraint definitions
      - Validation rule specifications
      - Integrity enforcement mechanisms
    complexity: Medium
    specializations:
      - DOM-008-SK-005-A: Relational constraints (PK, FK, unique)
      - DOM-008-SK-005-B: Domain constraints and checks
      - DOM-008-SK-005-C: Cross-storage consistency validation
      - DOM-008-SK-005-D: Soft delete and temporal constraints

  - skill_id: DOM-008-SK-006
    name: Retention Policy Design
    domain: SD-008a
    description: Design data retention policies; implement data lifecycle management; balance compliance, cost, and performance; design archival strategies.
    inputs:
      - Regulatory requirements
      - Business use cases
      - Storage cost models
    outputs:
      - Retention policy specifications
      - Archival strategies
      - Purge schedules
    complexity: Medium
    specializations:
      - DOM-008-SK-006-A: Compliance-driven retention (GDPR, CCPA, HIPAA)
      - DOM-008-SK-006-B: Hot/warm/cold tier management
      - DOM-008-SK-006-C: Archival and retrieval strategies

  # ============================================================================
  # SD-008b: Data Pipeline Skills
  # ============================================================================

  - skill_id: DOM-008-SK-007
    name: ETL/ELT Pipeline Design
    domain: SD-008b
    description: Design end-to-end Extract-Transform-Load or Extract-Load-Transform pipelines; define data flows; specify transformation logic; implement error handling.
    inputs:
      - Source data specifications
      - Target schema definitions
      - Transformation requirements
    outputs:
      - Pipeline architecture diagrams
      - Data flow specifications
      - Transformation rule definitions
    complexity: High
    specializations:
      - DOM-008-SK-007-A: Batch ETL design
      - DOM-008-SK-007-B: Stream ETL design
      - DOM-008-SK-007-C: Hybrid batch-stream pipelines
      - DOM-008-SK-007-D: Real-time data lake ingestion

  - skill_id: DOM-008-SK-008
    name: Transformation Logic Implementation
    domain: SD-008b
    description: Implement data transformation rules; design idempotent transformations; handle data quality issues; implement enrichment and deduplication logic.
    inputs:
      - Raw data samples
      - Business transformation rules
      - Quality requirements
    outputs:
      - Transformation code/expressions
      - Quality metrics
      - Idempotency proofs
    complexity: High
    specializations:
      - DOM-008-SK-008-A: SQL-based transformations
      - DOM-008-SK-008-B: Python/Scala transformation logic
      - DOM-008-SK-008-C: Semantic data enrichment
      - DOM-008-SK-008-D: Deduplication algorithms

  - skill_id: DOM-008-SK-009
    name: Streaming vs. Batch Processing Selection
    domain: SD-008b
    description: Analyze data requirements to determine optimal processing paradigm; design hybrid approaches; balance latency, throughput, and cost.
    inputs:
      - Data volume and velocity metrics
      - Latency requirements
      - Cost constraints
    outputs:
      - Processing paradigm recommendation
      - Cost-benefit analysis
      - Architecture justification
    complexity: Medium
    specializations:
      - DOM-008-SK-009-A: Batch processing design (Spark, Hadoop)
      - DOM-008-SK-009-B: Stream processing design (Kafka, Flink, Spark Streaming)
      - DOM-008-SK-009-C: Lambda architecture (batch + stream)
      - DOM-008-SK-009-D: Kappa architecture (stream-only)

  - skill_id: DOM-008-SK-010
    name: Pipeline Monitoring & Observability
    domain: SD-008b
    description: Design monitoring systems for pipelines; implement health checks; define SLOs and error budgets; create alerting strategies.
    inputs:
      - Pipeline specifications
      - Business SLAs
      - Failure modes
    outputs:
      - Monitoring metric definitions
      - Alert threshold specifications
      - Dashboard designs
    complexity: Medium
    specializations:
      - DOM-008-SK-010-A: Data freshness monitoring
      - DOM-008-SK-010-B: Data quality monitoring (completeness, accuracy, timeliness)
      - DOM-008-SK-010-C: Pipeline performance monitoring
      - DOM-008-SK-010-D: Cost monitoring and optimization

  - skill_id: DOM-008-SK-011
    name: Error Handling & Recovery in Pipelines
    domain: SD-008b
    description: Design fault-tolerant pipeline architectures; implement retry logic; design circuit breakers; implement dead letter queues; define recovery procedures.
    inputs:
      - Pipeline failure modes
      - Tolerance requirements
      - Recovery time objectives (RTO)
    outputs:
      - Fault tolerance patterns
      - Recovery procedures
      - Dead letter queue strategies
    complexity: High
    specializations:
      - DOM-008-SK-011-A: Retry strategies and exponential backoff
      - DOM-008-SK-011-B: Circuit breaker patterns
      - DOM-008-SK-011-C: Dead letter queue management
      - DOM-008-SK-011-D: Checkpoint and recovery mechanisms

  - skill_id: DOM-008-SK-012
    name: Data Lineage & Provenance Tracking
    domain: SD-008b
    description: Implement data lineage tracking; trace data origin to consumption; implement column-level lineage; support compliance and debugging.
    inputs:
      - Pipeline definitions
      - Transformation rules
      - Compliance requirements
    outputs:
      - Lineage graph specifications
      - Provenance metadata schemas
      - Lineage query interfaces
    complexity: Medium
    specializations:
      - DOM-008-SK-012-A: Table-level lineage tracking
      - DOM-008-SK-012-B: Column-level lineage tracking
      - DOM-008-SK-012-C: Process-level lineage (workflow dependencies)
      - DOM-008-SK-012-D: Compliance-driven audit trails

  # ============================================================================
  # SD-008c: Migration Strategies Skills
  # ============================================================================

  - skill_id: DOM-008-SK-013
    name: Zero-Downtime Migration Planning
    domain: SD-008c
    description: Plan schema migrations with zero or minimal downtime; design dual-write strategies; implement canary deployments; design rollback procedures.
    inputs:
      - Current schema version
      - Target schema version
      - Availability requirements
    outputs:
      - Migration step-by-step plan
      - Traffic routing strategy
      - Rollback procedures
    complexity: High
    specializations:
      - DOM-008-SK-013-A: Dual-write migration strategy
      - DOM-008-SK-013-B: Shadow reading strategies
      - DOM-008-SK-013-C: Canary deployment for data changes
      - DOM-008-SK-013-D: Feature flag-driven migrations

  - skill_id: DOM-008-SK-014
    name: Data Backfill & Reprocessing
    domain: SD-008c
    description: Design data backfill strategies for schema changes; implement batch reprocessing; handle partial backfill; validate backfill completeness.
    inputs:
      - Backfill data scope
      - Transformation logic
      - Validation requirements
    outputs:
      - Backfill procedures
      - Validation queries
      - Reprocessing schedules
    complexity: Medium
    specializations:
      - DOM-008-SK-014-A: Bulk backfill execution
      - DOM-008-SK-014-B: Incremental backfill strategies
      - DOM-008-SK-014-C: Validation and reconciliation

  - skill_id: DOM-008-SK-015
    name: Migration Rollback & Recovery
    domain: SD-008c
    description: Design rollback procedures for failed migrations; implement safe rollback automation; manage transaction rollback across distributed systems.
    inputs:
      - Migration failure state
      - Pre-migration state snapshots
      - Recovery time objectives
    outputs:
      - Rollback procedures
      - Automation scripts
      - State recovery strategies
    complexity: High
    specializations:
      - DOM-008-SK-015-A: Transactional rollback
      - DOM-008-SK-015-B: Distributed rollback coordination
      - DOM-008-SK-015-C: State reconciliation after rollback
      - DOM-008-SK-015-D: Automated rollback triggers

  - skill_id: DOM-008-SK-016
    name: Cross-Storage Migration
    domain: SD-008c
    description: Migrate data across different storage engines (relational→document, SQL→NoSQL, etc.); handle schema translation; implement consistency verification.
    inputs:
      - Source storage schema
      - Target storage schema
      - Data volume and constraints
    outputs:
      - Cross-storage migration procedures
      - Schema translation mappings
      - Validation strategies
    complexity: High
    specializations:
      - DOM-008-SK-016-A: Relational to document migration
      - DOM-008-SK-016-B: Document to graph migration
      - DOM-008-SK-016-C: Multi-storage consistency verification
      - DOM-008-SK-016-D: Incremental cross-storage sync

  - skill_id: DOM-008-SK-017
    name: Backup & Disaster Recovery Design
    domain: SD-008c
    description: Design backup strategies; define Recovery Time Objective (RTO) and Recovery Point Objective (RPO); implement restore procedures; test disaster recovery.
    inputs:
      - Data criticality levels
      - Regulatory requirements
      - Infrastructure constraints
    outputs:
      - Backup strategies