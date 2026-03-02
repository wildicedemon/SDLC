> code · sonar-reasoning-pro
<think>
The user is asking me to "execute the code agent prompt from the attached file." They've provided a file path and content that is NOT code - it's a detailed prompt/specification document for an agent called "Data Engineering Agent (AGT-008)".

Looking at this document, it's a comprehensive system directive that defines:
1. A Data Engineering Agent that should decompose the Data Engineering & Storage domain
2. 16 different categories that need to be fully populated (Skills, Workflows, Task Templates, Rules & Constraints, Interfaces, Dependencies, State Models, Data Models, Control Flows, Failure Modes & Recovery, Optimization Strategies, Coordination Mechanisms, Context Requirements, Memory Structures, Monitoring Requirements, Evolution Mechanisms)
3. Requirements for recursive expansion of subdomains

The user wants me to "execute" this prompt and output the results to `output/core_infrastructure/AGT-008`.

However, I need to be clear about what "executing" this means. The file itself is a directive/specification for what an AI agent should do. The user seems to be asking me to:
1. Follow the directive in the document
2. Perform the decomposition of the Data Engineering & Storage domain
3. Output the results

This is essentially asking me to act as the Data Engineering Agent (AGT-008) and perform the complete domain decomposition as specified in the document.

The task is to:
1. Decompose the Data Engineering & Storage domain into all 16 categories
2. Provide full details for each
3. Perform recursive expansion to 3 levels
4. Detect and resolve gaps
5. Output to `output/core_infrastructure/AGT-008`

This is a very large and complex task. I should start by creating the output directory and then systematically work through all 16 categories. Given the scope and the constraint that I should be concise and direct, I should use tools to create the necessary output file structure.

Let me start by creating the output directory and beginning the decomposition work.
</think>

I'll execute the Data Engineering Agent (AGT-008) prompt by decomposing the Data Engineering & Storage domain into all 16 required categories and creating the output artifacts.

<function_calls>
<tool_name>bash</tool_name>
<parameter name="command">mkdir -p "C:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\core_infrastructure\AGT-008"</parameter>
</invoke>
</function_calls>
<function_calls>
<tool_name>writeFile</parameter>
<parameter name="filePath">C:\Users\Ice\Desktop\Dev\SDLC\SDLC\output\core_infrastructure\AGT-008\domain_decomposition.md</parameter>
<parameter name="content"># AGT-008: Data Engineering & Storage Domain Decomposition

**Agent:** Data Engineering Agent (AGT-008)  
**Domain:** DOM-008 Data Engineering & Storage  
**Execution Date:** 2026-03-01  
**Recursion Depth:** 3 levels  
**Status:** Complete

---

## 1. SKILLS (DOM-008-SK-[NNN])

### DOM-008-SK-001: Schema Design & Normalization
- **Description:** Design normalized database schemas across relational, document, and graph storage engines using entity-relationship modeling and normalization theory (1NF-3NF+BCNF).
- **Inputs:** Business requirements, entity definitions, relationship specifications, cardinality constraints
- **Outputs:** Normalized schema DDL, ER diagrams, normalization documentation, denormalization justification
- **Complexity:** High

### DOM-008-SK-002: Data Pipeline Construction
- **Description:** Build end-to-end ETL/ELT pipelines including data ingestion, transformation, validation, and loading with monitoring and error handling.
- **Inputs:** Data source specifications, transformation requirements, target schema, SLAs
- **Outputs:** Pipeline DAG definitions, transformation logic, data lineage documentation
- **Complexity:** High

### DOM-008-SK-003: Migration Script Generation
- **Description:** Generate database migration scripts with rollback capabilities, supporting zero-downtime deployment and data backfill.
- **Inputs:** Schema version diff, current schema state, target schema state, data migration rules
- **Outputs:** Forward migration scripts, rollback scripts, validation checksums
- **Complexity:** High

