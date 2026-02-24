# Roocode Context Poisoning Analysis

## Executive Summary

Context poisoning is a critical security and reliability concern in AI coding systems, particularly in agentic development environments like Roocode. This analysis examines the Roocode documentation on context poisoning, which describes how contaminated context within a chat session can lead to progressive degradation of AI agent performance. The documentation emphasizes that **once a session's context is compromised, it must be treated as disposable** - there is no reliable recovery mechanism other than starting fresh. This represents a fundamental architectural constraint in current LLM-based coding agents that has significant implications for secure and reliable software development workflows.

**Key Finding**: The "no recovery" principle - Roocode explicitly states that corrective prompts ("wake-up prompts") cannot reliably fix context poisoning, making session hygiene a critical operational requirement.

---

## What is Context Poisoning

### Definition

Context poisoning occurs when **inaccurate or irrelevant data contaminates the language model's active context**, leading the model to:
- Draw incorrect conclusions
- Provide erroneous information to tools
- Progressively deviate from the intended task with each interaction

### Core Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Persistence** | Once bad data enters the context, it tends to persist across interactions |
| **Amplification** | The model re-evaluates tainted information in subsequent reasoning cycles |
| **Permanence** | Similar to a "permanent flaw affecting its perception until the context is completely reset" |
| **Session-bound** | Poisoning is contained within a single chat session |

### The "Disposable Session" Principle

> "Context poisoning is a persistent issue within a given session. Once a chat session's context is compromised, treat that session as disposable. Starting fresh with a clean context is crucial for maintaining the accuracy and effectiveness of your Roo Code agent."

This principle establishes a fundamental operational model: **sessions have integrity boundaries**, and crossing those boundaries (through poisoning) invalidates the entire session.

---

## Attack Vectors & Mechanisms

### 1. Model Hallucination

**Description**: The model generates an incorrect piece of information and subsequently treats it as a factual part of the context.

**Mechanism**:
```
User Query → Model Generates Incorrect "Fact" → Model References "Fact" in Future Reasoning → Compounding Errors
```

**Impact**: Self-reinforcing error propagation where the model's own incorrect outputs become part of its knowledge base for the session.

### 2. Code Comments Contamination

**Description**: Outdated, incorrect, or ambiguous comments in the codebase can be misinterpreted by the model.

**Attack Surface**:
- Legacy code with stale documentation
- Ambiguous or misleading inline comments
- TODO/FIXME comments that no longer apply
- Incorrect API documentation in comments

**Mechanism**: The model ingests code context including comments, treating them as authoritative guidance, which then influences subsequent code generation and modification decisions.

### 3. Contaminated User Input

**Description**: Copy-pasting logs or text containing hidden or rogue control characters.

**Technical Details**:
- Hidden Unicode characters (zero-width spaces, bidirectional overrides)
- Control characters in log outputs
- Formatted text with embedded formatting codes
- Clipboard content from rich text sources

**Risk Level**: High - user actions can inadvertently introduce invisible contamination.

### 4. Context Window Overflow

**Description**: As a session grows, older, useful information may be pushed out of the model's limited context window, allowing "poisoned" data to have a greater relative impact.

**Mechanism**:
```
Session Growth → Context Window Fills → Older Information Evicted → Poisoned Data Dominates Remaining Context
```

**Architectural Constraint**: This reveals a fundamental tension in LLM-based systems - finite context windows create vulnerability windows where poisoned data can achieve disproportionate influence.

### Attack Vector Summary Table

| Vector | Source | Visibility | Preventability |
|--------|--------|------------|----------------|
| Model Hallucination | Internal | Hidden | Partial (via validation) |
| Code Comments | External | Visible | Partial (code review) |
| Contaminated Input | User | Often Hidden | High (input sanitization) |
| Context Overflow | Architectural | Hidden | Partial (session management) |

---

## Mitigation Strategies

### Recovery Strategies (Post-Poisoning)

#### 1. Hard Reset the Session

**Effectiveness**: ★★★★★ (Most Dependable)

**Implementation**:
- Start a new chat session
- Clear the contaminated context entirely
- Provide clean prompt and correct tool definitions from the outset

**Rationale**: Complete elimination of poisoned context - the only guaranteed recovery method.

#### 2. Minimize Manual Data Dumps

