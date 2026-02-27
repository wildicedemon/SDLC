# Distributed Orchestration Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in distributed orchestration for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Cluster Architecture Patterns

### Federated Cluster Architecture

**Name**: Regional Coordinator Federation

**Description**: Organize agent clusters into regional federations, each with local coordinators that communicate for cross-region tasks. Local tasks stay within region; cross-region tasks coordinate through federation protocol.

**When to Use**:
- Geographically distributed teams
- Systems requiring low-latency local access
- Organizations with regional autonomy requirements

**Tradeoffs**:
- ✅ 3x throughput improvement over single coordinator
- ✅ Low latency for local operations
- ✅ Regional fault isolation
- ❌ Cross-region coordination complexity
- ❌ Consistency challenges between regions
- ❌ Requires federation protocol implementation

**Confidence: HIGH** - Validated in distributed systems research [paper:2].

---

### Service Mesh Coordination

**Name**: Sidecar-Based Agent Coordination

**Description**: Deploy coordination logic as sidecar proxies alongside agent processes. Service mesh handles service discovery, load balancing, and secure communication.

**When to Use**:
- Containerized agent deployments
- Systems requiring secure inter-agent communication
- Environments with dynamic agent scaling

**Tradeoffs**:
- ✅ Transparent coordination logic
- ✅ Built-in observability
- ✅ Secure communication (mTLS)
- ❌ Sidecar resource overhead
- ❌ Complexity in debugging
- ❌ Requires container orchestration

**Confidence: HIGH** - Established pattern with Istio, Linkerd.

---

### Worker Pool Pattern

**Name**: Pre-Warmed Agent Workers

**Description**: Maintain a pool of pre-initialized agent workers ready for task assignment. Workers are created ahead of demand and reused across tasks.

**When to Use**:
- Systems with variable but predictable load
- Tasks requiring fast startup
- Environments where agent initialization is expensive

**Tradeoffs**:
- ✅ Low task assignment latency
- ✅ Efficient resource utilization
- ✅ Predictable performance
- ❌ Resource overhead for idle workers
- ❌ Requires capacity planning
- ❌ Worker state management

**Confidence: HIGH** - Standard pattern from serverless and worker systems.

---

## Task Distribution Patterns

### Priority Queue with Fair Share

**Name**: Weighted Fair Queue Scheduling

**Description**: Combine priority queues with fair-share scheduling. High-priority tasks are processed first, but fair-share ensures lower-priority tasks eventually receive resources.

**When to Use**:
- Systems with mixed task criticality
- Multi-tenant environments
- Scenarios requiring both urgency and fairness

**Tradeoffs**:
- ✅ 89% reduction in task starvation
- ✅ Balances urgency with fairness
- ✅ Prevents priority inversion
- ❌ More complex scheduling logic
- ❌ Requires fair-share configuration
- ❌ May delay high-priority under load

**Confidence: HIGH** - Validated in scheduling research [paper:3].

---

### Work Stealing

**Name**: Dynamic Load Balancing

**Description**: Idle workers can steal tasks from busy workers' queues. Enables dynamic load balancing without central coordination.

**When to Use**:
- Variable task durations
- Systems with uneven load distribution
- Environments requiring automatic load balancing

**Tradeoffs**:
- ✅ Automatic load balancing
- ✅ No central scheduler bottleneck
- ✅ Adapts to variable task durations
- ❌ Coordination overhead for stealing
- ❌ May cause task reordering
- ❌ Complex to implement correctly

**Confidence: HIGH** - Established pattern from parallel computing.

---

### Sharded Task Queue

**Name**: Partition-Based Distribution

**Description**: Partition task queue by key (e.g., repository, project, user). Each partition has dedicated workers, ensuring ordering within partition.

**When to Use**:
- Tasks requiring ordering guarantees
- Systems with natural partition keys
- Scenarios benefiting from locality

**Tradeoffs**:
- ✅ Ordering guarantees within partition
- ✅ Reduced lock contention
- ✅ Natural locality for related tasks
- ❌ Uneven partition sizes
- ❌ Requires partition key selection
- ❌ Rebalancing complexity

**Confidence: MEDIUM** - Established pattern, agent-specific considerations.

---

## Concurrency Control Patterns

### Lease-Based Distributed Lock

