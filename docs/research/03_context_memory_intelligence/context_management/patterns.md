# Context Management - Patterns and Anti-Patterns

## Identified Patterns

### Pattern: Budget-Aware Retrieval

**Description**: Retrieval systems that respect explicit token budgets, returning optimally-sized context chunks that fit within allocated space while maximizing relevance.

**When to Use**:
- Large codebases with extensive context sources
- Cost-sensitive deployments with token limits
- Multi-stage workflows with predictable context needs

**Tradeoffs**:
- (+) Prevents context overflow errors
- (+) Enables predictable API costs
- (-) May truncate relevant context if budget too tight
- (-) Requires tuning for optimal budget allocation

**Implementation Considerations**:
- Define budgets per task phase (exploration vs. execution)
- Monitor budget utilization patterns
- Implement graceful degradation when budget exceeded

---

### Pattern: Hierarchical Summarization

**Description**: Multi-level summaries enabling zoom-in/zoom-out navigation through context, with high-level overviews and detailed drill-downs.

**When to Use**:
- Large codebases requiring multi-scale understanding
- Long-running agent sessions with accumulated context
- Cross-repository analysis requiring abstraction

**Tradeoffs**:
- (+) Enables navigation at multiple granularities
- (+) Reduces cognitive load for initial understanding
- (-) Summary quality depends on summarization model
- (-) May lose critical details at higher levels

**Implementation Considerations**:
- Define clear hierarchy levels (file → module → package → repo)
- Implement bidirectional navigation (zoom in/out)
- Cache summaries to avoid recomputation

---

### Pattern: U-Shaped Context Placement

**Description**: Placing critical information at context window beginnings and ends to mitigate the "lost in the middle" phenomenon where LLMs better attend to edges.

**When to Use**:
- Long context windows (>8K tokens)
- Critical instructions or constraints
- Multi-document reasoning tasks

**Tradeoffs**:
- (+) Improves recall of critical information
- (+) Aligns with observed LLM attention patterns
- (-) May disrupt logical document ordering
- (-) Requires identifying what's "critical"

**Implementation Considerations**:
- Place system prompts and constraints at start
- Position key retrieved documents at ends
- Use middle sections for supporting context

---

### Pattern: Task-Conditioned Context

**Description**: Context selection and filtering conditioned on current task type and phase, retrieving different context for coding vs. debugging vs. architecture tasks.

**When to Use**:
- Multi-mode agent systems
- Complex workflows with distinct phases
- Diverse task types requiring different context

**Tradeoffs**:
- (+) Improves context relevance
- (+) Reduces noise for specific tasks
- (-) Requires accurate task classification
- (-) Adds complexity to context pipeline

**Implementation Considerations**:
- Define task type taxonomy
- Map task types to context retrieval strategies
- Implement smooth transitions between phases

---

### Pattern: Context Caching

**Description**: Caching frequently-used or expensive-to-compute context to reduce latency and API costs across multiple queries.

**When to Use**:
- Repeated queries against same codebase
- Multi-turn conversations with shared context
- High-latency retrieval operations

**Tradeoffs**:
- (+) Reduces retrieval latency
- (+) Lowers API costs for repeated context
- (-) Cache invalidation complexity
- (-) Staleness risk for evolving codebases

**Implementation Considerations**:
- Define cache invalidation triggers (file changes, time-based)
- Implement cache warming for common queries
- Monitor cache hit rates and adjust strategy

---

### Pattern: Semantic Chunking

**Description**: Code-aware chunking that preserves semantic boundaries (functions, classes, modules) rather than arbitrary token limits.

**When to Use**:
- Code retrieval and understanding tasks
- Maintaining code coherence in context
- Cross-reference resolution

**Tradeoffs**:
- (+) Preserves code structure and meaning
- (+) Enables better cross-reference understanding
- (-) Variable chunk sizes complicate budgeting
- (-) May include unnecessary context within boundaries

**Implementation Considerations**:
- Use AST parsing for boundary detection
- Define maximum chunk size with graceful splitting
- Include context metadata (file path, line numbers)

---

### Pattern: Context Provenance Tracking

**Description**: Maintaining source attribution for all context, enabling debugging, trust evaluation, and context poisoning detection.

**When to Use**:
- Security-sensitive applications
- Multi-source context aggregation
- Debugging context-related errors

**Tradeoffs**:
- (+) Enables accountability and debugging
- (+) Supports trust scoring and filtering
- (-) Metadata overhead
- (-) Complexity in tracking transformations

**Implementation Considerations**:
- Attach source metadata to all context chunks
- Track transformations (summarization, compression)
- Implement provenance-aware retrieval

---

### Pattern: Sliding Window with Overlap

**Description**: Fixed-size context windows that slide through conversation/code with overlap to maintain continuity.