### DOM-008-SK-004: Storage Engine Selection
- **Description:** Evaluate and select appropriate storage engines (relational, document, graph, vector, time-series) based on access patterns, consistency requirements, and scalability needs.
- **Inputs:** Data model characteristics, query patterns, consistency requirements, scale projections, cost constraints
- **Outputs:** Engine selection justification, trade-off analysis, capacity planning estimates
- **Complexity:** Medium

### DOM-008-SK-005: Data Integrity Validation
- **Description:** Design and implement validation rules to ensure data quality, consistency, referential integrity, and business rule compliance.
- **Inputs:** Schema definition, business rules, data quality requirements
- **Outputs:** Validation rule sets, anomaly detection patterns, data quality metrics
- **Complexity:** Medium

### DOM-008-SK-006: Index Optimization
- **Description:** Design, create, and optimize database indexes to accelerate query performance while minimizing storage overhead and write latency.
- **Inputs:** Query patterns, cardinality statistics, performance baselines, workload profiles
- **Outputs:** Index definitions, execution plans, performance improvement metrics
- **Complexity:** Medium

### DOM-008-SK-007: Backup & Restore Operations
- **Description:** Design and execute backup strategies including point-in-time recovery, incremental backups, and disaster recovery procedures.
- **Inputs:** RTO/RPO requirements, retention policies, storage constraints
- **Outputs:** Backup procedures, restore runbooks, disaster recovery plans
- **Complexity:** Medium

### DOM-008-SK-008: Multi-Store Query Federation
- **Description:** Design query federation patterns to seamlessly query across heterogeneous storage engines while maintaining consistency and optimizing performance.
- **Inputs:** Multi-engine schema mappings, query requirements, consistency constraints
- **Outputs:** Federation layer specifications, cross-store join strategies, query optimization rules
- **Complexity:** High

### DOM-008-SK-009: Schema Versioning & Compatibility
- **Description:** Manage schema evolution while maintaining backward/forward compatibility, supporting multiple schema versions simultaneously.
- **Inputs:** Schema change requirements, compatibility constraints, deprecation timelines
- **Outputs:** Versioning strategy, compatibility matrices, migration pathways
- **Complexity:** Medium

### DOM-008-SK-010: Data Pipeline Monitoring & Observability
- **Description:** Implement comprehensive monitoring for data pipelines including latency tracking, data quality metrics, failure detection, and alerting.
- **Inputs:** Pipeline definitions, SLA requirements, alerting thresholds
- **Outputs:** Monitoring specifications, alert rules, dashboards, remediation runbooks
- **Complexity:** Medium

### DOM-008-SK-011: Stream vs. Batch Processing Selection
- **Description:** Evaluate and recommend optimal processing paradigm (streaming, batch, or hybrid) based on latency, throughput, and consistency requirements.
- **Inputs:** Data freshness requirements, volume projections, consistency needs, cost constraints
- **Outputs:** Processing paradigm recommendation, architecture rationale, proof-of-concept results
- **Complexity:** Medium

### DOM-008-SK-012: Data Lineage & Provenance Tracking
- **Description:** Implement end-to-end data lineage tracking showing data flow from source to consumption, enabling impact analysis and compliance auditing.
- **Inputs:** Pipeline definitions, schema mappings, transformation logic
- **Outputs:** Lineage graph, lineage query interfaces, impact analysis tools
- **Complexity:** Medium

---

## 2. WORKFLOWS (DOM-008-WF-[NNN])

### DOM-008-WF-001: Schema Creation & Validation Workflow
- **Trigger:** Architecture contract received from AGT-002 specifying new data persistence requirements
- **Steps:**
  1. Parse entity definitions and relationship specifications from architecture contract
  2. Design normalized schema across selected storage engines (DOM-008-SK-001)
  3. Generate DDL statements and migration scripts (DOM-008-SK-003)
  4. Validate schema against cardinality constraints and referential integrity rules (DOM-008-SK-005)
  5. Perform peer review of schema design
  6. Execute schema validation workflow (DOM-008-WF-002)
  7. Generate schema documentation and ER diagrams
  8. Update schema registry with versioned schema definition (v1.0)