**Name**: Time-Bounded Lock with Auto-Expire

**Description**: Acquire locks with time-based leases that automatically expire. Prevents deadlock from crashed agents holding locks indefinitely.

**When to Use**:
- All distributed locking scenarios
- Systems with potential for agent crashes
- Environments requiring fault tolerance

**Tradeoffs**:
- ✅ Automatic deadlock prevention
- ✅ Handles agent crashes gracefully
- ✅ Clear lock semantics
- ❌ Lease duration tuning required
- ❌ May expire during long operations
- ❌ Requires clock synchronization

**Confidence: HIGH** - Standard distributed systems pattern.

---

### Fencing Token Pattern

**Name**: Monotonic Token for Stale Lock Detection

**Description**: Include monotonically increasing token with lock acquisition. Operations check token to reject requests from stale lock holders.

**When to Use**:
- Systems with potential network partitions
- Scenarios requiring strict ordering
- Environments with delayed messages

**Tradeoffs**:
- ✅ Prevents stale lock holder interference
- ✅ Handles network delays
- ✅ Clear ordering semantics
- ❌ Requires token storage and checking
- ❌ Additional coordination overhead
- ❌ Not all systems support tokens

**Confidence: HIGH** - Established pattern from distributed databases.

---

### Optimistic Concurrency with Retry

**Name**: Version-Based Conflict Detection

**Description**: Proceed without locks, detect conflicts through version checking, retry on conflict. Suitable for low-contention scenarios.

**When to Use**:
- Low-contention resources
- Read-heavy workloads
- Systems preferring throughput over consistency

**Tradeoffs**:
- ✅ No lock overhead
- ✅ High throughput under low contention
- ✅ No deadlock risk
- ❌ Retry overhead under contention
- ❌ May starve under high contention
- ❌ Requires version tracking

**Confidence: HIGH** - Standard database concurrency pattern.

---

## Backpressure Patterns

### Adaptive Throttling

**Name**: Feedback-Based Rate Control

**Description**: Dynamically adjust request rate based on system metrics (latency, queue depth, error rate). Maintains stable performance under varying load.

**When to Use**:
- Systems with variable load
- Environments requiring latency guarantees
- Scenarios with unpredictable demand

**Tradeoffs**:
- ✅ Maintains 2x latency under 5x load
- ✅ Automatic adaptation
- ✅ Prevents cascade failures
- ❌ Requires metric collection
- ❌ Tuning of control parameters
- ❌ May over-throttle during spikes

**Confidence: HIGH** - Validated in reactive systems research [paper:4].

---

### Circuit Breaker

**Name**: Fail-Fast Under Load

**Description**: Monitor failure rate and open circuit when threshold exceeded. Fast-fail requests instead of waiting for timeouts.

**When to Use**:
- Systems with external dependencies
- Environments requiring fast failure
- Scenarios with potential cascade failures

**Tradeoffs**:
- ✅ Fast failure under problems
- ✅ Prevents cascade failures
- ✅ Allows recovery time
- ❌ May reject valid requests
- ❌ Requires threshold tuning
- ❌ Complex state management

**Confidence: HIGH** - Standard resilience pattern.

---

### Queue with Bounded Size

**Name**: Fixed-Capacity Request Buffer

**Description**: Maintain bounded queue for incoming requests. Reject requests when queue full, providing backpressure signal.

**When to Use**:
- Systems with bursty traffic
- Environments requiring memory bounds
- Scenarios with acceptable rejection

**Tradeoffs**:
- ✅ Memory bounded
- ✅ Clear backpressure signal
- ✅ Simple implementation
- ❌ Rejects valid requests when full
- ❌ Requires capacity planning
- ❌ May cause client failures

**Confidence: HIGH** - Standard queue pattern.

---

## Coordination Patterns

### MCP Protocol Integration

**Name**: Model Context Protocol for Tool Sharing

**Description**: Use MCP for standardized tool and context sharing between agents. Enables interoperability across different agent implementations.

**When to Use**:
- Multi-vendor agent environments
- Systems requiring tool portability
- Scenarios with evolving tool ecosystem

**Tradeoffs**:
- ✅ Standardized interfaces
- ✅ Tool portability
- ✅ Growing ecosystem
- ❌ Protocol overhead
- ❌ Requires MCP compliance
- ❌ Limited to protocol capabilities

