# SDLC Phase Knowledge Mapping

This document provides a structured mapping of knowledge atoms to each phase of the Software Development Life Cycle (SDLC). It helps agents identify relevant techniques, constraints, tools, and failure modes based on their current lifecycle phase.

## P1: Discovery & Onboarding
**What the Agent is Doing**: Gaining initial understanding of the project, repository structure, and requirements. Establishing context for subsequent development phases.

### Knowledge Atoms
- KA-009 (Budget-Aware Retrieval)
- KA-010 (Hierarchical Summarization)
- KA-011 (U-Shaped Context Placement)
- KA-012 (Task-Conditioned Context)
- KA-013 (Context Caching)
- KA-014 (Semantic Chunking)
- KA-015 (Context Provenance Tracking)
- KA-016 (Sliding Window with Overlap)

### Techniques to Use (Ranked by Step)
1. **Implement task-conditioned context selection** - [KA-012]
2. **Apply semantic chunking to repository content** - [KA-014]
3. **Use hierarchical summarization for project overview** - [KA-010]
4. **Establish context caching for frequently accessed information** - [KA-013]
5. **Implement context provenance tracking** - [KA-015]

### Constraints in Effect
- KA-035 (Context Stuffing - Anti-Pattern)
- KA-036 (Naive Truncation - Anti-Pattern)

### Failure Modes to Watch For
- KA-035 (Context Stuffing)
- KA-036 (Naive Truncation)

### Transitions
- **Exit to**: P2: Planning & Design
- **Exit Condition**: Project structure and requirements are understood, context is established
- **Fallback to**: (none)
- **Fallback Condition**: (none)

---

## P2: Planning & Design
**What the Agent is Doing**: Creating technical architecture, designing system components, and planning implementation strategies. Defining interfaces, data flows, and communication protocols.

### Knowledge Atoms
- KA-001 (System-Theoretic Agent Decomposition)
- KA-002 (Hierarchical Multi-Agent Orchestration)
- KA-003 (TEA Protocol Pattern)
- KA-004 (Layered Voting Architecture)
- KA-005 (Software Company Simulation)
- KA-006 (Explicit Mode Switching)
- KA-007 (Human-in-the-Loop Checkpoints)
- KA-009 (Budget-Aware Retrieval)
- KA-010 (Hierarchical Summarization)
- KA-011 (U-Shaped Context Placement)
- KA-012 (Task-Conditioned Context)
- KA-013 (Context Caching)
- KA-014 (Semantic Chunking)
- KA-015 (Context Provenance Tracking)
- KA-016 (Sliding Window with Overlap)
- KA-029 (System-Theoretic Agent Decomposition Tradeoff)
- KA-030 (Hierarchical Multi-Agent Orchestration Tradeoff)
- KA-031 (Layered Voting Architecture Tradeoff)
- KA-032 (Explicit Mode Switching Tradeoff)
- KA-033 (Human-in-the-Loop Checkpoints Tradeoff)
- KA-035 (Context Stuffing - Anti-Pattern)
- KA-036 (Naive Truncation - Anti-Pattern)

### Techniques to Use (Ranked by Step)
1. **Decompose agent system architecture** - [KA-001]
2. **Design hierarchical orchestration structure** - [KA-002]
3. **Define TEA protocol interfaces** - [KA-003]
4. **Implement layered voting architecture** - [KA-004]
5. **Define role-based agent responsibilities** - [KA-005]
6. **Configure explicit mode switching** - [KA-006]
7. **Plan human-in-the-loop checkpoints** - [KA-007]
8. **Design context management strategy** - [KA-009, KA-010, KA-011, KA-012, KA-013, KA-014, KA-015, KA-016]
9. **Evaluate tradeoffs of selected patterns** - [KA-029, KA-030, KA-031, KA-032, KA-033]
10. **Avoid context management anti-patterns** - [KA-035, KA-036]

### Constraints in Effect
- KA-029 (System-Theoretic Agent Decomposition Tradeoff)
- KA-030 (Hierarchical Multi-Agent Orchestration Tradeoff)
- KA-031 (Layered Voting Architecture Tradeoff)
- KA-032 (Explicit Mode Switching Tradeoff)
- KA-033 (Human-in-the-Loop Checkpoints Tradeoff)

