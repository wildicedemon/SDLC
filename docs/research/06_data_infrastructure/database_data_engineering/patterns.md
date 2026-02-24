# Database & Data Engineering - Patterns

This document catalogs identified patterns, anti-patterns, and use-cases for database and data engineering in autonomous AI coding systems.

---

## Identified Patterns

### Pattern 1: Declarative Schema as Code

**Name**: Declarative Schema as Code

**Description**: Define database schemas declaratively in version-controlled files (e.g., Prisma schema, Drizzle schema, Atlas HCL) rather than imperative migration scripts. The schema definition serves as the source of truth, and migrations are generated automatically.

**When to Use**:
- New projects with modern database tooling
- Teams using TypeScript/JavaScript ecosystems
- AI-assisted development where schema context is needed
- Projects requiring schema documentation as a byproduct

**Tradeoffs**:
- ✅ Single source of truth for schema
- ✅ Better AI comprehension (declarative intent is clearer)
- ✅ Auto-generated migrations reduce human error
- ✅ Schema documentation is always current
- ❌ Less control over migration implementation details
- ❌ May require escape hatches for complex migrations
- ❌ Tool-specific lock-in

**AI Coding Relevance**: Declarative schemas are significantly easier for AI agents to understand, modify, and generate. The intent is explicit rather than implicit in migration scripts.

---

### Pattern 2: Expand-Contract Migration

**Name**: Expand-Contract Migration

**Description**: Execute schema changes in phases: first expand (add new columns/tables without removing old), then migrate data and code, finally contract (remove old columns/tables). This enables zero-downtime deployments.

**When to Use**:
- Production systems requiring zero downtime
- Schema changes that affect active applications
- Microservices with independent deployment cycles
- High-availability requirements

**Tradeoffs**:
- ✅ Zero-downtime deployments
- ✅ Safe rollback at each phase
- ✅ Gradual migration of data
- ❌ Multiple deployments required
- ❌ Temporary data duplication
- ❌ Coordination between database and application changes

**AI Coding Relevance**: AI agents should be trained to generate expand-contract patterns by default for production migrations, understanding the safety benefits.

---

### Pattern 3: Schema Registry

**Name**: Schema Registry

**Description**: Maintain a centralized registry of schemas for all services, enabling schema discovery, compatibility checking, and evolution tracking across the organization.

**When to Use**:
- Microservices architectures
- Event-driven systems with Kafka/EventBridge
- Organizations with many teams and services
- API governance requirements

**Tradeoffs**:
- ✅ Cross-service schema visibility
- ✅ Breaking change detection
- ✅ Schema versioning and evolution tracking
- ❌ Infrastructure complexity
- ❌ Potential bottleneck
- ❌ Requires organizational buy-in

**AI Coding Relevance**: Schema registries provide context for AI agents working across services, enabling them to understand data contracts and dependencies.

---

### Pattern 4: Contract-First API Development

**Name**: Contract-First API Development

**Description**: Define API contracts (OpenAPI, AsyncAPI, GraphQL schema) before implementation. The contract drives code generation, documentation, and testing.

**When to Use**:
- API-first organizations
- Teams with frontend/backend separation
- Public APIs requiring stability
- AI-assisted development where context is critical

**Tradeoffs**:
- ✅ Clear contracts before implementation
- ✅ Enables parallel development
- ✅ Auto-generated documentation and clients
- ✅ Contract testing built-in
- ❌ Upfront design investment
- ❌ May constrain implementation flexibility
- ❌ Contract maintenance overhead

**AI Coding Relevance**: Contract-first development gives AI agents clear specifications to implement against, reducing ambiguity and improving correctness.

---

### Pattern 5: Test Data Builders

**Name**: Test Data Builders

**Description**: Use the Builder pattern to construct test data programmatically, providing fluent APIs for creating complex test entities with sensible defaults.

**When to Use**:
- Complex domain models
- Tests requiring varied data configurations
- Teams seeking readable test code
- AI-generated tests needing data construction

**Tradeoffs**:
- ✅ Readable test data construction
- ✅ Reusable across tests
- ✅ Encapsulates complexity
- ✅ Type-safe in typed languages
- ❌ Initial setup investment
- ❌ Maintenance as domain evolves
- ❌ May abstract away important details

**AI Coding Relevance**: Builders provide a clear API for AI agents to generate test data, with type safety and sensible defaults reducing errors.

---

### Pattern 6: Data Quality Gates

**Name**: Data Quality Gates

**Description**: Implement checkpoints in data pipelines that validate data quality before allowing data to proceed. Gates enforce schema compliance, data integrity, and business rules.

**When to Use**:
- Data pipelines with quality requirements
- ML training data pipelines
- ETL/ELT workflows
- Regulatory compliance requirements

**Tradeoffs**:
- ✅ Prevents bad data propagation
- ✅ Early detection of issues
- ✅ Documented quality expectations
- ❌ Pipeline complexity
- ❌ Potential bottlenecks
- ❌ False positives blocking valid data