**Confidence: MEDIUM** - Emerging standard [seed:Augment-MCP].

---

### Blackboard Pattern

**Name**: Shared State Space Coordination

**Description**: Agents communicate through shared blackboard (state space). Agents read from and write to blackboard without direct communication.

**When to Use**:
- Systems with many agents
- Scenarios requiring loose coupling
- Environments with complex coordination

**Tradeoffs**:
- ✅ Loose coupling between agents
- ✅ Scales to many agents
- ✅ Flexible coordination
- ❌ Blackboard contention
- ❌ State consistency challenges
- ❌ Debugging complexity

**Confidence: MEDIUM** - Established AI pattern, limited agent-specific validation.

---

### Contract Net Protocol

**Name**: Task Bidding and Assignment

**Description**: Tasks are announced to agents, who bid based on capability and availability. Best bid wins the task.

**When to Use**:
- Heterogeneous agent capabilities
- Dynamic task requirements
- Systems with variable agent availability

**Tradeoffs**:
- ✅ Dynamic capability matching
- ✅ Handles agent availability
- ✅ Decentralized assignment
- ❌ Bidding overhead
- ❌ May not find optimal assignment
- ❌ Requires bid evaluation

**Confidence: MEDIUM** - Established multi-agent pattern.

---

## Multi-Repo Patterns

### Event-Driven Cross-Repo Coordination

**Name**: Repository Event Propagation

**Description**: Changes in one repository emit events that trigger agents in other repositories. Enables loosely coupled cross-repo coordination.

**When to Use**:
- Microservice architectures
- Systems with repository boundaries
- Scenarios requiring eventual consistency

**Tradeoffs**:
- ✅ Loose coupling between repos
- ✅ Scalable to many repos
- ✅ Eventual consistency
- ❌ Event ordering challenges
- ❌ Debugging across repos
- ❌ Requires event infrastructure

**Confidence: MEDIUM** - Established event-driven pattern.

---

### Federated Context Management

**Name**: Per-Repo Context with Cross-Links

**Description**: Maintain separate context for each repository with links to related contexts. Agents load relevant contexts on demand.

**When to Use**:
- Large multi-repo systems
- Scenarios with context window limits
- Environments with clear repo boundaries

**Tradeoffs**:
- ✅ Respects context limits
- ✅ Clear repo boundaries
- ✅ On-demand loading
- ❌ Cross-repo context switching
- ❌ Link maintenance overhead
- ❌ May miss cross-repo dependencies

**Confidence: MEDIUM** - Emerging pattern for large codebases.

---

## Resilience Patterns

### Byzantine Fault Tolerance

**Name**: Consensus Despite Malicious Agents

**Description**: Use BFT consensus protocols to tolerate Byzantine (arbitrary/malicious) failures. Requires 3f+1 nodes to tolerate f failures.

**When to Use**:
- Security-critical systems
- Environments with potential compromise
- Scenarios requiring guaranteed correctness

**Tradeoffs**:
- ✅ Tolerates malicious behavior
- ✅ Guaranteed correctness
- ✅ No trusted coordinator needed
- ❌ High overhead (3f+1 nodes)
- ❌ Complex implementation
- ❌ Latency impact

**Confidence: MEDIUM** - Established theory, limited production use [paper:6].

---

### Consensus-Based Critical Changes

**Name**: Multi-Agent Agreement for Sensitive Operations

**Description**: Require multiple agents to agree on critical changes before execution. Prevents single compromised agent from causing harm.

**When to Use**:
- Critical code modifications
- Security-sensitive operations
- Production deployments

**Tradeoffs**:
- ✅ Prevents single point of compromise
- ✅ Increased confidence in changes
- ✅ Audit trail from consensus
- ❌ Increased latency
- ❌ Requires multiple agents
- ❌ May block on disagreement

**Confidence: MEDIUM** - Security best practice, implementation complexity.

---

## Anti-Patterns

### Single Coordinator Bottleneck

**Name**: Central Orchestrator SPOF

**Description**: All coordination flows through single coordinator, creating bottleneck and single point of failure.

**Failure Mode**:
- Scalability limited by coordinator capacity
- Coordinator failure halts entire system
- Latency increases with cluster size

