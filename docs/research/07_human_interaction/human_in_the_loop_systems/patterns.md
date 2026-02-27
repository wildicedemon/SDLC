# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |

# Human-in-the-Loop Systems: Patterns

This document catalogs identified patterns and anti-patterns for human-in-the-loop systems in autonomous AI coding agents, grounded in the research literature.

---

## Identified Patterns

### Pattern 1: Confidence-Calibrated Escalation

**Name**: Confidence-Calibrated Escalation

**Description**: Automatically escalate to human intervention when agent confidence falls below a calibrated threshold, with different thresholds for different risk levels.

**When to Use**:
- Tasks with measurable confidence scores
- Environments where some errors are acceptable but high-impact errors must be prevented
- Scenarios with varying risk levels across action types

**Implementation Elements**:
- Confidence estimation for each action/decision
- Risk classification for action categories
- Threshold calibration based on historical accuracy
- Graceful degradation path (base model → large model → human)

**Tradeoffs**:
- **Benefits**: Reduces unnecessary interruptions while maintaining safety; scalable to high-frequency operations
- **Costs**: Requires calibration data and ongoing monitoring; threshold tuning is non-trivial
- **Risks**: Poor calibration leads to either over-escalation (fatigue) or under-escalation (errors)

**Sources**: [paper:9][paper:10][paper:23][paper:24]

---

### Pattern 2: Progressive Disclosure of Reasoning

**Name**: Progressive Disclosure of Reasoning

**Description**: Present minimal explanation by default with option to expand for more detail, reducing cognitive load while maintaining transparency.

**When to Use**:
- Complex agent reasoning that could overwhelm users
- Mixed audience with varying expertise levels
- Time-sensitive decisions where quick review is needed

**Implementation Elements**:
- Tiered explanation levels (summary → key factors → full reasoning)
- Expandable UI elements for detail access
- Highlighted critical information at top level
- Optional deep-dive into specific reasoning steps

**Tradeoffs**:
- **Benefits**: Reduces cognitive load; accommodates different user needs; faster decision-making
- **Costs**: May hide relevant details; requires careful summarization
- **Risks**: Users may miss critical information in collapsed sections

**Sources**: [paper:13][paper:14][paper:19]

---

### Pattern 3: Intelligent Approval Batching

**Name**: Intelligent Approval Batching

**Description**: Group related approval requests together for batch review rather than interrupting for each individual request.

**When to Use**:
- High-frequency operations with multiple related actions
- Workflows with natural grouping points (e.g., after planning phase)
- Environments where interruption cost is high

**Implementation Elements**:
- Action dependency analysis for grouping
- Configurable batch windows (time-based or count-based)
- Priority override for urgent items
- Summary view showing batch contents

**Tradeoffs**:
- **Benefits**: Reduces interruption frequency; enables holistic review; better context for decisions
- **Costs**: May delay urgent approvals; batching logic adds complexity
- **Risks**: Urgent items may be delayed; batch size too large causes cognitive overload

**Sources**: [paper:13][paper:14]

---

### Pattern 4: Risk-Tiered Auto-Approval Gateway

**Name**: Risk-Tiered Auto-Approval Gateway

**Description**: Automatically approve low-risk actions while escalating medium and high-risk actions based on explicit risk classification.

**When to Use**:
- Environments with clear risk categorization
- High-volume operations where most actions are low-risk
- Compliance requirements for audit trail of approvals

**Implementation Elements**:
- Risk classification taxonomy (safe, moderate, high, critical)
- Explicit rules for each tier (auto-approve, auto-escalate, require approval)
- Override mechanisms for edge cases
- Audit logging for all decisions

**Tradeoffs**:
- **Benefits**: Reduces approval burden significantly; maintains oversight for consequential actions
- **Costs**: Requires upfront risk classification; ongoing maintenance of rules
- **Risks**: Misclassification leads to inappropriate auto-approval or unnecessary escalation

**Sources**: [paper:26][paper:27][paper:28][web:5]

---

### Pattern 5: Structured Follow-up Questions

**Name**: Structured Follow-up Questions

**Description**: When clarification is needed, present a clear question with 2-4 suggested answers rather than open-ended prompts.

**When to Use**:
- Agent needs specific information to proceed
- Multiple valid approaches exist
- User may not know what information is relevant

**Implementation Elements**:
- Clear, specific question text
- 2-4 complete, actionable suggested answers
- Option for custom response if suggestions don't fit
- Context explaining why clarification is needed

**Tradeoffs**:
- **Benefits**: Reduces user cognitive load; guides toward relevant information; faster resolution
- **Costs**: May limit user expression; requires good suggestion generation
- **Risks**: Suggestions may bias user response; may not cover all valid options

**Sources**: [web:2][paper:29]

---