**AI Coding Relevance**: Quality gates provide clear validation rules that AI agents can understand and generate tests for.

---

### Pattern 7: Synthetic Data Pipelines

**Name**: Synthetic Data Pipelines

**Description**: Automated pipelines that generate realistic synthetic data for development, testing, and ML training, maintaining statistical properties while protecting privacy.

**When to Use**:
- Environments requiring production-like data
- Privacy-sensitive domains (healthcare, finance)
- ML model training
- Load and performance testing

**Tradeoffs**:
- ✅ Privacy-preserving
- ✅ Unlimited data generation
- ✅ Reproducible test scenarios
- ❌ May not capture all edge cases
- ❌ Generation complexity
- ❌ Validation of synthetic data quality

**AI Coding Relevance**: Synthetic data pipelines can be orchestrated by AI agents to provision test environments on demand.

---

### Pattern 8: Database per Service

**Name**: Database per Service

**Description**: Each microservice owns its database, with no direct database sharing. Services communicate through well-defined APIs, ensuring loose coupling.

**When to Use**:
- Microservices architectures
- Domain-driven design contexts
- Teams requiring independent deployment
- Polyglot persistence needs

**Tradeoffs**:
- ✅ Service independence
- ✅ Technology flexibility
- ✅ Clear data ownership
- ❌ Data duplication
- ❌ Cross-service queries are complex
- ❌ Distributed transactions are difficult

**AI Coding Relevance**: Clear boundaries help AI agents understand data ownership and generate appropriate service-level code.

---

### Pattern 9: Event Sourcing for Audit

**Name**: Event Sourcing for Audit

**Description**: Store all changes as immutable events rather than just current state. Enables complete audit trails, time-travel queries, and event replay.

**When to Use**:
- Systems requiring complete audit history
- Financial and compliance systems
- Systems needing state reconstruction
- Debugging and analysis requirements

**Tradeoffs**:
- ✅ Complete audit trail
- ✅ Temporal queries
- ✅ Event replay for debugging
- ❌ Storage overhead
- ❌ Query complexity for current state
- ❌ Event schema evolution challenges

**AI Coding Relevance**: Event sourcing patterns provide clear context for AI agents about how data evolved, useful for debugging and analysis.

---

### Pattern 10: CQRS for Read/Write Separation

**Name**: CQRS for Read/Write Separation

**Description**: Separate command (write) and query (read) models, optimizing each independently. Often combined with event sourcing.

**When to Use**:
- Systems with different read/write patterns
- High-performance requirements
- Complex domain logic
- Scalability requirements

**Tradeoffs**:
- ✅ Optimized read and write paths
- ✅ Scalability
- ✅ Clear separation of concerns
- ❌ Increased complexity
- ❌ Eventual consistency
- ❌ More code to maintain

**AI Coding Relevance**: CQRS provides clear patterns for AI agents to follow when generating data access code.

---

## Identified Anti-Patterns

### Anti-Pattern 1: Shared Database

**Name**: Shared Database

**Description**: Multiple services or applications directly accessing the same database tables, creating tight coupling and coordination challenges.

**Failure Mode**:
- Schema changes break multiple services
- Unclear data ownership
- Performance issues from shared resource
- Difficult to evolve independently
- Testing contamination

**AI Coding Relevance**: AI agents may inadvertently create shared database patterns when generating code for multiple services, requiring explicit guidance to avoid.

---

### Anti-Pattern 2: Migration in Deployment

**Name**: Migration in Deployment

**Description**: Running database migrations as part of the application deployment process without separation, causing deployments to fail or block.

**Failure Mode**:
- Long migrations block deployments
- Failed migrations leave system in inconsistent state
- Rollback complexity
- Production incidents from schema changes
- Coordination failures in distributed systems

**AI Coding Relevance**: AI agents should be trained to separate migration execution from application deployment, understanding the operational risks.

---

### Anti-Pattern 3: God Table

**Name**: God Table

**Description**: A single table with many columns serving multiple purposes, often accumulating technical debt over time.

**Failure Mode**:
- Unclear column purposes
- Sparse data (many NULLs)
- Performance degradation
- Difficult to evolve schema
- Confusing for AI agents to understand

**AI Coding Relevance**: AI agents may generate or extend god tables when lacking domain context, perpetuating the anti-pattern.

---

### Anti-Pattern 4: Implicit Schema

**Name**: Implicit Schema

**Description**: Schema defined only in application code (ORM models, validation logic) without explicit database-level constraints.

**Failure Mode**:
- Data integrity violations
- Schema drift between code and database
- Difficult to understand schema without reading code
- No protection against direct database modifications
- AI agents lack schema context

**AI Coding Relevance**: AI agents need explicit schema definitions to generate correct code; implicit schemas create ambiguity.

---

### Anti-Pattern 5: Production Data in Development

**Name**: Production Data in Development

**Description**: Using production database copies in development environments without proper anonymization.

**Failure Mode**:
- Privacy and compliance violations
- Security risks from exposed data
- Developer access to sensitive information
- Potential for accidental data modification
- Legal liability