**Remediation**: Use distributed coordination (Raft) or federated architecture.

**Confidence: HIGH** - Well-understood distributed systems anti-pattern.

---

### Unbounded Queues

**Name**: Infinite Buffer Anti-Pattern

**Description**: Using unbounded queues that grow without limit under load, leading to memory exhaustion and unpredictable latency.

**Failure Mode**:
- Memory exhaustion
- Unbounded latency growth
- System instability under load

**Remediation**: Use bounded queues with backpressure.

**Confidence: HIGH** - Standard systems anti-pattern.

---

### Lock Without Timeout

**Name**: Indefinite Lock Hold

**Description**: Acquiring locks without timeout or lease, leading to deadlock when agents crash while holding locks.

**Failure Mode**:
- Deadlock from crashed agents
- System hang waiting for locks
- Manual intervention required

**Remediation**: Always use lease-based locks with reasonable timeouts.

**Confidence: HIGH** - Standard distributed systems anti-pattern.

---

### Ignoring Network Partitions

**Name**: Assume Reliable Network

**Description**: Designing system as if network is always available, failing to handle partition scenarios.

**Failure Mode**:
- Split-brain behavior
- Data inconsistency
- System unavailability

**Remediation**: Design for partition tolerance (CAP theorem awareness).

**Confidence: HIGH** - Well-understood distributed systems anti-pattern.

---

### Synchronous Cross-Service Calls

**Name**: Blocking Remote Dependencies

**Description**: Making synchronous calls to remote services without timeout or fallback, creating cascading failures.

**Failure Mode**:
- Cascading failures
- Thread pool exhaustion
- System-wide outage

**Remediation**: Use async patterns, circuit breakers, timeouts.

**Confidence: HIGH** - Standard microservices anti-pattern.

---

### No Backpressure Propagation

**Name**: Silent Overload

**Description**: Accepting requests without propagating backpressure to callers, leading to overload and failure.

**Failure Mode**:
- System overload
- Degraded performance
- Silent failures

**Remediation**: Implement backpressure signals and propagation.

**Confidence: HIGH** - Standard reactive systems anti-pattern.

---

## Use-Case Patterns

### Enterprise Multi-Team Orchestration

**Pattern**: Federated Clusters with Priority Queues

**Description**: Deploy regional clusters for each team with local autonomy. Cross-team tasks use federation protocol. Priority queues ensure critical tasks processed first.

**Implementation Notes**:
- Use federated cluster architecture
- Implement priority queue with fair share
- Use MCP for cross-team tool sharing
- Deploy circuit breakers for external calls

**Confidence: HIGH** - Enterprise deployment pattern.

---

### CI/CD Pipeline Integration

**Pattern**: Worker Pool with Sharded Queues

**Description**: Pre-warmed worker pool for CI/CD tasks. Shard queues by repository for ordering guarantees. Use adaptive throttling for load management.

**Implementation Notes**:
- Use worker pool pattern for fast startup
- Shard by repository for ordering
- Implement adaptive throttling
- Use lease-based locks for shared resources

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Cross-Repository Refactoring

**Pattern**: Event-Driven with Federated Context

**Description**: Emit events for cross-repo changes. Agents load federated contexts for affected repos. Use consensus for critical changes.

**Implementation Notes**:
- Use event-driven coordination
- Implement federated context management
- Require consensus for critical changes
- Use optimistic concurrency for speed

**Confidence: MEDIUM** - Complex scenario, emerging patterns.

---

## Summary

The patterns identified reveal key principles:

1. **Federation over centralization** - Regional coordinators scale better
2. **Lease-based locks essential** - Prevent deadlock from crashes
3. **Backpressure prevents cascade failures** - Adaptive throttling most effective
4. **MCP emerging as standard** - Protocol-based interoperability
5. **Consensus for critical operations** - Multi-agent agreement for security
6. **Bounded resources everywhere** - Queues, locks, and contexts need limits

**Confidence levels vary by pattern maturity** - Core distributed patterns (locks, queues, backpressure) HIGH confidence; agent-specific protocols (MCP, A2A) MEDIUM confidence; emerging patterns (federated context) MEDIUM to LOW.

# Distributed Orchestration Patterns

## Identified Patterns