### Failure Modes to Watch For
- KA-035 (Context Stuffing)
- KA-036 (Naive Truncation)

### Transitions
- **Exit to**: P3: Implementation
- **Exit Condition**: Architecture is finalized, design documents are complete
- **Fallback to**: P1: Discovery & Onboarding
- **Fallback Condition**: Project context or requirements change significantly

---

## P3: Implementation
**What the Agent is Doing**: Building system components based on the design. Writing code, integrating modules, and implementing functionality according to specifications.

### Knowledge Atoms
- KA-001 (System-Theoretic Agent Decomposition)
- KA-002 (Hierarchical Multi-Agent Orchestration)
- KA-003 (TEA Protocol Pattern)
- KA-004 (Layered Voting Architecture)
- KA-005 (Software Company Simulation)
- KA-006 (Explicit Mode Switching)
- KA-007 (Human-in-the-Loop Checkpoints)
- KA-008 (Zero-Shot Recovery Chaining)
- KA-009 (Budget-Aware Retrieval)
- KA-010 (Hierarchical Summarization)
- KA-011 (U-Shaped Context Placement)
- KA-012 (Task-Conditioned Context)
- KA-013 (Context Caching)
- KA-014 (Semantic Chunking)
- KA-015 (Context Provenance Tracking)
- KA-016 (Sliding Window with Overlap)
- KA-029 (System-Theoretic Agent Decomposition Tradeoff)
- KA-030 (Hierarchical Multi-Agent Orchestration Tradeoff)
- KA-031 (Layered Voting Architecture Tradeoff)
- KA-032 (Explicit Mode Switching Tradeoff)
- KA-033 (Human-in-the-Loop Checkpoints Tradeoff)
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)
- KA-035 (Context Stuffing - Anti-Pattern)
- KA-036 (Naive Truncation - Anti-Pattern)

### Techniques to Use (Ranked by Step)
1. **Implement system-theoretic agent decomposition** - [KA-001]
2. **Build hierarchical multi-agent orchestration** - [KA-002]
3. **Implement TEA protocol interfaces** - [KA-003]
4. **Build layered voting architecture** - [KA-004]
5. **Implement role-based agent system** - [KA-005]
6. **Implement explicit mode switching** - [KA-006]
7. **Add human-in-the-loop checkpoints** - [KA-007]
8. **Implement zero-shot recovery chaining** - [KA-008]
9. **Implement context management system** - [KA-009, KA-010, KA-011, KA-012, KA-013, KA-014, KA-015, KA-016]
10. **Monitor implementation tradeoffs** - [KA-029, KA-030, KA-031, KA-032, KA-033, KA-034]
11. **Avoid context management anti-patterns** - [KA-035, KA-036]

### Constraints in Effect
- KA-029 (System-Theoretic Agent Decomposition Tradeoff)
- KA-030 (Hierarchical Multi-Agent Orchestration Tradeoff)
- KA-031 (Layered Voting Architecture Tradeoff)
- KA-032 (Explicit Mode Switching Tradeoff)
- KA-033 (Human-in-the-Loop Checkpoints Tradeoff)
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)

### Failure Modes to Watch For
- KA-035 (Context Stuffing)
- KA-036 (Naive Truncation)

### Transitions
- **Exit to**: P4: Testing & Verification
- **Exit Condition**: Implementation is complete, all components are integrated
- **Fallback to**: P2: Planning & Design
- **Fallback Condition**: Design flaws or architectural issues are discovered

---

## P4: Testing & Verification
**What the Agent is Doing**: Executing tests to verify functionality, performance, and reliability. Identifying and reporting defects. Ensuring system meets quality standards.