**Effectiveness**: ★★★★☆ (Preventive)

**Implementation**:
- Be selective when pasting logs or other data
- Only include essential information the model requires
- Sanitize pasted content before inclusion

#### 3. Manage Context Window Size

**Effectiveness**: ★★★☆☆ (Architectural)

**Implementation**:
- Break large or complex tasks into smaller, focused chat sessions
- Ensure stale or irrelevant information ages out of context window more quickly
- Design task boundaries around natural context limits

#### 4. Validate Tool Output

**Effectiveness**: ★★★★☆ (Reactive)

**Implementation**:
- If a tool returns nonsensical or clearly incorrect data
- Delete that message from the chat history before the model processes it
- Prevent incorporation of bad data into context

### Why "Wake-Up Prompts" Don't Work

**Community Question**: "Have you found a prompt that wakes it back up? Maybe a prompt that just has the tools instructions we can push back in manually?"

**Roocode's Answer**: **No.**

**Detailed Explanation**:

| Aspect | Reality |
|--------|---------|
| Temporary Effect | Re-injecting tool definitions can mask damage for one or some interactions |
| Underlying Problem | The poisoned context remains in the conversational buffer |
| Reversion Risk | Any query outside the immediate "patch" will likely re-trigger the original issue |
| Reliability | "Akin to placing a warning label on a leaking pipe instead of repairing it" |

**Key Insight**: Corrective prompts only suppress symptoms; the corrupted data persists in session history, ready to cause further issues.

---

## Prevention Best Practices

### 1. Input Hygiene

- **Sanitize all pasted content**: Strip hidden characters before pasting into chat
- **Prefer plain text**: Avoid rich text clipboard sources
- **Review logs before sharing**: Remove irrelevant or potentially misleading entries

### 2. Codebase Hygiene

- **Maintain accurate comments**: Regularly audit and update code documentation
- **Remove stale TODOs**: Clean up outdated guidance that could mislead the model
- **Document known issues**: Explicitly mark problematic code sections

### 3. Session Management

- **Define session boundaries**: Plan natural breakpoints for complex tasks
- **Monitor for symptoms**: Watch for early signs of context poisoning
- **Don't hesitate to restart**: Treat compromised sessions as disposable

### 4. Output Validation

- **Review tool calls**: Verify tool invocations match intended operations
- **Check for coherence**: Watch for nonsensical or repetitive outputs
- **Delete bad outputs**: Remove incorrect tool responses before they enter context

### 5. Architectural Awareness

- **Understand context limits**: Know your model's context window size
- **Plan for overflow**: Design workflows that don't depend on distant context
- **Use focused sessions**: Prefer multiple short sessions over one long session

---

## Real-World Scenarios

### Scenario 1: The Hallucinated API

**Setup**: Developer asks Roocode to integrate with a third-party API

**Poisoning Event**:
1. Model hallucinates non-existent API endpoint parameters
2. Subsequent requests build on this incorrect specification
3. Generated code repeatedly fails with "parameter not recognized" errors
4. Model attempts to "fix" by hallucinating more incorrect parameters

**Resolution**: Hard reset, provide actual API documentation in fresh session

### Scenario 2: The Misleading Comment

**Setup**: Working with legacy codebase containing outdated comments

**Poisoning Event**:
1. Model reads stale comment describing deprecated function behavior
2. Implements new feature using incorrect assumptions from comment
3. Generated code appears correct but fails in production
4. Model's subsequent "fixes" compound the misunderstanding

**Resolution**: Codebase cleanup + fresh session with corrected context

### Scenario 3: The Hidden Character

**Setup**: Developer pastes error log from terminal

**Poisoning Event**:
1. Log contains zero-width Unicode characters from terminal formatting
2. Characters invisible to human eye but processed by model
3. Model behavior becomes erratic and unpredictable
4. Outputs don't correlate with visible input

**Resolution**: Session reset, paste logs through sanitization tool first

### Scenario 4: The Long-Running Session

**Setup**: Extended refactoring session with many iterations

**Poisoning Event**:
1. Session grows beyond effective context window
2. Early architectural decisions evicted from context
3. Later changes contradict established patterns (now invisible)
4. Codebase becomes inconsistent and broken

**Resolution**: Break into focused sessions per refactoring area

---