**When to Use**:
- Long conversations exceeding context limits
- Streaming code analysis
- Continuous monitoring tasks

**Tradeoffs**:
- (+) Maintains recent context
- (+) Predictable memory usage
- (-) Loses older context
- (-) Overhead from redundant overlap tokens

**Implementation Considerations**:
- Tune overlap size for continuity vs. efficiency
- Implement summary-based compression for dropped context
- Consider task-specific window sizes

---

## Identified Anti-Patterns

### Anti-Pattern: Context Stuffing

**Description**: Maximally filling context windows with all available information without prioritization or filtering.

**Failure Mode**:
- 23-45% of tokens wasted on irrelevant content
- "Lost in the middle" phenomenon buries critical information
- Increased API costs without proportional benefit
- Model confusion from contradictory or redundant context

**Mitigation**:
- Implement relevance-based filtering
- Use budget-aware retrieval with prioritization
- Apply U-shaped placement for critical items

---

### Anti-Pattern: Naive Truncation

**Description**: Simple cut-off of context when limits are reached, typically removing oldest or last-added content.

**Failure Mode**:
- Critical context lost arbitrarily
- Conversation coherence breaks
- Task failure when essential context removed
- Unpredictable behavior at boundaries

**Mitigation**:
- Implement intelligent summarization before truncation
- Use priority-based eviction
- Maintain critical context in reserved space

---

### Anti-Pattern: Context Silos

**Description**: Isolated context pools without sharing across related tasks, agents, or repositories.

**Failure Mode**:
- Redundant retrieval and computation
- Inconsistent understanding across agents
- Missed cross-repo patterns and dependencies
- Poor coordination in multi-agent systems

**Mitigation**:
- Implement shared context pools with namespacing
- Use context inheritance hierarchies
- Enable cross-agent context queries

---

### Anti-Pattern: Static Context Allocation

**Description**: Fixed context partitioning regardless of task type, phase, or content characteristics.

**Failure Mode**:
- Suboptimal allocation for varied tasks
- Wasted space on unused partitions
- Insufficient context for complex phases
- Inflexibility leads to errors

**Mitigation**:
- Implement dynamic allocation based on task phase
- Monitor utilization and adjust partitions
- Allow task-specific overrides

---

### Anti-Pattern: Unvalidated Context Injection

**Description**: Accepting external context (user input, retrieved documents, tool outputs) without validation or sanitization.

**Failure Mode**:
- Context poisoning attacks
- Injection of malicious instructions
- Quality degradation from low-quality sources
- Unpredictable agent behavior

**Mitigation**:
- Implement context provenance tracking
- Validate and sanitize external context
- Use trusted source whitelisting

---

### Anti-Pattern: Context Staleness

**Description**: Failing to update or invalidate cached context when underlying codebase changes.

**Failure Mode**:
- Decisions based on outdated information
- Inconsistency between context and actual code
- Debugging difficulty from stale references
- Security issues from outdated security context

**Mitigation**:
- Implement file-watcher-based invalidation
- Use versioning or timestamps for context
- Define staleness thresholds per context type

---

### Anti-Pattern: Retrieval Without Reranking

**Description**: Using initial retrieval scores without task-specific reranking or relevance refinement.

**Failure Mode**:
- Suboptimal context ordering
- Relevant items buried in results
- Generic relevance doesn't match task needs
- Wasted context on low-relevance items

**Mitigation**:
- Implement task-conditioned reranking
- Use cross-encoder models for relevance scoring
- Apply diversity and recency factors

---

### Anti-Pattern: Context Explosion

**Description**: Unbounded context growth through accumulation without compression or summarization.

**Failure Mode**:
- Context limits exceeded unexpectedly
- Degraded performance from context bloat
- Increased costs from redundant context
- Difficulty identifying relevant information

**Mitigation**:
- Implement periodic context compression
- Use hierarchical summarization
- Define context retention policies

---

## Use Cases Grounded in Research

### Use Case: Large Monorepo Navigation

**Pattern Combination**: Hierarchical Summarization + Semantic Chunking + Context Caching

**Scenario**: Agent navigating a 10M+ line monorepo to understand cross-module dependencies for a refactoring task.

**Implementation Notes**:
- Build multi-level summaries (file → module → package)
- Use AST-based chunking to preserve function boundaries
- Cache frequently-accessed module summaries
- Implement budget-aware retrieval per navigation depth

---

### Use Case: Multi-Agent Code Review

**Pattern Combination**: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement

**Scenario**: Multiple specialized agents (security, performance, style) reviewing the same codebase with different perspectives.

**Implementation Notes**:
- Track which agent contributed which context
- Condition context on review type (security → vulnerability DB, performance → benchmarks)
- Place code under review at context edges
- Share common context via shared pool