This document catalogs patterns and anti-patterns in distributed orchestration for autonomous AI coding systems, with use-cases grounded in research and practitioner experience.

---

## Cluster Architecture Patterns

### Federated Cluster Architecture

**Name**: Regional Coordinator Federation

**Description**: Organize agent clusters into regional federations, each with local coordinators that communicate for cross-region tasks. Local tasks stay within region; cross-region tasks coordinate through federation protocol.

**When to Use**:
- Geographically distributed teams
- Systems requiring low-latency local access
- Organizations with regional autonomy requirements

**Tradeoffs**:
- ✅ 3x throughput improvement over single coordinator
- ✅ Low latency for local operations
- ✅ Regional fault isolation
- ❌ Cross-region coordination complexity
- ❌ Consistency challenges between regions
- ❌ Requires federation protocol implementation

**Confidence: HIGH** - Validated in distributed systems research [paper:2].

---

### Service Mesh Coordination

**Name**: Sidecar-Based Agent Coordination

**Description**: Deploy coordination logic as sidecar proxies alongside agent processes. Service mesh handles service discovery, load balancing, and secure communication.

**When to Use**:
- Containerized agent deployments
- Systems requiring secure inter-agent communication
- Environments with dynamic agent scaling

**Tradeoffs**:
- ✅ Transparent coordination logic
- ✅ Built-in observability
- ✅ Secure communication (mTLS)
- ❌ Sidecar resource overhead
- ❌ Complexity in debugging
- ❌ Requires container orchestration

**Confidence: HIGH** - Established pattern with Istio, Linkerd.

---

### Worker Pool Pattern

**Name**: Pre-Warmed Agent Workers

**Description**: Maintain a pool of pre-initialized agent workers ready for task assignment. Workers are created ahead of demand and reused across tasks.

**When to Use**:
- Systems with variable but predictable load
- Tasks requiring fast startup
- Environments where agent initialization is expensive

**Tradeoffs**:
- ✅ Low task assignment latency
- ✅ Efficient resource utilization
- ✅ Predictable performance
- ❌ Resource overhead for idle workers
- ❌ Requires capacity planning
- ❌ Worker state management

**Confidence: HIGH** - Standard pattern from serverless and worker systems.

---

## Task Distribution Patterns

### Priority Queue with Fair Share

**Name**: Weighted Fair Queue Scheduling

**Description**: Combine priority queues with fair-share scheduling. High-priority tasks are processed first, but fair-share ensures lower-priority tasks eventually receive resources.

**When to Use**:
- Systems with mixed task criticality
- Multi-tenant environments
- Scenarios requiring both urgency and fairness

**Tradeoffs**:
- ✅ 89% reduction in task starvation
- ✅ Balances urgency with fairness
- ✅ Prevents priority inversion
- ❌ More complex scheduling logic
- ❌ Requires fair-share configuration
- ❌ May delay high-priority under load

**Confidence: HIGH** - Validated in scheduling research [paper:3].

---

### Work Stealing

**Name**: Dynamic Load Balancing

**Description**: Idle workers can steal tasks from busy workers' queues. Enables dynamic load balancing without central coordination.

**When to Use**:
- Variable task durations
- Systems with uneven load distribution
- Environments requiring automatic load balancing

**Tradeoffs**:
- ✅ Automatic load balancing
- ✅ No central scheduler bottleneck
- ✅ Adapts to variable task durations
- ❌ Coordination overhead for stealing
- ❌ May cause task reordering
- ❌ Complex to implement correctly

**Confidence: HIGH** - Established pattern from parallel computing.

---

### Sharded Task Queue

**Name**: Partition-Based Distribution

**Description**: Partition task queue by key (e.g., repository, project, user). Each partition has dedicated workers, ensuring ordering within partition.

**When to Use**:
- Tasks requiring ordering guarantees
- Systems with natural partition keys
- Scenarios benefiting from locality

**Tradeoffs**:
- ✅ Ordering guarantees within partition
- ✅ Reduced lock contention
- ✅ Natural locality for related tasks
- ❌ Uneven partition sizes
- ❌ Requires partition key selection
- ❌ Rebalancing complexity

**Confidence: MEDIUM** - Established pattern, agent-specific considerations.

---

## Concurrency Control Patterns

### Lease-Based Distributed Lock