## Relationship to Security Architecture

### Context Poisoning as a Security Concern

While Roocode frames context poisoning primarily as a reliability issue, it has significant security implications:

#### 1. Indirect Code Injection

Poisoned context can lead to:
- Inclusion of vulnerable dependencies (based on hallucinated recommendations)
- Generation of insecure code patterns (based on misinterpreted comments)
- Bypass of security controls (based on incorrect tool usage)

#### 2. Denial of Service

Context poisoning can cause:
- Infinite loops in orchestration chains
- Resource exhaustion through repeated failed operations
- Developer productivity loss requiring session restarts

#### 3. Integrity Violations

Compromised sessions may:
- Modify code in unintended ways
- Delete or corrupt files based on hallucinated requirements
- Apply changes that contradict security policies

### Architectural Implications

#### Trust Boundaries

```
┌─────────────────────────────────────────────────────────────┐
│                    TRUST BOUNDARY: SESSION                   │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  Context Window (Finite, Mutable)                     │  │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐     │  │
│  │  │ Message │ │ Message │ │ Message │ │ Message │ ... │  │
│  │  │   1     │ │   2     │ │   3     │ │   N     │     │  │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘     │  │
│  │                                                        │  │
│  │  [Poisoned data can persist and propagate here]       │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                              │
│  Mitigation: Hard reset creates NEW trust boundary          │
└─────────────────────────────────────────────────────────────┘
```

#### Defense in Depth

| Layer | Control | Effectiveness |
|-------|---------|---------------|
| Input | Sanitization | Prevents contaminated user input |
| Processing | Output validation | Catches hallucinated/incorrect tool outputs |
| Session | Size management | Limits context overflow risk |
| Recovery | Hard reset | Ultimate fallback when controls fail |

### Comparison to Traditional Security Concepts

| Traditional Concept | Context Poisoning Parallel |
|--------------------|---------------------------|
| Memory corruption | Context contamination |
| Buffer overflow | Context window overflow |
| Code injection | Malicious/hidden character injection |
| Session hijacking | Context manipulation |
| Input validation | Content sanitization |

### Integration with Broader AI Security

Context poisoning intersects with:

1. **Prompt Injection**: Both manipulate model behavior through input manipulation
2. **Jailbreaking**: Both seek to subvert model's intended operation
3. **Data Poisoning**: Both involve contamination of model's working context
4. **Supply Chain**: Code comments as an attack vector mirror dependency risks

---

## References

### Primary Source

| Reference | URL | Quality Score | Notes |
|-----------|-----|---------------|-------|
| Roocode Context Poisoning Documentation | https://docs.roocode.com/advanced-usage/context-poisoning | 9/10 | Official documentation, comprehensive coverage, clear recommendations, last updated Feb 11, 2026 |

**Quality Assessment**:
- **Completeness**: 9/10 - Covers definition, symptoms, causes, recovery, and prevention
- **Clarity**: 9/10 - Well-structured with clear headings and actionable advice
- **Technical Depth**: 7/10 - Practical focus, could benefit from more technical detail on underlying mechanisms
- **Currency**: 10/10 - Recently updated (Feb 2026), reflects current understanding
- **Actionability**: 10/10 - Clear, actionable recommendations throughout

### Related Concepts (External)

| Concept | Relevance |
|---------|-----------|
| LLM Context Window Management | Architectural foundation for understanding overflow issues |
| Prompt Injection Attacks | Related attack vector in LLM systems |
| AI Agent Reliability | Broader context for understanding operational challenges |
| Conversational State Management | Technical patterns for session handling |

---

## Key Findings Summary

1. **No Recovery Possible**: Once context is poisoned, the only reliable solution is a hard session reset

2. **Four Primary Attack Vectors**: Model hallucination, code comments, contaminated input, context overflow

3. **Symptoms Are Observable**: Degraded output, tool misalignment, orchestration failures, temporary fixes, tool confusion

4. **Prevention is Critical**: Input sanitization, codebase hygiene, session management, output validation

5. **Architectural Constraint**: Finite context windows create inherent vulnerability to overflow-based poisoning

6. **Security-Relevant**: While framed as reliability, context poisoning can lead to security vulnerabilities through incorrect code generation

---

*Analysis completed: Based on Roocode documentation as of February 2026*