---

### Use Case: Long-Running Debugging Session

**Pattern Combination**: Sliding Window with Overlap + Hierarchical Summarization + Context Caching

**Scenario**: Agent debugging complex issue over extended session with accumulated context from multiple investigations.

**Implementation Notes**:
- Maintain sliding window of recent investigation
- Compress older context into hierarchical summaries
- Cache error patterns and previous solutions
- Implement context prioritization for debugging clues

---

### Use Case: Cross-Repository Feature Implementation

**Pattern Combination**: Task-Conditioned Context + Semantic Chunking + Budget-Aware Retrieval

**Scenario**: Agent implementing feature spanning multiple repositories with shared libraries.

**Implementation Notes**:
- Condition context on current repo focus
- Use semantic chunking for dependency understanding
- Allocate budget across repos based on relevance
- Implement context inheritance from shared libraries

---

### Pattern: Disposable Session Boundaries

**Description**: Treating sessions as disposable units with integrity boundaries, where context poisoning invalidates the entire session requiring a hard reset.

**When to Use**:
- Security-sensitive coding tasks
- Long-running agent sessions
- Tasks involving external context ingestion

**Tradeoffs**:
- (+) Clear recovery path when poisoning detected
- (+) Prevents cascading error propagation
- (-) Loss of session context on reset
- (-) Potential productivity disruption

**Implementation Considerations**:
- Define clear session boundary criteria
- Implement session state checkpointing for recovery
- Monitor for poisoning symptoms (degraded output, tool misalignment)
- Design tasks to be resumable after reset

*Source: Kimi-Research analysis (Roocode)*

---

### Pattern: Input Sanitization Pipeline

**Description**: Sanitizing all external content before context injection, stripping hidden characters, control codes, and potentially misleading formatting.

**When to Use**:
- Accepting user-provided logs or error messages
- Processing content from external sources
- Multi-user collaborative environments

**Tradeoffs**:
- (+) Prevents hidden character injection attacks
- (+) Reduces context noise
- (-) May remove meaningful formatting
- (-) Processing overhead

**Implementation Considerations**:
- Strip zero-width Unicode characters
- Remove terminal control sequences
- Normalize whitespace and formatting
- Log sanitization actions for debugging

*Source: Kimi-Research analysis (Roocode)*

---

### Pattern: Context Overflow Prevention

**Description**: Proactively managing context window utilization to prevent overflow-based poisoning where older useful context is evicted.

**When to Use**:
- Long-running sessions
- Large codebase analysis
- Multi-stage workflows

**Tradeoffs**:
- (+) Maintains context coherence
- (+) Prevents disproportionate influence of poisoned data
- (-) Requires active monitoring
- (-) May force premature context compression

**Implementation Considerations**:
- Monitor context utilization percentage
- Implement proactive summarization at thresholds
- Define critical context that must be preserved
- Use hierarchical compression for evicted content

*Source: Kimi-Research analysis (Roocode)*

---

### Pattern: Tool Output Validation Gate

**Description**: Validating and filtering tool outputs before they enter the context window, deleting nonsensical or incorrect data.

**When to Use**:
- Agent systems with tool access
- Multi-tool orchestration chains
- External API integrations

**Tradeoffs**:
- (+) Prevents tool output poisoning
- (+) Maintains context quality
- (-) Latency from validation
- (-) Risk of filtering valid outputs

**Implementation Considerations**:
- Define validation criteria per tool type
- Implement anomaly detection on outputs
- Allow manual override for edge cases
- Log filtered outputs for analysis

*Source: Kimi-Research analysis (Roocode)*

---

## Additional Anti-Patterns

### Anti-Pattern: Wake-Up Prompt Reliance

**Description**: Attempting to fix context poisoning with corrective prompts ("wake-up prompts") instead of session reset.

**Failure Mode**:
- Temporary masking of symptoms
- Poisoned context persists in conversational buffer
- Reversion to problematic behavior on subsequent queries
- Unreliable agent behavior

**Mitigation**:
- Treat compromised sessions as disposable
- Implement hard reset as primary recovery
- Design for session resumability after reset

*Source: Kimi-Research analysis (Roocode)*

---

### Anti-Pattern: Blind Code Comment Trust

**Description**: Treating code comments as authoritative guidance without validation against actual code behavior.

**Failure Mode**:
- Misinterpretation of stale documentation
- Implementation based on incorrect assumptions
- Generated code fails in production
- Compounding errors from misleading context

**Mitigation**:
- Cross-reference comments with actual code
- Maintain codebase documentation hygiene
- Mark outdated comments explicitly
- Validate comment accuracy during code review

*Source: Kimi-Research analysis (Roocode)*

---