**Name**: Time-Bounded Lock with Auto-Expire

**Description**: Acquire locks with time-based leases that automatically expire. Prevents deadlock from crashed agents holding locks indefinitely.

**When to Use**:
- All distributed locking scenarios
- Systems with potential for agent crashes
- Environments requiring fault tolerance

**Tradeoffs**:
- ✅ Automatic deadlock prevention
- ✅ Handles agent crashes gracefully
- ✅ Clear lock semantics
- ❌ Lease duration tuning required
- ❌ May expire during long operations
- ❌ Requires clock synchronization

**Confidence: HIGH** - Standard distributed systems pattern.

---

### Fencing Token Pattern

**Name**: Monotonic Token for Stale Lock Detection

**Description**: Include monotonically increasing token with lock acquisition. Operations check token to reject requests from stale lock holders.

**When to Use**:
- Systems with potential network partitions
- Scenarios requiring strict ordering
- Environments with delayed messages

**Tradeoffs**:
- ✅ Prevents stale lock holder interference
- ✅ Handles network delays
- ✅ Clear ordering semantics
- ❌ Requires token storage and checking
- ❌ Additional coordination overhead
- ❌ Not all systems support tokens

**Confidence: HIGH** - Established pattern from distributed databases.

---

### Optimistic Concurrency with Retry

**Name**: Version-Based Conflict Detection

**Description**: Proceed without locks, detect conflicts through version checking, retry on conflict. Suitable for low-contention scenarios.

**When to Use**:
- Low-contention resources
- Read-heavy workloads
- Systems preferring throughput over consistency

**Tradeoffs**:
- ✅ No lock overhead
- ✅ High throughput under low contention
- ✅ No deadlock risk
- ❌ Retry overhead under contention
- ❌ May starve under high contention
- ❌ Requires version tracking

**Confidence: HIGH** - Standard database concurrency pattern.

---

## Backpressure Patterns

### Adaptive Throttling

**Name**: Feedback-Based Rate Control

**Description**: Dynamically adjust request rate based on system metrics (latency, queue depth, error rate). Maintains stable performance under varying load.

**When to Use**:
- Systems with variable load
- Environments requiring latency guarantees
- Scenarios with unpredictable demand

**Tradeoffs**:
- ✅ Maintains 2x latency under 5x load
- ✅ Automatic adaptation
- ✅ Prevents cascade failures
- ❌ Requires metric collection
- ❌ Tuning of control parameters
- ❌ May over-throttle during spikes

**Confidence: HIGH** - Validated in reactive systems research [paper:4].

---

### Circuit Breaker

**Name**: Fail-Fast Under Load

**Description**: Monitor failure rate and open circuit when threshold exceeded. Fast-fail requests instead of waiting for timeouts.

**When to Use**:
- Systems with external dependencies
- Environments requiring fast failure
- Scenarios with potential cascade failures

**Tradeoffs**:
- ✅ Fast failure under problems
- ✅ Prevents cascade failures
- ✅ Allows recovery time
- ❌ May reject valid requests
- ❌ Requires threshold tuning
- ❌ Complex state management

**Confidence: HIGH** - Standard resilience pattern.

---

### Queue with Bounded Size

**Name**: Fixed-Capacity Request Buffer

**Description**: Maintain bounded queue for incoming requests. Reject requests when queue full, providing backpressure signal.

**When to Use**:
- Systems with bursty traffic
- Environments requiring memory bounds
- Scenarios with acceptable rejection

**Tradeoffs**:
- ✅ Memory bounded
- ✅ Clear backpressure signal
- ✅ Simple implementation
- ❌ Rejects valid requests when full
- ❌ Requires capacity planning
- ❌ May cause client failures

**Confidence: HIGH** - Standard queue pattern.

---

## Coordination Patterns

### MCP Protocol Integration

**Name**: Model Context Protocol for Tool Sharing

**Description**: Use MCP for standardized tool and context sharing between agents. Enables interoperability across different agent implementations.

**When to Use**:
- Multi-vendor agent environments
- Systems requiring tool portability
- Scenarios with evolving tool ecosystem

**Tradeoffs**:
- ✅ Standardized interfaces
- ✅ Tool portability
- ✅ Growing ecosystem
- ❌ Protocol overhead
- ❌ Requires MCP compliance
- ❌ Limited to protocol capabilities