**AI Coding Relevance**: AI agents should never be trained on or given access to production data; synthetic data patterns are essential.

---

### Anti-Pattern 6: Unversioned Migrations

**Name**: Unversioned Migrations

**Description**: Running ad-hoc SQL scripts without version tracking, checksums, or rollback capabilities.

**Failure Mode**:
- Unknown database state
- Cannot reproduce environments
- No audit trail
- Failed migrations with no recovery
- Team coordination failures

**AI Coding Relevance**: AI-generated migrations must be version-controlled and trackable; unversioned migrations create chaos.

---

### Anti-Pattern 7: Over-Indexing

**Name**: Over-Indexing

**Description**: Creating indexes for every query pattern without considering write performance, storage, and maintenance overhead.

**Failure Mode**:
- Slow write performance
- Excessive storage consumption
- Index maintenance overhead
- Query optimizer confusion
- Migration slowdown

**AI Coding Relevance**: AI agents may suggest indexes for every query without understanding the tradeoffs; requires explicit guidance.

---

### Anti-Pattern 8: Missing Rollback

**Name**: Missing Rollback

**Description**: Migrations without corresponding rollback scripts, making it impossible to safely revert schema changes.

**Failure Mode**:
- Cannot recover from failed deployments
- Production incidents with no recovery path
- Risk-averse change management
- Accumulated technical debt

**AI Coding Relevance**: AI agents should always generate rollback scripts alongside migrations; missing rollbacks are a critical oversight.

---

## Use-Cases Grounded in Research

### Use-Case 1: AI-Assisted Schema Migration

**Scenario**: An autonomous coding agent needs to add a new column to a critical production table.

**Pattern Application**:
1. Agent analyzes existing schema using Schema Registry pattern
2. Generates Expand-Contract migration pattern
3. Creates Declarative Schema update
4. Produces rollback script
5. Suggests test data updates using Test Data Builders

**Research Basis**: Microsoft Research (2024) found AI-generated migrations achieve 73% correctness on first attempt with proper patterns [9].

---

### Use-Case 2: Cross-Service Data Contract Enforcement

**Scenario**: Multiple microservices need to share data through events while maintaining compatibility.

**Pattern Application**:
1. Define event schemas in Schema Registry
2. Use Contract-First API Development for event contracts
3. Implement Data Quality Gates for event validation
4. Generate synthetic events for testing

**Research Basis**: Confluent Schema Registry documentation demonstrates 99.9% compatibility when using schema evolution rules [12].

---

### Use-Case 3: Test Environment Provisioning

**Scenario**: Development team needs realistic test data for a new feature.

**Pattern Application**:
1. Synthetic Data Pipelines generate privacy-safe data
2. Test Data Builders create domain-specific test entities
3. Database per Service ensures isolation
4. Data Quality Gates validate generated data

**Research Basis**: Google DeepMind (2024) found LLM-generated test data achieved 82% edge case coverage [14].

---

### Use-Case 4: Data Drift Detection and Response

**Scenario**: Production data quality degrades, affecting downstream systems.

**Pattern Application**:
1. Data Quality Gates detect drift
2. Event Sourcing provides audit trail
3. Schema Registry tracks schema changes
4. Automated alerts trigger investigation

**Research Basis**: Chen et al. (2025) demonstrated 67% reduction in data incidents with combined drift detection [13].

---

### Use-Case 5: API Evolution Without Breaking Changes

**Scenario**: API needs to evolve while maintaining backward compatibility.

**Pattern Application**:
1. Contract-First API Development defines changes
2. Schema Registry checks compatibility
3. Expand-Contract pattern for schema changes
4. Feature Flags control rollout

**Research Basis**: Salesforce (2024) found automated API linting reduces breaking changes by 78% [16].

---

### Use-Case 6: Multi-Team Schema Coordination

**Scenario**: Multiple teams need to coordinate schema changes across services.

**Pattern Application**:
1. Schema Registry provides visibility
2. Contract-First development ensures coordination
3. Database per Service maintains independence
4. Data Quality Gates prevent cross-service issues

**Research Basis**: Uber Engineering (2024) describes schema registry approach for cross-service dependency tracking [5].

---

## Pattern Selection Guide

| Scenario | Recommended Patterns | Avoid Anti-Patterns |
|----------|---------------------|---------------------|
| New microservice | Database per Service, Contract-First, Declarative Schema | Shared Database, Implicit Schema |
| Production migration | Expand-Contract, Schema Registry, Missing Rollback | Migration in Deployment |
| Test data setup | Test Data Builders, Synthetic Data Pipelines | Production Data in Development |
| API development | Contract-First, Schema Registry | Implicit Schema |
| Data pipeline | Data Quality Gates, Event Sourcing | Unversioned Migrations |
| Performance optimization | CQRS, Database per Service | Over-Indexing, God Table |
| Audit requirements | Event Sourcing, Schema Registry | Unversioned Migrations |