### Pattern 6: Multi-Channel Notification Routing

**Name**: Multi-Channel Notification Routing

**Description**: Route notifications through appropriate channels based on urgency, time, and recipient preferences using a unified notification framework.

**When to Use**:
- Distributed teams across time zones
- Varying urgency levels for different events
- Need for reliable delivery confirmation

**Implementation Elements**:
- Unified notification API (e.g., Apprise)
- Channel selection rules based on urgency/priority
- Recipient preference management
- Delivery confirmation and retry logic

**Tradeoffs**:
- **Benefits**: Ensures reachability; respects recipient preferences; scalable
- **Costs**: Configuration complexity; multiple service integrations
- **Risks**: Notification fatigue if not properly managed; delivery failures

**Sources**: [web:1][paper:31]

---

### Pattern 7: Autonomy Level Declaration

**Name**: Autonomy Level Declaration

**Description**: Explicitly declare and enforce the autonomy level for each agent or task, defining the human role (operator, collaborator, consultant, approver, observer).

**When to Use**:
- Multiple agents with different autonomy requirements
- Tasks with varying risk profiles
- Need for clear accountability and expectations

**Implementation Elements**:
- Autonomy level taxonomy (5 levels)
- Per-agent or per-task level assignment
- Enforcement mechanisms for level boundaries
- Level transition protocols

**Tradeoffs**:
- **Benefits**: Clear expectations; appropriate oversight level; accountability
- **Costs**: Requires upfront decision; may need dynamic adjustment
- **Risks**: Level mismatch leads to over/under supervision

**Sources**: [paper:1][paper:2]

---

### Pattern 8: Checkpoint-Based Execution

**Name**: Checkpoint-Based Execution

**Description**: Insert approval checkpoints at natural boundaries in agent workflows (after planning, before execution, after critical steps).

**When to Use**:
- Multi-step workflows with clear phases
- Actions with significant consequences
- Need for human review at specific points

**Implementation Elements**:
- Checkpoint definition at workflow design time
- State serialization at checkpoints
- Resume capability after approval
- Rollback option if checkpoint rejected

**Tradeoffs**:
- **Benefits**: Natural review points; prevents runaway execution; enables course correction
- **Costs**: Execution latency; state management complexity
- **Risks**: Checkpoints at wrong points miss critical decisions

**Sources**: [paper:2][web:4]

---

### Pattern 9: Explainable Plan Visualization

**Name**: Explainable Plan Visualization

**Description**: Present agent plans with visual explanations showing why actions were chosen, dependencies between actions, and alternatives considered.

**When to Use**:
- Complex multi-step plans
- High-stakes decisions requiring human understanding
- Building trust in agent capabilities

**Implementation Elements**:
- Visual plan representation (graph, timeline, tree)
- Dependency arrows between actions
- Alternative action display with selection rationale
- Provenance tracking for decisions

**Tradeoffs**:
- **Benefits**: Builds trust; enables informed approval; supports error detection
- **Costs**: Visualization complexity; may overwhelm with detail
- **Risks**: "Explanation theater" without genuine insight

**Sources**: [paper:16][paper:17][paper:18][paper:20]

---

### Pattern 10: Learning from Approval Patterns

**Name**: Learning from Approval Patterns

**Description**: Use human approval/rejection decisions to improve agent behavior and auto-approval gateway accuracy over time.

**When to Use**:
- High-volume operations with repeated similar decisions
- Environment where agent behavior should adapt
- Sufficient approval data for learning

**Implementation Elements**:
- Approval/rejection logging with context
- Pattern analysis for common decisions
- Gateway rule updates based on patterns
- Feedback loop to agent planning

**Tradeoffs**:
- **Benefits**: Improves over time; reduces human burden; adapts to changing context
- **Costs**: Requires data infrastructure; potential for learning wrong patterns
- **Risks**: Feedback loops may amplify biases; cold start problem

**Sources**: [paper:25][paper:27]

---

## Identified Anti-Patterns

### Anti-Pattern 1: Approval Fatigue Spiral

**Name**: Approval Fatigue Spiral

**Description**: Excessive approval requests lead to human fatigue, causing rubber-stamp approvals that undermine the entire HITL system.

**Failure Mode**:
1. Agent escalates too many low-importance decisions
2. Human becomes fatigued from constant interruptions
3. Human starts approving without careful review
4. Agent learns that escalation is acceptable (no negative feedback)
5. Quality of oversight degrades progressively

**Causes**:
- Poor confidence calibration (over-escalation)
- Missing risk tiering (treating all actions equally)
- No batching mechanism (constant interruptions)
- Inadequate context summarization

**Prevention**:
- Implement confidence-calibrated escalation
- Use risk-tiered auto-approval gateways
- Batch related approvals
- Monitor approval rates and human response times