### Knowledge Atoms
- KA-007 (Human-in-the-Loop Checkpoints)
- KA-008 (Zero-Shot Recovery Chaining)
- KA-017 (Test Pyramid Pattern)
- KA-018 (Test-First Pattern - TDD)
- KA-019 (Property-Based Testing Pattern)
- KA-020 (Contract Testing Pattern)
- KA-021 (Mutation Testing Pattern)
- KA-022 (Test Fixture Pattern)
- KA-023 (Mock Object Pattern)
- KA-024 (Parameterized Test Pattern)
- KA-025 (Given-When-Then Pattern - BDD)
- KA-026 (Test Double Pattern)
- KA-027 (Happy Path / Sad Path Pattern)
- KA-028 (Multi-Stage Validation Pattern)
- KA-033 (Human-in-the-Loop Checkpoints Tradeoff)
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)

### Techniques to Use (Ranked by Step)
1. **Structure tests using test pyramid pattern** - [KA-017]
2. **Implement test-first development (TDD)** - [KA-018]
3. **Add property-based testing** - [KA-019]
4. **Implement contract testing** - [KA-020]
5. **Add mutation testing** - [KA-021]
6. **Implement test fixtures** - [KA-022]
7. **Use mock object patterns** - [KA-023]
8. **Implement parameterized tests** - [KA-024]
9. **Use BDD given-when-then pattern** - [KA-025]
10. **Implement test double patterns** - [KA-026]
11. **Test happy and sad paths** - [KA-027]
12. **Implement multi-stage validation** - [KA-028]
13. **Execute human-in-the-loop validation** - [KA-007]
14. **Test recovery mechanisms** - [KA-008]
15. **Monitor testing tradeoffs** - [KA-033, KA-034]

### Constraints in Effect
- KA-033 (Human-in-the-Loop Checkpoints Tradeoff)
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)

### Failure Modes to Watch For
- KA-035 (Context Stuffing)
- KA-036 (Naive Truncation)

### Transitions
- **Exit to**: P5: Code Review
- **Exit Condition**: All tests pass, quality standards are met
- **Fallback to**: P3: Implementation
- **Fallback Condition**: Critical defects are discovered

---

## P5: Code Review
**What the Agent is Doing**: Reviewing code changes for quality, security, and adherence to coding standards. Identifying issues and suggesting improvements.

### Knowledge Atoms
- KA-007 (Human-in-the-Loop Checkpoints)
- KA-008 (Zero-Shot Recovery Chaining)
- KA-033 (Human-in-the-Loop Checkpoints Tradeoff)
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)

### Techniques to Use (Ranked by Step)
1. **Conduct human-in-the-loop code review** - [KA-007]
2. **Implement automated code quality checks** - []
3. **Review recovery mechanisms** - [KA-008]
4. **Monitor review tradeoffs** - [KA-033, KA-034]

### Constraints in Effect
- KA-033 (Human-in-the-Loop Checkpoints Tradeoff)
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)

### Failure Modes to Watch For
- KA-035 (Context Stuffing)
- KA-036 (Naive Truncation)

### Transitions
- **Exit to**: P6: Debugging & Error Recovery
- **Exit Condition**: Code changes are approved and merged
- **Fallback to**: P3: Implementation
- **Fallback Condition**: Major issues are identified requiring rework

---

## P6: Debugging & Error Recovery
**What the Agent is Doing**: Investigating and fixing bugs. Implementing recovery mechanisms for failures. Optimizing system stability.

### Knowledge Atoms
- KA-008 (Zero-Shot Recovery Chaining)
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)

### Techniques to Use (Ranked by Step)
1. **Implement zero-shot recovery chaining** - [KA-008]
2. **Monitor recovery tradeoffs** - [KA-034]

### Constraints in Effect
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)

### Failure Modes to Watch For
- KA-035 (Context Stuffing)
- KA-036 (Naive Truncation)

### Transitions
- **Exit to**: P7: Deployment & Release
- **Exit Condition**: All bugs are fixed, system is stable
- **Fallback to**: P4: Testing & Verification
- **Fallback Condition**: Testing indicates unresolved issues

---

## P7: Deployment & Release
**What the Agent is Doing**: Deploying the system to production. Managing release processes and ensuring smooth deployment.

### Knowledge Atoms
- KA-028 (Multi-Stage Validation Pattern)

### Techniques to Use (Ranked by Step)
1. **Execute multi-stage deployment** - [KA-028]

### Constraints in Effect
- (none)