**Confidence: MEDIUM** - Emerging standard [seed:Augment-MCP].

---

### Blackboard Pattern

**Name**: Shared State Space Coordination

**Description**: Agents communicate through shared blackboard (state space). Agents read from and write to blackboard without direct communication.

**When to Use**:
- Systems with many agents
- Scenarios requiring loose coupling
- Environments with complex coordination

**Tradeoffs**:
- ✅ Loose coupling between agents
- ✅ Scales to many agents
- ✅ Flexible coordination
- ❌ Blackboard contention
- ❌ State consistency challenges
- ❌ Debugging complexity

**Confidence: MEDIUM** - Established AI pattern, limited agent-specific validation.

---

### Contract Net Protocol

**Name**: Task Bidding and Assignment

**Description**: Tasks are announced to agents, who bid based on capability and availability. Best bid wins the task.

**When to Use**:
- Heterogeneous agent capabilities
- Dynamic task requirements
- Systems with variable agent availability

**Tradeoffs**:
- ✅ Dynamic capability matching
- ✅ Handles agent availability
- ✅ Decentralized assignment
- ❌ Bidding overhead
- ❌ May not find optimal assignment
- ❌ Requires bid evaluation

**Confidence: MEDIUM** - Established multi-agent pattern.

---

## Multi-Repo Patterns

### Event-Driven Cross-Repo Coordination

**Name**: Repository Event Propagation

**Description**: Changes in one repository emit events that trigger agents in other repositories. Enables loosely coupled cross-repo coordination.

**When to Use**:
- Microservice architectures
- Systems with repository boundaries
- Scenarios requiring eventual consistency

**Tradeoffs**:
- ✅ Loose coupling between repos
- ✅ Scalable to many repos
- ✅ Eventual consistency
- ❌ Event ordering challenges
- ❌ Debugging across repos
- ❌ Requires event infrastructure

**Confidence: MEDIUM** - Established event-driven pattern.

---

### Federated Context Management

**Name**: Per-Repo Context with Cross-Links

**Description**: Maintain separate context for each repository with links to related contexts. Agents load relevant contexts on demand.

**When to Use**:
- Large multi-repo systems
- Scenarios with context window limits
- Environments with clear repo boundaries

**Tradeoffs**:
- ✅ Respects context limits
- ✅ Clear repo boundaries
- ✅ On-demand loading
- ❌ Cross-repo context switching
- ❌ Link maintenance overhead
- ❌ May miss cross-repo dependencies

**Confidence: MEDIUM** - Emerging pattern for large codebases.

---

## Resilience Patterns

### Byzantine Fault Tolerance

**Name**: Consensus Despite Malicious Agents

**Description**: Use BFT consensus protocols to tolerate Byzantine (arbitrary/malicious) failures. Requires 3f+1 nodes to tolerate f failures.

**When to Use**:
- Security-critical systems
- Environments with potential compromise
- Scenarios requiring guaranteed correctness

**Tradeoffs**:
- ✅ Tolerates malicious behavior
- ✅ Guaranteed correctness
- ✅ No trusted coordinator needed
- ❌ High overhead (3f+1 nodes)
- ❌ Complex implementation
- ❌ Latency impact

**Confidence: MEDIUM** - Established theory, limited production use [paper:6].

---

### Consensus-Based Critical Changes

**Name**: Multi-Agent Agreement for Sensitive Operations

**Description**: Require multiple agents to agree on critical changes before execution. Prevents single compromised agent from causing harm.

**When to Use**:
- Critical code modifications
- Security-sensitive operations
- Production deployments

**Tradeoffs**:
- ✅ Prevents single point of compromise
- ✅ Increased confidence in changes
- ✅ Audit trail from consensus
- ❌ Increased latency
- ❌ Requires multiple agents
- ❌ May block on disagreement

**Confidence: MEDIUM** - Security best practice, implementation complexity.

---

## Anti-Patterns

### Single Coordinator Bottleneck

**Name**: Central Orchestrator SPOF

**Description**: All coordination flows through single coordinator, creating bottleneck and single point of failure.

**Failure Mode**:
- Scalability limited by coordinator capacity
- Coordinator failure halts entire system
- Latency increases with cluster size