### Anti-Pattern: Unbounded Session Growth

**Description**: Allowing sessions to grow indefinitely without context management or reset boundaries.

**Failure Mode**:
- Context window overflow
- Older critical context evicted
- Increased poisoning vulnerability
- Degraded agent performance

**Mitigation**:
- Define maximum session lengths
- Implement periodic context compression
- Design natural session breakpoints
- Monitor for degradation symptoms

*Source: Kimi-Research analysis (Roocode)*

---

### Anti-Pattern: Hidden Character Blindness

**Description**: Accepting pasted content without sanitization, allowing invisible Unicode characters to enter context.

**Failure Mode**:
- Erratic model behavior
- Outputs that don't correlate with visible input
- Difficult-to-diagnose issues
- Potential security vulnerabilities

**Mitigation**:
- Implement input sanitization pipeline
- Strip zero-width characters and control codes
- Use plain text sources when possible
- Log all input transformations

*Source: Kimi-Research analysis (Roocode)*

---

## MCP-Based Context Engine Patterns

*Source: Kimi-Research analysis (Augment Context Engine MCP, February 2026)*

### Pattern: MCP-Based Context Delegation

**Description**: Delegating context retrieval to specialized MCP-compatible context engines rather than implementing context management within the agent itself.

**When to Use**:
- Multi-agent systems requiring consistent context
- Teams wanting to decouple agent choice from context quality
- Projects with large, complex codebases requiring semantic understanding

**Tradeoffs**:
- (+) Access to specialized semantic search capabilities
- (+) Consistent context across different agents
- (+) Reduced agent complexity
- (-) External dependency for context retrieval
- (-) Potential vendor lock-in with specific context engines

**Implementation Considerations**:
- Evaluate MCP-compatible context engines (Augment, Sourcegraph Cody)
- Design fallback mechanisms for context engine unavailability
- Monitor context quality metrics across engines
- Implement caching for frequently-accessed context

---

### Pattern: Context Engine Protocol Standardization

**Description**: Using standardized protocols (MCP) for context exchange between agents and context providers, enabling interoperability and specialization.

**When to Use**:
- Building agent systems that need to work with multiple context providers
- Enabling context engine competition and substitution
- Enterprise environments requiring vendor flexibility

**Tradeoffs**:
- (+) Interoperability across agents and context engines
- (+) Enables best-of-breed component selection
- (+) Reduces vendor lock-in risk
- (-) Protocol overhead and latency
- (-) May limit access to proprietary features

**Implementation Considerations**:
- Use MCP stdio mode for local development (minimal latency)
- Use HTTP/SSE mode for remote/CI environments
- Implement protocol version negotiation
- Design for graceful degradation on protocol errors

---

### Pattern: Semantic Context Retrieval

**Description**: Using semantic search engines that understand code meaning, relationships, and patterns rather than simple text matching for context retrieval.

**When to Use**:
- Large codebases where keyword search misses relevant context
- Cross-file dependency understanding
- Tasks requiring architectural awareness

**Tradeoffs**:
- (+) Higher relevance in retrieved context
- (+) Discovers non-obvious connections
- (+) Reduces manual context specification
- (-) Higher computational cost
- (-) Quality depends on indexing quality

**Implementation Considerations**:
- Ensure codebase is fully indexed before use
- Monitor retrieval relevance scores
- Combine with keyword search for hybrid approach
- Implement relevance thresholds for context inclusion

---

### Pattern: Multi-Source Context Aggregation

**Description**: Aggregating context from multiple sources (code, commit history, documentation, tickets, tribal knowledge) into unified context for agents.

**When to Use**:
- Complex tasks requiring historical context
- Understanding why code was written a certain way
- Onboarding and knowledge transfer scenarios

**Tradeoffs**:
- (+) Richer context for decision-making
- (+) Captures institutional knowledge
- (-) Increased context volume
- (-) Potential for conflicting information
- (-) Source synchronization complexity

**Implementation Considerations**:
- Define source priority for conflict resolution
- Implement source attribution for all context
- Monitor context freshness per source
- Design for source-specific update frequencies

---

### Pattern: Context Architecture Over Model Selection

**Description**: Prioritizing context architecture quality over model selection, recognizing that context quality can have greater impact on performance than model size.

**When to Use**:
- Cost optimization scenarios
- Multi-model deployments
- Performance troubleshooting

**Tradeoffs**:
- (+) Better cost-performance ratio
- (+) More predictable performance
- (+) Reduced dependency on largest models
- (-) Requires investment in context infrastructure
- (-) Context quality becomes critical path

**Implementation Considerations**:
- Benchmark context quality independently of model
- Measure "context multiplier effect" on different models
- Invest in semantic indexing and retrieval
- Monitor for context quality degradation