### Failure Modes to Watch For
- KA-035 (Context Stuffing)
- KA-036 (Naive Truncation)

### Transitions
- **Exit to**: P8: Maintenance & Monitoring
- **Exit Condition**: Deployment is successful, system is live
- **Fallback to**: P6: Debugging & Error Recovery
- **Fallback Condition**: Production issues are discovered

---

## P8: Maintenance & Monitoring
**What the Agent is Doing**: Monitoring system performance, addressing ongoing issues, and maintaining system functionality. Implementing updates and improvements.

### Knowledge Atoms
- KA-008 (Zero-Shot Recovery Chaining)
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)

### Techniques to Use (Ranked by Step)
1. **Implement recovery mechanisms** - [KA-008]
2. **Monitor recovery tradeoffs** - [KA-034]

### Constraints in Effect
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)

### Failure Modes to Watch For
- KA-035 (Context Stuffing)
- KA-036 (Naive Truncation)

### Transitions
- **Exit to**: (none)
- **Exit Condition**: (none)
- **Fallback to**: P6: Debugging & Error Recovery
- **Fallback Condition**: Critical issues requiring debugging are identified

---

## Summary

This SDLC phase knowledge mapping provides a comprehensive guide for agents operating in different lifecycle stages. Key insights include:

1. **Context Management Focus**: Phases P1-P3 emphasize context management techniques to establish and maintain effective working environments
2. **Recovery Mechanisms**: Zero-shot recovery chaining (KA-008) is critical across implementation, testing, debugging, and maintenance phases
3. **Human-in-the-Loop Integration**: Human checkpoints (KA-007) play a significant role in planning, implementation, testing, and code review
4. **Tradeoff Awareness**: Each phase includes relevant tradeoff atoms to help agents make informed decisions about architectural choices
5. **Anti-Pattern Avoidance**: Context stuffing (KA-035) and naive truncation (KA-036) are highlighted as failure modes to avoid across all phases

The mapping enables agents to dynamically adapt their behavior based on their current phase, ensuring they apply the most relevant techniques and avoid common pitfalls.

This document provides a structured mapping of knowledge atoms to each phase of the Software Development Life Cycle (SDLC). It helps agents identify relevant techniques, constraints, tools, and failure modes based on their current lifecycle phase.

## P1: Discovery & Onboarding
**What the Agent is Doing**: Gaining initial understanding of the project, repository structure, and requirements. Establishing context for subsequent development phases.

### Knowledge Atoms
- KA-009 (Budget-Aware Retrieval)
- KA-010 (Hierarchical Summarization)
- KA-011 (U-Shaped Context Placement)
- KA-012 (Task-Conditioned Context)
- KA-013 (Context Caching)
- KA-014 (Semantic Chunking)
- KA-015 (Context Provenance Tracking)
- KA-016 (Sliding Window with Overlap)

### Techniques to Use (Ranked by Step)
1. **Implement task-conditioned context selection** - [KA-012]
2. **Apply semantic chunking to repository content** - [KA-014]
3. **Use hierarchical summarization for project overview** - [KA-010]
4. **Establish context caching for frequently accessed information** - [KA-013]
5. **Implement context provenance tracking** - [KA-015]

### Constraints in Effect
- KA-035 (Context Stuffing - Anti-Pattern)
- KA-036 (Naive Truncation - Anti-Pattern)

### Failure Modes to Watch For
- KA-035 (Context Stuffing)
- KA-036 (Naive Truncation)

### Transitions
- **Exit to**: P2: Planning & Design
- **Exit Condition**: Project structure and requirements are understood, context is established
- **Fallback to**: (none)
- **Fallback Condition**: (none)

---

## P2: Planning & Design
**What the Agent is Doing**: Creating technical architecture, designing system components, and planning implementation strategies. Defining interfaces, data flows, and communication protocols.