**Remediation**: Use distributed coordination (Raft) or federated architecture.

**Confidence: HIGH** - Well-understood distributed systems anti-pattern.

---

### Unbounded Queues

**Name**: Infinite Buffer Anti-Pattern

**Description**: Using unbounded queues that grow without limit under load, leading to memory exhaustion and unpredictable latency.

**Failure Mode**:
- Memory exhaustion
- Unbounded latency growth
- System instability under load

**Remediation**: Use bounded queues with backpressure.

**Confidence: HIGH** - Standard systems anti-pattern.

---

### Lock Without Timeout

**Name**: Indefinite Lock Hold

**Description**: Acquiring locks without timeout or lease, leading to deadlock when agents crash while holding locks.

**Failure Mode**:
- Deadlock from crashed agents
- System hang waiting for locks
- Manual intervention required

**Remediation**: Always use lease-based locks with reasonable timeouts.

**Confidence: HIGH** - Standard distributed systems anti-pattern.

---

### Ignoring Network Partitions

**Name**: Assume Reliable Network

**Description**: Designing system as if network is always available, failing to handle partition scenarios.

**Failure Mode**:
- Split-brain behavior
- Data inconsistency
- System unavailability

**Remediation**: Design for partition tolerance (CAP theorem awareness).

**Confidence: HIGH** - Well-understood distributed systems anti-pattern.

---

### Synchronous Cross-Service Calls

**Name**: Blocking Remote Dependencies

**Description**: Making synchronous calls to remote services without timeout or fallback, creating cascading failures.

**Failure Mode**:
- Cascading failures
- Thread pool exhaustion
- System-wide outage

**Remediation**: Use async patterns, circuit breakers, timeouts.

**Confidence: HIGH** - Standard microservices anti-pattern.

---

### No Backpressure Propagation

**Name**: Silent Overload

**Description**: Accepting requests without propagating backpressure to callers, leading to overload and failure.

**Failure Mode**:
- System overload
- Degraded performance
- Silent failures

**Remediation**: Implement backpressure signals and propagation.

**Confidence: HIGH** - Standard reactive systems anti-pattern.

---

## Use-Case Patterns

### Enterprise Multi-Team Orchestration

**Pattern**: Federated Clusters with Priority Queues

**Description**: Deploy regional clusters for each team with local autonomy. Cross-team tasks use federation protocol. Priority queues ensure critical tasks processed first.

**Implementation Notes**:
- Use federated cluster architecture
- Implement priority queue with fair share
- Use MCP for cross-team tool sharing
- Deploy circuit breakers for external calls

**Confidence: HIGH** - Enterprise deployment pattern.

---

### CI/CD Pipeline Integration

**Pattern**: Worker Pool with Sharded Queues

**Description**: Pre-warmed worker pool for CI/CD tasks. Shard queues by repository for ordering guarantees. Use adaptive throttling for load management.

**Implementation Notes**:
- Use worker pool pattern for fast startup
- Shard by repository for ordering
- Implement adaptive throttling
- Use lease-based locks for shared resources

**Confidence: HIGH** - Standard CI/CD pattern.

---

### Cross-Repository Refactoring

**Pattern**: Event-Driven with Federated Context

**Description**: Emit events for cross-repo changes. Agents load federated contexts for affected repos. Use consensus for critical changes.

**Implementation Notes**:
- Use event-driven coordination
- Implement federated context management
- Require consensus for critical changes
- Use optimistic concurrency for speed

**Confidence: MEDIUM** - Complex scenario, emerging patterns.

---

## Summary

The patterns identified reveal key principles:

1. **Federation over centralization** - Regional coordinators scale better
2. **Lease-based locks essential** - Prevent deadlock from crashes
3. **Backpressure prevents cascade failures** - Adaptive throttling most effective
4. **MCP emerging as standard** - Protocol-based interoperability
5. **Consensus for critical operations** - Multi-agent agreement for security
6. **Bounded resources everywhere** - Queues, locks, and contexts need limits

**Confidence levels vary by pattern maturity** - Core distributed patterns (locks, queues, backpressure) HIGH confidence; agent-specific protocols (MCP, A2A) MEDIUM confidence; emerging patterns (federated context) MEDIUM to LOW.