**Sources**: [paper:12][paper:13][paper:14]

---

### Anti-Pattern 2: Context Poisoning from Human Input

**Name**: Context Poisoning from Human Input

**Description**: Human inputs during HITL interactions introduce errors, biases, or irrelevant information that degrades subsequent agent behavior.

**Failure Mode**:
1. Human provides incorrect or misleading input during approval
2. Agent incorporates input into context/memory
3. Subsequent decisions are influenced by poisoned context
4. Errors propagate through workflow

**Causes**:
- No validation of human input
- Over-trust in human correctness
- Context management that preserves all inputs equally
- Lack of input provenance tracking

**Prevention**:
- Validate human inputs where possible
- Track input provenance and confidence
- Implement context pruning mechanisms
- Allow human input to be marked as tentative

**Sources**: [web:8] (Roocode Context Poisoning)

---

### Anti-Pattern 3: Rubber-Stamp Automation Theatre

**Name**: Rubber-Stamp Automation Theatre

**Description**: HITL system exists for compliance or appearance but human review is perfunctory and provides no real oversight.

**Failure Mode**:
1. Approval required for compliance reasons
2. Human has insufficient time or context to review properly
3. Approval becomes a formality
4. Errors that should be caught are missed
5. System provides false sense of security

**Causes**:
- Compliance-driven rather than safety-driven design
- Insufficient time allocated for review
- Poor explanation quality
- High approval volume without support

**Prevention**:
- Design for genuine oversight, not just compliance
- Provide adequate context and time for review
- Measure approval quality, not just completion
- Implement spot-check audits of approved decisions

**Sources**: [paper:12][paper:19]

---

### Anti-Pattern 4: Escalation Threshold Drift

**Name**: Escalation Threshold Drift

**Description**: Escalation thresholds become misaligned with actual risk over time due to changes in agent capability, task distribution, or environment.

**Failure Mode**:
1. Initial thresholds calibrated for specific conditions
2. Agent capability improves (or degrades)
3. Task distribution shifts
4. Thresholds no longer appropriate
5. Over/under escalation results

**Causes**:
- No ongoing calibration monitoring
- Static thresholds in dynamic environment
- Missing feedback loop from outcomes to thresholds
- Insufficient metrics for threshold health

**Prevention**:
- Monitor escalation outcomes continuously
- Implement automatic threshold adjustment
- Track calibration metrics over time
- Periodic threshold review and tuning

**Sources**: [paper:9][paper:12][paper:23]

---

### Anti-Pattern 5: Explanation Overload

**Name**: Explanation Overload

**Description**: Providing too much explanation detail overwhelms users and reduces decision quality rather than improving it.

**Failure Mode**:
1. System provides comprehensive explanations
2. Users are overwhelmed by information volume
3. Users skim or ignore explanations
4. Decision quality degrades
5. Time to decision increases

**Causes**:
- Belief that more explanation is always better
- No progressive disclosure mechanism
- Missing explanation relevance filtering
- One-size-fits-all explanation design

**Prevention**:
- Implement progressive disclosure
- Filter explanations to relevant information
- Tailor explanation depth to user role
- Measure decision quality, not explanation completeness

**Sources**: [paper:13][paper:19]

---

### Anti-Pattern 6: Single Point of Approval Bottleneck

**Name**: Single Point of Approval Bottleneck

**Description**: All approvals flow through a single person, creating a bottleneck that delays execution and concentrates fatigue.

**Failure Mode**:
1. All approvals require specific individual
2. Individual becomes unavailable (vacation, overload)
3. Workflows stall waiting for approval
4. Pressure to approve quickly increases
5. Approval quality degrades

**Causes**:
- Simple single-approver design
- No delegation mechanism
- Missing role-based approval routing
- Insufficient backup approvers

**Prevention**:
- Implement role-based approval routing
- Enable delegation with audit trail
- Define backup approvers
- Monitor approval latency and distribute load

**Sources**: [paper:6][paper:31]

---

### Anti-Pattern 7: Trust Miscalibration

**Name**: Trust Miscalibration

**Description**: Humans either over-trust agent recommendations (automation bias) or under-trust them (excessive skepticism), leading to poor decision outcomes.

**Failure Mode**:
- **Over-trust**: Humans approve agent recommendations without adequate scrutiny, missing errors
- **Under-trust**: Humans reject correct recommendations, wasting effort and reducing efficiency

**Causes**:
- Poor understanding of agent capabilities and limitations
- No feedback on trust calibration
- Inconsistent agent performance
- Missing confidence indicators

**Prevention**:
- Provide clear confidence indicators
- Track and report calibration metrics
- Educate users on agent capabilities
- Implement trust calibration exercises

**Sources**: [paper:12][paper:32]