### Knowledge Atoms
- KA-001 (System-Theoretic Agent Decomposition)
- KA-002 (Hierarchical Multi-Agent Orchestration)
- KA-003 (TEA Protocol Pattern)
- KA-004 (Layered Voting Architecture)
- KA-005 (Software Company Simulation)
- KA-006 (Explicit Mode Switching)
- KA-007 (Human-in-the-Loop Checkpoints)
- KA-009 (Budget-Aware Retrieval)
- KA-010 (Hierarchical Summarization)
- KA-011 (U-Shaped Context Placement)
- KA-012 (Task-Conditioned Context)
- KA-013 (Context Caching)
- KA-014 (Semantic Chunking)
- KA-015 (Context Provenance Tracking)
- KA-016 (Sliding Window with Overlap)
- KA-029 (System-Theoretic Agent Decomposition Tradeoff)
- KA-030 (Hierarchical Multi-Agent Orchestration Tradeoff)
- KA-031 (Layered Voting Architecture Tradeoff)
- KA-032 (Explicit Mode Switching Tradeoff)
- KA-033 (Human-in-the-Loop Checkpoints Tradeoff)
- KA-035 (Context Stuffing - Anti-Pattern)
- KA-036 (Naive Truncation - Anti-Pattern)

### Techniques to Use (Ranked by Step)
1. **Decompose agent system architecture** - [KA-001]
2. **Design hierarchical orchestration structure** - [KA-002]
3. **Define TEA protocol interfaces** - [KA-003]
4. **Implement layered voting architecture** - [KA-004]
5. **Define role-based agent responsibilities** - [KA-005]
6. **Configure explicit mode switching** - [KA-006]
7. **Plan human-in-the-loop checkpoints** - [KA-007]
8. **Design context management strategy** - [KA-009, KA-010, KA-011, KA-012, KA-013, KA-014, KA-015, KA-016]
9. **Evaluate tradeoffs of selected patterns** - [KA-029, KA-030, KA-031, KA-032, KA-033]
10. **Avoid context management anti-patterns** - [KA-035, KA-036]

### Constraints in Effect
- KA-029 (System-Theoretic Agent Decomposition Tradeoff)
- KA-030 (Hierarchical Multi-Agent Orchestration Tradeoff)
- KA-031 (Layered Voting Architecture Tradeoff)
- KA-032 (Explicit Mode Switching Tradeoff)
- KA-033 (Human-in-the-Loop Checkpoints Tradeoff)

### Failure Modes to Watch For
- KA-035 (Context Stuffing)
- KA-036 (Naive Truncation)

### Transitions
- **Exit to**: P3: Implementation
- **Exit Condition**: Architecture is finalized, design documents are complete
- **Fallback to**: P1: Discovery & Onboarding
- **Fallback Condition**: Project context or requirements change significantly

---

## P3: Implementation
**What the Agent is Doing**: Building system components based on the design. Writing code, integrating modules, and implementing functionality according to specifications.

### Knowledge Atoms
- KA-001 (System-Theoretic Agent Decomposition)
- KA-002 (Hierarchical Multi-Agent Orchestration)
- KA-003 (TEA Protocol Pattern)
- KA-004 (Layered Voting Architecture)
- KA-005 (Software Company Simulation)
- KA-006 (Explicit Mode Switching)
- KA-007 (Human-in-the-Loop Checkpoints)
- KA-008 (Zero-Shot Recovery Chaining)
- KA-009 (Budget-Aware Retrieval)
- KA-010 (Hierarchical Summarization)
- KA-011 (U-Shaped Context Placement)
- KA-012 (Task-Conditioned Context)
- KA-013 (Context Caching)
- KA-014 (Semantic Chunking)
- KA-015 (Context Provenance Tracking)
- KA-016 (Sliding Window with Overlap)
- KA-029 (System-Theoretic Agent Decomposition Tradeoff)
- KA-030 (Hierarchical Multi-Agent Orchestration Tradeoff)
- KA-031 (Layered Voting Architecture Tradeoff)
- KA-032 (Explicit Mode Switching Tradeoff)
- KA-033 (Human-in-the-Loop Checkpoints Tradeoff)
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)
- KA-035 (Context Stuffing - Anti-Pattern)
- KA-036 (Naive Truncation - Anti-Pattern)