# Context Management - Patterns and Anti-Patterns

## Identified Patterns

### Pattern: Budget-Aware Retrieval

**Description**: Retrieval systems that respect explicit token budgets, returning optimally-sized context chunks that fit within allocated space while maximizing relevance.

**When to Use**:
- Large codebases with extensive context sources
- Cost-sensitive deployments with token limits
- Multi-stage workflows with predictable context needs

**Tradeoffs**:
- (+) Prevents context overflow errors
- (+) Enables predictable API costs
- (-) May truncate relevant context if budget too tight
- (-) Requires tuning for optimal budget allocation

**Implementation Considerations**:
- Define budgets per task phase (exploration vs. execution)
- Monitor budget utilization patterns
- Implement graceful degradation when budget exceeded

---

### Pattern: Hierarchical Summarization

**Description**: Multi-level summaries enabling zoom-in/zoom-out navigation through context, with high-level overviews and detailed drill-downs.

**When to Use**:
- Large codebases requiring multi-scale understanding
- Long-running agent sessions with accumulated context
- Cross-repository analysis requiring abstraction

**Tradeoffs**:
- (+) Enables navigation at multiple granularities
- (+) Reduces cognitive load for initial understanding
- (-) Summary quality depends on summarization model
- (-) May lose critical details at higher levels

**Implementation Considerations**:
- Define clear hierarchy levels (file → module → package → repo)
- Implement bidirectional navigation (zoom in/out)
- Cache summaries to avoid recomputation

---

### Pattern: U-Shaped Context Placement

**Description**: Placing critical information at context window beginnings and ends to mitigate the "lost in the middle" phenomenon where LLMs better attend to edges.

**When to Use**:
- Long context windows (>8K tokens)
- Critical instructions or constraints
- Multi-document reasoning tasks

**Tradeoffs**:
- (+) Improves recall of critical information
- (+) Aligns with observed LLM attention patterns
- (-) May disrupt logical document ordering
- (-) Requires identifying what's "critical"

**Implementation Considerations**:
- Place system prompts and constraints at start
- Position key retrieved documents at ends
- Use middle sections for supporting context

---

### Pattern: Task-Conditioned Context

**Description**: Context selection and filtering conditioned on current task type and phase, retrieving different context for coding vs. debugging vs. architecture tasks.

**When to Use**:
- Multi-mode agent systems
- Complex workflows with distinct phases
- Diverse task types requiring different context

**Tradeoffs**:
- (+) Improves context relevance
- (+) Reduces noise for specific tasks
- (-) Requires accurate task classification
- (-) Adds complexity to context pipeline

**Implementation Considerations**:
- Define task type taxonomy
- Map task types to context retrieval strategies
- Implement smooth transitions between phases

---

### Pattern: Context Caching

**Description**: Caching frequently-used or expensive-to-compute context to reduce latency and API costs across multiple queries.

**When to Use**:
- Repeated queries against same codebase
- Multi-turn conversations with shared context
- High-latency retrieval operations

**Tradeoffs**:
- (+) Reduces retrieval latency
- (+) Lowers API costs for repeated context
- (-) Cache invalidation complexity
- (-) Staleness risk for evolving codebases

**Implementation Considerations**:
- Define cache invalidation triggers (file changes, time-based)
- Implement cache warming for common queries
- Monitor cache hit rates and adjust strategy

---

### Pattern: Semantic Chunking

**Description**: Code-aware chunking that preserves semantic boundaries (functions, classes, modules) rather than arbitrary token limits.

**When to Use**:
- Code retrieval and understanding tasks
- Maintaining code coherence in context
- Cross-reference resolution

**Tradeoffs**:
- (+) Preserves code structure and meaning
- (+) Enables better cross-reference understanding
- (-) Variable chunk sizes complicate budgeting
- (-) May include unnecessary context within boundaries

**Implementation Considerations**:
- Use AST parsing for boundary detection
- Define maximum chunk size with graceful splitting
- Include context metadata (file path, line numbers)

---

### Pattern: Context Provenance Tracking

**Description**: Maintaining source attribution for all context, enabling debugging, trust evaluation, and context poisoning detection.

**When to Use**:
- Security-sensitive applications
- Multi-source context aggregation
- Debugging context-related errors

**Tradeoffs**:
- (+) Enables accountability and debugging
- (+) Supports trust scoring and filtering
- (-) Metadata overhead
- (-) Complexity in tracking transformations

**Implementation Considerations**:
- Attach source metadata to all context chunks
- Track transformations (summarization, compression)
- Implement provenance-aware retrieval

---

### Pattern: Sliding Window with Overlap

**Description**: Fixed-size context windows that slide through conversation/code with overlap to maintain continuity.