---

### Anti-Pattern 8: Notification Spam

**Name**: Notification Spam

**Description**: Excessive or poorly-targeted notifications cause users to ignore or disable the notification system entirely.

**Failure Mode**:
1. System sends notifications for all events
2. Users receive too many notifications
3. Users start ignoring notifications
4. Critical notifications are missed
5. Users disable notifications entirely

**Causes**:
- No notification prioritization
- Missing urgency classification
- No aggregation or batching
- All events treated equally

**Prevention**:
- Implement priority levels for notifications
- Aggregate related notifications
- Route based on urgency and channel
- Monitor notification response rates

**Sources**: [web:1][paper:31]

---

## Use Cases Grounded in Research

### Use Case 1: Autonomous Code Refactoring

**Scenario**: AI agent performs large-scale code refactoring across a codebase.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (safe: formatting; moderate: local refactoring; high: cross-file changes)
- Checkpoint-Based Execution (after planning, before execution)
- Progressive Disclosure of Reasoning (show summary of changes, expand for diff)

**Avoided Anti-Patterns**:
- Approval Fatigue Spiral (use auto-approval for safe changes)
- Rubber-Stamp Automation Theatre (provide meaningful context)

**Sources**: [paper:1][paper:26][paper:27]

---

### Use Case 2: Infrastructure Provisioning

**Scenario**: AI agent provisions cloud infrastructure based on high-level requirements.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate uncertain configurations)
- Multi-Channel Notification Routing (urgent issues via PagerDuty, info via Slack)
- Structured Follow-up Questions (clarify ambiguous requirements)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as infrastructure evolves)
- Single Point of Approval Bottleneck (route to appropriate team)

**Sources**: [paper:9][paper:31][web:1]

---

### Use Case 3: Security Vulnerability Remediation

**Scenario**: AI agent identifies and fixes security vulnerabilities.

**Recommended Patterns**:
- Autonomy Level Declaration (consultant mode for sensitive systems)
- Explainable Plan Visualization (show vulnerability and fix rationale)
- Learning from Approval Patterns (improve fix suggestions over time)

**Avoided Anti-Patterns**:
- Context Poisoning from Human Input (validate security guidance)
- Trust Miscalibration (clear confidence on fix correctness)

**Sources**: [paper:16][paper:28][paper:25]

---

### Use Case 4: Database Schema Migration

**Scenario**: AI agent designs and executes database schema migrations.

**Recommended Patterns**:
- Risk-Tiered Auto-Approval Gateway (critical tier for production databases)
- Intelligent Approval Batching (group related schema changes)
- Checkpoint-Based Execution (after design, before execution, after backup)

**Avoided Anti-Patterns**:
- Rubber-Stamp Automation Theatre (ensure DBA has time for review)
- Approval Fatigue Spiral (batch non-critical changes)

**Sources**: [paper:6][paper:26][paper:27]

---

### Use Case 5: Multi-Agent Feature Development

**Scenario**: Multiple AI agents collaborate on feature development with human oversight.

**Recommended Patterns**:
- Autonomy Level Declaration (different levels per agent)
- Structured Follow-up Questions (clarify feature requirements)
- Multi-Channel Notification Routing (coordinate across team)

**Avoided Anti-Patterns**:
- Single Point of Approval Bottleneck (distribute across team)
- Notification Spam (aggregate agent notifications)

**Sources**: [paper:1][paper:2][paper:31]

---

### Use Case 6: Continuous Integration Pipeline Management

**Scenario**: AI agent manages CI/CD pipeline configuration and optimization.

**Recommended Patterns**:
- Confidence-Calibrated Escalation (escalate pipeline changes)
- Learning from Approval Patterns (improve optimization suggestions)
- Progressive Disclosure of Reasoning (show performance impact summary)

**Avoided Anti-Patterns**:
- Escalation Threshold Drift (monitor as codebase evolves)
- Explanation Overload (focus on key metrics)

**Sources**: [paper:9][paper:25][paper:27]

---

## Pattern Selection Guide

| Factor | Lower Autonomy | Higher Autonomy |
|--------|---------------|-----------------|
| **Risk Level** | High risk → Operator/Consultant | Low risk → Approver/Observer |
| **Task Frequency** | Low frequency → Single approver | High frequency → Batching + auto-approval |
| **Decision Complexity** | High complexity → Collaborator + explanations | Low complexity → Auto-approval |
| **Team Distribution** | Co-located → Direct collaboration | Distributed → Notification routing |
| **Regulatory Requirements** | Strict → Role-based approval chain | Flexible → Risk-tiered gateway |
| **Agent Maturity** | Early → Operator/Consultant | Mature → Approver/Observer |
| **User Expertise** | Novice → Structured suggestions | Expert → Open flexibility |