### Techniques to Use (Ranked by Step)
1. **Implement system-theoretic agent decomposition** - [KA-001]
2. **Build hierarchical multi-agent orchestration** - [KA-002]
3. **Implement TEA protocol interfaces** - [KA-003]
4. **Build layered voting architecture** - [KA-004]
5. **Implement role-based agent system** - [KA-005]
6. **Implement explicit mode switching** - [KA-006]
7. **Add human-in-the-loop checkpoints** - [KA-007]
8. **Implement zero-shot recovery chaining** - [KA-008]
9. **Implement context management system** - [KA-009, KA-010, KA-011, KA-012, KA-013, KA-014, KA-015, KA-016]
10. **Monitor implementation tradeoffs** - [KA-029, KA-030, KA-031, KA-032, KA-033, KA-034]
11. **Avoid context management anti-patterns** - [KA-035, KA-036]

### Constraints in Effect
- KA-029 (System-Theoretic Agent Decomposition Tradeoff)
- KA-030 (Hierarchical Multi-Agent Orchestration Tradeoff)
- KA-031 (Layered Voting Architecture Tradeoff)
- KA-032 (Explicit Mode Switching Tradeoff)
- KA-033 (Human-in-the-Loop Checkpoints Tradeoff)
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)

### Failure Modes to Watch For
- KA-035 (Context Stuffing)
- KA-036 (Naive Truncation)

### Transitions
- **Exit to**: P4: Testing & Verification
- **Exit Condition**: Implementation is complete, all components are integrated
- **Fallback to**: P2: Planning & Design
- **Fallback Condition**: Design flaws or architectural issues are discovered

---

## P4: Testing & Verification
**What the Agent is Doing**: Executing tests to verify functionality, performance, and reliability. Identifying and reporting defects. Ensuring system meets quality standards.

### Knowledge Atoms
- KA-007 (Human-in-the-Loop Checkpoints)
- KA-008 (Zero-Shot Recovery Chaining)
- KA-017 (Test Pyramid Pattern)
- KA-018 (Test-First Pattern - TDD)
- KA-019 (Property-Based Testing Pattern)
- KA-020 (Contract Testing Pattern)
- KA-021 (Mutation Testing Pattern)
- KA-022 (Test Fixture Pattern)
- KA-023 (Mock Object Pattern)
- KA-024 (Parameterized Test Pattern)
- KA-025 (Given-When-Then Pattern - BDD)
- KA-026 (Test Double Pattern)
- KA-027 (Happy Path / Sad Path Pattern)
- KA-028 (Multi-Stage Validation Pattern)
- KA-033 (Human-in-the-Loop Checkpoints Tradeoff)
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)

### Techniques to Use (Ranked by Step)
1. **Structure tests using test pyramid pattern** - [KA-017]
2. **Implement test-first development (TDD)** - [KA-018]
3. **Add property-based testing** - [KA-019]
4. **Implement contract testing** - [KA-020]
5. **Add mutation testing** - [KA-021]
6. **Implement test fixtures** - [KA-022]
7. **Use mock object patterns** - [KA-023]
8. **Implement parameterized tests** - [KA-024]
9. **Use BDD given-when-then pattern** - [KA-025]
10. **Implement test double patterns** - [KA-026]
11. **Test happy and sad paths** - [KA-027]
12. **Implement multi-stage validation** - [KA-028]
13. **Execute human-in-the-loop validation** - [KA-007]
14. **Test recovery mechanisms** - [KA-008]
15. **Monitor testing tradeoffs** - [KA-033, KA-034]

### Constraints in Effect
- KA-033 (Human-in-the-Loop Checkpoints Tradeoff)
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)

### Failure Modes to Watch For
- KA-035 (Context Stuffing)
- KA-036 (Naive Truncation)

### Transitions
- **Exit to**: P5: Code Review
- **Exit Condition**: All tests pass, quality standards are met
- **Fallback to**: P3: Implementation
- **Fallback Condition**: Critical defects are discovered

---

## P5: Code Review
**What the Agent is Doing**: Reviewing code changes for quality, security, and adherence to coding standards. Identifying issues and suggesting improvements.

### Knowledge Atoms
- KA-007 (Human-in-the-Loop Checkpoints)
- KA-008 (Zero-Shot Recovery Chaining)
- KA-033 (Human-in-the-Loop Checkpoints Tradeoff)
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)