**When to Use**:
- Long conversations exceeding context limits
- Streaming code analysis
- Continuous monitoring tasks

**Tradeoffs**:
- (+) Maintains recent context
- (+) Predictable memory usage
- (-) Loses older context
- (-) Overhead from redundant overlap tokens

**Implementation Considerations**:
- Tune overlap size for continuity vs. efficiency
- Implement summary-based compression for dropped context
- Consider task-specific window sizes

---

## Identified Anti-Patterns

### Anti-Pattern: Context Stuffing

**Description**: Maximally filling context windows with all available information without prioritization or filtering.

**Failure Mode**:
- 23-45% of tokens wasted on irrelevant content
- "Lost in the middle" phenomenon buries critical information
- Increased API costs without proportional benefit
- Model confusion from contradictory or redundant context

**Mitigation**:
- Implement relevance-based filtering
- Use budget-aware retrieval with prioritization
- Apply U-shaped placement for critical items

---

### Anti-Pattern: Naive Truncation

**Description**: Simple cut-off of context when limits are reached, typically removing oldest or last-added content.

**Failure Mode**:
- Critical context lost arbitrarily
- Conversation coherence breaks
- Task failure when essential context removed
- Unpredictable behavior at boundaries

**Mitigation**:
- Implement intelligent summarization before truncation
- Use priority-based eviction
- Maintain critical context in reserved space

---

### Anti-Pattern: Context Silos

**Description**: Isolated context pools without sharing across related tasks, agents, or repositories.

**Failure Mode**:
- Redundant retrieval and computation
- Inconsistent understanding across agents
- Missed cross-repo patterns and dependencies
- Poor coordination in multi-agent systems

**Mitigation**:
- Implement shared context pools with namespacing
- Use context inheritance hierarchies
- Enable cross-agent context queries

---

### Anti-Pattern: Static Context Allocation

**Description**: Fixed context partitioning regardless of task type, phase, or content characteristics.

**Failure Mode**:
- Suboptimal allocation for varied tasks
- Wasted space on unused partitions
- Insufficient context for complex phases
- Inflexibility leads to errors

**Mitigation**:
- Implement dynamic allocation based on task phase
- Monitor utilization and adjust partitions
- Allow task-specific overrides

---

### Anti-Pattern: Unvalidated Context Injection

**Description**: Accepting external context (user input, retrieved documents, tool outputs) without validation or sanitization.

**Failure Mode**:
- Context poisoning attacks
- Injection of malicious instructions
- Quality degradation from low-quality sources
- Unpredictable agent behavior

**Mitigation**:
- Implement context provenance tracking
- Validate and sanitize external context
- Use trusted source whitelisting

---

### Anti-Pattern: Context Staleness

**Description**: Failing to update or invalidate cached context when underlying codebase changes.

**Failure Mode**:
- Decisions based on outdated information
- Inconsistency between context and actual code
- Debugging difficulty from stale references
- Security issues from outdated security context

**Mitigation**:
- Implement file-watcher-based invalidation
- Use versioning or timestamps for context
- Define staleness thresholds per context type

---

### Anti-Pattern: Retrieval Without Reranking

**Description**: Using initial retrieval scores without task-specific reranking or relevance refinement.

**Failure Mode**:
- Suboptimal context ordering
- Relevant items buried in results
- Generic relevance doesn't match task needs
- Wasted context on low-relevance items

**Mitigation**:
- Implement task-conditioned reranking
- Use cross-encoder models for relevance scoring
- Apply diversity and recency factors

---

### Anti-Pattern: Context Explosion

**Description**: Unbounded context growth through accumulation without compression or summarization.

**Failure Mode**:
- Context limits exceeded unexpectedly
- Degraded performance from context bloat
- Increased costs from redundant context
- Difficulty identifying relevant information

**Mitigation**:
- Implement periodic context compression
- Use hierarchical summarization
- Define context retention policies

---

## Use Cases Grounded in Research

### Use Case: Large Monorepo Navigation

**Pattern Combination**: Hierarchical Summarization + Semantic Chunking + Context Caching

**Scenario**: Agent navigating a 10M+ line monorepo to understand cross-module dependencies for a refactoring task.

**Implementation Notes**:
- Build multi-level summaries (file → module → package)
- Use AST-based chunking to preserve function boundaries
- Cache frequently-accessed module summaries
- Implement budget-aware retrieval per navigation depth

---

### Use Case: Multi-Agent Code Review

**Pattern Combination**: Context Provenance Tracking + Task-Conditioned Context + U-Shaped Placement

**Scenario**: Multiple specialized agents (security, performance, style) reviewing the same codebase with different perspectives.

**Implementation Notes**:
- Track which agent contributed which context
- Condition context on review type (security → vulnerability DB, performance → benchmarks)
- Place code under review at context edges
- Share common context via shared pool