- **Entry Criteria:** Architecture contract has clear data persistence requirements; all referenced entities defined
- **Exit Criteria:** Schema validated, documented, versioned, and ready for deployment; all constraints satisfied
- **Completion Criteria:** Schema passes all validation tests; peer review approved; documentation complete
- **Rollback Plan:** Revert to previous schema version; notify dependent agents; document change failure

### DOM-008-WF-002: Data Migration Execution Workflow
- **Trigger:** Schema migration required (version upgrade, data backfill, index optimization)
- **Steps:**
  1. Analyze current schema state and target schema state (DOM-008-SK-003)
  2. Generate forward and rollback migration scripts
  3. Validate migration scripts in staging environment (DOM-008-SK-005)
  4. Execute data backup and create restore point (DOM-008-SK-007)
  5. Execute forward migration in transactional context
  6. Validate data integrity post-migration (DOM-008-SK-005)
  7. Monitor post-migration performance and anomalies
  8. Mark old schema version as deprecated; activate new version
  9. Archive rollback scripts and migration metadata
- **Entry Criteria:** Migration scripts generated and tested; backup completed; maintenance window scheduled; stakeholders notified
- **Exit Criteria:** New schema active; data integrity verified; performance acceptable; rollback scripts archived
- **Completion Criteria:** Zero data loss; all validation checks pass; performance SLAs met; migration time within budget
- **Rollback Plan:** Execute rollback scripts in reverse; verify data restoration; reactivate previous schema version

### DOM-008-WF-003: Pipeline Deployment Workflow
- **Trigger:** New or modified data pipeline approved by AGT-002; pipeline definition updated in registry
- **Steps:**
  1. Validate pipeline definition (source, transformations, sink, schedule)
  2. Test data lineage and transformation logic in sandbox (DOM-008-SK-012)
  3. Validate data quality rules and output schema (DOM-008-SK-005)
  4. Deploy pipeline code to execution environment
  5. Execute test run with sample data
  6. Validate output data quality and schema compliance
  7. Enable monitoring and alerting (DOM-008-SK-010)
  8. Schedule pipeline execution; activate in production
  9. Monitor initial executions for failures or data quality issues
- **Entry Criteria:** Pipeline definition approved; all dependencies resolved; execution environment ready; sample data available
- **Exit Criteria:** Pipeline deployed; test execution passed; monitoring active; ready for production scheduling
- **Completion Criteria:** Pipeline running on schedule; data quality metrics within thresholds; zero data loss observed
- **Rollback Plan:** Rollback pipeline code to previous version; reprocess affected time windows; notify data consumers

### DOM-008-WF-004: Backup & Disaster Recovery Workflow
- **Trigger:** Scheduled backup window (daily/weekly/monthly); disaster recovery drill initiated; data loss incident detected
- **Steps:**
  1. Execute full or incremental backup based on schedule
  2. Validate backup integrity and completeness (checksum verification)
  3. Test restore capability in isolated environment
  4. Archive backup metadata and retention schedule
  5. Monitor backup storage capacity and retention policies
  6. Generate backup completion report and retention timeline
  7. For disaster recovery: Execute restore procedure to RTO target
  8. Validate restored data integrity and consistency
  9. Notify stakeholders of recovery completion
- **Entry Criteria:** Backup configuration defined; RTO/RPO requirements established; storage available; restore procedure tested
- **Exit Criteria:** Backup completed with validation passed; restore capability verified; backup archived with metadata
- **Completion Criteria:** Backup retention policy met; recovery time within RTO; data integrity verified
- **Rollback Plan:** Retain multiple backup copies; execute alternative restore from previous backup; escalate to incident management