### Techniques to Use (Ranked by Step)
1. **Conduct human-in-the-loop code review** - [KA-007]
2. **Implement automated code quality checks** - []
3. **Review recovery mechanisms** - [KA-008]
4. **Monitor review tradeoffs** - [KA-033, KA-034]

### Constraints in Effect
- KA-033 (Human-in-the-Loop Checkpoints Tradeoff)
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)

### Failure Modes to Watch For
- KA-035 (Context Stuffing)
- KA-036 (Naive Truncation)

### Transitions
- **Exit to**: P6: Debugging & Error Recovery
- **Exit Condition**: Code changes are approved and merged
- **Fallback to**: P3: Implementation
- **Fallback Condition**: Major issues are identified requiring rework

---

## P6: Debugging & Error Recovery
**What the Agent is Doing**: Investigating and fixing bugs. Implementing recovery mechanisms for failures. Optimizing system stability.

### Knowledge Atoms
- KA-008 (Zero-Shot Recovery Chaining)
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)

### Techniques to Use (Ranked by Step)
1. **Implement zero-shot recovery chaining** - [KA-008]
2. **Monitor recovery tradeoffs** - [KA-034]

### Constraints in Effect
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)

### Failure Modes to Watch For
- KA-035 (Context Stuffing)
- KA-036 (Naive Truncation)

### Transitions
- **Exit to**: P7: Deployment & Release
- **Exit Condition**: All bugs are fixed, system is stable
- **Fallback to**: P4: Testing & Verification
- **Fallback Condition**: Testing indicates unresolved issues

---

## P7: Deployment & Release
**What the Agent is Doing**: Deploying the system to production. Managing release processes and ensuring smooth deployment.

### Knowledge Atoms
- KA-028 (Multi-Stage Validation Pattern)

### Techniques to Use (Ranked by Step)
1. **Execute multi-stage deployment** - [KA-028]

### Constraints in Effect
- (none)

### Failure Modes to Watch For
- KA-035 (Context Stuffing)
- KA-036 (Naive Truncation)

### Transitions
- **Exit to**: P8: Maintenance & Monitoring
- **Exit Condition**: Deployment is successful, system is live
- **Fallback to**: P6: Debugging & Error Recovery
- **Fallback Condition**: Production issues are discovered

---

## P8: Maintenance & Monitoring
**What the Agent is Doing**: Monitoring system performance, addressing ongoing issues, and maintaining system functionality. Implementing updates and improvements.

### Knowledge Atoms
- KA-008 (Zero-Shot Recovery Chaining)
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)

### Techniques to Use (Ranked by Step)
1. **Implement recovery mechanisms** - [KA-008]
2. **Monitor recovery tradeoffs** - [KA-034]

### Constraints in Effect
- KA-034 (Zero-Shot Recovery Chaining Tradeoff)

### Failure Modes to Watch For
- KA-035 (Context Stuffing)
- KA-036 (Naive Truncation)

### Transitions
- **Exit to**: (none)
- **Exit Condition**: (none)
- **Fallback to**: P6: Debugging & Error Recovery
- **Fallback Condition**: Critical issues requiring debugging are identified

---

## Summary

This SDLC phase knowledge mapping provides a comprehensive guide for agents operating in different lifecycle stages. Key insights include:

1. **Context Management Focus**: Phases P1-P3 emphasize context management techniques to establish and maintain effective working environments
2. **Recovery Mechanisms**: Zero-shot recovery chaining (KA-008) is critical across implementation, testing, debugging, and maintenance phases
3. **Human-in-the-Loop Integration**: Human checkpoints (KA-007) play a significant role in planning, implementation, testing, and code review
4. **Tradeoff Awareness**: Each phase includes relevant tradeoff atoms to help agents make informed decisions about architectural choices
5. **Anti-Pattern Avoidance**: Context stuffing (KA-035) and naive truncation (KA-036) are highlighted as failure modes to avoid across all phases

The mapping enables agents to dynamically adapt their behavior based on their current phase, ensuring they apply the most relevant techniques and avoid common pitfalls.