---

### Use Case: Long-Running Debugging Session

**Pattern Combination**: Sliding Window with Overlap + Hierarchical Summarization + Context Caching

**Scenario**: Agent debugging complex issue over extended session with accumulated context from multiple investigations.

**Implementation Notes**:
- Maintain sliding window of recent investigation
- Compress older context into hierarchical summaries
- Cache error patterns and previous solutions
- Implement context prioritization for debugging clues

---

### Use Case: Cross-Repository Feature Implementation

**Pattern Combination**: Task-Conditioned Context + Semantic Chunking + Budget-Aware Retrieval

**Scenario**: Agent implementing feature spanning multiple repositories with shared libraries.

**Implementation Notes**:
- Condition context on current repo focus
- Use semantic chunking for dependency understanding
- Allocate budget across repos based on relevance
- Implement context inheritance from shared libraries

---

### Pattern: Disposable Session Boundaries

**Description**: Treating sessions as disposable units with integrity boundaries, where context poisoning invalidates the entire session requiring a hard reset.

**When to Use**:
- Security-sensitive coding tasks
- Long-running agent sessions
- Tasks involving external context ingestion

**Tradeoffs**:
- (+) Clear recovery path when poisoning detected
- (+) Prevents cascading error propagation
- (-) Loss of session context on reset
- (-) Potential productivity disruption

**Implementation Considerations**:
- Define clear session boundary criteria
- Implement session state checkpointing for recovery
- Monitor for poisoning symptoms (degraded output, tool misalignment)
- Design tasks to be resumable after reset

*Source: Kimi-Research analysis (Roocode)*

---

### Pattern: Input Sanitization Pipeline

**Description**: Sanitizing all external content before context injection, stripping hidden characters, control codes, and potentially misleading formatting.

**When to Use**:
- Accepting user-provided logs or error messages
- Processing content from external sources
- Multi-user collaborative environments

**Tradeoffs**:
- (+) Prevents hidden character injection attacks
- (+) Reduces context noise
- (-) May remove meaningful formatting
- (-) Processing overhead

**Implementation Considerations**:
- Strip zero-width Unicode characters
- Remove terminal control sequences
- Normalize whitespace and formatting
- Log sanitization actions for debugging

*Source: Kimi-Research analysis (Roocode)*

---

### Pattern: Context Overflow Prevention

**Description**: Proactively managing context window utilization to prevent overflow-based poisoning where older useful context is evicted.

**When to Use**:
- Long-running sessions
- Large codebase analysis
- Multi-stage workflows

**Tradeoffs**:
- (+) Maintains context coherence
- (+) Prevents disproportionate influence of poisoned data
- (-) Requires active monitoring
- (-) May force premature context compression

**Implementation Considerations**:
- Monitor context utilization percentage
- Implement proactive summarization at thresholds
- Define critical context that must be preserved
- Use hierarchical compression for evicted content

*Source: Kimi-Research analysis (Roocode)*

---

### Pattern: Tool Output Validation Gate

**Description**: Validating and filtering tool outputs before they enter the context window, deleting nonsensical or incorrect data.

**When to Use**:
- Agent systems with tool access
- Multi-tool orchestration chains
- External API integrations

**Tradeoffs**:
- (+) Prevents tool output poisoning
- (+) Maintains context quality
- (-) Latency from validation
- (-) Risk of filtering valid outputs

**Implementation Considerations**:
- Define validation criteria per tool type
- Implement anomaly detection on outputs
- Allow manual override for edge cases
- Log filtered outputs for analysis

*Source: Kimi-Research analysis (Roocode)*

---

## Additional Anti-Patterns

### Anti-Pattern: Wake-Up Prompt Reliance

**Description**: Attempting to fix context poisoning with corrective prompts ("wake-up prompts") instead of session reset.

**Failure Mode**:
- Temporary masking of symptoms
- Poisoned context persists in conversational buffer
- Reversion to problematic behavior on subsequent queries
- Unreliable agent behavior

**Mitigation**:
- Treat compromised sessions as disposable
- Implement hard reset as primary recovery
- Design for session resumability after reset

*Source: Kimi-Research analysis (Roocode)*

---

### Anti-Pattern: Blind Code Comment Trust

**Description**: Treating code comments as authoritative guidance without validation against actual code behavior.

**Failure Mode**:
- Misinterpretation of stale documentation
- Implementation based on incorrect assumptions
- Generated code fails in production
- Compounding errors from misleading context

**Mitigation**:
- Cross-reference comments with actual code
- Maintain codebase documentation hygiene
- Mark outdated comments explicitly
- Validate comment accuracy during code review

*Source: Kimi-Research analysis (Roocode)*

---