### DOM-008-WF-005: Data Integrity Audit Workflow
- **Trigger:** Scheduled audit window; data quality anomaly detected; post-migration verification
- **Steps:**
  1. Define audit scope (tables, columns, date ranges)
  2. Execute data validation rules (DOM-008-SK-005)
  3. Check referential integrity constraints
  4. Validate business rule compliance
  5. Detect anomalies and outliers using statistical methods
  6. Generate data quality report with findings
  7. For detected issues: Execute remediation steps (data correction, cascade updates)
  8. Re-validate after remediation
  9. Archive audit trail with findings and remediations
- **Entry Criteria:** Audit rules defined; baseline quality metrics established; validation scope clear
- **Exit Criteria:** Audit completed; all critical issues resolved; quality report generated
- **Completion Criteria:** Data quality metrics meet SLAs; all anomalies documented or resolved
- **Rollback Plan:** For corrections, retain previous values; execute rollback if data correction fails validation

### DOM-008-WF-006: Index Optimization Workflow
- **Trigger:** Query performance degradation detected; new workload pattern identified; periodic optimization cycle
- **Steps:**
  1. Analyze query patterns and execution plans (DOM-008-SK-006)
  2. Identify missing, unused, or inefficient indexes
  3. Generate index creation/modification scripts
  4. Estimate impact on read/write performance and storage
  5. Test index changes in staging with production workload
  6. Execute index changes during low-traffic window
  7. Monitor query performance post-optimization
  8. Archive old indexes for 30-day retention before deletion
  9. Update index registry and documentation
- **Entry Criteria:** Query performance baseline established; bottleneck analysis completed; staging environment available
- **Exit Criteria:** New indexes deployed; performance improvements measured and documented
- **Completion Criteria:** Query latency improved by target percentage; write performance impact within acceptable range
- **Rollback Plan:** Restore archived indexes; revert index definitions; monitor for performance regression

### DOM-008-WF-007: Schema Version Lifecycle Workflow
- **Trigger:** Schema version reaches end-of-life; new major version released; deprecation period expires
- **Steps:**
  1. Define version lifecycle: Designed → Validated → Deploying → Active → Migrating → Deprecated → Archived
  2. Transition schema through states with timestamp and reason documentation
  3. Track dependent consumers of each schema version
  4. Plan migration timeline for deprecated versions
  5. Execute forced migrations for remaining consumers
  6. Archive deprecated schemas with metadata
  7. Update schema registry to reflect version status
  8. Notify all consumers of version status changes
- **Entry Criteria:** Schema version management policy defined; version transition criteria clear
- **Exit Criteria:** Version transitions tracked; consumers migrated; schema archived with metadata
- **Completion Criteria:** All consumers migrated; deprecated version archived; no active dependencies remain
- **Rollback Plan:** Reactivate previous version if critical issue discovered; update consumer dependencies

---

## 3. TASK TEMPLATES (DOM-008-TT-[NNN])

### DOM-008-TT-001: Schema Design Task Template
```
{
  "id": "TT-001",
  "type": "schema_design",
  "inputs": {
    "requirements": "entity_definitions, relationship_specs, cardinality_constraints",
    "storage_engines": "selected_engines_list",
    "constraints": "consistency_requirements, scale_projections"
  },
  "process": [
    "normalize_schema(requirements)",
    "design_er_model(entity_definitions)",
    "map_to_storage_engines(storage_engines)",
    "validate_constraints()"
  ],
  "outputs": {
    "schema_ddl": "DDL_statements",
    "er_diagram": "visual_representation",
    "documentation": "design_rationale_and_decisions"
  },
  "validation": ["cardinality_check", "referential_integrity", "constraint_validation"],
  "owner": "AGT-008"
}
```

### DOM-008-TT-002: Pipeline Transformation Task Template
```
{
  "id": "TT-002",
  "type": "pipeline_transformation",
  "inputs": {
    "source_schema": "source_table_definitions",
    "target_schema": "target_table_definitions",
    "rules": "transformation_rules_and_logic",
    "data_sample": "sample_data_for_testing"
  },
  "process": [
    "parse_transformation_rules(rules)",
    "generate_sql_or_code()",
    "test_with_sample_data(data_sample)",
    "validate_output