### Anti-Pattern: Unbounded Session Growth

**Description**: Allowing sessions to grow indefinitely without context management or reset boundaries.

**Failure Mode**:
- Context window overflow
- Older critical context evicted
- Increased poisoning vulnerability
- Degraded agent performance

**Mitigation**:
- Define maximum session lengths
- Implement periodic context compression
- Design natural session breakpoints
- Monitor for degradation symptoms

*Source: Kimi-Research analysis (Roocode)*

---

### Anti-Pattern: Hidden Character Blindness

**Description**: Accepting pasted content without sanitization, allowing invisible Unicode characters to enter context.

**Failure Mode**:
- Erratic model behavior
- Outputs that don't correlate with visible input
- Difficult-to-diagnose issues
- Potential security vulnerabilities

**Mitigation**:
- Implement input sanitization pipeline
- Strip zero-width characters and control codes
- Use plain text sources when possible
- Log all input transformations

*Source: Kimi-Research analysis (Roocode)*

---

## MCP-Based Context Engine Patterns

*Source: Kimi-Research analysis (Augment Context Engine MCP, February 2026)*

### Pattern: MCP-Based Context Delegation

**Description**: Delegating context retrieval to specialized MCP-compatible context engines rather than implementing context management within the agent itself.

**When to Use**:
- Multi-agent systems requiring consistent context
- Teams wanting to decouple agent choice from context quality
- Projects with large, complex codebases requiring semantic understanding

**Tradeoffs**:
- (+) Access to specialized semantic search capabilities
- (+) Consistent context across different agents
- (+) Reduced agent complexity
- (-) External dependency for context retrieval
- (-) Potential vendor lock-in with specific context engines

**Implementation Considerations**:
- Evaluate MCP-compatible context engines (Augment, Sourcegraph Cody)
- Design fallback mechanisms for context engine unavailability
- Monitor context quality metrics across engines
- Implement caching for frequently-accessed context

---

### Pattern: Context Engine Protocol Standardization

**Description**: Using standardized protocols (MCP) for context exchange between agents and context providers, enabling interoperability and specialization.

**When to Use**:
- Building agent systems that need to work with multiple context providers
- Enabling context engine competition and substitution
- Enterprise environments requiring vendor flexibility

**Tradeoffs**:
- (+) Interoperability across agents and context engines
- (+) Enables best-of-breed component selection
- (+) Reduces vendor lock-in risk
- (-) Protocol overhead and latency
- (-) May limit access to proprietary features

**Implementation Considerations**:
- Use MCP stdio mode for local development (minimal latency)
- Use HTTP/SSE mode for remote/CI environments
- Implement protocol version negotiation
- Design for graceful degradation on protocol errors

---

### Pattern: Semantic Context Retrieval

**Description**: Using semantic search engines that understand code meaning, relationships, and patterns rather than simple text matching for context retrieval.

**When to Use**:
- Large codebases where keyword search misses relevant context
- Cross-file dependency understanding
- Tasks requiring architectural awareness

**Tradeoffs**:
- (+) Higher relevance in retrieved context
- (+) Discovers non-obvious connections
- (+) Reduces manual context specification
- (-) Higher computational cost
- (-) Quality depends on indexing quality

**Implementation Considerations**:
- Ensure codebase is fully indexed before use
- Monitor retrieval relevance scores
- Combine with keyword search for hybrid approach
- Implement relevance thresholds for context inclusion

---

### Pattern: Multi-Source Context Aggregation

**Description**: Aggregating context from multiple sources (code, commit history, documentation, tickets, tribal knowledge) into unified context for agents.

**When to Use**:
- Complex tasks requiring historical context
- Understanding why code was written a certain way
- Onboarding and knowledge transfer scenarios

**Tradeoffs**:
- (+) Richer context for decision-making
- (+) Captures institutional knowledge
- (-) Increased context volume
- (-) Potential for conflicting information
- (-) Source synchronization complexity

**Implementation Considerations**:
- Define source priority for conflict resolution
- Implement source attribution for all context
- Monitor context freshness per source
- Design for source-specific update frequencies

---

### Pattern: Context Architecture Over Model Selection

**Description**: Prioritizing context architecture quality over model selection, recognizing that context quality can have greater impact on performance than model size.

**When to Use**:
- Cost optimization scenarios
- Multi-model deployments
- Performance troubleshooting

**Tradeoffs**:
- (+) Better cost-performance ratio
- (+) More predictable performance
- (+) Reduced dependency on largest models
- (-) Requires investment in context infrastructure
- (-) Context quality becomes critical path

**Implementation Considerations**:
- Benchmark context quality independently of model
- Measure "context multiplier effect" on different models
- Invest in semantic indexing and retrieval
- Monitor for context quality degradation
